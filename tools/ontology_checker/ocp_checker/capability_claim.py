from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .capability import resolve_capability_definition
from .checker import ValidationResult, validate_resource
from .assessment import validate_outcome_assessment
from .event import validate_event, validate_observation


CAPABILITY_CLAIM_ERROR_CODES = frozenset(
    {
        "CAPABILITY_CLAIM_ASSERTION_INVALID",
        "CAPABILITY_CLAIM_ACTIVATION_FIELDS_FORBIDDEN",
        "CAPABILITY_CLAIM_ACTIVATION_REQUIRED",
        "CAPABILITY_CLAIM_ACTIVATION_TIME_INVALID",
        "CAPABILITY_CLAIM_AMBIGUITY_RULE_INVALID",
        "CAPABILITY_CLAIM_AMBIGUITY_STATE_MISMATCH",
        "CAPABILITY_CLAIM_BINDING_MISMATCH",
        "CAPABILITY_CLAIM_CAPABILITY_REF_INVALID",
        "CAPABILITY_CLAIM_CAPABILITY_UNRESOLVED",
        "CAPABILITY_CLAIM_CLAIMANT_REQUIRED",
        "CAPABILITY_CLAIM_CONDITION_SET_REF_REQUIRED",
        "CAPABILITY_CLAIM_EVIDENCE_BINDINGS_INVALID",
        "CAPABILITY_CLAIM_EVIDENCE_EXPECTATION_INVALID",
        "CAPABILITY_CLAIM_EVIDENCE_EXPECTATION_REQUIRED",
        "CAPABILITY_CLAIM_EVIDENCE_KIND_UNSUPPORTED",
        "CAPABILITY_CLAIM_EVIDENCE_REFERENCE_UNRESOLVED",
        "CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_MISMATCH",
        "CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_REQUIRED",
        "CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_UNRESOLVED",
        "CAPABILITY_CLAIM_FORBIDDEN_COUPLING",
        "CAPABILITY_CLAIM_FRESHNESS_RULE_INVALID",
        "CAPABILITY_CLAIM_FRESHNESS_STATE_MISMATCH",
        "CAPABILITY_CLAIM_HOLDER_KIND_UNSUPPORTED",
        "CAPABILITY_CLAIM_HOLDER_REF_REQUIRED",
        "CAPABILITY_CLAIM_HOLDER_UNRESOLVED",
        "CAPABILITY_CLAIM_ID_REQUIRED",
        "CAPABILITY_CLAIM_IDENTITY_DUPLICATE",
        "CAPABILITY_CLAIM_INTERVAL_INVALID",
        "CAPABILITY_CLAIM_INPUT_SNAPSHOT_REQUIRED",
        "CAPABILITY_CLAIM_INPUT_SNAPSHOT_RULE_MISMATCH",
        "CAPABILITY_CLAIM_INPUT_SNAPSHOT_UNRESOLVED",
        "CAPABILITY_CLAIM_KIND_UNSUPPORTED",
        "CAPABILITY_CLAIM_PROVENANCE_REF_REQUIRED",
        "CAPABILITY_CLAIM_RECORDED_AT_REQUIRED",
        "CAPABILITY_CLAIM_SELF_SUPERSESSION",
        "CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH",
        "CAPABILITY_CLAIM_SUPPORT_STATE_INVALID",
        "CAPABILITY_CLAIM_SUPPORT_MODE_INVALID",
        "CAPABILITY_CLAIM_SUPPORT_MODE_TRANSITION_INVALID",
        "CAPABILITY_CLAIM_SUPERSESSION_CYCLE",
        "CAPABILITY_CLAIM_SUPERSESSION_TARGET_UNRESOLVED",
        "CAPABILITY_CLAIM_AUTHORITY_REF_REQUIRED",
        "CAPABILITY_CLAIM_EFFECTIVE_FROM_REQUIRED",
        "CAPABILITY_CLAIM_WITHDRAWAL_TARGET_REQUIRED",
        "CAPABILITY_CLAIM_TIME_ORDER_INVALID",
    }
)

CAPABILITY_CLAIM_DERIVATION_RULES = frozenset(
    {
        "capability_claim_effective_at",
        "capability_claim_heads",
        "derive_capability_claim_support_usability",
        "effective_capability_claim",
        "resolve_capability_claim",
    }
)

ACTIVATED_CLAIM_KIND = "holder-capability@2"
SUPPORTED_CLAIM_KINDS = frozenset({"holder-capability@1", ACTIVATED_CLAIM_KIND})
SUPPORTED_HOLDER_KINDS = frozenset({"resource@1"})
SUPPORTED_EVIDENCE_KINDS = frozenset(
    {"event@1", "observation-record@1", "outcome-assessment-record@1"}
)
ASSERTIONS = frozenset({"positive", "negative", "indeterminate", "withdrawn"})
SUPPORT_STATES = frozenset(
    {"declared", "sufficient", "missing", "stale", "ambiguous", "conflicting"}
)
NON_PERMISSIVE_SUPPORT_STATES = frozenset(
    {"missing", "stale", "ambiguous", "conflicting"}
)
SUPPORT_MODES = frozenset({"declaration-only", "evidence-backed"})
ACTIVATION_FIELDS = frozenset(
    {
        "support_mode",
        "evidence_expectation_ref",
        "input_snapshot_ref",
        "freshness_rule_ref",
        "freshness_state",
        "ambiguity_rule_ref",
        "ambiguity_state",
        "ambiguity_findings",
        "support_evaluated_at",
    }
)
EVIDENCE_MODE_FIELDS = ACTIVATION_FIELDS - {"support_mode"}
FRESHNESS_STATES = frozenset({"fresh", "stale", "indeterminate", "not_applicable"})
AMBIGUITY_STATES = frozenset({"clear", "ambiguous"})
AMBIGUITY_BASES = frozenset({"rule-derived", "attributable"})
TEMPORAL_DIMENSION = "temporal@1"
REFERENCE_DIMENSION = "reference@1"
PROTECTED_USE_REF = "capability-claim-source-projection@1"
TEMPORAL_FACT_FIELDS = {
    ("event@1", "event-occurred-at@1"): "occurred_at",
    ("observation-record@1", "observation-observed-at@1"): "observed_at",
    ("outcome-assessment-record@1", "assessment-evaluated-at@1"): "evaluated_at",
}
FORBIDDEN_COUPLING_KEYS = frozenset(
    {
        "organization_ref",
        "organization_refs",
        "readiness",
        "availability",
        "capacity",
        "authorization",
        "admissibility",
        "assignment_ref",
        "operation_ref",
        "interchangeable_with",
        "verified",
        "certified",
        "objective_truth",
        "current",
        "is_current",
        "latest",
    }
)


