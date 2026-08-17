from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ._common import nonempty, parse_time, result
from .checker import ValidationResult


COMPLETENESS_EVALUATOR_ERROR_CODES = frozenset(
    {
        "COMPLETENESS_EVALUATOR_FIXTURE_INVALID",
        "COMPLETENESS_EVALUATOR_REQUEST_INVALID",
        "COMPLETENESS_EVALUATOR_PROFILE_INVALID",
        "COMPLETENESS_EVALUATOR_EVIDENCE_INVALID",
        "COMPLETENESS_EVALUATOR_REFERENCE_UNRESOLVED",
        "COMPLETENESS_EVALUATOR_REFERENCE_AMBIGUOUS",
        "COMPLETENESS_EVALUATOR_SUBJECT_MISMATCH",
        "COMPLETENESS_EVALUATOR_SCOPE_MISMATCH",
        "COMPLETENESS_EVALUATOR_TIME_INVALID",
        "COMPLETENESS_EVALUATOR_AUTHORITY_UNRESOLVED",
        "COMPLETENESS_EVALUATOR_EVIDENCE_CONFLICT",
        "COMPLETENESS_EVALUATOR_ACTIVATION_FORBIDDEN",
        "COMPLETENESS_EVALUATOR_FORBIDDEN_COUPLING",
        "COMPLETENESS_EVALUATOR_RESULT_MISMATCH",
    }
)
COMPLETENESS_EVALUATOR_DERIVATION_RULES = frozenset(
    {"derive_completeness_evidence_recognition"}
)

RULE_REF = "assignment-set-completeness-recognition@0.1.0"
DOMAIN_REF = "resource-occupancy"
SUBJECT_KIND = "resource-assignment-set-completeness"
COVERAGE_KIND = "all-assignments-for-resource-at-time"
POSITIVE_CLAIM = "assignment_set_complete_for_resource"
REFERENCE_RESULT = "synthetic-reference-recognized"
INDETERMINATE = "indeterminate"
SYNTHETIC_EVALUATOR_PREFIX = "SYNTH-EVALUATOR-"
SYNTHETIC_AUTHORITY_PREFIX = "SYNTH-AUTHORITY-"

DATASET_FIELDS = frozenset(
    {"recognition_request", "evaluator_profiles", "completeness_evidence"}
)
REQUEST_FIELDS = frozenset(
    {
        "request_id", "rule_ref", "resource_ref", "evaluation_time",
        "assignment_snapshot_ref", "evaluator_profile_ref",
        "completeness_evidence_ref", "stored_result",
    }
)
PROFILE_FIELDS = frozenset(
    {
        "evaluator_profile_ref", "evaluator_ref", "domain_ref", "subject_kind",
        "authority_basis_ref", "valid_from", "valid_until",
    }
)
EVIDENCE_FIELDS = frozenset(
    {
        "completeness_evidence_ref", "evaluator_profile_ref", "resource_ref",
        "evaluation_time", "assignment_snapshot_ref", "produced_at",
        "coverage_kind", "claim",
    }
)
ACTIVATION_FIELDS = frozenset(
    {"activation_state", "activation_baseline_ref", "production_context_ref"}
)
FORBIDDEN_FIELDS = frozenset(
    {
        "occupied", "conflict", "priority", "capacity", "reservation", "allocation",
        "permission", "authorization", "assignment_lifecycle_transition",
        "action_recommendation",
    }
)


@dataclass(frozen=True)
class CompletenessEvidenceRecognition:
    result: str
    evaluator_ref: str | None
    authority_basis_ref: str | None


INDETERMINATE_RESULT = CompletenessEvidenceRecognition(INDETERMINATE, None, None)


def _text(value: Any) -> str | None:
    return str(value).strip() if nonempty(value) else None


def _has_prefix(value: Any, prefix: str) -> bool:
    normalized = _text(value)
    return bool(normalized and normalized.startswith(prefix))


def _contains_named(value: Any, names: frozenset[str]) -> bool:
    if isinstance(value, dict):
        return any(
            key in names or _contains_named(item, names)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_named(item, names) for item in value)
    return False


