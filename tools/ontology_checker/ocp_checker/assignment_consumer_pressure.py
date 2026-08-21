from __future__ import annotations

import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

from ._common import nonempty, parse_time, result
from .checker import ValidationResult
from .resource_occupancy import derive_resource_occupancy, validate_resource_occupancy_dataset
from .foundation_promotion_gate import promotion_gate_guard_is_current


ASSIGNMENT_PRESSURE_MAP_INVALID = "ASSIGNMENT_PRESSURE_MAP_INVALID"
ASSIGNMENT_PRESSURE_BLOCKER_DRIFT = "ASSIGNMENT_PRESSURE_BLOCKER_DRIFT"
ASSIGNMENT_PRESSURE_CONSUMER_NEED_DRIFT = "ASSIGNMENT_PRESSURE_CONSUMER_NEED_DRIFT"
ASSIGNMENT_PRESSURE_PROBE_DRIFT = "ASSIGNMENT_PRESSURE_PROBE_DRIFT"
ASSIGNMENT_PRESSURE_GATE_DRIFT = "ASSIGNMENT_PRESSURE_GATE_DRIFT"

ASSIGNMENT_PRESSURE_FIXTURE_INVALID = "ASSIGNMENT_PRESSURE_FIXTURE_INVALID"
ASSIGNMENT_PRESSURE_BLOCKER_INVALID = "ASSIGNMENT_PRESSURE_BLOCKER_INVALID"
ASSIGNMENT_PRESSURE_RESOLUTION_INVALID = "ASSIGNMENT_PRESSURE_RESOLUTION_INVALID"
ASSIGNMENT_PRESSURE_NEED_BINDING_INVALID = "ASSIGNMENT_PRESSURE_NEED_BINDING_INVALID"
ASSIGNMENT_PRESSURE_SELF_SUPPLY_FORBIDDEN = "ASSIGNMENT_PRESSURE_SELF_SUPPLY_FORBIDDEN"
ASSIGNMENT_PRESSURE_FORBIDDEN_OUTCOME = "ASSIGNMENT_PRESSURE_FORBIDDEN_OUTCOME"
ASSIGNMENT_PRESSURE_RESULT_MISMATCH = "ASSIGNMENT_PRESSURE_RESULT_MISMATCH"

ASSIGNMENT_PRESSURE_ERROR_CODES = frozenset(
    {
        ASSIGNMENT_PRESSURE_FIXTURE_INVALID,
        ASSIGNMENT_PRESSURE_BLOCKER_INVALID,
        ASSIGNMENT_PRESSURE_RESOLUTION_INVALID,
        ASSIGNMENT_PRESSURE_NEED_BINDING_INVALID,
        ASSIGNMENT_PRESSURE_SELF_SUPPLY_FORBIDDEN,
        ASSIGNMENT_PRESSURE_FORBIDDEN_OUTCOME,
        ASSIGNMENT_PRESSURE_RESULT_MISMATCH,
    }
)

MAP_PATH = Path("architecture/assignment-consumer-pressure.yaml")
SURFACE_PATH = Path("architecture/assignment-stable-surface.yaml")
NEED_PATH = Path("architecture/consumer-need-discovery.yaml")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
FIXTURE_ROOT = Path("tools/ontology_checker/fixtures/assignment_consumer_pressure")
OCCUPANCY_FIXTURE_ROOT = Path("tools/ontology_checker/fixtures/resource_occupancy")

BASELINE = "6099a1ce042624b86fb4289f75d396a53fa9addb"
CONSUMER_REF = "OCP-023@0.2.0"
NEED_ID = "RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS"
NEED_TOKEN = "assignment_set_complete_for_resource(resource_ref, evaluation_time, snapshot_ref)"
LIVE_SATISFACTION = "undecidable-from-inside"
PRESSURED_CLASSIFICATION = "pressured"
CURRENT_BINDINGS_ADEQUATE = "current-three-bindings-adequate"
OBSERVATION_CUT_REQUIRED = "additional-observation-cut-binding-required"
SCOPE_CLOSURE_REQUIRED = "additional-part-whole-closure-binding-required"
ABSENT_AUTHORITY = "absent"

