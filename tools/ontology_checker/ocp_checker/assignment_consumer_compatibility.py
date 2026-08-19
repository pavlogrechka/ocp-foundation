from __future__ import annotations

import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

from .checker import effective_constraint_result, load_fixture, validate_assignment
from .coordination_workflow import derive_coordination_evidence
from .interchangeability import derive_resource_interchangeability
from .operation_lifecycle import validate_operation_q3i_fixture
from .quantitative_input import validate_quantitative_input_fixture
from .reservation_boundary import validate_reservation_boundary_fixture
from .resource_occupancy import derive_resource_occupancy


ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID = "ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID"
ASSIGNMENT_CONSUMER_COMPATIBILITY_INVENTORY_DRIFT = "ASSIGNMENT_CONSUMER_COMPATIBILITY_INVENTORY_DRIFT"
ASSIGNMENT_CONSUMER_COMPATIBILITY_TEXT_DRIFT = "ASSIGNMENT_CONSUMER_COMPATIBILITY_TEXT_DRIFT"
ASSIGNMENT_CONSUMER_COMPATIBILITY_PROBE_DRIFT = "ASSIGNMENT_CONSUMER_COMPATIBILITY_PROBE_DRIFT"
ASSIGNMENT_CONSUMER_COMPATIBILITY_PROJECTION_DRIFT = "ASSIGNMENT_CONSUMER_COMPATIBILITY_PROJECTION_DRIFT"
ASSIGNMENT_CONSUMER_COMPATIBILITY_GATE_DRIFT = "ASSIGNMENT_CONSUMER_COMPATIBILITY_GATE_DRIFT"

MAP_KEYS = frozenset(
    {
        "schema_version", "rule_owner", "current_projection_owner", "baseline", "gate_first", "subject", "criterion",
        "stable_surface_witness", "consumer_results", "projection", "promotion_gate_guard",
        "baseline_evidence_objects", "forbidden_outcomes",
    }
)
CONSUMER_IDS = frozenset({"OCP-006", "OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021", "OCP-023"})
NEGATIVE_CONSUMER_IDS = frozenset({"OCP-013", "OCP-015", "OCP-020", "OCP-021"})
POSITIVE_CONSUMER_IDS = frozenset({"OCP-006", "OCP-017", "OCP-023"})
STABLE_SURFACE_IDS = frozenset(
    {
        "ASSIGNMENT_IDENTITY_REFERENCE_KERNEL", "TRANSITION_HISTORY_LIFECYCLE_KERNEL",
        "STRUCTURAL_ROLE_PROVENANCE_KERNEL", "NON_INHERITANCE_NON_AUTHORITY_BOUNDARY",
        "SUPERSESSION_IDENTITY_BOUNDARY", "EXECUTABLE_ASSIGNMENT_BOUNDARY",
    }
)
MOVING_SURFACE_IDS = frozenset(
    {
        "AMENDMENT_AFTER_ESTABLISHMENT", "TEMPORAL_EFFECTIVITY_EXTENSION", "ROLE_GOVERNANCE",
        "COMPOSITE_RESOURCE_SCOPE", "CONSTRAINT_CONFLICT_HANDOFF", "PROVENANCE_TAXONOMY",
        "REPLACEMENT_POLICY",
    }
)
REMAINING_BLOCKER_IDS = frozenset(
    {"AMENDMENT_MODEL_ABSENT", "TEMPORAL_MODEL_UNRESOLVED", "PARTIAL_SCOPE_IDENTITY_UNRESOLVED"}
)
FORBIDDEN_OUTCOMES = frozenset(
    {
        "ASSIGNMENT_SELECTION", "PROMOTION_CYCLE_START", "OCP005_PROMOTION",
        "ASSIGNMENT_FREEZE_REACHABLE", "OPEN_QUESTION_CLOSURE", "T7_OPEN",
    }
)

