from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


EVENT_PROMOTION_SELECTION_MAP_INVALID = "EVENT_PROMOTION_SELECTION_MAP_INVALID"
EVENT_PROMOTION_SELECTION_SUBJECT_DRIFT = "EVENT_PROMOTION_SELECTION_SUBJECT_DRIFT"
EVENT_PROMOTION_SELECTION_CONSUMER_DRIFT = "EVENT_PROMOTION_SELECTION_CONSUMER_DRIFT"
EVENT_PROMOTION_SELECTION_EVIDENCE_DRIFT = "EVENT_PROMOTION_SELECTION_EVIDENCE_DRIFT"
EVENT_PROMOTION_SELECTION_GATE_DRIFT = "EVENT_PROMOTION_SELECTION_GATE_DRIFT"

MAP_KEYS = frozenset({
    "schema_version", "rule_owner", "baseline", "baseline_subject_state",
    "baseline_evidence_objects", "gate_applicability", "selected_unit",
    "compatibility", "migration", "rollback", "witness_model", "evidence",
})
BASELINE_SUBJECT_KEYS = frozenset({"version", "status", "concept_status", "blob", "sha256"})
BASELINE_OBJECT_KEYS = frozenset({"path", "blob", "sha256"})
SELECTED_UNIT_KEYS = frozenset({
    "document_id", "primary", "expected_version", "expected_status",
    "expected_concept_status", "selection_input", "disposition",
})
COMPATIBILITY_KEYS = frozenset({"consumers", "blocker_contracts"})
CONSUMER_KEYS = frozenset({
    "document_id", "primary", "expected_version", "expected_status",
    "document_binding", "preserved_refs",
})
BLOCKER_KEYS = frozenset({"blocker_id", "treatment", "promotion_effect"})
MIGRATION_KEYS = frozenset({"data", "references", "schemas", "promotion_preconditions"})
ROLLBACK_KEYS = frozenset({"unit", "partial_rollback", "restores"})
WITNESS_KEYS = frozenset({
    "selected", "rejected", "selected_consequence", "rejected_harm",
    "dependency_criterion", "executable_locations", "descriptive_locations",
})
EVIDENCE_KEYS = frozenset({"path", "tokens"})
CONSUMER_IDS = frozenset({"OCP-011", "OCP-017"})
BLOCKER_IDS = frozenset({
    "EVENT_OWNER_UNRESOLVED", "EVENT_LEGACY_OVERLAP",
    "EVENT_CONSUMER_BINDINGS_UNVERSIONED",
})
TREATMENTS = frozenset({
    "EXCLUDE_POSITIVE_OPERATION_EVENT_RELATION_UNTIL_SEPARATE_OWNER_ACT",
    "PRESERVE_OCP011_ASSESSMENT_AUTHORITY_AND_REMEDIATE_LOCAL_ENVELOPE",
    "PROVE_OCP011_OCP017_COMPATIBILITY_WITH_SELECTED_SURFACE",
})
PROMOTION_EFFECTS = frozenset({
    "BLOCKS_WHOLE_DOCUMENT_FREEZE", "REQUIRES_EVENT_REMEDIATION",
    "REQUIRES_CONSUMER_COMPATIBILITY_EVIDENCE",
})
PRECONDITIONS = frozenset({
    "EVENT_OWNER_BOUNDARY_REMEDIATED", "LEGACY_ASSESSMENT_OVERLAP_REMEDIATED",
    "PRIMARY_CONSUMER_COMPATIBILITY_PROVED",
})
DEPENDENCY_CRITERIA = frozenset({
    "READS_GATE_STATE_FIELDS", "CARRIES_GATE_STATE_AS_EVIDENCE_TOKENS",
    "VALIDATES_HISTORICAL_RECORD_AGAINST_LIVE_GATE", "CLAIMS_CURRENT_GATE_STATE_IN_ACCOUNTING",
})
EXECUTABLE_LOCATIONS = frozenset({
    "architecture/foundation-promotion-gate.yaml",
    "architecture/foundation-promotion-reassessment.yaml",
    "architecture/event-stable-surface.yaml",
    "architecture/event-promotion-selection.yaml",
    "tools/ontology_checker/ocp_checker/foundation_promotion_gate.py",
    "tools/ontology_checker/ocp_checker/foundation_promotion_reassessment.py",
    "tools/ontology_checker/ocp_checker/event_stable_surface.py",
    "tools/ontology_checker/ocp_checker/event_promotion_selection.py",
})
DESCRIPTIVE_LOCATIONS = frozenset({
    "architecture/discovery/AD-016-foundation-canonicalization-readiness.md",
    "architecture/discovery/AD-031-event-dependency-stable-surface.md",
    "README.md", "backlog/roadmap.md", "backlog/architecture-backlog.md",
    "tools/ontology_checker/README.md",
})