BLOCKER_QUESTIONS = {
    "AMENDMENT_MODEL_ABSENT": ("Q2",),
    "TEMPORAL_MODEL_UNRESOLVED": ("Q3", "Q9"),
    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": ("Q5",),
}
CURRENT_BLOCKER_QUESTIONS = {
    "AMENDMENT_MODEL_ABSENT": ("Q2",),
    "TEMPORAL_MODEL_UNRESOLVED": ("Q9",),
    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": ("Q5",),
}
BLOCKER_SOLUTIONS = {
    "AMENDMENT_MODEL_ABSENT": (
        "IN_PLACE_TRACEABLE_AMENDMENT",
        "SUPERSEDING_ASSIGNMENT_FOR_CHANGE",
        "POST_ESTABLISHMENT_IMMUTABILITY",
    ),
    "TEMPORAL_MODEL_UNRESOLVED": (
        "PROSPECTIVE_ONLY_SINGLE_INTERVAL",
        "PROSPECTIVE_ONLY_MULTIPLE_INTERVALS",
        "RETROACTIVE_ALLOWED_SINGLE_INTERVAL",
        "RETROACTIVE_ALLOWED_MULTIPLE_INTERVALS",
    ),
    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": (
        "WHOLE_RESOURCE_ONLY",
        "EXPLICIT_PART_SCOPE_ON_ASSIGNMENT",
        "PART_AS_RESOURCE_IDENTITY",
    ),
}
RESOLUTION_DETAILS = {
    "IN_PLACE_TRACEABLE_AMENDMENT": ("same-assignment-identity-with-attributable-versioned-change", "pressure-q2-in-place.yaml"),
    "SUPERSEDING_ASSIGNMENT_FOR_CHANGE": ("new-assignment-identity-linked-to-predecessor", "pressure-q2-superseding.yaml"),
    "POST_ESTABLISHMENT_IMMUTABILITY": ("change-forbidden-after-establishment", "pressure-q2-immutable.yaml"),
    "PROSPECTIVE_ONLY_SINGLE_INTERVAL": ("no-retroactivity-and-one-interval", "pressure-temporal-prospective-single.yaml"),
    "PROSPECTIVE_ONLY_MULTIPLE_INTERVALS": ("no-retroactivity-and-many-intervals", "pressure-temporal-prospective-multiple.yaml"),
    "RETROACTIVE_ALLOWED_SINGLE_INTERVAL": ("retroactivity-and-one-interval", "pressure-temporal-retroactive-single.yaml"),
    "RETROACTIVE_ALLOWED_MULTIPLE_INTERVALS": ("retroactivity-and-many-intervals", "pressure-temporal-retroactive-multiple.yaml"),
    "WHOLE_RESOURCE_ONLY": ("assignment-subject-is-whole-resource", "pressure-q5-whole-resource.yaml"),
    "EXPLICIT_PART_SCOPE_ON_ASSIGNMENT": ("assignment-adds-part-scope-under-resource-reference", "pressure-q5-explicit-scope.yaml"),
    "PART_AS_RESOURCE_IDENTITY": ("part-receives-own-resource-identity", "pressure-q5-part-identity.yaml"),
}
RESOLUTION_ADEQUACY = {
    "IN_PLACE_TRACEABLE_AMENDMENT": OBSERVATION_CUT_REQUIRED,
    "SUPERSEDING_ASSIGNMENT_FOR_CHANGE": CURRENT_BINDINGS_ADEQUATE,
    "POST_ESTABLISHMENT_IMMUTABILITY": CURRENT_BINDINGS_ADEQUATE,
    "PROSPECTIVE_ONLY_SINGLE_INTERVAL": CURRENT_BINDINGS_ADEQUATE,
    "PROSPECTIVE_ONLY_MULTIPLE_INTERVALS": CURRENT_BINDINGS_ADEQUATE,
    "RETROACTIVE_ALLOWED_SINGLE_INTERVAL": OBSERVATION_CUT_REQUIRED,
    "RETROACTIVE_ALLOWED_MULTIPLE_INTERVALS": OBSERVATION_CUT_REQUIRED,
    "WHOLE_RESOURCE_ONLY": CURRENT_BINDINGS_ADEQUATE,
    "EXPLICIT_PART_SCOPE_ON_ASSIGNMENT": CURRENT_BINDINGS_ADEQUATE,
    "PART_AS_RESOURCE_IDENTITY": SCOPE_CLOSURE_REQUIRED,
}
RESOLUTION_EVIDENCE_MODES = {
    resolution: (
        "analytic" if resolution == "POST_ESTABLISHMENT_IMMUTABILITY" else "observed"
    )
    for resolution in RESOLUTION_ADEQUACY
}
EXPECTED_BLOCKER_CLASSIFICATIONS = {
    "AMENDMENT_MODEL_ABSENT": "pressured",
    "TEMPORAL_MODEL_UNRESOLVED": "pressured",
    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": "pressured",
}
BLOCKER_ADEQUACY_SUMMARIES = {
    "AMENDMENT_MODEL_ABSENT": "current-bindings-adequate-except-in-place-amendment",
    "TEMPORAL_MODEL_UNRESOLVED": "current-bindings-adequate-only-for-prospective-resolutions",
    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": "current-bindings-adequate-except-part-as-resource-identity",
}
BLOCKER_REASONS = {
    "AMENDMENT_MODEL_ABSENT": "in-place-amendment-requires-an-observation-cut-binding-that-the-current-signature-does-not-carry",
    "TEMPORAL_MODEL_UNRESOLVED": "retroactive-resolutions-require-an-observation-cut-binding-that-the-current-signature-does-not-carry",
    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": "part-as-resource-identity-requires-part-whole-closure-that-the-current-signature-does-not-carry",
}
EXPECTED_GATE_FIRST = {
    "ocp016_gate": "G4",
    "applies": False,
    "reason": "discovery-classification-does-not-create-a-positive-capable-rule-result-profile-or-activation",
    "hypothetical_activation_still_requires_g4": True,
}
EXPECTED_CRITERION = {
    "pressured": "declared-need-bindings-are-adequate-for-some-but-not-all-resolutions",
    "neutral": "declared-need-bindings-are-adequate-and-live-satisfaction-is-proven-for-every-resolution",
    "undecidable-from-inside": "no-resolution-dependent-adequacy-difference-and-live-satisfaction-requires-missing-external-input",
    "negative_proof_rule": "enumerate-every-resolution-and-derive-adequacy-before-testing-live-satisfaction",
}
EXPECTED_MISSING_INPUTS = [
    "legitimate-completeness-owner-evaluator",
    "externally-grounded-all-assignments-coverage-observation",
    "activation-baseline-rule-snapshot-context-binding",
]
EXPECTED_CONSUMER = {
    "accepted_consumer_ref": CONSUMER_REF,
    "need_id": NEED_ID,
    "token": NEED_TOKEN,
    "real_completeness_authority_available": False,
    "current_disposition": "unmet-positive-consumer-need",
}
PROBE_FIELDS = frozenset(
    {
        "probe_id",
        "accepted_consumer_ref",
        "consumer_need_id",
        "consumer_need_token",
        "blocker_id",
        "question_ids",
        "resolution_id",
        "resource_ref",
        "evaluation_time",
        "snapshot_ref",
        "completeness_authority_state",
        "completeness_authority_ref",
        "stored_adequacy_effect",
        "stored_live_satisfaction",
        "stored_blocker_classification",
    }
)
FORBIDDEN_FIELDS = frozenset(
    {
        "selected_resolution",
        "blocker_removed",
        "question_resolved",
        "activation_state",
        "promotion_cycle_id",
        "concept_status",
        "assignment_rule",
    }
)
FORBIDDEN_OUTCOMES = frozenset(
    {
        "BLOCKER_REMOVAL",
        "OPEN_QUESTION_RESOLUTION",
        "ASSIGNMENT_RULE_SELECTION",
        "POSITIVE_MODEL_ACTIVATION",
        "OCP005_CHANGE",
        "CONCEPT_OR_GRAPH_CHANGE",
        "PROMOTION_CYCLE_START",
        "NEXT_ACT_AUTHORIZATION",
    }
)


