from __future__ import annotations

from typing import Any, Iterable

from .checker import ValidationResult


SPATIAL_ERROR_CODES = frozenset(
    {
        "OPERATION_SPATIAL_BINDING_DUPLICATE",
        "OPERATION_SPATIAL_BINDING_VERSION_REUSED",
        "OPERATION_SPATIAL_CONTEXT_INVALID",
        "OPERATION_SPATIAL_CONTEXT_VERSION_REUSED",
        "OPERATION_SPATIAL_FORBIDDEN_COUPLING",
        "OPERATION_SPATIAL_PROFILE_UNRESOLVED",
        "OPERATION_SPATIAL_SNAPSHOT_PROFILE_MISMATCH",
        "OPERATION_SPATIAL_SNAPSHOT_UNRESOLVED",
        "OPERATION_SPATIAL_TEMPORAL_CONTEXT_INVALID",
        "OPERATION_SPATIAL_TRANSITION_ID_MISMATCH",
    }
)

TEMPORAL_SCOPES = frozenset(
    {"operation-context", "planned-context", "actual-context"}
)

CONTEXT_FIELDS = frozenset({"context_version_ref", "bindings"})
BINDING_FIELDS = frozenset(
    {
        "binding_id",
        "binding_version_ref",
        "purpose_ref",
        "representation_profile_ref",
        "payload_snapshot_ref",
        "temporal_scope",
        "provenance_ref",
    }
)
PROFILE_FIELDS = frozenset({"profile_ref", "profile_owner_ref"})
SNAPSHOT_FIELDS = frozenset(
    {
        "snapshot_ref",
        "representation_profile_ref",
        "opaque_payload_ref",
        "provenance_ref",
    }
)


def _result(errors: Iterable[str]) -> ValidationResult:
    return ValidationResult(tuple(dict.fromkeys(errors)))


def _nonempty(value: Any) -> bool:
    return value is not None and bool(str(value).strip())


