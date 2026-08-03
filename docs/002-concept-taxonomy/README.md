---
Document-ID: OCP-002
Title: Concept Taxonomy
Version: 0.10.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001
Used-By: Domain Model, Knowledge Graph, Architecture
Concept-Statuses:
  Resource: Accepted
  Operation: Accepted
  Assignment: Accepted
  Constraint: Accepted
  Organization: Accepted
  Objective: Under Review
Last-Review: 2026-08-03
---

# Concept Taxonomy

## Верхній рівень

```text
Concept Categories
├── Organization
├── Resource
├── Operation
├── Objective
├── Environment
├── Governance
├── Event
└── Information
```

Ця структура є робочою гіпотезою та не має статусу Canonical.

Вузол у цій структурі є категорією класифікації. Категорія таксономії не вважається визначеним фундаментальним Concept без окремого визначення, статусу та рішення Architecture Board. `Governance` є категорією, а не визначеним Concept.

## Organization

Concept `Organization` має статус `Accepted` і визначений у [OCP-007 — Organization Concept](../007-organization-concept/README.md).

Organization представляє сталу організаційну ідентичність. Структурні, оперативні, адміністративні, support і coordination relations моделюються окремими локальними `OrganizationRelationshipRecord` відповідно до AD-001 та P-001; вони не є універсальним фундаментальним Relationship Concept.

`Organization ≠ Resource`. Можливий mapping до Organizational Resource залишається відкритим і не змінює identity жодного Concept.

## Resource

Прийнята чернетка Concept `Resource` визначена в [OCP-003 — Resource Concept](../003-resource-concept/README.md).

```text
Resource
├── Human Resource
│   ├── Person
│   ├── Crew
│   └── Duty Team
├── Organizational Resource
│   └── Unit
├── Technical Resource
│   ├── Platform
│   ├── Equipment
│   ├── Communication Asset
│   └── EW Asset
├── Infrastructure Resource
│   ├── Position Site
│   ├── Launch Site
│   └── Relay Site
└── Consumable Resource
    ├── Fuel Stock
    ├── Energy Stock
    └── Other Consumable Stock
```

`Fuel`, `energy` або інший матеріал як абстрактний тип чи значення кількості не є окремим Resource. Resource у витратній гілці представляє ідентифікований керований запас, партію, контейнер, комплект або іншу облікову одиницю.

## Operation

Concept `Operation` має статус `Accepted` і визначений у [OCP-004](../004-operation-concept/README.md).

Operation є універсальним контекстом координованої діяльності. Предметні типи визначаються domain або capability modules.

```text
Operation
├── Identity
├── Intent
│   └── Objective [Under Review]
├── Temporal Context
├── Spatial Context
│   └── Operational Area [Proposed]
├── Participation
│   └── Assignment [Accepted]
├── Constraints
│   └── Constraint [Accepted]
└── Outcome
    ├── Event [Proposed]
    └── Result [Proposed]
```

## Objective

Concept `Objective` має статус `Under Review` і визначається в [OCP-008 — Objective Concept](../008-objective-concept/README.md) на підставі прийнятої межі AD-003.

Objective представляє intended outcome, condition або effect операційної діяльності. Objective має власну identity, не є Operation, Order, Task або `ExplicitIntentRecord`, а оцінка його досягнення належить майбутнім Event/Result моделям.

Objective не має поточної фундаментальної Concept dependency. Operation нормативно залежить від Objective лише через явну `Concept-Depends-On` декларацію OCP-004.

## Assignment

Concept `Assignment` має статус `Accepted` і визначений у [OCP-005](../005-assignment-concept/README.md).

Assignment є ідентифікованим контекстним зв’язком рівно одного Resource з рівно однією Operation. Участь Resource в Operation є похідною від ефективного Assignment.

## Constraint

Concept `Constraint` має статус `Accepted` і визначений у [OCP-006](../006-constraint-concept/README.md).

Constraint є ідентифікованою декларативною умовою, яка обмежує допустимість або сумісність операційного context. Constraint violation не є автоматично Conflict, Risk, Readiness або State.

## Прийнята робоча гіпотеза

`Actor` не виділяється в окрему фундаментальну гілку. Діяч є Resource, який отримує роль у конкретному контексті через Assignment.

```text
Resource + Assignment + Operation Context = Operational Role
```

## Базові типи зв’язків

Перелік нижче є taxonomy vocabulary, а не універсальною моделлю Relationship:

- Structural;
- Operational;
- Constraint;
- Spatial;
- Temporal;
- Dependency;
- Information.

Конкретна семантика relation належить defining Concept або governed Pattern invocation.

## Питання до наступного рев’ю

- Межа Organization / Organizational Resource.
- Organization identity continuity.
- Taxonomy organization relationship kinds.
- Чи є State окремою верхньорівневою категорією?
- Чи потрібен окремий Concept Operational Intent?
- Чи потрібні окремі Concept Reservation, Allocation, Role Taxonomy або Conflict?