@dataclass(frozen=True)
class AssignmentConsumerPressureResult:
    adequacy_effect: str | None
    live_satisfaction: str | None
    blocker_classification: str | None


@dataclass(frozen=True)
class AssignmentConsumerPressureMapResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _map_result(errors: Iterable[str]) -> AssignmentConsumerPressureMapResult:
    return AssignmentConsumerPressureMapResult(tuple(dict.fromkeys(errors)))


def _text(value: Any) -> str | None:
    return str(value).strip() if nonempty(value) else None


def _contains_named(value: Any, names: frozenset[str]) -> bool:
    if isinstance(value, dict):
        return any(key in names or _contains_named(item, names) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_named(item, names) for item in value)
    return False


def _probe_shape_valid(probe: Any) -> bool:
    return bool(
        isinstance(probe, dict)
        and set(probe) == PROBE_FIELDS
        and all(
            _text(probe.get(field))
            for field in PROBE_FIELDS - {"completeness_authority_ref", "question_ids"}
        )
        and isinstance(probe.get("question_ids"), list)
        and all(_text(item) for item in probe.get("question_ids"))
        and parse_time(probe.get("evaluation_time")) is not None
    )


def _derive_blocker_classification(blocker: str) -> str | None:
    resolutions = BLOCKER_SOLUTIONS.get(blocker)
    if not resolutions:
        return None
    effects = {RESOLUTION_ADEQUACY.get(resolution) for resolution in resolutions}
    if None in effects:
        return None
    if len(effects) > 1:
        return PRESSURED_CLASSIFICATION
    if effects == {CURRENT_BINDINGS_ADEQUATE}:
        return LIVE_SATISFACTION
    return None


