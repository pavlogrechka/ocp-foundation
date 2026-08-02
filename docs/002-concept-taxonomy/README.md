---
Document-ID: OCP-002
Title: Concept Taxonomy
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001
Used-By: Domain Model, Knowledge Graph, Architecture
Last-Review: 2026-08-02
---

# Concept Taxonomy

## Верхній рівень

```text
Concept
├── Organization
├── Resource
├── Operation
├── Environment
├── Governance
├── Event
└── Information
```

Ця структура є робочою гіпотезою та не має статусу Canonical.

## Resource

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
│   ├── Position
│   ├── Launch Site
│   └── Relay Site
└── Consumable Resource
```

## Прийнята робоча гіпотеза

`Actor` не виділяється в окрему фундаментальну гілку. Діяч є Resource, який отримує роль у конкретному контексті через Assignment.

```text
Resource + Assignment = operational role in Operation
```

## Базові типи зв’язків

- Structural: `contains`, `belongs_to`, `owns`, `part_of`;
- Operational: `assigned_to`, `participates_in`, `controls`, `coordinates`;
- Spatial: `located_in`, `overlaps`, `intersects`, `adjacent_to`;
- Temporal: `starts_before`, `ends_after`, `overlaps_time`;
- Dependency: `requires`, `depends_on`, `blocks`, `enables`;
- Information: `creates`, `updates`, `confirms`, `reports`.

## Питання до наступного рев’ю

- Чи має Environment залишатися єдиною верхньорівневою категорією для Space, Time і Spectrum?
- Чи є Organization окремою категорією від Resource в усіх операційних контекстах?
- Чи є State окремою верхньорівневою категорією?
