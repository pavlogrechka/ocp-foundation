from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .checker import ValidationResult


OUTCOME_ASSESSMENT_ERROR_CODES = frozenset(
    {
        "OUTCOME_ASSESSMENT_BINDING_MISMATCH",
        "OUTCOME_ASSESSMENT_ACTIVATION_FIELDS_FORBIDDEN",
        "OUTCOME_ASSESSMENT_ACTIVATION_REQUIRED",
        "OUTCOME_ASSESSMENT_ACTIVATION_TIME_INVALID",
        "OUTCOME_ASSESSMENT_AMBIGUITY_RULE_INVALID",
        "OUTCOME_ASSESSMENT_AMBIGUITY_STATE_MISMATCH",
        "OUTCOME_ASSESSMENT_CONCLUSION_INVALID",
        "OUTCOME_ASSESSMENT_FRESHNESS_RULE_INVALID",
        "OUTCOME_ASSESSMENT_FRESHNESS_STATE_MISMATCH",
        "OUTCOME_ASSESSMENT_DEFINITIVE_EVIDENCE_UNSAFE",
        "OUTCOME_ASSESSMENT_EVALUATED_AT_REQUIRED",
        "OUTCOME_ASSESSMENT_EVALUATOR_REQUIRED",
        "OUTCOME_ASSESSMENT_EVIDENCE_BINDINGS_INVALID",
        "OUTCOME_ASSESSMENT_EVIDENCE_KIND_UNSUPPORTED",
        "OUTCOME_ASSESSMENT_EVIDENCE_REFERENCE_UNRESOLVED",
        "OUTCOME_ASSESSMENT_EVIDENCE_SNAPSHOT_MISMATCH",
        "OUTCOME_ASSESSMENT_EVIDENCE_SNAPSHOT_REQUIRED",
        "OUTCOME_ASSESSMENT_EVIDENCE_SNAPSHOT_UNRESOLVED",
        "OUTCOME_ASSESSMENT_EVIDENCE_STATE_INVALID",
        "OUTCOME_ASSESSMENT_EVIDENCE_STATE_MISMATCH",
        "OUTCOME_ASSESSMENT_ID_REQUIRED",
        "OUTCOME_ASSESSMENT_IDENTITY_DUPLICATE",
        "OUTCOME_ASSESSMENT_INPUT_SNAPSHOT_REQUIRED",
        "OUTCOME_ASSESSMENT_INPUT_SNAPSHOT_RULE_MISMATCH",
        "OUTCOME_ASSESSMENT_INPUT_SNAPSHOT_UNRESOLVED",
        "OUTCOME_ASSESSMENT_KIND_REF_REQUIRED",
        "OUTCOME_ASSESSMENT_KIND_UNSUPPORTED",
        "OUTCOME_ASSESSMENT_PROVENANCE_REF_REQUIRED",
        "OUTCOME_ASSESSMENT_RECORDED_AT_REQUIRED",
        "OUTCOME_ASSESSMENT_RESULT_COUPLING_FORBIDDEN",
        "OUTCOME_ASSESSMENT_SELF_SUPERSESSION",
        "OUTCOME_ASSESSMENT_SUPERSESSION_CYCLE",
        "OUTCOME_ASSESSMENT_SUPERSESSION_TARGET_UNRESOLVED",
        "OUTCOME_ASSESSMENT_TARGET_KIND_UNSUPPORTED",
        "OUTCOME_ASSESSMENT_TARGET_REF_REQUIRED",
        "OUTCOME_ASSESSMENT_TARGET_UNRESOLVED",
        "OUTCOME_ASSESSMENT_TIME_ORDER_INVALID",
        "OUTCOME_ASSESSMENT_CRITERION_REF_REQUIRED",
    }
)

OUTCOME_ASSESSMENT_DERIVATION_RULES = frozenset(
    {
        "effective_outcome_conclusion",
        "derive_outcome_evidence_usability",
        "outcome_assessment_heads",
        "resolve_outcome_assessment",
    }
)

