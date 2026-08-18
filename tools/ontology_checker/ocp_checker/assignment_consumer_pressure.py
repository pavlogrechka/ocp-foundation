from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

from ._common import nonempty, parse_time, result
from .checker import ValidationResult


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

BASELINE = "6099a1ce042624b86fb4289f75d396a53fa9addb"
CONSUMER_REF = "OCP-023@0.2.0"
NEED_ID = "RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS"
NEED_TOKEN = "assignment_set_complete_for_resource(resource_ref, evaluation_time, snapshot_ref)"
LIVE_CLASSIFICATION = "undecidable-from-inside"
SIGNATURE_EFFECT = "preserved"
ABSENT_AUTHORITY = "absent"

BLOCKER_QUESTIONS = {
    "AMENDMENT_MODEL_ABSENT": ("Q2",),
    "TEMPORAL_MODEL_UNRESOLVED": ("Q3", "Q9"),
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
BLOCKER_REASONS = {
    "AMENDMENT_MODEL_ABSENT": "every-amendment-representation-can-bind-the-same-resource-time-snapshot-need-but-none-supplies-real-set-completeness",
    "TEMPORAL_MODEL_UNRESOLVED": "every-retroactivity-interval-combination-can-bind-a-snapshot-but-only-an-external-coverage-source-can-prove-that-later-or-omitted-records-do-not-exist",
    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": "whole-resource-explicit-scope-and-part-identity-forms-can-each-name-a-resource-bound-snapshot-but-none-proves-coverage",
}
EXPECTED_GATE_FIRST = {
    "ocp016_gate": "G4",
    "applies": False,
    "reason": "discovery-classification-does-not-create-a-positive-capable-rule-result-profile-or-activation",
    "hypothetical_activation_still_requires_g4": True,
}
EXPECTED_CRITERION = {
    "pressured": "at-least-one-resolution-cannot-satisfy-the-need-while-another-can",
    "neutral": "every-resolution-satisfies-the-need-on-live-inputs",
    "undecidable-from-inside": "satisfaction-test-requires-a-real-completeness-authority-or-coverage-observation-absent-from-the-repository",
    "negative_proof_rule": "enumerate-every-resolution-and-show-no-repository-input-selects-exactly-one",
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
        "stored_signature_effect",
        "stored_classification",
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
    signature_effect: str | None
    classification: str | None


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


def derive_assignment_consumer_pressure(probe: Any) -> AssignmentConsumerPressureResult:
    if not _probe_shape_valid(probe) or _contains_named(probe, FORBIDDEN_FIELDS):
        return AssignmentConsumerPressureResult(None, None)
    blocker = str(probe["blocker_id"])
    resolution = str(probe["resolution_id"])
    if blocker not in BLOCKER_SOLUTIONS or resolution not in BLOCKER_SOLUTIONS[blocker]:
        return AssignmentConsumerPressureResult(None, None)
    if tuple(probe["question_ids"]) != BLOCKER_QUESTIONS[blocker]:
        return AssignmentConsumerPressureResult(None, None)
    if (
        probe.get("accepted_consumer_ref") != CONSUMER_REF
        or probe.get("consumer_need_id") != NEED_ID
        or probe.get("consumer_need_token") != NEED_TOKEN
    ):
        return AssignmentConsumerPressureResult(None, None)
    if probe.get("completeness_authority_ref") is not None:
        return AssignmentConsumerPressureResult(SIGNATURE_EFFECT, None)
    if probe.get("completeness_authority_state") != ABSENT_AUTHORITY:
        return AssignmentConsumerPressureResult(SIGNATURE_EFFECT, None)
    return AssignmentConsumerPressureResult(SIGNATURE_EFFECT, LIVE_CLASSIFICATION)


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
        probe.get("stored_signature_effect") != derived.signature_effect
        or probe.get("stored_classification") != derived.classification
    ):
        errors.append(ASSIGNMENT_PRESSURE_RESULT_MISMATCH)
    return result(errors)


def validate_assignment_consumer_pressure_fixture(fixture: Any) -> ValidationResult:
    if not isinstance(fixture, dict) or fixture.get("concept") != "AssignmentConsumerPressureProbe":
        return result((ASSIGNMENT_PRESSURE_FIXTURE_INVALID,))
    return validate_assignment_consumer_pressure_probe(fixture.get("probe"))


def _load_yaml(repo_root: Path, relative: Path) -> Any:
    return yaml.safe_load((repo_root / relative).read_text(encoding="utf-8"))


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
    ):
        errors.append(ASSIGNMENT_PRESSURE_MAP_INVALID)

    live_blockers = {
        item.get("blocker_id"): tuple(item.get("question_ids") or ())
        for item in (surface.get("blockers") if isinstance(surface, dict) else [])
        if item.get("disposition") == "blocks-whole-document-freeze"
    }
    if live_blockers != BLOCKER_QUESTIONS:
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
                        "need_signature_effect": SIGNATURE_EFFECT,
                        "live_satisfaction": LIVE_CLASSIFICATION,
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

    results = payload.get("blocker_results") if isinstance(payload, dict) else None
    result_map = {item.get("blocker_id"): item for item in results or [] if isinstance(item, dict)}
    expected_results = []
    for blocker, resolutions in BLOCKER_SOLUTIONS.items():
        expected_results.append(
            {
                "blocker_id": blocker,
                "question_ids": list(BLOCKER_QUESTIONS[blocker]),
                "classification": LIVE_CLASSIFICATION,
                "structural_signature_effect": "preserved-by-all-resolutions",
                "reason": BLOCKER_REASONS[blocker],
                "resolution_ids": list(resolutions),
            }
        )
        item = result_map.get(blocker, {})
        if (
            item.get("question_ids") != list(BLOCKER_QUESTIONS[blocker])
            or item.get("classification") != LIVE_CLASSIFICATION
            or item.get("structural_signature_effect") != "preserved-by-all-resolutions"
            or item.get("reason") != BLOCKER_REASONS[blocker]
            or item.get("resolution_ids") != list(resolutions)
        ):
            errors.append(ASSIGNMENT_PRESSURE_PROBE_DRIFT)
    if results != expected_results:
        errors.append(ASSIGNMENT_PRESSURE_PROBE_DRIFT)

    guard = payload.get("promotion_gate_guard") if isinstance(payload, dict) else None
    cycle_protocol = gate.get("cycle_protocol") if isinstance(gate, dict) else None
    if (
        guard != {"schema_version": 5, "completed_cycle_ids": ["EVENT_T6"], "active_cycle_id": None}
        or gate.get("schema_version") != 5
        or not isinstance(cycle_protocol, dict)
        or cycle_protocol.get("active_cycle_id") is not None
        or [
            item.get("cycle_id") for item in gate.get("cycles", [])
            if isinstance(item.get("steps"), dict)
            and set(item["steps"].values()) == {"completed"}
        ] != ["EVENT_T6"]
    ):
        errors.append(ASSIGNMENT_PRESSURE_GATE_DRIFT)
    return _map_result(errors)
