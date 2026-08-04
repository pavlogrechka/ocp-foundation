from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable

from .capability import resolve_capability_definition
from .checker import ValidationResult, validate_resource


CAPABILITY_CLAIM_ERROR_CODES = frozenset(
    {
        "CAPABILITY_CLAIM_ASSERTION_INVALID",
        "CAPABILITY_CLAIM_BINDING_MISMATCH",
        "CAPABILITY_CLAIM_CAPABILITY_REF_INVALID",
        "CAPABILITY_CLAIM_CAPABILITY_UNRESOLVED",
        "CAPABILITY_CLAIM_CLAIMANT_REQUIRED",
        "CAPABILITY_CLAIM_CONDITION_SET_REF_REQUIRED",
        "CAPABILITY_CLAIM_EVIDENCE_BINDINGS_INVALID",
        "CAPABILITY_CLAIM_EVIDENCE_KIND_UNSUPPORTED",
        "CAPABILITY_CLAIM_EVIDENCE_REFERENCE_UNRESOLVED",
        "CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_MISMATCH",
        "CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_REQUIRED",
        "CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_UNRESOLVED",
        "CAPABILITY_CLAIM_FORBIDDEN_COUPLING",
        "CAPABILITY_CLAIM_HOLDER_KIND_UNSUPPORTED",
        "CAPABILITY_CLAIM_HOLDER_REF_REQUIRED",
        "CAPABILITY_CLAIM_HOLDER_UNRESOLVED",
        "CAPABILITY_CLAIM_ID_REQUIRED",
        "CAPABILITY_CLAIM_IDENTITY_DUPLICATE",
        "CAPABILITY_CLAIM_INTERVAL_INVALID",
        "CAPABILITY_CLAIM_KIND_UNSUPPORTED",
        "CAPABILITY_CLAIM_PROVENANCE_REF_REQUIRED",
        "CAPABILITY_CLAIM_RECORDED_AT_REQUIRED",
        "CAPABILITY_CLAIM_SELF_SUPERSESSION",
        "CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH",
        "CAPABILITY_CLAIM_SUPPORT_STATE_INVALID",
        "CAPABILITY_CLAIM_SUPERSESSION_CYCLE",
        "CAPABILITY_CLAIM_SUPERSESSION_TARGET_UNRESOLVED",
        "CAPABILITY_CLAIM_AUTHORITY_REF_REQUIRED",
        "CAPABILITY_CLAIM_EFFECTIVE_FROM_REQUIRED",
        "CAPABILITY_CLAIM_WITHDRAWAL_TARGET_REQUIRED",
    }
)

CAPABILITY_CLAIM_DERIVATION_RULES = frozenset(
    {
        "capability_claim_effective_at",
        "capability_claim_heads",
        "effective_capability_claim",
        "resolve_capability_claim",
    }
)

SUPPORTED_CLAIM_KINDS = frozenset({"holder-capability@1"})
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

    if _normalized_ref(claim.get("claim_kind_ref")) not in SUPPORTED_CLAIM_KINDS:
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

    bindings = _normalized_bindings(claim.get("evidence_bindings"))
    if bindings is None:
        errors.append("CAPABILITY_CLAIM_EVIDENCE_BINDINGS_INVALID")
    elif any(kind_ref not in SUPPORTED_EVIDENCE_KINDS for kind_ref, _ in bindings):
        errors.append("CAPABILITY_CLAIM_EVIDENCE_KIND_UNSUPPORTED")
    elif not bindings:
        if support_state not in {"declared", "missing"}:
            errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")
        if _normalized_ref(claim.get("evidence_snapshot_ref")) is not None:
            errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")
    else:
        if support_state in {"declared", "missing"}:
            errors.append("CAPABILITY_CLAIM_SUPPORT_STATE_MISMATCH")
        if _normalized_ref(claim.get("evidence_snapshot_ref")) is None:
            errors.append("CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_REQUIRED")

    if _normalized_ref(claim.get("authority_ref")) is None:
        errors.append("CAPABILITY_CLAIM_AUTHORITY_REF_REQUIRED")
    if _normalized_ref(claim.get("provenance_ref")) is None:
        errors.append("CAPABILITY_CLAIM_PROVENANCE_REF_REQUIRED")
    if _parse_time(claim.get("recorded_at")) is None:
        errors.append("CAPABILITY_CLAIM_RECORDED_AT_REQUIRED")

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
    if assertion == "withdrawn" and (
        support_state != "declared" or bindings not in ((), None)
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

    evidence_indexes = _evidence_indexes(
        events=events, observations=observations, assessments=assessments
    )
    snapshots = _snapshot_index(evidence_snapshots)
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

        bindings = _normalized_bindings(claim.get("evidence_bindings"))
        if bindings is not None:
            for kind_ref, evidence_ref in bindings:
                if kind_ref in evidence_indexes and evidence_ref not in evidence_indexes[kind_ref]:
                    errors.append("CAPABILITY_CLAIM_EVIDENCE_REFERENCE_UNRESOLVED")

        snapshot_ref = _normalized_ref(claim.get("evidence_snapshot_ref"))
        if bindings and snapshot_ref is not None:
            snapshot_bindings = snapshots.get(snapshot_ref)
            if snapshot_bindings is None:
                errors.append("CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_UNRESOLVED")
            elif snapshot_bindings != bindings:
                errors.append("CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_MISMATCH")

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
        elif len(sources) == 1 and _binding_identity(sources[0]) != _binding_identity(targets[0]):
            errors.append("CAPABILITY_CLAIM_BINDING_MISMATCH")

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
) -> str:
    heads = capability_claim_heads(
        claims,
        holder_ref=holder_ref,
        capability_ref=capability_ref,
        claimant_ref=claimant_ref,
        claim_kind_ref=claim_kind_ref,
        condition_set_ref=condition_set_ref,
        at=at,
    )
    if not heads:
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
    )