SUPPORTED_TARGET_KINDS = frozenset({"objective@1"})
SUPPORTED_EVIDENCE_KINDS = frozenset({"event@1", "observation-record@1"})
ACTIVATED_ASSESSMENT_KIND = "objective-achievement@2"
SUPPORTED_ASSESSMENT_KINDS = frozenset(
    {"objective-achievement@1", ACTIVATED_ASSESSMENT_KIND}
)
ACTIVATION_FIELDS = frozenset(
    {
        "freshness_rule_ref",
        "freshness_state",
        "ambiguity_rule_ref",
        "ambiguity_state",
        "ambiguity_findings",
    }
)
FRESHNESS_STATES = frozenset({"fresh", "stale", "indeterminate", "not_applicable"})
AMBIGUITY_STATES = frozenset({"clear", "ambiguous"})
AMBIGUITY_BASES = frozenset({"rule-derived", "attributable"})
TEMPORAL_DIMENSION = "temporal@1"
REFERENCE_DIMENSION = "reference@1"
TEMPORAL_FACT_FIELDS = {
    ("event@1", "event-occurred-at@1"): "occurred_at",
    ("observation-record@1", "observation-observed-at@1"): "observed_at",
}
CONCLUSIONS = frozenset(
    {"achieved", "not_achieved", "partially_achieved", "indeterminate"}
)
EVIDENCE_STATES = frozenset(
    {"sufficient", "missing", "stale", "ambiguous", "conflicting"}
)
DEFINITIVE_CONCLUSIONS = frozenset(
    {"achieved", "not_achieved", "partially_achieved"}
)
FORBIDDEN_COUPLING_KEYS = frozenset(
    {
        "result_id",
        "result_status",
        "operation_success",
        "operation_lifecycle_stage",
        "objective_achievement_status",
        "capability_claim",
        "readiness",
        "authorization",
        "admissibility",
        "state",
        "conflict",
        "risk",
        "current",
        "is_current",
        "latest",
    }
)


def _result(errors: Iterable[str]) -> ValidationResult:
    return ValidationResult(tuple(dict.fromkeys(errors)))


def _nonempty(value: Any) -> bool:
    return value is not None and bool(str(value).strip())


def _normalized_ref(value: Any) -> str | None:
    if not _nonempty(value):
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
    bindings: list[tuple[str, str]] = []
    for item in value:
        binding = _normalized_binding(item)
        if binding is None:
            return None
        bindings.append(binding)
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


