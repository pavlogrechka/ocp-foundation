from __future__ import annotations

from typing import Any, Iterable

from .checker import ValidationResult
from ._common import nonempty, parse_time, projection_mismatches, result, signature, times_non_decreasing, transition

ORGANIZATION_PATHS = {
    (),
    (("Draft", "Established"),),
    (("Draft", "Established"), ("Established", "Retired")),
    (("Draft", "Cancelled"),),
}
RELATIONSHIP_PATHS = {
    (),
    (("Draft", "Established"),),
    (("Draft", "Established"), ("Established", "Closed")),
    (("Draft", "Established"), ("Established", "Revoked")),
    (("Draft", "Cancelled"),),
}
INITIAL_RELATION_CLASSES = frozenset({"structural", "operational", "administrative", "support", "coordination"})
FORBIDDEN_ORGANIZATION_FIELDS = frozenset({"parent_id", "parent_ref", "parentOrganizationId", "children"})
VERSIONED_REF_SEPARATOR = "@"
KIND_PROFILE_FIELDS = frozenset({"kind_ref", "profile_owner_ref", "relationship_class"})

ORGANIZATION_ERROR_CODES = frozenset({
    "ORGANIZATION_ID_REQUIRED", "ORGANIZATION_ID_DUPLICATE",
    "ORGANIZATION_CLASSIFICATION_ANNOTATIONS_INVALID", "ORGANIZATION_HISTORY_INVALID",
    "ORGANIZATION_TRANSITION_INCOMPLETE", "ORGANIZATION_TRANSITION_REF_MISMATCH",
    "ORGANIZATION_TRANSITION_ID_DUPLICATE", "ORGANIZATION_TRANSITION_TIME_ORDER",
    "ORGANIZATION_LIFECYCLE_STAGE_MISMATCH", "ORGANIZATION_ESTABLISHED_AT_MISMATCH",
    "ORGANIZATION_RETIRED_AT_MISMATCH", "ORGANIZATION_ESTABLISHMENT_PROVENANCE_REF_MISMATCH",
    "ORGANIZATION_CREATED_AFTER_TRANSITION", "ORGANIZATION_UNIVERSAL_HIERARCHY_FIELD",
    "ORGANIZATION_RELATIONSHIP_ID_REQUIRED", "ORGANIZATION_RELATIONSHIP_ID_DUPLICATE",
    "ORGANIZATION_RELATIONSHIP_CLASS_INVALID", "ORGANIZATION_RELATIONSHIP_TYPE_REQUIRED",
    "ORGANIZATION_RELATIONSHIP_KIND_PROFILE_INVALID", "ORGANIZATION_RELATIONSHIP_TYPE_UNRESOLVED",
    "ORGANIZATION_RELATIONSHIP_TYPE_CLASS_MISMATCH", "ORGANIZATION_RELATIONSHIP_ENDPOINTS_REQUIRED",
    "ORGANIZATION_RELATIONSHIP_ENDPOINT_UNRESOLVED", "ORGANIZATION_RELATIONSHIP_SELF_REFERENCE",
    "ORGANIZATION_RELATIONSHIP_HISTORY_INVALID", "ORGANIZATION_RELATIONSHIP_TRANSITION_INCOMPLETE",
    "ORGANIZATION_RELATIONSHIP_TRANSITION_REF_MISMATCH", "ORGANIZATION_RELATIONSHIP_TRANSITION_ID_DUPLICATE",
    "ORGANIZATION_RELATIONSHIP_TRANSITION_TIME_ORDER", "ORGANIZATION_RELATIONSHIP_LIFECYCLE_STAGE_MISMATCH",
    "ORGANIZATION_RELATIONSHIP_ESTABLISHED_AT_MISMATCH", "ORGANIZATION_RELATIONSHIP_TERMINAL_AT_MISMATCH",
    "ORGANIZATION_RELATIONSHIP_ESTABLISHMENT_PROVENANCE_REF_MISMATCH",
    "ORGANIZATION_RELATIONSHIP_VALIDITY_START_REQUIRED", "ORGANIZATION_RELATIONSHIP_VALIDITY_INTERVAL_INVALID",
    "ORGANIZATION_RELATIONSHIP_CREATED_AFTER_TRANSITION", "ORGANIZATION_RELATIONSHIP_SELF_SUPERSESSION",
    "ORGANIZATION_RELATIONSHIP_SUPERSESSION_TARGET_UNRESOLVED",
    "ORGANIZATION_RELATIONSHIP_SUPERSESSION_CYCLE", "ORGANIZATION_STRUCTURAL_SCHEME_REQUIRED",
    "ORGANIZATION_STRUCTURAL_VALIDATION_SCOPE_REQUIRED", "ORGANIZATION_STRUCTURAL_CYCLE",
    "ORGANIZATION_MULTIPLE_STRUCTURAL_SUPERIORS", "ORGANIZATION_Q2_FIXTURE_INVALID",
})
ORGANIZATION_DERIVATION_RULES = frozenset({
    "organization_established_at",
    "organization_relationship_effective_at",
    "organization_relationship_successor_ids",
})


