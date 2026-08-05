from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .checker import ValidationResult


OBJECTIVE_ERROR_CODES = frozenset(
    {
        "OBJECTIVE_CREATED_AT_REQUIRED",
        "OBJECTIVE_IDENTITY_DUPLICATE",
        "OBJECTIVE_ID_REQUIRED",
        "OBJECTIVE_PROVENANCE_REF_REQUIRED",
        "OBJECTIVE_SELF_SUPERSESSION",
        "OBJECTIVE_STATEMENT_REQUIRED",
        "OBJECTIVE_SUPERSESSION_CYCLE",
        "OPERATION_EXPLICIT_INTENT_EVIDENCE_CONFLICT",
        "OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID",
        "OPERATION_EXPLICIT_INTENT_EVIDENCE_MISSING",
        "OPERATION_EXPLICIT_INTENT_EVIDENCE_STALE",
        "OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH",
        "OPERATION_INTENT_REPRESENTATION_CONFLICT",
        "OPERATION_OBJECTIVE_REFERENCE_INVALID",
        "OPERATION_OBJECTIVE_REFERENCE_UNRESOLVED",
    }
)

VALIDATION_RESULTS = frozenset({"not_evaluated", "passed", "failed"})


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
    identity_counts: dict[str, int] = {}

    for objective in objectives:
        if not isinstance(objective, dict):
            errors.append("OBJECTIVE_ID_REQUIRED")
            continue
        errors.extend(validate_objective(objective).errors)
        objective_id = objective.get("objective_id")
        supersedes = objective.get("supersedes_objective_ref")
        if _nonempty(objective_id):
            identity = str(objective_id)
            identity_counts[identity] = identity_counts.get(identity, 0) + 1
        if _nonempty(objective_id) and _nonempty(supersedes):
            graph[str(objective_id)] = str(supersedes)

    if any(count > 1 for count in identity_counts.values()):
        errors.append("OBJECTIVE_IDENTITY_DUPLICATE")
    if _has_supersession_cycle(graph):
        errors.append("OBJECTIVE_SUPERSESSION_CYCLE")
    return _result(errors)


def validate_objective_correction_fixture(fixture: dict[str, Any]) -> ValidationResult:
    """Validate immutable Objective history and exact historical consumers."""
    from .assessment import validate_outcome_assessment_dataset

    errors: list[str] = []
    objectives = fixture.get("objectives") or []
    errors.extend(validate_objective_dataset(objectives).errors)

    operation = fixture.get("operation") or {}
    operation_fixture = {
        "concept": "Operation",
        "entity": operation,
        "references": {"objectives": objectives},
    }
    errors.extend(validate_operation_fixture(operation_fixture).errors)

    assessment = fixture.get("assessment") or {}
    errors.extend(
        validate_outcome_assessment_dataset(
            [assessment],
            objectives=objectives,
            events=fixture.get("events") or [],
            observations=fixture.get("observations") or [],
            evidence_snapshots=fixture.get("evidence_snapshots") or [],
            input_snapshots=fixture.get("input_snapshots") or [],
            freshness_rules=fixture.get("freshness_rules") or [],
            ambiguity_rules=fixture.get("ambiguity_rules") or [],
        ).errors
    )
    return _result(errors)


def _validation_record_valid(record: Any) -> bool:
    if not isinstance(record, dict):
        return False
    return (
        _nonempty(record.get("validation_id"))
        and _versioned_ref(record.get("intent_version_ref"))
        and _versioned_ref(record.get("validation_rule_ref"))
        and _nonempty(record.get("input_snapshot_ref"))
        and _parse_time(record.get("evaluated_at")) is not None
        and _nonempty(record.get("evaluator_ref"))
        and record.get("result") in VALIDATION_RESULTS
    )


def _validate_explicit_intent(intent: Any) -> list[str]:
    if not isinstance(intent, dict):
        return ["OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID"]

    errors: list[str] = []
    top_level_valid = (
        _nonempty(intent.get("intent_id"))
        and _versioned_ref(intent.get("intent_version_ref"))
        and _has_alnum(intent.get("statement"))
        and _versioned_ref(intent.get("validation_rule_ref"))
        and _nonempty(intent.get("input_snapshot_ref"))
    )
    if not top_level_valid:
        errors.append("OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID")

    effective_result: str | None = None
    records = intent.get("validation_records")
    if not isinstance(records, list) or not records:
        errors.append("OPERATION_EXPLICIT_INTENT_EVIDENCE_MISSING")
    elif any(not _validation_record_valid(record) for record in records):
        errors.append("OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID")
    elif top_level_valid:
        exact = [
            record
            for record in records
            if record.get("intent_version_ref") == intent.get("intent_version_ref")
            and record.get("validation_rule_ref") == intent.get("validation_rule_ref")
            and record.get("input_snapshot_ref") == intent.get("input_snapshot_ref")
        ]
        if not exact:
            errors.append("OPERATION_EXPLICIT_INTENT_EVIDENCE_STALE")
        else:
            exact_results = {str(record["result"]) for record in exact}
            if len(exact_results) != 1:
                errors.append("OPERATION_EXPLICIT_INTENT_EVIDENCE_CONFLICT")
            else:
                effective_result = next(iter(exact_results))

    normative_projection = effective_result or "not_evaluated"
    if "validation_status" in intent and intent.get("validation_status") != normative_projection:
        errors.append("OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH")
    if effective_result is not None and effective_result != "passed":
        errors.append("OPERATION_INTENT_REQUIRED")
    return errors


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
    from .spatial import validate_operation_spatial_context

    operation = fixture.get("entity") or {}
    errors: list[str] = list(validate_operation_spatial_context(fixture).errors)

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
            errors.extend(_validate_explicit_intent(operation.get("explicit_intent_record")))
        else:
            errors.append("OPERATION_INTENT_REQUIRED")

    return _result(errors)
