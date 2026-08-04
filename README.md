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

- Resource, Operation, Assignment, Constraint, Organization і Objective мають статус `Accepted`;
- AD-005C прийняв two-layer Capability model і направив AB-004 до reusable definition та governed registry contract;
- Capability лишається `Proposed`; draft `PR-0010 / OCP-009` визначає definition-layer identity, namespace ownership, exact versioning, supersession і deterministic resolution без holder claims;
- OCP-004 v0.7.0 визначає plural Objective references та fail-safe exact-binding evidence contract для локального explicit intent;
- reference checker перевіряє fixtures, lifecycle projections, exact-version evaluation, Operation intent evidence, Capability registry resolution, Concept status synchronization і dependency graph;
- artifact-governance slice перевіряє identifiers, taxonomy statuses, duplicate AB records, accepted AD↔AB synchronization і `Uses-Patterns` за політикою `track-current`;
- post-factum process audit перевіряє повну Git-історію після governed legacy baseline і fail-closed для shallow, malformed або unreachable evidence;
- GitHub Actions запускає unit tests, fixture validation і перевірку фактичного proposed head у `main`-контексті;
- State і Readiness залишаються `Deferred` за AD-002 до окремого evidence-based рішення;
- після Capability definition cycle заплановані Event/Result та Coordination boundaries; holder claims і AB-011 лишаються окремими downstream-рішеннями;
- checker не є production validator, persistence schema або незалежним нормативним джерелом;
- не-нормативна оцінка загальної foundation-готовності: **≈42%**.

Детальна не-нормативна оцінка та послідовність робіт наведені в [Foundation Roadmap](backlog/roadmap.md).
