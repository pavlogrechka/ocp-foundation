from __future__ import annotations

from datetime import timedelta
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

ORGANIZATION_ERROR_CODES = frozenset({
    "ORGANIZATION_ID_REQUIRED", "ORGANIZATION_CLASSIFICATION_REQUIRED", "ORGANIZATION_HISTORY_INVALID",
    "ORGANIZATION_TRANSITION_INCOMPLETE", "ORGANIZATION_TRANSITION_REF_MISMATCH",
    "ORGANIZATION_TRANSITION_TIME_ORDER", "ORGANIZATION_LIFECYCLE_STAGE_MISMATCH",
    "ORGANIZATION_ESTABLISHED_AT_MISMATCH", "ORGANIZATION_RETIRED_AT_MISMATCH",
    "ORGANIZATION_ESTABLISHMENT_PROVENANCE_REF_MISMATCH", "ORGANIZATION_CREATED_AFTER_TRANSITION",
    "ORGANIZATION_UNIVERSAL_HIERARCHY_FIELD", "ORGANIZATION_RELATIONSHIP_ID_REQUIRED",
    "ORGANIZATION_RELATIONSHIP_CLASS_INVALID", "ORGANIZATION_RELATIONSHIP_TYPE_REQUIRED",
    "ORGANIZATION_RELATIONSHIP_ENDPOINTS_REQUIRED", "ORGANIZATION_RELATIONSHIP_SELF_REFERENCE",
    "ORGANIZATION_RELATIONSHIP_HISTORY_INVALID", "ORGANIZATION_RELATIONSHIP_TRANSITION_INCOMPLETE",
    "ORGANIZATION_RELATIONSHIP_TRANSITION_REF_MISMATCH", "ORGANIZATION_RELATIONSHIP_TRANSITION_TIME_ORDER",
    "ORGANIZATION_RELATIONSHIP_LIFECYCLE_STAGE_MISMATCH", "ORGANIZATION_RELATIONSHIP_ESTABLISHED_AT_MISMATCH",
    "ORGANIZATION_RELATIONSHIP_TERMINAL_AT_MISMATCH",
    "ORGANIZATION_RELATIONSHIP_ESTABLISHMENT_PROVENANCE_REF_MISMATCH",
    "ORGANIZATION_RELATIONSHIP_VALIDITY_START_REQUIRED", "ORGANIZATION_RELATIONSHIP_VALIDITY_INTERVAL_INVALID",
    "ORGANIZATION_RELATIONSHIP_CREATED_AFTER_TRANSITION", "ORGANIZATION_RELATIONSHIP_SELF_SUPERSESSION",
    "ORGANIZATION_STRUCTURAL_SCHEME_REQUIRED", "ORGANIZATION_STRUCTURAL_CYCLE",
    "ORGANIZATION_MULTIPLE_STRUCTURAL_SUPERIORS",
})
ORGANIZATION_DERIVATION_RULES = frozenset({"organization_established_at", "organization_relationship_effective_at"})


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
    if not nonempty(oid): errors.append("ORGANIZATION_ID_REQUIRED")
    history = entity.get("transition_history") or []
    if not isinstance(history, list) or signature(history) not in ORGANIZATION_PATHS:
        errors.append("ORGANIZATION_HISTORY_INVALID"); history = history if isinstance(history, list) else []
    for record in history:
        required = ("transition_id", "organization_ref", "from_stage", "to_stage", "occurred_at", "provenance_ref")
        if not all(nonempty(record.get(k)) for k in required): errors.append("ORGANIZATION_TRANSITION_INCOMPLETE"); break
        if record.get("organization_ref") != oid: errors.append("ORGANIZATION_TRANSITION_REF_MISMATCH"); break
    if history and not times_non_decreasing(history): errors.append("ORGANIZATION_TRANSITION_TIME_ORDER")
    projection = organization_projections(entity)
    errors.extend(projection_mismatches(entity, projection, "ORGANIZATION"))
    if projection["lifecycle_stage"] in {"Established", "Retired"}:
        refs = entity.get("classification_refs") or []
        if not isinstance(refs, list) or not any(nonempty(x) for x in refs): errors.append("ORGANIZATION_CLASSIFICATION_REQUIRED")
    created = parse_time(entity.get("created_at")); first = parse_time(history[0].get("occurred_at")) if history else None
    if first is not None and (created is None or created > first): errors.append("ORGANIZATION_CREATED_AFTER_TRANSITION")
    if FORBIDDEN_ORGANIZATION_FIELDS.intersection(entity): errors.append("ORGANIZATION_UNIVERSAL_HIERARCHY_FIELD")
    return result(errors)


def relationship_class(entity: dict[str, Any]) -> str:
    return str(entity.get("relationship_class", "")).strip().lower()


