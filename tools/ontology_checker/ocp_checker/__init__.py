from .checker import (
    DERIVATION_RULES,
    ERROR_CODES as CORE_ERROR_CODES,
    ValidationResult,
    assignment_effective_at,
    constraint_applicable_to,
    constraint_blocks,
    constraint_effective_at,
    constraint_set_decision,
    derived_participates_in,
    effective_constraint_result,
    load_fixture,
    validate_assignment,
    validate_constraint,
    validate_fixture,
    validate_operation,
    validate_repository,
    validate_resource,
)
from .objective import (
    OBJECTIVE_ERROR_CODES,
    validate_objective,
    validate_objective_dataset,
    validate_operation_fixture,
)

ERROR_CODES = CORE_ERROR_CODES | OBJECTIVE_ERROR_CODES


def validate_reference_fixture(fixture):
    concept = fixture.get("concept")
    if concept == "Objective":
        return validate_objective(fixture.get("entity") or {})
    if concept == "ObjectiveDataset":
        return validate_objective_dataset(fixture.get("entities") or [])
    return validate_fixture(fixture)


__all__ = [name for name in globals() if not name.startswith("_")]
