from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .checker import ValidationResult


OBJECTIVE_ERROR_CODES = frozenset(
    {
        "OBJECTIVE_CREATED_AT_REQUIRED",
        "OBJECTIVE_ID_REQUIRED",
        "OBJECTIVE_PROVENANCE_REF_REQUIRED",
        "OBJECTIVE_SELF_SUPERSESSION",
        "OBJECTIVE_STATEMENT_REQUIRED",
        "OBJECTIVE_SUPERSESSION_CYCLE",
        "OPERATION_INTENT_REPRESENTATION_CONFLICT",
        "OPERATION_OBJECTIVE_REFERENCE_INVALID",
        "OPERATION_OBJECTIVE_REFERENCE_UNRESOLVED",
    }
)


def _result(errors: Iterable[str]) -> ValidationResult:
    return ValidationResult(tuple(dict.fromkeys(errors)))


def _nonempty(value: Any) -> bool:
    return value is not None and bool(str(value).strip())


def _has_alnum(value: Any) -> bool:
    return isinstance(value, str) and any(char.isalnum() for char in value)


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


def validate_objective(objective: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    objective_id = objective.get("objective_id")
    if not _nonempty(objective_id):
        errors.append("OBJECTIVE_ID_REQUIRED")
    if not _has_alnum(objective.get("statement")):
        errors.append("OBJECTIVE_STATEMENT_REQUIRED")
    if _parse_time(objective.get("created_at")) is None:
        errors.append("OBJECTIVE_CREATED_AT_REQUIRED")
    if not _nonempty(objective.get("provenance_ref")):
        errors.append("OBJECTIVE_PROVENANCE_REF_REQUIRED")
    if objective.get("supersedes_objective_ref") == objective_id and _nonempty(objective_id):
        errors.append("OBJECTIVE_SELF_SUPERSESSION")
    return _result(errors)


def _has_supersession_cycle(graph: dict[str, str]) -> bool:
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


def validate_objective_dataset(objectives: Iterable[dict[str, Any]]) -> ValidationResult:
    errors: list[str] = []
    graph: dict[str, str] = {}

    for objective in objectives:
        if not isinstance(objective, dict):
            errors.append("OBJECTIVE_ID_REQUIRED")
            continue
        errors.extend(validate_objective(objective).errors)
        objective_id = objective.get("objective_id")
        supersedes = objective.get("supersedes_objective_ref")
        if _nonempty(objective_id) and _nonempty(supersedes):
            graph[str(objective_id)] = str(supersedes)

    if _has_supersession_cycle(graph):
        errors.append("OBJECTIVE_SUPERSESSION_CYCLE")
    return _result(errors)


def _valid_explicit_intent(intent: Any) -> bool:
    if not isinstance(intent, dict):
        return False
    return (
        _nonempty(intent.get("intent_id"))
        and _has_alnum(intent.get("statement"))
        and intent.get("validation_status") == "passed"
        and _nonempty(intent.get("validation_rule_ref"))
        and _parse_time(intent.get("validated_at")) is not None
    )


def _objective_index(fixture: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    references = fixture.get("references") or {}
    objectives = references.get("objectives") or []
    index: dict[str, list[dict[str, Any]]] = {}
    if not isinstance(objectives, list):
        return index
    for objective in objectives:
        if not isinstance(objective, dict):
            continue
        objective_id = objective.get("objective_id")
        if _nonempty(objective_id):
            index.setdefault(str(objective_id), []).append(objective)
    return index


def validate_operation_fixture(fixture: dict[str, Any]) -> ValidationResult:
    operation = fixture.get("entity") or {}
    errors: list[str] = []

    operation_id = operation.get("operation_id")
    if not _nonempty(operation_id):
        errors.append("OPERATION_ID_REQUIRED")
    if operation.get("parent_operation_ref") == operation_id and _nonempty(operation_id):
        errors.append("OPERATION_SELF_PARENT")

    stage = operation.get("lifecycle_stage", "Draft")
    raw_refs = operation.get("objective_refs", [])
    refs_present = "objective_refs" in operation and raw_refs not in (None, [])
    refs_valid = isinstance(raw_refs, list) and all(_nonempty(item) for item in raw_refs)
    refs = [str(item).strip() for item in raw_refs] if refs_valid else []
    if refs_present and (not refs_valid or len(refs) != len(set(refs))):
        errors.append("OPERATION_OBJECTIVE_REFERENCE_INVALID")

    explicit_present = bool(operation.get("explicit_intent_record"))
    if stage != "Draft" and refs_present and explicit_present:
        errors.append("OPERATION_INTENT_REPRESENTATION_CONFLICT")
        return _result(errors)

    if stage != "Draft" and refs_present and refs_valid:
        index = _objective_index(fixture)
        for objective_ref in refs:
            candidates = index.get(objective_ref, [])
            if len(candidates) != 1 or not validate_objective(candidates[0]).valid:
                errors.append("OPERATION_OBJECTIVE_REFERENCE_UNRESOLVED")
                break

    if stage != "Draft":
        if refs_present:
            if not refs_valid:
                return _result(errors)
        elif explicit_present:
            if not _valid_explicit_intent(operation.get("explicit_intent_record")):
                errors.append("OPERATION_INTENT_REQUIRED")
        else:
            errors.append("OPERATION_INTENT_REQUIRED")

    return _result(errors)
