# Foundation Roadmap

## Progress Estimate

Оцінка є не-нормативною управлінською метрикою. Вона показує готовність foundation-репозиторію до переходу від онтологічного каркаса до машинозчитуваних правил і реалізації.

| Напрям | Орієнтовна готовність | Коментар |
|---|---:|---|
| Engineering and governance foundation | 100% | Репозиторій, taxonomy, decision/review process, versioning, Ruleset, required checker і post-factum history audit діють |
| Core domain ontology | 55% | Шість Concepts Accepted; AD-005C завершив Capability boundary, а OCP-009 definition/registry contract проходить активний draft cycle; Event/Result і Coordination ще не визначені |
| Operational rules and workflows | 15% | Є participation, admissibility, lifecycle projection та explicit-intent validation contracts; coordination, authorization, reservation і conflict models не завершені |
| Machine-readable schemas and enforcement | 45% | Є fixtures, exact manifests, status sync, Concept graph, generated map, artifact governance, Pattern checks, real-history audit і draft Capability registry resolver; production contracts і повний normative linter відсутні |
| **Загальна foundation-готовність** | **≈42%** | Foundation Wave 2 має шість Accepted Concepts, accepted Capability boundary і активний PR-0010 definition/registry cycle |

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
- [ ] Capability Concept and governed registry contract — active draft `PR-0010 / OCP-009`
- [ ] Event and Result boundary
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
- [ ] OCP-009 Capability exact-resolution, namespace, supersession and registry≠possession evidence — active in PR-0010
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
- [ ] Example datasets without sensitive information
- [ ] Expanded CI checks for schemas, lifecycle consistency and normative references
- [ ] Versioned implementation-facing contracts

## Planned Sequence

1. Complete `PR-0010 — Define Capability Concept and Registry Contract`: keep Capability `Proposed` while draft, move synchronously to `Under Review` at ready-for-review, then to `Accepted` only by explicit Board act before merge.
2. Define Event and Result boundaries, including Objective achievement evidence without collapsing events into lifecycle state.
3. Define the holder-specific Capability Claim boundary and record contract; keep Organization claims bound by AB-006/AB-052.
4. Resolve AB-011 Resource interchangeability using exact Capability claims, applicable Constraint results and operational context without identity collapse.
5. Define Coordination boundaries and workflows for independent verticals.
6. Revisit State and Readiness under the AD-002 evidence contract after Capability claims and Event observations exist.
7. Continue checker expansion with every accepted Concept cycle and complete the full normative reference linter before first Canonical promotion.
