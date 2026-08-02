---
Document-ID: OCP-000
Title: Operational Ontology
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: ADR-000
Used-By: Product Vision, Domain Model, Business Rules, Architecture, API, UI
Last-Review: 2026-08-02
---

# Operational Ontology

## Преамбула

> Ми не проєктуємо програму. Ми формалізуємо операційну модель реального світу, яку програма лише реалізує.

## Призначення

Operational Ontology визначає канонічні поняття, зв’язки та інваріанти предметної області OCP.

Онтологія описує реальний операційний світ, а не таблиці бази даних, API, екрани або конкретні технології.

## Фундаментальні принципи

1. **Operational Space First** — центром моделі є спільний операційний простір.
2. **Operation First** — будь-яка координована активність моделюється як Operation.
3. **Resource Agnostic** — сили та засоби моделюються через універсальне поняття Resource.
4. **Separation of Structures** — штатна структура, оперативне підпорядкування й операційна координація є незалежними моделями.
5. **One Concept — One Name** — кожне поняття має одну канонічну назву та визначення.
6. **Knowledge Graph Model** — онтологія є мережею понять і типізованих зв’язків; технологія зберігання не визначається цим документом.

## Початкові канонічні поняття

- Operation
- Operational Space
- Operational Area
- Organization
- Resource
- Assignment
- Objective
- Readiness
- Result
- Event
- Spectrum
- Constraint
- Risk
- Order
- Coordination
- Capability

## Робоче рішення щодо Resource

Actor не є окремим фундаментальним Concept. Людина, екіпаж, розрахунок, технічний засіб або інший залучений елемент моделюється як Resource. Його операційна роль визначається через Assignment.

## Незалежні моделі

- Organizational Model — штатна належність.
- Command Model — актуальне управління та підпорядкування.
- Operational Model — участь в операціях.
- Coordination Model — взаємодія між учасниками, зокрема між незалежними вертикалями у спільній операційній зоні.

## Відкриті питання

- Чи є State окремим фундаментальним Concept?
- Межі між Resource та Organization.
- Канонічна модель Operational Situation.
- Канонічна модель погодження між незалежними вертикалями.
