from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .checker import ValidationResult, validate_resource


INTERCHANGEABILITY_ERROR_CODES = frozenset(
    {
        "INTERCHANGEABILITY_REQUIREMENT_ID_REQUIRED",
        "INTERCHANGEABILITY_REQUIREMENT_VERSION_REQUIRED",
        "INTERCHANGEABILITY_REQUIREMENT_OWNER_REQUIRED",
        "INTERCHANGEABILITY_REQUIREMENT_CONTEXT_REQUIRED",
        "INTERCHANGEABILITY_REQUIREMENT_PROVENANCE_REQUIRED",
        "INTERCHANGEABILITY_REQUIREMENT_INTERVAL_INVALID",
        "INTERCHANGEABILITY_CAPABILITY_BINDINGS_INVALID",
        "INTERCHANGEABILITY_CAPABILITY_BINDING_DUPLICATE",
        "INTERCHANGEABILITY_REQUIREMENT_DUPLICATE",
        "INTERCHANGEABILITY_TARGET_UNRESOLVED",
        "INTERCHANGEABILITY_FORBIDDEN_COUPLING",
        "COORDINATION_REQUIREMENT_OWNER_MISMATCH",
    }
)

INTERCHANGEABILITY_DERIVATION_RULES = frozenset(
    {
        "derive_resource_interchangeability",
        "resolve_interchangeability_requirement",
    }
)

RULE_REF = "resource-interchangeability@1"
COORDINATION_OWNER_REF = "ocp-coordination-consumer@0.1.0"
CLAIM_PROJECTIONS = frozenset({"positive", "negative", "indeterminate", "withdrawn"})
CLAIM_INPUT_STATES = frozenset(
    {"effective", "missing", "stale", "ambiguous", "conflicting", "unresolved"}
)
CONSTRAINT_DECISIONS = frozenset({"admissible", "inadmissible", "review_required"})
FORBIDDEN_COUPLING_KEYS = frozenset(
    {
        "available",
        "availability",
        "authorized",
        "authorization",
        "selected",
        "selection",
        "ranking",
        "score",
        "replacement_instruction",
        "assignment_mutation",
        "new_assignment",
        "equivalent_resource_ref",
        "interchangeable_with",
    }
)


def _result(errors: Iterable[str]) -> ValidationResult:
    return ValidationResult(tuple(dict.fromkeys(errors)))


def _nonempty(value: Any) -> str | None:
    if value is None or not str(value).strip():
        return None
    return str(value).strip()


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


def _capability_key(value: Any) -> tuple[str, str, str] | None:
    if not isinstance(value, dict):
        return None
    namespace = _nonempty(value.get("namespace"))
    capability_id = _nonempty(value.get("capability_id"))
    version = _nonempty(value.get("version"))
    if None in (namespace, capability_id, version):
        return None
    return namespace, capability_id, version


def _binding_key(value: Any) -> tuple[tuple[str, str, str], str] | None:
    if not isinstance(value, dict):
        return None
    capability = _capability_key(value.get("capability_ref"))
    condition = _nonempty(value.get("condition_set_ref"))
    if capability is None or condition is None or "@" not in condition:
        return None
    return capability, condition


def requirement_ref(requirement: dict[str, Any]) -> str | None:
    requirement_id = _nonempty(requirement.get("requirement_id"))
    version = _nonempty(requirement.get("version"))
    if requirement_id is None or version is None:
        return None
    return f"{requirement_id}@{version}"


