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
- OCP-011 `0.3.0 / Accepted` реалізує AD-006C outcome R3 через governed `OutcomeAssessmentRecord`, а не fundamental Result Concept, і виконує першу AD-012B activation;
- OutcomeAssessmentRecord invokes `P-001@0.1.0`, exact-bind-ить Objective target, assessment kind, criterion, Event/ObservationRecord evidence, immutable evidence/input snapshots, evaluator, evaluation and recording time, conclusion та provenance;
- fail-safe matrix дозволяє definitive conclusion лише для `evidence_state: sufficient`; missing, stale, ambiguous або conflicting evidence дозволяє лише `indeterminate`;
- checker механічно виводить `missing` і finite `conflicting` probe; для exact `objective-achievement@2` OCP-011 додатково exact-bind-ить criterion-local F1/A1 rules, виводить freshness та reference/temporal ambiguity, а для semantic ambiguity зберігає attributable basis;
- `objective-achievement@1`, `holder-capability@1` і всі інші неактивовані consumers лишаються під F0/A0; одна activation не створює global evidence lifetime, freshness field або успадкованого rule;
- OCP-012 `0.3.0 / Accepted` реалізує AD-013B через unified `holder-capability@2`, explicit declaration/evidence modes, forward-only same-kind transition та OCP-012-local F1/A1 source-use rules;
- explicit supersession зберігає history, дозволяє branching і не може змінити assessment kind, target або criterion binding identity; newest record, evaluator count і list order не визначають authority;
- integrated scenario використовує нормативний OCP-011 record contract і продовжує механічно доводити `Completed ≠ achieved`;
- AB-056 завершено рішенням Architecture Board по PR-0013;
- фундаментальний `Result` відхилено AD-006C і видалено з active Concept registry та generated Foundation map без переходу в Accepted, Deprecated або Archived;
- вісь AD-006 завершена: occurrence Event + attributable ObservationRecord + governed OutcomeAssessmentRecord;
- OCP-009 визначає reusable Capability definition, governed namespace ownership, exact-version resolution і supersession без holder claims;
- AD-007C обрав single CapabilityClaimRecord direction; OCP-012 `0.3.0 / Accepted` реалізує її як governed non-Concept record contract без нового graph edge;
- CapabilityClaimRecord exact-bind-ить Resource, OCP-009 Capability version, claimant, governed claim kind, condition set, authority, evidence/support, time та provenance; activated evidence-backed mode додатково exact-bind-ить source use, F1/A1 rules і immutable rule inputs;
- withdrawal не дорівнює negative claim; branching, stale/conflicting support і unresolved inputs fail safe без newest/order/count authority;
- AD-008C приймає Model A як напрямок AB-011: deterministic directional eligibility з consumer-owned exact requirement; matching claims не створюють Resource equality, а admissibility, availability, authorization, selection і Assignment execution лишаються окремими шарами;
- OCP-013 `0.2.0 / Accepted` визначає exact consumer requirement, directional eligibility, fail-safe claim/Constraint bindings, rule-version replay та executable evidence для всіх AD-008 §12 counterexamples;
- OCP-014 `0.2.0 / Accepted` активує exact governed owner `ocp-coordination-consumer@0.1.0` для одного contextual requirement, fail-safe wrong-owner binding і окрему actor-authorization boundary без workflow authority;
- AD-009 і OCP-015 `0.2.0 / Accepted` визначають окремі immutable proposal/response records, exact-revision confirmation та fail-safe evidence projection без authorization, selection або Assignment mutation;
- OCP-004 `0.8.0` визначає plural Objective references, fail-safe exact-binding explicit intent і zero/one/many Operation-local spatial bindings з exact opaque profile/payload snapshots;
- spatial binding має identity лише в межах owning Operation, не є Operational Area Concept або P-001 record і не створює Resource equality, Assignment, overlap consequence, coordination, suitability, authorization чи Readiness;
- reference checker перевіряє fixtures, lifecycle projections, exact-version evaluation, Operation intent/spatial evidence, Capability registry resolution, Event/Observation references, OutcomeAssessmentRecord, accepted Coordination workflow evidence, integrated scenario, Concept status synchronization і dependency graph;
- assessment module має власний exact `assessment-rules.yaml` manifest за чинним module-manifest precedent;
- artifact-governance slice перевіряє global uniqueness primary OCP/Pattern/AD/ADR/AB identifiers, taxonomy statuses, exact-resolvable non-duplicate `Depends-On`, accepted AD↔AB synchronization, global rule-manifest IDs/source bindings і `Uses-Patterns` за політикою `track-current`;
- post-factum process audit перевіряє повну Git-історію після governed legacy baseline і fail-closed для shallow, malformed або unreachable evidence;
- GitHub Actions запускає unit tests, fixture validation і перевірку фактичного proposed head у `main`-контексті;
- AD-011 `0.3.0 / Accepted` окремо приймає S0 і R0 no-new-authority controls; State та Readiness deregistered як Concept candidates після negative current-scope identity verdicts, а R1 лишається окремо gated future direction;
- AD-014B `0.3.0 / Accepted` обирає Operation-local spatial binding; OCP-004 `0.8.0` реалізує exact local profile/snapshot envelope, завершує AB-008 і видаляє temporary Operational Area marker без нового Concept чи graph edge;
- AD-015B `0.3.0 / Accepted` обирає C3 (`G2 × H2`) для Core Boundary: один primary semantic-authority route, orthogonal Pattern form route і human-readable OCP-001/OCP-016 ownership split;
- OCP-001 `1.0.0 / Canonical` визначає mandatory Core Boundary trigger і governance choreography, а OCP-016 `1.0.0 / Canonical` стабілізує Routes F/C/E/D/I без self-approval, admission registry, numeric score, P-002 або machine authority; AB-061 Resolved;
- AD-016B `0.3.0 / Accepted` обирає R4 (`F → C`) та L2, обмежує current preparation окремими T0–T3 enabling cycles і вимагає AD-016C reassessment + AD-016D Board selection перед T4; сам акт не змінює OCP/Concept/Pattern status або `1.0.0`;
- T0 встановлює OCP-000 `1.0.0 / Canonical` як стабільний Concept registry contract, замінює двозначний `Operational Space First` на `Explicit Operational Context` і не змінює статус жодного Concept або graph edge;
- T1 встановлює OCP-016 `1.0.0 / Canonical` як стабільний routing contract, exact-anchor-ить reviewed baseline і не переносить OCP-000 Concept-row status у route selection;
- T2 встановлює OCP-001 `1.0.0 / Canonical` як стабільний governance contract, інкорпорує L2, R4/atomicity/non-transfer boundaries і додає fail-safe structural witness без дублювання OCP-016 routes;
- перший T3 act встановлює OCP-002 `1.0.0 / Canonical` як exact Concept-status projection contract; category/subtype/decomposition views явно ненормативні, а extra projection fail-safe відхиляється;
- окремий T3 act приймає P-001 `0.1.0 / Accepted` без зміни §§1–10 або invoker versions; шість primary contracts лишаються exact-bound, Pattern не стає Canonical і не переносить доменну семантику;
- AD-016C `0.4.0` recompute-ить post-enabling readiness: OCP-009 Capability є єдиним T4 кандидатом без current B-item, G2 micro-waves inside C — провідна гіпотеза, але окремий AD-016D Board act ще обов'язковий;
- AB-011 / AD-008 Resource interchangeability, AB-003 consumer profile та AB-058 workflow-evidence scope завершено через Accepted OCP-013–OCP-015; залишкові visibility-policy та agreement-semantics питання обліковуються окремо в AB-059;
- checker не є production validator, persistence schema або незалежним нормативним джерелом;
- reference suite містить 115 non-sensitive fixtures і 161 unit tests;
- не-нормативна оцінка загальної foundation-готовності після завершення T0–T3 enabling phase — **≈67%**; AD-016C не підвищує lifecycle readiness сам по собі, а окремий AD-016D Board act лишається обов'язковим перед T4.

Детальна не-нормативна оцінка та послідовність робіт наведені в [Foundation Roadmap](backlog/roadmap.md).
