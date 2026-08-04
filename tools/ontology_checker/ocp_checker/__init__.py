from .checker import (
    DERIVATION_RULES as CORE_DERIVATION_RULES,
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
from .capability import (
    CAPABILITY_DERIVATION_RULES,
    CAPABILITY_ERROR_CODES,
    resolve_capability_definition,
    validate_capability,
    validate_capability_reference_fixture,
    validate_capability_registry,
)
from .event import (
    EVENT_DERIVATION_RULES,
    EVENT_ERROR_CODES,
    observations_for_event,
    resolve_event,
    validate_event,
    validate_event_dataset,
    validate_event_observation_fixture,
    validate_event_reference_fixture,
    validate_integrated_event_scenario,
    validate_observation,
    validate_observation_dataset,
)
from .assessment import (
    OUTCOME_ASSESSMENT_DERIVATION_RULES,
    OUTCOME_ASSESSMENT_ERROR_CODES,
    effective_outcome_conclusion,
    outcome_assessment_heads,
    resolve_outcome_assessment,
    validate_integrated_outcome_scenario,
    validate_outcome_assessment,
    validate_outcome_assessment_dataset,
    validate_outcome_assessment_fixture,
)
from .objective import (
    OBJECTIVE_ERROR_CODES,
    validate_objective,
    validate_objective_dataset,
    validate_operation_fixture,
)
from .artifact_governance import GOVERNANCE_ERROR_CODES

ERROR_CODES = (
    CORE_ERROR_CODES
    | CAPABILITY_ERROR_CODES
    | EVENT_ERROR_CODES
    | OBJECTIVE_ERROR_CODES
    | GOVERNANCE_ERROR_CODES
)
DERIVATION_RULES = (
    CORE_DERIVATION_RULES
    | CAPABILITY_DERIVATION_RULES
    | EVENT_DERIVATION_RULES
)


def validate_reference_fixture(fixture):
    concept = fixture.get("concept")
    if concept == "Capability":
        return validate_capability(fixture.get("entity") or {})
    if concept == "CapabilityRegistry":
        return validate_capability_registry(fixture.get("entities") or [])
    if concept == "CapabilityReference":
        return validate_capability_reference_fixture(fixture)
    if concept == "Event":
        return validate_event(fixture.get("entity") or {})
    if concept == "EventDataset":
        return validate_event_dataset(fixture.get("events") or fixture.get("entities") or [])
    if concept == "EventReference":
        return validate_event_reference_fixture(fixture)
    if concept == "ObservationRecord":
        return validate_observation(fixture.get("entity") or {})
    if concept == "ObservationDataset":
        return validate_observation_dataset(
            fixture.get("observations") or fixture.get("entities") or [],
            fixture.get("events") or [],
        )
    if concept == "EventObservationDataset":
        return validate_event_observation_fixture(fixture)
    if concept == "IntegratedEventScenario":
        return validate_integrated_outcome_scenario(fixture)
    if concept == "OutcomeAssessmentRecord":
        return validate_outcome_assessment(fixture.get("entity") or {})
    if concept == "OutcomeAssessmentDataset":
        return validate_outcome_assessment_fixture(fixture)
    if concept == "Objective":
        return validate_objective(fixture.get("entity") or {})
    if concept == "ObjectiveDataset":
        return validate_objective_dataset(fixture.get("entities") or [])
    return validate_fixture(fixture)


__all__ = [name for name in globals() if not name.startswith("_")]
