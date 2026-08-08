from __future__ import annotations

from collections import defaultdict
from typing import Any

from ._common import nonempty, parse_time, result
from .checker import ValidationResult, assignment_effective_at, validate_assignment
from .objective import validate_operation_fixture


OPERATION_LIFECYCLE_ERROR_CODES = frozenset(
    {
        "OPERATION_Q3I_FIXTURE_INVALID",
        "OPERATION_Q3I_OPERATION_DUPLICATE",
        "OPERATION_Q3I_OPERATION_CONTRACT_REF_INVALID",
        "OPERATION_Q3I_INTENT_CONFORMANCE_INVALID",
        "OPERATION_Q3I_RECORD_ID_DUPLICATE",
        "OPERATION_Q3I_PARENT_UNRESOLVED",
        "OPERATION_Q3I_COMPOSITION_CYCLE",
        "OPERATION_Q3I_RELATION_INVALID",
        "OPERATION_Q3I_RELATION_TARGET_UNRESOLVED",
        "OPERATION_Q3I_RELATION_DUPLICATE",
        "OPERATION_Q3I_RELATION_FORBIDDEN_INDEPENDENT_RECORD",
        "OPERATION_LIFECYCLE_CONTRACT_DUPLICATE",
        "OPERATION_LIFECYCLE_OPERATION_UNRESOLVED",
        "OPERATION_LIFECYCLE_HISTORY_INVALID",
        "OPERATION_LIFECYCLE_TRANSITION_INVALID",
        "OPERATION_LIFECYCLE_TRANSITION_DUPLICATE",
        "OPERATION_LIFECYCLE_COMPLETENESS_UNRESOLVED",
        "OPERATION_LIFECYCLE_COMPLETENESS_FAILED",
        "OPERATION_LIFECYCLE_AUTHORIZATION_UNRESOLVED",
        "OPERATION_LIFECYCLE_AUTHORIZATION_INVALID",
        "OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID",
        "OPERATION_LIFECYCLE_STAGE_MISMATCH",
        "OPERATION_LIFECYCLE_OPERATION_MINIMUM_INCOMPLETE",
        "OPERATION_LIFECYCLE_FORBIDDEN_COUPLING",
    }
)

OPERATION_LIFECYCLE_DERIVATION_RULES = frozenset(
    {"derive_operation_lifecycle_stage"}
)

OPERATION_CONTRACT_REF = "OCP-004@0.9.0"
INTENT_KIND_REF = "operation-explicit-intent@1"
VALIDATION_KIND_REF = "operation-intent-validation@1"
TRANSITION_KIND_REF = "operation-lifecycle-transition@1"
RELATION_TYPES = frozenset(
    {"coordinates_with", "depends_on", "supports", "conflicts_with"}
)
ALLOWED_TRANSITIONS = frozenset(
    {
        ("Draft", "Planned"),
        ("Draft", "Cancelled"),
        ("Planned", "Authorized"),
        ("Planned", "Cancelled"),
        ("Authorized", "Active"),
        ("Authorized", "Cancelled"),
        ("Active", "Completed"),
        ("Active", "Aborted"),
    }
)
TERMINAL_STAGES = frozenset({"Completed", "Cancelled", "Aborted"})
RELATION_FORBIDDEN_FIELDS = frozenset(
    {
        "relationship_id",
        "relation_id",
        "record_id",
        "effective_from",
        "effective_until",
        "supersedes_ref",
        "transition_history",
        "current_head_ref",
    }
)
FORBIDDEN_COUPLING_FIELDS = frozenset(
    {
        "authorization_granted",
        "assignment_mutation",
        "event_generated",
        "outcome_achieved",
        "readiness",
        "state",
        "resource_available",
        "resource_interchangeable",
    }
)


def _text(value: Any) -> str | None:
    return str(value).strip() if nonempty(value) else None