EXPECTED_IDENTITY = {
    "schema_version": 2,
    "rule_owner": "AD-040",
    "current_projection_owner": "AD-053",
    "baseline": "747d5aa2e71bd87c4e024d62f80d8cfa122d8279",
}
EXPECTED_GATE_FIRST = {
    "evidence_form": {
        "ocp016_gate": "G4",
        "applies": False,
        "reason": "compatibility-preservation-evidence-is-not-a-positive-capable-rule-result-or-profile",
    },
    "blocker_closure": {
        "ocp016_gate": "G4",
        "applies": False,
        "reason": "removing-an-evidence-debt-after-replay-adds-no-rule-field-result-or-profile",
    },
}
EXPECTED_SUBJECT = {
    "document_id": "OCP-005",
    "primary": "docs/005-assignment-concept/README.md",
    "expected_version": "0.2.8",
    "expected_status": "Draft",
    "expected_concept_status": "Accepted",
}
EXPECTED_CRITERION = {
    "accepted_consumer": "current-status-is-Accepted-and-Depends-On-exactly-includes-OCP-005",
    "preservation": "every-declared-consumed-element-is-inside-the-bounded-stable-surface-and-its-predeclared-real-fixture-result-is-unchanged-while-moving-surfaces-remain-open",
    "negative_consumer": "assignment-coupling-remains-fail-safe-and-non-permissive",
    "positive_consumer": "exact-current-assignment-alignment-remains-valid-with-the-same-terminal-disposition",
}
EXPECTED_CONSUMERS = {
    "OCP-006": {
        "primary": "docs/006-constraint-concept/README.md", "consumer_class": "positive-derivation",
        "consumed_tokens": (
            "кілька ефективних Assignment одного Resource",
            "Сам `supersedes_assignment_ref` не визначає допустимі часові межі",
            "Без цього Constraint сам факт кількох Assignment не є порушенням",
        ),
        "stable_surface_ids": (
            "ASSIGNMENT_IDENTITY_REFERENCE_KERNEL", "SUPERSESSION_IDENTITY_BOUNDARY",
            "EXECUTABLE_ASSIGNMENT_BOUNDARY",
        ),
        "moving_consumed_surface_ids": (),
        "moving_probe_surface_ids": (
            "AMENDMENT_AFTER_ESTABLISHMENT", "TEMPORAL_EFFECTIVITY_EXTENSION", "ROLE_GOVERNANCE",
            "COMPOSITE_RESOURCE_SCOPE", "CONSTRAINT_CONFLICT_HANDOFF", "PROVENANCE_TAXONOMY",
            "REPLACEMENT_POLICY",
        ),
        "fixture": "tools/ontology_checker/fixtures/constraint/valid-assignment-moving-surfaces-independent.yaml",
        "probe": "assignment_moving_surfaces_do_not_change_exact_snapshot_result",
        "expected_control": "satisfied",
        "expected_probe": "moving:satisfied|binding:indeterminate|assignment:valid/valid",
        "result": "preserved",
    },
    "OCP-013": {
        "primary": "docs/013-resource-interchangeability/README.md",
        "consumer_class": "negative-exclusion",
        "consumed_tokens": ("retain every exclusion of availability, authorization, ranking, selection, replacement and Assignment mutation",),
        "stable_surface_ids": ("NON_INHERITANCE_NON_AUTHORITY_BOUNDARY", "SUPERSESSION_IDENTITY_BOUNDARY"),
        "moving_consumed_surface_ids": (), "moving_probe_surface_ids": (),
        "fixture": "tools/ontology_checker/fixtures/interchangeability/mandatory-counterexamples.yaml",
        "probe": "assignment_mutation_is_rejected", "expected_control": "positive",
        "expected_probe": "indeterminate", "result": "preserved",
    },
    "OCP-015": {
        "primary": "docs/015-coordination-workflow/README.md", "consumer_class": "negative-exclusion",
        "consumed_tokens": ("preserves Resource and Assignment identity", "alter Resource or Assignment identity"),
        "stable_surface_ids": ("ASSIGNMENT_IDENTITY_REFERENCE_KERNEL", "NON_INHERITANCE_NON_AUTHORITY_BOUNDARY"),
        "moving_consumed_surface_ids": (), "moving_probe_surface_ids": (),
        "fixture": "tools/ontology_checker/fixtures/coordination_workflow/mandatory-cases.yaml",
        "probe": "assignment_mutation", "expected_control": "positive", "expected_probe": "indeterminate",
        "result": "preserved",
    },
    "OCP-017": {
        "primary": "docs/017-operation-lifecycle/README.md", "consumer_class": "positive-derivation",
        "consumed_tokens": (
            "if OCP-005 `assignment_effective_at` is true at that instant",
            "whose `operation_ref` names the Operation", "never edits an Assignment transition history",
        ),
        "stable_surface_ids": (
            "ASSIGNMENT_IDENTITY_REFERENCE_KERNEL", "TRANSITION_HISTORY_LIFECYCLE_KERNEL",
            "STRUCTURAL_ROLE_PROVENANCE_KERNEL", "EXECUTABLE_ASSIGNMENT_BOUNDARY",
        ),
        "moving_consumed_surface_ids": (),
        "moving_probe_surface_ids": (
            "AMENDMENT_AFTER_ESTABLISHMENT", "TEMPORAL_EFFECTIVITY_EXTENSION", "ROLE_GOVERNANCE",
            "COMPOSITE_RESOURCE_SCOPE",
        ),
        "fixture": "tools/ontology_checker/fixtures/operation_lifecycle/valid-q3i-completed.yaml",
        "probe": "terminal_alignment_with_open_moving_extensions",
        "expected_control": "valid-remains_effective_independently",
        "expected_probe": "valid-remains_effective_independently", "result": "preserved",
    },
    "OCP-020": {
        "primary": "docs/020-quantitative-constraint-input/README.md", "consumer_class": "negative-exclusion",
        "consumed_tokens": (
            "create, amend, activate, suspend or terminate an Assignment",
            "Existing Resource, Operation, Assignment and Constraint artifacts remain valid",
        ),
        "stable_surface_ids": ("NON_INHERITANCE_NON_AUTHORITY_BOUNDARY",),
        "moving_consumed_surface_ids": (), "moving_probe_surface_ids": (),
        "fixture": "tools/ontology_checker/fixtures/quantitative_input/invalid-forbidden-coupling.yaml",
        "probe": "assignment_mutation_forbidden_coupling",
        "expected_control": "valid",
        "expected_probe": "QUANTITATIVE_INPUT_FORBIDDEN_COUPLING", "result": "preserved",
    },
    "OCP-021": {
        "primary": "docs/021-reservation-allocation-boundary/README.md", "consumer_class": "negative-exclusion",
        "consumed_tokens": (
            "Their truth remains owned by OCP-005/OCP-006",
            "creates, blocks, cancels, supersedes or mutates an Assignment",
        ),
        "stable_surface_ids": (
            "ASSIGNMENT_IDENTITY_REFERENCE_KERNEL", "NON_INHERITANCE_NON_AUTHORITY_BOUNDARY",
            "SUPERSESSION_IDENTITY_BOUNDARY",
        ),
        "moving_consumed_surface_ids": (), "moving_probe_surface_ids": (),
        "fixture": "tools/ontology_checker/fixtures/reservation_boundary/invalid-forbidden-coupling.yaml",
        "probe": "assignment_mutation_forbidden_coupling",
        "expected_control": "valid",
        "expected_probe": "RESERVATION_BOUNDARY_FORBIDDEN_COUPLING+RESERVATION_BOUNDARY_REQUEST_INVALID",
        "result": "preserved",
    },
    "OCP-023": {
        "primary": "docs/023-resource-occupancy/README.md", "consumer_class": "positive-derivation",
        "consumed_tokens": (
            "assignment_effective_at(assignment, at)",
            "Every Assignment must independently satisfy the current OCP-005 reference validator",
        ),
        "stable_surface_ids": ("ASSIGNMENT_IDENTITY_REFERENCE_KERNEL", "EXECUTABLE_ASSIGNMENT_BOUNDARY"),
        "moving_consumed_surface_ids": (), "moving_probe_surface_ids": (),
        "fixture": "tools/ontology_checker/fixtures/resource_occupancy/valid-one-effective.yaml",
        "probe": "completeness_evidence_removed", "expected_control": "occupied:A-001",
        "expected_probe": "indeterminate", "result": "preserved",
    },
}
EXPECTED_PROJECTION = {
    "blocker_removed": "ACCEPTED_CONSUMER_COMPATIBILITY_UNPROVEN",
    "remaining_blockers": ["AMENDMENT_MODEL_ABSENT", "TEMPORAL_MODEL_UNRESOLVED", "PARTIAL_SCOPE_IDENTITY_UNRESOLVED"],
    "promotion_reachable": False,
    "questions_changed": [],
}
EXPECTED_GATE_GUARD = {"schema_version": 5, "completed_cycle_ids": ["EVENT_T6"], "active_cycle_id": None}
EXPECTED_ANCHORS = {
    "docs/005-assignment-concept/README.md": ("6e6c00e723b15a348e7610d4ca5a1ae23526c52b", "a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065"),
    "docs/013-resource-interchangeability/README.md": ("658a291b4c3b9a0229aba09d485c1137723fe70b", "a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74"),
    "docs/015-coordination-workflow/README.md": ("ea60634e54faedabb8c5e08b036030c2f0e4e20b", "6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d"),
    "docs/017-operation-lifecycle/README.md": ("0b2ea683df308babd1111ff47e9272c9b0742f78", "061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030"),
    "docs/020-quantitative-constraint-input/README.md": ("0e1e7d0947ab3c7d1c0355258651179f618636a2", "1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c"),
    "docs/021-reservation-allocation-boundary/README.md": ("bae4ac5de36b5d2a2d0c9182e5f1208c14593a35", "6289378b6d9f785e24abca39dbd6d3da550ccb21a43b3d1632e8c5de4894a89e"),
    "docs/016-core-boundary/README.md": ("94f5d997deea0168a3c553c2ac9f19d2ee03b4fb", "78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4"),
    "architecture/discovery/AD-035-assignment-stable-surface.md": ("81ed1c4981c97a0d0a4511e4492741bf5382ce05", "85a10e965faaa7ba65484efe08e985b7a04bf06712553c914673d65faf1df805"),
    "architecture/assignment-stable-surface.yaml": ("ae8a2ff5bf493182d4cd51e897afe736ed36cd5d", "617af7d0598bbdd756fd890a6dcd38f0324d6c481abf2f72c5a871c439a6bcc8"),
    "architecture/foundation-promotion-gate.yaml": ("78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1", "ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd"),
    "tools/ontology_checker/fixtures/interchangeability/mandatory-counterexamples.yaml": ("3437e78bbff39a3ac977755ebe9e7af849aed60e", "6815557ac57854ba3dfa1214462818132595b13cd0594b220cef8a649e7eca66"),
    "tools/ontology_checker/fixtures/coordination_workflow/mandatory-cases.yaml": ("6ce9ce33cc648ce6825fe8e9009caffdc5a53768", "16fdfbe2943760435a8030b8558290640b8dbf4abe882ee1cc985821015e2162"),
    "tools/ontology_checker/fixtures/operation_lifecycle/valid-q3i-completed.yaml": ("c85a65e217c7d0ecdbabf8e9adf76f1a88a7faff", "901ce32b9af2dcf9e664b565c7a6a4fc8919c7329d40d666a38a3115d0fb5672"),
    "tools/ontology_checker/fixtures/quantitative_input/invalid-forbidden-coupling.yaml": ("ce9e2a55acb574b0d542e29764ef5ef3f6b43834", "2ec5f9c2c2893c10cfd14fb25531a1f374d29a166b5f0696a5c374f7a481007e"),
    "tools/ontology_checker/fixtures/reservation_boundary/invalid-forbidden-coupling.yaml": ("580df6de3974854d52e3d56df41d16b4f274895c", "6d66155d4c438304449242def419c1f40078ddbcbe0898c01faeed63c9d24135"),
}


