from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


FOUNDATION_PROMOTION_GATE_MAP_INVALID = "FOUNDATION_PROMOTION_GATE_MAP_INVALID"
FOUNDATION_PROMOTION_GATE_CANDIDATE_DRIFT = "FOUNDATION_PROMOTION_GATE_CANDIDATE_DRIFT"
FOUNDATION_PROMOTION_GATE_L2_MISMATCH = "FOUNDATION_PROMOTION_GATE_L2_MISMATCH"
FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED = "FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED"

REQUIRED_COMPLETED_STEPS = frozenset(
    {"T0", "T1", "T2", "T3", "AD-016C", "AD-016D", "T4", "T5", "AD-016Y", "AD-016Z"}
)
REQUIRED_COMPLETED_STEP_ORDER = (
    "T0", "T1", "T2", "T3", "AD-016C", "AD-016D", "T4", "T5", "AD-016Y", "AD-016Z"
)
REQUIRED_NEXT_GATES = frozenset(
    {"Y10D_DISCOVERY", "POST_DISCOVERY_REASSESSMENT", "CANDIDATE_BOARD_SELECTION"}
)
REQUIRED_NEXT_GATE_ORDER = (
    "Y10D_DISCOVERY", "POST_DISCOVERY_REASSESSMENT", "CANDIDATE_BOARD_SELECTION"
)
CANDIDATE_IDS = frozenset({"OCP-005", "OCP-006", "OCP-010"})
ALLOWED_L2_RESULTS = frozenset({"pass", "fail"})

MAP_KEYS = {
    "schema_version",
    "rule_owner",
    "sequence",
    "promotion_selections",
    "candidates",
}
SEQUENCE_KEYS = {
    "completed_steps",
    "selected_next_scope",
    "selected_next_scope_state",
    "required_before_promotion",
}
CANDIDATE_KEYS = {
    "document_id",
    "primary",
    "slot",
    "expected_document_status",
    "expected_concept_status",
    "direct_ocp_dependencies",
    "expected_l2",
    "l2_blockers",
}


@dataclass(frozen=True)
class FoundationPromotionGateResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> FoundationPromotionGateResult:
    return FoundationPromotionGateResult(tuple(dict.fromkeys(errors)))


def _frontmatter(path: Path) -> dict[str, Any] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        loaded = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return loaded if isinstance(loaded, dict) else None


def _ocp_index(repo_root: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    result: dict[str, tuple[Path, dict[str, Any]]] = {}
    for primary in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(primary)
        if metadata is None:
            continue
        document_id = metadata.get("Document-ID")
        if isinstance(document_id, str):
            result[document_id] = (primary, metadata)
    return result


def _references(value: Any) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(str(item).strip() for item in value if str(item).strip())
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    return ()


def validate_foundation_promotion_gate(repo_root: Path) -> FoundationPromotionGateResult:
    errors: list[str] = []
    gate_path = repo_root / "architecture/foundation-promotion-gate.yaml"
    try:
        payload = yaml.safe_load(gate_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return _result((FOUNDATION_PROMOTION_GATE_MAP_INVALID,))

    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((FOUNDATION_PROMOTION_GATE_MAP_INVALID,))
    sequence = payload.get("sequence")
    candidates = payload.get("candidates")
    selections = payload.get("promotion_selections")
    if (
        payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-016AA"
        or not isinstance(sequence, dict)
        or set(sequence) != SEQUENCE_KEYS
        or set(sequence.get("completed_steps") or ()) != REQUIRED_COMPLETED_STEPS
        or tuple(sequence.get("completed_steps") or ()) != REQUIRED_COMPLETED_STEP_ORDER
        or sequence.get("selected_next_scope") != "Y10D"
        or sequence.get("selected_next_scope_state") != "absent"
        or set(sequence.get("required_before_promotion") or ()) != REQUIRED_NEXT_GATES
        or tuple(sequence.get("required_before_promotion") or ()) != REQUIRED_NEXT_GATE_ORDER
        or selections != []
        or not isinstance(candidates, list)
        or not candidates
    ):
        errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)

    ocps = _ocp_index(repo_root)
    statuses = {document_id: str(metadata.get("Status") or "") for document_id, (_, metadata) in ocps.items()}
    seen: set[str] = set()
    for candidate in candidates if isinstance(candidates, list) else ():
        if not isinstance(candidate, dict) or set(candidate) != CANDIDATE_KEYS:
            errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)
            continue
        document_id = candidate.get("document_id")
        primary_value = candidate.get("primary")
        dependencies = candidate.get("direct_ocp_dependencies")
        blockers = candidate.get("l2_blockers")
        expected_l2 = candidate.get("expected_l2")
        if (
            not isinstance(document_id, str)
            or document_id not in CANDIDATE_IDS
            or document_id in seen
            or not isinstance(primary_value, str)
            or not isinstance(dependencies, list)
            or len(dependencies) != len(set(dependencies))
            or any(not isinstance(item, str) or not item.startswith("OCP-") for item in dependencies)
            or not isinstance(blockers, list)
            or len(blockers) != len(set(blockers))
            or expected_l2 not in ALLOWED_L2_RESULTS
            or candidate.get("slot") not in {"T6", "T7"}
            or candidate.get("expected_document_status") != "Draft"
            or candidate.get("expected_concept_status") != "Accepted"
        ):
            errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)
            continue
        seen.add(document_id)

        primary = Path(primary_value)
        resolved = ocps.get(document_id)
        if (
            primary.is_absolute()
            or ".." in primary.parts
            or resolved is None
            or resolved[0] != repo_root / primary
        ):
            errors.append(FOUNDATION_PROMOTION_GATE_CANDIDATE_DRIFT)
            continue
        metadata = resolved[1]
        actual_dependencies = tuple(
            item for item in _references(metadata.get("Depends-On")) if item.startswith("OCP-")
        )
        if (
            metadata.get("Status") != candidate.get("expected_document_status")
            or metadata.get("Concept-Status") != candidate.get("expected_concept_status")
            or actual_dependencies != tuple(dependencies)
        ):
            errors.append(FOUNDATION_PROMOTION_GATE_CANDIDATE_DRIFT)

        actual_blockers = tuple(item for item in dependencies if statuses.get(item) != "Canonical")
        actual_l2 = "pass" if not actual_blockers else "fail"
        if actual_l2 != expected_l2 or actual_blockers != tuple(blockers):
            errors.append(FOUNDATION_PROMOTION_GATE_L2_MISMATCH)
        if metadata.get("Status") == "Canonical" and document_id not in selections:
            errors.append(FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED)

    if seen != CANDIDATE_IDS:
        errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)
    return _result(errors)
