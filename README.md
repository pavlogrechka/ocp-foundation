# OCP Foundation

**Operational Coordination Platform (OCP)** — платформа оперативної координації, що моделює реальний операційний простір та взаємодію сил і засобів.

Цей репозиторій є канонічним джерелом фундаментальних онтологічних, архітектурних та інженерних специфікацій OCP.

## Основний принцип

> Ми не проєктуємо програму. Ми формалізуємо операційну модель реального світу, яку програма лише реалізує.

## Правило затвердження

Жоден документ не потрапляє в `main`, поки його не затвердить Architecture Board.

Усі зміни проходять через окрему гілку та draft pull request.

## Межі репозиторію

Репозиторій містить:

- Operational Ontology;
- Ontology Governance;
- Concept Taxonomy;
- Architecture Decisions і discovery records;
- архітектурний backlog;
- reference checker, схеми та приклади без чутливих даних.

Репозиторій **не повинен містити**:

- реальні операційні дані;
- координати;
- відомості про підрозділи;
- персональні дані;
- ключі, токени та облікові дані;
- інші матеріали обмеженого доступу.

## Структура

```text
docs/                    фундаментальні OCP-специфікації
architecture/discovery/  активні Architecture Decisions і discovery cycles
architecture/reviews/    records зовнішнього review та resolution evidence
patterns/                versioned binding-when-invoked modeling contracts
adr/                     заморожений історичний ADR registry
schemas/                 машинозчитувані схеми
tools/                   reference checker та інженерні перевірки
backlog/                 відкриті питання та дорожня карта
```

## Статус

**Foundation Wave 2 — Governed Executable Foundation.**

- Resource, Operation, Assignment, Constraint, Organization, Objective і Capability мають статус `Accepted`;
- OCP-009 визначає reusable Capability definition, governed namespace ownership, exact-version resolution і supersession без holder claims;
- AB-004 завершено; holder-specific Capability Claim і AB-011 лишаються окремими downstream-рішеннями;
- AD-006C приймає E3: `Event` як occurrence-layer Concept direction, відокремлений від attributable ObservationRecord;
- AD-006C приймає R3: operational result semantics як governed OutcomeAssessmentRecord без фундаментального Result Concept;
- Event і Result поки залишаються `Proposed`: Event — до OCP-010 acceptance, Result — як тимчасовий registry/migration accounting до прийняття R3 contract;
- AB-054 завершено; AB-055 планує Event/Observation contract, AB-056 — OutcomeAssessmentRecord і атомарне розв’язання Result registry entry;
- Operation completion не означає Objective achievement; Event, observation або positive assessment не створюють Capability, Readiness, authorization, admissibility чи State;
- OCP-004 v0.7.0 визначає plural Objective references та fail-safe exact-binding evidence contract для локального explicit intent;
- reference checker перевіряє fixtures, lifecycle projections, exact-version evaluation, Operation intent evidence, Capability registry resolution, Concept status synchronization і dependency graph;
- artifact-governance slice перевіряє identifiers, taxonomy statuses, duplicate AB records, accepted AD↔AB synchronization і `Uses-Patterns` за політикою `track-current`;
- post-factum process audit перевіряє повну Git-історію після governed legacy baseline і fail-closed для shallow, malformed або unreachable evidence;
- GitHub Actions запускає unit tests, fixture validation і перевірку фактичного proposed head у `main`-контексті;
- State і Readiness залишаються `Deferred` за AD-002 до окремого evidence-based рішення;
- наступні заплановані цикли — OCP-010 Event + ObservationRecord, OutcomeAssessmentRecord, integrated non-sensitive scenario, holder-specific Capability Claim і Coordination;
- checker не є production validator, persistence schema або незалежним нормативним джерелом;
- не-нормативна оцінка загальної foundation-готовності: **≈42%**.

Детальна не-нормативна оцінка та послідовність робіт наведені в [Foundation Roadmap](backlog/roadmap.md).
