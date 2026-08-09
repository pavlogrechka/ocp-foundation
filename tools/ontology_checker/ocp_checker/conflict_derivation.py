from __future__ import annotations

from collections import defaultdict
from typing import Any

from ._common import nonempty, parse_time, result
from .checker import ValidationResult


CONFLICT_DERIVATION_ERROR_CODES = frozenset(
    {
        "CONFLICT_DERIVATION_FIXTURE_INVALID",
        "CONFLICT_DERIVATION_REQUEST_INVALID",
        "CONFLICT_DERIVATION_EVALUATION_INVALID",
        "CONFLICT_DERIVATION_EVALUATION_DUPLICATE",
        "CONFLICT_DERIVATION_EVALUATION_UNRESOLVED",
        "CONFLICT_DERIVATION_EVALUATION_AMBIGUOUS",
        "CONFLICT_DERIVATION_BINDING_MISMATCH",
        "CONFLICT_DERIVATION_STALE_INPUT",
        "CONFLICT_DERIVATION_RESULT_MISMATCH",
        "CONFLICT_DERIVATION_POSITIVE_AUTHORITY_FORBIDDEN",
        "CONFLICT_DERIVATION_FORBIDDEN_COUPLING",
    }
)

CONFLICT_DERIVATION_DERIVATION_RULES = frozenset(
    {"derive_conflict_establishment_result"}
)

BOUNDARY_RULE_REF = "conflict-establishment-boundary@1"
EVALUATION_RESULTS = frozenset(
    {"satisfied", "violated", "indeterminate", "not_applicable"}
)
DERIVED_RESULTS = frozenset({"conflict_not_established", "indeterminate"})
FORBIDDEN_FIELDS = frozenset(
    {
        "conflict",
        "conflict_id",
        "conflict_record",
        "conflict_result",
        "risk",
        "risk_ref",
        "risk_level",
        "policy_ref",
        "precedence",
        "override",
        "waiver",
        "remediation",
        "lifecycle_stage",
        "lifecycle_transition",
        "assignment_mutation",
        "capacity",
        "quantity",
    }
)
POSITIVE_AUTHORITY_FIELDS = frozenset(
    {"positive_conflict", "conflict_present", "conflict_established", "derived_conflict"}
)
SNAPSHOT_FIELDS = frozenset({"derivation_request", "constraint_evaluations"})
REQUEST_FIELDS = frozenset(
    {
        "request_id",
        "rule_ref",
        "context_ref",
        "input_snapshot_ref",
        "evaluation_refs",
        "derived_at",
        "evidence_state",
        "stored_result",
    }
)
EVALUATION_FIELDS = frozenset(
    {
        "evaluation_id",
        "constraint_ref",
        "constraint_version_ref",
        "context_ref",
        "input_snapshot_ref",
        "evaluated_at",
        "result",
        "evidence_refs",
        "evaluator_ref",
    }
)


def _text(value: Any) -> str | None:
    return str(value).strip() if nonempty(value) else None


def _versioned_ref(value: Any) -> str | None:
    text = _text(value)
    if text is None or "@" not in text:
        return None
    identity, version = text.rsplit("@", 1)
    return text if identity.strip() and version.strip() else None


