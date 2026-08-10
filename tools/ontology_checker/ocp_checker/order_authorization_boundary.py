from __future__ import annotations

from typing import Any

from ._common import nonempty, result
from .checker import ValidationResult


ORDER_AUTHORIZATION_BOUNDARY_ERROR_CODES = frozenset(
    {
        "ORDER_AUTHORIZATION_BOUNDARY_FIXTURE_INVALID",
        "ORDER_AUTHORIZATION_BOUNDARY_REQUEST_INVALID",
        "ORDER_AUTHORIZATION_BOUNDARY_QUESTION_INVALID",
        "ORDER_AUTHORIZATION_BOUNDARY_SNAPSHOT_INVALID",
        "ORDER_AUTHORIZATION_BOUNDARY_SNAPSHOT_UNRESOLVED",
        "ORDER_AUTHORIZATION_BOUNDARY_SNAPSHOT_AMBIGUOUS",
        "ORDER_AUTHORIZATION_BOUNDARY_BINDING_MISMATCH",
        "ORDER_AUTHORIZATION_BOUNDARY_SOURCE_CONTRACT_INVALID",
        "ORDER_AUTHORIZATION_BOUNDARY_EVIDENCE_STALE",
        "ORDER_AUTHORIZATION_BOUNDARY_SOURCE_RESULT_INVALID",
        "ORDER_AUTHORIZATION_BOUNDARY_POSITIVE_AUTHORITY_FORBIDDEN",
        "ORDER_AUTHORIZATION_BOUNDARY_CONCEPT_COUPLING_FORBIDDEN",
        "ORDER_AUTHORIZATION_BOUNDARY_CONVENIENCE_SELECTOR_FORBIDDEN",
        "ORDER_AUTHORIZATION_BOUNDARY_SELF_SUPPLY_FORBIDDEN",
        "ORDER_AUTHORIZATION_BOUNDARY_FORBIDDEN_COUPLING",
        "ORDER_AUTHORIZATION_BOUNDARY_RESULT_MISMATCH",
    }
)

ORDER_AUTHORIZATION_BOUNDARY_DERIVATION_RULES = frozenset(
    {"derive_order_authorization_boundary"}
)

QUESTIONS = frozenset(
    {
        "mandatory_order",
        "sufficient_order",
        "admissible_order_source",
    }
)
RULE_REFS = {
    "mandatory_order": "mandatory-order-establishment-boundary@1",
    "sufficient_order": "sufficient-order-establishment-boundary@1",
    "admissible_order_source": "admissible-order-source-establishment-boundary@1",
}
NEGATIVE_RESULTS = {
    "mandatory_order": "mandatory_order_not_established",
    "sufficient_order": "sufficient_order_authorization_not_established",
    "admissible_order_source": "admissible_order_source_not_established",
}
DERIVED_RESULTS = frozenset({"indeterminate", *NEGATIVE_RESULTS.values()})
SOURCE_CONTRACT_REF = "OCP-018@0.2.1"
SOURCE_RESULTS = frozenset({"accepted", "denied"})

DATASET_FIELDS = frozenset({"boundary_request", "authorization_snapshots", "claims"})
REQUEST_FIELDS = frozenset(
    {
        "request_id",
        "question",
        "rule_ref",
        "subject_operation_ref",
        "authorization_snapshot_ref",
        "stored_result",
    }
)
AUTHORIZATION_SNAPSHOT_FIELDS = frozenset(
    {
        "snapshot_ref",
        "subject_operation_ref",
        "source_contract_ref",
        "source_owner_ref",
        "input_snapshot_ref",
        "evaluation_context_ref",
        "evidence_state",
        "source_result",
        "order_candidate_ref",
    }
)
POSITIVE_AUTHORITY_FIELDS = frozenset(
    {
        "order_required",
        "order_sufficient",
        "order_admissible",
        "authorization_established",
        "permission_granted",
    }
)
CONCEPT_COUPLING_FIELDS = frozenset(
    {"order_concept_ref", "concept_status", "registry_entry", "graph_edge"}
)
CONVENIENCE_SELECTOR_FIELDS = frozenset(
    {"newest_timestamp", "record_order", "source_count", "issuer_count", "caller_identity"}
)
SELF_SUPPLY_FIELDS = frozenset({"activation_attempt"})
FORBIDDEN_FIELDS = frozenset(
    {
        "authority_concept_ref",
        "approval_concept_ref",
        "policy_concept_ref",
        "lifecycle_stage",
        "assignment_mutation",
        "production_profile",
    }
)


def _text(value: Any) -> str | None:
    return str(value).strip() if nonempty(value) else None


def _contains_named(value: Any, names: frozenset[str]) -> bool:
    if isinstance(value, dict):
        return any(
            (key in names and item not in (None, False, "", [], {}))
            or _contains_named(item, names)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_named(item, names) for item in value)
    return False


def _request_valid(request: Any) -> bool:
    return bool(
        isinstance(request, dict)
        and set(request) == REQUEST_FIELDS
        and all(_text(request.get(field)) is not None for field in REQUEST_FIELDS)
    )


def _snapshot_valid(snapshot: Any) -> bool:
    return bool(
        isinstance(snapshot, dict)
        and set(snapshot) == AUTHORIZATION_SNAPSHOT_FIELDS
        and all(
            _text(snapshot.get(field)) is not None
            for field in AUTHORIZATION_SNAPSHOT_FIELDS
        )
        and snapshot.get("evidence_state") in {"current", "stale"}
    )


