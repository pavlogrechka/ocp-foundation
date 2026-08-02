# Foundation Roadmap

## Progress Estimate

Оцінка є не-нормативною управлінською метрикою. Вона показує готовність foundation-репозиторію до переходу від онтологічного каркаса до машинозчитуваних правил і реалізації.

| Напрям | Орієнтовна готовність | Коментар |
|---|---:|---|
| Engineering and governance foundation | 100% | Репозиторій, ADR, governance, registry, review process і versioning створені |
| Core domain ontology | 30% | Resource, Operation та Assignment Accepted; Constraint у PR-0005; більшість Concept ще не визначена |
| Operational rules and workflows | 5% | Є окремі invariants і derivations, але немає завершених coordination, authorization, lifecycle та conflict models |
| Machine-readable schemas and enforcement | 0% | Reference checker, fixtures і CI ще не злиті; перший executable slice заплановано PR-0006 |
| **Загальна foundation-готовність** | **≈25%** | Після прийняття Constraint очікується орієнтовно **≈30%** |

Відсоток не означає готовність production-системи. Репозиторій поки формує специфікаційний фундамент, а не програмну реалізацію.

## Milestone 0 — Engineering Foundation

- [x] Repository initialized
- [x] Branch and PR governance adopted
- [x] Operational Ontology draft
- [x] Ontology Governance draft
- [x] Concept Taxonomy draft
- [x] ADR registry and ADR-000…ADR-006
- [x] ADR-DRAFT-007
- [x] Architecture Board review process established
- [x] Initial foundation merged after approval
- [ ] GitHub Ruleset / branch protection mechanically enforced

## Milestone 1 — Core Domain Foundation

- [x] Resource Accepted working description
- [x] Operation Accepted working description
- [x] Assignment Accepted working description
- [ ] Constraint Accepted working description — PR-0005
- [ ] Review ADR-DRAFT-007 after Constraint and first executable fixtures
- [ ] Organization Model
- [ ] Operational Coordination Model
- [ ] Objective, Event and Result boundary
- [ ] Operational Area and environment boundary
- [ ] Capability boundary and registry
- [ ] Core Boundary specification
- [ ] Promote stable core descriptions to Canonical

## Milestone 1A — Early Executable Validation Loop

Цей milestone виконується одразу після PR-0005, а не відкладається до завершення Operational Rules.

- [ ] `PR-0006 — Add Executable Ontology Checker`
- [ ] YAML fixtures for Resource, Operation, Assignment and Constraint
- [ ] Valid and invalid lifecycle fixtures
- [ ] Regression fixtures for accepted review counterexamples
- [ ] Reference checks for two-way field invariants and authoritative transition histories
- [ ] Reference derivations:
  - `assignment_effective_at`
  - `derived_participates_in`
  - `constraint_applicable_to`
  - `effective_constraint_result`
  - `constraint_set_decision`
- [ ] Initial CI status check
- [ ] Checker guidance for every subsequent Concept PR

PR-0006 є reference validation layer, а не production implementation. Expression language, persistence model і production evaluator залишаються окремими рішеннями.

## Milestone 2 — Operational Rules

- [ ] Constraint pattern library
- [ ] Assignment conflict, exclusivity and capacity rules
- [ ] Business Rules specification
- [ ] Operation Lifecycle
- [ ] Assignment / Operation lifecycle coordination
- [ ] Coordination Workflows
- [ ] Visibility, authorization and approval model
- [ ] Reservation and Allocation decision
- [ ] Conflict and remediation model

## Milestone 3 — Machine-Readable Foundation Expansion

- [ ] Machine-readable Concept registry
- [ ] Machine-readable invariants and derivation rules beyond the PR-0006 reference slice
- [ ] Full ontology reference and status linter
- [ ] Constraint expression and evaluator contracts
- [ ] Example datasets without sensitive information
- [ ] CI checks for schemas, lifecycle consistency and normative references
- [ ] Versioned implementation-facing contracts

## Planned Sequence

1. PR-0005 — Define Constraint Concept.
2. Resolve accepted PR-0005 review findings in the same Concept PR.
3. Architecture Board decision on Constraint; synchronize status before merge.
4. PR-0006 — Add Executable Ontology Checker and regression fixtures.
5. Require fixtures for subsequent Concept and corrective cycles where expressible.
6. Constraint patterns for Assignment conflict, exclusivity, capacity and replacement timing.
7. Review ADR-DRAFT-007 using evidence from Operation, Assignment, Constraint and executable fixtures.
8. Organization and Coordination concepts.
9. Expand machine-readable schemas and ontology linter before first Canonical promotion.