EXPECTED_CONSUMERS = {
    "OCP-011": ("docs/011-outcome-assessment-record/README.md", "0.3.0", "Accepted", ("event@1", "observation-record@1")),
    "OCP-017": ("docs/017-operation-lifecycle/README.md", "0.2.0", "Accepted", ()),
}
EXPECTED_BLOCKERS = {
    "EVENT_OWNER_UNRESOLVED": ("EXCLUDE_POSITIVE_OPERATION_EVENT_RELATION_UNTIL_SEPARATE_OWNER_ACT", "BLOCKS_WHOLE_DOCUMENT_FREEZE"),
    "EVENT_LEGACY_OVERLAP": ("PRESERVE_OCP011_ASSESSMENT_AUTHORITY_AND_REMEDIATE_LOCAL_ENVELOPE", "REQUIRES_EVENT_REMEDIATION"),
    "EVENT_CONSUMER_BINDINGS_UNVERSIONED": ("PROVE_OCP011_OCP017_COMPATIBILITY_WITH_SELECTED_SURFACE", "REQUIRES_CONSUMER_COMPATIBILITY_EVIDENCE"),
}
EXPECTED_EVIDENCE = {
    "EVENT_OWNER_UNRESOLVED": (("docs/010-event-concept/README.md", ("не вводить current Concept edge `Event → Operation` або `Operation → Event`", "Operation-to-Event relationship record")),),
    "EVENT_LEGACY_OVERLAP": (("docs/010-event-concept/README.md", ("checker-local assessment envelope", "не є normative OutcomeAssessmentRecord contract")), ("docs/011-outcome-assessment-record/README.md", ("Status: Accepted", "OutcomeAssessmentRecord"))),
    "EVENT_CONSUMER_BINDINGS_UNVERSIONED": (("docs/011-outcome-assessment-record/README.md", ("Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, OCP-006, OCP-008, OCP-010",)), ("docs/017-operation-lifecycle/README.md", ("Depends-On: AD-020, OCP-001, OCP-004, OCP-005, OCP-006, OCP-010",))),
}
EXPECTED_BASELINE_SUBJECT_STATE = {
    "version": "0.2.1",
    "status": "Draft",
    "concept_status": "Accepted",
    "blob": "3a49b75bfa479e24debb89a130b7a05d6c790a88",
    "sha256": "5ead70eb7238d6b6e630d2fa5850bb4a9325a752fed57d9239b9977642d67706",
}
EXPECTED_BASELINE_EVIDENCE_OBJECTS = {
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
class EventPromotionSelectionResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> EventPromotionSelectionResult:
    return EventPromotionSelectionResult(tuple(dict.fromkeys(errors)))


def _load(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None


def _frontmatter(path: Path) -> dict[str, Any] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return None
    end = text.find("\n---\n", 4)
    try:
        value = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return value if isinstance(value, dict) else None


def validate_event_promotion_selection(repo_root: Path) -> EventPromotionSelectionResult:
    errors: list[str] = []
    payload = _load(repo_root / "architecture/event-promotion-selection.yaml")
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((EVENT_PROMOTION_SELECTION_MAP_INVALID,))
    if (
        payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-016AC"
        or payload.get("baseline") != "ffc698ecc7fabab9d0f8ade9c85913f7cc95eadc"
        or payload.get("gate_applicability") != {
            "form": "governance-selection-compatibility-witness",
            "g4_required": False,
            "accepted_consumer_required": False,
        }
    ):
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)

    baseline_subject = payload.get("baseline_subject_state")
    if (
        not isinstance(baseline_subject, dict)
        or set(baseline_subject) != BASELINE_SUBJECT_KEYS
        or baseline_subject != EXPECTED_BASELINE_SUBJECT_STATE
    ):
        errors.append(EVENT_PROMOTION_SELECTION_SUBJECT_DRIFT)

    baseline_objects = payload.get("baseline_evidence_objects")
    normalized_objects: dict[str, tuple[str, str]] = {}
    if not isinstance(baseline_objects, list):
        errors.append(EVENT_PROMOTION_SELECTION_EVIDENCE_DRIFT)
    else:
        for item in baseline_objects:
            if not isinstance(item, dict) or set(item) != BASELINE_OBJECT_KEYS:
                errors.append(EVENT_PROMOTION_SELECTION_EVIDENCE_DRIFT)
                continue
            path = item.get("path")
            if not isinstance(path, str) or path in normalized_objects:
                errors.append(EVENT_PROMOTION_SELECTION_EVIDENCE_DRIFT)
                continue
            normalized_objects[path] = (str(item.get("blob")), str(item.get("sha256")))
        if normalized_objects != EXPECTED_BASELINE_EVIDENCE_OBJECTS:
            errors.append(EVENT_PROMOTION_SELECTION_EVIDENCE_DRIFT)

    selected = payload.get("selected_unit")
    if not isinstance(selected, dict) or set(selected) != SELECTED_UNIT_KEYS:
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
    elif selected != {
        "document_id": "OCP-010", "primary": "docs/010-event-concept/README.md",
        "expected_version": "0.2.1", "expected_status": "Draft",
        "expected_concept_status": "Accepted", "selection_input": "ARCHITECTURE_BOARD_EVENT",
        "disposition": "SELECTED_NOT_PROMOTED",
    }:
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)

    compatibility = payload.get("compatibility")
    if not isinstance(compatibility, dict) or set(compatibility) != COMPATIBILITY_KEYS:
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
        compatibility = {}
    consumers = compatibility.get("consumers")
    if not isinstance(consumers, list) or {item.get("document_id") for item in consumers if isinstance(item, dict)} != CONSUMER_IDS:
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
        consumers = []
    for item in consumers:
        if not isinstance(item, dict) or set(item) != CONSUMER_KEYS:
            errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
            continue
        expected = EXPECTED_CONSUMERS.get(str(item.get("document_id")))
        if expected is None:
            errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
            continue
        path, version, status, refs = expected
        if item != {"document_id": item["document_id"], "primary": path, "expected_version": version, "expected_status": status, "document_binding": "unversioned-document", "preserved_refs": list(refs)}:
            errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
        consumer_meta = _frontmatter(repo_root / path)
        text = (repo_root / path).read_text(encoding="utf-8") if (repo_root / path).is_file() else ""
        if consumer_meta is None or str(consumer_meta.get("Version")) != version or consumer_meta.get("Status") != status or "OCP-010" not in str(consumer_meta.get("Depends-On")) or any(ref not in text for ref in refs):
            errors.append(EVENT_PROMOTION_SELECTION_CONSUMER_DRIFT)

    blockers = compatibility.get("blocker_contracts")
    if not isinstance(blockers, list) or {item.get("blocker_id") for item in blockers if isinstance(item, dict)} != BLOCKER_IDS:
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
        blockers = []
    for item in blockers:
        if not isinstance(item, dict) or set(item) != BLOCKER_KEYS or (item.get("treatment"), item.get("promotion_effect")) != EXPECTED_BLOCKERS.get(str(item.get("blocker_id"))):
            errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
    if {item.get("treatment") for item in blockers if isinstance(item, dict)} != TREATMENTS or {item.get("promotion_effect") for item in blockers if isinstance(item, dict)} != PROMOTION_EFFECTS:
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)

    migration = payload.get("migration")
    if not isinstance(migration, dict) or set(migration) != MIGRATION_KEYS or migration.get("data") != "NONE_AT_SELECTION" or migration.get("references") != "NONE_AT_SELECTION" or migration.get("schemas") != "NONE_AT_SELECTION" or set(migration.get("promotion_preconditions") or ()) != PRECONDITIONS:
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
    rollback = payload.get("rollback")
    if not isinstance(rollback, dict) or set(rollback) != ROLLBACK_KEYS or rollback != {"unit": "SELECTION_GATE_WITNESS_AND_ACCOUNTING", "partial_rollback": "FORBIDDEN", "restores": "REASSESSED_UNSELECTED_STATE"}:
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
    witness = payload.get("witness_model")
    if not isinstance(witness, dict) or set(witness) != WITNESS_KEYS or witness.get("selected") != "IMMUTABLE_BASELINE_BOUND" or witness.get("rejected") != "LIVE_GATE_TRACKING" or witness.get("selected_consequence") != "COMPLETED_STEP_EVIDENCE_REMAINS_VALID_AFTER_LATER_GATE_TRANSITIONS" or witness.get("rejected_harm") != "LEGAL_SELECTION_INVALIDATES_DISCOVERY_AND_REASSESSMENT_HISTORY" or set(witness.get("dependency_criterion") or ()) != DEPENDENCY_CRITERIA or set(witness.get("executable_locations") or ()) != EXECUTABLE_LOCATIONS or set(witness.get("descriptive_locations") or ()) != DESCRIPTIVE_LOCATIONS:
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)

    evidence = payload.get("evidence")
    if not isinstance(evidence, dict) or set(evidence) != BLOCKER_IDS:
        errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
        evidence = {}
    for blocker_id, expected_items in EXPECTED_EVIDENCE.items():
        items = evidence.get(blocker_id)
        normalized = []
        if not isinstance(items, list):
            errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
            continue
        for item in items:
            if not isinstance(item, dict) or set(item) != EVIDENCE_KEYS:
                errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
                continue
            path = item.get("path")
            tokens = item.get("tokens")
            normalized.append((path, tuple(tokens or ())))
            if not isinstance(tokens, list) or not tokens:
                errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)
        if tuple(normalized) != expected_items:
            errors.append(EVENT_PROMOTION_SELECTION_MAP_INVALID)

    evidence_paths = {
        path for expected_items in EXPECTED_EVIDENCE.values() for path, _ in expected_items
    }
    if evidence_paths != set(EXPECTED_BASELINE_EVIDENCE_OBJECTS):
        errors.append(EVENT_PROMOTION_SELECTION_EVIDENCE_DRIFT)

    return _result(errors)