def derive_assignment_consumer_pressure(probe: Any) -> AssignmentConsumerPressureResult:
    if not _probe_shape_valid(probe) or _contains_named(probe, FORBIDDEN_FIELDS):
        return AssignmentConsumerPressureResult(None, None, None)
    blocker = str(probe["blocker_id"])
    resolution = str(probe["resolution_id"])
    if blocker not in BLOCKER_SOLUTIONS or resolution not in BLOCKER_SOLUTIONS[blocker]:
        return AssignmentConsumerPressureResult(None, None, None)
    if tuple(probe["question_ids"]) != BLOCKER_QUESTIONS[blocker]:
        return AssignmentConsumerPressureResult(None, None, None)
    if (
        probe.get("accepted_consumer_ref") != CONSUMER_REF
        or probe.get("consumer_need_id") != NEED_ID
        or probe.get("consumer_need_token") != NEED_TOKEN
    ):
        return AssignmentConsumerPressureResult(None, None, None)
    adequacy = RESOLUTION_ADEQUACY.get(resolution)
    classification = _derive_blocker_classification(blocker)
    if adequacy is None or classification is None:
        return AssignmentConsumerPressureResult(None, None, None)
    if probe.get("completeness_authority_ref") is not None:
        return AssignmentConsumerPressureResult(adequacy, None, classification)
    if probe.get("completeness_authority_state") != ABSENT_AUTHORITY:
        return AssignmentConsumerPressureResult(adequacy, None, classification)
    return AssignmentConsumerPressureResult(adequacy, LIVE_SATISFACTION, classification)


def validate_assignment_consumer_pressure_probe(probe: Any) -> ValidationResult:
    errors: list[str] = []
    if _contains_named(probe, FORBIDDEN_FIELDS):
        errors.append(ASSIGNMENT_PRESSURE_FORBIDDEN_OUTCOME)
    if not _probe_shape_valid(probe):
        errors.append(ASSIGNMENT_PRESSURE_FIXTURE_INVALID)
        return result(errors)
    blocker = str(probe.get("blocker_id"))
    resolution = str(probe.get("resolution_id"))
    if blocker not in BLOCKER_QUESTIONS or tuple(probe.get("question_ids") or ()) != BLOCKER_QUESTIONS.get(blocker):
        errors.append(ASSIGNMENT_PRESSURE_BLOCKER_INVALID)
    if blocker not in BLOCKER_SOLUTIONS or resolution not in BLOCKER_SOLUTIONS.get(blocker, ()):
        errors.append(ASSIGNMENT_PRESSURE_RESOLUTION_INVALID)
    if (
        probe.get("accepted_consumer_ref") != CONSUMER_REF
        or probe.get("consumer_need_id") != NEED_ID
        or probe.get("consumer_need_token") != NEED_TOKEN
    ):
        errors.append(ASSIGNMENT_PRESSURE_NEED_BINDING_INVALID)
    if probe.get("completeness_authority_ref") is not None or probe.get("completeness_authority_state") != ABSENT_AUTHORITY:
        errors.append(ASSIGNMENT_PRESSURE_SELF_SUPPLY_FORBIDDEN)
    derived = derive_assignment_consumer_pressure(probe)
    if (
        probe.get("stored_adequacy_effect") != derived.adequacy_effect
        or probe.get("stored_live_satisfaction") != derived.live_satisfaction
        or probe.get("stored_blocker_classification") != derived.blocker_classification
    ):
        errors.append(ASSIGNMENT_PRESSURE_RESULT_MISMATCH)
    return result(errors)


def validate_assignment_consumer_pressure_fixture(fixture: Any) -> ValidationResult:
    if not isinstance(fixture, dict) or fixture.get("concept") != "AssignmentConsumerPressureProbe":
        return result((ASSIGNMENT_PRESSURE_FIXTURE_INVALID,))
    return validate_assignment_consumer_pressure_probe(fixture.get("probe"))


def _load_yaml(repo_root: Path, relative: Path) -> Any:
    return yaml.safe_load((repo_root / relative).read_text(encoding="utf-8"))