def _result(errors: Iterable[str]) -> ValidationResult:
    return ValidationResult(tuple(dict.fromkeys(errors)))


def _normalized_ref(value: Any) -> str | None:
    if value is None or not str(value).strip():
        return None
    return str(value).strip()


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


def _parse_strict_time(value: Any) -> datetime | None:
    if isinstance(value, datetime):
        parsed = value
    else:
        if not isinstance(value, str) or not value.strip():
            return None
        try:
            parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        except ValueError:
            return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed.astimezone(timezone.utc)


def _capability_key(value: Any) -> tuple[str, str, str] | None:
    if not isinstance(value, dict):
        return None
    namespace = _normalized_ref(value.get("namespace"))
    capability_id = _normalized_ref(value.get("capability_id"))
    version = _normalized_ref(value.get("version"))
    if None in (namespace, capability_id, version):
        return None
    return namespace, capability_id, version


def _normalized_binding(binding: Any) -> tuple[str, str] | None:
    if not isinstance(binding, dict):
        return None
    kind_ref = _normalized_ref(binding.get("evidence_kind_ref"))
    evidence_ref = _normalized_ref(binding.get("evidence_ref"))
    if kind_ref is None or evidence_ref is None or not _versioned_ref(kind_ref):
        return None
    return kind_ref, evidence_ref


def _normalized_bindings(value: Any) -> tuple[tuple[str, str], ...] | None:
    if not isinstance(value, list):
        return None
    normalized = [_normalized_binding(item) for item in value]
    if any(item is None for item in normalized):
        return None
    bindings = tuple(item for item in normalized if item is not None)
    if len(bindings) != len(set(bindings)):
        return None
    return tuple(sorted(bindings))


def _normalized_findings(value: Any) -> tuple[tuple[str, str, str], ...] | None:
    if not isinstance(value, list):
        return None
    findings: list[tuple[str, str, str]] = []
    for item in value:
        if not isinstance(item, dict):
            return None
        dimension_ref = _normalized_ref(item.get("dimension_ref"))
        reason_ref = _normalized_ref(item.get("reason_ref"))
        basis = _normalized_ref(item.get("basis"))
        if (
            dimension_ref is None
            or reason_ref is None
            or not _versioned_ref(dimension_ref)
            or not _versioned_ref(reason_ref)
            or basis not in AMBIGUITY_BASES
        ):
            return None
        findings.append((dimension_ref, reason_ref, basis))
    if len(findings) != len(set(findings)):
        return None
    return tuple(sorted(findings))


def _binding_identity(claim: dict[str, Any]) -> tuple[Any, ...]:
    return (
        _normalized_ref(claim.get("claim_kind_ref")),
        _normalized_ref(claim.get("holder_kind_ref")),
        _normalized_ref(claim.get("holder_ref")),
        _capability_key(claim.get("capability_ref")),
        _normalized_ref(claim.get("claimant_ref")),
        _normalized_ref(claim.get("condition_set_ref")),
    )