def validate_outcome_assessment(assessment: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []

    assessment_id = _normalized_ref(assessment.get("assessment_id"))
    if assessment_id is None:
        errors.append("OUTCOME_ASSESSMENT_ID_REQUIRED")
    assessment_kind_ref = _normalized_ref(assessment.get("assessment_kind_ref"))
    if not _versioned_ref(assessment.get("assessment_kind_ref")):
        errors.append("OUTCOME_ASSESSMENT_KIND_REF_REQUIRED")
    elif assessment_kind_ref not in SUPPORTED_ASSESSMENT_KINDS:
        errors.append("OUTCOME_ASSESSMENT_KIND_UNSUPPORTED")

    if assessment_kind_ref == ACTIVATED_ASSESSMENT_KIND:
        findings = _normalized_findings(assessment.get("ambiguity_findings"))
        if (
            not _versioned_ref(assessment.get("freshness_rule_ref"))
            or assessment.get("freshness_state") not in FRESHNESS_STATES
            or not _versioned_ref(assessment.get("ambiguity_rule_ref"))
            or assessment.get("ambiguity_state") not in AMBIGUITY_STATES
            or findings is None
        ):
            errors.append("OUTCOME_ASSESSMENT_ACTIVATION_REQUIRED")
        if (
            _parse_strict_time(assessment.get("evaluated_at")) is None
            or _parse_strict_time(assessment.get("recorded_at")) is None
        ):
            errors.append("OUTCOME_ASSESSMENT_ACTIVATION_TIME_INVALID")
    elif any(field in assessment for field in ACTIVATION_FIELDS):
        errors.append("OUTCOME_ASSESSMENT_ACTIVATION_FIELDS_FORBIDDEN")

    target_kind_ref = _normalized_ref(assessment.get("target_kind_ref"))
    if target_kind_ref not in SUPPORTED_TARGET_KINDS:
        errors.append("OUTCOME_ASSESSMENT_TARGET_KIND_UNSUPPORTED")
    if _normalized_ref(assessment.get("target_ref")) is None:
        errors.append("OUTCOME_ASSESSMENT_TARGET_REF_REQUIRED")
    if not _versioned_ref(assessment.get("criterion_ref")):
        errors.append("OUTCOME_ASSESSMENT_CRITERION_REF_REQUIRED")

    bindings = _normalized_bindings(assessment.get("evidence_bindings"))
    if bindings is None:
        errors.append("OUTCOME_ASSESSMENT_EVIDENCE_BINDINGS_INVALID")
    elif any(kind_ref not in SUPPORTED_EVIDENCE_KINDS for kind_ref, _ in bindings):
        errors.append("OUTCOME_ASSESSMENT_EVIDENCE_KIND_UNSUPPORTED")

    if _normalized_ref(assessment.get("evidence_snapshot_ref")) is None:
        errors.append("OUTCOME_ASSESSMENT_EVIDENCE_SNAPSHOT_REQUIRED")
    if _normalized_ref(assessment.get("input_snapshot_ref")) is None:
        errors.append("OUTCOME_ASSESSMENT_INPUT_SNAPSHOT_REQUIRED")

    evidence_state = assessment.get("evidence_state")
    if evidence_state not in EVIDENCE_STATES:
        errors.append("OUTCOME_ASSESSMENT_EVIDENCE_STATE_INVALID")

    conclusion = assessment.get("conclusion")
    if conclusion not in CONCLUSIONS:
        errors.append("OUTCOME_ASSESSMENT_CONCLUSION_INVALID")
    elif evidence_state in EVIDENCE_STATES:
        if evidence_state != "sufficient" and conclusion in DEFINITIVE_CONCLUSIONS:
            errors.append("OUTCOME_ASSESSMENT_DEFINITIVE_EVIDENCE_UNSAFE")
        if bindings == () and evidence_state != "missing":
            errors.append("OUTCOME_ASSESSMENT_EVIDENCE_STATE_MISMATCH")
        if bindings and evidence_state == "missing":
            errors.append("OUTCOME_ASSESSMENT_EVIDENCE_STATE_MISMATCH")

    if _normalized_ref(assessment.get("evaluator_ref")) is None:
        errors.append("OUTCOME_ASSESSMENT_EVALUATOR_REQUIRED")
    evaluated_at = _parse_time(assessment.get("evaluated_at"))
    recorded_at = _parse_time(assessment.get("recorded_at"))
    if evaluated_at is None:
        errors.append("OUTCOME_ASSESSMENT_EVALUATED_AT_REQUIRED")
    if recorded_at is None:
        errors.append("OUTCOME_ASSESSMENT_RECORDED_AT_REQUIRED")
    if evaluated_at is not None and recorded_at is not None and evaluated_at > recorded_at:
        errors.append("OUTCOME_ASSESSMENT_TIME_ORDER_INVALID")
    if _normalized_ref(assessment.get("provenance_ref")) is None:
        errors.append("OUTCOME_ASSESSMENT_PROVENANCE_REF_REQUIRED")

    supersedes = _normalized_ref(assessment.get("supersedes_assessment_ref"))
    if assessment_id is not None and supersedes == assessment_id:
        errors.append("OUTCOME_ASSESSMENT_SELF_SUPERSESSION")

    if any(
        key in assessment and assessment.get(key) not in (None, False, "", [], {})
        for key in FORBIDDEN_COUPLING_KEYS
    ):
        errors.append("OUTCOME_ASSESSMENT_RESULT_COUPLING_FORBIDDEN")

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
    candidates: list[dict[str, Any] | None] = []
    for item in value:
        if isinstance(item, dict):
            if _normalized_ref(item.get("snapshot_ref")) == requested:
                candidates.append(item)
        elif _normalized_ref(item) == requested:
            candidates.append(None)
    if len(candidates) != 1:
        return False, None
    return True, candidates[0]


def _unique_record_index(
    entries: Iterable[dict[str, Any]], identity_field: str
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


def _freshness_rule_valid(rule: Any) -> bool:
    return bool(
        isinstance(rule, dict)
        and _versioned_ref(rule.get("rule_ref"))
        and rule.get("protected_assessment_kind_ref") == ACTIVATED_ASSESSMENT_KIND
        and _versioned_ref(rule.get("criterion_ref"))
        and rule.get("evaluation_time_source") == "evaluated_at"
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
        and rule.get("protected_assessment_kind_ref") == ACTIVATED_ASSESSMENT_KIND
        and _versioned_ref(rule.get("criterion_ref"))
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


def _finding_dicts(
    findings: Iterable[tuple[str, str, str]],
) -> list[dict[str, str]]:
    return [
        {"dimension_ref": dimension, "reason_ref": reason, "basis": basis}
        for dimension, reason, basis in sorted(findings)
    ]


def derive_outcome_evidence_usability(
    assessment: dict[str, Any],
    *,
    freshness_rules: Any = (),
    ambiguity_rules: Any = (),
    evidence_snapshots: Any = (),
    input_snapshots: Any = (),
    events: Iterable[dict[str, Any]] = (),
    observations: Iterable[dict[str, Any]] = (),
    query_time: Any | None = None,
) -> dict[str, Any]:
    """Derive one exact use-specific view without consulting wall clock or latest data."""
    freshness_rule = _resolve_local_rule(
        freshness_rules,
        assessment.get("freshness_rule_ref"),
        _freshness_rule_valid,
    )
    ambiguity_rule = _resolve_local_rule(
        ambiguity_rules,
        assessment.get("ambiguity_rule_ref"),
        _ambiguity_rule_valid,
    )
    bindings = _normalized_bindings(assessment.get("evidence_bindings"))
    declared_findings = _normalized_findings(assessment.get("ambiguity_findings")) or ()
    evidence_snapshot_resolved, snapshot_bindings = _resolve_evidence_snapshot(
        evidence_snapshots, assessment.get("evidence_snapshot_ref")
    )
    input_snapshot_resolved, input_snapshot = _resolve_input_snapshot(
        input_snapshots, assessment.get("input_snapshot_ref")
    )
    criterion_ref = _normalized_ref(assessment.get("criterion_ref"))

    unresolved = (
        freshness_rule is None
        or ambiguity_rule is None
        or bindings is None
        or not evidence_snapshot_resolved
        or snapshot_bindings != bindings
        or not input_snapshot_resolved
        or not isinstance(input_snapshot, dict)
        or _normalized_ref(input_snapshot.get("criterion_ref")) != criterion_ref
        or _normalized_ref(input_snapshot.get("freshness_rule_ref"))
        != _normalized_ref(assessment.get("freshness_rule_ref"))
        or _normalized_ref(input_snapshot.get("ambiguity_rule_ref"))
        != _normalized_ref(assessment.get("ambiguity_rule_ref"))
        or _normalized_ref(freshness_rule.get("criterion_ref"))
        != criterion_ref
        or _normalized_ref(ambiguity_rule.get("criterion_ref"))
        != criterion_ref
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
        assessment.get("evaluated_at") if query_time is None else query_time
    )
    machine_findings: set[tuple[str, str, str]] = set()
    if moment is None:
        machine_findings.add(
            (TEMPORAL_DIMENSION, "evaluation-time-incomparable@1", "rule-derived")
        )

    event_index = _unique_record_index(events, "event_id")
    observation_index = _unique_record_index(observations, "observation_id")
    policies = _freshness_policy_index(freshness_rule) or {}
    stale = False
    for kind_ref, evidence_ref in bindings:
        evidence = (
            event_index.get(evidence_ref)
            if kind_ref == "event@1"
            else observation_index.get(evidence_ref)
        )
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


def _binding_identity(assessment: dict[str, Any]) -> tuple[str | None, ...]:
    return (
        _normalized_ref(assessment.get("assessment_kind_ref")),
        _normalized_ref(assessment.get("target_kind_ref")),
        _normalized_ref(assessment.get("target_ref")),
        _normalized_ref(assessment.get("criterion_ref")),
    )


def validate_outcome_assessment_dataset(
    assessments: Iterable[dict[str, Any]],
    *,
    objectives: Iterable[dict[str, Any]] = (),
    events: Iterable[dict[str, Any]] = (),
    observations: Iterable[dict[str, Any]] = (),
    evidence_snapshots: Any = (),
    input_snapshots: Any = (),
    freshness_rules: Any = (),
    ambiguity_rules: Any = (),
) -> ValidationResult:
    errors: list[str] = []
    entries = list(assessments)
    objective_entries = list(objectives)
    event_entries = list(events)
    observation_entries = list(observations)
    objective_index = _unique_record_index(objective_entries, "objective_id")
    event_index = _unique_record_index(event_entries, "event_id")
    observation_index = _unique_record_index(
        observation_entries, "observation_id"
    )
    assessment_index: dict[str, list[dict[str, Any]]] = {}
    graph: dict[str, str] = {}

    for assessment in entries:
        if not isinstance(assessment, dict):
            errors.append("OUTCOME_ASSESSMENT_ID_REQUIRED")
            continue
        errors.extend(validate_outcome_assessment(assessment).errors)
        assessment_id = _normalized_ref(assessment.get("assessment_id"))
        if assessment_id is not None:
            assessment_index.setdefault(assessment_id, []).append(assessment)

        target_kind_ref = _normalized_ref(assessment.get("target_kind_ref"))
        target_ref = _normalized_ref(assessment.get("target_ref"))
        if target_kind_ref == "objective@1" and target_ref not in objective_index:
            errors.append("OUTCOME_ASSESSMENT_TARGET_UNRESOLVED")

        bindings = _normalized_bindings(assessment.get("evidence_bindings"))
        actual_conflict = False
        if bindings is not None:
            statements: set[str] = set()
            for kind_ref, evidence_ref in bindings:
                if kind_ref == "observation-record@1":
                    observation = observation_index.get(evidence_ref)
                    if observation is None:
                        errors.append("OUTCOME_ASSESSMENT_EVIDENCE_REFERENCE_UNRESOLVED")
                    else:
                        statements.add(
                            str(observation.get("statement", "")).strip().casefold()
                        )
                elif kind_ref == "event@1" and evidence_ref not in event_index:
                    errors.append("OUTCOME_ASSESSMENT_EVIDENCE_REFERENCE_UNRESOLVED")
            actual_conflict = len(statements) > 1

        evidence_state = assessment.get("evidence_state")
        conclusion = assessment.get("conclusion")
        if actual_conflict and evidence_state != "conflicting":
            errors.append("OUTCOME_ASSESSMENT_EVIDENCE_STATE_MISMATCH")
        if actual_conflict and conclusion in DEFINITIVE_CONCLUSIONS:
            errors.append("OUTCOME_ASSESSMENT_DEFINITIVE_EVIDENCE_UNSAFE")

        snapshot_ref = _normalized_ref(assessment.get("evidence_snapshot_ref"))
        if snapshot_ref is not None:
            snapshot_resolved, snapshot_bindings = _resolve_evidence_snapshot(
                evidence_snapshots, snapshot_ref
            )
            if not snapshot_resolved:
                errors.append("OUTCOME_ASSESSMENT_EVIDENCE_SNAPSHOT_UNRESOLVED")
            elif bindings is not None and bindings != snapshot_bindings:
                errors.append("OUTCOME_ASSESSMENT_EVIDENCE_SNAPSHOT_MISMATCH")

        input_snapshot_ref = _normalized_ref(assessment.get("input_snapshot_ref"))
        input_snapshot_resolved, input_snapshot = _resolve_input_snapshot(
            input_snapshots, input_snapshot_ref
        )
        if input_snapshot_ref is not None and not input_snapshot_resolved:
            errors.append("OUTCOME_ASSESSMENT_INPUT_SNAPSHOT_UNRESOLVED")

        if _normalized_ref(assessment.get("assessment_kind_ref")) == ACTIVATED_ASSESSMENT_KIND:
            freshness_rule = _resolve_local_rule(
                freshness_rules,
                assessment.get("freshness_rule_ref"),
                _freshness_rule_valid,
            )
            ambiguity_rule = _resolve_local_rule(
                ambiguity_rules,
                assessment.get("ambiguity_rule_ref"),
                _ambiguity_rule_valid,
            )
            criterion_ref = _normalized_ref(assessment.get("criterion_ref"))
            freshness_rule_bound = bool(
                freshness_rule is not None
                and _normalized_ref(freshness_rule.get("criterion_ref")) == criterion_ref
            )
            ambiguity_rule_bound = bool(
                ambiguity_rule is not None
                and _normalized_ref(ambiguity_rule.get("criterion_ref")) == criterion_ref
            )
            if not freshness_rule_bound:
                errors.append("OUTCOME_ASSESSMENT_FRESHNESS_RULE_INVALID")
            if not ambiguity_rule_bound:
                errors.append("OUTCOME_ASSESSMENT_AMBIGUITY_RULE_INVALID")

            input_snapshot_bound = isinstance(input_snapshot, dict)
            if isinstance(input_snapshot, dict):
                input_snapshot_bound = bool(
                    _normalized_ref(input_snapshot.get("criterion_ref"))
                    == criterion_ref
                    and _normalized_ref(input_snapshot.get("freshness_rule_ref"))
                    == _normalized_ref(assessment.get("freshness_rule_ref"))
                    and _normalized_ref(input_snapshot.get("ambiguity_rule_ref"))
                    == _normalized_ref(assessment.get("ambiguity_rule_ref"))
                )
            if not input_snapshot_bound:
                errors.append("OUTCOME_ASSESSMENT_INPUT_SNAPSHOT_RULE_MISMATCH")

            evidence_snapshot_resolved, activated_snapshot_bindings = (
                _resolve_evidence_snapshot(evidence_snapshots, snapshot_ref)
            )
            evidence_snapshot_bound = bool(
                evidence_snapshot_resolved and activated_snapshot_bindings == bindings
            )
            if (
                freshness_rule_bound
                and ambiguity_rule_bound
                and evidence_snapshot_bound
                and input_snapshot_bound
            ):
                derived = derive_outcome_evidence_usability(
                    assessment,
                    freshness_rules=freshness_rules,
                    ambiguity_rules=ambiguity_rules,
                    evidence_snapshots=evidence_snapshots,
                    input_snapshots=input_snapshots,
                    events=event_entries,
                    observations=observation_entries,
                )
                if assessment.get("freshness_state") != derived["freshness_state"]:
                    errors.append("OUTCOME_ASSESSMENT_FRESHNESS_STATE_MISMATCH")
                declared_findings = _normalized_findings(
                    assessment.get("ambiguity_findings")
                )
                derived_findings = _normalized_findings(
                    derived.get("ambiguity_findings")
                )
                if (
                    assessment.get("ambiguity_state") != derived["ambiguity_state"]
                    or declared_findings != derived_findings
                ):
                    errors.append("OUTCOME_ASSESSMENT_AMBIGUITY_STATE_MISMATCH")

                if bindings == ():
                    expected_evidence_state = "missing"
                elif actual_conflict:
                    expected_evidence_state = "conflicting"
                elif derived["ambiguity_state"] == "ambiguous":
                    expected_evidence_state = "ambiguous"
                elif derived["freshness_state"] == "stale":
                    expected_evidence_state = "stale"
                else:
                    expected_evidence_state = "sufficient"
                if evidence_state != expected_evidence_state:
                    errors.append("OUTCOME_ASSESSMENT_EVIDENCE_STATE_MISMATCH")
                if (
                    expected_evidence_state != "sufficient"
                    and conclusion in DEFINITIVE_CONCLUSIONS
                ):
                    errors.append("OUTCOME_ASSESSMENT_DEFINITIVE_EVIDENCE_UNSAFE")

        supersedes = _normalized_ref(assessment.get("supersedes_assessment_ref"))
        if assessment_id is not None and supersedes is not None and supersedes != assessment_id:
            graph[assessment_id] = supersedes

    if any(len(candidates) > 1 for candidates in assessment_index.values()):
        errors.append("OUTCOME_ASSESSMENT_IDENTITY_DUPLICATE")

    for source, target in graph.items():
        target_candidates = assessment_index.get(target, [])
        source_candidates = assessment_index.get(source, [])
        if len(target_candidates) != 1:
            errors.append("OUTCOME_ASSESSMENT_SUPERSESSION_TARGET_UNRESOLVED")
        elif (
            len(source_candidates) == 1
            and _binding_identity(source_candidates[0])
            != _binding_identity(target_candidates[0])
        ):
            errors.append("OUTCOME_ASSESSMENT_BINDING_MISMATCH")

    if _has_cycle(graph):
        errors.append("OUTCOME_ASSESSMENT_SUPERSESSION_CYCLE")

    return _result(errors)


def resolve_outcome_assessment(
    assessments: Iterable[dict[str, Any]], assessment_ref: Any
) -> dict[str, Any] | None:
    requested = _normalized_ref(assessment_ref)
    if requested is None:
        return None
    candidates = [
        item
        for item in assessments
        if isinstance(item, dict)
        and _normalized_ref(item.get("assessment_id")) == requested
        and validate_outcome_assessment(item).valid
    ]
    return candidates[0] if len(candidates) == 1 else None


def outcome_assessment_heads(
    assessments: Iterable[dict[str, Any]],
    *,
    target_kind_ref: Any | None = None,
    target_ref: Any | None = None,
    criterion_ref: Any | None = None,
) -> tuple[dict[str, Any], ...]:
    entries = [
        item
        for item in assessments
        if isinstance(item, dict) and validate_outcome_assessment(item).valid
    ]
    superseded = {
        target
        for item in entries
        for target in [_normalized_ref(item.get("supersedes_assessment_ref"))]
        if target is not None
    }
    requested_target_kind = _normalized_ref(target_kind_ref)
    requested_target = _normalized_ref(target_ref)
    requested_criterion = _normalized_ref(criterion_ref)
    heads = []
    for item in entries:
        assessment_id = _normalized_ref(item.get("assessment_id"))
        if assessment_id is None or assessment_id in superseded:
            continue
        if (
            requested_target_kind is not None
            and _normalized_ref(item.get("target_kind_ref"))
            != requested_target_kind
        ):
            continue
        if (
            requested_target is not None
            and _normalized_ref(item.get("target_ref")) != requested_target
        ):
            continue
        if (
            requested_criterion is not None
            and _normalized_ref(item.get("criterion_ref"))
            != requested_criterion
        ):
            continue
        heads.append(item)
    return tuple(sorted(heads, key=lambda item: _normalized_ref(item.get("assessment_id")) or ""))


def effective_outcome_conclusion(
    assessments: Iterable[dict[str, Any]],
    target_kind_ref: Any,
    target_ref: Any,
    criterion_ref: Any,
    *,
    objectives: Iterable[dict[str, Any]] = (),
    events: Iterable[dict[str, Any]] = (),
    observations: Iterable[dict[str, Any]] = (),
    evidence_snapshots: Any = (),
    input_snapshots: Any = (),
    freshness_rules: Any = (),
    ambiguity_rules: Any = (),
) -> str | None:
    entries = list(assessments)
    heads = outcome_assessment_heads(
        entries,
        target_kind_ref=target_kind_ref,
        target_ref=target_ref,
        criterion_ref=criterion_ref,
    )
    if not heads:
        return None
    if any(
        _normalized_ref(item.get("assessment_kind_ref"))
        == ACTIVATED_ASSESSMENT_KIND
        for item in heads
    ):
        activated_context = validate_outcome_assessment_dataset(
            entries,
            objectives=objectives,
            events=events,
            observations=observations,
            evidence_snapshots=evidence_snapshots,
            input_snapshots=input_snapshots,
            freshness_rules=freshness_rules,
            ambiguity_rules=ambiguity_rules,
        )
        if not activated_context.valid:
            return "indeterminate"
    exact_bindings = {
        (
            _normalized_ref(item.get("evidence_snapshot_ref")),
            _normalized_ref(item.get("input_snapshot_ref")),
        )
        for item in heads
    }
    conclusions = {item.get("conclusion") for item in heads}
    if len(exact_bindings) != 1 or len(conclusions) != 1:
        return "indeterminate"
    return str(next(iter(conclusions)))


def validate_outcome_assessment_fixture(fixture: dict[str, Any]) -> ValidationResult:
    assessments = fixture.get("assessments")
    if assessments is None:
        entity = fixture.get("entity")
        assessments = [entity] if isinstance(entity, dict) else []
    return validate_outcome_assessment_dataset(
        assessments or [],
        objectives=fixture.get("objectives") or [],
        events=fixture.get("events") or [],
        observations=fixture.get("observations") or [],
        evidence_snapshots=fixture.get("evidence_snapshots") or [],
        input_snapshots=fixture.get("input_snapshots") or [],
        freshness_rules=fixture.get("freshness_rules") or [],
        ambiguity_rules=fixture.get("ambiguity_rules") or [],
    )


def validate_integrated_outcome_scenario(fixture: dict[str, Any]) -> ValidationResult:
    from .event import validate_integrated_event_scenario

    scenario = fixture.get("scenario") or fixture.get("entity") or {}
    assessment = scenario.get("assessment") or {}
    assessment_result = validate_outcome_assessment_dataset(
        [assessment],
        objectives=[scenario.get("objective") or {}],
        events=scenario.get("events") or [],
        observations=scenario.get("observations") or [],
        evidence_snapshots=scenario.get("evidence_snapshots") or [],
        input_snapshots=scenario.get("input_snapshots") or [],
        freshness_rules=scenario.get("freshness_rules") or [],
        ambiguity_rules=scenario.get("ambiguity_rules") or [],
    )

    translated = dict(fixture)
    translated_scenario = dict(scenario)
    bindings = _normalized_bindings(assessment.get("evidence_bindings")) or ()
    translated_scenario["assessment"] = {
        "assessment_id": assessment.get("assessment_id"),
        "target_objective_ref": assessment.get("target_ref"),
        "rule_ref": assessment.get("criterion_ref"),
        "evidence_observation_refs": [
            evidence_ref
            for kind_ref, evidence_ref in bindings
            if kind_ref == "observation-record@1"
        ],
        "evidence_snapshot_ref": assessment.get("evidence_snapshot_ref"),
        "evaluator_ref": assessment.get("evaluator_ref"),
        "evaluated_at": assessment.get("evaluated_at"),
        "conclusion": "indeterminate",
        "provenance_ref": assessment.get("provenance_ref"),
    }
    translated["scenario"] = translated_scenario
    base_result = validate_integrated_event_scenario(translated)
    filtered_base_errors = [
        code
        for code in base_result.errors
        if code
        not in {
            "SCENARIO_ASSESSMENT_INVALID",
            "SCENARIO_CONFLICTING_EVIDENCE_POSITIVE",
            "SCENARIO_EVIDENCE_REFERENCE_UNRESOLVED",
        }
    ]
    return _result([*filtered_base_errors, *assessment_result.errors])