@dataclass(frozen=True)
class AssignmentConsumerCompatibilityResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentConsumerCompatibilityResult:
    return AssignmentConsumerCompatibilityResult(tuple(dict.fromkeys(errors)))


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
        value = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return value if isinstance(value, dict) else None


def _refs(value: Any) -> set[str]:
    if isinstance(value, list):
        return {str(item).strip() for item in value}
    if isinstance(value, str):
        return {item.strip() for item in value.split(",")}
    return set()


def _normalize_consumer(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "primary": item.get("primary"), "consumer_class": item.get("consumer_class"),
        "consumed_tokens": tuple(item.get("consumed_tokens") or ()),
        "stable_surface_ids": tuple(item.get("stable_surface_ids") or ()),
        "moving_consumed_surface_ids": tuple(item.get("moving_consumed_surface_ids") or ()),
        "moving_probe_surface_ids": tuple(item.get("moving_probe_surface_ids") or ()),
        "fixture": item.get("fixture"), "probe": item.get("probe"),
        "expected_control": item.get("expected_control"), "expected_probe": item.get("expected_probe"),
        "result": item.get("result"),
    }


def _anchors(value: Any) -> dict[str, tuple[str, str]] | None:
    if not isinstance(value, list):
        return None
    result: dict[str, tuple[str, str]] = {}
    for item in value:
        if not isinstance(item, dict) or set(item) != {"path", "blob", "sha256"}:
            return None
        path = item.get("path")
        if not isinstance(path, str) or path in result:
            return None
        result[path] = (str(item.get("blob")), str(item.get("sha256")))
    return result