def validate_capability_claim(claim: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    claim_id = _normalized_ref(claim.get("claim_id"))
    if claim_id is None:
        errors.append("CAPABILITY_CLAIM_ID_REQUIRED")

    claim_kind_ref = _normalized_ref(claim.get("claim_kind_ref"))
    if claim_kind_ref not in SUPPORTED_CLAIM_KINDS:
        errors.append("CAPABILITY_CLAIM_KIND_UNSUPPORTED")
    if _normalized_ref(claim.get("holder_kind_ref")) not in SUPPORTED_HOLDER_KINDS:
        errors.append("CAPABILITY_CLAIM_HOLDER_KIND_UNSUPPORTED")
    if _normalized_ref(claim.get("holder_ref")) is None:
        errors.append("CAPABILITY_CLAIM_HOLDER_REF_REQUIRED")
    if _capability_key(claim.get("capability_ref")) is None:
        errors.append("CAPABILITY_CLAIM_CAPABILITY_REF_INVALID")
    if _normalized_ref(claim.get("claimant_ref")) is None:
        errors.append("CAPABILITY_CLAIM_CLAIMANT_REQUIRED")
    if not _versioned_ref(claim.get("condition_set_ref")):
        errors.append("CAPABILITY_CLAIM_CONDITION_SET_REF_REQUIRED")

    assertion = claim.get("assertion")
    if assertion not in ASSERTIONS:
        errors.append("CAPABILITY_CLAIM_ASSERTION_INVALID")

    support_state = claim.get("support_state")
    if support_state not in SUPPORT_STATES:
        errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_INVALID")

    support_mode = _normalized_ref(claim.get("support_mode"))
    if claim_kind_ref == ACTIVATED_CLAIM_KIND:
        if support_mode not in SUPPORT_MODES:
            errors.append("CAPABILITY_CLAIM_SUPPORT_MODE_INVALID")
        elif assertion == "withdrawn":
            if any(field in claim for field in EVIDENCE_MODE_FIELDS):
                errors.append("CAPABILITY_CLAIM_ACTIVATION_FIELDS_FORBIDDEN")
        elif support_mode == "declaration-only":
            if any(field in claim for field in EVIDENCE_MODE_FIELDS):
                errors.append("CAPABILITY_CLAIM_ACTIVATION_FIELDS_FORBIDDEN")
        else:
            findings = _normalized_findings(claim.get("ambiguity_findings"))
            if not _versioned_ref(claim.get("evidence_expectation_ref")):
                errors.append("CAPABILITY_CLAIM_EVIDENCE_EXPECTATION_REQUIRED")
            if _normalized_ref(claim.get("input_snapshot_ref")) is None:
                errors.append("CAPABILITY_CLAIM_INPUT_SNAPSHOT_REQUIRED")
            if (
                _normalized_ref(claim.get("input_snapshot_ref")) is None
                or not _versioned_ref(claim.get("evidence_expectation_ref"))
                or not _versioned_ref(claim.get("freshness_rule_ref"))
                or claim.get("freshness_state") not in FRESHNESS_STATES
                or not _versioned_ref(claim.get("ambiguity_rule_ref"))
                or claim.get("ambiguity_state") not in AMBIGUITY_STATES
                or findings is None
                or _normalized_ref(claim.get("support_evaluated_at")) is None
            ):
                errors.append("CAPABILITY_CLAIM_ACTIVATION_REQUIRED")
            if (
                _parse_strict_time(claim.get("support_evaluated_at")) is None
                or _parse_strict_time(claim.get("recorded_at")) is None
            ):
                errors.append("CAPABILITY_CLAIM_ACTIVATION_TIME_INVALID")
    elif any(field in claim for field in ACTIVATION_FIELDS):
        errors.append("CAPABILITY_CLAIM_ACTIVATION_FIELDS_FORBIDDEN")

    bindings = _normalized_bindings(claim.get("evidence_bindings"))
    if bindings is None:
        errors.append("CAPABILITY_CLAIM_EVIDENCE_BINDINGS_INVALID")
    elif any(kind_ref not in SUPPORTED_EVIDENCE_KINDS for kind_ref, _ in bindings):
        errors.append("CAPABILITY_CLAIM_EVIDENCE_KIND_UNSUPPORTED")
    else:
        snapshot_ref = _normalized_ref(claim.get("evidence_snapshot_ref"))
        if claim_kind_ref == ACTIVATED_CLAIM_KIND and assertion == "withdrawn":
            if bindings or support_state != "declared" or snapshot_ref is not None:
                errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")
        elif claim_kind_ref == ACTIVATED_CLAIM_KIND and support_mode == "declaration-only":
            if bindings or support_state != "declared" or snapshot_ref is not None:
                errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")
        elif claim_kind_ref == ACTIVATED_CLAIM_KIND and support_mode == "evidence-backed":
            if not bindings and support_state != "missing":
                errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")
            if bindings and support_state in {"declared", "missing"}:
                errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")
            if snapshot_ref is None:
                errors.append("CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_REQUIRED")
        elif not bindings:
            if support_state not in {"declared", "missing"}:
                errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")
            if snapshot_ref is not None:
                errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")
        else:
            if support_state in {"declared", "missing"}:
                errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")
            if snapshot_ref is None:
                errors.append("CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_REQUIRED")

    if _normalized_ref(claim.get("authority_ref")) is None:
        errors.append("CAPABILITY_CLAIM_AUTHORITY_REF_REQUIRED")
    if _normalized_ref(claim.get("provenance_ref")) is None:
        errors.append("CAPABILITY_CLAIM_PROVENANCE_REF_REQUIRED")
    if _parse_time(claim.get("recorded_at")) is None:
        errors.append("CAPABILITY_CLAIM_RECORDED_AT_REQUIRED")
    support_evaluated_at = _parse_strict_time(claim.get("support_evaluated_at"))
    recorded_at = _parse_strict_time(claim.get("recorded_at"))
    if (
        claim_kind_ref == ACTIVATED_CLAIM_KIND
        and support_mode == "evidence-backed"
        and assertion != "withdrawn"
        and support_evaluated_at is not None
        and recorded_at is not None
        and support_evaluated_at > recorded_at
    ):
        errors.append("CAPABILITY_CLAIM_TIME_ORDER_INVALID")

    effective_from = _parse_time(claim.get("effective_from"))
    effective_until = _parse_time(claim.get("effective_until"))
    if effective_from is None:
        errors.append("CAPABILITY_CLAIM_EFFECTIVE_FROM_REQUIRED")
    if effective_until is not None and (
        effective_from is None or effective_from >= effective_until
    ):
        errors.append("CAPABILITY_CLAIM_INTERVAL_INVALID")

    supersedes = _normalized_ref(claim.get("supersedes_claim_ref"))
    if claim_id is not None and supersedes == claim_id:
        errors.append("CAPABILITY_CLAIM_SELF_SUPERSESSION")
    if assertion == "withdrawn" and supersedes is None:
        errors.append("CAPABILITY_CLAIM_WITHDRAWAL_TARGET_REQUIRED")
    if (
        assertion == "withdrawn"
        and claim_kind_ref != ACTIVATED_CLAIM_KIND
        and (support_state != "declared" or bindings not in ((), None))
    ):
        errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")

    if any(
        key in claim and claim.get(key) not in (None, False, "", [], {})
        for key in FORBIDDEN_COUPLING_KEYS
    ):
        errors.append("CAPABILITY_CLAIM_FORBIDDEN_COUPLING")

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
        if target in graph and visit(target):
            return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in sorted(graph))


def _resolve_evidence_snapshot(
    value: Any, snapshot_ref: Any
) -> tuple[bool, tuple[tuple[str, str], ...] | None]:
    requested = _normalized_ref(snapshot_ref)
    if requested is None or not isinstance(value, list):
        return False, None
    candidates = [
        _normalized_bindings(item.get("evidence_bindings"))
        for item in value
        if isinstance(item, dict)
        and _normalized_ref(item.get("snapshot_ref")) == requested
    ]
    if len(candidates) != 1 or candidates[0] is None:
        return False, None
    return True, candidates[0]