def _scope_adequacy(
    candidate: dict[str, Any], whole_bound_twin: dict[str, Any]
) -> str | None:
    candidate_valid = validate_resource_occupancy_dataset(candidate).valid
    candidate_result = derive_resource_occupancy(candidate).occupied
    if candidate_valid and candidate_result is not None:
        return CURRENT_BINDINGS_ADEQUATE
    twin_valid = validate_resource_occupancy_dataset(whole_bound_twin).valid
    twin_result = derive_resource_occupancy(whole_bound_twin).occupied
    if not candidate_valid and candidate_result is None and twin_valid and twin_result is not None:
        return SCOPE_CLOSURE_REQUIRED
    return None


def _derive_live_adequacy_evidence(repo_root: Path) -> dict[str, str] | None:
    try:
        control = _load_yaml(repo_root, OCCUPANCY_FIXTURE_ROOT / "valid-one-effective.yaml")["dataset"]
        empty = _load_yaml(repo_root, OCCUPANCY_FIXTURE_ROOT / "valid-zero-assignments.yaml")["dataset"]
        overlapping = _load_yaml(repo_root, OCCUPANCY_FIXTURE_ROOT / "valid-two-overlapping.yaml")["dataset"]
    except (KeyError, OSError, TypeError, yaml.YAMLError):
        return None

    def assignments(dataset: dict[str, Any]) -> list[dict[str, Any]]:
        return dataset["assignment_snapshots"][0]["assignments"]

    def retained_pre_change_payload(before: dict[str, Any], after: dict[str, Any]) -> bool:
        fields = (
            "assignment_id",
            "resource_ref",
            "operation_ref",
            "role_specification",
            "applicability_start",
            "applicability_end",
        )
        before_payloads = {
            tuple(yaml.safe_dump(item.get(field), sort_keys=True) for field in fields)
            for item in assignments(before)
        }
        after_payloads = {
            tuple(yaml.safe_dump(item.get(field), sort_keys=True) for field in fields)
            for item in assignments(after)
        }
        return bool(before_payloads) and before_payloads <= after_payloads

    def change_adequacy(before: dict[str, Any], after: dict[str, Any]) -> str | None:
        if not (
            validate_resource_occupancy_dataset(before).valid
            and validate_resource_occupancy_dataset(after).valid
        ):
            return None
        before_result = derive_resource_occupancy(before).occupied
        after_result = derive_resource_occupancy(after).occupied
        if before_result == after_result or retained_pre_change_payload(before, after):
            return CURRENT_BINDINGS_ADEQUATE
        return OBSERVATION_CUT_REQUIRED

    def late_assignment(template: dict[str, Any], suffix: str, established_at: str) -> dict[str, Any]:
        item = copy.deepcopy(template)
        item.update(
            {
                "assignment_id": f"A-LATE-{suffix}",
                "applicability_end": "2026-08-02T13:00:00Z",
                "created_at": "2026-08-02T11:50:00Z",
                "established_at": established_at,
                "provenance_ref": f"SYNTH-LATE-{suffix}",
                "supersedes_assignment_ref": None,
            }
        )
        item["transition_history"][0].update(
            {
                "transition_id": f"AT-LATE-{suffix}",
                "assignment_ref": f"A-LATE-{suffix}",
                "occurred_at": established_at,
                "provenance_ref": f"SYNTH-LATE-{suffix}",
            }
        )
        return item

    in_place = copy.deepcopy(control)
    in_place["assignment_snapshots"][0]["assignments"][0]["applicability_end"] = "2026-08-02T10:30:00Z"
    in_place["occupancy_request"]["stored_occupied"] = False
    in_place["occupancy_request"]["stored_witness_assignment_refs"] = []

    superseding = copy.deepcopy(control)
    prior = superseding["assignment_snapshots"][0]["assignments"][0]
    prior["transition_history"].append(
        {
            "transition_id": "AT-OLD-TERM",
            "assignment_ref": "A-001",
            "from_stage": "Established",
            "to_stage": "Revoked",
            "occurred_at": "2026-08-02T10:30:00Z",
            "provenance_ref": "SYNTH-DECISION-TERM",
        }
    )
    prior["lifecycle_stage"] = "Revoked"
    prior["terminal_at"] = "2026-08-02T10:30:00Z"
    successor = copy.deepcopy(control["assignment_snapshots"][0]["assignments"][0])
    successor.update(
        {
            "assignment_id": "A-002",
            "applicability_end": "2026-08-02T10:30:00Z",
            "created_at": "2026-08-02T10:15:00Z",
            "established_at": "2026-08-02T10:20:00Z",
            "provenance_ref": "SYNTH-DECISION-002",
            "supersedes_assignment_ref": "A-001",
        }
    )
    successor["transition_history"][0].update(
        {
            "transition_id": "AT-002",
            "assignment_ref": "A-002",
            "occurred_at": "2026-08-02T10:20:00Z",
            "provenance_ref": "SYNTH-DECISION-002",
        }
    )
    superseding["assignment_snapshots"][0]["assignments"].append(successor)
    superseding["occupancy_request"]["stored_occupied"] = False
    superseding["occupancy_request"]["stored_witness_assignment_refs"] = []

    before_prospective = copy.deepcopy(empty)
    before_prospective["occupancy_request"]["evaluation_time"] = "2026-08-02T11:00:00Z"
    before_prospective["occupancy_request"]["assignment_snapshot_ref"] = "SYNTH-SNAPSHOT-PROSPECTIVE"
    before_prospective["assignment_snapshots"][0]["snapshot_ref"] = "SYNTH-SNAPSHOT-PROSPECTIVE"
    prospective_single = copy.deepcopy(before_prospective)
    prospective_single["assignment_snapshots"][0]["assignments"] = [
        late_assignment(control["assignment_snapshots"][0]["assignments"][0], "001", "2026-08-02T12:00:00Z")
    ]
    prospective_multiple = copy.deepcopy(before_prospective)
    prospective_multiple["assignment_snapshots"][0]["assignments"] = [
        late_assignment(overlapping["assignment_snapshots"][0]["assignments"][0], "001", "2026-08-02T12:00:00Z"),
        late_assignment(overlapping["assignment_snapshots"][0]["assignments"][1], "002", "2026-08-02T12:05:00Z"),
    ]

    before_retroactive = copy.deepcopy(empty)
    before_retroactive["occupancy_request"]["evaluation_time"] = "2026-08-02T11:00:00Z"
    before_retroactive["occupancy_request"]["assignment_snapshot_ref"] = "SYNTH-SNAPSHOT-RETRO"
    before_retroactive["assignment_snapshots"][0]["snapshot_ref"] = "SYNTH-SNAPSHOT-RETRO"
    after_retroactive = copy.deepcopy(before_retroactive)
    retroactive = copy.deepcopy(control["assignment_snapshots"][0]["assignments"][0])
    retroactive["assignment_id"] = "A-RETRO"
    retroactive["transition_history"][0]["transition_id"] = "AT-RETRO"
    retroactive["transition_history"][0]["assignment_ref"] = "A-RETRO"
    after_retroactive["assignment_snapshots"][0]["assignments"] = [retroactive]
    after_retroactive["occupancy_request"]["stored_occupied"] = True
    after_retroactive["occupancy_request"]["stored_witness_assignment_refs"] = ["A-RETRO"]

    before_retroactive_multiple = copy.deepcopy(before_retroactive)
    before_retroactive_multiple["occupancy_request"]["assignment_snapshot_ref"] = "SYNTH-SNAPSHOT-RETRO-MULTI"
    before_retroactive_multiple["assignment_snapshots"][0]["snapshot_ref"] = "SYNTH-SNAPSHOT-RETRO-MULTI"
    after_retroactive_multiple = copy.deepcopy(before_retroactive_multiple)
    retroactive_multiple = copy.deepcopy(overlapping["assignment_snapshots"][0]["assignments"])
    for index, item in enumerate(retroactive_multiple, start=1):
        item["assignment_id"] = f"A-RETRO-{index}"
        item["transition_history"][0]["transition_id"] = f"AT-RETRO-{index}"
        item["transition_history"][0]["assignment_ref"] = f"A-RETRO-{index}"
    after_retroactive_multiple["assignment_snapshots"][0]["assignments"] = retroactive_multiple
    after_retroactive_multiple["occupancy_request"]["stored_occupied"] = True
    after_retroactive_multiple["occupancy_request"]["stored_witness_assignment_refs"] = [
        "A-RETRO-1",
        "A-RETRO-2",
    ]

    whole_resource = copy.deepcopy(control)
    explicit_part_scope = copy.deepcopy(control)
    explicit_part_scope["assignment_snapshots"][0]["assignments"][0]["part_scope_ref"] = "R-001-PART-A"

    cross_bound_part = copy.deepcopy(control)
    cross_bound_part["assignment_snapshots"][0]["assignments"][0]["resource_ref"] = "R-001-PART-A"
    whole_bound_twin = copy.deepcopy(cross_bound_part)
    whole_bound_twin["assignment_snapshots"][0]["assignments"][0]["resource_ref"] = "R-001"

    valid_datasets = (
        control,
        in_place,
        superseding,
        before_prospective,
        prospective_single,
        prospective_multiple,
        before_retroactive,
        after_retroactive,
        before_retroactive_multiple,
        after_retroactive_multiple,
        whole_resource,
        explicit_part_scope,
        whole_bound_twin,
    )
    if not all(validate_resource_occupancy_dataset(item).valid for item in valid_datasets):
        return None
    evidence = {
        "IN_PLACE_TRACEABLE_AMENDMENT": change_adequacy(control, in_place),
        "SUPERSEDING_ASSIGNMENT_FOR_CHANGE": change_adequacy(control, superseding),
        "PROSPECTIVE_ONLY_SINGLE_INTERVAL": change_adequacy(before_prospective, prospective_single),
        "PROSPECTIVE_ONLY_MULTIPLE_INTERVALS": change_adequacy(before_prospective, prospective_multiple),
        "RETROACTIVE_ALLOWED_SINGLE_INTERVAL": change_adequacy(before_retroactive, after_retroactive),
        "RETROACTIVE_ALLOWED_MULTIPLE_INTERVALS": change_adequacy(
            before_retroactive_multiple, after_retroactive_multiple
        ),
        "WHOLE_RESOURCE_ONLY": _scope_adequacy(whole_resource, whole_resource),
        "EXPLICIT_PART_SCOPE_ON_ASSIGNMENT": _scope_adequacy(
            explicit_part_scope, explicit_part_scope
        ),
        "PART_AS_RESOURCE_IDENTITY": _scope_adequacy(cross_bound_part, whole_bound_twin),
    }
    return evidence if None not in evidence.values() else None


