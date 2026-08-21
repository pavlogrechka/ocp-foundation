from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


FOUNDATION_REASSESSMENT_MAP_INVALID = "FOUNDATION_REASSESSMENT_MAP_INVALID"
FOUNDATION_REASSESSMENT_L2_MISMATCH = "FOUNDATION_REASSESSMENT_L2_MISMATCH"
FOUNDATION_REASSESSMENT_EVIDENCE_DRIFT = "FOUNDATION_REASSESSMENT_EVIDENCE_DRIFT"
FOUNDATION_REASSESSMENT_GATE_STATE_INVALID = "FOUNDATION_REASSESSMENT_GATE_STATE_INVALID"
FOUNDATION_REASSESSMENT_SELECTION_FORBIDDEN = "FOUNDATION_REASSESSMENT_SELECTION_FORBIDDEN"

CRITERION_IDS = frozenset({"LIVE_L2", "CURRENT_BLOCKERS", "COST", "UNLOCKS", "LEGALITY_GAP"})
CRITERION_ORDER = ("LIVE_L2", "CURRENT_BLOCKERS", "COST", "UNLOCKS", "LEGALITY_GAP")
CANDIDATE_IDS = frozenset({"OCP-005", "OCP-006", "OCP-010"})
OPTION_IDS = frozenset(
    {"HOLD", "ASSIGNMENT", "EVENT", "JOINT_ASSIGNMENT_CONSTRAINT", "CONSTRAINT_REMEDIATION"}
)
L2_RESULTS = frozenset({"not-applicable", "pass", "fail", "mixed"})
BLOCKER_IDS = frozenset(
    {
        "ASSIGNMENT_COMPATIBILITY_SURFACE_ABSENT",
        "EVENT_OWNER_UNRESOLVED",
        "EVENT_LEGACY_OVERLAP",
        "EVENT_CONSUMER_BINDINGS_UNVERSIONED",
        "JOINT_CURRENT_L2_MIXED",
        "CONSTRAINT_L2_BLOCKED_BY_OCP005",
        "CONSTRAINT_REMEDIATION_SURFACE_ABSENT",
        "BOARD_SELECTION_ABSENT",
    }
)
COST_IDS = frozenset(
    {
        "DELAY_ONLY",
        "BROAD_ASSIGNMENT_DISCOVERY",
        "BOUNDED_EVENT_REMEDIATION",
        "HIGH_JOINT_COMPATIBILITY",
        "SEQUENCED_CONSTRAINT_REMEDIATION",
    }
)
UNLOCK_IDS = frozenset({"T6_ASSIGNMENT", "CONSTRAINT_L2", "T6_EVENT", "T7_CONSTRAINT"})
MISSING_IDS = frozenset(
    {
        "ASSIGNMENT_BOUNDED_SURFACE",
        "EVENT_YK_REMEDIATION",
        "CONSTRAINT_REMEDIATION_CONTRACT",
        "JOINT_COMPATIBILITY_CONTRACT",
        "OCP005_CANONICAL_OR_SELECTED_JOINT",
        "CANDIDATE_BOARD_SELECTION",
    }
)
OPTION_RESULTS = frozenset(
    {"legal-current", "not-ready", "leading-continuation-not-selected", "sequenced-only"}
)
RECOMMENDATION_VALUES = frozenset({"HOLD", "EVENT_YK_REMEDIATION"})

