# Foundation Roadmap

## Progress Estimate

Оцінка є не-нормативною управлінською метрикою. Вона показує готовність foundation-репозиторію до переходу від онтологічного каркаса до машинозчитуваних правил і реалізації.

| Напрям | Орієнтовна готовність | Коментар |
|---|---:|---|
| Engineering and governance foundation | 100% | Репозиторій, taxonomy, decision/review process, versioning, Ruleset, required checker і post-factum history audit діють |
| Core domain ontology | 65% | Сім Concepts Accepted; Event occurrence і ObservationRecord визначені в OCP-010 та проходять review; OutcomeAssessmentRecord, Coordination, Operational Area та Core Boundary лишаються відкритими |
| Operational rules and workflows | 15% | Є participation, admissibility, lifecycle projection та explicit-intent validation contracts; coordination, authorization, reservation і conflict models не завершені |
| Machine-readable schemas and enforcement | 50% | PR-0012 додає Event/Observation validators, exact resolution, supersession evidence та перший integrated scenario; production contracts і повний normative linter відсутні |
| **Загальна foundation-готовність** | **≈42%** | OCP-010 ще не Accepted, тому загальний baseline не підвищується до завершення зовнішнього review і Board acceptance; operational rules and workflows лишаються найслабшим напрямом |

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
- [x] State/Readiness review mandate and guardrails accepted in AD-002; final Concepts remain Deferred
- [x] Capability boundary and registry direction accepted in `AD-005C`
- [x] Capability Concept and governed registry contract accepted in `PR-0010 / OCP-009`
- [x] Event and Result boundary accepted in `AD-006C`: E3 occurrence + observation records, R3 governed assessment records
- [ ] Event occurrence Concept and governed ObservationRecord contract — `AB-055 / OCP-010 / PR-0012`, Under Review
- [ ] OutcomeAssessmentRecord contract and Result registry resolution — AB-056
- [ ] Operational Coordination Model
- [ ] Operational Area and environment boundary
- [ ] Core Boundary specification
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
- [ ] OCP-010 Event identity, ObservationRecord, exact references, supersession and zero-observation evidence — implemented in PR-0012, pending review/acceptance
- [ ] Normative OutcomeAssessmentRecord executable evidence — AB-056
- [ ] Cross-file identity uniqueness beyond the currently governed artifact classes
- [ ] Full duplicate normative-rule and reference-integrity linter across all normative artifacts
- [ ] Production validator, persistence and implementation-facing contracts

The checker is a reference validation layer, not production implementation. OCP documents, accepted decisions and machine-readable taxonomy remain authoritative. Expression language, persistence model and production evaluator remain separate decisions.

## Milestone 2 — Operational Rules

- [ ] Constraint pattern library
- [ ] Assignment conflict, exclusivity and capacity rules
- [ ] Business Rules specification
- [ ] Operation Lifecycle completion
- [ ] Assignment / Operation lifecycle coordination
- [ ] Coordination Workflows
- [ ] Visibility, authorization and approval model
- [ ] Reservation and Allocation decision
- [ ] Conflict and remediation model

## Milestone 3 — Machine-Readable Foundation Expansion

- [ ] Machine-readable Concept registry beyond the current status projection
- [ ] Machine-readable invariants and derivation rules beyond the current reference slice
- [ ] Full ontology duplicate/reference linter
- [ ] Constraint expression and evaluator contracts
- [ ] First integrated non-sensitive scenario spanning Operation, Objective, Assignment, Constraint, Event, observations and assessments — implemented in PR-0012, pending external review and Board acceptance
- [ ] Additional example datasets without sensitive information
- [ ] Expanded CI checks for schemas, lifecycle consistency and normative references
- [ ] Versioned implementation-facing contracts

## Planned Sequence

1. Complete external adversarial review and Architecture Board acceptance of `OCP-010 / PR-0012`: occurrence-layer Event Concept, P-001 ObservationRecord, exact references, correction history and integrated non-sensitive scenario.
2. Define the governed OutcomeAssessmentRecord contract under R3, bind exact target/rule/evidence/evaluator semantics and atomically resolve the `Result: Proposed` registry entry when that contract is accepted.
3. Replace the OCP-010 checker-local assessment probe with the accepted AB-056 record contract while preserving the integrated scenario and its fail-safe conclusions.
4. Define the holder-specific Capability Claim boundary and record contract; keep Organization claims bound by AB-006/AB-052.
5. Resolve AB-011 Resource interchangeability using exact Capability claims, applicable Constraint results and operational context without identity collapse.
6. Define Coordination boundaries and workflows for independent verticals.
7. Revisit State and Readiness under the AD-002 evidence contract after Capability claims and Event observations exist.
8. Continue checker expansion with every accepted Concept cycle and complete the full normative reference linter before first Canonical promotion.