def _duplicates(values: Iterable[Any]) -> bool:
    normalized = [str(value) for value in values if nonempty(value)]
    return len(normalized) != len(set(normalized))


def _exact_matches(records: Iterable[dict[str, Any]], field: str, reference: Any) -> list[dict[str, Any]]:
    if not nonempty(reference):
        return []
    return [record for record in records if isinstance(record, dict) and record.get(field) == reference]


def organization_projections(entity: dict[str, Any]) -> dict[str, Any]:
    history = entity.get("transition_history") or []
    established = transition(history, "Draft", "Established")
    retired = transition(history, "Established", "Retired")
    return {
        "lifecycle_stage": history[-1].get("to_stage") if history else "Draft",
        "established_at": established.get("occurred_at") if established else None,
        "retired_at": retired.get("occurred_at") if retired else None,
        "establishment_provenance_ref": established.get("provenance_ref") if established else None,
    }


def relationship_projections(entity: dict[str, Any]) -> dict[str, Any]:
    history = entity.get("transition_history") or []
    established = transition(history, "Draft", "Established")
    terminal = transition(history, "Established", "Closed") or transition(history, "Established", "Revoked")
    return {
        "lifecycle_stage": history[-1].get("to_stage") if history else "Draft",
        "established_at": established.get("occurred_at") if established else None,
        "terminal_at": terminal.get("occurred_at") if terminal else None,
        "establishment_provenance_ref": established.get("provenance_ref") if established else None,
    }