EXPECTED_L2 = {
    "OCP-005": (("OCP-000", "OCP-001", "OCP-002", "OCP-003", "OCP-004"), "pass", ()),
    "OCP-006": (("OCP-000", "OCP-001", "OCP-002", "OCP-003", "OCP-004", "OCP-005"), "pass", ()),
    "OCP-010": (("OCP-000", "OCP-001", "OCP-002", "OCP-004", "OCP-008"), "pass", ()),
}
EXPECTED_OPTIONS = {
    "HOLD": ((), "not-applicable", (), "DELAY_ONLY", (), (), "legal-current"),
    "ASSIGNMENT": (
        ("OCP-005",), "pass",
        ("ASSIGNMENT_COMPATIBILITY_SURFACE_ABSENT", "BOARD_SELECTION_ABSENT"),
        "BROAD_ASSIGNMENT_DISCOVERY", ("T6_ASSIGNMENT", "CONSTRAINT_L2"),
        ("ASSIGNMENT_BOUNDED_SURFACE", "CANDIDATE_BOARD_SELECTION"), "not-ready",
    ),
    "EVENT": (
        ("OCP-010",), "pass",
        ("EVENT_OWNER_UNRESOLVED", "EVENT_LEGACY_OVERLAP", "EVENT_CONSUMER_BINDINGS_UNVERSIONED", "BOARD_SELECTION_ABSENT"),
        "BOUNDED_EVENT_REMEDIATION", ("T6_EVENT",),
        ("EVENT_YK_REMEDIATION", "CANDIDATE_BOARD_SELECTION"),
        "leading-continuation-not-selected",
    ),
    "JOINT_ASSIGNMENT_CONSTRAINT": (
        ("OCP-005", "OCP-006"), "mixed",
        ("JOINT_CURRENT_L2_MIXED", "ASSIGNMENT_COMPATIBILITY_SURFACE_ABSENT", "CONSTRAINT_REMEDIATION_SURFACE_ABSENT", "BOARD_SELECTION_ABSENT"),
        "HIGH_JOINT_COMPATIBILITY", ("T6_ASSIGNMENT", "T7_CONSTRAINT"),
        ("ASSIGNMENT_BOUNDED_SURFACE", "CONSTRAINT_REMEDIATION_CONTRACT", "JOINT_COMPATIBILITY_CONTRACT", "CANDIDATE_BOARD_SELECTION"),
        "not-ready",
    ),
    "CONSTRAINT_REMEDIATION": (
        ("OCP-006",), "fail",
        ("CONSTRAINT_L2_BLOCKED_BY_OCP005", "CONSTRAINT_REMEDIATION_SURFACE_ABSENT", "BOARD_SELECTION_ABSENT"),
        "SEQUENCED_CONSTRAINT_REMEDIATION", ("T7_CONSTRAINT",),
        ("OCP005_CANONICAL_OR_SELECTED_JOINT", "CONSTRAINT_REMEDIATION_CONTRACT", "CANDIDATE_BOARD_SELECTION"),
        "sequenced-only",
    ),
}
EXPECTED_EVIDENCE = {
    "ASSIGNMENT_COMPATIBILITY_SURFACE_ABSENT": (("docs/005-assignment-concept/README.md", ("## 19. Open Questions and Resolved Boundaries", "Яка amendment model потрібна", "Яка replacement policy")),),
    "EVENT_OWNER_UNRESOLVED": (("docs/010-event-concept/README.md", ("Який normative owner визначить Operation-to-Event relationship record",)),),
    "EVENT_LEGACY_OVERLAP": (("docs/010-event-concept/README.md", ("checker-local assessment envelope", "не є normative OutcomeAssessmentRecord contract")), ("docs/011-outcome-assessment-record/README.md", ("Status: Accepted", "OutcomeAssessmentRecord"))),
    "EVENT_CONSUMER_BINDINGS_UNVERSIONED": (("docs/011-outcome-assessment-record/README.md", ("Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, OCP-006, OCP-008, OCP-010",)), ("docs/017-operation-lifecycle/README.md", ("Depends-On: AD-020, OCP-001, OCP-004, OCP-005, OCP-006, OCP-010",))),
    "JOINT_CURRENT_L2_MIXED": (("docs/006-constraint-concept/README.md", ("Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-004, OCP-005",)), ("docs/005-assignment-concept/README.md", ("Status: Draft",))),
    "CONSTRAINT_L2_BLOCKED_BY_OCP005": (("docs/006-constraint-concept/README.md", ("Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-004, OCP-005",)), ("docs/005-assignment-concept/README.md", ("Status: Draft",))),
    "CONSTRAINT_REMEDIATION_SURFACE_ABSENT": (("docs/006-constraint-concept/README.md", ("## 22. Open Questions and Resolved Boundaries", "Яка канонічна expression або rule language", "Який строк актуальності")),),
    "BOARD_SELECTION_ABSENT": (("architecture/foundation-promotion-reassessment.yaml", ("baseline_gate_state:", "required_before_promotion: [CANDIDATE_BOARD_SELECTION]", "promotion_selections: []")),),
}

MAP_KEYS = {
    "schema_version", "rule_owner", "baseline", "baseline_gate_state",
    "baseline_evidence_objects", "gate_applicability", "criterion",
    "live_l2", "options", "recommendation", "evidence",
}
BASELINE_OBJECT_KEYS = {"path", "blob", "sha256"}
L2_KEYS = {"document_id", "direct_ocp_dependencies", "result", "blockers"}
OPTION_KEYS = {
    "option_id", "candidate_documents", "l2_result", "blocker_ids", "cost_id",
    "unlock_ids", "missing_for_legality", "result",
}
EVIDENCE_KEYS = {"path", "tokens"}
EXPECTED_BASELINE_EVIDENCE_OBJECTS = {
    "docs/005-assignment-concept/README.md": (
        "7a82a051cfb572e31cceded52bdfbb8e917bffba",
        "fbdbe9b4547f7b1f14c766e1925ff28d620c671a271cfc8721f8d6b8d4db7b5a",
    ),
    "docs/006-constraint-concept/README.md": (
        "95ef13a917e0f579cdd656672a6bd883060bb818",
        "d1d2a8c4d85ffba3bbe22d38ed443946e8196558e42c67d929347436468632b6",
    ),
    "docs/010-event-concept/README.md": (
        "3a49b75bfa479e24debb89a130b7a05d6c790a88",
        "5ead70eb7238d6b6e630d2fa5850bb4a9325a752fed57d9239b9977642d67706",
    ),
    "docs/011-outcome-assessment-record/README.md": (
        "ff2608a372c6305db4c290f05c15e961ca96e6f6",
        "1fb08e18fab560e671b468585d699a7d70bd55ed5be674315cb780a48bc70cc5",
    ),
    "docs/017-operation-lifecycle/README.md": (
        "0b2ea683df308babd1111ff47e9272c9b0742f78",
        "061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030",
    ),
}


