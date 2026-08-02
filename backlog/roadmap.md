# Foundation Roadmap

## Progress Estimate

Оцінка є не-нормативною управлінською метрикою. Вона показує готовність foundation-репозиторію до переходу від онтологічного каркаса до машинозчитуваних правил і реалізації.

| Напрям | Орієнтовна готовність | Коментар |
|---|---:|---|
| Engineering and governance foundation | 100% | Репозиторій, ADR, governance, registry, review process і versioning створені |
| Core domain ontology | 40% | Resource, Operation, Assignment і Constraint мають статус Accepted; більшість інших фундаментальних Concept ще не визначена |
| Operational rules and workflows | 10% | Є invariants, participation та admissibility derivations, але немає завершених coordination, authorization, lifecycle та conflict models |
| Machine-readable schemas and enforcement | 20% | Є reference checker, exact-version evaluation, YAML fixtures, regression tests, status synchronization і CI; повний duplicate/reference linter та implementation contracts ще відсутні |
| **Загальна foundation-готовність** | **≈35%** | Перший executable validation loop створено; наступний крок — розширення fixtures і Constraint patterns |

Відсоток не означає готовність production-системи. Репозиторій поки формує специфікаційний фундамент і reference validation layer, а не програмну реалізацію платформи.

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
- [x] Constraint Accepted working description — PR-0005
- [ ] Review ADR-DRAFT-007 after Constraint and first executable fixtures
- [ ] Organization Model
- [ ] Operational Coordination Model
- [ ] Objective, Event and Result boundary
- [ ] Operational Area and environment boundary
- [ ] Capability boundary and registry
- [ ] Core Boundary specification
- [ ] Promote stable core descriptions to Canonical

## Milestone 1A — Early Executable Validation Loop

- [x] `PR-0006 — Add Executable Ontology Checker`
- [x] YAML fixtures for Resource, Operation, Assignment and Constraint
- [x] Valid and invalid lifecycle fixtures for the initial reference subset
- [x] Regression fixtures for silent Assignment termination, contradictory `not_applicable` and stale Constraint versions
- [x] Reference checks for optional materialized projections and authoritative transition histories
- [x] Exact Constraint version and input snapshot selection independent of YAML record order
- [x] Complete provenance manifest for emitted validation codes and derivations
- [x] Meta-test enforcing manifest completeness
- [x] Reference derivations:
  - `assignment_effective_at`
  - `derived_participates_in`
  - `constraint_effective_at`
  - `constraint_applicable_to`
  - `effective_constraint_result`
  - `constraint_blocks`
  - `constraint_set_decision`
- [x] Cross-document Concept status synchronization check
- [x] Initial GitHub Actions CI check
- [x] Checker guidance for subsequent Concept PRs
- [ ] Graph-wide identity uniqueness and acyclicity checks
- [ ] Duplicate normative-rule and reference-integrity linter

PR-0006 є reference validation layer, а не production implementation. OCP documents remain authoritative. Expression language, persistence model and production evaluator remain separate decisions.

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

- [ ] Machine-readable Concept registry beyond the current status projection
- [ ] Machine-readable invariants and derivation rules beyond the PR-0006 reference slice
- [ ] Full ontology duplicate/reference linter
- [ ] Constraint expression and evaluator contracts
- [ ] Example datasets without sensitive information
- [ ] Expanded CI checks for schemas, lifecycle consistency and normative references
- [ ] Versioned implementation-facing contracts

## Planned Sequence

1. `PR-0005 — Define Constraint Concept` — completed and Accepted.
2. `PR-0006 — Add Executable Ontology Checker` — implementation and external review cycle.
3. Require fixtures for subsequent Concept and corrective cycles where expressible.
4. Define Constraint patterns for Assignment conflict, exclusivity, capacity and replacement timing.
5. Review ADR-DRAFT-007 using evidence from Operation, Assignment, Constraint and executable fixtures.
6. Define Organization and Coordination concepts.
7. Expand machine-readable schemas and ontology linter before first Canonical promotion.
