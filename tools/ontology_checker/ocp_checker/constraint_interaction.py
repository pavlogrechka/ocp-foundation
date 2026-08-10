from __future__ import annotations

from typing import Any

from ._common import nonempty, result
from .checker import ValidationResult


CONSTRAINT_INTERACTION_ERROR_CODES = frozenset(
    {
        "CONSTRAINT_INTERACTION_FIXTURE_INVALID",
        "CONSTRAINT_INTERACTION_REQUEST_INVALID",
        "CONSTRAINT_INTERACTION_KIND_INVALID",
        "CONSTRAINT_INTERACTION_INPUT_INVALID",
        "CONSTRAINT_INTERACTION_INPUT_UNRESOLVED",
        "CONSTRAINT_INTERACTION_INPUT_AMBIGUOUS",
        "CONSTRAINT_INTERACTION_CONTEXT_MISMATCH",
        "CONSTRAINT_INTERACTION_SNAPSHOT_MISMATCH",
        "CONSTRAINT_INTERACTION_INPUT_STALE",
        "CONSTRAINT_INTERACTION_OVERRIDE_TARGET_INVALID",
        "CONSTRAINT_INTERACTION_PRECEDENCE_SELECTOR_FORBIDDEN",
        "CONSTRAINT_INTERACTION_CONVENIENCE_OVERRIDE_FORBIDDEN",
        "CONSTRAINT_INTERACTION_OCP018_TAKEOVER_FORBIDDEN",
        "CONSTRAINT_INTERACTION_WAIVER_BYPASS_FORBIDDEN",
        "CONSTRAINT_INTERACTION_POSITIVE_RESULT_FORBIDDEN",
        "CONSTRAINT_INTERACTION_RESULT_MISMATCH",
    }
)

CONSTRAINT_INTERACTION_DERIVATION_RULES = frozenset(
    {
        "derive_constraint_application_order_boundary",
        "derive_constraint_override_boundary",
        "derive_contextual_waiver_boundary",
    }
)

APPLICATION_ORDER = "application_order"
OVERRIDE = "override"
CONTEXTUAL_WAIVER = "contextual_waiver"
INTERACTION_KINDS = frozenset({APPLICATION_ORDER, OVERRIDE, CONTEXTUAL_WAIVER})

RULE_REFS = {
    APPLICATION_ORDER: "constraint-application-order-boundary@1",
    OVERRIDE: "constraint-override-boundary@1",
    CONTEXTUAL_WAIVER: "constraint-waiver-boundary@1",
}

NEGATIVE_RESULTS = {
    APPLICATION_ORDER: "constraint_application_order_not_established",
    OVERRIDE: "constraint_override_not_established",
    CONTEXTUAL_WAIVER: "contextual_waiver_not_established",
}
DERIVED_RESULTS = frozenset({"indeterminate", *NEGATIVE_RESULTS.values()})

# These finite defensive vocabularies are deliberately exported. Each individual
# value has its own fixture and focused mutation assertion; none is category-only.
PRECEDENCE_SELECTOR_FIELDS = frozenset(
    {
        "precedence_timestamp",
        "precedence_record_order",
        "precedence_source_count",
        "precedence_issuer_count",
        "precedence_caller_identity",
        "precedence_provenance_label",
        "precedence_operation_relation_value",
    }
)
CONVENIENCE_OVERRIDE_FIELDS = frozenset({"convenience_override"})
OCP018_TAKEOVER_FIELDS = frozenset(
    {
        "operation_authorization_level_order",
        "operation_authorization_derivation_override",
    }
)
WAIVER_BYPASS_FIELDS = frozenset(
    {
        "waiver_ref",
        "exception_ref",
        "exception_label",
        "producer_bypass",
        "policy_ref",
        "authority_ref",
        "approval_ref",
    }
)
POSITIVE_RESULTS = frozenset(
    {"precedence_established", "override_effective", "waiver_granted"}
)
EVIDENCE_STATES = frozenset({"current", "stale"})

