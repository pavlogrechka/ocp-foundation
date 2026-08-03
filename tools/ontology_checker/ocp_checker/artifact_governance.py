from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
from typing import Any, Iterable

import yaml


ARTIFACT_ID_MISMATCH = "ARTIFACT_ID_MISMATCH"
ARTIFACT_STATUS_INVALID = "ARTIFACT_STATUS_INVALID"
ARTIFACT_METADATA_MISSING = "ARTIFACT_METADATA_MISSING"
ARTIFACT_TAXONOMY_INVALID = "ARTIFACT_TAXONOMY_INVALID"
BACKLOG_ID_DUPLICATE = "BACKLOG_ID_DUPLICATE"
AD_BACKLOG_REFERENCE_MISSING = "AD_BACKLOG_REFERENCE_MISSING"
AD_BACKLOG_STATUS_UNRESOLVED = "AD_BACKLOG_STATUS_UNRESOLVED"
PATTERN_REFERENCE_INVALID = "PATTERN_REFERENCE_INVALID"
PATTERN_REFERENCE_MISSING = "PATTERN_REFERENCE_MISSING"
PATTERN_VERSION_MISMATCH = "PATTERN_VERSION_MISMATCH"
PROCESS_HISTORY_NON_LINEAR = "PROCESS_HISTORY_NON_LINEAR"

AB_ACTIVE_STATUSES = frozenset({"Open", "Proposed", "Discovery", "Under Review"})
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
PATTERN_REF = re.compile(r"^(P-\d{3})@(\d+\.\d+\.\d+)$")
AB_REF = re.compile(r"\bAB-\d{3}\b")


@dataclass(frozen=True)
class GovernanceResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> GovernanceResult:
    return GovernanceResult(tuple(dict.fromkeys(errors)))


def _frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    loaded = yaml.safe_load(text[4:end])
    return loaded if isinstance(loaded, dict) else {}


