from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .checker import ValidationResult


OUTCOME_ASSESSMENT_ERROR_CODES = frozenset(
    {
        "OUTCOME_ASSESSMENT_BINDING_MISMATCH",
        "OUTCOME_ASSESSMENT_CONCLUSION_INVALID",
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
        "OUTCOME_ASSESSMENT_INPUT_SNAPSHOT_UNRESOLVED",
        "OUTCOME_ASSESSMENT_KIND_REF_REQUIRED",
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
        "outcome_assessment_heads",
        "resolve_outcome_assessment",
    }
)

SUPPORTED_TARGET_KINDS = frozenset({"objective@1"})
SUPPORTED_EVIDENCE_KINDS = frozenset({"event@1", "observation-record@1"})
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


def validate_outcome_assessment(assessment: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []

    assessment_id = _normalized_ref(assessment.get("assessment_id"))
    if assessment_id is None:
        errors.append("OUTCOME_ASSESSMENT_ID_REQUIRED")
    if not _versioned_ref(assessment.get("assessment_kind_ref")):
        errors.append("OUTCOME_ASSESSMENT_KIND_REF_REQUIRED")

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


def _snapshot_index(value: Any) -> dict[str, tuple[tuple[str, str], ...]]:
    index: dict[str, tuple[tuple[str, str], ...]] = {}
    if not isinstance(value, list):
        return index
    for snapshot in value:
        if not isinstance(snapshot, dict):
            continue
        snapshot_ref = _normalized_ref(snapshot.get("snapshot_ref"))
        bindings = _normalized_bindings(snapshot.get("evidence_bindings"))
        if snapshot_ref is not None and bindings is not None:
            index[snapshot_ref] = bindings
    return index


def _ref_set(value: Any) -> set[str]:
    if isinstance(value, dict):
        values = value.keys()
    elif isinstance(value, list):
        values = value
    else:
        return set()
    return {
        normalized
        for item in values
        for normalized in [_normalized_ref(item)]
        if normalized is not None
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
) -> ValidationResult:
    errors: list[str] = []
    entries = list(assessments)
    objective_index = {
        objective_id: item
        for item in objectives
        if isinstance(item, dict)
        for objective_id in [_normalized_ref(item.get("objective_id"))]
        if objective_id is not None
    }
    event_index = {
        event_id: item
        for item in events
        if isinstance(item, dict)
        for event_id in [_normalized_ref(item.get("event_id"))]
        if event_id is not None
    }
    observation_index = {
        observation_id: item
        for item in observations
        if isinstance(item, dict)
        for observation_id in [_normalized_ref(item.get("observation_id"))]
        if observation_id is not None
    }
    snapshot_index = _snapshot_index(evidence_snapshots)
    input_snapshot_refs = _ref_set(input_snapshots)
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
            snapshot_bindings = snapshot_index.get(snapshot_ref)
            if snapshot_bindings is None:
                errors.append("OUTCOME_ASSESSMENT_EVIDENCE_SNAPSHOT_UNRESOLVED")
            elif bindings is not None and bindings != snapshot_bindings:
                errors.append("OUTCOME_ASSESSMENT_EVIDENCE_SNAPSHOT_MISMATCH")

        input_snapshot_ref = _normalized_ref(assessment.get("input_snapshot_ref"))
        if input_snapshot_ref is not None and input_snapshot_ref not in input_snapshot_refs:
            errors.append("OUTCOME_ASSESSMENT_INPUT_SNAPSHOT_UNRESOLVED")

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
        elif len(source_candidates) == 1 and _binding_identity(source_candidates[0]) != _binding_identity(target_candidates[0]):
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
        if requested_target_kind is not None and _normalized_ref(item.get("target_kind_ref")) != requested_target_kind:
            continue
        if requested_target is not None and _normalized_ref(item.get("target_ref")) != requested_target:
            continue
        if requested_criterion is not None and _normalized_ref(item.get("criterion_ref")) != requested_criterion:
            continue
        heads.append(item)
    return tuple(sorted(heads, key=lambda item: _normalized_ref(item.get("assessment_id")) or ""))


def effective_outcome_conclusion(
    assessments: Iterable[dict[str, Any]],
    target_kind_ref: Any,
    target_ref: Any,
    criterion_ref: Any,
) -> str | None:
    heads = outcome_assessment_heads(
        assessments,
        target_kind_ref=target_kind_ref,
        target_ref=target_ref,
        criterion_ref=criterion_ref,
    )
    if not heads:
        return None
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
