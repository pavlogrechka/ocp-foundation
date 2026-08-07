from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml


ALNUM = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

ERROR_CODES = frozenset(
    {
        "RESOURCE_ID_REQUIRED",
        "RESOURCE_CLASSIFICATION_REQUIRED",
        "RESOURCE_SELF_CONTAINMENT",
        "OPERATION_ID_REQUIRED",
        "OPERATION_INTENT_REQUIRED",
        "OPERATION_SELF_PARENT",
        "ASSIGNMENT_ID_REQUIRED",
        "ASSIGNMENT_HISTORY_INVALID",
        "ASSIGNMENT_TRANSITION_INCOMPLETE",
        "ASSIGNMENT_TRANSITION_REF_MISMATCH",
        "ASSIGNMENT_TRANSITION_TIME_ORDER",
        "ASSIGNMENT_LIFECYCLE_STAGE_MISMATCH",
        "ASSIGNMENT_ESTABLISHED_AT_MISMATCH",
        "ASSIGNMENT_TERMINAL_AT_MISMATCH",
        "ASSIGNMENT_PROVENANCE_REF_MISMATCH",
        "ASSIGNMENT_RESOURCE_REQUIRED",
        "ASSIGNMENT_OPERATION_REQUIRED",
        "ASSIGNMENT_ROLE_REQUIRED",
        "ASSIGNMENT_APPLICABILITY_START_REQUIRED",
        "ASSIGNMENT_APPLICABILITY_INTERVAL_INVALID",
        "ASSIGNMENT_CREATED_AFTER_TRANSITION",
        "ASSIGNMENT_TERMINAL_BEFORE_ESTABLISHMENT",
        "ASSIGNMENT_SELF_SUPERSESSION",
        "CONSTRAINT_ID_REQUIRED",
        "CONSTRAINT_HISTORY_INVALID",
        "CONSTRAINT_TRANSITION_INCOMPLETE",
        "CONSTRAINT_TRANSITION_REF_MISMATCH",
        "CONSTRAINT_TRANSITION_TIME_ORDER",
        "CONSTRAINT_LIFECYCLE_STAGE_MISMATCH",
        "CONSTRAINT_ESTABLISHED_AT_MISMATCH",
        "CONSTRAINT_RETIRED_AT_MISMATCH",
        "CONSTRAINT_ESTABLISHMENT_PROVENANCE_REF_MISMATCH",
        "CONSTRAINT_TARGET_REQUIRED",
        "CONSTRAINT_PREDICATE_INCOMPLETE",
        "CONSTRAINT_ENFORCEMENT_INVALID",
        "CONSTRAINT_VALIDITY_INTERVAL_INVALID",
        "CONSTRAINT_EVALUATION_INCOMPLETE",
        "CONSTRAINT_EVALUATION_REF_MISMATCH",
        "CONSTRAINT_NOT_APPLICABLE_CONTRADICTION",
        "CONSTRAINT_AUTHORITATIVE_RESULT_CONFLICT",
        "CONSTRAINT_SELF_SUPERSESSION",
        "FIXTURE_CONCEPT_UNSUPPORTED",
        "FIXTURE_CONSTRAINT_VERSION_REF_REQUIRED",
        "STATUS_REGISTRY_MISSING",
        "STATUS_TAXONOMY_MISSING",
        "STATUS_TAXONOMY_DUPLICATE",
        "STATUS_TAXONOMY_EXTRA",
        "STATUS_DEFINING_DOCUMENT_MISSING",
        "STATUS_MISMATCH",
        "STATUS_PEER_VIEW_MISMATCH",
    }
)

DERIVATION_RULES = frozenset(
    {
        "assignment_effective_at",
        "derived_participates_in",
        "constraint_effective_at",
        "constraint_applicable_to",
        "effective_constraint_result",
        "constraint_blocks",
        "constraint_set_decision",
    }
)


@dataclass(frozen=True)
class ValidationResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> ValidationResult:
    return ValidationResult(tuple(dict.fromkeys(errors)))


def _nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    return bool(str(value).strip())


def _has_alnum(value: Any) -> bool:
    return isinstance(value, str) and any(char in ALNUM for char in value)