def _positive_disposition(fixture: dict[str, Any]) -> str | None:
    try:
        return fixture["operation_lifecycles"][0]["transition_history"][-1]["assignment_alignment"]["dispositions"][0]["disposition"]
    except (KeyError, IndexError, TypeError):
        return None


def _probe(repo_root: Path, consumer_id: str, consumer: dict[str, Any]) -> tuple[str, str] | None:
    try:
        fixture = load_fixture(repo_root / consumer["fixture"])
    except (OSError, ValueError, yaml.YAMLError):
        return None
    if consumer_id == "OCP-006":
        constraint = fixture["entity"]
        context = fixture["contexts"][0]
        version = fixture["reference"]["constraint_version_ref"]
        assignment = fixture["assignments"][0]
        control = effective_constraint_result(constraint, context, version)
        mutated_assignment = copy.deepcopy(assignment)
        mutated_assignment.update({
            "amendment_model": {"synthetic": True},
            "applicability_intervals": [{"start": "2026-08-02T10:00:00Z", "end": "2026-08-02T12:00:00Z"}],
            "role_governance": {"synthetic": True},
            "resource_scope": {"kind": "component", "component_ref": "R-SYNTH-COMPONENT"},
            "constraint_conflict_handoff": {"synthetic": True},
            "provenance_taxonomy": {"synthetic": True},
            "replacement_policy": {"synthetic": True},
        })
        moving = effective_constraint_result(constraint, context, version)
        mismatched_context = copy.deepcopy(context)
        mismatched_context["input_snapshot_ref"] = "SNAP-MISMATCH"
        binding = effective_constraint_result(constraint, mismatched_context, version)
        original_valid = validate_assignment(assignment).valid
        mutated_valid = validate_assignment(mutated_assignment).valid
        return control, f"moving:{moving}|binding:{binding}|assignment:{'valid' if original_valid else 'invalid'}/{'valid' if mutated_valid else 'invalid'}"
    if consumer_id == "OCP-013":
        control = fixture["cases"]["b_substitutes_for_a"]
        probe = fixture["cases"][consumer["probe"]]
        return (
            derive_resource_interchangeability(control["evaluation"], fixture["requirements"]),
            derive_resource_interchangeability(probe["evaluation"], fixture["requirements"]),
        )
    if consumer_id == "OCP-015":
        snapshot = fixture["cases"]["all_invited_responders_confirm"]["snapshot"]
        mutated = copy.deepcopy(snapshot)
        mutated[consumer["probe"]] = {"synthetic": True}
        return derive_coordination_evidence(snapshot), derive_coordination_evidence(mutated)
    if consumer_id == "OCP-017":
        control = validate_operation_q3i_fixture(fixture)
        mutated = copy.deepcopy(fixture)
        assignment = mutated["assignments"][0]
        assignment["amendment_model"] = {"synthetic": True}
        assignment["applicability_intervals"] = [{"start": "2026-08-08T10:20:00Z", "end": "2026-08-08T11:00:00Z"}]
        assignment["role_governance"] = {"synthetic": True}
        assignment["resource_scope"] = {"kind": "component", "component_ref": "R-SYNTH-COMPONENT"}
        probe = validate_operation_q3i_fixture(mutated)
        control_value = f"{'valid' if control.valid else 'invalid'}-{_positive_disposition(fixture)}"
        probe_value = f"{'valid' if probe.valid else 'invalid'}-{_positive_disposition(mutated)}"
        return control_value, probe_value
    if consumer_id == "OCP-020":
        controlled = copy.deepcopy(fixture)
        controlled["dataset"].pop("reservation", None)
        controlled["dataset"]["aggregation_request"]["stored_total"] = {
            "magnitude_lexeme": "1", "unit_ref": "UNIT-SYNTH-O@1", "dimension_ref": "DIMENSION-SYNTH-O@1"
        }
        control = validate_quantitative_input_fixture(controlled)
        probed = copy.deepcopy(fixture)
        probed["dataset"].pop("reservation", None)
        probed["dataset"]["assignment_mutation"] = {"synthetic": True}
        probe = validate_quantitative_input_fixture(probed)
        return ("valid" if control.valid else "+".join(sorted(control.errors))), "+".join(sorted(probe.errors))
    if consumer_id == "OCP-021":
        controlled = copy.deepcopy(fixture)
        controlled["dataset"]["establishment_request"].pop("assignment_mutation", None)
        controlled["dataset"]["establishment_request"]["stored_result"] = "whole_resource_reservation_not_established"
        control = validate_reservation_boundary_fixture(controlled)
        probe = validate_reservation_boundary_fixture(fixture)
        return ("valid" if control.valid else "+".join(sorted(control.errors))), "+".join(sorted(probe.errors))
    if consumer_id == "OCP-023":
        control = derive_resource_occupancy(fixture["dataset"])
        mutated = copy.deepcopy(fixture["dataset"])
        mutated["assignment_snapshots"][0]["completeness_evidence_ref"] = None
        probe = derive_resource_occupancy(mutated)
        control_value = (
            f"occupied:{','.join(control.witness_assignment_refs)}"
            if control.occupied is True else "indeterminate"
        )
        probe_value = (
            f"occupied:{','.join(probe.witness_assignment_refs)}"
            if probe.occupied is True else "indeterminate"
        )
        return control_value, probe_value
    return None


