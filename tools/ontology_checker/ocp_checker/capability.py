from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .checker import ValidationResult


CAPABILITY_ERROR_CODES = frozenset(
    {
        "CAPABILITY_DEFINITION_REQUIRED",
        "CAPABILITY_HOLDER_COUPLING_FORBIDDEN",
        "CAPABILITY_ID_REQUIRED",
        "CAPABILITY_IDENTITY_DUPLICATE",
        "CAPABILITY_LABEL_REQUIRED",
        "CAPABILITY_NAMESPACE_OWNER_CONFLICT",
        "CAPABILITY_NAMESPACE_OWNER_REQUIRED",
        "CAPABILITY_NAMESPACE_REQUIRED",
        "CAPABILITY_PROVENANCE_REF_REQUIRED",
        "CAPABILITY_PUBLISHED_AT_REQUIRED",
        "CAPABILITY_REFERENCE_AMBIGUOUS",
        "CAPABILITY_REFERENCE_INVALID",
        "CAPABILITY_REFERENCE_UNRESOLVED",
        "CAPABILITY_SELF_SUPERSESSION",
        "CAPABILITY_SUPERSESSION_CYCLE",
        "CAPABILITY_SUPERSESSION_IDENTITY_MISMATCH",
        "CAPABILITY_SUPERSESSION_REFERENCE_INVALID",
        "CAPABILITY_SUPERSESSION_TARGET_UNRESOLVED",
        "CAPABILITY_VERSION_REQUIRED",
    }
)

CAPABILITY_DERIVATION_RULES = frozenset({"resolve_capability_definition"})

FORBIDDEN_HOLDER_KEYS = frozenset(
    {
        "holder_ref",
        "holder_refs",
        "resource_ref",
        "resource_refs",
        "organization_ref",
        "organization_refs",
        "assignment_ref",
        "assignment_refs",
        "claim",
        "claims",
        "possessed_by",
        "granted_to",
        "readiness",
        "availability",
        "authorization",
        "admissibility",
    }
)


def _result(errors: Iterable[str]) -> ValidationResult:
    return ValidationResult(tuple(dict.fromkeys(errors)))


def _nonempty(value: Any) -> bool:
    return value is not None and bool(str(value).strip())


def _has_alnum(value: Any) -> bool:
    return isinstance(value, str) and any(char.isalnum() for char in value)


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


def _reference_key(reference: Any) -> tuple[str, str, str] | None:
    if not isinstance(reference, dict):
        return None
    namespace = reference.get("namespace")
    capability_id = reference.get("capability_id")
    version = reference.get("version")
    if not all(_nonempty(value) for value in (namespace, capability_id, version)):
        return None
    return (
        str(namespace).strip(),
        str(capability_id).strip(),
        str(version).strip(),
    )


def _entry_key(entry: Any) -> tuple[str, str, str] | None:
    return _reference_key(entry)