def _resolve_input_snapshot(
    value: Any, snapshot_ref: Any
) -> tuple[bool, dict[str, Any] | None]:
    requested = _normalized_ref(snapshot_ref)
    if requested is None or not isinstance(value, list):
        return False, None
    candidates = [
        item
        for item in value
        if isinstance(item, dict)
        and _normalized_ref(item.get("snapshot_ref")) == requested
    ]
    if len(candidates) != 1:
        return False, None
    return True, candidates[0]


def _unique_record_index(
    entries: Iterable[dict[str, Any]], identity_field: str, validator: Any | None = None
) -> dict[str, dict[str, Any]]:
    candidates: dict[str, list[dict[str, Any]]] = {}
    for item in entries:
        if not isinstance(item, dict):
            continue
        identity = _normalized_ref(item.get(identity_field))
        if identity is not None:
            candidates.setdefault(identity, []).append(item)
    return {
        identity: items[0]
        for identity, items in candidates.items()
        if len(items) == 1
        and (validator is None or validator(items[0]).valid)
    }


def _freshness_policy_index(rule: Any) -> dict[str, dict[str, Any]] | None:
    if not isinstance(rule, dict):
        return None
    policies = rule.get("evidence_policies")
    if not isinstance(policies, list) or not policies:
        return None
    index: dict[str, dict[str, Any]] = {}
    for policy in policies:
        if not isinstance(policy, dict):
            return None
        kind_ref = _normalized_ref(policy.get("evidence_kind_ref"))
        fact_ref = _normalized_ref(policy.get("temporal_fact_ref"))
        maximum = policy.get("max_age_seconds")
        if (
            kind_ref not in SUPPORTED_EVIDENCE_KINDS
            or (kind_ref, fact_ref) not in TEMPORAL_FACT_FIELDS
            or isinstance(maximum, bool)
            or not isinstance(maximum, int)
            or maximum < 0
            or policy.get("cutoff") not in {"inclusive", "exclusive"}
            or kind_ref in index
        ):
            return None
        index[kind_ref] = policy
    return index


def _evidence_expectation_valid(expectation: Any) -> bool:
    admitted = (
        expectation.get("admitted_evidence_kinds")
        if isinstance(expectation, dict)
        else None
    )
    return bool(
        isinstance(expectation, dict)
        and _versioned_ref(expectation.get("expectation_ref"))
        and expectation.get("protected_use_ref") == PROTECTED_USE_REF
        and expectation.get("protected_claim_kind_ref") == ACTIVATED_CLAIM_KIND
        and expectation.get("protected_support_mode") == "evidence-backed"
        and _versioned_ref(expectation.get("condition_set_ref"))
        and isinstance(admitted, list)
        and admitted
        and len(admitted) == len(set(admitted))
        and set(admitted).issubset(SUPPORTED_EVIDENCE_KINDS)
        and expectation.get("minimum_evidence_count") == 1
    )


def _freshness_rule_valid(rule: Any) -> bool:
    return bool(
        isinstance(rule, dict)
        and _versioned_ref(rule.get("rule_ref"))
        and rule.get("protected_use_ref") == PROTECTED_USE_REF
        and rule.get("protected_claim_kind_ref") == ACTIVATED_CLAIM_KIND
        and rule.get("protected_support_mode") == "evidence-backed"
        and _versioned_ref(rule.get("condition_set_ref"))
        and rule.get("evaluation_time_source") == "support_evaluated_at"
        and rule.get("comparison_precision") == "microsecond"
        and rule.get("missing_temporal_fact") == "indeterminate"
        and rule.get("future_temporal_fact") == "indeterminate"
        and rule.get("incomparable_temporal_fact") == "indeterminate"
        and _freshness_policy_index(rule) is not None
    )


def _ambiguity_rule_valid(rule: Any) -> bool:
    if not isinstance(rule, dict):
        return False
    machine = rule.get("machine_dimensions")
    attributable = rule.get("attributable_dimensions")
    return bool(
        _versioned_ref(rule.get("rule_ref"))
        and rule.get("protected_use_ref") == PROTECTED_USE_REF
        and rule.get("protected_claim_kind_ref") == ACTIVATED_CLAIM_KIND
        and rule.get("protected_support_mode") == "evidence-backed"
        and _versioned_ref(rule.get("condition_set_ref"))
        and isinstance(machine, list)
        and len(machine) == len(set(machine))
        and set(machine) == {REFERENCE_DIMENSION, TEMPORAL_DIMENSION}
        and isinstance(attributable, list)
        and len(attributable) == len(set(attributable))
        and set(attributable) == {"semantic-classification@1"}
    )


def _resolve_local_rule(
    rules: Any, rule_ref: Any, validator: Any
) -> dict[str, Any] | None:
    requested = _normalized_ref(rule_ref)
    if requested is None or not isinstance(rules, list):
        return None
    candidates = [
        item
        for item in rules
        if isinstance(item, dict)
        and _normalized_ref(item.get("rule_ref")) == requested
        and validator(item)
    ]
    return candidates[0] if len(candidates) == 1 else None


def _resolve_evidence_expectation(
    expectations: Any, expectation_ref: Any
) -> dict[str, Any] | None:
    requested = _normalized_ref(expectation_ref)
    if requested is None or not isinstance(expectations, list):
        return None
    candidates = [
        item
        for item in expectations
        if isinstance(item, dict)
        and _normalized_ref(item.get("expectation_ref")) == requested
        and _evidence_expectation_valid(item)
    ]
    return candidates[0] if len(candidates) == 1 else None


def _finding_dicts(
    findings: Iterable[tuple[str, str, str]],
) -> list[dict[str, str]]:
    return [
        {"dimension_ref": dimension, "reason_ref": reason, "basis": basis}
        for dimension, reason, basis in sorted(findings)
    ]