def _resolution_count(request: dict[str, Any], snapshots: list[Any]) -> int:
    return sum(
        1
        for snapshot in snapshots
        if isinstance(snapshot, dict)
        and _text(snapshot.get("snapshot_ref"))
        == _text(request.get("authorization_snapshot_ref"))
    )


def _selected_snapshot(
    request: dict[str, Any], snapshots: list[Any]
) -> dict[str, Any] | None:
    selected = [
        snapshot
        for snapshot in snapshots
        if isinstance(snapshot, dict)
        and _text(snapshot.get("snapshot_ref"))
        == _text(request.get("authorization_snapshot_ref"))
    ]
    return selected[0] if len(selected) == 1 else None


def derive_order_authorization_boundary(dataset: Any) -> str:
    """Derive only one of the three negative Order authority results."""
    if not isinstance(dataset, dict) or set(dataset) != DATASET_FIELDS:
        return "indeterminate"
    claims = dataset.get("claims")
    if not isinstance(claims, dict) or any(
        _contains_named(claims, names)
        for names in (
            POSITIVE_AUTHORITY_FIELDS,
            CONCEPT_COUPLING_FIELDS,
            CONVENIENCE_SELECTOR_FIELDS,
            SELF_SUPPLY_FIELDS,
            FORBIDDEN_FIELDS,
        )
    ):
        return "indeterminate"
    request = dataset.get("boundary_request")
    snapshots = dataset.get("authorization_snapshots")
    if not _request_valid(request) or not isinstance(snapshots, list):
        return "indeterminate"
    question = request.get("question")
    if (
        question not in QUESTIONS
        or request.get("rule_ref") != RULE_REFS.get(question)
        or request.get("stored_result") not in DERIVED_RESULTS
    ):
        return "indeterminate"
    selected = _selected_snapshot(request, snapshots)
    if selected is None or not _snapshot_valid(selected):
        return "indeterminate"
    if (
        _text(selected.get("subject_operation_ref"))
        != _text(request.get("subject_operation_ref"))
        or selected.get("source_contract_ref") != SOURCE_CONTRACT_REF
        or selected.get("evidence_state") != "current"
        or selected.get("source_result") not in SOURCE_RESULTS
    ):
        return "indeterminate"
    return NEGATIVE_RESULTS[question]


def validate_order_authorization_boundary_dataset(dataset: Any) -> ValidationResult:
    if not isinstance(dataset, dict) or set(dataset) != DATASET_FIELDS:
        return result(["ORDER_AUTHORIZATION_BOUNDARY_FIXTURE_INVALID"])

    errors: list[str] = []
    request = dataset.get("boundary_request")
    snapshots = dataset.get("authorization_snapshots")
    claims = dataset.get("claims")
    if not isinstance(claims, dict):
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_FIXTURE_INVALID")
        claims = {}
    if _contains_named(claims, POSITIVE_AUTHORITY_FIELDS):
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_POSITIVE_AUTHORITY_FORBIDDEN")
    if _contains_named(claims, CONCEPT_COUPLING_FIELDS):
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_CONCEPT_COUPLING_FORBIDDEN")
    if _contains_named(claims, CONVENIENCE_SELECTOR_FIELDS):
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_CONVENIENCE_SELECTOR_FORBIDDEN")
    if _contains_named(claims, SELF_SUPPLY_FIELDS):
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_SELF_SUPPLY_FORBIDDEN")
    if _contains_named(claims, FORBIDDEN_FIELDS):
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_FORBIDDEN_COUPLING")

    if not _request_valid(request):
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_REQUEST_INVALID")
    if not isinstance(request, dict):
        return result(errors)

    question = request.get("question")
    if question not in QUESTIONS or request.get("rule_ref") != RULE_REFS.get(question):
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_QUESTION_INVALID")

    if not isinstance(snapshots, list):
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_SNAPSHOT_UNRESOLVED")
        snapshots = []
    resolution_count = _resolution_count(request, snapshots)
    if resolution_count == 0:
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_SNAPSHOT_UNRESOLVED")
    elif resolution_count > 1:
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_SNAPSHOT_AMBIGUOUS")
    selected = _selected_snapshot(request, snapshots)
    if selected is not None:
        if not _snapshot_valid(selected):
            errors.append("ORDER_AUTHORIZATION_BOUNDARY_SNAPSHOT_INVALID")
        if _text(selected.get("subject_operation_ref")) != _text(
            request.get("subject_operation_ref")
        ):
            errors.append("ORDER_AUTHORIZATION_BOUNDARY_BINDING_MISMATCH")
        if selected.get("source_contract_ref") != SOURCE_CONTRACT_REF:
            errors.append("ORDER_AUTHORIZATION_BOUNDARY_SOURCE_CONTRACT_INVALID")
        if selected.get("evidence_state") == "stale":
            errors.append("ORDER_AUTHORIZATION_BOUNDARY_EVIDENCE_STALE")
        if selected.get("source_result") not in SOURCE_RESULTS:
            errors.append("ORDER_AUTHORIZATION_BOUNDARY_SOURCE_RESULT_INVALID")

    derived = derive_order_authorization_boundary(dataset)
    if request.get("stored_result") != derived:
        errors.append("ORDER_AUTHORIZATION_BOUNDARY_RESULT_MISMATCH")
    return result(errors)


def validate_order_authorization_boundary_fixture(
    fixture: dict[str, Any],
) -> ValidationResult:
    if fixture.get("concept") != "OrderAuthorizationBoundaryDataset":
        return result(["ORDER_AUTHORIZATION_BOUNDARY_FIXTURE_INVALID"])
    return validate_order_authorization_boundary_dataset(fixture.get("dataset"))