def validate_organization_relationship(entity: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    rid = entity.get("relationship_id")
    if not nonempty(rid): errors.append("ORGANIZATION_RELATIONSHIP_ID_REQUIRED")
    history = entity.get("transition_history") or []
    if not isinstance(history, list) or signature(history) not in RELATIONSHIP_PATHS:
        errors.append("ORGANIZATION_RELATIONSHIP_HISTORY_INVALID"); history = history if isinstance(history, list) else []
    for record in history:
        required = ("transition_id", "relationship_ref", "from_stage", "to_stage", "occurred_at", "provenance_ref")
        if not all(nonempty(record.get(k)) for k in required): errors.append("ORGANIZATION_RELATIONSHIP_TRANSITION_INCOMPLETE"); break
        if record.get("relationship_ref") != rid: errors.append("ORGANIZATION_RELATIONSHIP_TRANSITION_REF_MISMATCH"); break
    if history and not times_non_decreasing(history): errors.append("ORGANIZATION_RELATIONSHIP_TRANSITION_TIME_ORDER")
    projection = relationship_projections(entity)
    errors.extend(projection_mismatches(entity, projection, "ORGANIZATION_RELATIONSHIP"))
    stage = projection["lifecycle_stage"]
    cls = relationship_class(entity)
    if stage in {"Established", "Closed", "Revoked"}:
        if cls not in INITIAL_RELATION_CLASSES: errors.append("ORGANIZATION_RELATIONSHIP_CLASS_INVALID")
        type_ref = str(entity.get("relationship_type_ref", ""))
        if not nonempty(type_ref) or VERSIONED_REF_SEPARATOR not in type_ref: errors.append("ORGANIZATION_RELATIONSHIP_TYPE_REQUIRED")
        if not nonempty(entity.get("source_organization_ref")) or not nonempty(entity.get("target_organization_ref")):
            errors.append("ORGANIZATION_RELATIONSHIP_ENDPOINTS_REQUIRED")
        if cls in INITIAL_RELATION_CLASSES and entity.get("source_organization_ref") == entity.get("target_organization_ref"):
            errors.append("ORGANIZATION_RELATIONSHIP_SELF_REFERENCE")
        if parse_time(entity.get("validity_start")) is None: errors.append("ORGANIZATION_RELATIONSHIP_VALIDITY_START_REQUIRED")
        if cls == "structural" and not nonempty(entity.get("scheme_ref")): errors.append("ORGANIZATION_STRUCTURAL_SCHEME_REQUIRED")
    start = parse_time(entity.get("validity_start")); end = parse_time(entity.get("validity_end"))
    if end is not None and (start is None or start >= end): errors.append("ORGANIZATION_RELATIONSHIP_VALIDITY_INTERVAL_INVALID")
    created = parse_time(entity.get("created_at")); first = parse_time(history[0].get("occurred_at")) if history else None
    if first is not None and (created is None or created > first): errors.append("ORGANIZATION_RELATIONSHIP_CREATED_AFTER_TRANSITION")
    if entity.get("supersedes_relationship_ref") == rid: errors.append("ORGANIZATION_RELATIONSHIP_SELF_SUPERSESSION")
    return result(errors)


def organization_established_at(entity: dict[str, Any], at: str) -> bool:
    moment = parse_time(at); p = organization_projections(entity)
    established = parse_time(p["established_at"]); retired = parse_time(p["retired_at"])
    return bool(moment and established and established <= moment and (retired is None or moment < retired))


def organization_relationship_effective_at(entity: dict[str, Any], at: str) -> bool:
    moment = parse_time(at); p = relationship_projections(entity)
    established = parse_time(p["established_at"]); terminal = parse_time(p["terminal_at"])
    start = parse_time(entity.get("validity_start")); end = parse_time(entity.get("validity_end"))
    return bool(moment and established and start and established <= moment and start <= moment and (end is None or moment < end) and (terminal is None or moment < terminal))


def _graph_errors(records: Iterable[dict[str, Any]], at: str) -> list[str]:
    effective = [r for r in records if relationship_class(r) == "structural" and organization_relationship_effective_at(r, at)]
    errors: list[str] = []
    by_scheme: dict[str, list[dict[str, Any]]] = {}
    for r in effective: by_scheme.setdefault(str(r.get("scheme_ref")), []).append(r)
    for scheme_records in by_scheme.values():
        parents: dict[str, set[str]] = {}; adjacency: dict[str, set[str]] = {}
        for r in scheme_records:
            s, t = str(r.get("source_organization_ref")), str(r.get("target_organization_ref"))
            parents.setdefault(s, set()).add(t); adjacency.setdefault(s, set()).add(t)
        if any(len(v) > 1 for v in parents.values()): errors.append("ORGANIZATION_MULTIPLE_STRUCTURAL_SUPERIORS")
        visiting: set[str] = set(); visited: set[str] = set()
        def visit(node: str) -> bool:
            if node in visiting: return True
            if node in visited: return False
            visiting.add(node)
            if any(visit(t) for t in adjacency.get(node, set())): return True
            visiting.remove(node); visited.add(node); return False
        if any(visit(n) for n in list(adjacency)): errors.append("ORGANIZATION_STRUCTURAL_CYCLE")
    return errors


def graph_breakpoints(records: Iterable[dict[str, Any]]) -> list[str]:
    points = set()
    for r in records:
        if relationship_class(r) != "structural": continue
        p = relationship_projections(r)
        for value in (p["established_at"], r.get("validity_start"), r.get("validity_end"), p["terminal_at"]):
            dt = parse_time(value)
            if dt is not None: points.add(dt)
    ordered = sorted(points)
    samples = set(ordered)
    for left, right in zip(ordered, ordered[1:]):
        if left < right: samples.add(left + (right - left) / 2)
    return [x.isoformat() for x in sorted(samples)]


def validate_organization_graph(records: Iterable[dict[str, Any]], reference_time: str | None = None) -> ValidationResult:
    items = list(records)
    times = [reference_time] if reference_time else graph_breakpoints(items)
    errors: list[str] = []
    for at in times: errors.extend(_graph_errors(items, str(at)))
    return result(errors)