def validate_assignment_consumer_pressure(repo_root: Path) -> AssignmentConsumerPressureMapResult:
    errors: list[str] = []
    try:
        payload = _load_yaml(repo_root, MAP_PATH)
        surface = _load_yaml(repo_root, SURFACE_PATH)
        need = _load_yaml(repo_root, NEED_PATH)
        gate = _load_yaml(repo_root, GATE_PATH)
    except (OSError, yaml.YAMLError):
        return _map_result((ASSIGNMENT_PRESSURE_MAP_INVALID,))

    expected_keys = {
        "schema_version", "rule_owner", "baseline", "gate_first", "criterion",
        "consumer_need", "blocker_results", "resolution_inventory",
        "external_missing_inputs", "promotion_gate_guard", "forbidden_outcomes",
    }
    if (
        not isinstance(payload, dict)
        or set(payload) != expected_keys
        or payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-044"
        or payload.get("baseline") != BASELINE
        or payload.get("gate_first") != EXPECTED_GATE_FIRST
        or payload.get("criterion") != EXPECTED_CRITERION
        or payload.get("external_missing_inputs") != EXPECTED_MISSING_INPUTS
        or payload.get("forbidden_outcomes") != sorted(FORBIDDEN_OUTCOMES)
        or set(RESOLUTION_ADEQUACY.values())
        != {CURRENT_BINDINGS_ADEQUATE, OBSERVATION_CUT_REQUIRED, SCOPE_CLOSURE_REQUIRED}
    ):
        errors.append(ASSIGNMENT_PRESSURE_MAP_INVALID)

    live_blockers = {
        item.get("blocker_id"): tuple(item.get("question_ids") or ())
        for item in (surface.get("blockers") if isinstance(surface, dict) else [])
        if item.get("disposition") == "blocks-whole-document-freeze"
    }
    if live_blockers != CURRENT_BLOCKER_QUESTIONS:
        errors.append(ASSIGNMENT_PRESSURE_BLOCKER_DRIFT)

    current_needs = (
        need.get("current_result", {}).get("unmet_positive_needs")
        if isinstance(need, dict) else None
    )
    consumer = payload.get("consumer_need") if isinstance(payload, dict) else None
    if (
        current_needs != [NEED_ID]
        or consumer != EXPECTED_CONSUMER
    ):
        errors.append(ASSIGNMENT_PRESSURE_CONSUMER_NEED_DRIFT)

    inventory = payload.get("resolution_inventory") if isinstance(payload, dict) else None
    expected_pairs = {
        (blocker, resolution)
        for blocker, resolutions in BLOCKER_SOLUTIONS.items()
        for resolution in resolutions
    }
    expected_inventory = []
    try:
        for blocker, resolutions in BLOCKER_SOLUTIONS.items():
            for resolution in resolutions:
                visible_form, fixture_name = RESOLUTION_DETAILS[resolution]
                expected_inventory.append(
                    {
                        "blocker_id": blocker,
                        "question_ids": list(BLOCKER_QUESTIONS[blocker]),
                        "resolution_id": resolution,
                        "externally_visible_form": visible_form,
                        "need_adequacy_effect": RESOLUTION_ADEQUACY[resolution],
                        "evidence_mode": RESOLUTION_EVIDENCE_MODES[resolution],
                        "live_satisfaction": LIVE_SATISFACTION,
                        "blocker_classification": _derive_blocker_classification(blocker),
                        "probe_fixture": fixture_name,
                    }
                )
    except (KeyError, TypeError, ValueError):
        errors.append(ASSIGNMENT_PRESSURE_PROBE_DRIFT)
    fixture_pairs: set[tuple[str, str]] = set()
    try:
        for fpath in sorted((repo_root / FIXTURE_ROOT).glob("*.yaml")):
            fixture = yaml.safe_load(fpath.read_text(encoding="utf-8"))
            validation = validate_assignment_consumer_pressure_fixture(fixture)
            if not validation.valid:
                errors.append(ASSIGNMENT_PRESSURE_PROBE_DRIFT)
            probe = fixture.get("probe") if isinstance(fixture, dict) else {}
            fixture_pairs.add((probe.get("blocker_id"), probe.get("resolution_id")))
    except (OSError, yaml.YAMLError):
        errors.append(ASSIGNMENT_PRESSURE_PROBE_DRIFT)
    if inventory != expected_inventory or fixture_pairs != expected_pairs:
        errors.append(ASSIGNMENT_PRESSURE_PROBE_DRIFT)
    observed_adequacy = {
        resolution: adequacy
        for resolution, adequacy in RESOLUTION_ADEQUACY.items()
        if RESOLUTION_EVIDENCE_MODES[resolution] == "observed"
    }
    if (
        set(RESOLUTION_EVIDENCE_MODES.values()) != {"observed", "analytic"}
        or [
            resolution
            for resolution, mode in RESOLUTION_EVIDENCE_MODES.items()
            if mode == "analytic"
        ] != ["POST_ESTABLISHMENT_IMMUTABILITY"]
        or _derive_live_adequacy_evidence(repo_root) != observed_adequacy
    ):
        errors.append(ASSIGNMENT_PRESSURE_PROBE_DRIFT)

    results = payload.get("blocker_results") if isinstance(payload, dict) else None
    result_map = {item.get("blocker_id"): item for item in results or [] if isinstance(item, dict)}
    expected_results = []
    for blocker, resolutions in BLOCKER_SOLUTIONS.items():
        expected_results.append(
            {
                "blocker_id": blocker,
                "question_ids": list(BLOCKER_QUESTIONS[blocker]),
                "classification": _derive_blocker_classification(blocker),
                "need_adequacy_effect": BLOCKER_ADEQUACY_SUMMARIES[blocker],
                "reason": BLOCKER_REASONS[blocker],
                "resolution_ids": list(resolutions),
            }
        )
        item = result_map.get(blocker, {})
        if (
            item.get("question_ids") != list(BLOCKER_QUESTIONS[blocker])
            or item.get("classification") != _derive_blocker_classification(blocker)
            or item.get("need_adequacy_effect") != BLOCKER_ADEQUACY_SUMMARIES[blocker]
            or item.get("reason") != BLOCKER_REASONS[blocker]
            or item.get("resolution_ids") != list(resolutions)
        ):
            errors.append(ASSIGNMENT_PRESSURE_PROBE_DRIFT)
    if results != expected_results:
        errors.append(ASSIGNMENT_PRESSURE_PROBE_DRIFT)
    if {
        blocker: _derive_blocker_classification(blocker)
        for blocker in BLOCKER_SOLUTIONS
    } != EXPECTED_BLOCKER_CLASSIFICATIONS:
        errors.append(ASSIGNMENT_PRESSURE_PROBE_DRIFT)

    guard = payload.get("promotion_gate_guard") if isinstance(payload, dict) else None
    cycle_protocol = gate.get("cycle_protocol") if isinstance(gate, dict) else None
    if (
        set(guard or {}) != {"schema_version", "completed_cycle_ids", "active_cycle_id"}
        or not isinstance(cycle_protocol, dict)
        or not promotion_gate_guard_is_current(gate, guard)
    ):
        errors.append(ASSIGNMENT_PRESSURE_GATE_DRIFT)
    return _map_result(errors)
