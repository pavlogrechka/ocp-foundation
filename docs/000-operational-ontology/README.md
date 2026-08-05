---
Document-ID: OCP-000
Title: Operational Ontology
Version: 0.16.0
Status: Draft
Owner: Architecture Board
Depends-On: ADR-000
Used-By: Product Vision, Domain Model, Business Rules, Architecture, API, UI
Last-Review: 2026-08-05
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
| Event | Accepted | OCP-010; AD-006C E3 occurrence/observation model; Architecture Board approval of PR-0012 |
| Spectrum | Proposed | — |
| Constraint | Accepted | OCP-006; Architecture Board approval of PR-0005 |
| Risk | Proposed | AB-005; після Constraint |
| Order | Proposed | AB-002 |
| Coordination | Proposed | — |
| Capability | Accepted | OCP-009; AD-005C; Architecture Board approval of PR-0010 |

Статуси в таблиці є статусами Concept, а не статусами документів. `Accepted` означає, що Architecture Board прийняла поточне визначення як основу подальшої роботи; це не означає `Canonical` і не змінює автоматично статус документа.

## Negative identity decision for Result

AD-006C відхилив фундаментальний Concept `Result`: realized outcome не отримує універсальної незалежної identity у foundation ontology.

Architecture Board прийняла OCP-011 у PR-0013 і завершила migration accounting, тому тимчасовий рядок `Result: Proposed` видалено з активного Concept registry. Це не перехід у `Accepted`, `Deprecated` або `Archived`; кандидат deregistered після negative identity verdict.

Термін `result` може використовуватися описово або в локальних контрактах, зокрема `Constraint evaluation result`, але таке використання не створює фундаментальний Concept `Result`.

## Negative identity decisions for State and Readiness

AD-011 окремо прийняв S0 і R0. Поточний foundation не має shared State abstraction і не видає shared Readiness conclusion.

`State` не має доведеної identity незалежно від subject, локального lifecycle, observation, assessment, criterion, context або time. `Readiness` за поточними evidence є можливою contextual conclusion, але не має accepted consumer, criterion owner, target contract, evaluator/rule authority або complete freshness/replay boundary.

Тому рядки `State: Deferred` і `Readiness: Deferred` видалено з active Concept registry. Це не перехід у `Accepted`, `Deprecated` або `Archived`. Терміни можуть лишатися описовими або domain-owned, але не створюють Core Concept чи positive authority. Reopening регулюється AD-011 §25.3.

## Governed assessment records

OCP-011 визначає Accepted `OutcomeAssessmentRecord` як P-001 identified record, а не фундаментальний Concept. Record exact-bind-ить Objective target, criterion, evidence snapshot, input snapshot, evaluator, evaluation time, conclusion і provenance та зберігає correction history через explicit supersession.

OutcomeAssessmentRecord не є Operation lifecycle stage, mutable Objective status, Event truth або універсальним realized outcome. Missing, stale, ambiguous чи conflicting evidence не може створювати definitive conclusion за baseline contract.

## Governed Capability Claim records

OCP-012 визначає Accepted `CapabilityClaimRecord` як P-001 identified record, а не фундаментальний Concept. Record exact-bind-ить Resource holder, одну точну OCP-009 Capability version, claimant, condition set, authority, evidence/support, effectivity та provenance; однакові claims не роблять Resources однаковими або взаємозамінними.

`holder-capability@1` зберігає attributable F0/A0 baseline. `holder-capability@2` явно розділяє declaration-only та evidence-backed modes; лише evidence-backed mode може invoke exact OCP-012-local F1/A1 source-use rules. Така classification не є Capability truth, Readiness, availability, authorization, admissibility або downstream eligibility.

## Робоче рішення щодо Resource

`Actor` не є окремим фундаментальним Concept. Людина, екіпаж, розрахунок, технічний засіб або інший залучений елемент моделюється як Resource. Його операційна роль визначається через Assignment.

## Незалежні моделі

- Organizational Model — штатна належність.
- Command Model — актуальне управління та підпорядкування.
- Operational Model — участь в операціях.
- Coordination Model — взаємодія між учасниками, зокрема між незалежними вертикалями у спільній операційній зоні.

Назви моделей не створюють однойменні фундаментальні Concept автоматично.

## Відкриті питання

- Межі між Resource та Organization.
- Канонічна модель Operational Situation.
- Канонічна модель погодження між незалежними вертикалями.
- Межа між Constraint violation та майбутнім Conflict Concept.
- Наступні contract-local freshness/ambiguity activations після окремих OCP-011 і OCP-012 activations; жодна з них не створює глобального evidence lifetime.
