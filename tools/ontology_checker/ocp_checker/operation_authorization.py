from __future__ import annotations

from collections import defaultdict
from typing import Any, Iterable

from ._common import nonempty, parse_time, result
from .capability import validate_capability_registry
from .checker import ValidationResult
from .organization import validate_organization


OPERATION_AUTHORIZATION_ERROR_CODES = frozenset(
    {
        "OPERATION_AUTHORIZATION_FIXTURE_INVALID",
        "OPERATION_AUTHORIZATION_SOURCE_PROFILE_INVALID",
        "OPERATION_AUTHORIZATION_SOURCE_UNRESOLVED",
        "OPERATION_AUTHORIZATION_DECISION_INVALID",
        "OPERATION_AUTHORIZATION_DECISION_DUPLICATE",
        "OPERATION_AUTHORIZATION_REFERENCE_UNRESOLVED",
        "OPERATION_AUTHORIZATION_LEVEL_INVALID",
        "OPERATION_AUTHORIZATION_ELIGIBILITY_INVALID",
        "OPERATION_AUTHORIZATION_SUPERSESSION_INVALID",
        "OPERATION_AUTHORIZATION_CONFLICTING_HEADS",
        "OPERATION_AUTHORIZATION_EVIDENCE_BINDING_INVALID",
        "OPERATION_AUTHORIZATION_FORBIDDEN_COUPLING",
    }
)

OPERATION_AUTHORIZATION_DERIVATION_RULES = frozenset(
    {"derive_operation_authorization_result"}
)