def derive_capability_claim_support_usability(
    claim: dict[str, Any],
    *,
    freshness_rules: Any = (),
    ambiguity_rules: Any = (),
    evidence_expectations: Any = (),
    evidence_snapshots: Any = (),
    input_snapshots: Any = (),
    events: Iterable[dict[str, Any]] = (),
    observations: Iterable[dict[str, Any]] = (),
    assessments: Iterable[dict[str, Any]] = (),
    query_time: Any | None = None,
) -> dict[str, Any]:
    """Replay one exact OCP-012 source-use classification at an explicit time."""
    freshness_rule = _resolve_local_rule(
        freshness_rules, claim.get("freshness_rule_ref"), _freshness_rule_valid
    )
    ambiguity_rule = _resolve_local_rule(
        ambiguity_rules, claim.get("ambiguity_rule_ref"), _ambiguity_rule_valid
    )
    evidence_expectation = _resolve_evidence_expectation(
        evidence_expectations, claim.get("evidence_expectation_ref")
    )
    bindings = _normalized_bindings(claim.get("evidence_bindings"))
    declared_findings = _normalized_findings(claim.get("ambiguity_findings")) or ()
    evidence_snapshot_resolved, snapshot_bindings = _resolve_evidence_snapshot(
        evidence_snapshots, claim.get("evidence_snapshot_ref")
    )
    input_snapshot_resolved, input_snapshot = _resolve_input_snapshot(
        input_snapshots, claim.get("input_snapshot_ref")
    )
    condition_set_ref = _normalized_ref(claim.get("condition_set_ref"))

    unresolved = (
        claim.get("claim_kind_ref") != ACTIVATED_CLAIM_KIND
        or claim.get("support_mode") != "evidence-backed"
        or freshness_rule is None
        or ambiguity_rule is None
        or evidence_expectation is None
        or bindings is None
        or not evidence_snapshot_resolved
        or snapshot_bindings != bindings
        or not input_snapshot_resolved
        or not isinstance(input_snapshot, dict)
        or input_snapshot.get("protected_use_ref") != PROTECTED_USE_REF
        or input_snapshot.get("protected_claim_kind_ref") != ACTIVATED_CLAIM_KIND
        or input_snapshot.get("protected_support_mode") != "evidence-backed"
        or _normalized_ref(input_snapshot.get("evidence_expectation_ref"))
        != _normalized_ref(claim.get("evidence_expectation_ref"))
        or _normalized_ref(input_snapshot.get("condition_set_ref"))
        != condition_set_ref
        or _normalized_ref(input_snapshot.get("freshness_rule_ref"))
        != _normalized_ref(claim.get("freshness_rule_ref"))
        or _normalized_ref(input_snapshot.get("ambiguity_rule_ref"))
        != _normalized_ref(claim.get("ambiguity_rule_ref"))
        or _normalized_ref(freshness_rule.get("condition_set_ref"))
        != condition_set_ref
        or _normalized_ref(ambiguity_rule.get("condition_set_ref"))
        != condition_set_ref
        or _normalized_ref(evidence_expectation.get("condition_set_ref"))
        != condition_set_ref
        or any(
            kind_ref not in set(evidence_expectation.get("admitted_evidence_kinds") or [])
            for kind_ref, _ in bindings
        )
    )
    if unresolved:
        findings = (
            (REFERENCE_DIMENSION, "activation-input-unresolved@1", "rule-derived"),
        )
        return {
            "freshness_state": "indeterminate",
            "ambiguity_state": "ambiguous",
            "ambiguity_findings": _finding_dicts(findings),
        }

    attributable_dimensions = set(ambiguity_rule.get("attributable_dimensions") or [])
    attributed = tuple(
        item
        for item in declared_findings
        if item[2] == "attributable" and item[0] in attributable_dimensions
    )
    if not bindings:
        return {
            "freshness_state": "not_applicable",
            "ambiguity_state": "ambiguous" if attributed else "clear",
            "ambiguity_findings": _finding_dicts(attributed),
        }

    moment = _parse_strict_time(
        claim.get("support_evaluated_at") if query_time is None else query_time
    )
    machine_findings: set[tuple[str, str, str]] = set()
    if moment is None:
        machine_findings.add(
            (TEMPORAL_DIMENSION, "evaluation-time-incomparable@1", "rule-derived")
        )

    record_indexes = {
        "event@1": _unique_record_index(events, "event_id", validate_event),
        "observation-record@1": _unique_record_index(
            observations, "observation_id", validate_observation
        ),
        "outcome-assessment-record@1": _unique_record_index(
            assessments, "assessment_id", validate_outcome_assessment
        ),
    }
    policies = _freshness_policy_index(freshness_rule) or {}
    stale = False
    for kind_ref, evidence_ref in bindings:
        evidence = record_indexes.get(kind_ref, {}).get(evidence_ref)
        policy = policies.get(kind_ref)
        if evidence is None or policy is None:
            machine_findings.add(
                (REFERENCE_DIMENSION, "activation-input-unresolved@1", "rule-derived")
            )
            continue
        fact_field = TEMPORAL_FACT_FIELDS.get(
            (kind_ref, _normalized_ref(policy.get("temporal_fact_ref")))
        )
        raw_fact = evidence.get(fact_field) if fact_field is not None else None
        if raw_fact in (None, ""):
            machine_findings.add(
                (TEMPORAL_DIMENSION, "temporal-fact-missing@1", "rule-derived")
            )
            continue
        fact = _parse_strict_time(raw_fact)
        if fact is None:
            machine_findings.add(
                (TEMPORAL_DIMENSION, "temporal-fact-incomparable@1", "rule-derived")
            )
            continue
        if moment is None:
            continue
        if fact > moment:
            machine_findings.add(
                (TEMPORAL_DIMENSION, "temporal-fact-future@1", "rule-derived")
            )
            continue
        age = (moment - fact).total_seconds()
        maximum = float(policy["max_age_seconds"])
        if (
            (policy.get("cutoff") == "inclusive" and age > maximum)
            or (policy.get("cutoff") == "exclusive" and age >= maximum)
        ):
            stale = True

    findings = tuple(sorted({*machine_findings, *attributed}))
    freshness_state = (
        "indeterminate" if machine_findings else "stale" if stale else "fresh"
    )
    return {
        "freshness_state": freshness_state,
        "ambiguity_state": "ambiguous" if findings else "clear",
        "ambiguity_findings": _finding_dicts(findings),
    }


