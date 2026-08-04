from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .checker import (
    ValidationResult,
    constraint_applicable_to,
    derived_participates_in,
    effective_constraint_result,
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


def _normalized_ref(value: Any) -> str | None:
    if not _nonempty(value):
        return None
    return str(value).strip()


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
        event_id = _normalized_ref(event.get("event_id"))
        if event_id is not None:
            index.setdefault(event_id, []).append(event)

    if any(len(candidates) > 1 for candidates in index.values()):
        errors.append("EVENT_IDENTITY_DUPLICATE")

    return _result(errors)


def resolve_event(
    events: Iterable[dict[str, Any]], event_ref: Any
) -> dict[str, Any] | None:
    requested = _normalized_ref(event_ref)
    if requested is None:
        return None
    candidates = [
        event
        for event in events
        if isinstance(event, dict)
        and _normalized_ref(event.get("event_id")) == requested
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

    observation_id = _normalized_ref(observation.get("observation_id"))
    supersedes = _normalized_ref(observation.get("supersedes_observation_ref"))
    if observation_id is not None and supersedes == observation_id:
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
        if not isinstance(event, dict):
            continue
        event_id = _normalized_ref(event.get("event_id"))
        if event_id is not None:
            event_index.setdefault(event_id, []).append(event)

    for observation in observation_entries:
        if not isinstance(observation, dict):
            errors.append("OBSERVATION_ID_REQUIRED")
            continue
        errors.extend(validate_observation(observation).errors)
        observation_id = _normalized_ref(observation.get("observation_id"))
        if observation_id is not None:
            observation_index.setdefault(observation_id, []).append(observation)
            supersedes = _normalized_ref(
                observation.get("supersedes_observation_ref")
            )
            if supersedes is not None and supersedes != observation_id:
                graph[observation_id] = supersedes

        if "event_ref" in observation and observation.get("event_ref") is not None:
            event_ref = _normalized_ref(observation.get("event_ref"))
            if event_ref is None:
                errors.append("EVENT_REFERENCE_INVALID")
            else:
                candidates = event_index.get(event_ref, [])
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
    requested = _normalized_ref(event_ref)
    if requested is None:
        return ()
    matches = [
        observation
        for observation in observations
        if isinstance(observation, dict)
        and _normalized_ref(observation.get("event_ref")) == requested
        and validate_observation(observation).valid
    ]
    return tuple(
        sorted(
            matches,
            key=lambda item: _normalized_ref(item.get("observation_id")) or "",
        )
    )


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
    event_ref = _normalized_ref(reference.get("event_ref"))
    if event_ref is None:
        errors.append("EVENT_REFERENCE_INVALID")
        return _result(errors)

    candidates = [
        event
        for event in events
        if isinstance(event, dict)
        and _normalized_ref(event.get("event_id")) == event_ref
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
    normalized_evidence_refs = (
        [_normalized_ref(item) for item in evidence_refs]
        if isinstance(evidence_refs, list)
        else []
    )
    return (
        _nonempty(assessment.get("assessment_id"))
        and _nonempty(assessment.get("target_objective_ref"))
        and _versioned_ref(assessment.get("rule_ref"))
        and isinstance(evidence_refs, list)
        and bool(evidence_refs)
        and all(item is not None for item in normalized_evidence_refs)
        and len(normalized_evidence_refs) == len(set(normalized_evidence_refs))
        and _nonempty(assessment.get("evidence_snapshot_ref"))
        and _nonempty(assessment.get("evaluator_ref"))
        and _parse_time(assessment.get("evaluated_at")) is not None
        and assessment.get("conclusion") in ASSESSMENT_CONCLUSIONS
        and _nonempty(assessment.get("provenance_ref"))
    )


def _scenario_assignment_links_valid(
    assignments: list[dict[str, Any]],
    resource_ids: set[str],
    operation_id: str | None,
    evaluation_time: Any,
) -> bool:
    if operation_id is None or _parse_time(evaluation_time) is None:
        return False

    normalized_assignments: list[dict[str, Any]] = []
    referenced_resource_ids: list[str] = []
    for assignment in assignments:
        resource_ref = _normalized_ref(assignment.get("resource_ref"))
        operation_ref = _normalized_ref(assignment.get("operation_ref"))
        if resource_ref not in resource_ids or operation_ref != operation_id:
            return False
        normalized = dict(assignment)
        normalized["resource_ref"] = resource_ref
        normalized["operation_ref"] = operation_ref
        normalized_assignments.append(normalized)
        referenced_resource_ids.append(resource_ref)

    return all(
        derived_participates_in(
            normalized_assignments,
            resource_ref,
            operation_id,
            str(evaluation_time),
        )
        for resource_ref in referenced_resource_ids
    )


def _scenario_constraint_links_valid(
    constraint: dict[str, Any],
    context: dict[str, Any],
    constraint_version_ref: Any,
    resource_ids: set[str],
    operation_id: str | None,
) -> bool:
    if operation_id is None or not isinstance(context, dict):
        return False

    context_id = _normalized_ref(context.get("context_id"))
    context_operation_ref = _normalized_ref(context.get("operation_context_ref"))
    raw_subject_refs = context.get("subject_refs")
    if (
        context_id is None
        or context_operation_ref != operation_id
        or not isinstance(raw_subject_refs, list)
        or not raw_subject_refs
    ):
        return False

    subject_refs = [_normalized_ref(item) for item in raw_subject_refs]
    if any(item is None or item not in resource_ids for item in subject_refs):
        return False

    target = constraint.get("target_specification") or {}
    target_operation_ref = _normalized_ref(target.get("operation_context_ref"))
    if target_operation_ref is not None and target_operation_ref != operation_id:
        return False

    raw_target_subjects = target.get("explicit_subject_refs") or []
    if not isinstance(raw_target_subjects, list):
        return False
    target_subjects = [_normalized_ref(item) for item in raw_target_subjects]
    if any(item is None or item not in resource_ids for item in target_subjects):
        return False

    if not constraint_applicable_to(constraint, context):
        return False

    return (
        effective_constraint_result(
            constraint,
            context,
            str(constraint_version_ref or ""),
        )
        != "indeterminate"
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

    resources_structurally_valid = (
        isinstance(resources, list)
        and bool(resources)
        and all(
            isinstance(resource, dict) and validate_resource(resource).valid
            for resource in resources
        )
    )
    resource_ids = {
        resource_id
        for resource in resources
        if isinstance(resource, dict)
        for resource_id in [_normalized_ref(resource.get("resource_id"))]
        if resource_id is not None
    }
    if not resources_structurally_valid or len(resource_ids) != len(resources):
        errors.append("SCENARIO_RESOURCE_INVALID")

    assignments_structurally_valid = (
        isinstance(assignments, list)
        and bool(assignments)
        and all(
            isinstance(assignment, dict) and validate_assignment(assignment).valid
            for assignment in assignments
        )
    )
    operation_id = _normalized_ref(operation.get("operation_id"))
    evaluation_time = context.get("evaluation_time") if isinstance(context, dict) else None
    if (
        not assignments_structurally_valid
        or not _scenario_assignment_links_valid(
            assignments,
            resource_ids,
            operation_id,
            evaluation_time,
        )
    ):
        errors.append("SCENARIO_ASSIGNMENT_INVALID")

    contexts = (
        {_normalized_ref(context.get("context_id")): context}
        if isinstance(context, dict)
        and _normalized_ref(context.get("context_id")) is not None
        else {}
    )
    constraint_structurally_valid = validate_constraint(
        constraint, contexts, constraint_version_ref
    ).valid
    if (
        not constraint_structurally_valid
        or not _scenario_constraint_links_valid(
            constraint,
            context,
            constraint_version_ref,
            resource_ids,
            operation_id,
        )
    ):
        errors.append("SCENARIO_CONSTRAINT_INVALID")

    if not validate_event_dataset(events).valid:
        errors.append("SCENARIO_EVENT_INVALID")
    if not validate_observation_dataset(observations, events).valid:
        errors.append("SCENARIO_OBSERVATION_INVALID")

    if not _assessment_valid(assessment):
        errors.append("SCENARIO_ASSESSMENT_INVALID")
        return _result(errors)

    objective_ref = _normalized_ref(assessment.get("target_objective_ref"))
    if objective_ref != _normalized_ref(objective.get("objective_id")):
        errors.append("SCENARIO_ASSESSMENT_INVALID")

    observation_index = {
        observation_id: item
        for item in observations
        if isinstance(item, dict)
        for observation_id in [_normalized_ref(item.get("observation_id"))]
        if observation_id is not None
    }
    evidence_refs = [
        _normalized_ref(item)
        for item in assessment["evidence_observation_refs"]
    ]
    if any(
        reference is None or reference not in observation_index
        for reference in evidence_refs
    ):
        errors.append("SCENARIO_EVIDENCE_REFERENCE_UNRESOLVED")
    else:
        statements = {
            str(observation_index[reference].get("statement", "")).strip().casefold()
            for reference in evidence_refs
            if reference is not None
        }
        if len(statements) > 1 and assessment.get("conclusion") in POSITIVE_CONCLUSIONS:
            errors.append("SCENARIO_CONFLICTING_EVIDENCE_POSITIVE")

    return _result(errors)