def validate_assignment_consumer_compatibility(repo_root: Path) -> AssignmentConsumerCompatibilityResult:
    errors: list[str] = []
    try:
        payload = yaml.safe_load((repo_root / "architecture/assignment-consumer-compatibility.yaml").read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return _result((ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID,))
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID,))
    if (
        any(payload.get(key) != value for key, value in EXPECTED_IDENTITY.items())
        or payload.get("gate_first") != EXPECTED_GATE_FIRST
        or payload.get("subject") != EXPECTED_SUBJECT
        or payload.get("criterion") != EXPECTED_CRITERION
        or payload.get("stable_surface_witness") != "architecture/assignment-stable-surface.yaml"
        or payload.get("projection") != EXPECTED_PROJECTION
        or payload.get("promotion_gate_guard") != EXPECTED_GATE_GUARD
        or _anchors(payload.get("baseline_evidence_objects")) != EXPECTED_ANCHORS
        or set(payload.get("forbidden_outcomes") or ()) != FORBIDDEN_OUTCOMES
        or len(payload.get("forbidden_outcomes") or ()) != len(FORBIDDEN_OUTCOMES)
    ):
        errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID)

    entries = payload.get("consumer_results")
    normalized: dict[str, dict[str, Any]] = {}
    if isinstance(entries, list):
        for item in entries:
            if not isinstance(item, dict) or set(item) != {"consumer_id", *next(iter(EXPECTED_CONSUMERS.values())).keys()}:
                errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID)
                continue
            consumer_id = item.get("consumer_id")
            if not isinstance(consumer_id, str) or consumer_id in normalized:
                errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID)
                continue
            normalized[consumer_id] = _normalize_consumer(item)
    else:
        errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID)
    if set(normalized) != CONSUMER_IDS or normalized != EXPECTED_CONSUMERS:
        errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID)
    if {key for key, value in normalized.items() if value.get("consumer_class") == "negative-exclusion"} != NEGATIVE_CONSUMER_IDS:
        errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID)
    if {key for key, value in normalized.items() if value.get("consumer_class") == "positive-derivation"} != POSITIVE_CONSUMER_IDS:
        errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID)
    for value in normalized.values():
        if (
            not set(value.get("stable_surface_ids") or ()) <= STABLE_SURFACE_IDS
            or value.get("moving_consumed_surface_ids")
            or not set(value.get("moving_probe_surface_ids") or ()) <= MOVING_SURFACE_IDS
        ):
            errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_MAP_INVALID)

    current: set[str] = set()
    for path in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(path)
        if metadata and metadata.get("Status") == "Accepted" and "OCP-005" in _refs(metadata.get("Depends-On")):
            current.add(str(metadata.get("Document-ID")))
    if current != CONSUMER_IDS:
        errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_INVENTORY_DRIFT)
    subject = _frontmatter(repo_root / EXPECTED_SUBJECT["primary"])
    if not subject or any(
        str(subject.get(field)) != str(expected)
        for field, expected in (("Document-ID", "OCP-005"), ("Version", "0.3.0"), ("Status", "Draft"), ("Concept-Status", "Accepted"))
    ):
        errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_INVENTORY_DRIFT)

    for consumer_id, consumer in normalized.items():
        try:
            text = (repo_root / consumer["primary"]).read_text(encoding="utf-8")
        except OSError:
            text = ""
        if any(token not in text for token in consumer["consumed_tokens"]):
            errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_TEXT_DRIFT)
        try:
            observed = _probe(repo_root, consumer_id, consumer)
        except (KeyError, IndexError, TypeError, ValueError):
            observed = None
        if observed != (consumer["expected_control"], consumer["expected_probe"]):
            errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_PROBE_DRIFT)

    try:
        surface = yaml.safe_load((repo_root / "architecture/assignment-stable-surface.yaml").read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        surface = None
    if not isinstance(surface, dict):
        errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_PROJECTION_DRIFT)
    else:
        stable_ids = {item.get("surface_id") for item in surface.get("stable_candidates") or [] if isinstance(item, dict)}
        moving_ids = {item.get("surface_id") for item in surface.get("moving_surfaces") or [] if isinstance(item, dict)}
        blockers = {item.get("blocker_id") for item in surface.get("blockers") or [] if isinstance(item, dict)}
        accepted = {
            item.get("document_id") for item in surface.get("direct_consumers") or []
            if isinstance(item, dict) and item.get("lifecycle_class") == "accepted"
        }
        if (
            stable_ids != STABLE_SURFACE_IDS or moving_ids != MOVING_SURFACE_IDS
            or blockers != REMAINING_BLOCKER_IDS or "ACCEPTED_CONSUMER_COMPATIBILITY_UNPROVEN" in blockers
            or accepted != CONSUMER_IDS
        ):
            errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_PROJECTION_DRIFT)

    try:
        gate = yaml.safe_load((repo_root / "architecture/foundation-promotion-gate.yaml").read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        gate = None
    cycles = gate.get("cycles") if isinstance(gate, dict) else None
    completed = [
        item.get("cycle_id") for item in cycles or [] if isinstance(item, dict)
        and isinstance(item.get("steps"), dict) and set(item["steps"].values()) == {"completed"}
    ]
    protocol = gate.get("cycle_protocol") if isinstance(gate, dict) else None
    if (
        not isinstance(gate, dict) or gate.get("schema_version") != 5 or completed != ["EVENT_T6"]
        or not isinstance(protocol, dict) or protocol.get("active_cycle_id") is not None
    ):
        errors.append(ASSIGNMENT_CONSUMER_COMPATIBILITY_GATE_DRIFT)
    return _result(errors)
