from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


FOUNDATION_PROMOTION_GATE_MAP_INVALID = "FOUNDATION_PROMOTION_GATE_MAP_INVALID"
FOUNDATION_PROMOTION_GATE_CANDIDATE_DRIFT = "FOUNDATION_PROMOTION_GATE_CANDIDATE_DRIFT"
FOUNDATION_PROMOTION_GATE_L2_MISMATCH = "FOUNDATION_PROMOTION_GATE_L2_MISMATCH"
FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED = "FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED"

CYCLE_STEPS = (
    "CANDIDATE_BOARD_SELECTION", "DOCUMENT_PROMOTION", "CONCEPT_CANONICALIZATION",
)
STEP_STATES = frozenset({"pending", "completed"})
CANDIDATE_IDS = frozenset({"OCP-005", "OCP-006", "OCP-010"})
ALLOWED_L2_RESULTS = frozenset({"pass", "fail"})
ALLOWED_STATUS_PAIRS = frozenset({
    ("Draft", "Accepted"), ("Canonical", "Accepted"), ("Canonical", "Canonical"),
})
SLOT_IDS = frozenset({"T6", "T7"})

MAP_KEYS = frozenset({"schema_version", "rule_owner", "cycle_protocol", "cycles", "candidates"})
PROTOCOL_KEYS = frozenset({"ordered_steps", "allowed_step_states", "active_cycle_id"})
CYCLE_KEYS = frozenset({"cycle_id", "candidate_id", "slot", "steps", "evidence"})
CANDIDATE_KEYS = frozenset({
    "document_id", "primary", "slot", "expected_document_status", "expected_concept_status",
    "direct_ocp_dependencies", "expected_l2", "l2_blockers",
})


@dataclass(frozen=True)
class FoundationPromotionGateResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> FoundationPromotionGateResult:
    return FoundationPromotionGateResult(tuple(dict.fromkeys(errors)))


def _frontmatter(fpath: Path) -> dict[str, Any] | None:
    try:
        text = fpath.read_text(encoding="utf-8")
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
        if metadata is not None and isinstance(metadata.get("Document-ID"), str):
            result[str(metadata["Document-ID"])] = (primary, metadata)
    return result


def _references(value: Any) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(str(item).strip() for item in value if str(item).strip())
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    return ()


def _completed_prefix(steps: dict[str, Any]) -> bool:
    pending_seen = False
    for step in CYCLE_STEPS:
        state = steps.get(step)
        if state == "pending":
            pending_seen = True
        elif state != "completed" or pending_seen:
            return False
    return True


