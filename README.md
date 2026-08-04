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

- Resource, Operation, Assignment, Constraint, Organization, Objective, Capability і Event мають статус `Accepted`;
- OCP-010 реалізує AD-006C outcome E3: Event має незалежну occurrence identity, може існувати з zero observations, а kind, timestamp, source count і record order не визначають identity або truth;
- ObservationRecord invokes `P-001@0.1.0`, має власну identity, optional exact Event linkage, attributable provenance і history-preserving supersession з дозволеним branching;
- AB-055 завершено рішенням Architecture Board по PR-0012; Event є восьмим Accepted Concept і лишається isolated у current Concept graph;
- PR-0012 містить перший integrated non-sensitive scenario: Objective + Completed Operation + два Resource/Assignment + Constraint + Event + conflicting observations + fail-safe `indeterminate` checker envelope;
- scenario використовує чинні `derived_participates_in`, `constraint_applicable_to` та `effective_constraint_result`, тому його з'єднання є виконуваними, а не декоративними;
- AD-006C outcome R3 зберігається: normative OutcomeAssessmentRecord належить AB-056, фундаментальний Result Concept не вводиться;
- `Result` тимчасово лишається `Proposed` до атомарної registry resolution разом із прийняттям R3 contract;
- checker-local assessment envelope не є нормативним OutcomeAssessmentRecord і не завершує AB-056;
- Operation completion не означає Objective achievement; Event, observation або positive assessment не створюють Capability, Readiness, authorization, admissibility, Conflict чи State;
- OCP-009 визначає reusable Capability definition, governed namespace ownership, exact-version resolution і supersession без holder claims;
- OCP-004 v0.7.0 визначає plural Objective references та fail-safe exact-binding evidence contract для локального explicit intent;
- reference checker перевіряє fixtures, lifecycle projections, exact-version evaluation, Operation intent evidence, Capability registry resolution, Event/Observation references, integrated scenario, Concept status synchronization і dependency graph;
- artifact-governance slice перевіряє identifiers, taxonomy statuses, duplicate AB records, accepted AD↔AB synchronization і `Uses-Patterns` за політикою `track-current`;
- post-factum process audit перевіряє повну Git-історію після governed legacy baseline і fail-closed для shallow, malformed або unreachable evidence;
- GitHub Actions запускає unit tests, fixture validation і перевірку фактичного proposed head у `main`-контексті;
- State і Readiness залишаються `Deferred` за AD-002 до окремого evidence-based рішення;
- наступні planned cycles — OutcomeAssessmentRecord, holder-specific Capability Claim і Coordination;
- checker не є production validator, persistence schema або незалежним нормативним джерелом;
- не-нормативна оцінка загальної foundation-готовності: **≈46%**.

Детальна не-нормативна оцінка та послідовність робіт наведені в [Foundation Roadmap](backlog/roadmap.md).