def _versioned_ref(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    subject, separator, version = value.strip().rpartition("@")
    return bool(separator and subject.strip() and version.strip())


def _binding_shape_valid(binding: Any) -> bool:
    if not isinstance(binding, dict) or set(binding) != BINDING_FIELDS:
        return False
    required_nonempty = (
        "binding_id",
        "provenance_ref",
    )
    required_versioned = (
        "binding_version_ref",
        "purpose_ref",
        "representation_profile_ref",
        "payload_snapshot_ref",
    )
    binding_id = str(binding.get("binding_id", "")).strip()
    binding_subject = str(binding.get("binding_version_ref", "")).strip().rpartition("@")[0]
    return (
        all(_nonempty(binding.get(field)) for field in required_nonempty)
        and all(_versioned_ref(binding.get(field)) for field in required_versioned)
        and binding_subject == binding_id
        and binding.get("temporal_scope") in TEMPORAL_SCOPES
    )


def _profile_valid(profile: Any) -> bool:
    return (
        isinstance(profile, dict)
        and set(profile) == PROFILE_FIELDS
        and _versioned_ref(profile.get("profile_ref"))
        and _nonempty(profile.get("profile_owner_ref"))
    )


def _snapshot_valid(snapshot: Any) -> bool:
    return (
        isinstance(snapshot, dict)
        and set(snapshot) == SNAPSHOT_FIELDS
        and _versioned_ref(snapshot.get("snapshot_ref"))
        and _versioned_ref(snapshot.get("representation_profile_ref"))
        and _versioned_ref(snapshot.get("opaque_payload_ref"))
        and _nonempty(snapshot.get("provenance_ref"))
    )


def _exact_candidates(entries: Any, field: str, reference: str) -> list[dict[str, Any]]:
    if not isinstance(entries, list):
        return []
    return [
        entry
        for entry in entries
        if isinstance(entry, dict) and entry.get(field) == reference
    ]


def validate_operation_spatial_context(fixture: dict[str, Any]) -> ValidationResult:
    operation = fixture.get("entity") or {}
    if "spatial_context" not in operation:
        return _result(())

    context = operation.get("spatial_context")
    if (
        not isinstance(context, dict)
        or set(context) != CONTEXT_FIELDS
        or not _versioned_ref(context.get("context_version_ref"))
        or not isinstance(context.get("bindings"), list)
    ):
        return _result(("OPERATION_SPATIAL_CONTEXT_INVALID",))

    errors: list[str] = []
    bindings = context["bindings"]
    if any(not _binding_shape_valid(binding) for binding in bindings):
        errors.append("OPERATION_SPATIAL_CONTEXT_INVALID")

    valid_bindings = [binding for binding in bindings if _binding_shape_valid(binding)]
    binding_ids = [str(binding["binding_id"]) for binding in valid_bindings]
    version_refs = [str(binding["binding_version_ref"]) for binding in valid_bindings]
    if len(binding_ids) != len(set(binding_ids)) or len(version_refs) != len(set(version_refs)):
        errors.append("OPERATION_SPATIAL_BINDING_DUPLICATE")

    references = fixture.get("references") or {}
    profiles = references.get("spatial_representation_profiles")
    snapshots = references.get("spatial_payload_snapshots")

    for binding in valid_bindings:
        profile_ref = str(binding["representation_profile_ref"])
        profile_candidates = _exact_candidates(profiles, "profile_ref", profile_ref)
        if len(profile_candidates) != 1 or not _profile_valid(profile_candidates[0]):
            errors.append("OPERATION_SPATIAL_PROFILE_UNRESOLVED")

        snapshot_ref = str(binding["payload_snapshot_ref"])
        snapshot_candidates = _exact_candidates(snapshots, "snapshot_ref", snapshot_ref)
        if len(snapshot_candidates) != 1 or not _snapshot_valid(snapshot_candidates[0]):
            errors.append("OPERATION_SPATIAL_SNAPSHOT_UNRESOLVED")
        elif snapshot_candidates[0]["representation_profile_ref"] != profile_ref:
            errors.append("OPERATION_SPATIAL_SNAPSHOT_PROFILE_MISMATCH")

        temporal_scope = binding["temporal_scope"]
        if temporal_scope == "planned-context" and not _nonempty(operation.get("planned_start")):
            errors.append("OPERATION_SPATIAL_TEMPORAL_CONTEXT_INVALID")
        if temporal_scope == "actual-context" and not _nonempty(operation.get("actual_start")):
            errors.append("OPERATION_SPATIAL_TEMPORAL_CONTEXT_INVALID")

    forbidden_fields = {
        "area_id",
        "area_ref",
        "operational_area_ref",
        "environment_ref",
        "resource_ref",
        "assignment_ref",
        "organization_ref",
        "coordination_ref",
        "conflict_ref",
        "authorization_ref",
        "readiness",
        "availability",
        "admissibility",
        "suitability",
        "selection_ref",
        "overlap",
        "visibility",
        "coordinates",
        "geometry",
    }
    if isinstance(context, dict) and any(
        isinstance(binding, dict) and forbidden_fields.intersection(binding)
        for binding in bindings
    ):
        errors.append("OPERATION_SPATIAL_FORBIDDEN_COUPLING")

    return _result(errors)


def validate_operation_spatial_transition(
    previous: dict[str, Any], current: dict[str, Any]
) -> ValidationResult:
    errors: list[str] = []
    previous_id = previous.get("operation_id")
    current_id = current.get("operation_id")
    if not _nonempty(previous_id) or previous_id != current_id:
        errors.append("OPERATION_SPATIAL_TRANSITION_ID_MISMATCH")
        return _result(errors)

    previous_context = previous.get("spatial_context")
    current_context = current.get("spatial_context")
    def normalized(context: Any) -> Any:
        if not isinstance(context, dict):
            return context
        bindings = context.get("bindings")
        if not isinstance(bindings, list):
            return context
        normalized_bindings = tuple(
            sorted(
                (tuple(sorted(item.items())) for item in bindings if isinstance(item, dict)),
                key=repr,
            )
        )
        return (context.get("context_version_ref"), normalized_bindings)

    if normalized(previous_context) == normalized(current_context):
        return _result(errors)
    if not isinstance(previous_context, dict) or not isinstance(current_context, dict):
        return _result(errors)

    if previous_context.get("context_version_ref") == current_context.get("context_version_ref"):
        errors.append("OPERATION_SPATIAL_CONTEXT_VERSION_REUSED")

    previous_bindings = {
        str(item.get("binding_id")): item
        for item in previous_context.get("bindings", [])
        if isinstance(item, dict) and _nonempty(item.get("binding_id"))
    }
    current_bindings = {
        str(item.get("binding_id")): item
        for item in current_context.get("bindings", [])
        if isinstance(item, dict) and _nonempty(item.get("binding_id"))
    }
    for binding_id in sorted(previous_bindings.keys() & current_bindings.keys()):
        before = previous_bindings[binding_id]
        after = current_bindings[binding_id]
        if before != after and before.get("binding_version_ref") == after.get("binding_version_ref"):
            errors.append("OPERATION_SPATIAL_BINDING_VERSION_REUSED")
            break

    return _result(errors)


def validate_operation_spatial_transition_fixture(
    fixture: dict[str, Any],
) -> ValidationResult:
    previous = fixture.get("previous") or {}
    current = fixture.get("current") or {}
    references = fixture.get("references")
    errors: list[str] = []
    for entity in (previous, current):
        candidate: dict[str, Any] = {"entity": entity}
        if references is not None:
            candidate["references"] = references
        errors.extend(validate_operation_spatial_context(candidate).errors)
    errors.extend(validate_operation_spatial_transition(previous, current).errors)
    return _result(errors)
