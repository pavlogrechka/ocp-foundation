---
Document-ID: OCP-000
Title: Operational Ontology
Version: 0.5.0
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

Operational Ontology веде реєстр понять, їхніх статусів, зв’язків та інваріантів предметної області OCP.

Онтологія описує реальний операційний світ, а не таблиці бази даних, API, екрани або конкретні технології.

Термін стає канонічним лише після проходження життєвого циклу, визначеного в OCP-001. Сам факт згадування в цьому документі не надає статусу Accepted або Canonical.

## Фундаментальні принципи

1. **Operational Space First** — центром моделі є спільний операційний простір.
2. **Operation First** — будь-яка координована активність моделюється як Operation.
3. **Resource Agnostic** — сили та засоби моделюються через універсальне поняття Resource.
4. **Separation of Structures** — штатна структура, оперативне підпорядкування й операційна координація є незалежними моделями.
5. **One Concept — One Name** — кожне прийняте поняття має одну назву та одне місце визначення.
6. **Knowledge Graph Model** — онтологія є мережею понять і типізованих зв’язків; технологія зберігання не визначається цим документом.

## Початковий реєстр Concept

| Concept | Status | Specification / Decision |
|---|---|---|
| Resource | Accepted | OCP-003 |
| Operation | Accepted | OCP-004; Architecture Board approval of PR-0003 |
| Assignment | Accepted | OCP-005; Architecture Board approval of PR-0004 |
| Operational Space | Proposed | — |
| Operational Area | Proposed | — |
| Organization | Proposed | — |
| Objective | Proposed | — |
| Readiness | Deferred | ADR-DRAFT-007; після Constraint та стабілізації Operation і Assignment |
| State | Deferred | ADR-DRAFT-007; після Constraint та стабілізації Operation і Assignment |
| Result | Proposed | — |
| Event | Proposed | — |
| Spectrum | Proposed | — |
| Constraint | Proposed | наступний Concept cycle; AB-034 |
| Risk | Proposed | — |
| Order | Proposed | AB-002 |
| Coordination | Proposed | — |
| Capability | Proposed | AB-004 |

Статуси в таблиці є статусами Concept, а не статусами документів. `Accepted` означає, що Architecture Board прийняла поточне визначення як основу подальшої роботи; це не означає `Canonical` і не змінює автоматично статус документа.

## Робоче рішення щодо Resource

`Actor` не є окремим фундаментальним Concept. Людина, екіпаж, розрахунок, технічний засіб або інший залучений елемент моделюється як Resource. Його операційна роль визначається через Assignment.

## Незалежні моделі

- Organizational Model — штатна належність.
- Command Model — актуальне управління та підпорядкування.
- Operational Model — участь в операціях.
- Coordination Model — взаємодія між учасниками, зокрема між незалежними вертикалями у спільній операційній зоні.

Назви моделей не створюють однойменні фундаментальні Concept автоматично.

## Відкриті питання

- Остаточна онтологічна природа State і Readiness.
- Межі між Resource та Organization.
- Канонічна модель Operational Situation.
- Канонічна модель погодження між незалежними вертикалями.