def _request_valid(value: Any) -> bool:
    return bool(
        isinstance(value, dict)
        and set(value) == REQUEST_FIELDS
        and all(_text(value.get(field)) for field in REQUEST_FIELDS)
        and value.get("stored_result") in {REFERENCE_RESULT, INDETERMINATE}
        and parse_time(value.get("evaluation_time")) is not None
    )


def _profile_valid(value: Any) -> bool:
    return bool(
        isinstance(value, dict)
        and set(value) == PROFILE_FIELDS
        and all(_text(value.get(field)) for field in PROFILE_FIELDS)
        and parse_time(value.get("valid_from")) is not None
        and parse_time(value.get("valid_until")) is not None
    )


def _evidence_valid(value: Any) -> bool:
    return bool(
        isinstance(value, dict)
        and set(value) == EVIDENCE_FIELDS
        and all(_text(value.get(field)) for field in EVIDENCE_FIELDS)
        and parse_time(value.get("evaluation_time")) is not None
        and parse_time(value.get("produced_at")) is not None
    )


def _matches(records: Any, key: str, reference: Any) -> list[dict[str, Any]]:
    if not isinstance(records, list):
        return []
    return [
        item for item in records
        if isinstance(item, dict) and _text(item.get(key)) == _text(reference)
    ]


def derive_completeness_evidence_recognition(dataset: Any) -> CompletenessEvidenceRecognition:
    if (
        not isinstance(dataset, dict)
        or set(dataset) != DATASET_FIELDS
        or _contains_named(dataset, ACTIVATION_FIELDS)
        or _contains_named(dataset, FORBIDDEN_FIELDS)
    ):
        return INDETERMINATE_RESULT
    request = dataset.get("recognition_request")
    if not _request_valid(request) or request.get("rule_ref") != RULE_REF:
        return INDETERMINATE_RESULT
    profiles = _matches(
        dataset.get("evaluator_profiles"), "evaluator_profile_ref",
        request.get("evaluator_profile_ref"),
    )
    evidence = _matches(
        dataset.get("completeness_evidence"), "completeness_evidence_ref",
        request.get("completeness_evidence_ref"),
    )
    if len(profiles) != 1 or len(evidence) != 1:
        return INDETERMINATE_RESULT
    profile, record = profiles[0], evidence[0]
    if not _profile_valid(profile) or not _evidence_valid(record):
        return INDETERMINATE_RESULT
    evaluation_time = parse_time(request.get("evaluation_time"))
    valid_from = parse_time(profile.get("valid_from"))
    valid_until = parse_time(profile.get("valid_until"))
    produced_at = parse_time(record.get("produced_at"))
    if not all((evaluation_time, valid_from, valid_until, produced_at)):
        return INDETERMINATE_RESULT
    if not (
        profile.get("domain_ref") == DOMAIN_REF
        and profile.get("subject_kind") == SUBJECT_KIND
        and _has_prefix(profile.get("evaluator_ref"), SYNTHETIC_EVALUATOR_PREFIX)
        and _has_prefix(profile.get("authority_basis_ref"), SYNTHETIC_AUTHORITY_PREFIX)
        and valid_from <= evaluation_time < valid_until
        and produced_at <= evaluation_time
        and record.get("evaluator_profile_ref") == request.get("evaluator_profile_ref")
        and record.get("resource_ref") == request.get("resource_ref")
        and record.get("evaluation_time") == request.get("evaluation_time")
        and record.get("assignment_snapshot_ref") == request.get("assignment_snapshot_ref")
        and record.get("coverage_kind") == COVERAGE_KIND
        and record.get("claim") == POSITIVE_CLAIM
    ):
        return INDETERMINATE_RESULT
    return CompletenessEvidenceRecognition(
        REFERENCE_RESULT, str(profile["evaluator_ref"]), str(profile["authority_basis_ref"])
    )


