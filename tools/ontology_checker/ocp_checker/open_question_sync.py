from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable

import yaml


OPEN_QUESTION_SYNC_MAP_INVALID = "OPEN_QUESTION_SYNC_MAP_INVALID"
OPEN_QUESTION_SYNC_BACKLOG_INVALID = "OPEN_QUESTION_SYNC_BACKLOG_INVALID"
OPEN_QUESTION_RESOLUTION_MISSING = "OPEN_QUESTION_RESOLUTION_MISSING"
OPEN_QUESTION_RESOLUTION_REFERENCE_MISSING = (
    "OPEN_QUESTION_RESOLUTION_REFERENCE_MISSING"
)

ENTRY_ID = re.compile(r"^QSYNC-\d{3}$")
AB_ID = re.compile(r"^AB-\d{3}$")


@dataclass(frozen=True)
class OpenQuestionSyncResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> OpenQuestionSyncResult:
    return OpenQuestionSyncResult(tuple(dict.fromkeys(errors)))


def _backlog_statuses(path: Path) -> dict[str, str] | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None

    statuses: dict[str, str] = {}
    for line in lines:
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and AB_ID.fullmatch(cells[0]):
            statuses[cells[0]] = cells[2]
    return statuses


def validate_open_question_sync(repo_root: Path) -> OpenQuestionSyncResult:
    errors: list[str] = []
    map_path = repo_root / "architecture/open-question-resolution-map.yaml"
    try:
        payload = yaml.safe_load(map_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return _result((OPEN_QUESTION_SYNC_MAP_INVALID,))

    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        return _result((OPEN_QUESTION_SYNC_MAP_INVALID,))
    entries = payload.get("entries")
    if not isinstance(entries, list) or not entries:
        return _result((OPEN_QUESTION_SYNC_MAP_INVALID,))

    statuses = _backlog_statuses(repo_root / "backlog/architecture-backlog.md")
    if statuses is None:
        return _result((OPEN_QUESTION_SYNC_BACKLOG_INVALID,))

    seen_ids: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append(OPEN_QUESTION_SYNC_MAP_INVALID)
            continue

        entry_id = entry.get("id")
        ab_ids = entry.get("ab_ids")
        document = entry.get("document")
        question = entry.get("question")
        resolution_ref = entry.get("resolution_ref")
        if (
            not isinstance(entry_id, str)
            or not ENTRY_ID.fullmatch(entry_id)
            or entry_id in seen_ids
            or not isinstance(ab_ids, list)
            or not ab_ids
            or len(ab_ids) != len(set(ab_ids))
            or any(not isinstance(ab_id, str) or not AB_ID.fullmatch(ab_id) for ab_id in ab_ids)
            or not isinstance(document, str)
            or not isinstance(question, str)
            or not question
            or not isinstance(resolution_ref, str)
            or not resolution_ref
        ):
            errors.append(OPEN_QUESTION_SYNC_MAP_INVALID)
            continue
        seen_ids.add(entry_id)

        relative_path = Path(document)
        if relative_path.is_absolute() or ".." in relative_path.parts or relative_path.suffix != ".md":
            errors.append(OPEN_QUESTION_SYNC_MAP_INVALID)
            continue
        if "reviewed-contract" in relative_path.name:
            errors.append(OPEN_QUESTION_SYNC_MAP_INVALID)
            continue

        if any(statuses.get(ab_id) != "Resolved" for ab_id in ab_ids):
            errors.append(OPEN_QUESTION_SYNC_BACKLOG_INVALID)

        try:
            lines = (repo_root / relative_path).read_text(encoding="utf-8").splitlines()
        except OSError:
            errors.append(OPEN_QUESTION_RESOLUTION_MISSING)
            continue

        marker = f"~~{question}~~"
        matching_lines = [line for line in lines if marker in line]
        if len(matching_lines) != 1:
            errors.append(OPEN_QUESTION_RESOLUTION_MISSING)
            continue
        if resolution_ref not in matching_lines[0]:
            errors.append(OPEN_QUESTION_RESOLUTION_REFERENCE_MISSING)

    return _result(errors)