def _contains_forbidden(value: Any) -> bool:
    if isinstance(value, dict):
        return any(
            key in FORBIDDEN_COUPLING_FIELDS or _contains_forbidden(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_forbidden(item) for item in value)
    return False


def _index_exact(records: Any, field: str) -> dict[str, list[dict[str, Any]]]:
    index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    if not isinstance(records, list):
        return index
    for record in records:
        if isinstance(record, dict) and _text(record.get(field)) is not None:
            index[str(record[field]).strip()].append(record)
    return index


def _ordered_history(history: Any) -> list[dict[str, Any]] | None:
    if not isinstance(history, list) or any(not isinstance(item, dict) for item in history):
        return None
    if not history:
        return []

    by_id = _index_exact(history, "transition_id")
    if len(by_id) != len(history) or any(len(items) != 1 for items in by_id.values()):
        return None

    roots = [item for item in history if _text(item.get("predecessor_transition_ref")) is None]
    if len(roots) != 1:
        return None

    successors: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in history:
        predecessor = _text(item.get("predecessor_transition_ref"))
        transition_id = _text(item.get("transition_id"))
        if predecessor is None:
            continue
        if predecessor == transition_id or len(by_id.get(predecessor, [])) != 1:
            return None
        successors[predecessor].append(item)
    if any(len(items) != 1 for items in successors.values()):
        return None

    ordered: list[dict[str, Any]] = []
    seen: set[str] = set()
    current = roots[0]
    while current is not None:
        transition_id = _text(current.get("transition_id"))
        if transition_id is None or transition_id in seen:
            return None
        seen.add(transition_id)
        ordered.append(current)
        following = successors.get(transition_id, [])
        current = following[0] if following else None
    return ordered if len(ordered) == len(history) else None


def derive_operation_lifecycle_stage(lifecycle: dict[str, Any]) -> str | None:
    """Project the unique chain leaf; timestamps and storage order never elect authority."""
    ordered = _ordered_history(lifecycle.get("transition_history"))
    if ordered is None:
        return None
    return str(ordered[-1].get("to_stage")) if ordered else "Draft"


def _explicit_intent_conforms(operation: dict[str, Any]) -> tuple[bool, list[str]]:
    intent = operation.get("explicit_intent_record")
    if not intent:
        return True, []
    if not isinstance(intent, dict):
        return False, []

    ids: list[str] = []
    intent_id = _text(intent.get("intent_id"))
    if intent_id is not None:
        ids.append(intent_id)
    valid = (
        intent.get("record_kind_ref") == INTENT_KIND_REF
        and intent_id is not None
        and _text(intent.get("authoring_provenance_ref")) is not None
    )
    records = intent.get("validation_records")
    if not isinstance(records, list):
        return False, ids
    for record in records:
        if not isinstance(record, dict):
            valid = False
            continue
        validation_id = _text(record.get("validation_id"))
        if validation_id is not None:
            ids.append(validation_id)
        if (
            record.get("record_kind_ref") != VALIDATION_KIND_REF
            or validation_id is None
            or _text(record.get("provenance_ref")) is None
        ):
            valid = False
    return valid, ids


def _has_cycle(graph: dict[str, str]) -> bool:
    for start in graph:
        seen: set[str] = set()
        current: str | None = start
        while current is not None and current in graph:
            if current in seen:
                return True
            seen.add(current)
            current = graph.get(current)
    return False


def _validate_operation_kernel(
    operations: list[dict[str, Any]], objectives: list[dict[str, Any]]
) -> list[str]:
    errors: list[str] = []
    operation_index = _index_exact(operations, "operation_id")
    if any(len(items) > 1 for items in operation_index.values()):
        errors.append("OPERATION_Q3I_OPERATION_DUPLICATE")

    record_ids: list[str] = []
    parent_graph: dict[str, str] = {}
    relation_keys: list[tuple[str, str, str]] = []
    for operation in operations:
        errors.extend(
            validate_operation_fixture(
                {
                    "concept": "Operation",
                    "entity": operation,
                    "references": {"objectives": objectives},
                }
            ).errors
        )
        if operation.get("operation_contract_ref") != OPERATION_CONTRACT_REF:
            errors.append("OPERATION_Q3I_OPERATION_CONTRACT_REF_INVALID")
        if _contains_forbidden(operation):
            errors.append("OPERATION_LIFECYCLE_FORBIDDEN_COUPLING")

        intent_valid, local_record_ids = _explicit_intent_conforms(operation)
        record_ids.extend(local_record_ids)
        if not intent_valid:
            errors.append("OPERATION_Q3I_INTENT_CONFORMANCE_INVALID")

        operation_id = _text(operation.get("operation_id"))
        parent = _text(operation.get("parent_operation_ref"))
        if parent is not None:
            if len(operation_index.get(parent, [])) != 1:
                errors.append("OPERATION_Q3I_PARENT_UNRESOLVED")
            elif operation_id is not None:
                parent_graph[operation_id] = parent

        relations = operation.get("inter_operation_relationships", [])
        if not isinstance(relations, list):
            errors.append("OPERATION_Q3I_RELATION_INVALID")
            continue
        for relation in relations:
            if not isinstance(relation, dict):
                errors.append("OPERATION_Q3I_RELATION_INVALID")
                continue
            if any(field in relation for field in RELATION_FORBIDDEN_FIELDS):
                errors.append("OPERATION_Q3I_RELATION_FORBIDDEN_INDEPENDENT_RECORD")
            source = _text(relation.get("source_operation_ref"))
            target = _text(relation.get("target_operation_ref"))
            kind = _text(relation.get("relation_type"))
            if (
                source != operation_id
                or target is None
                or target == source
                or kind not in RELATION_TYPES
                or _text(relation.get("provenance_ref")) is None
            ):
                errors.append("OPERATION_Q3I_RELATION_INVALID")
                continue
            if len(operation_index.get(target, [])) != 1:
                errors.append("OPERATION_Q3I_RELATION_TARGET_UNRESOLVED")
            relation_keys.append((source, str(kind), target))

    if _has_cycle(parent_graph):
        errors.append("OPERATION_Q3I_COMPOSITION_CYCLE")
    if len(relation_keys) != len(set(relation_keys)):
        errors.append("OPERATION_Q3I_RELATION_DUPLICATE")
    if len(record_ids) != len(set(record_ids)):
        errors.append("OPERATION_Q3I_RECORD_ID_DUPLICATE")
    return errors


def _completeness_errors(
    transition: dict[str, Any], profiles: dict[str, list[dict[str, Any]]]
) -> list[str]:
    binding = transition.get("completeness_binding")
    if not isinstance(binding, dict):
        return ["OPERATION_LIFECYCLE_COMPLETENESS_UNRESOLVED"]
    profile_ref = _text(binding.get("profile_ref"))
    candidates = profiles.get(profile_ref or "", [])
    if (
        profile_ref is None
        or len(candidates) != 1
        or _text(candidates[0].get("profile_owner_ref"))
        != _text(binding.get("profile_owner_ref"))
        or _text(binding.get("input_snapshot_ref")) is None
        or _text(binding.get("provenance_ref")) is None
    ):
        return ["OPERATION_LIFECYCLE_COMPLETENESS_UNRESOLVED"]
    if binding.get("input_state") != "effective" or binding.get("result") != "passed":
        return ["OPERATION_LIFECYCLE_COMPLETENESS_FAILED"]
    return []


def _authorization_errors(
    transition: dict[str, Any], sources: dict[str, list[dict[str, Any]]]
) -> list[str]:
    binding = transition.get("authorization_evidence_binding")
    requires = transition.get("to_stage") == "Authorized"
    if not requires and binding not in (None, {}):
        return ["OPERATION_LIFECYCLE_AUTHORIZATION_INVALID"]
    if not requires:
        return []
    if not isinstance(binding, dict):
        return ["OPERATION_LIFECYCLE_AUTHORIZATION_UNRESOLVED"]
    source_ref = _text(binding.get("source_contract_ref"))
    candidates = sources.get(source_ref or "", [])
    if (
        source_ref is None
        or len(candidates) != 1
        or _text(candidates[0].get("source_owner_ref"))
        != _text(binding.get("source_owner_ref"))
    ):
        return ["OPERATION_LIFECYCLE_AUTHORIZATION_UNRESOLVED"]
    if (
        _text(binding.get("evidence_ref")) is None
        or _text(binding.get("input_snapshot_ref")) is None
        or _text(binding.get("provenance_ref")) is None
        or _text(binding.get("subject_operation_ref"))
        != _text(transition.get("operation_ref"))
        or binding.get("input_state") != "effective"
        or binding.get("result") != "accepted"
    ):
        return ["OPERATION_LIFECYCLE_AUTHORIZATION_INVALID"]
    return []


def _assignment_alignment_errors(
    transition: dict[str, Any], assignments: list[dict[str, Any]]
) -> list[str]:
    alignment = transition.get("assignment_alignment")
    terminal = transition.get("to_stage") in TERMINAL_STAGES
    if not terminal and alignment not in (None, {}):
        return ["OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID"]
    if not terminal:
        return []
    if not isinstance(alignment, dict):
        return ["OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID"]

    at = transition.get("occurred_at")
    if (
        parse_time(alignment.get("evaluation_time")) != parse_time(at)
        or _text(alignment.get("input_snapshot_ref")) is None
    ):
        return ["OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID"]

    relevant = [
        item
        for item in assignments
        if isinstance(item, dict)
        and _text(item.get("operation_ref")) == _text(transition.get("operation_ref"))
    ]
    if any(not validate_assignment(item).valid for item in relevant):
        return ["OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID"]
    expected = {_text(item.get("assignment_id")): item for item in relevant}
    if None in expected:
        return ["OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID"]

    dispositions = alignment.get("dispositions")
    if not isinstance(dispositions, list):
        return ["OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID"]
    actual: dict[str | None, dict[str, Any]] = {}
    for item in dispositions:
        if not isinstance(item, dict):
            return ["OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID"]
        assignment_ref = _text(item.get("assignment_ref"))
        if assignment_ref in actual:
            return ["OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID"]
        actual[assignment_ref] = item
    if set(actual) != set(expected):
        return ["OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID"]

    for assignment_ref, assignment in expected.items():
        item = actual[assignment_ref]
        required = (
            "remains_effective_independently"
            if assignment_effective_at(assignment, str(at))
            else "not_effective_at_transition"
        )
        if item.get("disposition") != required or _text(item.get("evidence_ref")) is None:
            return ["OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID"]
    return []


def _minimum_errors(operation: dict[str, Any], ordered: list[dict[str, Any]]) -> list[str]:
    transitions = {(item.get("from_stage"), item.get("to_stage")) for item in ordered}
    stage = ordered[-1].get("to_stage") if ordered else "Draft"
    required_fields: list[str] = []
    if any(target == "Planned" for _, target in transitions):
        required_fields.append("planned_start")
    if any(target == "Active" for _, target in transitions):
        required_fields.append("actual_start")
    if stage in {"Completed", "Aborted"}:
        required_fields.append("actual_end")
    if any(parse_time(operation.get(field)) is None for field in required_fields):
        return ["OPERATION_LIFECYCLE_OPERATION_MINIMUM_INCOMPLETE"]
    return []


def _validate_lifecycle(
    lifecycle: dict[str, Any],
    operation: dict[str, Any],
    *,
    profiles: dict[str, list[dict[str, Any]]],
    sources: dict[str, list[dict[str, Any]]],
    assignments: list[dict[str, Any]],
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    transition_ids: list[str] = []
    history = lifecycle.get("transition_history")
    ordered = _ordered_history(history)
    if ordered is None:
        return ["OPERATION_LIFECYCLE_HISTORY_INVALID"], transition_ids

    previous: dict[str, Any] | None = None
    for transition in ordered:
        transition_id = _text(transition.get("transition_id"))
        if transition_id is not None:
            transition_ids.append(transition_id)
        valid = (
            transition.get("record_kind_ref") == TRANSITION_KIND_REF
            and transition_id is not None
            and _text(transition.get("operation_ref"))
            == _text(operation.get("operation_id"))
            and (transition.get("from_stage"), transition.get("to_stage"))
            in ALLOWED_TRANSITIONS
            and parse_time(transition.get("occurred_at")) is not None
            and _text(transition.get("provenance_ref")) is not None
        )
        if previous is None:
            valid = valid and transition.get("from_stage") == "Draft"
        else:
            previous_time = parse_time(previous.get("occurred_at"))
            current_time = parse_time(transition.get("occurred_at"))
            valid = (
                valid
                and _text(transition.get("predecessor_transition_ref"))
                == _text(previous.get("transition_id"))
                and transition.get("from_stage") == previous.get("to_stage")
                and previous_time is not None
                and current_time is not None
                and previous_time <= current_time
            )
        if not valid:
            errors.append("OPERATION_LIFECYCLE_TRANSITION_INVALID")
        errors.extend(_completeness_errors(transition, profiles))
        errors.extend(_authorization_errors(transition, sources))
        errors.extend(_assignment_alignment_errors(transition, assignments))
        previous = transition

    projected = derive_operation_lifecycle_stage(lifecycle)
    if (
        "lifecycle_stage" in lifecycle
        and lifecycle.get("lifecycle_stage") != projected
    ) or (
        "lifecycle_stage" in operation
        and operation.get("lifecycle_stage") != projected
    ):
        errors.append("OPERATION_LIFECYCLE_STAGE_MISMATCH")
    errors.extend(_minimum_errors(operation, ordered))
    if _contains_forbidden(lifecycle):
        errors.append("OPERATION_LIFECYCLE_FORBIDDEN_COUPLING")
    return errors, transition_ids


def validate_operation_q3i_dataset(fixture: dict[str, Any]) -> ValidationResult:
    operations = fixture.get("operations")
    lifecycles = fixture.get("operation_lifecycles")
    objectives = fixture.get("objectives", [])
    profiles = fixture.get("completeness_profiles")
    sources = fixture.get("authorization_evidence_sources")
    assignments = fixture.get("assignments", [])
    if not all(
        isinstance(items, list)
        for items in (operations, lifecycles, objectives, profiles, sources, assignments)
    ):
        return result(["OPERATION_Q3I_FIXTURE_INVALID"])

    typed_operations = [item for item in operations if isinstance(item, dict)]
    typed_lifecycles = [item for item in lifecycles if isinstance(item, dict)]
    if (
        len(typed_operations) != len(operations)
        or len(typed_lifecycles) != len(lifecycles)
        or any(not isinstance(item, dict) for item in objectives)
        or any(not isinstance(item, dict) for item in profiles)
        or any(not isinstance(item, dict) for item in sources)
        or any(not isinstance(item, dict) for item in assignments)
    ):
        return result(["OPERATION_Q3I_FIXTURE_INVALID"])

    errors = _validate_operation_kernel(typed_operations, objectives)
    operation_index = _index_exact(typed_operations, "operation_id")
    lifecycle_index = _index_exact(typed_lifecycles, "operation_ref")
    if any(len(items) > 1 for items in lifecycle_index.values()):
        errors.append("OPERATION_LIFECYCLE_CONTRACT_DUPLICATE")
    if set(lifecycle_index) != set(operation_index):
        errors.append("OPERATION_LIFECYCLE_OPERATION_UNRESOLVED")

    profile_index = _index_exact(profiles, "profile_ref")
    source_index = _index_exact(sources, "source_contract_ref")
    assignment_ids = [_text(item.get("assignment_id")) for item in assignments]
    if (
        any(item is None for item in assignment_ids)
        or len(assignment_ids) != len(set(assignment_ids))
        or any(not validate_assignment(item).valid for item in assignments)
    ):
        errors.append("OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID")
    transition_ids: list[str] = []
    for operation_ref, lifecycle_candidates in lifecycle_index.items():
        operation_candidates = operation_index.get(operation_ref, [])
        if len(lifecycle_candidates) != 1 or len(operation_candidates) != 1:
            continue
        lifecycle_errors, local_ids = _validate_lifecycle(
            lifecycle_candidates[0],
            operation_candidates[0],
            profiles=profile_index,
            sources=source_index,
            assignments=assignments,
        )
        errors.extend(lifecycle_errors)
        transition_ids.extend(local_ids)
    if len(transition_ids) != len(set(transition_ids)):
        errors.append("OPERATION_LIFECYCLE_TRANSITION_DUPLICATE")
    return result(errors)


def validate_operation_q3i_fixture(fixture: dict[str, Any]) -> ValidationResult:
    return validate_operation_q3i_dataset(fixture)


__all__ = [name for name in globals() if not name.startswith("_")]