def validate_interchangeability_requirement(requirement: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    if _nonempty(requirement.get("requirement_id")) is None:
        errors.append("INTERCHANGEABILITY_REQUIREMENT_ID_REQUIRED")
    if _nonempty(requirement.get("version")) is None:
        errors.append("INTERCHANGEABILITY_REQUIREMENT_VERSION_REQUIRED")
    if _nonempty(requirement.get("owner_ref")) is None:
        errors.append("INTERCHANGEABILITY_REQUIREMENT_OWNER_REQUIRED")
    if _nonempty(requirement.get("context_ref")) is None:
        errors.append("INTERCHANGEABILITY_REQUIREMENT_CONTEXT_REQUIRED")
    if _nonempty(requirement.get("provenance_ref")) is None:
        errors.append("INTERCHANGEABILITY_REQUIREMENT_PROVENANCE_REQUIRED")

    start = _parse_time(requirement.get("effective_from"))
    end = _parse_time(requirement.get("effective_until"))
    if start is None or (end is not None and start >= end):
        errors.append("INTERCHANGEABILITY_REQUIREMENT_INTERVAL_INVALID")

    bindings = requirement.get("capability_bindings")
    if not isinstance(bindings, list) or not bindings:
        errors.append("INTERCHANGEABILITY_CAPABILITY_BINDINGS_INVALID")
    else:
        keys = [_binding_key(binding) for binding in bindings]
        if any(key is None for key in keys):
            errors.append("INTERCHANGEABILITY_CAPABILITY_BINDINGS_INVALID")
        elif len(keys) != len(set(keys)):
            errors.append("INTERCHANGEABILITY_CAPABILITY_BINDING_DUPLICATE")

    if any(
        key in requirement and requirement.get(key) not in (None, False, "", [], {})
        for key in FORBIDDEN_COUPLING_KEYS
    ):
        errors.append("INTERCHANGEABILITY_FORBIDDEN_COUPLING")
    return _result(errors)


def validate_coordination_requirement(requirement: dict[str, Any]) -> ValidationResult:
    """Validate the accepted OCP-014 profile without treating caller identity as authority."""
    errors = list(validate_interchangeability_requirement(requirement).errors)
    if _nonempty(requirement.get("owner_ref")) != COORDINATION_OWNER_REF:
        errors.append("COORDINATION_REQUIREMENT_OWNER_MISMATCH")
    return _result(errors)


def resolve_interchangeability_requirement(
    requirements: Iterable[dict[str, Any]], exact_ref: Any
) -> dict[str, Any] | None:
    normalized = _nonempty(exact_ref)
    matches = [
        item
        for item in requirements
        if isinstance(item, dict)
        and requirement_ref(item) == normalized
        and validate_interchangeability_requirement(item).valid
    ]
    return matches[0] if len(matches) == 1 else None


def validate_interchangeability_dataset(
    requirements: Iterable[dict[str, Any]], *, resources: Iterable[dict[str, Any]] = ()
) -> ValidationResult:
    errors: list[str] = []
    entries = list(requirements)
    refs: list[str] = []
    resource_ids = {
        item.get("resource_id")
        for item in resources
        if isinstance(item, dict) and validate_resource(item).valid
    }
    for requirement in entries:
        if not isinstance(requirement, dict):
            errors.append("INTERCHANGEABILITY_REQUIREMENT_ID_REQUIRED")
            continue
        errors.extend(validate_interchangeability_requirement(requirement).errors)
        exact_ref = requirement_ref(requirement)
        if exact_ref is not None:
            refs.append(exact_ref)
        target_ref = _nonempty(requirement.get("comparison_target_ref"))
        if target_ref is not None and target_ref not in resource_ids:
            errors.append("INTERCHANGEABILITY_TARGET_UNRESOLVED")
    if len(refs) != len(set(refs)):
        errors.append("INTERCHANGEABILITY_REQUIREMENT_DUPLICATE")
    return _result(errors)


def _requirement_effective(requirement: dict[str, Any], at: Any) -> bool:
    moment = _parse_time(at)
    start = _parse_time(requirement.get("effective_from"))
    end = _parse_time(requirement.get("effective_until"))
    return bool(
        moment is not None
        and start is not None
        and start <= moment
        and (end is None or moment < end)
    )


def derive_resource_interchangeability(
    evaluation: dict[str, Any], requirements: Iterable[dict[str, Any]]
) -> str:
    """Return contextual eligibility only; never permission, selection, or execution."""
    if not isinstance(evaluation, dict) or evaluation.get("rule_ref") != RULE_REF:
        return "indeterminate"
    if any(
        key in evaluation and evaluation.get(key) not in (None, False, "", [], {})
        for key in FORBIDDEN_COUPLING_KEYS
    ):
        return "indeterminate"

    requirement = resolve_interchangeability_requirement(
        requirements, evaluation.get("requirement_ref")
    )
    candidate_ref = _nonempty(evaluation.get("candidate_ref"))
    context_ref = _nonempty(evaluation.get("context_ref"))
    at = evaluation.get("evaluation_time")
    if (
        requirement is None
        or candidate_ref is None
        or context_ref != _nonempty(requirement.get("context_ref"))
        or not _requirement_effective(requirement, at)
        or _nonempty(evaluation.get("input_snapshot_ref")) is None
    ):
        return "indeterminate"

    constraint = evaluation.get("constraint_input")
    if not isinstance(constraint, dict):
        return "indeterminate"
    if (
        _nonempty(constraint.get("candidate_ref")) != candidate_ref
        or _nonempty(constraint.get("context_ref")) != context_ref
        or _parse_time(constraint.get("evaluated_at")) != _parse_time(at)
        or _nonempty(constraint.get("input_snapshot_ref")) is None
    ):
        return "indeterminate"
    decision = constraint.get("decision")
    if decision not in CONSTRAINT_DECISIONS:
        return "indeterminate"

    claims = evaluation.get("claim_inputs")
    if not isinstance(claims, list):
        return "indeterminate"
    claim_index: dict[tuple[tuple[str, str, str], str], list[dict[str, Any]]] = {}
    for claim in claims:
        key = _binding_key(claim)
        if key is not None:
            claim_index.setdefault(key, []).append(claim)

    saw_negative = decision == "inadmissible"
    saw_review = decision == "review_required"
    saw_indeterminate = False
    for binding in requirement["capability_bindings"]:
        key = _binding_key(binding)
        matches = claim_index.get(key, []) if key is not None else []
        if len(matches) != 1:
            saw_indeterminate = True
            continue
        claim = matches[0]
        if (
            _nonempty(claim.get("holder_ref")) != candidate_ref
            or _parse_time(claim.get("effective_at")) != _parse_time(at)
            or not isinstance(claim.get("claim_head_refs"), list)
            or not claim.get("claim_head_refs")
            or _nonempty(claim.get("claimant_ref")) is None
        ):
            saw_indeterminate = True
            continue
        state = claim.get("input_state")
        projection = claim.get("projection")
        if state not in CLAIM_INPUT_STATES or projection not in CLAIM_PROJECTIONS:
            saw_indeterminate = True
        elif state != "effective" or projection in {"indeterminate", "withdrawn"}:
            saw_indeterminate = True
        else:
            if projection == "negative":
                saw_negative = True
            if claim.get("requires_review") is True:
                saw_review = True

    if saw_indeterminate:
        return "indeterminate"
    if saw_review:
        return "review_required"
    if saw_negative:
        return "negative"
    return "positive"


def validate_interchangeability_fixture(fixture: dict[str, Any]) -> ValidationResult:
    return validate_interchangeability_dataset(
        fixture.get("requirements") or [], resources=fixture.get("resources") or []
    )