def _contains_forbidden(value: Any) -> bool:
    if isinstance(value, dict):
        return any(
            (key in FORBIDDEN_FIELDS and item not in (None, False, "", [], {}))
            or _contains_forbidden(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_forbidden(item) for item in value)
    return False


def _contains_positive_authority(value: Any) -> bool:
    if isinstance(value, dict):
        return any(
            (key in POSITIVE_AUTHORITY_FIELDS and item not in (None, False, "", [], {}))
            or _contains_positive_authority(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_positive_authority(item) for item in value)
    return False


def _request_valid(request: Any) -> bool:
    if not isinstance(request, dict):
        return False
    refs = request.get("evaluation_refs")
    return bool(
        set(request) <= REQUEST_FIELDS
        and _text(request.get("request_id")) is not None
        and request.get("rule_ref") == BOUNDARY_RULE_REF
        and _text(request.get("context_ref")) is not None
        and _text(request.get("input_snapshot_ref")) is not None
        and isinstance(refs, list)
        and refs
        and all(_text(item) is not None for item in refs)
        and parse_time(request.get("derived_at")) is not None
        and request.get("evidence_state") in {"current", "stale"}
        and request.get("stored_result") in DERIVED_RESULTS
    )


def _evaluation_valid(evaluation: Any) -> bool:
    if not isinstance(evaluation, dict):
        return False
    return bool(
        set(evaluation) <= EVALUATION_FIELDS
        and all(
            _text(evaluation.get(field)) is not None
            for field in (
                "evaluation_id",
                "constraint_ref",
                "context_ref",
                "input_snapshot_ref",
                "evaluator_ref",
            )
        )
        and isinstance(evaluation.get("evidence_refs"), list)
        and all(_text(item) is not None for item in evaluation.get("evidence_refs") or [])
        and _versioned_ref(evaluation.get("constraint_version_ref")) is not None
        and parse_time(evaluation.get("evaluated_at")) is not None
        and evaluation.get("result") in EVALUATION_RESULTS
    )


def _selected_evaluations(
    request: dict[str, Any], evaluations: list[dict[str, Any]]
) -> list[dict[str, Any]] | None:
    by_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for evaluation in evaluations:
        evaluation_id = _text(evaluation.get("evaluation_id"))
        if evaluation_id is not None:
            by_id[evaluation_id].append(evaluation)
    selected: list[dict[str, Any]] = []
    for reference in request.get("evaluation_refs") or []:
        matches = by_id.get(_text(reference) or "", [])
        if len(matches) != 1:
            return None
        selected.append(matches[0])
    return selected


def _ambiguous(evaluations: list[dict[str, Any]]) -> bool:
    results: dict[tuple[str | None, str | None, str | None], set[Any]] = defaultdict(set)
    for evaluation in evaluations:
        key = tuple(
            _text(evaluation.get(field))
            for field in ("constraint_version_ref", "context_ref", "input_snapshot_ref")
        )
        results[key].add(evaluation.get("result"))
    return any(len(values) > 1 for values in results.values())


def derive_conflict_establishment_result(snapshot: dict[str, Any]) -> str:
    """Apply OCP-019's negative boundary without asserting Conflict presence or absence."""
    if (
        not isinstance(snapshot, dict)
        or set(snapshot) != SNAPSHOT_FIELDS
        or _contains_forbidden(snapshot)
        or _contains_positive_authority(snapshot)
    ):
        return "indeterminate"
    request = snapshot.get("derivation_request")
    evaluations = snapshot.get("constraint_evaluations")
    if not _request_valid(request) or not isinstance(evaluations, list):
        return "indeterminate"
    typed = [item for item in evaluations if isinstance(item, dict)]
    refs = [_text(item) for item in request.get("evaluation_refs") or []]
    if len(refs) != len(set(refs)):
        return "indeterminate"
    selected = _selected_evaluations(request, typed)
    if selected is None or any(not _evaluation_valid(item) for item in selected):
        return "indeterminate"
    if _ambiguous(selected):
        return "indeterminate"
    if request.get("evidence_state") != "current":
        return "indeterminate"
    derived_at = parse_time(request.get("derived_at"))
    for evaluation in selected:
        if (
            _text(evaluation.get("context_ref")) != _text(request.get("context_ref"))
            or _text(evaluation.get("input_snapshot_ref"))
            != _text(request.get("input_snapshot_ref"))
            or parse_time(evaluation.get("evaluated_at")) is None
            or derived_at is None
            or parse_time(evaluation.get("evaluated_at")) > derived_at
        ):
            return "indeterminate"
    if any(item.get("result") == "indeterminate" for item in selected):
        return "indeterminate"
    return "conflict_not_established"


def validate_conflict_derivation_dataset(snapshot: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    request = snapshot.get("derivation_request")
    evaluations = snapshot.get("constraint_evaluations")
    if not isinstance(request, dict) or not isinstance(evaluations, list):
        return result(["CONFLICT_DERIVATION_REQUEST_INVALID"])
    if set(snapshot) != SNAPSHOT_FIELDS or _contains_forbidden(snapshot):
        errors.append("CONFLICT_DERIVATION_FORBIDDEN_COUPLING")
    if request.get("stored_result") == "conflict" or _contains_positive_authority(snapshot):
        errors.append("CONFLICT_DERIVATION_POSITIVE_AUTHORITY_FORBIDDEN")
    if not _request_valid(request):
        errors.append("CONFLICT_DERIVATION_REQUEST_INVALID")

    typed = [item for item in evaluations if isinstance(item, dict)]
    refs = [_text(item) for item in request.get("evaluation_refs") or []]
    if len(refs) != len(set(refs)):
        errors.append("CONFLICT_DERIVATION_EVALUATION_DUPLICATE")
    selected = _selected_evaluations(request, typed)
    if selected is None:
        errors.append("CONFLICT_DERIVATION_EVALUATION_UNRESOLVED")
        selected = []
    if any(not _evaluation_valid(item) for item in selected):
        errors.append("CONFLICT_DERIVATION_EVALUATION_INVALID")
    if _ambiguous(selected):
        errors.append("CONFLICT_DERIVATION_EVALUATION_AMBIGUOUS")
    if any(
        _text(item.get("context_ref")) != _text(request.get("context_ref"))
        or _text(item.get("input_snapshot_ref")) != _text(request.get("input_snapshot_ref"))
        for item in selected
    ):
        errors.append("CONFLICT_DERIVATION_BINDING_MISMATCH")
    derived_at = parse_time(request.get("derived_at"))
    if request.get("evidence_state") == "stale" or any(
        parse_time(item.get("evaluated_at")) is not None
        and derived_at is not None
        and parse_time(item.get("evaluated_at")) > derived_at
        for item in selected
    ):
        errors.append("CONFLICT_DERIVATION_STALE_INPUT")
    derived = derive_conflict_establishment_result(snapshot)
    if request.get("stored_result") not in DERIVED_RESULTS or request.get("stored_result") != derived:
        errors.append("CONFLICT_DERIVATION_RESULT_MISMATCH")
    return result(errors)


def validate_conflict_derivation_fixture(fixture: dict[str, Any]) -> ValidationResult:
    snapshot = fixture.get("snapshot")
    if not isinstance(snapshot, dict):
        return result(["CONFLICT_DERIVATION_FIXTURE_INVALID"])
    return validate_conflict_derivation_dataset(snapshot)
