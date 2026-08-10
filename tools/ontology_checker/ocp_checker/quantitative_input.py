from __future__ import annotations

from decimal import Decimal, InvalidOperation
import re

from .checker import ValidationResult


QUANTITATIVE_INPUT_ERROR_CODES = frozenset(
    {
        "QUANTITATIVE_INPUT_FIXTURE_INVALID",
        "QUANTITATIVE_INPUT_PROFILE_INVALID",
        "QUANTITATIVE_INPUT_REFERENCE_UNRESOLVED",
        "QUANTITATIVE_INPUT_REFERENCE_AMBIGUOUS",
        "QUANTITATIVE_INPUT_OWNER_MISMATCH",
        "QUANTITATIVE_INPUT_VALUE_INVALID",
        "QUANTITATIVE_INPUT_BINDING_MISMATCH",
        "QUANTITATIVE_INPUT_STALE",
        "QUANTITATIVE_INPUT_AGGREGATION_INVALID",
        "QUANTITATIVE_INPUT_UNIT_MISMATCH",
        "QUANTITATIVE_INPUT_DIMENSION_MISMATCH",
        "QUANTITATIVE_INPUT_RESULT_MISMATCH",
        "QUANTITATIVE_INPUT_FORBIDDEN_COUPLING",
    }
)

QUANTITATIVE_INPUT_DERIVATION_RULES = frozenset({"derive_quantitative_total"})

CONTRACT_REF = "OCP-020@0.1.0"
AGGREGATION_RULE_REF = "exact-unit-quantity-sum@1"
ROLES = frozenset({"demand", "capacity_limit", "consumed"})
AGGREGATABLE_ROLES = frozenset({"demand", "consumed"})
RESULT_KEYS = frozenset({"magnitude_lexeme", "unit_ref", "dimension_ref"})
FORBIDDEN_KEYS = frozenset(
    {
        "reservation",
        "reserved",
        "allocation",
        "allocated",
        "available",
        "availability",
        "capacity",
        "capacity_result",
        "capacity_sufficient",
        "remaining_capacity",
        "admissible",
        "within_capacity",
        "capacity_exceeded",
        "assignment_mutation",
        "lifecycle_transition",
        "permission",
        "authorization",
        "risk",
        "conflict",
        "write_off",
        "unit_conversion",
        "conversion_factor",
    }
)
DECIMAL_RE = re.compile(r"^(?:0|[1-9][0-9]*)(?:\.[0-9]*[1-9])?$")


def _nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _decimal(value: object) -> Decimal | None:
    if not isinstance(value, str) or not DECIMAL_RE.fullmatch(value):
        return None
    try:
        parsed = Decimal(value)
    except InvalidOperation:
        return None
    if not parsed.is_finite() or parsed < 0:
        return None
    return parsed


def _canonical_decimal(value: Decimal) -> str:
    if value == 0:
        return "0"
    rendered = format(value, "f")
    if "." in rendered:
        rendered = rendered.rstrip("0").rstrip(".")
    return rendered


def _contains_forbidden(value: object) -> bool:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_KEYS or _contains_forbidden(child):
                return True
    elif isinstance(value, list):
        return any(_contains_forbidden(child) for child in value)
    return False


