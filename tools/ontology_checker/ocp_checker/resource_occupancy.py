from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ._common import nonempty, parse_time, result
from .checker import ValidationResult, assignment_effective_at, validate_assignment


RESOURCE_OCCUPANCY_ERROR_CODES = frozenset(
    {
        "RESOURCE_OCCUPANCY_FIXTURE_INVALID",
        "RESOURCE_OCCUPANCY_REQUEST_INVALID",
        "RESOURCE_OCCUPANCY_SNAPSHOT_INVALID",
        "RESOURCE_OCCUPANCY_SNAPSHOT_UNRESOLVED",
        "RESOURCE_OCCUPANCY_SNAPSHOT_AMBIGUOUS",
        "RESOURCE_OCCUPANCY_BINDING_MISMATCH",
        "RESOURCE_OCCUPANCY_COMPLETENESS_EVIDENCE_REQUIRED",
        "RESOURCE_OCCUPANCY_ASSIGNMENT_INVALID",
        "RESOURCE_OCCUPANCY_ASSIGNMENT_DUPLICATE",
        "RESOURCE_OCCUPANCY_ACTIVATION_FORBIDDEN",
        "RESOURCE_OCCUPANCY_FORBIDDEN_COUPLING",
        "RESOURCE_OCCUPANCY_RESULT_MISMATCH",
    }
)

RESOURCE_OCCUPANCY_DERIVATION_RULES = frozenset({"derive_resource_occupancy"})

RULE_REF = "resource-occupancy-at@0.1.0"
SYNTHETIC_COMPLETENESS_PREFIX = "SYNTH-COMPLETE-"
DATASET_FIELDS = frozenset({"occupancy_request", "assignment_snapshots"})
REQUEST_FIELDS = frozenset(
    {
        "request_id",
        "rule_ref",
        "resource_ref",
        "evaluation_time",
        "assignment_snapshot_ref",
        "stored_occupied",
        "stored_witness_assignment_refs",
    }
)
SNAPSHOT_FIELDS = frozenset(
    {
        "snapshot_ref",
        "resource_ref",
        "completeness_evidence_ref",
        "assignments",
    }
)
ACTIVATION_FIELDS = frozenset(
    {
        "activation_state",
        "accepted_consumer_ref",
        "activation_baseline_ref",
        "owner_evaluator_ref",
    }
)
FORBIDDEN_FIELDS = frozenset(
    {
        "conflict",
        "conflict_established",
        "priority",
        "selection_order",
        "capacity",
        "remaining_capacity",
        "reservation",
        "allocation",
        "permission",
        "authorization",
        "assignment_lifecycle_transition",
        "action_recommendation",
    }
)


@dataclass(frozen=True)
class ResourceOccupancyResult:
    occupied: bool | None
    witness_assignment_refs: tuple[str, ...]


INDETERMINATE = ResourceOccupancyResult(None, ())


def _text(value: Any) -> str | None:
    return str(value).strip() if nonempty(value) else None


def _completeness_ref_valid(value: Any) -> bool:
    normalized = _text(value)
    return bool(normalized and normalized.startswith(SYNTHETIC_COMPLETENESS_PREFIX))


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
    if not isinstance(request, dict) or set(request) != REQUEST_FIELDS:
        return False
    witnesses = request.get("stored_witness_assignment_refs")
    return bool(
        all(
            _text(request.get(field)) is not None
            for field in (
                "request_id",
                "rule_ref",
                "resource_ref",
                "evaluation_time",
                "assignment_snapshot_ref",
            )
        )
        and parse_time(request.get("evaluation_time")) is not None
        and isinstance(request.get("stored_occupied"), bool)
        and isinstance(witnesses, list)
        and all(_text(item) is not None for item in witnesses)
        and len(witnesses) == len(set(witnesses))
    )


def _snapshot_valid(snapshot: Any) -> bool:
    return bool(
        isinstance(snapshot, dict)
        and set(snapshot) == SNAPSHOT_FIELDS
        and _text(snapshot.get("snapshot_ref")) is not None
        and _text(snapshot.get("resource_ref")) is not None
        and isinstance(snapshot.get("assignments"), list)
    )


def _resolution_count(request: dict[str, Any], snapshots: list[Any]) -> int:
    return sum(
        1
        for snapshot in snapshots
        if isinstance(snapshot, dict)
        and _text(snapshot.get("snapshot_ref"))
        == _text(request.get("assignment_snapshot_ref"))
    )


def _selected_snapshot(
    request: dict[str, Any], snapshots: list[Any]
) -> dict[str, Any] | None:
    matches = [
        snapshot
        for snapshot in snapshots
        if isinstance(snapshot, dict)
        and _text(snapshot.get("snapshot_ref"))
        == _text(request.get("assignment_snapshot_ref"))
    ]
    return matches[0] if len(matches) == 1 else None


def _assignment_ids(assignments: list[Any]) -> tuple[str | None, ...]:
    return tuple(
        _text(item.get("assignment_id")) if isinstance(item, dict) else None
        for item in assignments
    )


