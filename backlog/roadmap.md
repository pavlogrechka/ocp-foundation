# Foundation Roadmap

## Progress Estimate

Оцінка є не-нормативною управлінською метрикою. Вона показує готовність foundation-репозиторію до переходу від онтологічного каркаса до машинозчитуваних правил і реалізації.

| Напрям | Орієнтовна готовність | Коментар |
|---|---:|---|
| Engineering and governance foundation | 100% | Репозиторій, taxonomy, decision/review process, versioning, Ruleset, required checker і post-factum history audit діють |
| Core domain ontology | 82% | Вісім Concepts і governed OCP-012–OCP-015 contracts Accepted; OCP-004 реалізує AD-014B local spatial binding і завершує Operational Area registry migration без нового Concept |
| Operational rules and workflows | 19% | Є participation, admissibility, lifecycle projection, explicit-intent validation, assessment, interchangeability, Coordination consumer profile та proposal-response evidence workflow; AD-010 зберігає visibility та agreement як no-new-authority controls, а authorization, reservation і conflict models не завершені |
| Machine-readable schemas and enforcement | 72% | Local spatial profile/snapshot resolution і immutable transition evidence додані до checker; production contracts, geometry evaluator і semantic duplicate analysis відсутні |
| **Загальна foundation-готовність** | **≈61%** | Spatial/environment boundary реалізовано й AB-008 закрито; наступний великий ontology gap — окрема Core Boundary specification |

Відсоток не означає готовність production-системи. Репозиторій формує специфікаційний фундамент і reference validation layer, а не програмну реалізацію платформи.

## Milestone 0 — Engineering Foundation

- [x] Repository initialized
- [x] Branch and PR governance adopted
- [x] Operational Ontology draft
- [x] Ontology Governance draft
- [x] Concept Taxonomy draft
- [x] ADR registry and ADR-000…ADR-006
- [x] ADR-DRAFT-007
- [x] Active AD discovery/decision registry
- [x] Architecture Board review process established
- [x] Initial foundation merged after approval
- [x] GitHub Ruleset mechanically enforces PR-only, required checker and linear/squash history
- [x] Post-factum Git history audit with governed legacy baseline

## Milestone 1 — Core Domain Foundation

- [x] Resource Accepted working description
- [x] Operation Accepted working description
- [x] Assignment Accepted working description
- [x] Constraint Accepted working description
- [x] Organization Accepted working description
- [x] Objective Accepted working description
- [x] State/Readiness mandate and final axis decision — `AD-002 / AD-011`; S0/R0 accepted, candidates deregistered, R1 remains a separately gated reopening path
- [x] Capability boundary and registry direction accepted in `AD-005C`
- [x] Capability Concept and governed registry contract accepted in `PR-0010 / OCP-009`
- [x] Event and Result boundary accepted in `AD-006C`: E3 occurrence + observation records, R3 governed assessment records
- [x] Event occurrence Concept and governed ObservationRecord contract — `AB-055 / OCP-010 / PR-0012`
- [x] OutcomeAssessmentRecord contract and Result registry resolution — `AB-056 / OCP-011 / PR-0013`
- [x] Holder-specific Capability Claim boundary accepted in `AD-007C`: Outcome B, a single narrowly attributable CapabilityClaimRecord direction
- [x] Normative CapabilityClaimRecord contract with fail-safe claim-head projection — `AB-057 / OCP-012 / PR-0014A`
- [x] Resource interchangeability boundary and Model A direction accepted — `AB-011 / AD-008C`
- [x] Normative deterministic Resource interchangeability contract and executable evidence — `AB-011 / OCP-013 / PR #49`
- [x] Governed Coordination consumer profile — `AB-003 / OCP-014`
- [x] Operational Coordination workflow-evidence boundary — `AB-058 / AD-009 / OCP-015`
- [x] Evidence-based State/Readiness selection — `AB-007 / AD-011`; S0 and R0 no-new-authority controls
- [x] Operational Area and environment boundary — `OCP-004 0.8.0` implements AD-014B Outcome A, resolves `AB-008` and removes the temporary Operational Area registry marker without a new Concept or graph edge
- [ ] Core Boundary specification — `AB-061 / AD-015 0.1.0` Discovery opened; semantic admission and artifact home remain separate unselected axes
- [ ] Promote stable core descriptions to Canonical

## Milestone 1A — Governed Executable Validation Loop

