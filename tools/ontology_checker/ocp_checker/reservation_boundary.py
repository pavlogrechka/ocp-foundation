from __future__ import annotations

from typing import Any

from ._common import nonempty, result
from .checker import ValidationResult


RESERVATION_BOUNDARY_ERROR_CODES = frozenset(
    {
        "RESERVATION_BOUNDARY_FIXTURE_INVALID",
        "RESERVATION_BOUNDARY_REQUEST_INVALID",
        "RESERVATION_BOUNDARY_BRANCH_INVALID",
        "RESERVATION_BOUNDARY_ACTION_INVALID",
        "RESERVATION_BOUNDARY_SNAPSHOT_INVALID",
        "RESERVATION_BOUNDARY_SNAPSHOT_UNRESOLVED",
        "RESERVATION_BOUNDARY_SNAPSHOT_AMBIGUOUS",
        "RESERVATION_BOUNDARY_BINDING_MISMATCH",
        "RESERVATION_BOUNDARY_EVIDENCE_STALE",
        "RESERVATION_BOUNDARY_QUANTITATIVE_PREREQUISITE_INVALID",
        "RESERVATION_BOUNDARY_BRANCH_COUPLING_FORBIDDEN",
        "RESERVATION_BOUNDARY_POSITIVE_AUTHORITY_FORBIDDEN",
        "RESERVATION_BOUNDARY_SELF_SUPPLY_FORBIDDEN",
        "RESERVATION_BOUNDARY_FORBIDDEN_COUPLING",
        "RESERVATION_BOUNDARY_RESULT_MISMATCH",
    }
)

RESERVATION_BOUNDARY_DERIVATION_RULES = frozenset(
    {
        "derive_whole_resource_reservation_boundary",
        "derive_quantitative_reservation_boundary",
    }
)

WHOLE_RESOURCE_BRANCH = "whole_resource_exclusivity"
QUANTITATIVE_BRANCH = "partial_quantitative"
BRANCHES = frozenset({WHOLE_RESOURCE_BRANCH, QUANTITATIVE_BRANCH})
ACTIONS = frozenset({"reservation", "allocation"})
QUANTITATIVE_CONTRACT_REF = "OCP-020@0.2.0"
RULE_REFS = {
    WHOLE_RESOURCE_BRANCH: "whole-resource-reservation-allocation-boundary@1",
    QUANTITATIVE_BRANCH: "quantitative-reservation-allocation-boundary@1",
}
NEGATIVE_RESULTS = {
    (WHOLE_RESOURCE_BRANCH, "reservation"): "whole_resource_reservation_not_established",
    (WHOLE_RESOURCE_BRANCH, "allocation"): "whole_resource_allocation_not_established",
    (QUANTITATIVE_BRANCH, "reservation"): "quantitative_reservation_not_established",
    (QUANTITATIVE_BRANCH, "allocation"): "quantitative_allocation_not_established",
}
DERIVED_RESULTS = frozenset({"indeterminate", *NEGATIVE_RESULTS.values()})
POSITIVE_RESULTS = frozenset({"reserved", "allocated", "available", "capacity_sufficient"})