def _legacy_ad_metadata(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    metadata: dict[str, Any] = {}
    heading = re.search(r"^#\s+(AD-\d{3})\b", text, flags=re.MULTILINE)
    if heading:
        metadata["Decision-ID"] = heading.group(1)
    for key in ("Status", "Applies-To"):
        match = re.search(rf"^-\s+{re.escape(key)}:\s*(.+?)\s*$", text, flags=re.MULTILINE)
        if match:
            metadata[key] = match.group(1)
    return metadata


def _metadata(path: Path, artifact_class: str) -> dict[str, Any]:
    data = _frontmatter(path)
    if not data and artifact_class == "AD":
        data = _legacy_ad_metadata(path)
    return data


def _backlog_rows(path: Path) -> tuple[dict[str, str], bool]:
    rows: dict[str, str] = {}
    duplicate = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4 or not re.fullmatch(r"AB-\d{3}", cells[0]):
            continue
        if cells[0] in rows:
            duplicate = True
        rows[cells[0]] = cells[2]
    return rows, duplicate


def _status_set(class_spec: dict[str, Any], field: str = "lifecycle") -> set[str]:
    values = class_spec.get(field) or []
    return {str(item) for item in values}


def _iter_invocations(value: Any) -> Iterable[str]:
    if value is None:
        return ()
    if isinstance(value, list):
        return (str(item).strip() for item in value if str(item).strip())
    return (item.strip() for item in str(value).split(",") if item.strip())


def validate_artifact_governance(repo_root: Path) -> GovernanceResult:
    errors: list[str] = []
    taxonomy_path = repo_root / "architecture/artifact-taxonomy.yaml"
    backlog_path = repo_root / "backlog/architecture-backlog.md"
    try:
        taxonomy = yaml.safe_load(taxonomy_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return _result((ARTIFACT_TAXONOMY_INVALID,))
    classes = taxonomy.get("artifact_classes") if isinstance(taxonomy, dict) else None
    if not isinstance(classes, dict):
        return _result((ARTIFACT_TAXONOMY_INVALID,))

    if not backlog_path.exists():
        errors.append(ARTIFACT_METADATA_MISSING)
        backlog: dict[str, str] = {}
    else:
        backlog, duplicate = _backlog_rows(backlog_path)
        if duplicate:
            errors.append(BACKLOG_ID_DUPLICATE)
        allowed_ab = _status_set(classes.get("AB") or {})
        for status in backlog.values():
            if status not in allowed_ab:
                errors.append(ARTIFACT_STATUS_INVALID)

    patterns: dict[str, str] = {}
    pattern_allowed = _status_set(classes.get("Pattern") or {})
    for path in sorted((repo_root / "patterns").glob("P-[0-9][0-9][0-9]-*.md")):
        metadata = _metadata(path, "Pattern")
        expected_id = "-".join(path.name.split("-", 2)[:2])
        actual = str(metadata.get("Pattern-ID") or "")
        if actual != expected_id:
            errors.append(ARTIFACT_ID_MISMATCH)
        status = str(metadata.get("Status") or "")
        version = str(metadata.get("Version") or "")
        if not status or not version:
            errors.append(ARTIFACT_METADATA_MISSING)
        elif status not in pattern_allowed:
            errors.append(ARTIFACT_STATUS_INVALID)
        if actual and SEMVER.fullmatch(version):
            patterns[actual] = version

    ocp_spec = classes.get("OCP") or {}
    document_allowed = _status_set(ocp_spec, "document_lifecycle")
    concept_allowed = _status_set(ocp_spec, "concept_lifecycle")
    for path in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _metadata(path, "OCP")
        expected_id = f"OCP-{path.parent.name[:3]}"
        if str(metadata.get("Document-ID") or "") != expected_id:
            errors.append(ARTIFACT_ID_MISMATCH)
        status = str(metadata.get("Status") or "")
        if not status:
            errors.append(ARTIFACT_METADATA_MISSING)
        elif status not in document_allowed:
            errors.append(ARTIFACT_STATUS_INVALID)
        if metadata.get("Defines-Concepts"):
            concept_status = str(metadata.get("Concept-Status") or "")
            if not concept_status:
                errors.append(ARTIFACT_METADATA_MISSING)
            elif concept_status not in concept_allowed:
                errors.append(ARTIFACT_STATUS_INVALID)

    ad_allowed = _status_set(classes.get("AD") or {})
    for path in sorted((repo_root / "architecture/discovery").glob("AD-[0-9][0-9][0-9]-*.md")):
        metadata = _metadata(path, "AD")
        expected_id = path.name[:6]
        if str(metadata.get("Decision-ID") or "") != expected_id:
            errors.append(ARTIFACT_ID_MISMATCH)
        status = str(metadata.get("Status") or "")
        if not status:
            errors.append(ARTIFACT_METADATA_MISSING)
        elif status not in ad_allowed:
            errors.append(ARTIFACT_STATUS_INVALID)
        if status == "Accepted":
            refs = set(AB_REF.findall(str(metadata.get("Applies-To") or "")))
            for ref in refs:
                if ref not in backlog:
                    errors.append(AD_BACKLOG_REFERENCE_MISSING)
                elif backlog[ref] in AB_ACTIVE_STATUSES:
                    errors.append(AD_BACKLOG_STATUS_UNRESOLVED)

    for root in (repo_root / "docs", repo_root / "architecture", repo_root / "patterns"):
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            metadata = _frontmatter(path)
            for invocation in _iter_invocations(metadata.get("Uses-Patterns")):
                match = PATTERN_REF.fullmatch(invocation)
                if not match:
                    errors.append(PATTERN_REFERENCE_INVALID)
                    continue
                pattern_id, version = match.groups()
                if pattern_id not in patterns:
                    errors.append(PATTERN_REFERENCE_MISSING)
                elif patterns[pattern_id] != version:
                    errors.append(PATTERN_VERSION_MISMATCH)

    return _result(errors)


def _parent_count(rev_line: str) -> int:
    fields = rev_line.strip().split()
    return max(0, len(fields) - 1)


def validate_process_audit(repo_root: Path, context: str) -> GovernanceResult:
    if context != "main":
        return _result(())
    try:
        completed = subprocess.run(
            ["git", "rev-list", "--parents", "-n", "1", "HEAD"],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return _result((ARTIFACT_METADATA_MISSING,))
    return _result((PROCESS_HISTORY_NON_LINEAR,)) if _parent_count(completed.stdout) > 1 else _result(())