@dataclass(frozen=True)
class FoundationPromotionReassessmentResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> FoundationPromotionReassessmentResult:
    return FoundationPromotionReassessmentResult(tuple(dict.fromkeys(errors)))


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
        value = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return value if isinstance(value, dict) else None


def _references(value: Any) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(str(item).strip() for item in value if str(item).strip())
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    return ()


def _ocp_index(repo_root: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    result: dict[str, tuple[Path, dict[str, Any]]] = {}
    for primary in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(primary)
        if metadata is not None and isinstance(metadata.get("Document-ID"), str):
            result[str(metadata["Document-ID"])] = (primary, metadata)
    return result


def _load_yaml(fpath: Path) -> Any:
    try:
        return yaml.safe_load(fpath.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None


def validate_foundation_promotion_reassessment(
    repo_root: Path,
) -> FoundationPromotionReassessmentResult:
    errors: list[str] = []
    payload = _load_yaml(repo_root / "architecture/foundation-promotion-reassessment.yaml")
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((FOUNDATION_REASSESSMENT_MAP_INVALID,))
    baseline_objects = payload.get("baseline_evidence_objects")
    normalized_objects: dict[str, tuple[str, str]] = {}
    if not isinstance(baseline_objects, list):
        errors.append(FOUNDATION_REASSESSMENT_EVIDENCE_DRIFT)
    else:
        for item in baseline_objects:
            if not isinstance(item, dict) or set(item) != BASELINE_OBJECT_KEYS:
                errors.append(FOUNDATION_REASSESSMENT_EVIDENCE_DRIFT)
                continue
            path = item.get("path")
            if not isinstance(path, str) or path in normalized_objects:
                errors.append(FOUNDATION_REASSESSMENT_EVIDENCE_DRIFT)
                continue
            normalized_objects[path] = (str(item.get("blob")), str(item.get("sha256")))
        if normalized_objects != EXPECTED_BASELINE_EVIDENCE_OBJECTS:
            errors.append(FOUNDATION_REASSESSMENT_EVIDENCE_DRIFT)
    gate_applicability = payload.get("gate_applicability")
    if (
        payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-016AB"
        or payload.get("baseline") != "53d254405e6f75c7198e3e989d14a5a5678628ce"
        or payload.get("baseline_gate_state") != {
            "completed_steps": [
                "T0", "T1", "T2", "T3", "AD-016C", "AD-016D", "T4", "T5",
                "AD-016Y", "AD-016Z", "Y10D", "POST_DISCOVERY_REASSESSMENT",
            ],
            "required_before_promotion": ["CANDIDATE_BOARD_SELECTION"],
            "promotion_selections": [],
        }
        or gate_applicability != {
            "form": "governance-reassessment",
            "g4_required": False,
            "accepted_consumer_required": False,
        }
        or tuple(payload.get("criterion") or ()) != CRITERION_ORDER
        or set(payload.get("criterion") or ()) != CRITERION_IDS
    ):
        errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)

    ocps = _ocp_index(repo_root)
    statuses = {
        document_id: str(metadata.get("Status") or "")
        for document_id, (_, metadata) in ocps.items()
    }
    live_entries = payload.get("live_l2")
    if not isinstance(live_entries, list):
        errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
        live_entries = []
    seen_l2: set[str] = set()
    derived_l2: dict[str, tuple[tuple[str, ...], str, tuple[str, ...]]] = {}
    for entry in live_entries:
        if not isinstance(entry, dict) or set(entry) != L2_KEYS:
            errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
            continue
        document_id = entry.get("document_id")
        resolved = ocps.get(str(document_id))
        if document_id not in CANDIDATE_IDS or document_id in seen_l2 or resolved is None:
            errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
            continue
        seen_l2.add(str(document_id))
        dependencies = tuple(
            item for item in _references(resolved[1].get("Depends-On")) if item.startswith("OCP-")
        )
        blockers = tuple(item for item in dependencies if statuses.get(item) != "Canonical")
        result = "pass" if not blockers else "fail"
        derived = (dependencies, result, blockers)
        derived_l2[str(document_id)] = derived
        declared = (
            tuple(entry.get("direct_ocp_dependencies") or ()),
            entry.get("result"),
            tuple(entry.get("blockers") or ()),
        )
        if declared != derived or derived != EXPECTED_L2.get(str(document_id)):
            errors.append(FOUNDATION_REASSESSMENT_L2_MISMATCH)
    if seen_l2 != CANDIDATE_IDS:
        errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)

    gate_candidates = payload.get("live_l2")
    if not isinstance(gate_candidates, list):
        errors.append(FOUNDATION_REASSESSMENT_GATE_STATE_INVALID)
    else:
        for candidate in gate_candidates:
            if not isinstance(candidate, dict):
                errors.append(FOUNDATION_REASSESSMENT_GATE_STATE_INVALID)
                continue
            document_id = str(candidate.get("document_id"))
            derived = derived_l2.get(document_id)
            claimed = (
                tuple(candidate.get("direct_ocp_dependencies") or ()),
                candidate.get("result"),
                tuple(candidate.get("blockers") or ()),
            )
            if derived is None or claimed != derived:
                errors.append(FOUNDATION_REASSESSMENT_L2_MISMATCH)

    options = payload.get("options")
    if not isinstance(options, list):
        errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
        options = []
    seen_options: set[str] = set()
    for option in options:
        if not isinstance(option, dict) or set(option) != OPTION_KEYS:
            errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
            continue
        option_id = str(option.get("option_id"))
        normalized = (
            tuple(option.get("candidate_documents") or ()),
            option.get("l2_result"),
            tuple(option.get("blocker_ids") or ()),
            option.get("cost_id"),
            tuple(option.get("unlock_ids") or ()),
            tuple(option.get("missing_for_legality") or ()),
            option.get("result"),
        )
        if option_id in seen_options or normalized != EXPECTED_OPTIONS.get(option_id):
            errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
        seen_options.add(option_id)
        if (
            not set(normalized[0]) <= CANDIDATE_IDS
            or normalized[1] not in L2_RESULTS
            or not set(normalized[2]) <= BLOCKER_IDS
            or normalized[3] not in COST_IDS
            or not set(normalized[4]) <= UNLOCK_IDS
            or not set(normalized[5]) <= MISSING_IDS
            or normalized[6] not in OPTION_RESULTS
        ):
            errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
    if seen_options != OPTION_IDS:
        errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)

    recommendation = payload.get("recommendation")
    if recommendation != {
        "current_promotion": "HOLD",
        "continuation": "EVENT_YK_REMEDIATION",
        "selection_authority": False,
        "selected_candidates": [],
    }:
        errors.append(FOUNDATION_REASSESSMENT_SELECTION_FORBIDDEN)
    elif {
        recommendation["current_promotion"], recommendation["continuation"]
    } != RECOMMENDATION_VALUES:
        errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)

    evidence = payload.get("evidence")
    if not isinstance(evidence, dict) or set(evidence) != BLOCKER_IDS:
        errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
        evidence = {}
    for blocker_id, expected_items in EXPECTED_EVIDENCE.items():
        items = evidence.get(blocker_id)
        if not isinstance(items, list):
            errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
            continue
        normalized_items: list[tuple[str, tuple[str, ...]]] = []
        for item in items:
            if not isinstance(item, dict) or set(item) != EVIDENCE_KEYS:
                errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
                continue
            fpath = item.get("path")
            tokens = item.get("tokens")
            candidate = Path(str(fpath))
            if (
                not isinstance(fpath, str)
                or candidate.is_absolute()
                or ".." in candidate.parts
                or not isinstance(tokens, list)
                or not tokens
                or any(not isinstance(token, str) or not token for token in tokens)
            ):
                errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
                continue
            normalized_items.append((fpath, tuple(tokens)))
        if tuple(normalized_items) != expected_items:
            errors.append(FOUNDATION_REASSESSMENT_MAP_INVALID)
    # Tokens in this map's own baseline_gate_state are executable schema
    # invariants, not claims about a pre-existing baseline object.
    evidence_paths = {
        path for expected_items in EXPECTED_EVIDENCE.values() for path, _ in expected_items
    } - {"architecture/foundation-promotion-reassessment.yaml"}
    if evidence_paths != set(EXPECTED_BASELINE_EVIDENCE_OBJECTS):
        errors.append(FOUNDATION_REASSESSMENT_EVIDENCE_DRIFT)
    return _result(errors)