def validate_organization(entity: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    oid = entity.get("organization_id")
    if not nonempty(oid):
        errors.append("ORGANIZATION_ID_REQUIRED")
    annotations = entity.get("classification_refs")
    if annotations is not None and (
        not isinstance(annotations, list) or any(not nonempty(item) for item in annotations)
    ):
        errors.append("ORGANIZATION_CLASSIFICATION_ANNOTATIONS_INVALID")
    history = entity.get("transition_history") or []
    if not isinstance(history, list) or signature(history) not in ORGANIZATION_PATHS:
        errors.append("ORGANIZATION_HISTORY_INVALID")
        history = history if isinstance(history, list) else []
    for record in history:
        required = ("transition_id", "organization_ref", "from_stage", "to_stage", "occurred_at", "provenance_ref")
        if not all(nonempty(record.get(key)) for key in required):
            errors.append("ORGANIZATION_TRANSITION_INCOMPLETE")
            break
        if record.get("organization_ref") != oid:
            errors.append("ORGANIZATION_TRANSITION_REF_MISMATCH")
            break
    if _duplicates(record.get("transition_id") for record in history):
        errors.append("ORGANIZATION_TRANSITION_ID_DUPLICATE")
    if history and not times_non_decreasing(history):
        errors.append("ORGANIZATION_TRANSITION_TIME_ORDER")
    errors.extend(projection_mismatches(entity, organization_projections(entity), "ORGANIZATION"))
    created = parse_time(entity.get("created_at"))
    first = parse_time(history[0].get("occurred_at")) if history else None
    if first is not None and (created is None or created > first):
        errors.append("ORGANIZATION_CREATED_AFTER_TRANSITION")
    if FORBIDDEN_ORGANIZATION_FIELDS.intersection(entity):
        errors.append("ORGANIZATION_UNIVERSAL_HIERARCHY_FIELD")
    return result(errors)


def relationship_class(entity: dict[str, Any]) -> str:
    return str(entity.get("relationship_class", ""))


def _profile_valid(profile: Any) -> bool:
    return (
        isinstance(profile, dict)
        and set(profile) == KIND_PROFILE_FIELDS
        and nonempty(profile.get("kind_ref"))
        and VERSIONED_REF_SEPARATOR in str(profile.get("kind_ref"))
        and nonempty(profile.get("profile_owner_ref"))
        and relationship_class(profile) in INITIAL_RELATION_CLASSES
    )


def validate_organization_relationship(
    entity: dict[str, Any],
    organizations: Iterable[dict[str, Any]] = (),
    relationship_kind_profiles: Iterable[dict[str, Any]] = (),
) -> ValidationResult:
    errors: list[str] = []
    rid = entity.get("relationship_id")
    if not nonempty(rid):
        errors.append("ORGANIZATION_RELATIONSHIP_ID_REQUIRED")
    history = entity.get("transition_history") or []
    if not isinstance(history, list) or signature(history) not in RELATIONSHIP_PATHS:
        errors.append("ORGANIZATION_RELATIONSHIP_HISTORY_INVALID")
        history = history if isinstance(history, list) else []
    for record in history:
        required = ("transition_id", "relationship_ref", "from_stage", "to_stage", "occurred_at", "provenance_ref")
        if not all(nonempty(record.get(key)) for key in required):
            errors.append("ORGANIZATION_RELATIONSHIP_TRANSITION_INCOMPLETE")
            break
        if record.get("relationship_ref") != rid:
            errors.append("ORGANIZATION_RELATIONSHIP_TRANSITION_REF_MISMATCH")
            break
    if _duplicates(record.get("transition_id") for record in history):
        errors.append("ORGANIZATION_RELATIONSHIP_TRANSITION_ID_DUPLICATE")
    if history and not times_non_decreasing(history):
        errors.append("ORGANIZATION_RELATIONSHIP_TRANSITION_TIME_ORDER")
    errors.extend(projection_mismatches(entity, relationship_projections(entity), "ORGANIZATION_RELATIONSHIP"))

    stage = relationship_projections(entity)["lifecycle_stage"]
    cls = relationship_class(entity)
    if stage in {"Established", "Closed", "Revoked"}:
        if cls not in INITIAL_RELATION_CLASSES:
            errors.append("ORGANIZATION_RELATIONSHIP_CLASS_INVALID")
        type_ref = entity.get("relationship_type_ref")
        if not nonempty(type_ref) or VERSIONED_REF_SEPARATOR not in str(type_ref):
            errors.append("ORGANIZATION_RELATIONSHIP_TYPE_REQUIRED")
        elif cls in INITIAL_RELATION_CLASSES:
            profiles = list(relationship_kind_profiles)
            matches = _exact_matches(profiles, "kind_ref", type_ref)
            if any(not _profile_valid(profile) for profile in matches):
                errors.append("ORGANIZATION_RELATIONSHIP_KIND_PROFILE_INVALID")
            if len(matches) != 1:
                errors.append("ORGANIZATION_RELATIONSHIP_TYPE_UNRESOLVED")
            elif _profile_valid(matches[0]) and relationship_class(matches[0]) != cls:
                errors.append("ORGANIZATION_RELATIONSHIP_TYPE_CLASS_MISMATCH")

        source = entity.get("source_organization_ref")
        target = entity.get("target_organization_ref")
        if not nonempty(source) or not nonempty(target):
            errors.append("ORGANIZATION_RELATIONSHIP_ENDPOINTS_REQUIRED")
        elif organizations:
            if len(_exact_matches(organizations, "organization_id", source)) != 1 or len(
                _exact_matches(organizations, "organization_id", target)
            ) != 1:
                errors.append("ORGANIZATION_RELATIONSHIP_ENDPOINT_UNRESOLVED")
        else:
            errors.append("ORGANIZATION_RELATIONSHIP_ENDPOINT_UNRESOLVED")
        if cls in INITIAL_RELATION_CLASSES and source == target:
            errors.append("ORGANIZATION_RELATIONSHIP_SELF_REFERENCE")
        if parse_time(entity.get("validity_start")) is None:
            errors.append("ORGANIZATION_RELATIONSHIP_VALIDITY_START_REQUIRED")
        if cls == "structural" and not nonempty(entity.get("scheme_ref")):
            errors.append("ORGANIZATION_STRUCTURAL_SCHEME_REQUIRED")

    start = parse_time(entity.get("validity_start"))
    end = parse_time(entity.get("validity_end"))
    if end is not None and (start is None or start >= end):
        errors.append("ORGANIZATION_RELATIONSHIP_VALIDITY_INTERVAL_INVALID")
    created = parse_time(entity.get("created_at"))
    first = parse_time(history[0].get("occurred_at")) if history else None
    if first is not None and (created is None or created > first):
        errors.append("ORGANIZATION_RELATIONSHIP_CREATED_AFTER_TRANSITION")
    if entity.get("supersedes_relationship_ref") == rid:
        errors.append("ORGANIZATION_RELATIONSHIP_SELF_SUPERSESSION")
    return result(errors)


def organization_established_at(entity: dict[str, Any], at: str) -> bool:
    moment = parse_time(at)
    projection = organization_projections(entity)
    established = parse_time(projection["established_at"])
    retired = parse_time(projection["retired_at"])
    return bool(moment and established and established <= moment and (retired is None or moment < retired))


def organization_relationship_effective_at(entity: dict[str, Any], at: str) -> bool:
    moment = parse_time(at)
    projection = relationship_projections(entity)
    established = parse_time(projection["established_at"])
    terminal = parse_time(projection["terminal_at"])
    start = parse_time(entity.get("validity_start"))
    end = parse_time(entity.get("validity_end"))
    return bool(
        moment and established and start and established <= moment and start <= moment
        and (end is None or moment < end) and (terminal is None or moment < terminal)
    )


def _graph_errors(records: Iterable[dict[str, Any]], at: str) -> list[str]:
    effective = [
        record for record in records
        if relationship_class(record) == "structural" and organization_relationship_effective_at(record, at)
    ]
    errors: list[str] = []
    by_scheme: dict[str, list[dict[str, Any]]] = {}
    for record in effective:
        by_scheme.setdefault(str(record.get("scheme_ref")), []).append(record)
    for scheme_records in by_scheme.values():
        parents: dict[str, set[str]] = {}
        adjacency: dict[str, set[str]] = {}
        for record in scheme_records:
            source = str(record.get("source_organization_ref"))
            target = str(record.get("target_organization_ref"))
            parents.setdefault(source, set()).add(target)
            adjacency.setdefault(source, set()).add(target)
        if any(len(values) > 1 for values in parents.values()):
            errors.append("ORGANIZATION_MULTIPLE_STRUCTURAL_SUPERIORS")
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(node: str) -> bool:
            if node in visiting:
                return True
            if node in visited:
                return False
            visiting.add(node)
            if any(visit(target) for target in adjacency.get(node, set())):
                return True
            visiting.remove(node)
            visited.add(node)
            return False

        if any(visit(node) for node in list(adjacency)):
            errors.append("ORGANIZATION_STRUCTURAL_CYCLE")
    return errors


def graph_breakpoints(records: Iterable[dict[str, Any]]) -> list[str]:
    points = set()
    for record in records:
        if relationship_class(record) != "structural":
            continue
        projection = relationship_projections(record)
        for value in (projection["established_at"], record.get("validity_start"), record.get("validity_end"), projection["terminal_at"]):
            moment = parse_time(value)
            if moment is not None:
                points.add(moment)
    ordered = sorted(points)
    samples = set(ordered)
    for left, right in zip(ordered, ordered[1:]):
        if left < right:
            samples.add(left + (right - left) / 2)
    return [moment.isoformat() for moment in sorted(samples)]


def validate_organization_graph(records: Iterable[dict[str, Any]], reference_time: str | None = None) -> ValidationResult:
    items = list(records)
    times = [reference_time] if reference_time else graph_breakpoints(items)
    errors: list[str] = []
    for at in times:
        errors.extend(_graph_errors(items, str(at)))
    return result(errors)


def _supersession_errors(records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    ids = [record.get("relationship_id") for record in records]
    adjacency: dict[str, set[str]] = {}
    for record in records:
        predecessor = record.get("supersedes_relationship_ref")
        if not nonempty(predecessor):
            continue
        if ids.count(predecessor) != 1:
            errors.append("ORGANIZATION_RELATIONSHIP_SUPERSESSION_TARGET_UNRESOLVED")
            continue
        adjacency.setdefault(str(record.get("relationship_id")), set()).add(str(predecessor))
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        if any(visit(target) for target in adjacency.get(node, set())):
            return True
        visiting.remove(node)
        visited.add(node)
        return False

    if any(visit(node) for node in list(adjacency)):
        errors.append("ORGANIZATION_RELATIONSHIP_SUPERSESSION_CYCLE")
    return errors


def validate_organization_dataset(
    organizations: Iterable[dict[str, Any]],
    relationships: Iterable[dict[str, Any]],
    relationship_kind_profiles: Iterable[dict[str, Any]],
    validation_scope_ref: Any,
) -> ValidationResult:
    organization_records = list(organizations)
    relationship_records = list(relationships)
    profiles = list(relationship_kind_profiles)
    errors: list[str] = []
    for record in organization_records:
        errors.extend(validate_organization(record).errors)
    for record in relationship_records:
        errors.extend(validate_organization_relationship(record, organization_records, profiles).errors)
    if _duplicates(record.get("organization_id") for record in organization_records):
        errors.append("ORGANIZATION_ID_DUPLICATE")
    if _duplicates(
        transition_record.get("transition_id")
        for record in organization_records
        for transition_record in (record.get("transition_history") or [])
    ):
        errors.append("ORGANIZATION_TRANSITION_ID_DUPLICATE")
    if _duplicates(record.get("relationship_id") for record in relationship_records):
        errors.append("ORGANIZATION_RELATIONSHIP_ID_DUPLICATE")
    if _duplicates(
        transition_record.get("transition_id")
        for record in relationship_records
        for transition_record in (record.get("transition_history") or [])
    ):
        errors.append("ORGANIZATION_RELATIONSHIP_TRANSITION_ID_DUPLICATE")
    if any(relationship_class(record) == "structural" for record in relationship_records):
        if not nonempty(validation_scope_ref):
            errors.append("ORGANIZATION_STRUCTURAL_VALIDATION_SCOPE_REQUIRED")
    errors.extend(_supersession_errors(relationship_records))
    errors.extend(validate_organization_graph(relationship_records).errors)
    return result(errors)


def validate_organization_relationship_fixture(fixture: dict[str, Any]) -> ValidationResult:
    references = fixture.get("references") or {}
    return validate_organization_dataset(
        references.get("organizations") or [],
        [fixture.get("entity") or {}],
        references.get("relationship_kind_profiles") or [],
        fixture.get("validation_scope_ref"),
    )


def validate_organization_dataset_fixture(fixture: dict[str, Any]) -> ValidationResult:
    return validate_organization_dataset(
        fixture.get("organizations") or [],
        fixture.get("relationships") or [],
        fixture.get("relationship_kind_profiles") or [],
        fixture.get("validation_scope_ref"),
    )


def validate_organization_q2_fixture(fixture: dict[str, Any]) -> ValidationResult:
    cases = fixture.get("cases")
    if not isinstance(cases, dict) or not cases:
        return result(["ORGANIZATION_Q2_FIXTURE_INVALID"])
    for case in cases.values():
        if not isinstance(case, dict) or not isinstance(case.get("expected_error_codes"), list):
            return result(["ORGANIZATION_Q2_FIXTURE_INVALID"])
        actual = validate_organization_dataset(
            case.get("organizations") or [],
            case.get("relationships") or [],
            case.get("relationship_kind_profiles") or [],
            case.get("validation_scope_ref"),
        )
        if set(actual.errors) != set(case["expected_error_codes"]):
            return result(["ORGANIZATION_Q2_FIXTURE_INVALID"])
    return result([])


def organization_relationship_successor_ids(
    records: Iterable[dict[str, Any]], predecessor_ref: str
) -> tuple[str, ...]:
    """Return every exact successor ID; this is history visibility, never a head election."""
    return tuple(sorted(
        str(record.get("relationship_id"))
        for record in records
        if record.get("supersedes_relationship_ref") == predecessor_ref and nonempty(record.get("relationship_id"))
    ))
