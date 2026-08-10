from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import re
from typing import Iterable

import yaml


ACCEPTED_SNAPSHOT_MAP_INVALID = "ACCEPTED_SNAPSHOT_MAP_INVALID"
ACCEPTED_SNAPSHOT_PRIMARY_INVALID = "ACCEPTED_SNAPSHOT_PRIMARY_INVALID"
ACCEPTED_SNAPSHOT_COVERAGE_MISMATCH = "ACCEPTED_SNAPSHOT_COVERAGE_MISMATCH"
ACCEPTED_SNAPSHOT_NAME_MISMATCH = "ACCEPTED_SNAPSHOT_NAME_MISMATCH"
ACCEPTED_SNAPSHOT_MISSING = "ACCEPTED_SNAPSHOT_MISSING"
ACCEPTED_SNAPSHOT_CONTENT_MISMATCH = "ACCEPTED_SNAPSHOT_CONTENT_MISMATCH"
ACCEPTED_SNAPSHOT_DECLARATION_MISSING = "ACCEPTED_SNAPSHOT_DECLARATION_MISSING"

OCP_ID = re.compile(r"^OCP-\d{3}$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
DIGEST = re.compile(r"^[0-9a-f]{64}$")
ENTRY_KEYS = {
    "document_id",
    "primary",
    "current_status",
    "reviewed_version",
    "snapshot",
    "sha256",
    "basis",
}
BASES = {"current-accepted", "retained-acceptance-evidence"}


@dataclass(frozen=True)
class AcceptedSnapshotResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AcceptedSnapshotResult:
    return AcceptedSnapshotResult(tuple(dict.fromkeys(errors)))


def _safe_relative_markdown(value: object) -> Path | None:
    if not isinstance(value, str):
        return None
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or path.suffix != ".md":
        return None
    return path


def _frontmatter(path: Path) -> dict[str, str] | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    if not lines or lines[0] != "---":
        return None
    values: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return values
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return None


def _current_accepted_ids(repo_root: Path) -> set[str] | None:
    accepted: set[str] = set()
    for primary in sorted((repo_root / "docs").glob("*/README.md")):
        metadata = _frontmatter(primary)
        if metadata is None:
            return None
        document_id = metadata.get("Document-ID")
        if metadata.get("Status") == "Accepted":
            if not isinstance(document_id, str) or not OCP_ID.fullmatch(document_id):
                return None
            accepted.add(document_id)
    return accepted


def validate_accepted_snapshots(repo_root: Path) -> AcceptedSnapshotResult:
    errors: list[str] = []
    map_path = repo_root / "architecture/accepted-document-snapshot-map.yaml"
    try:
        payload = yaml.safe_load(map_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return _result((ACCEPTED_SNAPSHOT_MAP_INVALID,))

    if (
        not isinstance(payload, dict)
        or set(payload) != {
            "schema_version",
            "rule_owner",
            "current_accepted_status",
            "required_retained_evidence",
            "entries",
        }
        or payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-029"
        or payload.get("current_accepted_status") != "Accepted"
    ):
        return _result((ACCEPTED_SNAPSHOT_MAP_INVALID,))

    retained = payload.get("required_retained_evidence")
    entries = payload.get("entries")
    if (
        not isinstance(retained, list)
        or len(retained) != len(set(retained))
        or any(not isinstance(item, str) or not OCP_ID.fullmatch(item) for item in retained)
        or not isinstance(entries, list)
        or not entries
    ):
        return _result((ACCEPTED_SNAPSHOT_MAP_INVALID,))

    seen_ids: set[str] = set()
    accepted_entries: set[str] = set()
    retained_entries: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != ENTRY_KEYS:
            errors.append(ACCEPTED_SNAPSHOT_MAP_INVALID)
            continue

        document_id = entry.get("document_id")
        primary = _safe_relative_markdown(entry.get("primary"))
        current_status = entry.get("current_status")
        reviewed_version = entry.get("reviewed_version")
        snapshot = _safe_relative_markdown(entry.get("snapshot"))
        expected_digest = entry.get("sha256")
        basis = entry.get("basis")
        if (
            not isinstance(document_id, str)
            or not OCP_ID.fullmatch(document_id)
            or document_id in seen_ids
            or primary is None
            or primary.name != "README.md"
            or not isinstance(current_status, str)
            or current_status not in {"Accepted", "Canonical"}
            or not isinstance(reviewed_version, str)
            or not SEMVER.fullmatch(reviewed_version)
            or snapshot is None
            or not isinstance(expected_digest, str)
            or not DIGEST.fullmatch(expected_digest)
            or basis not in BASES
        ):
            errors.append(ACCEPTED_SNAPSHOT_MAP_INVALID)
            continue
        seen_ids.add(document_id)

        if primary.parent != snapshot.parent:
            errors.append(ACCEPTED_SNAPSHOT_MAP_INVALID)
        expected_name = f"reviewed-contract-v{reviewed_version}.md"
        if snapshot.name != expected_name:
            errors.append(ACCEPTED_SNAPSHOT_NAME_MISMATCH)

        metadata = _frontmatter(repo_root / primary)
        if (
            metadata is None
            or metadata.get("Document-ID") != document_id
            or metadata.get("Status") != current_status
        ):
            errors.append(ACCEPTED_SNAPSHOT_PRIMARY_INVALID)

        if basis == "current-accepted":
            accepted_entries.add(document_id)
            if current_status != "Accepted":
                errors.append(ACCEPTED_SNAPSHOT_PRIMARY_INVALID)
        else:
            retained_entries.add(document_id)
            if current_status != "Canonical":
                errors.append(ACCEPTED_SNAPSHOT_PRIMARY_INVALID)

        snapshot_path = repo_root / snapshot
        try:
            snapshot_bytes = snapshot_path.read_bytes()
        except OSError:
            errors.append(ACCEPTED_SNAPSHOT_MISSING)
            snapshot_bytes = None
        if snapshot_bytes is not None and sha256(snapshot_bytes).hexdigest() != expected_digest:
            errors.append(ACCEPTED_SNAPSHOT_CONTENT_MISMATCH)

        try:
            primary_text = (repo_root / primary).read_text(encoding="utf-8")
        except OSError:
            primary_text = ""
        if f"]({snapshot.name})" not in primary_text:
            errors.append(ACCEPTED_SNAPSHOT_DECLARATION_MISSING)

        sibling_snapshots = {
            path.name for path in (repo_root / primary.parent).glob("reviewed-contract-v*.md")
        }
        if sibling_snapshots != {snapshot.name}:
            errors.append(ACCEPTED_SNAPSHOT_NAME_MISMATCH)

    current_accepted = _current_accepted_ids(repo_root)
    if current_accepted is None:
        errors.append(ACCEPTED_SNAPSHOT_PRIMARY_INVALID)
    elif accepted_entries != current_accepted:
        errors.append(ACCEPTED_SNAPSHOT_COVERAGE_MISMATCH)
    if retained_entries != set(retained):
        errors.append(ACCEPTED_SNAPSHOT_COVERAGE_MISMATCH)

    return _result(errors)
