---
Document-ID: OCP-001
Title: Ontology Governance
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000
Used-By: All OCP specifications and AI development workflows
Last-Review: 2026-08-02
---

# Ontology Governance

## Мета

Визначити правила створення, зміни, канонізації та депрекації понять Operational Ontology.

## Обов’язкові правила

- Operational Ontology є єдиним джерелом канонічних визначень.
- Одне поняття має одну назву й одне місце визначення.
- Поняття реалізації не включаються до онтології.
- Нове фундаментальне поняття потребує рішення Architecture Board.
- Канонічні документи не змінюються напряму в `main`.
- Кожна зміна проходить окрему гілку, draft PR та затвердження Architecture Board.

## Життєвий цикл поняття

`Proposed → Under Review → Accepted → Canonical → Deprecated → Archived`

## Перевірка нового поняття

Поняття може бути запропоноване, якщо воно:

1. існує в реальній операційній діяльності;
2. має самостійне значення або життєвий цикл;
3. має власні правила чи зв’язки;
4. не є лише атрибутом іншого поняття;
5. не дублює наявне канонічне поняття.

## Канонічний шаблон Concept

- Name
- Definition
- Purpose
- Why Exists
- Lifecycle
- Owner
- Participants
- Inputs
- Outputs
- Dependencies
- Relationships
- Events
- Business Rules
- Invariants
- Examples
- Open Questions

## Версіонування

Онтологія використовує Semantic Versioning:

- PATCH — редакційні уточнення без зміни змісту;
- MINOR — сумісне додавання понять або зв’язків;
- MAJOR — несумісна зміна фундаментальної моделі.