def _evaluate(dataset: object) -> tuple[dict[str, str] | None, set[str]]:
    errors: set[str] = set()
    if not isinstance(dataset, dict):
        return None, {"QUANTITATIVE_INPUT_FIXTURE_INVALID"}

    profiles = dataset.get("measurement_profiles")
    snapshots = dataset.get("input_snapshots")
    request = dataset.get("aggregation_request")
    if not isinstance(profiles, list) or not isinstance(snapshots, list) or not isinstance(request, dict):
        return None, {"QUANTITATIVE_INPUT_FIXTURE_INVALID"}

    if _contains_forbidden(dataset):
        errors.add("QUANTITATIVE_INPUT_FORBIDDEN_COUPLING")

    valid_profiles: list[dict] = []
    for profile in profiles:
        if not isinstance(profile, dict):
            errors.add("QUANTITATIVE_INPUT_PROFILE_INVALID")
            continue
        profile_ref = profile.get("profile_ref")
        owner_ref = profile.get("profile_owner_ref")
        units = profile.get("units")
        if not _nonempty(profile_ref) or not _nonempty(owner_ref) or not isinstance(units, list) or not units:
            errors.add("QUANTITATIVE_INPUT_PROFILE_INVALID")
            continue
        unit_valid = True
        for unit in units:
            if not isinstance(unit, dict) or not _nonempty(unit.get("unit_ref")) or not _nonempty(unit.get("dimension_ref")):
                unit_valid = False
        if not unit_valid:
            errors.add("QUANTITATIVE_INPUT_PROFILE_INVALID")
            continue
        valid_profiles.append(profile)

    snapshot_ref = request.get("input_snapshot_ref")
    context_ref = request.get("context_ref")
    profile_ref = request.get("measurement_profile_ref")
    owner_ref = request.get("profile_owner_ref")
    role = request.get("role")
    operand_keys = request.get("operand_keys")
    if (
        request.get("contract_ref") != CONTRACT_REF
        or request.get("rule_ref") != AGGREGATION_RULE_REF
        or not _nonempty(snapshot_ref)
        or not _nonempty(context_ref)
        or not _nonempty(profile_ref)
        or not _nonempty(owner_ref)
        or role not in AGGREGATABLE_ROLES
        or not isinstance(operand_keys, list)
        or not operand_keys
        or any(not _nonempty(key) for key in operand_keys)
        or len(operand_keys) != len(set(operand_keys))
    ):
        errors.add("QUANTITATIVE_INPUT_AGGREGATION_INVALID")

    profile_matches = [item for item in valid_profiles if item.get("profile_ref") == profile_ref]
    if not profile_matches:
        errors.add("QUANTITATIVE_INPUT_REFERENCE_UNRESOLVED")
    elif len(profile_matches) > 1:
        errors.add("QUANTITATIVE_INPUT_REFERENCE_AMBIGUOUS")
    profile = profile_matches[0] if len(profile_matches) == 1 else None
    if profile is not None and profile.get("profile_owner_ref") != owner_ref:
        errors.add("QUANTITATIVE_INPUT_OWNER_MISMATCH")

    snapshot_matches = [item for item in snapshots if isinstance(item, dict) and item.get("snapshot_ref") == snapshot_ref]
    if not snapshot_matches:
        errors.add("QUANTITATIVE_INPUT_REFERENCE_UNRESOLVED")
    elif len(snapshot_matches) > 1:
        errors.add("QUANTITATIVE_INPUT_REFERENCE_AMBIGUOUS")
    snapshot = snapshot_matches[0] if len(snapshot_matches) == 1 else None
    if snapshot is not None:
        if snapshot.get("evidence_state") != "current":
            errors.add("QUANTITATIVE_INPUT_STALE")
        if snapshot.get("context_ref") != context_ref:
            errors.add("QUANTITATIVE_INPUT_BINDING_MISMATCH")

    bindings = snapshot.get("bindings") if isinstance(snapshot, dict) else None
    if snapshot is not None and not isinstance(bindings, list):
        errors.add("QUANTITATIVE_INPUT_FIXTURE_INVALID")
        bindings = []
    if isinstance(bindings, list) and any(not isinstance(item, dict) for item in bindings):
        errors.add("QUANTITATIVE_INPUT_FIXTURE_INVALID")
    all_bindings = [item for item in bindings or [] if isinstance(item, dict)]

    selected: list[dict] = []
    if isinstance(bindings, list) and isinstance(operand_keys, list):
        for operand_key in operand_keys:
            matches = [item for item in all_bindings if item.get("binding_key") == operand_key]
            if not matches:
                errors.add("QUANTITATIVE_INPUT_REFERENCE_UNRESOLVED")
                continue
            if len(matches) > 1:
                errors.add("QUANTITATIVE_INPUT_REFERENCE_AMBIGUOUS")
                continue
            selected.append(matches[0])

    units: set[str] = set()
    dimensions: set[str] = set()
    values: list[Decimal] = []
    selected_objects = {id(item) for item in selected}
    for binding in all_bindings:
        is_selected = id(binding) in selected_objects
        required = (
            "binding_key",
            "subject_ref",
            "role",
            "magnitude_lexeme",
            "unit_ref",
            "dimension_ref",
            "measurement_profile_ref",
            "profile_owner_ref",
            "context_ref",
            "input_snapshot_ref",
            "provenance_ref",
            "evaluator_ref",
        )
        if any(not _nonempty(binding.get(key)) for key in required):
            errors.add("QUANTITATIVE_INPUT_VALUE_INVALID")
            continue
        value = _decimal(binding.get("magnitude_lexeme"))
        if value is None:
            errors.add("QUANTITATIVE_INPUT_VALUE_INVALID")
        elif is_selected:
            values.append(value)
        if binding.get("role") not in ROLES:
            errors.add("QUANTITATIVE_INPUT_AGGREGATION_INVALID")
        if is_selected and binding.get("role") != role:
            errors.add("QUANTITATIVE_INPUT_AGGREGATION_INVALID")
        if (
            binding.get("measurement_profile_ref") != profile_ref
            or binding.get("profile_owner_ref") != owner_ref
            or binding.get("context_ref") != context_ref
            or binding.get("input_snapshot_ref") != snapshot_ref
        ):
            errors.add("QUANTITATIVE_INPUT_BINDING_MISMATCH")
        if is_selected:
            units.add(binding.get("unit_ref"))
            dimensions.add(binding.get("dimension_ref"))

        if profile is not None:
            unit_matches = [unit for unit in profile.get("units", []) if unit.get("unit_ref") == binding.get("unit_ref")]
            if not unit_matches:
                errors.add("QUANTITATIVE_INPUT_REFERENCE_UNRESOLVED")
            elif len(unit_matches) > 1:
                errors.add("QUANTITATIVE_INPUT_REFERENCE_AMBIGUOUS")
            elif unit_matches[0].get("dimension_ref") != binding.get("dimension_ref"):
                errors.add("QUANTITATIVE_INPUT_DIMENSION_MISMATCH")

    if len(units) > 1:
        errors.add("QUANTITATIVE_INPUT_UNIT_MISMATCH")
    if len(dimensions) > 1:
        errors.add("QUANTITATIVE_INPUT_DIMENSION_MISMATCH")

    blocking = errors - {"QUANTITATIVE_INPUT_RESULT_MISMATCH"}
    if blocking or not selected or len(values) != len(selected) or len(units) != 1 or len(dimensions) != 1:
        return None, errors
    return {
        "magnitude_lexeme": _canonical_decimal(sum(values, Decimal("0"))),
        "unit_ref": next(iter(units)),
        "dimension_ref": next(iter(dimensions)),
    }, errors


def derive_quantitative_total(dataset: object) -> dict[str, str] | None:
    result, _ = _evaluate(dataset)
    return result


def validate_quantitative_input_dataset(dataset: object) -> ValidationResult:
    result, errors = _evaluate(dataset)
    if isinstance(dataset, dict):
        request = dataset.get("aggregation_request")
        stored = request.get("stored_total") if isinstance(request, dict) else None
        if result is None:
            if stored is not None:
                errors.add("QUANTITATIVE_INPUT_RESULT_MISMATCH")
        elif not isinstance(stored, dict) or set(stored) != RESULT_KEYS or stored != result:
            errors.add("QUANTITATIVE_INPUT_RESULT_MISMATCH")
    return ValidationResult(tuple(sorted(errors)))


def validate_quantitative_input_fixture(fixture: object) -> ValidationResult:
    if not isinstance(fixture, dict):
        return ValidationResult(("QUANTITATIVE_INPUT_FIXTURE_INVALID",))
    return validate_quantitative_input_dataset(fixture.get("dataset"))