def derive_resource_occupancy(dataset: Any) -> ResourceOccupancyResult:
    if (
        not isinstance(dataset, dict)
        or set(dataset) != DATASET_FIELDS
        or _contains_named(dataset, ACTIVATION_FIELDS)
        or _contains_named(dataset, FORBIDDEN_FIELDS)
    ):
        return INDETERMINATE
    request = dataset.get("occupancy_request")
    snapshots = dataset.get("assignment_snapshots")
    if not _request_valid(request) or not isinstance(snapshots, list):
        return INDETERMINATE
    if request.get("rule_ref") != RULE_REF:
        return INDETERMINATE
    snapshot = _selected_snapshot(request, snapshots)
    if snapshot is None or not _snapshot_valid(snapshot):
        return INDETERMINATE
    if snapshot.get("resource_ref") != request.get("resource_ref"):
        return INDETERMINATE
    if not _completeness_ref_valid(snapshot.get("completeness_evidence_ref")):
        return INDETERMINATE
    assignments = snapshot.get("assignments")
    ids = _assignment_ids(assignments)
    if (
        any(item is None for item in ids)
        or len(ids) != len(set(ids))
        or any(
            not isinstance(item, dict)
            or not validate_assignment(item).valid
            or item.get("resource_ref") != request.get("resource_ref")
            for item in assignments
        )
    ):
        return INDETERMINATE
    witnesses = tuple(
        sorted(
            str(item["assignment_id"])
            for item in assignments
            if assignment_effective_at(item, str(request["evaluation_time"]))
        )
    )
    return ResourceOccupancyResult(bool(witnesses), witnesses)


def validate_resource_occupancy_dataset(dataset: Any) -> ValidationResult:
    errors: list[str] = []
    if not isinstance(dataset, dict) or set(dataset) != DATASET_FIELDS:
        return result(("RESOURCE_OCCUPANCY_FIXTURE_INVALID",))

    if _contains_named(dataset, ACTIVATION_FIELDS):
        errors.append("RESOURCE_OCCUPANCY_ACTIVATION_FORBIDDEN")
    if _contains_named(dataset, FORBIDDEN_FIELDS):
        errors.append("RESOURCE_OCCUPANCY_FORBIDDEN_COUPLING")

    request = dataset.get("occupancy_request")
    snapshots = dataset.get("assignment_snapshots")
    if not _request_valid(request):
        errors.append("RESOURCE_OCCUPANCY_REQUEST_INVALID")
        request = request if isinstance(request, dict) else {}
    if request.get("rule_ref") != RULE_REF:
        errors.append("RESOURCE_OCCUPANCY_REQUEST_INVALID")

    if not isinstance(snapshots, list) or any(
        not _snapshot_valid(snapshot) for snapshot in (snapshots if isinstance(snapshots, list) else [])
    ):
        errors.append("RESOURCE_OCCUPANCY_SNAPSHOT_INVALID")
        snapshots = snapshots if isinstance(snapshots, list) else []

    count = _resolution_count(request, snapshots)
    if count == 0:
        errors.append("RESOURCE_OCCUPANCY_SNAPSHOT_UNRESOLVED")
    elif count > 1:
        errors.append("RESOURCE_OCCUPANCY_SNAPSHOT_AMBIGUOUS")

    snapshot = _selected_snapshot(request, snapshots)
    if snapshot is not None:
        if snapshot.get("resource_ref") != request.get("resource_ref"):
            errors.append("RESOURCE_OCCUPANCY_BINDING_MISMATCH")
        if not _completeness_ref_valid(snapshot.get("completeness_evidence_ref")):
            errors.append("RESOURCE_OCCUPANCY_COMPLETENESS_EVIDENCE_REQUIRED")
        assignments = snapshot.get("assignments")
        if isinstance(assignments, list):
            ids = _assignment_ids(assignments)
            if any(item is None for item in ids) or any(
                not isinstance(item, dict) or not validate_assignment(item).valid
                for item in assignments
            ):
                errors.append("RESOURCE_OCCUPANCY_ASSIGNMENT_INVALID")
            if len(ids) != len(set(ids)):
                errors.append("RESOURCE_OCCUPANCY_ASSIGNMENT_DUPLICATE")
            if any(
                isinstance(item, dict)
                and item.get("resource_ref") != request.get("resource_ref")
                for item in assignments
            ):
                errors.append("RESOURCE_OCCUPANCY_BINDING_MISMATCH")

    derived = derive_resource_occupancy(dataset)
    stored_witnesses = request.get("stored_witness_assignment_refs")
    if (
        derived.occupied is not None
        and (
            request.get("stored_occupied") != derived.occupied
            or tuple(stored_witnesses or ()) != derived.witness_assignment_refs
        )
    ):
        errors.append("RESOURCE_OCCUPANCY_RESULT_MISMATCH")
    return result(errors)


def validate_resource_occupancy_fixture(fixture: Any) -> ValidationResult:
    if not isinstance(fixture, dict) or fixture.get("concept") != "ResourceOccupancyDataset":
        return result(("RESOURCE_OCCUPANCY_FIXTURE_INVALID",))
    return validate_resource_occupancy_dataset(fixture.get("dataset"))
