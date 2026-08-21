from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

import yaml


SUCCESSION_MAPS = (
    Path("architecture/constraint-document-acceptance.yaml"),
    Path("architecture/assignment-document-acceptance.yaml"),
    Path("architecture/assignment-promotion-selection.yaml"),
    Path("architecture/assignment-document-canonicalization.yaml"),
)


def historical_path(repo_root: Path, original: Path, expected_sha256: str) -> Path:
    """Resolve an immutable predecessor declared by the current lifecycle act.

    Completed acts continue to name their original paths.  When a lifecycle act
    legitimately advances one of those paths, this data-owned relation points
    the historical assertion at the exact preserved predecessor bytes.
    """
    for succession_map in SUCCESSION_MAPS:
        try:
            payload: Any = yaml.safe_load((repo_root / succession_map).read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError):
            continue
        rows = payload.get("historical_evidence_successions") if isinstance(payload, dict) else None
        for row in rows or ():
            if not isinstance(row, dict):
                continue
            if row.get("original_path") != original.as_posix() or row.get("sha256") != expected_sha256:
                continue
            successor = Path(str(row.get("preserved_path", "")))
            if successor.is_absolute() or ".." in successor.parts:
                return original
            candidate = repo_root / successor
            try:
                digest = hashlib.sha256(candidate.read_bytes()).hexdigest()
            except OSError:
                return original
            return successor if digest == expected_sha256 else original
    return original