def _evidence_indexes(
    *,
    events: Iterable[dict[str, Any]],
    observations: Iterable[dict[str, Any]],
    assessments: Iterable[dict[str, Any]],
) -> dict[str, set[str]]:
    return {
        "event@1": {
            item_id
            for item in events
            if isinstance(item, dict)
            for item_id in [_normalized_ref(item.get("event_id"))]
            if item_id is not None
        },
        "observation-record@1": {
            item_id
            for item in observations
            if isinstance(item, dict)
            for item_id in [_normalized_ref(item.get("observation_id"))]
            if item_id is not None
        },
        "outcome-assessment-record@1": {
            item_id
            for item in assessments
            if isinstance(item, dict)
            for item_id in [_normalized_ref(item.get("assessment_id"))]
            if item_id is not None
        },
    }


def validate_capability_claim_dataset(
    claims: Iterable[dict[str, Any]],
    *,
    resources: Iterable[dict[str, Any]] = (),
    capabilities: Iterable[dict[str, Any]] = (),
    events: Iterable[dict[str, Any]] = (),
    observations: Iterable[dict[str, Any]] = (),
    assessments: Iterable[dict[str, Any]] = (),
    evidence_snapshots: Any = (),
    input_snapshots: Any = (),
    freshness_rules: Any = (),
    ambiguity_rules: Any = (),
    evidence_expectations: Any = (),
) -> ValidationResult:
    errors: list[str] = []
    entries = list(claims)
    resource_index: dict[str, list[dict[str, Any]]] = {}
    for resource in resources:
        if not isinstance(resource, dict) or not validate_resource(resource).valid:
            continue
        resource_id = _normalized_ref(resource.get("resource_id"))
        if resource_id is not None:
            resource_index.setdefault(resource_id, []).append(resource)

    event_entries = list(events)
    observation_entries = list(observations)
    assessment_entries = list(assessments)
    evidence_indexes = _evidence_indexes(
        events=event_entries,
        observations=observation_entries,
        assessments=assessment_entries,
    )
    observations_by_id = _unique_record_index(
        observation_entries, "observation_id"
    )
    activated_evidence_indexes = {
        "event@1": _unique_record_index(event_entries, "event_id", validate_event),
        "observation-record@1": _unique_record_index(
            observation_entries, "observation_id", validate_observation
        ),
        "outcome-assessment-record@1": _unique_record_index(
            assessment_entries, "assessment_id", validate_outcome_assessment
        ),
    }
    claim_index: dict[str, list[dict[str, Any]]] = {}
    graph: dict[str, str] = {}

    for claim in entries:
        if not isinstance(claim, dict):
            errors.append("CAPABILITY_CLAIM_ID_REQUIRED")
            continue
        errors.extend(validate_capability_claim(claim).errors)
        claim_id = _normalized_ref(claim.get("claim_id"))
        if claim_id is not None:
            claim_index.setdefault(claim_id, []).append(claim)

        holder_ref = _normalized_ref(claim.get("holder_ref"))
        if holder_ref is not None and len(resource_index.get(holder_ref, [])) != 1:
            errors.append("CAPABILITY_CLAIM_HOLDER_UNRESOLVED")

        capability_ref = claim.get("capability_ref")
        if _capability_key(capability_ref) is not None and resolve_capability_definition(
            capabilities, capability_ref
        ) is None:
            errors.append("CAPABILITY_CLAIM_CAPABILITY_UNRESOLVED")

        is_activated_evidence = bool(
            claim.get("claim_kind_ref") == ACTIVATED_CLAIM_KIND
            and claim.get("support_mode") == "evidence-backed"
            and claim.get("assertion") != "withdrawn"
        )
        bindings = _normalized_bindings(claim.get("evidence_bindings"))
        observation_statements: set[str] = set()
        if bindings is not None:
            for kind_ref, evidence_ref in bindings:
                if kind_ref in evidence_indexes and evidence_ref not in evidence_indexes[kind_ref]:
                    errors.append("CAPABILITY_CLAIM_EVIDENCE_REFERENCE_UNRESOLVED")
                if (
                    is_activated_evidence
                    and kind_ref in activated_evidence_indexes
                    and evidence_ref not in activated_evidence_indexes[kind_ref]
                ):
                    errors.append("CAPABILITY_CLAIM_EVIDENCE_REFERENCE_UNRESOLVED")
                if kind_ref == "observation-record@1":
                    observation = (
                        activated_evidence_indexes[kind_ref].get(evidence_ref)
                        if is_activated_evidence
                        else observations_by_id.get(evidence_ref)
                    )
                    if observation is not None:
                        observation_statements.add(
                            str(observation.get("statement", "")).strip().casefold()
                        )
        actual_conflict = len(observation_statements) > 1

        snapshot_ref = _normalized_ref(claim.get("evidence_snapshot_ref"))
        if snapshot_ref is not None:
            snapshot_resolved, snapshot_bindings = _resolve_evidence_snapshot(
                evidence_snapshots, snapshot_ref
            )
            if not snapshot_resolved:
                errors.append("CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_UNRESOLVED")
            elif bindings is not None and snapshot_bindings != bindings:
                errors.append("CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_MISMATCH")

        if is_activated_evidence:
            evidence_expectation = _resolve_evidence_expectation(
                evidence_expectations, claim.get("evidence_expectation_ref")
            )
            freshness_rule = _resolve_local_rule(
                freshness_rules, claim.get("freshness_rule_ref"), _freshness_rule_valid
            )
            ambiguity_rule = _resolve_local_rule(
                ambiguity_rules, claim.get("ambiguity_rule_ref"), _ambiguity_rule_valid
            )
            condition_set_ref = _normalized_ref(claim.get("condition_set_ref"))
            expectation_bound = bool(
                evidence_expectation is not None
                and _normalized_ref(evidence_expectation.get("condition_set_ref"))
                == condition_set_ref
                and bindings is not None
                and all(
                    kind_ref
                    in set(evidence_expectation.get("admitted_evidence_kinds") or [])
                    for kind_ref, _ in bindings
                )
            )
            if not expectation_bound:
                errors.append("CAPABILITY_CLAIM_EVIDENCE_EXPECTATION_INVALID")
            freshness_policies = _freshness_policy_index(freshness_rule) or {}
            freshness_rule_bound = bool(
                freshness_rule is not None
                and _normalized_ref(freshness_rule.get("condition_set_ref"))
                == condition_set_ref
                and evidence_expectation is not None
                and set(freshness_policies)
                == set(evidence_expectation.get("admitted_evidence_kinds") or [])
                and bindings is not None
                and all(kind_ref in freshness_policies for kind_ref, _ in bindings)
            )
            ambiguity_rule_bound = bool(
                ambiguity_rule is not None
                and _normalized_ref(ambiguity_rule.get("condition_set_ref"))
                == condition_set_ref
            )
            if not freshness_rule_bound:
                errors.append("CAPABILITY_CLAIM_FRESHNESS_RULE_INVALID")
            if not ambiguity_rule_bound:
                errors.append("CAPABILITY_CLAIM_AMBIGUITY_RULE_INVALID")

            input_snapshot_ref = _normalized_ref(claim.get("input_snapshot_ref"))
            input_snapshot_resolved, input_snapshot = _resolve_input_snapshot(
                input_snapshots, input_snapshot_ref
            )
            if input_snapshot_ref is not None and not input_snapshot_resolved:
                errors.append("CAPABILITY_CLAIM_INPUT_SNAPSHOT_UNRESOLVED")
            input_snapshot_bound = bool(
                isinstance(input_snapshot, dict)
                and input_snapshot.get("protected_use_ref") == PROTECTED_USE_REF
                and input_snapshot.get("protected_claim_kind_ref")
                == ACTIVATED_CLAIM_KIND
                and input_snapshot.get("protected_support_mode") == "evidence-backed"
                and _normalized_ref(input_snapshot.get("evidence_expectation_ref"))
                == _normalized_ref(claim.get("evidence_expectation_ref"))
                and _normalized_ref(input_snapshot.get("condition_set_ref"))
                == condition_set_ref
                and _normalized_ref(input_snapshot.get("freshness_rule_ref"))
                == _normalized_ref(claim.get("freshness_rule_ref"))
                and _normalized_ref(input_snapshot.get("ambiguity_rule_ref"))
                == _normalized_ref(claim.get("ambiguity_rule_ref"))
            )
            if input_snapshot_resolved and not input_snapshot_bound:
                errors.append("CAPABILITY_CLAIM_INPUT_SNAPSHOT_RULE_MISMATCH")

            evidence_snapshot_bound = bool(
                snapshot_ref is not None
                and snapshot_resolved
                and snapshot_bindings == bindings
            )
            if (
                freshness_rule_bound
                and ambiguity_rule_bound
                and expectation_bound
                and input_snapshot_bound
                and evidence_snapshot_bound
                and _parse_strict_time(claim.get("support_evaluated_at")) is not None
                and _parse_strict_time(claim.get("recorded_at")) is not None
            ):
                derived = derive_capability_claim_support_usability(
                    claim,
                    freshness_rules=freshness_rules,
                    ambiguity_rules=ambiguity_rules,
                    evidence_expectations=evidence_expectations,
                    evidence_snapshots=evidence_snapshots,
                    input_snapshots=input_snapshots,
                    events=event_entries,
                    observations=observation_entries,
                    assessments=assessment_entries,
                )
                if claim.get("freshness_state") != derived["freshness_state"]:
                    errors.append("CAPABILITY_CLAIM_FRESHNESS_STATE_MISMATCH")
                declared_findings = _normalized_findings(
                    claim.get("ambiguity_findings")
                )
                derived_findings = _normalized_findings(
                    derived.get("ambiguity_findings")
                )
                if (
                    claim.get("ambiguity_state") != derived["ambiguity_state"]
                    or declared_findings != derived_findings
                ):
                    errors.append("CAPABILITY_CLAIM_AMBIGUITY_STATE_MISMATCH")

                if bindings == ():
                    expected_support_state = "missing"
                elif actual_conflict:
                    expected_support_state = "conflicting"
                elif derived["ambiguity_state"] == "ambiguous":
                    expected_support_state = "ambiguous"
                elif derived["freshness_state"] == "stale":
                    expected_support_state = "stale"
                else:
                    expected_support_state = "sufficient"
                if claim.get("support_state") != expected_support_state:
                    errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")

        supersedes = _normalized_ref(claim.get("supersedes_claim_ref"))
        if claim_id is not None and supersedes is not None and supersedes != claim_id:
            graph[claim_id] = supersedes

    if any(len(candidates) > 1 for candidates in claim_index.values()):
        errors.append("CAPABILITY_CLAIM_IDENTITY_DUPLICATE")

    for source_id, target_id in graph.items():
        targets = claim_index.get(target_id, [])
        sources = claim_index.get(source_id, [])
        if len(targets) != 1:
            errors.append("CAPABILITY_CLAIM_SUPERSESSION_TARGET_UNRESOLVED")
        elif len(sources) == 1:
            source = sources[0]
            target = targets[0]
            if _binding_identity(source) != _binding_identity(target):
                errors.append("CAPABILITY_CLAIM_BINDING_MISMATCH")
            elif (
                source.get("claim_kind_ref") == ACTIVATED_CLAIM_KIND
                and target.get("claim_kind_ref") == ACTIVATED_CLAIM_KIND
            ):
                source_mode = source.get("support_mode")
                target_mode = target.get("support_mode")
                if source_mode != target_mode and not (
                    target_mode == "declaration-only"
                    and source_mode == "evidence-backed"
                    and source.get("assertion") == target.get("assertion")
                ):
                    errors.append("CAPABILITY_CLAIM_SUPPORT_MODE_TRANSITION_INVALID")

    if _has_cycle(graph):
        errors.append("CAPABILITY_CLAIM_SUPERSESSION_CYCLE")

    return _result(errors)