def _parse_time(value: Any) -> datetime | None:
    if isinstance(value, datetime):
        parsed = value
    else:
        if not isinstance(value, str) or not value.strip():
            return None
        text = value.strip().replace("Z", "+00:00")
        try:
            parsed = datetime.fromisoformat(text)
        except ValueError:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _transition_signature(history: list[dict[str, Any]]) -> tuple[tuple[str, str], ...]:
    return tuple((str(item.get("from_stage")), str(item.get("to_stage"))) for item in history)


def _derived_stage(history: list[dict[str, Any]], default: str = "Draft") -> str:
    return str(history[-1]["to_stage"]) if history else default


def _transition(history: list[dict[str, Any]], from_stage: str, to_stage: str) -> dict[str, Any] | None:
    matches = [item for item in history if item.get("from_stage") == from_stage and item.get("to_stage") == to_stage]
    return matches[0] if len(matches) == 1 else None


def _times_non_decreasing(history: list[dict[str, Any]]) -> bool:
    times = [_parse_time(item.get("occurred_at")) for item in history]
    return all(item is not None for item in times) and all(a <= b for a, b in zip(times, times[1:]))


def _check_materialized_projections(
    entity: dict[str, Any], projections: dict[str, Any], prefix: str
) -> list[str]:
    errors: list[str] = []
    for field, expected in projections.items():
        if field in entity and entity[field] != expected:
            errors.append(f"{prefix}_{field.upper()}_MISMATCH")
    return errors


