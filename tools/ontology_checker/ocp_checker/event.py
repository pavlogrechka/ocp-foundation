from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .checker import (
    ValidationResult,
    validate_assignment,
    validate_constraint,
    validate_operation,
    validate_resource,
)
from .objective import validate_objective


EVENT_ERROR_CODES = frozenset(
    {
        "EVENT_ID_REQUIRED",
        "EVENT_IDENTITY_DUPLICATE",
        "EVENT_KIND_REF_REQUIRED",
        "EVENT_OBSERVATION_COUPLING_FORBIDDEN",
        "EVENT_OCCURRED_AT_INVALID",
        "EVENT_PROVENANCE_REF_REQUIRED",
        "EVENT_REFERENCE_AMBIGUOUS",
        "EVENT_REFERENCE_INVALID",
        "EVENT_REFERENCE_UNRESOLVED",
        "EVENT_REGISTERED_AT_REQUIRED",
        "OBSERVATION_EVENT_REF_AMBIGUOUS",
        "OBSERVATION_EVENT_REF_UNRESOLVED",
        "OBSERVATION_ID_REQUIRED",
        "OBSERVATION_IDENTITY_DUPLICATE",
        "OBSERVATION_KIND_REF_REQUIRED",
        "OBSERVATION_OBSERVED_AT_REQUIRED",
        "OBSERVATION_OBSERVER_REQUIRED",
        "OBSERVATION_PROVENANCE_REF_REQUIRED",
        "OBSERVATION_RECORDED_AT_REQUIRED",
        "OBSERVATION_SELF_SUPERSESSION",
        "OBSERVATION_STATEMENT_REQUIRED",
        "OBSERVATION_SUPERSESSION_CYCLE",
        "OBSERVATION_SUPERSESSION_TARGET_UNRESOLVED",
        "OBSERVATION_TIME_ORDER_INVALID",
        "SCENARIO_ASSIGNMENT_INVALID",
        "SCENARIO_ASSESSMENT_INVALID",
        "SCENARIO_CONFLICTING_EVIDENCE_POSITIVE",
        "SCENARIO_CONSTRAINT_INVALID",
        "SCENARIO_EVENT_INVALID",
        "SCENARIO_EVIDENCE_REFERENCE_UNRESOLVED",
        "SCENARIO_OBJECTIVE_INVALID",
        "SCENARIO_OBSERVATION_INVALID",
        "SCENARIO_OPERATION_INVALID",
        "SCENARIO_RESOURCE_INVALID",
    }
)

EVENT_DERIVATION_RULES = frozenset({"resolve_event", "observations_for_event"})

FORBIDDEN_EVENT_KEYS = frozenset(
    {
        "observation",
        "observations",
        "observation_refs",
        "observer_ref",
        "source_count",
        "latest_observation_ref",
        "truth_status",
        "confidence",
        "achieved",
        "achievement_status",
        "assessment",
        "assessment_refs",
    }
)

POSITIVE_CONCLUSIONS = frozenset({"achieved", "partial"})
ASSESSMENT_CONCLUSIONS = frozenset(
    {"achieved", "not_achieved", "partial", "indeterminate"}
)


def _result(errors: Iterable[str]) -> ValidationResult:
    return ValidationResult(tuple(dict.fromkeys(errors)))


def _nonempty(value: Any) -> bool:
    return value is not None and bool(str(value).strip())


def _has_alnum(value: Any) -> bool:
    return isinstance(value, str) and any(char.isalnum() for char in value)