def resolve_capability_claim(
    claims: Iterable[dict[str, Any]], claim_ref: str
) -> dict[str, Any] | None:
    normalized = _normalized_ref(claim_ref)
    candidates = [
        claim
        for claim in claims
        if isinstance(claim, dict)
        and _normalized_ref(claim.get("claim_id")) == normalized
        and validate_capability_claim(claim).valid
    ]
    return candidates[0] if len(candidates) == 1 else None


def capability_claim_effective_at(claim: dict[str, Any], at: str) -> bool:
    moment = _parse_time(at)
    start = _parse_time(claim.get("effective_from"))
    end = _parse_time(claim.get("effective_until"))
    return bool(
        moment is not None
        and start is not None
        and start <= moment
        and (end is None or moment < end)
    )


def capability_claim_heads(
    claims: Iterable[dict[str, Any]],
    *,
    holder_ref: str,
    capability_ref: dict[str, Any],
    claimant_ref: str,
    claim_kind_ref: str,
    condition_set_ref: str,
    at: str,
) -> list[dict[str, Any]]:
    wanted = (
        _normalized_ref(claim_kind_ref),
        "resource@1",
        _normalized_ref(holder_ref),
        _capability_key(capability_ref),
        _normalized_ref(claimant_ref),
        _normalized_ref(condition_set_ref),
    )
    candidates = [
        claim
        for claim in claims
        if isinstance(claim, dict)
        and validate_capability_claim(claim).valid
        and _binding_identity(claim) == wanted
        and capability_claim_effective_at(claim, at)
    ]
    ids = {
        claim_id
        for claim in candidates
        for claim_id in [_normalized_ref(claim.get("claim_id"))]
        if claim_id is not None
    }
    superseded = {
        target
        for claim in candidates
        for target in [_normalized_ref(claim.get("supersedes_claim_ref"))]
        if target in ids
    }
    return sorted(
        [
            claim
            for claim in candidates
            if _normalized_ref(claim.get("claim_id")) not in superseded
        ],
        key=lambda claim: str(claim.get("claim_id")),
    )


