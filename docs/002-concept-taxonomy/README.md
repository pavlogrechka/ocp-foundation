---
Document-ID: OCP-002
Title: Concept Taxonomy
Version: 0.5.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001
Used-By: Domain Model, Knowledge Graph, Architecture
Last-Review: 2026-08-02
---

# Concept Taxonomy

## Верхній рівень

```text
Concept Categories
├── Organization
├── Resource
├── Operation
├── Environment
├── Governance
├── Event
└── Information
```

Ця структура є робочою гіпотезою та не має статусу Canonical.

Вузол у цій структурі є категорією класифікації. Категорія таксономії не вважається визначеним фундаментальним Concept без окремого визначення, статусу та рішення Architecture Board. Зокрема, `Governance` у цьому дереві є категорією, а не визначеним Concept.

## Resource

Прийнята чернетка Concept `Resource` визначена в [OCP-003 — Resource Concept](../003-resource-concept/README.md).

Робоча класифікація:

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

Остаточна класифікація Resource не затверджена. Зокрема, відкритими залишаються межі між `Organization`, `Organizational Resource`, `Infrastructure Resource` та категорією `Environment`.

## Operation

Прийнята чернетка Concept `Operation` має статус `Accepted` і визначена в [OCP-004 — Operation Concept](../004-operation-concept/README.md).

Operation є універсальним контекстом координованої діяльності. Предметні типи, зокрема місія БпС або операція РЕБ, визначаються domain або capability modules і не входять до Core Taxonomy автоматично.

Робоча структура:

```text
Operation
├── Identity
├── Intent
│   └── Objective [Proposed]
├── Temporal Context
├── Spatial Context
│   └── Operational Area [Proposed]
├── Participation
│   └── Assignment [Proposed]
├── Constraints
│   └── Constraint [Proposed]
└── Outcome
    ├── Event [Proposed]
    └── Result [Proposed]
```

`Intent`, `Temporal Context`, `Spatial Context`, `Participation`, `Constraints` і `Outcome` у цьому дереві є секціями моделі Operation, а не автоматично окремими фундаментальними Concept.

Остаточна класифікація Operation та її предметних спеціалізацій не затверджена.

## Прийнята робоча гіпотеза

`Actor` не виділяється в окрему фундаментальну гілку. Діяч є Resource, який отримує роль у конкретному контексті через Assignment.

```text
Resource + Assignment + Operation Context = Operational Role
```

## Базові типи зв’язків

- Structural: `contains`, `belongs_to`, `owns`, `part_of`;
- Operational: `assigned_to`, `participates_in`, `controls`, `coordinates`;
- Spatial: `located_in`, `overlaps`, `intersects`, `adjacent_to`;
- Temporal: `starts_before`, `ends_after`, `overlaps_time`;
- Dependency: `requires`, `depends_on`, `blocks`, `enables`;
- Information: `creates`, `updates`, `confirms`, `reports`.

## Питання до наступного рев’ю

- Чи має категорія Environment залишатися єдиною верхньорівневою категорією для Space, Time і Spectrum?
- Чи є Organization окремою категорією від Resource в усіх операційних контекстах?
- Чи є State окремою верхньорівневою категорією?
- Чи потрібна окрема проєкція Organization як Organizational Resource?
- Чи частина Infrastructure Resource повинна належати категорії Environment?
- Чи потрібен окремий Concept Operational Intent?
- Чи належать Objective, Result і Constraint до окремих верхньорівневих категорій?
