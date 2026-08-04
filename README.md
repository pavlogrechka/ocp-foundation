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
- PR-0012 створив перший integrated non-sensitive scenario з виконуваними `derived_participates_in`, `constraint_applicable_to` та `effective_constraint_result` joints;
- OCP-011 `0.2.0 / Accepted` реалізує AD-006C outcome R3 через governed `OutcomeAssessmentRecord`, а не fundamental Result Concept;
- OutcomeAssessmentRecord invokes `P-001@0.1.0`, exact-bind-ить Objective target, assessment kind, criterion, Event/ObservationRecord evidence, immutable evidence/input snapshots, evaluator, evaluation and recording time, conclusion та provenance;
- fail-safe matrix дозволяє definitive conclusion лише для `evidence_state: sufficient`; missing, stale, ambiguous або conflicting evidence дозволяє лише `indeterminate`;
- checker механічно виводить `missing` і finite `conflicting` probe; `stale` та `ambiguous` залишаються attributable evaluator assertions до прийняття freshness/replay semantics в AB-039;
- explicit supersession зберігає history, дозволяє branching і не може змінити assessment kind, target або criterion binding identity; newest record, evaluator count і list order не визначають authority;
- integrated scenario використовує нормативний OCP-011 record contract і продовжує механічно доводити `Completed ≠ achieved`;
- AB-056 завершено рішенням Architecture Board по PR-0013;
- фундаментальний `Result` відхилено AD-006C і видалено з active Concept registry та generated Foundation map без переходу в Accepted, Deprecated або Archived;
- вісь AD-006 завершена: occurrence Event + attributable ObservationRecord + governed OutcomeAssessmentRecord;
- OCP-009 визначає reusable Capability definition, governed namespace ownership, exact-version resolution і supersession без holder claims;
- AD-007C обрав single CapabilityClaimRecord direction; OCP-012 `0.2.0 / Accepted` реалізує її як governed non-Concept record contract без нового graph edge;
- CapabilityClaimRecord exact-bind-ить Resource, OCP-009 Capability version, claimant, governed claim kind, condition set, authority, evidence/support, time та provenance;
- withdrawal не дорівнює negative claim; branching, stale/conflicting support і unresolved inputs fail safe без newest/order/count authority;
- AD-008C приймає Model A як напрямок AB-011: deterministic directional eligibility з consumer-owned exact requirement; matching claims не створюють Resource equality, а admissibility, availability, authorization, selection і Assignment execution лишаються окремими шарами;
- OCP-013 `0.2.0 / Accepted` визначає exact consumer requirement, directional eligibility, fail-safe claim/Constraint bindings, rule-version replay та executable evidence для всіх AD-008 §12 counterexamples;
- OCP-014 `0.2.0 / Accepted` активує exact governed owner `ocp-coordination-consumer@0.1.0` для одного contextual requirement, fail-safe wrong-owner binding і окрему actor-authorization boundary без workflow authority;
- AD-009 і OCP-015 `0.2.0 / Accepted` визначають окремі immutable proposal/response records, exact-revision confirmation та fail-safe evidence projection без authorization, selection або Assignment mutation;
- OCP-004 v0.7.0 визначає plural Objective references та fail-safe exact-binding evidence contract для локального explicit intent;
- reference checker перевіряє fixtures, lifecycle projections, exact-version evaluation, Operation intent evidence, Capability registry resolution, Event/Observation references, OutcomeAssessmentRecord, accepted Coordination workflow evidence, integrated scenario, Concept status synchronization і dependency graph;
- assessment module має власний exact `assessment-rules.yaml` manifest за чинним module-manifest precedent;
- artifact-governance slice перевіряє identifiers, taxonomy statuses, duplicate AB records, accepted AD↔AB synchronization і `Uses-Patterns` за політикою `track-current`;
- post-factum process audit перевіряє повну Git-історію після governed legacy baseline і fail-closed для shallow, malformed або unreachable evidence;
- GitHub Actions запускає unit tests, fixture validation і перевірку фактичного proposed head у `main`-контексті;
- State і Readiness залишаються `Deferred` за AD-002 до окремого evidence-based рішення;
- AB-011 / AD-008 Resource interchangeability, AB-003 consumer profile та AB-058 workflow-evidence scope завершено через Accepted OCP-013–OCP-015; залишкові visibility-policy та agreement-semantics питання обліковуються окремо в AB-059;
- checker не є production validator, persistence schema або незалежним нормативним джерелом;
- не-нормативна оцінка загальної foundation-готовності з Accepted OCP-015 — **≈52%**.

Детальна не-нормативна оцінка та послідовність робіт наведені в [Foundation Roadmap](backlog/roadmap.md).