def validate_foundation_promotion_gate(repo_root: Path) -> FoundationPromotionGateResult:
    errors: list[str] = []
    try:
        payload = yaml.safe_load(
            (repo_root / "architecture/foundation-promotion-gate.yaml").read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        return _result((FOUNDATION_PROMOTION_GATE_MAP_INVALID,))

    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((FOUNDATION_PROMOTION_GATE_MAP_INVALID,))
    protocol = payload.get("cycle_protocol")
    cycles = payload.get("cycles")
    candidates = payload.get("candidates")
    if (
        payload.get("schema_version") != 5
        or payload.get("rule_owner") != "AD-033"
        or not isinstance(protocol, dict)
        or set(protocol) != PROTOCOL_KEYS
        or tuple(protocol.get("ordered_steps") or ()) != CYCLE_STEPS
        or set(protocol.get("allowed_step_states") or ()) != STEP_STATES
        or not isinstance(cycles, list)
        or not cycles
        or not isinstance(candidates, list)
        or not candidates
        or CYCLE_STEPS != (
            "CANDIDATE_BOARD_SELECTION", "DOCUMENT_PROMOTION", "CONCEPT_CANONICALIZATION",
        )
        or STEP_STATES != frozenset({"pending", "completed"})
        or ALLOWED_STATUS_PAIRS != frozenset({
            ("Draft", "Accepted"), ("Canonical", "Accepted"), ("Canonical", "Canonical"),
        })
    ):
        errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)

    ocps = _ocp_index(repo_root)
    statuses = {
        document_id: str(metadata.get("Status") or "")
        for document_id, (_, metadata) in ocps.items()
    }
    candidate_metadata: dict[str, dict[str, Any]] = {}
    candidate_l2: dict[str, str] = {}
    seen_candidates: set[str] = set()
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
            or document_id in seen_candidates
            or not isinstance(primary_value, str)
            or not isinstance(dependencies, list)
            or len(dependencies) != len(set(dependencies))
            or any(not isinstance(item, str) or not item.startswith("OCP-") for item in dependencies)
            or not isinstance(blockers, list)
            or len(blockers) != len(set(blockers))
            or expected_l2 not in ALLOWED_L2_RESULTS
            or candidate.get("slot") not in SLOT_IDS
            or (candidate.get("expected_document_status"), candidate.get("expected_concept_status"))
            not in ALLOWED_STATUS_PAIRS
        ):
            errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)
            continue
        seen_candidates.add(document_id)
        primary = Path(primary_value)
        resolved = ocps.get(document_id)
        if primary.is_absolute() or ".." in primary.parts or resolved is None or resolved[0] != repo_root / primary:
            errors.append(FOUNDATION_PROMOTION_GATE_CANDIDATE_DRIFT)
            continue
        metadata = resolved[1]
        candidate_metadata[document_id] = metadata
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
        candidate_l2[document_id] = actual_l2
        if actual_l2 != expected_l2 or actual_blockers != tuple(blockers):
            errors.append(FOUNDATION_PROMOTION_GATE_L2_MISMATCH)
    if seen_candidates != CANDIDATE_IDS:
        errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)

    active_cycle_id = protocol.get("active_cycle_id") if isinstance(protocol, dict) else None
    seen_cycle_ids: set[str] = set()
    seen_cycle_candidates: set[str] = set()
    incomplete_ids: list[str] = []
    for index, cycle in enumerate(cycles if isinstance(cycles, list) else ()):
        if not isinstance(cycle, dict) or set(cycle) != CYCLE_KEYS:
            errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)
            continue
        cycle_id = cycle.get("cycle_id")
        candidate_id = cycle.get("candidate_id")
        steps = cycle.get("steps")
        evidence = cycle.get("evidence")
        if (
            not isinstance(cycle_id, str) or not cycle_id or cycle_id in seen_cycle_ids
            or not isinstance(candidate_id, str) or candidate_id not in CANDIDATE_IDS
            or candidate_id in seen_cycle_candidates
            or cycle.get("slot") not in SLOT_IDS
            or not isinstance(steps, dict) or tuple(steps) != CYCLE_STEPS
            or set(steps.values()) - STEP_STATES
            or not _completed_prefix(steps)
            or not isinstance(evidence, dict)
            or set(evidence) != {step for step in CYCLE_STEPS if steps.get(step) == "completed"}
            or any(not isinstance(value, str) or not value for value in evidence.values())
        ):
            errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)
            continue
        seen_cycle_ids.add(cycle_id)
        seen_cycle_candidates.add(candidate_id)
        if index < len(cycles) - 1 and any(steps[step] != "completed" for step in CYCLE_STEPS):
            errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)
        if any(steps[step] != "completed" for step in CYCLE_STEPS):
            incomplete_ids.append(cycle_id)

        metadata = candidate_metadata.get(candidate_id, {})
        selected = steps["CANDIDATE_BOARD_SELECTION"] == "completed"
        document_promoted = steps["DOCUMENT_PROMOTION"] == "completed"
        concept_canonical = steps["CONCEPT_CANONICALIZATION"] == "completed"
        if document_promoted and metadata.get("Status") != "Canonical":
            errors.append(FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED)
        if not document_promoted and metadata.get("Status") == "Canonical":
            errors.append(FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED)
        if concept_canonical and metadata.get("Concept-Status") != "Canonical":
            errors.append(FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED)
        if not concept_canonical and metadata.get("Concept-Status") == "Canonical":
            errors.append(FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED)
        if (document_promoted or concept_canonical) and not selected:
            errors.append(FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED)
        if selected and candidate_l2.get(candidate_id) != "pass":
            errors.append(FOUNDATION_PROMOTION_GATE_L2_MISMATCH)

    if len(incomplete_ids) > 1 or active_cycle_id != (incomplete_ids[0] if incomplete_ids else None):
        errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)
    if active_cycle_id is not None and active_cycle_id not in seen_cycle_ids:
        errors.append(FOUNDATION_PROMOTION_GATE_MAP_INVALID)
    for document_id, metadata in candidate_metadata.items():
        cycle = next((item for item in cycles if item.get("candidate_id") == document_id), None)
        if metadata.get("Status") == "Canonical" and (
            cycle is None or cycle.get("steps", {}).get("DOCUMENT_PROMOTION") != "completed"
        ):
            errors.append(FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED)
        if metadata.get("Concept-Status") == "Canonical" and (
            cycle is None or cycle.get("steps", {}).get("CONCEPT_CANONICALIZATION") != "completed"
        ):
            errors.append(FOUNDATION_PROMOTION_GATE_SELECTION_REQUIRED)
    return _result(errors)