def validate_completeness_evaluator_dataset(dataset: Any) -> ValidationResult:
    errors: list[str] = []
    if not isinstance(dataset, dict) or set(dataset) != DATASET_FIELDS:
        return result(("COMPLETENESS_EVALUATOR_FIXTURE_INVALID",))
    if _contains_named(dataset, ACTIVATION_FIELDS):
        errors.append("COMPLETENESS_EVALUATOR_ACTIVATION_FORBIDDEN")
    if _contains_named(dataset, FORBIDDEN_FIELDS):
        errors.append("COMPLETENESS_EVALUATOR_FORBIDDEN_COUPLING")

    request = dataset.get("recognition_request")
    profiles = dataset.get("evaluator_profiles")
    evidence_records = dataset.get("completeness_evidence")
    if not _request_valid(request) or request.get("rule_ref") != RULE_REF:
        errors.append("COMPLETENESS_EVALUATOR_REQUEST_INVALID")
        request = request if isinstance(request, dict) else {}
    if not isinstance(profiles, list) or any(not _profile_valid(item) for item in profiles):
        errors.append("COMPLETENESS_EVALUATOR_PROFILE_INVALID")
        profiles = profiles if isinstance(profiles, list) else []
    if not isinstance(evidence_records, list) or any(
        not _evidence_valid(item) for item in evidence_records
    ):
        errors.append("COMPLETENESS_EVALUATOR_EVIDENCE_INVALID")
        evidence_records = evidence_records if isinstance(evidence_records, list) else []

    profile_matches = _matches(
        profiles, "evaluator_profile_ref", request.get("evaluator_profile_ref")
    )
    evidence_matches = _matches(
        evidence_records, "completeness_evidence_ref",
        request.get("completeness_evidence_ref"),
    )
    if not profile_matches or not evidence_matches:
        errors.append("COMPLETENESS_EVALUATOR_REFERENCE_UNRESOLVED")
    if len(profile_matches) > 1 or len(evidence_matches) > 1:
        errors.append("COMPLETENESS_EVALUATOR_REFERENCE_AMBIGUOUS")
    if len(evidence_matches) > 1 and len({item.get("claim") for item in evidence_matches}) > 1:
        errors.append("COMPLETENESS_EVALUATOR_EVIDENCE_CONFLICT")

    if len(profile_matches) == 1 and len(evidence_matches) == 1:
        profile, record = profile_matches[0], evidence_matches[0]
        if (
            record.get("evaluator_profile_ref") != request.get("evaluator_profile_ref")
            or record.get("resource_ref") != request.get("resource_ref")
            or record.get("assignment_snapshot_ref") != request.get("assignment_snapshot_ref")
            or record.get("evaluation_time") != request.get("evaluation_time")
        ):
            errors.append("COMPLETENESS_EVALUATOR_SUBJECT_MISMATCH")
        if (
            profile.get("domain_ref") != DOMAIN_REF
            or profile.get("subject_kind") != SUBJECT_KIND
            or record.get("coverage_kind") != COVERAGE_KIND
            or record.get("claim") != POSITIVE_CLAIM
        ):
            errors.append("COMPLETENESS_EVALUATOR_SCOPE_MISMATCH")
        evaluation_time = parse_time(request.get("evaluation_time"))
        valid_from = parse_time(profile.get("valid_from"))
        valid_until = parse_time(profile.get("valid_until"))
        produced_at = parse_time(record.get("produced_at"))
        if not all((evaluation_time, valid_from, valid_until, produced_at)) or not (
            valid_from <= evaluation_time < valid_until and produced_at <= evaluation_time
        ):
            errors.append("COMPLETENESS_EVALUATOR_TIME_INVALID")
        if not (
            _has_prefix(profile.get("evaluator_ref"), SYNTHETIC_EVALUATOR_PREFIX)
            and _has_prefix(profile.get("authority_basis_ref"), SYNTHETIC_AUTHORITY_PREFIX)
        ):
            errors.append("COMPLETENESS_EVALUATOR_AUTHORITY_UNRESOLVED")

    derived = derive_completeness_evidence_recognition(dataset)
    if request.get("stored_result") != derived.result:
        errors.append("COMPLETENESS_EVALUATOR_RESULT_MISMATCH")
    return result(errors)


def validate_completeness_evaluator_fixture(fixture: Any) -> ValidationResult:
    if not isinstance(fixture, dict) or fixture.get("concept") != "CompletenessEvaluatorDataset":
        return result(("COMPLETENESS_EVALUATOR_FIXTURE_INVALID",))
    return validate_completeness_evaluator_dataset(fixture.get("dataset"))