def _versioned_ref(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    subject, separator, version = value.strip().rpartition("@")
    return bool(separator and subject.strip() and version.strip())


def _parse_time(value: Any) -> datetime | None:
    if isinstance(value, datetime):
        parsed = value
    else:
        if not isinstance(value, str) or not value.strip():
            return None
        try:
            parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        except ValueError:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def validate_event(event: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []

    if not _nonempty(event.get("event_id")):
        errors.append("EVENT_ID_REQUIRED")
    if not _versioned_ref(event.get("event_kind_ref")):
        errors.append("EVENT_KIND_REF_REQUIRED")
    if _parse_time(event.get("registered_at")) is None:
        errors.append("EVENT_REGISTERED_AT_REQUIRED")
    if not _nonempty(event.get("identity_provenance_ref")):
        errors.append("EVENT_PROVENANCE_REF_REQUIRED")
    if "occurred_at" in event and _parse_time(event.get("occurred_at")) is None:
        errors.append("EVENT_OCCURRED_AT_INVALID")

    if any(
        key in event and event.get(key) not in (None, [], {}, "")
        for key in FORBIDDEN_EVENT_KEYS
    ):
        errors.append("EVENT_OBSERVATION_COUPLING_FORBIDDEN")

    return _result(errors)


def validate_event_dataset(events: Iterable[dict[str, Any]]) -> ValidationResult:
    errors: list[str] = []
    index: dict[str, list[dict[str, Any]]] = {}

    for event in events:
        if not isinstance(event, dict):
            errors.append("EVENT_REFERENCE_INVALID")
            continue
        errors.extend(validate_event(event).errors)
        event_id = event.get("event_id")
        if _nonempty(event_id):
            index.setdefault(str(event_id).strip(), []).append(event)

    if any(len(candidates) > 1 for candidates in index.values()):
        errors.append("EVENT_IDENTITY_DUPLICATE")

    return _result(errors)


def resolve_event(
    events: Iterable[dict[str, Any]], event_ref: Any
) -> dict[str, Any] | None:
    if not _nonempty(event_ref):
        return None
    requested = str(event_ref).strip()
    candidates = [
        event
        for event in events
        if isinstance(event, dict)
        and _nonempty(event.get("event_id"))
        and str(event.get("event_id")).strip() == requested
    ]
    if len(candidates) != 1:
        return None
    candidate = candidates[0]
    return candidate if validate_event(candidate).valid else None


def validate_observation(observation: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []

    if not _nonempty(observation.get("observation_id")):
        errors.append("OBSERVATION_ID_REQUIRED")
    if not _nonempty(observation.get("observer_ref")):
        errors.append("OBSERVATION_OBSERVER_REQUIRED")
    if not _versioned_ref(observation.get("observation_kind_ref")):
        errors.append("OBSERVATION_KIND_REF_REQUIRED")
    if not _has_alnum(observation.get("statement")):
        errors.append("OBSERVATION_STATEMENT_REQUIRED")

    observed_at = _parse_time(observation.get("observed_at"))
    recorded_at = _parse_time(observation.get("recorded_at"))
    if observed_at is None:
        errors.append("OBSERVATION_OBSERVED_AT_REQUIRED")
    if recorded_at is None:
        errors.append("OBSERVATION_RECORDED_AT_REQUIRED")
    if observed_at is not None and recorded_at is not None and observed_at > recorded_at:
        errors.append("OBSERVATION_TIME_ORDER_INVALID")
    if not _nonempty(observation.get("provenance_ref")):
        errors.append("OBSERVATION_PROVENANCE_REF_REQUIRED")

    observation_id = observation.get("observation_id")
    supersedes = observation.get("supersedes_observation_ref")
    if _nonempty(observation_id) and supersedes == observation_id:
        errors.append("OBSERVATION_SELF_SUPERSESSION")

    return _result(errors)


def _has_cycle(graph: dict[str, str]) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        target = graph.get(node)
        if target in graph and visit(str(target)):
            return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in sorted(graph))


def validate_observation_dataset(
    observations: Iterable[dict[str, Any]], events: Iterable[dict[str, Any]]
) -> ValidationResult:
    errors: list[str] = []
    observation_entries = list(observations)
    event_entries = list(events)
    observation_index: dict[str, list[dict[str, Any]]] = {}
    event_index: dict[str, list[dict[str, Any]]] = {}
    graph: dict[str, str] = {}

    for event in event_entries:
        if isinstance(event, dict) and _nonempty(event.get("event_id")):
            event_index.setdefault(str(event.get("event_id")).strip(), []).append(event)

    for observation in observation_entries:
        if not isinstance(observation, dict):
            errors.append("OBSERVATION_ID_REQUIRED")
            continue
        errors.extend(validate_observation(observation).errors)
        observation_id = observation.get("observation_id")
        if _nonempty(observation_id):
            normalized_id = str(observation_id).strip()
            observation_index.setdefault(normalized_id, []).append(observation)
            supersedes = observation.get("supersedes_observation_ref")
            if _nonempty(supersedes) and str(supersedes).strip() != normalized_id:
                graph[normalized_id] = str(supersedes).strip()

        if "event_ref" in observation and observation.get("event_ref") is not None:
            event_ref = observation.get("event_ref")
            if not _nonempty(event_ref):
                errors.append("EVENT_REFERENCE_INVALID")
            else:
                candidates = event_index.get(str(event_ref).strip(), [])
                if not candidates:
                    errors.append("OBSERVATION_EVENT_REF_UNRESOLVED")
                elif len(candidates) > 1:
                    errors.append("OBSERVATION_EVENT_REF_AMBIGUOUS")
                elif not validate_event(candidates[0]).valid:
                    errors.append("OBSERVATION_EVENT_REF_UNRESOLVED")

    if any(len(candidates) > 1 for candidates in observation_index.values()):
        errors.append("OBSERVATION_IDENTITY_DUPLICATE")

    for target in graph.values():
        if target not in observation_index:
            errors.append("OBSERVATION_SUPERSESSION_TARGET_UNRESOLVED")

    if _has_cycle(graph):
        errors.append("OBSERVATION_SUPERSESSION_CYCLE")

    return _result(errors)


def observations_for_event(
    observations: Iterable[dict[str, Any]], event_ref: Any
) -> tuple[dict[str, Any], ...]:
    if not _nonempty(event_ref):
        return ()
    requested = str(event_ref).strip()
    matches = [
        observation
        for observation in observations
        if isinstance(observation, dict)
        and observation.get("event_ref") == requested
        and validate_observation(observation).valid
    ]
    return tuple(sorted(matches, key=lambda item: str(item.get("observation_id"))))


def validate_event_reference_fixture(fixture: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    events = fixture.get("events")
    if events is None:
        events = fixture.get("entries")
    if not isinstance(events, list):
        events = []
        errors.append("EVENT_REFERENCE_INVALID")

    errors.extend(validate_event_dataset(events).errors)
    reference = fixture.get("reference") or {}
    event_ref = reference.get("event_ref")
    if not _nonempty(event_ref):
        errors.append("EVENT_REFERENCE_INVALID")
        return _result(errors)

    candidates = [
        event
        for event in events
        if isinstance(event, dict) and event.get("event_id") == event_ref
    ]
    if not candidates:
        errors.append("EVENT_REFERENCE_UNRESOLVED")
    elif len(candidates) > 1:
        errors.append("EVENT_REFERENCE_AMBIGUOUS")
    elif not validate_event(candidates[0]).valid:
        errors.append("EVENT_REFERENCE_UNRESOLVED")

    return _result(errors)


def validate_event_observation_fixture(fixture: dict[str, Any]) -> ValidationResult:
    events = fixture.get("events") or []
    observations = fixture.get("observations") or []
    errors = list(validate_event_dataset(events).errors)
    errors.extend(validate_observation_dataset(observations, events).errors)
    return _result(errors)


def _assessment_valid(assessment: Any) -> bool:
    if not isinstance(assessment, dict):
        return False
    evidence_refs = assessment.get("evidence_observation_refs")
    return (
        _nonempty(assessment.get("assessment_id"))
        and _nonempty(assessment.get("target_objective_ref"))
        and _versioned_ref(assessment.get("rule_ref"))
        and isinstance(evidence_refs, list)
        and bool(evidence_refs)
        and all(_nonempty(item) for item in evidence_refs)
        and len(evidence_refs) == len(set(str(item) for item in evidence_refs))
        and _nonempty(assessment.get("evidence_snapshot_ref"))
        and _nonempty(assessment.get("evaluator_ref"))
        and _parse_time(assessment.get("evaluated_at")) is not None
        and assessment.get("conclusion") in ASSESSMENT_CONCLUSIONS
        and _nonempty(assessment.get("provenance_ref"))
    )


def validate_integrated_event_scenario(fixture: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    scenario = fixture.get("scenario") or fixture.get("entity") or {}

    objective = scenario.get("objective") or {}
    operation = scenario.get("operation") or {}
    resources = scenario.get("resources") or []
    assignments = scenario.get("assignments") or []
    constraint = scenario.get("constraint") or {}
    context = scenario.get("constraint_context") or {}
    constraint_version_ref = scenario.get("constraint_version_ref")
    events = scenario.get("events") or []
    observations = scenario.get("observations") or []
    assessment = scenario.get("assessment")

    if not validate_objective(objective).valid:
        errors.append("SCENARIO_OBJECTIVE_INVALID")

    operation_result = validate_operation(
        operation, {"objectives": [objective] if objective else []}
    )
    if not operation_result.valid:
        errors.append("SCENARIO_OPERATION_INVALID")

    if not isinstance(resources, list) or not resources or any(
        not isinstance(resource, dict) or not validate_resource(resource).valid
        for resource in resources
    ):
        errors.append("SCENARIO_RESOURCE_INVALID")

    if not isinstance(assignments, list) or not assignments or any(
        not isinstance(assignment, dict) or not validate_assignment(assignment).valid
        for assignment in assignments
    ):
        errors.append("SCENARIO_ASSIGNMENT_INVALID")

    contexts = (
        {str(context.get("context_id")): context}
        if isinstance(context, dict) and _nonempty(context.get("context_id"))
        else {}
    )
    if not validate_constraint(constraint, contexts, constraint_version_ref).valid:
        errors.append("SCENARIO_CONSTRAINT_INVALID")

    if not validate_event_dataset(events).valid:
        errors.append("SCENARIO_EVENT_INVALID")
    if not validate_observation_dataset(observations, events).valid:
        errors.append("SCENARIO_OBSERVATION_INVALID")

    if not _assessment_valid(assessment):
        errors.append("SCENARIO_ASSESSMENT_INVALID")
        return _result(errors)

    objective_ref = assessment.get("target_objective_ref")
    if objective_ref != objective.get("objective_id"):
        errors.append("SCENARIO_ASSESSMENT_INVALID")

    observation_index = {
        str(item.get("observation_id")): item
        for item in observations
        if isinstance(item, dict) and _nonempty(item.get("observation_id"))
    }
    evidence_refs = [str(item) for item in assessment["evidence_observation_refs"]]
    if any(reference not in observation_index for reference in evidence_refs):
        errors.append("SCENARIO_EVIDENCE_REFERENCE_UNRESOLVED")
    else:
        statements = {
            str(observation_index[reference].get("statement", "")).strip().casefold()
            for reference in evidence_refs
        }
        if len(statements) > 1 and assessment.get("conclusion") in POSITIVE_CONCLUSIONS:
            errors.append("SCENARIO_CONFLICTING_EVIDENCE_POSITIVE")

    return _result(errors)