def validate_resource(resource: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    if not _nonempty(resource.get("resource_id")):
        errors.append("RESOURCE_ID_REQUIRED")
    classifications = resource.get("classifications")
    if not isinstance(classifications, list) or not any(_nonempty(item) for item in classifications):
        errors.append("RESOURCE_CLASSIFICATION_REQUIRED")
    contains = resource.get("contains_refs", [])
    if resource.get("resource_id") in contains:
        errors.append("RESOURCE_SELF_CONTAINMENT")
    return _result(errors)


def validate_operation(
    operation: dict[str, Any],
    references: dict[str, Any] | None = None,
) -> ValidationResult:
    """Delegate to the single authoritative Operation fixture validator."""
    from .objective import validate_operation_fixture

    fixture: dict[str, Any] = {"concept": "Operation", "entity": operation}
    if references is not None:
        fixture["references"] = references
    return validate_operation_fixture(fixture)


ASSIGNMENT_PATHS = {
    (),
    (("Draft", "Established"),),
    (("Draft", "Established"), ("Established", "Closed")),
    (("Draft", "Established"), ("Established", "Revoked")),
    (("Draft", "Cancelled"),),
}


def assignment_projections(assignment: dict[str, Any]) -> dict[str, Any]:
    history = assignment.get("transition_history") or []
    established = _transition(history, "Draft", "Established")
    closed = _transition(history, "Established", "Closed")
    revoked = _transition(history, "Established", "Revoked")
    terminal = closed or revoked
    return {
        "lifecycle_stage": _derived_stage(history),
        "established_at": established.get("occurred_at") if established else None,
        "terminal_at": terminal.get("occurred_at") if terminal else None,
        "provenance_ref": established.get("provenance_ref") if established else None,
    }


def validate_assignment(assignment: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    assignment_id = assignment.get("assignment_id")
    if not _nonempty(assignment_id):
        errors.append("ASSIGNMENT_ID_REQUIRED")

    history = assignment.get("transition_history") or []
    if not isinstance(history, list) or _transition_signature(history) not in ASSIGNMENT_PATHS:
        errors.append("ASSIGNMENT_HISTORY_INVALID")
        history = history if isinstance(history, list) else []

    for record in history:
        required = ("transition_id", "assignment_ref", "from_stage", "to_stage", "occurred_at", "provenance_ref")
        if not all(_nonempty(record.get(field)) for field in required):
            errors.append("ASSIGNMENT_TRANSITION_INCOMPLETE")
            break
        if record.get("assignment_ref") != assignment_id:
            errors.append("ASSIGNMENT_TRANSITION_REF_MISMATCH")
            break

    if history and not _times_non_decreasing(history):
        errors.append("ASSIGNMENT_TRANSITION_TIME_ORDER")

    projections = assignment_projections(assignment)
    errors.extend(_check_materialized_projections(assignment, projections, "ASSIGNMENT"))

    stage = projections["lifecycle_stage"]
    if stage in {"Established", "Closed", "Revoked"}:
        if not _nonempty(assignment.get("resource_ref")):
            errors.append("ASSIGNMENT_RESOURCE_REQUIRED")
        if not _nonempty(assignment.get("operation_ref")):
            errors.append("ASSIGNMENT_OPERATION_REQUIRED")
        role = assignment.get("role_specification") or {}
        if not _has_alnum(role.get("role_code")):
            errors.append("ASSIGNMENT_ROLE_REQUIRED")
        if _parse_time(assignment.get("applicability_start")) is None:
            errors.append("ASSIGNMENT_APPLICABILITY_START_REQUIRED")

    start = _parse_time(assignment.get("applicability_start"))
    end = _parse_time(assignment.get("applicability_end"))
    if end is not None and (start is None or start >= end):
        errors.append("ASSIGNMENT_APPLICABILITY_INTERVAL_INVALID")

    created = _parse_time(assignment.get("created_at"))
    first = _parse_time(history[0].get("occurred_at")) if history else None
    if first is not None and (created is None or created > first):
        errors.append("ASSIGNMENT_CREATED_AFTER_TRANSITION")

    established = _parse_time(projections["established_at"])
    terminal = _parse_time(projections["terminal_at"])
    if terminal is not None and (established is None or established > terminal):
        errors.append("ASSIGNMENT_TERMINAL_BEFORE_ESTABLISHMENT")

    if assignment.get("supersedes_assignment_ref") == assignment_id:
        errors.append("ASSIGNMENT_SELF_SUPERSESSION")
    return _result(errors)


def assignment_effective_at(assignment: dict[str, Any], at: str) -> bool:
    projections = assignment_projections(assignment)
    moment = _parse_time(at)
    established = _parse_time(projections["established_at"])
    start = _parse_time(assignment.get("applicability_start"))
    end = _parse_time(assignment.get("applicability_end"))
    terminal = _parse_time(projections["terminal_at"])
    if moment is None or established is None or start is None:
        return False
    return (
        established <= moment
        and start <= moment
        and (end is None or moment < end)
        and (terminal is None or moment < terminal)
    )


def derived_participates_in(
    assignments: Iterable[dict[str, Any]], resource_ref: str, operation_ref: str, at: str
) -> bool:
    return any(
        item.get("resource_ref") == resource_ref
        and item.get("operation_ref") == operation_ref
        and assignment_effective_at(item, at)
        for item in assignments
    )


CONSTRAINT_PATHS = {
    (),
    (("Draft", "Established"),),
    (("Draft", "Established"), ("Established", "Retired")),
    (("Draft", "Cancelled"),),
}


def constraint_projections(constraint: dict[str, Any]) -> dict[str, Any]:
    history = constraint.get("transition_history") or []
    established = _transition(history, "Draft", "Established")
    retired = _transition(history, "Established", "Retired")
    return {
        "lifecycle_stage": _derived_stage(history),
        "established_at": established.get("occurred_at") if established else None,
        "retired_at": retired.get("occurred_at") if retired else None,
        "establishment_provenance_ref": established.get("provenance_ref") if established else None,
    }


def constraint_effective_at(constraint: dict[str, Any], at: str) -> bool:
    projection = constraint_projections(constraint)
    moment = _parse_time(at)
    established = _parse_time(projection["established_at"])
    start = _parse_time(constraint.get("validity_start"))
    end = _parse_time(constraint.get("validity_end"))
    retired = _parse_time(projection["retired_at"])
    if moment is None or established is None:
        return False
    return (
        established <= moment
        and (start is None or start <= moment)
        and (end is None or moment < end)
        and (retired is None or moment < retired)
    )


def _target_matches(target: dict[str, Any], context: dict[str, Any]) -> bool:
    explicit = set(target.get("explicit_subject_refs") or [])
    subjects = set(context.get("subject_refs") or [])
    selector = target.get("subject_selector") or {}
    explicit_match = bool(explicit.intersection(subjects)) if explicit else False
    selector_match = bool(selector.get("match_all"))
    operation_match = (
        not target.get("operation_context_ref")
        or target.get("operation_context_ref") == context.get("operation_context_ref")
    )
    return (explicit_match or selector_match) and operation_match


def constraint_applicable_to(constraint: dict[str, Any], context: dict[str, Any]) -> bool:
    return constraint_effective_at(constraint, str(context.get("evaluation_time"))) and _target_matches(
        constraint.get("target_specification") or {}, context
    )


def _matching_evaluations(
    constraint: dict[str, Any],
    context: dict[str, Any],
    constraint_version_ref: str,
) -> list[dict[str, Any]]:
    return [
        item
        for item in constraint.get("evaluation_records", [])
        if item.get("constraint_version_ref") == constraint_version_ref
        and item.get("context_ref") == context.get("context_id")
        and item.get("input_snapshot_ref") == context.get("input_snapshot_ref")
    ]


def effective_constraint_result(
    constraint: dict[str, Any],
    context: dict[str, Any],
    constraint_version_ref: str,
) -> str:
    if not constraint_applicable_to(constraint, context):
        return "not_applicable"
    if not _nonempty(constraint_version_ref):
        return "indeterminate"

    candidates = _matching_evaluations(constraint, context, constraint_version_ref)
    if not candidates:
        return "indeterminate"

    results = {item.get("result") for item in candidates}
    if len(results) != 1:
        return "indeterminate"

    result = next(iter(results))
    return result if result in {"satisfied", "violated", "indeterminate"} else "indeterminate"


def constraint_blocks(
    constraint: dict[str, Any],
    context: dict[str, Any],
    constraint_version_ref: str,
) -> bool:
    if not constraint_applicable_to(constraint, context):
        return False
    enforcement = constraint.get("enforcement_specification") or {}
    if enforcement.get("mode") != "blocking":
        return False
    result = effective_constraint_result(constraint, context, constraint_version_ref)
    return result == "violated" or (
        result == "indeterminate" and enforcement.get("indeterminate_disposition") == "block"
    )


def constraint_set_decision(
    constraints: Iterable[dict[str, Any]],
    context: dict[str, Any],
    constraint_version_refs: dict[str, str],
) -> str:
    applicable = [item for item in constraints if constraint_applicable_to(item, context)]
    if any(
        constraint_blocks(
            item,
            context,
            constraint_version_refs.get(str(item.get("constraint_id")), ""),
        )
        for item in applicable
    ):
        return "inadmissible"
    for item in applicable:
        enforcement = item.get("enforcement_specification") or {}
        result = effective_constraint_result(
            item,
            context,
            constraint_version_refs.get(str(item.get("constraint_id")), ""),
        )
        if result == "indeterminate" and enforcement.get("indeterminate_disposition") == "require_review":
            return "review_required"
    return "admissible"


def validate_constraint(
    constraint: dict[str, Any],
    contexts: dict[str, dict[str, Any]] | None = None,
    constraint_version_ref: str | None = None,
) -> ValidationResult:
    errors: list[str] = []
    constraint_id = constraint.get("constraint_id")
    if not _nonempty(constraint_id):
        errors.append("CONSTRAINT_ID_REQUIRED")
    if not _nonempty(constraint_version_ref):
        errors.append("FIXTURE_CONSTRAINT_VERSION_REF_REQUIRED")

    history = constraint.get("transition_history") or []
    if not isinstance(history, list) or _transition_signature(history) not in CONSTRAINT_PATHS:
        errors.append("CONSTRAINT_HISTORY_INVALID")
        history = history if isinstance(history, list) else []
    for record in history:
        required = ("transition_id", "constraint_ref", "from_stage", "to_stage", "occurred_at", "provenance_ref")
        if not all(_nonempty(record.get(field)) for field in required):
            errors.append("CONSTRAINT_TRANSITION_INCOMPLETE")
            break
        if record.get("constraint_ref") != constraint_id:
            errors.append("CONSTRAINT_TRANSITION_REF_MISMATCH")
            break

    if history and not _times_non_decreasing(history):
        errors.append("CONSTRAINT_TRANSITION_TIME_ORDER")

    projection = constraint_projections(constraint)
    errors.extend(_check_materialized_projections(constraint, projection, "CONSTRAINT"))

    if projection["lifecycle_stage"] in {"Established", "Retired"}:
        target = constraint.get("target_specification") or {}
        selector = target.get("subject_selector")
        selector_present = isinstance(selector, dict) and bool(selector)
        if not (target.get("explicit_subject_refs") or selector_present):
            errors.append("CONSTRAINT_TARGET_REQUIRED")
        predicate = constraint.get("predicate_specification") or {}
        for field in ("predicate_code", "predicate_namespace", "predicate_version", "input_contract_ref"):
            if not _nonempty(predicate.get(field)):
                errors.append("CONSTRAINT_PREDICATE_INCOMPLETE")
                break
        enforcement = constraint.get("enforcement_specification") or {}
        if enforcement.get("mode") not in {"blocking", "advisory"} or enforcement.get(
            "indeterminate_disposition"
        ) not in {"block", "require_review", "allow"}:
            errors.append("CONSTRAINT_ENFORCEMENT_INVALID")

    start = _parse_time(constraint.get("validity_start"))
    end = _parse_time(constraint.get("validity_end"))
    if start is not None and end is not None and start >= end:
        errors.append("CONSTRAINT_VALIDITY_INTERVAL_INVALID")

    contexts = contexts or {}
    authoritative: dict[tuple[Any, Any, Any], str] = {}
    for record in constraint.get("evaluation_records", []):
        required = (
            "evaluation_id",
            "constraint_ref",
            "constraint_version_ref",
            "context_ref",
            "input_snapshot_ref",
            "evaluated_at",
            "result",
            "evaluator_ref",
        )
        if not all(_nonempty(record.get(field)) for field in required):
            errors.append("CONSTRAINT_EVALUATION_INCOMPLETE")
            continue
        if record.get("constraint_ref") != constraint_id:
            errors.append("CONSTRAINT_EVALUATION_REF_MISMATCH")
        context = contexts.get(str(record.get("context_ref")))
        if (
            context
            and record.get("constraint_version_ref") == constraint_version_ref
            and record.get("result") == "not_applicable"
            and constraint_applicable_to(constraint, context)
        ):
            errors.append("CONSTRAINT_NOT_APPLICABLE_CONTRADICTION")
        key = (
            record.get("constraint_version_ref"),
            record.get("context_ref"),
            record.get("input_snapshot_ref"),
        )
        previous = authoritative.setdefault(key, str(record.get("result")))
        if previous != record.get("result"):
            errors.append("CONSTRAINT_AUTHORITATIVE_RESULT_CONFLICT")

    if constraint.get("supersedes_constraint_ref") == constraint_id:
        errors.append("CONSTRAINT_SELF_SUPERSESSION")
    return _result(errors)


def load_fixture(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    if not isinstance(loaded, dict):
        raise ValueError(f"Fixture {path} must contain a mapping")
    return loaded


def validate_fixture(fixture: dict[str, Any]) -> ValidationResult:
    concept = fixture.get("concept")
    entity = fixture.get("entity") or {}
    if concept == "Resource":
        return validate_resource(entity)
    if concept == "Operation":
        return validate_operation(entity, fixture.get("references"))
    if concept == "Assignment":
        return validate_assignment(entity)
    if concept == "Constraint":
        contexts = {item["context_id"]: item for item in fixture.get("contexts", [])}
        reference = fixture.get("reference") or {}
        return validate_constraint(entity, contexts, reference.get("constraint_version_ref"))
    return ValidationResult(("FIXTURE_CONCEPT_UNSUPPORTED",))


def _read_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    loaded = yaml.safe_load(text[4:end])
    return loaded if isinstance(loaded, dict) else {}


def _concept_status_projection_has_duplicates(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False
    end = text.find("\n---\n", 4)
    if end == -1:
        return False
    try:
        root = yaml.compose(text[4:end])
    except yaml.YAMLError:
        return False
    if not isinstance(root, yaml.nodes.MappingNode):
        return False

    projections = [
        value
        for key, value in root.value
        if getattr(key, "value", None) == "Concept-Statuses"
    ]
    if len(projections) > 1:
        return True
    if not projections or not isinstance(projections[0], yaml.nodes.MappingNode):
        return False
    keys = [getattr(key, "value", None) for key, _ in projections[0].value]
    return len(keys) != len(set(keys))


def _ontology_registry(path: Path) -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0] in {"Concept", "---"} or set(cells[0]) == {"-"}:
            continue
        rows[cells[0]] = cells[1]
    return rows



def _peer_concept_status_rows(path: Path) -> list[tuple[int, str, str]]:
    """Read current peer Concept status rows from the governed section/table shape."""
    lines = path.read_text(encoding="utf-8").splitlines()
    rows: list[tuple[int, str, str]] = []

    for section_start, line in enumerate(lines):
        if not line.startswith("## "):
            continue
        heading = line[3:].strip()
        number, separator, title = heading.partition(". ")
        if separator and number.isdigit():
            heading = title
        if heading != "Concept Status and Dependencies":
            continue

        section_end = len(lines)
        for index in range(section_start + 1, len(lines)):
            if lines[index].startswith("## "):
                section_end = index
                break

        index = section_start + 1
        while index < section_end:
            line = lines[index]
            if not line.startswith("|"):
                index += 1
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) < 2 or cells[:2] != ["Concept", "Status"]:
                index += 1
                continue

            index += 1
            while index < section_end and lines[index].startswith("|"):
                cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
                index += 1
                if len(cells) < 2 or not cells[0] or set(cells[0]) == {"-"}:
                    continue
                rows.append((section_start, cells[0], cells[1]))
            continue

    return rows


def validate_repository(repo_root: Path) -> ValidationResult:
    errors: list[str] = []
    registry_path = repo_root / "docs/000-operational-ontology/README.md"
    taxonomy_path = repo_root / "docs/002-concept-taxonomy/README.md"
    if not registry_path.exists():
        return ValidationResult(("STATUS_REGISTRY_MISSING",))
    if not taxonomy_path.exists():
        return ValidationResult(("STATUS_TAXONOMY_MISSING",))

    registry = _ontology_registry(registry_path)
    taxonomy = _read_frontmatter(taxonomy_path).get("Concept-Statuses") or {}
    if _concept_status_projection_has_duplicates(taxonomy_path):
        errors.append("STATUS_TAXONOMY_DUPLICATE")
    if not isinstance(taxonomy, dict):
        taxonomy = {}

    defining: dict[str, str] = {}
    for path in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _read_frontmatter(path)
        concepts = metadata.get("Defines-Concepts")
        status = metadata.get("Concept-Status")
        if not concepts:
            continue
        names = [item.strip() for item in str(concepts).split(",") if item.strip()]
        for name in names:
            if not _nonempty(status):
                errors.append("STATUS_DEFINING_DOCUMENT_MISSING")
            else:
                defining[name] = str(status)

    for concept, status in defining.items():
        registry_status = registry.get(concept)
        taxonomy_status = taxonomy.get(concept)
        if registry_status is None:
            errors.append("STATUS_REGISTRY_MISSING")
        if taxonomy_status is None:
            errors.append("STATUS_TAXONOMY_MISSING")
        if registry_status is not None and registry_status != status:
            errors.append("STATUS_MISMATCH")
        if taxonomy_status is not None and str(taxonomy_status) != status:
            errors.append("STATUS_MISMATCH")

    for concept in taxonomy:
        if concept not in defining:
            errors.append("STATUS_TAXONOMY_EXTRA")

    peer_status_rows: set[tuple[Path, int, str]] = set()
    for path in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        for section_start, concept, status in _peer_concept_status_rows(path):
            if concept not in registry:
                continue
            key = (path, section_start, concept)
            if key in peer_status_rows or status != registry[concept]:
                errors.append("STATUS_PEER_VIEW_MISMATCH")
            peer_status_rows.add(key)

    return _result(errors)
