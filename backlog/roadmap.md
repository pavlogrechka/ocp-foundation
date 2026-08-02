# Foundation Roadmap

## Progress Estimate

Оцінка є не-нормативною управлінською метрикою. Вона показує готовність foundation-репозиторію до переходу від онтологічного каркаса до машинозчитуваних правил і реалізації.

| Напрям | Орієнтовна готовність | Коментар |
|---|---:|---|
| Engineering and governance foundation | 100% | Репозиторій, ADR, governance, registry, review process і versioning створені |
| Core domain ontology | 30% | Resource, Operation та Assignment Accepted; Constraint у PR-0005; більшість Concept ще не визначена |
| Operational rules and workflows | 5% | Є окремі invariants і derivations, але немає завершених coordination, authorization, lifecycle та conflict models |
| Machine-readable schemas and enforcement | 0% | Немає ontology linter, executable schemas, deterministic fixtures або CI checks |
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
- [ ] Review ADR-DRAFT-007 after Constraint
- [ ] Organization Model
- [ ] Operational Coordination Model
- [ ] Objective, Event and Result boundary
- [ ] Operational Area and environment boundary
- [ ] Capability boundary and registry
- [ ] Core Boundary specification
- [ ] Promote stable core descriptions to Canonical

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

## Milestone 3 — Machine-Readable Foundation

- [ ] Machine-readable Concept registry
- [ ] Machine-readable invariants and derivation rules
- [ ] Ontology reference and status linter
- [ ] Constraint evaluation contract and deterministic fixtures
- [ ] Example datasets without sensitive information
- [ ] CI checks for schemas, lifecycle consistency and normative references
- [ ] Versioned implementation-facing contracts

## Planned Sequence

1. PR-0005 — Define Constraint Concept.
2. External review and corrective cycle if required.
3. Constraint patterns for Assignment conflict, exclusivity, capacity and replacement timing.
4. Review ADR-DRAFT-007 using evidence from Operation, Assignment and Constraint.
5. Organization and Coordination concepts.
6. Machine-readable schemas and ontology linter before first Canonical promotion.