DATASET_FIELDS = frozenset({"establishment_request", "resource_snapshots"})
REQUEST_FIELDS = frozenset(
    {
        "request_id",
        "branch",
        "action",
        "rule_ref",
        "resource_ref",
        "context_ref",
        "resource_snapshot_ref",
        "quantitative_contract_ref",
        "stored_result",
    }
)
RESOURCE_SNAPSHOT_FIELDS = frozenset(
    {
        "snapshot_ref",
        "resource_ref",
        "context_ref",
        "evidence_state",
        "assignment_refs",
        "constraint_evaluation_refs",
        "quantitative_input_snapshot_ref",
    }
)
POSITIVE_AUTHORITY_FIELDS = frozenset(
    {
        "reserved",
        "allocated",
        "reservation_established",
        "allocation_established",
        "exclusive_permission",
        "positive_result",
    }
)
FORBIDDEN_FIELDS = frozenset(
    {
        "availability",
        "capacity_sufficient",
        "remaining_capacity",
        "assignment_mutation",
        "lifecycle_transition",
        "authorization",
        "permission",
        "risk",
        "conflict",
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


def _contains_self_supply(value: Any) -> bool:
    if isinstance(value, dict):
        return bool(value.get("activation_attempt")) or any(
            _contains_self_supply(item) for item in value.values()
        )
    if isinstance(value, list):
        return any(_contains_self_supply(item) for item in value)
    return False


def _request_shape_valid(request: Any) -> bool:
    if not isinstance(request, dict) or set(request) != REQUEST_FIELDS:
        return False
    return bool(
        all(
            _text(request.get(field)) is not None
            for field in (
                "request_id",
                "branch",
                "action",
                "rule_ref",
                "resource_ref",
                "context_ref",
                "resource_snapshot_ref",
                "stored_result",
            )
        )
        and (
            request.get("quantitative_contract_ref") is None
            or _text(request.get("quantitative_contract_ref")) is not None
        )
    )


def _reference_list_valid(value: Any, *, require_one: bool) -> bool:
    if not isinstance(value, list) or (require_one and not value):
        return False
    normalized = [_text(item) for item in value]
    return all(item is not None for item in normalized) and len(normalized) == len(set(normalized))


def _snapshot_valid(snapshot: Any) -> bool:
    if not isinstance(snapshot, dict) or set(snapshot) != RESOURCE_SNAPSHOT_FIELDS:
        return False
    quantitative_ref = snapshot.get("quantitative_input_snapshot_ref")
    return bool(
        all(
            _text(snapshot.get(field)) is not None
            for field in ("snapshot_ref", "resource_ref", "context_ref")
        )
        and snapshot.get("evidence_state") in {"current", "stale"}
        and _reference_list_valid(snapshot.get("assignment_refs"), require_one=True)
        and _reference_list_valid(snapshot.get("constraint_evaluation_refs"), require_one=False)
        and (quantitative_ref is None or _text(quantitative_ref) is not None)
    )


def _selected_snapshot(request: dict[str, Any], snapshots: list[Any]) -> dict[str, Any] | None:
    selected = [
        item
        for item in snapshots
        if isinstance(item, dict)
        and _text(item.get("snapshot_ref")) == _text(request.get("resource_snapshot_ref"))
    ]
    return selected[0] if len(selected) == 1 else None


def _snapshot_resolution_count(request: dict[str, Any], snapshots: list[Any]) -> int:
    return sum(
        1
        for item in snapshots
        if isinstance(item, dict)
        and _text(item.get("snapshot_ref")) == _text(request.get("resource_snapshot_ref"))
    )


def _branch_coupling_valid(request: dict[str, Any], snapshot: dict[str, Any]) -> bool:
    branch = request.get("branch")
    contract_ref = request.get("quantitative_contract_ref")
    quantitative_snapshot_ref = snapshot.get("quantitative_input_snapshot_ref")
    if branch == WHOLE_RESOURCE_BRANCH:
        return contract_ref is None and quantitative_snapshot_ref is None
    if branch == QUANTITATIVE_BRANCH:
        return (
            contract_ref == QUANTITATIVE_CONTRACT_REF
            and _text(quantitative_snapshot_ref) is not None
        )
    return False


def _derive(dataset: Any, expected_branch: str) -> str:
    if (
        not isinstance(dataset, dict)
        or set(dataset) != DATASET_FIELDS
        or _contains_named(dataset, POSITIVE_AUTHORITY_FIELDS)
        or _contains_named(dataset, FORBIDDEN_FIELDS)
        or _contains_self_supply(dataset)
    ):
        return "indeterminate"
    request = dataset.get("establishment_request")
    snapshots = dataset.get("resource_snapshots")
    if not _request_shape_valid(request) or not isinstance(snapshots, list):
        return "indeterminate"
    branch = request.get("branch")
    action = request.get("action")
    if (
        branch != expected_branch
        or branch not in BRANCHES
        or action not in ACTIONS
        or request.get("rule_ref") != RULE_REFS.get(branch)
        or request.get("stored_result") not in DERIVED_RESULTS
    ):
        return "indeterminate"
    selected = _selected_snapshot(request, snapshots)
    if selected is None or not _snapshot_valid(selected):
        return "indeterminate"
    if (
        _text(selected.get("resource_ref")) != _text(request.get("resource_ref"))
        or _text(selected.get("context_ref")) != _text(request.get("context_ref"))
        or selected.get("evidence_state") != "current"
        or not _branch_coupling_valid(request, selected)
    ):
        return "indeterminate"
    return NEGATIVE_RESULTS[(branch, action)]


def derive_whole_resource_reservation_boundary(dataset: Any) -> str:
    """Derive only branch E's negative authority result."""
    return _derive(dataset, WHOLE_RESOURCE_BRANCH)


def derive_quantitative_reservation_boundary(dataset: Any) -> str:
    """Derive only branch Q's negative authority result."""
    return _derive(dataset, QUANTITATIVE_BRANCH)


def validate_reservation_boundary_dataset(dataset: Any) -> ValidationResult:
    if not isinstance(dataset, dict) or set(dataset) != DATASET_FIELDS:
        return result(["RESERVATION_BOUNDARY_FIXTURE_INVALID"])

    errors: list[str] = []
    request = dataset.get("establishment_request")
    snapshots = dataset.get("resource_snapshots")
    if _contains_named(dataset, POSITIVE_AUTHORITY_FIELDS):
        errors.append("RESERVATION_BOUNDARY_POSITIVE_AUTHORITY_FORBIDDEN")
    if _contains_self_supply(dataset):
        errors.append("RESERVATION_BOUNDARY_SELF_SUPPLY_FORBIDDEN")
    if _contains_named(dataset, FORBIDDEN_FIELDS):
        errors.append("RESERVATION_BOUNDARY_FORBIDDEN_COUPLING")
    if not _request_shape_valid(request):
        errors.append("RESERVATION_BOUNDARY_REQUEST_INVALID")
    if not isinstance(request, dict):
        return result(errors)

    if request.get("stored_result") in POSITIVE_RESULTS:
        errors.append("RESERVATION_BOUNDARY_POSITIVE_AUTHORITY_FORBIDDEN")

    branch = request.get("branch")
    action = request.get("action")
    if branch not in BRANCHES or request.get("rule_ref") != RULE_REFS.get(branch):
        errors.append("RESERVATION_BOUNDARY_BRANCH_INVALID")
    if action not in ACTIONS:
        errors.append("RESERVATION_BOUNDARY_ACTION_INVALID")

    if not isinstance(snapshots, list):
        errors.append("RESERVATION_BOUNDARY_SNAPSHOT_UNRESOLVED")
        snapshots = []
    resolution_count = _snapshot_resolution_count(request, snapshots)
    if resolution_count == 0:
        errors.append("RESERVATION_BOUNDARY_SNAPSHOT_UNRESOLVED")
    elif resolution_count > 1:
        errors.append("RESERVATION_BOUNDARY_SNAPSHOT_AMBIGUOUS")
    selected = _selected_snapshot(request, snapshots)
    if selected is not None:
        if not _snapshot_valid(selected):
            errors.append("RESERVATION_BOUNDARY_SNAPSHOT_INVALID")
        if (
            _text(selected.get("resource_ref")) != _text(request.get("resource_ref"))
            or _text(selected.get("context_ref")) != _text(request.get("context_ref"))
        ):
            errors.append("RESERVATION_BOUNDARY_BINDING_MISMATCH")
        if selected.get("evidence_state") == "stale":
            errors.append("RESERVATION_BOUNDARY_EVIDENCE_STALE")

        contract_ref = request.get("quantitative_contract_ref")
        quantitative_snapshot_ref = selected.get("quantitative_input_snapshot_ref")
        if branch == QUANTITATIVE_BRANCH and (
            contract_ref != QUANTITATIVE_CONTRACT_REF
            or _text(quantitative_snapshot_ref) is None
        ):
            errors.append("RESERVATION_BOUNDARY_QUANTITATIVE_PREREQUISITE_INVALID")
        if branch == WHOLE_RESOURCE_BRANCH and (
            contract_ref is not None or quantitative_snapshot_ref is not None
        ):
            errors.append("RESERVATION_BOUNDARY_BRANCH_COUPLING_FORBIDDEN")

    if branch == WHOLE_RESOURCE_BRANCH:
        derived = derive_whole_resource_reservation_boundary(dataset)
    elif branch == QUANTITATIVE_BRANCH:
        derived = derive_quantitative_reservation_boundary(dataset)
    else:
        derived = "indeterminate"
    if request.get("stored_result") not in DERIVED_RESULTS or request.get("stored_result") != derived:
        errors.append("RESERVATION_BOUNDARY_RESULT_MISMATCH")
    return result(errors)


def validate_reservation_boundary_fixture(fixture: dict[str, Any]) -> ValidationResult:
    dataset = fixture.get("dataset")
    if not isinstance(dataset, dict):
        return result(["RESERVATION_BOUNDARY_FIXTURE_INVALID"])
    return validate_reservation_boundary_dataset(dataset)