DATASET_FIELDS = frozenset({"interaction_request", "constraint_application_inputs"})
COMMON_REQUEST_FIELDS = frozenset(
    {
        "request_id",
        "interaction_kind",
        "rule_ref",
        "context_ref",
        "input_snapshot_ref",
        "stored_result",
    }
)
APPLICATION_REQUEST_FIELDS = COMMON_REQUEST_FIELDS | {"constraint_version_refs"}
OVERRIDE_REQUEST_FIELDS = COMMON_REQUEST_FIELDS | {
    "overriding_constraint_version_ref",
    "affected_constraint_version_ref",
}
WAIVER_REQUEST_FIELDS = COMMON_REQUEST_FIELDS | {"affected_constraint_version_ref"}
INPUT_FIELDS = frozenset(
    {
        "constraint_version_ref",
        "context_ref",
        "input_snapshot_ref",
        "evidence_state",
        "provenance_ref",
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


def _contains_positive_result(value: Any) -> bool:
    if isinstance(value, dict):
        return any(_contains_positive_result(item) for item in value.values())
    if isinstance(value, list):
        return any(_contains_positive_result(item) for item in value)
    return isinstance(value, str) and value in POSITIVE_RESULTS


def _unique_text_list(value: Any, *, minimum: int) -> bool:
    if not isinstance(value, list) or len(value) < minimum:
        return False
    normalized = [_text(item) for item in value]
    return all(item is not None for item in normalized) and len(normalized) == len(
        set(normalized)
    )


def _request_fields(kind: Any) -> frozenset[str] | None:
    if kind == APPLICATION_ORDER:
        return APPLICATION_REQUEST_FIELDS
    if kind == OVERRIDE:
        return OVERRIDE_REQUEST_FIELDS
    if kind == CONTEXTUAL_WAIVER:
        return WAIVER_REQUEST_FIELDS
    return None


def _request_shape_valid(request: Any) -> bool:
    if not isinstance(request, dict):
        return False
    kind = request.get("interaction_kind")
    fields = _request_fields(kind)
    if fields is None or set(request) != fields:
        return False
    if not all(
        _text(request.get(field)) is not None
        for field in COMMON_REQUEST_FIELDS
    ):
        return False
    if kind == APPLICATION_ORDER:
        return _unique_text_list(request.get("constraint_version_refs"), minimum=2)
    if kind == OVERRIDE:
        overriding = _text(request.get("overriding_constraint_version_ref"))
        affected = _text(request.get("affected_constraint_version_ref"))
        return overriding is not None and affected is not None
    return _text(request.get("affected_constraint_version_ref")) is not None


def _input_shape_valid(item: Any) -> bool:
    return bool(
        isinstance(item, dict)
        and set(item) == INPUT_FIELDS
        and all(
            _text(item.get(field)) is not None
            for field in (
                "constraint_version_ref",
                "context_ref",
                "input_snapshot_ref",
                "provenance_ref",
            )
        )
        and item.get("evidence_state") in EVIDENCE_STATES
    )


def _expected_refs(request: dict[str, Any]) -> list[str]:
    kind = request.get("interaction_kind")
    if kind == APPLICATION_ORDER:
        return [str(item).strip() for item in request["constraint_version_refs"]]
    if kind == OVERRIDE:
        return [
            str(request["overriding_constraint_version_ref"]).strip(),
            str(request["affected_constraint_version_ref"]).strip(),
        ]
    if kind == CONTEXTUAL_WAIVER:
        return [str(request["affected_constraint_version_ref"]).strip()]
    return []


def _resolution_count(ref: str, inputs: list[Any]) -> int:
    return sum(
        1
        for item in inputs
        if isinstance(item, dict)
        and _text(item.get("constraint_version_ref")) == ref
    )


def _selected_inputs(request: dict[str, Any], inputs: list[Any]) -> list[dict[str, Any]] | None:
    selected: list[dict[str, Any]] = []
    for ref in _expected_refs(request):
        matches = [
            item
            for item in inputs
            if isinstance(item, dict)
            and _text(item.get("constraint_version_ref")) == ref
        ]
        if len(matches) != 1:
            return None
        selected.append(matches[0])
    return selected


def _derive(dataset: Any, expected_kind: str) -> str:
    if (
        not isinstance(dataset, dict)
        or set(dataset) != DATASET_FIELDS
        or _contains_named(dataset, PRECEDENCE_SELECTOR_FIELDS)
        or _contains_named(dataset, CONVENIENCE_OVERRIDE_FIELDS)
        or _contains_named(dataset, OCP018_TAKEOVER_FIELDS)
        or _contains_named(dataset, WAIVER_BYPASS_FIELDS)
        or _contains_positive_result(dataset)
    ):
        return "indeterminate"
    request = dataset.get("interaction_request")
    inputs = dataset.get("constraint_application_inputs")
    if not _request_shape_valid(request) or not isinstance(inputs, list):
        return "indeterminate"
    kind = request.get("interaction_kind")
    if kind != expected_kind or request.get("rule_ref") != RULE_REFS.get(kind):
        return "indeterminate"
    if kind == OVERRIDE and (
        _text(request.get("overriding_constraint_version_ref"))
        == _text(request.get("affected_constraint_version_ref"))
    ):
        return "indeterminate"
    selected = _selected_inputs(request, inputs)
    if selected is None or any(not _input_shape_valid(item) for item in selected):
        return "indeterminate"
    if any(
        _text(item.get("context_ref")) != _text(request.get("context_ref"))
        or _text(item.get("input_snapshot_ref"))
        != _text(request.get("input_snapshot_ref"))
        or item.get("evidence_state") != "current"
        for item in selected
    ):
        return "indeterminate"
    return NEGATIVE_RESULTS[kind]


def derive_constraint_application_order_boundary(dataset: Any) -> str:
    """Derive only the absence of normative Constraint application precedence."""
    return _derive(dataset, APPLICATION_ORDER)


def derive_constraint_override_boundary(dataset: Any) -> str:
    """Derive only the absence of one Constraint overriding another."""
    return _derive(dataset, OVERRIDE)


def derive_contextual_waiver_boundary(dataset: Any) -> str:
    """Derive only the absence of a contextual Constraint waiver."""
    return _derive(dataset, CONTEXTUAL_WAIVER)


def _derive_for_kind(dataset: Any, kind: Any) -> str:
    if kind == APPLICATION_ORDER:
        return derive_constraint_application_order_boundary(dataset)
    if kind == OVERRIDE:
        return derive_constraint_override_boundary(dataset)
    if kind == CONTEXTUAL_WAIVER:
        return derive_contextual_waiver_boundary(dataset)
    return "indeterminate"


def validate_constraint_interaction_dataset(dataset: Any) -> ValidationResult:
    if not isinstance(dataset, dict) or set(dataset) != DATASET_FIELDS:
        return result(["CONSTRAINT_INTERACTION_FIXTURE_INVALID"])

    errors: list[str] = []
    request = dataset.get("interaction_request")
    inputs = dataset.get("constraint_application_inputs")

    if _contains_named(dataset, PRECEDENCE_SELECTOR_FIELDS):
        errors.append("CONSTRAINT_INTERACTION_PRECEDENCE_SELECTOR_FORBIDDEN")
    if _contains_named(dataset, CONVENIENCE_OVERRIDE_FIELDS):
        errors.append("CONSTRAINT_INTERACTION_CONVENIENCE_OVERRIDE_FORBIDDEN")
    if _contains_named(dataset, OCP018_TAKEOVER_FIELDS):
        errors.append("CONSTRAINT_INTERACTION_OCP018_TAKEOVER_FORBIDDEN")
    if _contains_named(dataset, WAIVER_BYPASS_FIELDS):
        errors.append("CONSTRAINT_INTERACTION_WAIVER_BYPASS_FORBIDDEN")
    if _contains_positive_result(dataset):
        errors.append("CONSTRAINT_INTERACTION_POSITIVE_RESULT_FORBIDDEN")

    if not _request_shape_valid(request):
        errors.append("CONSTRAINT_INTERACTION_REQUEST_INVALID")
        return result(errors)

    kind = request.get("interaction_kind")
    if kind not in INTERACTION_KINDS or request.get("rule_ref") != RULE_REFS.get(kind):
        errors.append("CONSTRAINT_INTERACTION_KIND_INVALID")

    if kind == OVERRIDE and (
        _text(request.get("overriding_constraint_version_ref"))
        == _text(request.get("affected_constraint_version_ref"))
    ):
        errors.append("CONSTRAINT_INTERACTION_OVERRIDE_TARGET_INVALID")

    if not isinstance(inputs, list):
        errors.append("CONSTRAINT_INTERACTION_INPUT_UNRESOLVED")
        inputs = []

    expected_refs = _expected_refs(request)
    for ref in expected_refs:
        count = _resolution_count(ref, inputs)
        if count == 0:
            errors.append("CONSTRAINT_INTERACTION_INPUT_UNRESOLVED")
        elif count > 1:
            errors.append("CONSTRAINT_INTERACTION_INPUT_AMBIGUOUS")

    selected = _selected_inputs(request, inputs)
    if selected is not None:
        if any(not _input_shape_valid(item) for item in selected):
            errors.append("CONSTRAINT_INTERACTION_INPUT_INVALID")
        if any(
            _text(item.get("context_ref")) != _text(request.get("context_ref"))
            for item in selected
        ):
            errors.append("CONSTRAINT_INTERACTION_CONTEXT_MISMATCH")
        if any(
            _text(item.get("input_snapshot_ref"))
            != _text(request.get("input_snapshot_ref"))
            for item in selected
        ):
            errors.append("CONSTRAINT_INTERACTION_SNAPSHOT_MISMATCH")
        if any(item.get("evidence_state") == "stale" for item in selected):
            errors.append("CONSTRAINT_INTERACTION_INPUT_STALE")

    derived = _derive_for_kind(dataset, kind)
    if request.get("stored_result") not in DERIVED_RESULTS or request.get("stored_result") != derived:
        errors.append("CONSTRAINT_INTERACTION_RESULT_MISMATCH")
    return result(errors)


def validate_constraint_interaction_fixture(fixture: dict[str, Any]) -> ValidationResult:
    dataset = fixture.get("dataset")
    if not isinstance(dataset, dict):
        return result(["CONSTRAINT_INTERACTION_FIXTURE_INVALID"])
    return validate_constraint_interaction_dataset(dataset)