def validate_capability(capability: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []

    if not _nonempty(capability.get("namespace")):
        errors.append("CAPABILITY_NAMESPACE_REQUIRED")
    if not _nonempty(capability.get("capability_id")):
        errors.append("CAPABILITY_ID_REQUIRED")
    if not _nonempty(capability.get("version")):
        errors.append("CAPABILITY_VERSION_REQUIRED")
    if not _nonempty(capability.get("label")):
        errors.append("CAPABILITY_LABEL_REQUIRED")
    if not _has_alnum(capability.get("definition")):
        errors.append("CAPABILITY_DEFINITION_REQUIRED")
    if not _nonempty(capability.get("namespace_owner_ref")):
        errors.append("CAPABILITY_NAMESPACE_OWNER_REQUIRED")
    if _parse_time(capability.get("published_at")) is None:
        errors.append("CAPABILITY_PUBLISHED_AT_REQUIRED")
    if not _nonempty(capability.get("provenance_ref")):
        errors.append("CAPABILITY_PROVENANCE_REF_REQUIRED")

    if any(
        key in capability and capability.get(key) not in (None, [], {}, "")
        for key in FORBIDDEN_HOLDER_KEYS
    ):
        errors.append("CAPABILITY_HOLDER_COUPLING_FORBIDDEN")

    supersedes = capability.get("supersedes_capability_ref")
    if supersedes is not None:
        target = _reference_key(supersedes)
        current = _entry_key(capability)
        if target is None:
            errors.append("CAPABILITY_SUPERSESSION_REFERENCE_INVALID")
        elif current is not None:
            if target == current:
                errors.append("CAPABILITY_SELF_SUPERSESSION")
            elif target[:2] != current[:2]:
                errors.append("CAPABILITY_SUPERSESSION_IDENTITY_MISMATCH")

    return _result(errors)


def _has_cycle(graph: dict[tuple[str, str, str], tuple[str, str, str]]) -> bool:
    visiting: set[tuple[str, str, str]] = set()
    visited: set[tuple[str, str, str]] = set()

    def visit(node: tuple[str, str, str]) -> bool:
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


def validate_capability_registry(
    capabilities: Iterable[dict[str, Any]],
) -> ValidationResult:
    errors: list[str] = []
    entries = list(capabilities)
    index: dict[tuple[str, str, str], list[dict[str, Any]]] = {}
    namespace_owners: dict[str, str] = {}
    graph: dict[tuple[str, str, str], tuple[str, str, str]] = {}

    for capability in entries:
        if not isinstance(capability, dict):
            errors.append("CAPABILITY_REFERENCE_INVALID")
            continue

        errors.extend(validate_capability(capability).errors)
        key = _entry_key(capability)
        if key is None:
            continue

        index.setdefault(key, []).append(capability)

        namespace = key[0]
        owner = capability.get("namespace_owner_ref")
        if _nonempty(owner):
            normalized_owner = str(owner).strip()
            existing = namespace_owners.get(namespace)
            if existing is None:
                namespace_owners[namespace] = normalized_owner
            elif existing != normalized_owner:
                errors.append("CAPABILITY_NAMESPACE_OWNER_CONFLICT")

        supersedes = capability.get("supersedes_capability_ref")
        target = _reference_key(supersedes) if supersedes is not None else None
        if target is not None and target != key and target[:2] == key[:2]:
            graph[key] = target

    if any(len(candidates) > 1 for candidates in index.values()):
        errors.append("CAPABILITY_IDENTITY_DUPLICATE")

    for target in graph.values():
        if target not in index:
            errors.append("CAPABILITY_SUPERSESSION_TARGET_UNRESOLVED")

    if _has_cycle(graph):
        errors.append("CAPABILITY_SUPERSESSION_CYCLE")

    return _result(errors)


def resolve_capability_definition(
    capabilities: Iterable[dict[str, Any]],
    reference: dict[str, Any],
) -> dict[str, Any] | None:
    key = _reference_key(reference)
    if key is None:
        return None

    candidates = [
        capability
        for capability in capabilities
        if isinstance(capability, dict) and _entry_key(capability) == key
    ]
    if len(candidates) != 1:
        return None
    candidate = candidates[0]
    if not validate_capability(candidate).valid:
        return None
    return candidate


def validate_capability_reference_fixture(
    fixture: dict[str, Any],
) -> ValidationResult:
    errors: list[str] = []
    entries = fixture.get("entries")
    if entries is None:
        entries = fixture.get("entities")
    if not isinstance(entries, list):
        entries = []
        errors.append("CAPABILITY_REFERENCE_INVALID")

    errors.extend(validate_capability_registry(entries).errors)

    reference = fixture.get("reference")
    key = _reference_key(reference)
    if key is None:
        errors.append("CAPABILITY_REFERENCE_INVALID")
        return _result(errors)

    candidates = [
        capability
        for capability in entries
        if isinstance(capability, dict) and _entry_key(capability) == key
    ]
    if not candidates:
        errors.append("CAPABILITY_REFERENCE_UNRESOLVED")
    elif len(candidates) > 1:
        errors.append("CAPABILITY_REFERENCE_AMBIGUOUS")
    elif not validate_capability(candidates[0]).valid:
        errors.append("CAPABILITY_REFERENCE_UNRESOLVED")

    return _result(errors)
