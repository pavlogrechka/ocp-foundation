---
Document-ID: OCP-000
Title: Operational Ontology
Version: 0.12.0
Status: Draft
Owner: Architecture Board
Depends-On: ADR-000
Used-By: Product Vision, Domain Model, Business Rules, Architecture, API, UI
Last-Review: 2026-08-04
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
| Organization | Accepted | OCP-007; Architecture Board approval of PR-0007 |
| Objective | Accepted | OCP-008; AD-003 boundary and Architecture Board approval of PR-0009 |
| Readiness | Deferred | ADR-DRAFT-007; після Constraint та стабілізації Operation і Assignment |
| State | Deferred | ADR-DRAFT-007; після Constraint та стабілізації Operation і Assignment |
| Result | Proposed | Temporary migration accounting: AD-006C rejected a fundamental Result; OCP-011 / AB-056 is Under Review and must remove this entry atomically on acceptance |
| Event | Accepted | OCP-010; AD-006C E3 occurrence/observation model; Architecture Board approval of PR-0012 |
| Spectrum | Proposed | — |
| Constraint | Accepted | OCP-006; Architecture Board approval of PR-0005 |
| Risk | Proposed | AB-005; після Constraint |
| Order | Proposed | AB-002 |
| Coordination | Proposed | — |
| Capability | Accepted | OCP-009; AD-005C; Architecture Board approval of PR-0010 |

Статуси в таблиці є статусами Concept, а не статусами документів. `Accepted` означає, що Architecture Board прийняла поточне визначення як основу подальшої роботи; це не означає `Canonical` і не змінює автоматично статус документа.

`Result: Proposed` не є позитивним identity verdict. Це тимчасовий migration marker, який зберігається до завершення review OCP-011. AD-006C уже встановив negative independent-identity verdict; acceptance OCP-011 повинна видалити Result з активного Concept registry, а не перевести його в `Accepted` або `Deprecated`.

## Governed assessment records

OCP-011 визначає OutcomeAssessmentRecord як P-001 identified record, а не фундаментальний Concept. Record exact-bind-ить Objective target, criterion, evidence snapshot, input snapshot, evaluator, evaluation time, conclusion і provenance та зберігає correction history через explicit supersession.

Під час зовнішнього review OCP-011 цей contract не є Accepted і не резолвить registry entry Result.

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
- Межа між Constraint violation та майбутнім Conflict Concept.
- Зовнішня перевірка OCP-011, його fail-safe assessment semantics і атомарне видалення migration entry `Result` за AB-056.