- [x] `PR-0006 — Add Executable Ontology Checker`
- [x] YAML fixtures for Resource, Operation, Assignment and Constraint
- [x] Valid and invalid lifecycle fixtures for the initial reference subset
- [x] Regression fixtures for silent Assignment termination, contradictory `not_applicable` and stale Constraint versions
- [x] Reference checks for optional materialized projections and authoritative transition histories
- [x] Exact Constraint version and input snapshot selection independent of YAML record order
- [x] Complete provenance manifest for emitted validation codes and derivations
- [x] Meta-test enforcing exact manifest completeness
- [x] Reference derivations:
  - `assignment_effective_at`
  - `derived_participates_in`
  - `constraint_effective_at`
  - `constraint_applicable_to`
  - `effective_constraint_result`
  - `constraint_blocks`
  - `constraint_set_decision`
- [x] Cross-document Concept status synchronization check
- [x] Defining-document Concept dependency graph, phantom-reference and cycle checks
- [x] Generated Foundation map and CI drift detection
- [x] OCP-004 exact-binding explicit-intent evidence and fail-safe projection fixtures
- [x] Artifact ID and taxonomy-status checks
- [x] Duplicate AB and accepted AD↔AB synchronization checks
- [x] Pattern semver and `Uses-Patterns` `track-current` checks
- [x] Full-history checkout and post-baseline non-linear-history audit
- [x] PR CI validates the actual proposed head in explicit `main` context
- [x] OCP-009 Capability exact-resolution, namespace, supersession and registry≠possession evidence
- [x] OCP-010 Event identity, ObservationRecord, exact references, supersession and zero-observation evidence
- [x] First integrated non-sensitive scenario with `derived_participates_in`, `constraint_applicable_to` and `effective_constraint_result`
- [x] OCP-011 normative OutcomeAssessmentRecord evidence with exact snapshots, fail-safe states and branching supersession
- [x] Atomic removal of temporary `Result: Proposed` registry marker without creating a Result Concept
- [x] Draft OCP-012 CapabilityClaimRecord exact binding, temporal/supersession history and fail-safe projection fixtures
- [x] OCP-014 exact governed owner binding and wrong-owner fail-safe fixture
- [x] OCP-015 proposal/response exact binding, history-preserving withdrawal, fail-safe projection and symmetric reference-normalization evidence
- [x] First machine-verifiable evidence freshness, ambiguity and deterministic replay activation — `OCP-011 0.3.0` activates F1+A1 for exact `objective-achievement@2`; `AB-039` is Resolved while unactivated consumers remain under F0/A0
- [x] Capability Claim support-usability activation — `OCP-012 0.3.0` implements the AD-013B unified `holder-capability@2` boundary, reviewed `declaration-only → evidence-backed` transition, exact source-use F1/A1 rules and replay evidence; `AB-060` is Resolved
- [x] Global primary-artifact identity uniqueness across OCP, Pattern, AD, ADR and AB registries
- [x] Structured normative-rule and reference-integrity linter for exact `Depends-On`, global manifest rule IDs and resolvable OCP sources
- [x] OCP-004 Operation-local spatial binding with exact profile/snapshot resolution, immutable transition evidence and fail-safe non-implication fixtures
- [ ] Production validator, persistence and implementation-facing contracts

The checker is a reference validation layer, not production implementation. OCP documents, accepted decisions and machine-readable taxonomy remain authoritative. Semantic equivalence or duplication in natural-language normative text remains an external-review obligation; expression language, persistence model and production evaluator remain separate decisions.

## Milestone 2 — Operational Rules

- [ ] Constraint pattern library
- [ ] Assignment conflict, exclusivity and capacity rules
- [ ] Business Rules specification
- [ ] Operation Lifecycle completion
- [ ] Assignment / Operation lifecycle coordination
- [x] Coordination proposal-response evidence workflow — `OCP-015`
- [x] Cross-vertical visibility/agreement boundary — `AD-010` selects independent V0/A0 no-new-authority controls
- [ ] Visibility, authorization and approval model
- [ ] Reservation and Allocation decision
- [ ] Conflict and remediation model

## Milestone 3 — Machine-Readable Foundation Expansion

- [ ] Machine-readable Concept registry beyond the current status projection
- [ ] Machine-readable invariants and derivation rules beyond the current reference slice
- [x] Structured ontology identity/reference linter for primary artifacts, dependency metadata and rule manifests
- [ ] Semantic duplicate analysis across natural-language normative text (external review; no machine-completeness claim)
- [ ] Constraint expression and evaluator contracts
- [x] First integrated non-sensitive scenario spanning Operation, Objective, Assignment, Constraint, Event, observations and assessments — accepted in PR-0012
- [x] Replace its temporary assessment envelope with Accepted OCP-011 OutcomeAssessmentRecord — PR-0013
- [ ] Additional example datasets without sensitive information
- [ ] Expanded CI checks for schemas, lifecycle consistency and normative references
- [ ] Versioned implementation-facing contracts

## Planned Sequence

1. Complete the external AD-015A comparison of semantic-admission models G0–G4 and artifact homes H0–H5 before any Core Boundary implementation artifact is selected.
