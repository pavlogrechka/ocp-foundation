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
- PR-0012 створив перший integrated non-sensitive scenario з виконуваними `derived_participates_in`, `constraint_applicable_to` та `effective_constraint_result` joints;
- PR-0013 / OCP-011 відкриває AB-056 як `Under Review` і реалізує AD-006C outcome R3 через governed `OutcomeAssessmentRecord`, а не fundamental Result Concept;
- OutcomeAssessmentRecord invokes `P-001@0.1.0`, exact-bind-ить Objective target, assessment kind, criterion, Event/ObservationRecord evidence, immutable evidence/input snapshots, evaluator, evaluation and recording time, conclusion та provenance;
- початкова fail-safe matrix дозволяє definitive conclusion лише для `evidence_state: sufficient`; missing, stale, ambiguous або conflicting evidence дозволяє лише `indeterminate`;
- explicit supersession зберігає history, дозволяє branching і не може змінити target/criterion binding identity; newest record, evaluator count і list order не визначають authority;
- accepted PR-0012 scenario вже мігровано з checker-local assessment envelope на OCP-011 record contract без послаблення cross-Concept derivations;
- `Result` тимчасово лишається `Proposed` лише як migration marker під час review; acceptance OCP-011 повинна атомарно видалити його з active Concept registry, а не перевести в Accepted або Deprecated;
- Operation completion не означає Objective achievement; assessment conclusion не змінює lifecycle і не створює Capability, Readiness, authorization, admissibility, Conflict, Risk чи State;
- OCP-009 визначає reusable Capability definition, governed namespace ownership, exact-version resolution і supersession без holder claims;
- OCP-004 v0.7.0 визначає plural Objective references та fail-safe exact-binding evidence contract для локального explicit intent;
- reference checker перевіряє fixtures, lifecycle projections, exact-version evaluation, Operation intent evidence, Capability registry resolution, Event/Observation references, OutcomeAssessmentRecord, integrated scenario, Concept status synchronization і dependency graph;
- assessment module має власний exact `assessment-rules.yaml` manifest за чинним module-manifest precedent;
- artifact-governance slice перевіряє identifiers, taxonomy statuses, duplicate AB records, accepted AD↔AB synchronization і `Uses-Patterns` за політикою `track-current`;
- post-factum process audit перевіряє повну Git-історію після governed legacy baseline і fail-closed для shallow, malformed або unreachable evidence;
- GitHub Actions запускає unit tests, fixture validation і перевірку фактичного proposed head у `main`-контексті;
- State і Readiness залишаються `Deferred` за AD-002 до окремого evidence-based рішення;
- після AB-056 заплановані holder-specific Capability Claim і Coordination cycles;
- checker не є production validator, persistence schema або незалежним нормативним джерелом;
- не-нормативна оцінка загальної foundation-готовності лишається **≈46%** до external review і Board acceptance OCP-011.

Детальна не-нормативна оцінка та послідовність робіт наведені в [Foundation Roadmap](backlog/roadmap.md).