def effective_capability_claim(
    claims: Iterable[dict[str, Any]],
    *,
    holder_ref: str,
    capability_ref: dict[str, Any],
    claimant_ref: str,
    claim_kind_ref: str,
    condition_set_ref: str,
    at: str,
    resources: Iterable[dict[str, Any]] = (),
    capabilities: Iterable[dict[str, Any]] = (),
    events: Iterable[dict[str, Any]] = (),
    observations: Iterable[dict[str, Any]] = (),
    assessments: Iterable[dict[str, Any]] = (),
    evidence_snapshots: Any = (),
    input_snapshots: Any = (),
    freshness_rules: Any = (),
    ambiguity_rules: Any = (),
    evidence_expectations: Any = (),
) -> str:
    entries = list(claims)
    heads = capability_claim_heads(
        entries,
        holder_ref=holder_ref,
        capability_ref=capability_ref,
        claimant_ref=claimant_ref,
        claim_kind_ref=claim_kind_ref,
        condition_set_ref=condition_set_ref,
        at=at,
    )
    if not heads:
        return "indeterminate"
    if any(
        head.get("claim_kind_ref") == ACTIVATED_CLAIM_KIND
        and head.get("support_mode") == "evidence-backed"
        and head.get("assertion") != "withdrawn"
        for head in heads
    ):
        activated_context = validate_capability_claim_dataset(
            entries,
            resources=resources,
            capabilities=capabilities,
            events=events,
            observations=observations,
            assessments=assessments,
            evidence_snapshots=evidence_snapshots,
            input_snapshots=input_snapshots,
            freshness_rules=freshness_rules,
            ambiguity_rules=ambiguity_rules,
            evidence_expectations=evidence_expectations,
        )
        if not activated_context.valid:
            return "indeterminate"
    if any(head.get("support_state") in NON_PERMISSIVE_SUPPORT_STATES for head in heads):
        return "indeterminate"
    assertions = {head.get("assertion") for head in heads}
    if len(assertions) != 1:
        return "indeterminate"
    assertion = next(iter(assertions))
    return assertion if assertion in ASSERTIONS else "indeterminate"


def validate_capability_claim_fixture(fixture: dict[str, Any]) -> ValidationResult:
    return validate_capability_claim_dataset(
        fixture.get("claims") or fixture.get("entities") or [],
        resources=fixture.get("resources") or [],
        capabilities=fixture.get("capabilities") or [],
        events=fixture.get("events") or [],
        observations=fixture.get("observations") or [],
        assessments=fixture.get("assessments") or [],
        evidence_snapshots=fixture.get("evidence_snapshots") or [],
        input_snapshots=fixture.get("input_snapshots") or [],
        freshness_rules=fixture.get("freshness_rules") or [],
        ambiguity_rules=fixture.get("ambiguity_rules") or [],
        evidence_expectations=fixture.get("evidence_expectations") or [],
    )
