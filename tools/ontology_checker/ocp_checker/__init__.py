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
from .capability_claim import (
    CAPABILITY_CLAIM_DERIVATION_RULES,
    CAPABILITY_CLAIM_ERROR_CODES,
    capability_claim_effective_at,
    capability_claim_heads,
    derive_capability_claim_support_usability,
    effective_capability_claim,
    resolve_capability_claim,
    validate_capability_claim,
    validate_capability_claim_dataset,
    validate_capability_claim_fixture,
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
    derive_outcome_evidence_usability,
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
    validate_objective_correction_fixture,
    validate_objective_dataset,
    validate_operation_fixture,
)
from .spatial import (
    SPATIAL_ERROR_CODES,
    validate_operation_spatial_context,
    validate_operation_spatial_transition,
    validate_operation_spatial_transition_fixture,
)
from .organization import (
    ORGANIZATION_DERIVATION_RULES,
    ORGANIZATION_ERROR_CODES,
    graph_breakpoints,
    organization_established_at,
    organization_relationship_effective_at,
    organization_relationship_successor_ids,
    validate_organization,
    validate_organization_dataset,
    validate_organization_dataset_fixture,
    validate_organization_graph,
    validate_organization_q2_fixture,
    validate_organization_relationship,
    validate_organization_relationship_fixture,
)
from .artifact_governance import GOVERNANCE_ERROR_CODES
from .interchangeability import (
    COORDINATION_OWNER_REF,
    INTERCHANGEABILITY_DERIVATION_RULES,
    INTERCHANGEABILITY_ERROR_CODES,
    derive_resource_interchangeability,
    resolve_interchangeability_requirement,
    validate_coordination_requirement,
    validate_interchangeability_dataset,
    validate_interchangeability_fixture,
    validate_interchangeability_requirement,
)
from .coordination_workflow import (
    COORDINATION_WORKFLOW_DERIVATION_RULES,
    COORDINATION_WORKFLOW_ERROR_CODES,
    derive_coordination_evidence,
    validate_coordination_proposal,
    validate_coordination_response,
    validate_coordination_workflow_dataset,
    validate_coordination_workflow_fixture,
)
from .operation_lifecycle import (
    OPERATION_LIFECYCLE_DERIVATION_RULES,
    OPERATION_LIFECYCLE_ERROR_CODES,
    derive_operation_lifecycle_stage,
    validate_operation_q3i_dataset,
    validate_operation_q3i_fixture,
)
from .operation_authorization import (
    OPERATION_AUTHORIZATION_DERIVATION_RULES,
    OPERATION_AUTHORIZATION_ERROR_CODES,
    derive_operation_authorization_result,
    validate_operation_authorization_dataset,
    validate_operation_authorization_fixture,
)
from .conflict_derivation import (
    CONFLICT_DERIVATION_DERIVATION_RULES,
    CONFLICT_DERIVATION_ERROR_CODES,
    derive_conflict_establishment_result,
    validate_conflict_derivation_dataset,
    validate_conflict_derivation_fixture,
)
from .quantitative_input import (
    QUANTITATIVE_INPUT_DERIVATION_RULES,
    QUANTITATIVE_INPUT_ERROR_CODES,
    derive_quantitative_total,
    validate_quantitative_input_dataset,
    validate_quantitative_input_fixture,
)
from .reservation_boundary import (
    RESERVATION_BOUNDARY_DERIVATION_RULES,
    RESERVATION_BOUNDARY_ERROR_CODES,
    derive_quantitative_reservation_boundary,
    derive_whole_resource_reservation_boundary,
    validate_reservation_boundary_dataset,
    validate_reservation_boundary_fixture,
)
from .constraint_interaction import (
    CONSTRAINT_INTERACTION_DERIVATION_RULES,
    CONSTRAINT_INTERACTION_ERROR_CODES,
    derive_constraint_application_order_boundary,
    derive_constraint_override_boundary,
    derive_contextual_waiver_boundary,
    validate_constraint_interaction_dataset,
    validate_constraint_interaction_fixture,
)

ERROR_CODES = (
    CORE_ERROR_CODES
    | CAPABILITY_ERROR_CODES
    | EVENT_ERROR_CODES
    | OBJECTIVE_ERROR_CODES
    | SPATIAL_ERROR_CODES
    | GOVERNANCE_ERROR_CODES
)
DERIVATION_RULES = (
    CORE_DERIVATION_RULES
    | CAPABILITY_DERIVATION_RULES
    | EVENT_DERIVATION_RULES
)


def validate_reference_fixture(fixture):
    concept = fixture.get("concept")
    if concept == "Organization":
        return validate_organization(fixture.get("entity") or {})
    if concept == "OrganizationRelationshipRecord":
        return validate_organization_relationship_fixture(fixture)
    if concept == "OrganizationDataset":
        return validate_organization_dataset_fixture(fixture)
    if concept == "OrganizationQ2ContractDataset":
        return validate_organization_q2_fixture(fixture)
    if concept == "OperationSpatialTransitionEvidence":
        return validate_operation_spatial_transition_fixture(fixture)
    if concept == "Capability":
        return validate_capability(fixture.get("entity") or {})
    if concept == "CapabilityRegistry":
        return validate_capability_registry(fixture.get("entities") or [])
    if concept == "CapabilityReference":
        return validate_capability_reference_fixture(fixture)
    if concept == "CapabilityClaimRecord":
        return validate_capability_claim(fixture.get("entity") or {})
    if concept == "CapabilityClaimDataset":
        return validate_capability_claim_fixture(fixture)
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
    if concept == "ObjectiveCorrectionEvidence":
        return validate_objective_correction_fixture(fixture)
    if concept == "ResourceInterchangeabilityDataset":
        return validate_interchangeability_fixture(fixture)
    if concept == "CoordinationResourceRequirement":
        return validate_coordination_requirement(fixture.get("entity") or {})
    if concept == "CoordinationWorkflowDataset":
        return validate_coordination_workflow_fixture(fixture)
    if concept == "OperationQ3IContractDataset":
        return validate_operation_q3i_fixture(fixture)
    if concept == "OperationAuthorizationSourceDataset":
        return validate_operation_authorization_fixture(fixture)
    if concept == "ConflictDerivationBoundaryDataset":
        return validate_conflict_derivation_fixture(fixture)
    if concept == "QuantitativeInputDataset":
        return validate_quantitative_input_fixture(fixture)
    if concept == "ReservationBoundaryDataset":
        return validate_reservation_boundary_fixture(fixture)
    if concept == "ConstraintInteractionDataset":
        return validate_constraint_interaction_fixture(fixture)
    return validate_fixture(fixture)


__all__ = [name for name in globals() if not name.startswith("_")]