SOURCE_PROFILE_KIND = "operation-authorization-source-profile@1"
DECISION_KIND = "operation-authorization-decision@1"
FRESHNESS_RULE_REF = "operation-authorization-effective@1"
DECISIONS = frozenset({"authorize", "deny"})
ELIGIBILITY_RESULTS = frozenset({"eligible", "ineligible", "indeterminate"})
DERIVED_RESULTS = frozenset({"accepted", "denied", "indeterminate"})
FORBIDDEN_COUPLING_FIELDS = frozenset(
    {
        "authority_concept_ref",
        "approval_concept_ref",
        "policy_concept_ref",
        "order_required",
        "authorization_granted",
        "lifecycle_stage",
        "assignment_mutation",
        "readiness",
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


def _capability_key(value: Any) -> tuple[str, str, str] | None:
    if not isinstance(value, dict):
        return None
    parts = tuple(_text(value.get(field)) for field in ("namespace", "capability_id", "version"))
    if any(part is None for part in parts):
        return None
    return parts  # type: ignore[return-value]


def _forbidden(value: Any) -> bool:
    if isinstance(value, dict):
        return any(
            (key in FORBIDDEN_COUPLING_FIELDS and item not in (None, False, "", [], {}))
            or _forbidden(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_forbidden(item) for item in value)
    return False


def _snapshot_forbidden(snapshot: dict[str, Any]) -> bool:
    if any(
        key in snapshot and snapshot.get(key) not in (None, False, "", [], {})
        for key in FORBIDDEN_COUPLING_FIELDS
    ):
        return True
    return any(
        _forbidden(value)
        for field in ("source_profiles", "decisions", "authorization_evidence_binding")
        for value in ([snapshot.get(field)] if field == "authorization_evidence_binding" else snapshot.get(field) or [])
    )


def _exact_matches(records: Iterable[dict[str, Any]], field: str, reference: Any) -> list[dict[str, Any]]:
    normalized = _text(reference)
    return [record for record in records if _text(record.get(field)) == normalized]


def _capability_matches(capabilities: Iterable[dict[str, Any]], reference: Any) -> list[dict[str, Any]]:
    key = _capability_key(reference)
    return [item for item in capabilities if _capability_key(item) == key] if key else []


def _organization_valid(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    try:
        return validate_organization(value).valid
    except (AttributeError, TypeError, ValueError):
        return False


def _capability_registry_valid(values: Any) -> bool:
    if not isinstance(values, list):
        return False
    try:
        return validate_capability_registry(values).valid
    except (AttributeError, TypeError, ValueError):
        return False


def _interval_valid(record: dict[str, Any]) -> bool:
    start = parse_time(record.get("effective_from"))
    end = parse_time(record.get("effective_until"))
    return start is not None and end is not None and start < end


def _effective(record: dict[str, Any], at: Any) -> bool:
    moment = parse_time(at)
    start = parse_time(record.get("effective_from"))
    end = parse_time(record.get("effective_until"))
    return bool(moment is not None and start is not None and end is not None and start <= moment < end)


def _source_profile_valid(
    profile: dict[str, Any], organizations: list[dict[str, Any]], capabilities: list[dict[str, Any]]
) -> bool:
    levels = profile.get("decision_levels")
    if (
        profile.get("profile_kind_ref") != SOURCE_PROFILE_KIND
        or _versioned_ref(profile.get("source_contract_ref")) is None
        or _text(profile.get("source_owner_ref")) is None
        or _versioned_ref(profile.get("level_rule_ref")) is None
        or profile.get("freshness_rule_ref") != FRESHNESS_RULE_REF
        or not isinstance(levels, list)
        or not levels
        or _forbidden(profile)
    ):
        return False
    if len(_exact_matches(organizations, "organization_id", profile.get("source_owner_ref"))) != 1:
        return False
    level_refs: list[str] = []
    for level in levels:
        if not isinstance(level, dict):
            return False
        level_ref = _versioned_ref(level.get("decision_level_ref"))
        if level_ref is None or len(_capability_matches(capabilities, level.get("required_capability_ref"))) != 1:
            return False
        level_refs.append(level_ref)
    return len(level_refs) == len(set(level_refs))


def _selected_level(profile: dict[str, Any], decision_level_ref: Any) -> dict[str, Any] | None:
    matches = _exact_matches(profile.get("decision_levels") or [], "decision_level_ref", decision_level_ref)
    return matches[0] if len(matches) == 1 else None


def _level_binding_valid(decision: dict[str, Any], profile: dict[str, Any]) -> bool:
    binding = decision.get("level_binding")
    level = _selected_level(profile, decision.get("decision_level_ref"))
    return bool(
        isinstance(binding, dict)
        and level is not None
        and binding.get("rule_ref") == profile.get("level_rule_ref")
        and _text(binding.get("input_snapshot_ref")) == _text(decision.get("input_snapshot_ref"))
        and _text(binding.get("result_level_ref")) == _text(decision.get("decision_level_ref"))
        and binding.get("result") == "resolved"
        and _text(binding.get("evidence_ref")) is not None
        and _text(binding.get("provenance_ref")) is not None
        and _capability_key(decision.get("authorizer_capability_ref"))
        == _capability_key(level.get("required_capability_ref"))
    )


def _eligibility_binding_valid(decision: dict[str, Any]) -> bool:
    binding = decision.get("eligibility_binding")
    return bool(
        isinstance(binding, dict)
        and _text(binding.get("authorizer_organization_ref"))
        == _text(decision.get("authorizer_organization_ref"))
        and _capability_key(binding.get("capability_ref"))
        == _capability_key(decision.get("authorizer_capability_ref"))
        and _text(binding.get("input_snapshot_ref")) == _text(decision.get("input_snapshot_ref"))
        and binding.get("result") in ELIGIBILITY_RESULTS
        and _text(binding.get("evidence_ref")) is not None
        and _text(binding.get("provenance_ref")) is not None
    )


def _decision_identity_valid(decision: dict[str, Any]) -> bool:
    return bool(
        decision.get("record_kind") == DECISION_KIND
        and all(
            _text(decision.get(field)) is not None
            for field in (
                "decision_id",
                "source_owner_ref",
                "subject_operation_ref",
                "authorizer_organization_ref",
                "input_snapshot_ref",
                "provenance_ref",
            )
        )
        and _versioned_ref(decision.get("source_contract_ref")) is not None
        and _versioned_ref(decision.get("decision_level_ref")) is not None
        and _capability_key(decision.get("authorizer_capability_ref")) is not None
        and decision.get("decision") in DECISIONS
        and _interval_valid(decision)
        and parse_time(decision.get("recorded_at")) is not None
        and not _forbidden(decision)
    )


def _decision_contract_valid(
    decision: dict[str, Any],
    profiles: list[dict[str, Any]],
    operations: list[dict[str, Any]],
    organizations: list[dict[str, Any]],
    capabilities: list[dict[str, Any]],
) -> bool:
    if not _decision_identity_valid(decision):
        return False
    profile_matches = _exact_matches(profiles, "source_contract_ref", decision.get("source_contract_ref"))
    if len(profile_matches) != 1:
        return False
    profile = profile_matches[0]
    return bool(
        _text(decision.get("source_owner_ref")) == _text(profile.get("source_owner_ref"))
        and len(_exact_matches(operations, "operation_id", decision.get("subject_operation_ref"))) == 1
        and len(_exact_matches(organizations, "organization_id", decision.get("authorizer_organization_ref"))) == 1
        and len(_capability_matches(capabilities, decision.get("authorizer_capability_ref"))) == 1
        and _level_binding_valid(decision, profile)
        and _eligibility_binding_valid(decision)
    )


def _lineage_errors(decisions: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    index = {_text(item.get("decision_id")): item for item in decisions}
    successors: dict[str, int] = defaultdict(int)
    identity_fields = ("source_contract_ref", "source_owner_ref", "subject_operation_ref")
    for decision in decisions:
        decision_id = _text(decision.get("decision_id"))
        predecessor_id = _text(decision.get("supersedes_decision_ref"))
        if predecessor_id is None:
            continue
        predecessor = index.get(predecessor_id)
        if (
            decision_id is None
            or predecessor is None
            or decision_id == predecessor_id
            or any(_text(decision.get(field)) != _text(predecessor.get(field)) for field in identity_fields)
        ):
            errors.append("OPERATION_AUTHORIZATION_SUPERSESSION_INVALID")
            continue
        successors[predecessor_id] += 1
    if any(count > 1 for count in successors.values()):
        errors.extend(
            [
                "OPERATION_AUTHORIZATION_SUPERSESSION_INVALID",
                "OPERATION_AUTHORIZATION_CONFLICTING_HEADS",
            ]
        )
    for decision in decisions:
        seen: set[str] = set()
        current = _text(decision.get("decision_id"))
        while current is not None and current in index:
            if current in seen:
                errors.append("OPERATION_AUTHORIZATION_SUPERSESSION_INVALID")
                break
            seen.add(current)
            current = _text(index[current].get("supersedes_decision_ref"))
    return errors


def _binding_key(decision: dict[str, Any]) -> tuple[str | None, ...]:
    return tuple(
        _text(decision.get(field))
        for field in ("source_contract_ref", "source_owner_ref", "subject_operation_ref")
    )


def _heads(decisions: list[dict[str, Any]], at: Any) -> list[dict[str, Any]]:
    effective = [decision for decision in decisions if _effective(decision, at)]
    superseded = {
        _text(decision.get("supersedes_decision_ref"))
        for decision in effective
        if _text(decision.get("supersedes_decision_ref")) is not None
    }
    return [decision for decision in effective if _text(decision.get("decision_id")) not in superseded]


def derive_operation_authorization_result(snapshot: dict[str, Any]) -> str:
    """Derive accepted/denied/indeterminate for one exact OCP-017 evidence binding."""
    if not isinstance(snapshot, dict) or _snapshot_forbidden(snapshot):
        return "indeterminate"
    binding = snapshot.get("authorization_evidence_binding")
    profiles = snapshot.get("source_profiles")
    decisions = snapshot.get("decisions")
    organizations = snapshot.get("organizations")
    capabilities = snapshot.get("capabilities")
    operations = snapshot.get("operations")
    if not all(isinstance(value, list) for value in (profiles, decisions, organizations, capabilities, operations)):
        return "indeterminate"
    if (
        any(not _organization_valid(organization) for organization in organizations)
        or not _capability_registry_valid(capabilities)
        or any(
            not isinstance(profile, dict) or not _source_profile_valid(profile, organizations, capabilities)
            for profile in profiles
        )
        or len({_text(profile.get("source_contract_ref")) for profile in profiles}) != len(profiles)
        or any(not isinstance(item, dict) for item in decisions)
    ):
        return "indeterminate"
    typed_decisions = [item for item in decisions if isinstance(item, dict)]
    if (
        len({_text(item.get("decision_id")) for item in typed_decisions}) != len(typed_decisions)
        or any(
            not _decision_contract_valid(item, profiles, operations, organizations, capabilities)
            for item in typed_decisions
        )
        or _lineage_errors(typed_decisions)
    ):
        return "indeterminate"
    if not isinstance(binding, dict) or _text(binding.get("evidence_ref")) is None:
        return "indeterminate"
    decision_matches = _exact_matches(decisions, "decision_id", binding.get("evidence_ref"))
    if len(decision_matches) != 1:
        return "indeterminate"
    decision = decision_matches[0]
    if (
        any(
            _text(binding.get(field)) != _text(decision.get(field))
            for field in (
                "source_contract_ref",
                "source_owner_ref",
                "subject_operation_ref",
                "input_snapshot_ref",
            )
        )
        or binding.get("input_state") != "effective"
        or _text(binding.get("provenance_ref")) is None
    ):
        return "indeterminate"
    profile_matches = _exact_matches(profiles, "source_contract_ref", decision.get("source_contract_ref"))
    if len(profile_matches) != 1:
        return "indeterminate"
    profile = profile_matches[0]
    same_binding = [item for item in decisions if isinstance(item, dict) and _binding_key(item) == _binding_key(decision)]
    heads = _heads(same_binding, snapshot.get("evaluation_time"))
    if len(heads) != 1 or _text(heads[0].get("decision_id")) != _text(decision.get("decision_id")):
        return "indeterminate"
    if decision["eligibility_binding"].get("result") != "eligible":
        return "indeterminate"
    return "accepted" if decision.get("decision") == "authorize" else "denied"


def validate_operation_authorization_dataset(snapshot: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    profiles = snapshot.get("source_profiles")
    decisions = snapshot.get("decisions")
    organizations = snapshot.get("organizations")
    capabilities = snapshot.get("capabilities")
    operations = snapshot.get("operations")
    if not all(isinstance(value, list) for value in (profiles, decisions, organizations, capabilities, operations)):
        return result(["OPERATION_AUTHORIZATION_FIXTURE_INVALID"])
    if _snapshot_forbidden(snapshot):
        errors.append("OPERATION_AUTHORIZATION_FORBIDDEN_COUPLING")
    if any(not _organization_valid(organization) for organization in organizations) or not _capability_registry_valid(capabilities):
        errors.append("OPERATION_AUTHORIZATION_REFERENCE_UNRESOLVED")

    for profile in profiles:
        if not isinstance(profile, dict) or not _source_profile_valid(profile, organizations, capabilities):
            errors.append("OPERATION_AUTHORIZATION_SOURCE_PROFILE_INVALID")
    profile_refs = [_text(item.get("source_contract_ref")) for item in profiles if isinstance(item, dict)]
    if len(profile_refs) != len(set(profile_refs)):
        errors.append("OPERATION_AUTHORIZATION_SOURCE_UNRESOLVED")

    valid_decisions = [item for item in decisions if isinstance(item, dict)]
    for decision in decisions:
        if not isinstance(decision, dict) or not _decision_identity_valid(decision):
            errors.append("OPERATION_AUTHORIZATION_DECISION_INVALID")
            continue
        profile_matches = _exact_matches(profiles, "source_contract_ref", decision.get("source_contract_ref"))
        if len(profile_matches) != 1:
            errors.append("OPERATION_AUTHORIZATION_SOURCE_UNRESOLVED")
            continue
        profile = profile_matches[0]
        if _text(decision.get("source_owner_ref")) != _text(profile.get("source_owner_ref")):
            errors.append("OPERATION_AUTHORIZATION_SOURCE_UNRESOLVED")
        if (
            len(_exact_matches(operations, "operation_id", decision.get("subject_operation_ref"))) != 1
            or len(_exact_matches(organizations, "organization_id", decision.get("authorizer_organization_ref"))) != 1
            or len(_capability_matches(capabilities, decision.get("authorizer_capability_ref"))) != 1
        ):
            errors.append("OPERATION_AUTHORIZATION_REFERENCE_UNRESOLVED")
        if not _level_binding_valid(decision, profile):
            errors.append("OPERATION_AUTHORIZATION_LEVEL_INVALID")
        if not _eligibility_binding_valid(decision):
            errors.append("OPERATION_AUTHORIZATION_ELIGIBILITY_INVALID")
        if _forbidden(decision):
            errors.append("OPERATION_AUTHORIZATION_FORBIDDEN_COUPLING")

    decision_ids = [_text(item.get("decision_id")) for item in valid_decisions]
    if len(decision_ids) != len(set(decision_ids)):
        errors.append("OPERATION_AUTHORIZATION_DECISION_DUPLICATE")
    errors.extend(_lineage_errors(valid_decisions))

    binding = snapshot.get("authorization_evidence_binding")
    derived = derive_operation_authorization_result(snapshot)
    if (
        not isinstance(binding, dict)
        or derived not in DERIVED_RESULTS
        or derived != "accepted"
        or any(
            _text(binding.get(field)) is None
            for field in (
                "source_contract_ref",
                "source_owner_ref",
                "evidence_ref",
                "subject_operation_ref",
                "input_snapshot_ref",
                "provenance_ref",
            )
        )
        or binding.get("input_state") != "effective"
        or binding.get("result") != "accepted"
    ):
        errors.append("OPERATION_AUTHORIZATION_EVIDENCE_BINDING_INVALID")
    elif isinstance(binding, dict):
        matches = _exact_matches(valid_decisions, "decision_id", binding.get("evidence_ref"))
        if len(matches) != 1:
            errors.append("OPERATION_AUTHORIZATION_EVIDENCE_BINDING_INVALID")
        else:
            decision = matches[0]
            for field in ("source_contract_ref", "source_owner_ref", "subject_operation_ref", "input_snapshot_ref"):
                if _text(binding.get(field)) != _text(decision.get(field)):
                    errors.append("OPERATION_AUTHORIZATION_EVIDENCE_BINDING_INVALID")
                    break
    return result(errors)


def validate_operation_authorization_fixture(fixture: dict[str, Any]) -> ValidationResult:
    snapshot = fixture.get("snapshot")
    if not isinstance(snapshot, dict):
        return result(["OPERATION_AUTHORIZATION_FIXTURE_INVALID"])
    return validate_operation_authorization_dataset(snapshot)
