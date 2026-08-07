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

- Capability, Objective та Resource мають статус `Canonical`; Operation, Assignment, Constraint, Organization та Event лишаються `Accepted`;
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
- OCP-004 `0.8.2` визначає plural Objective references, fail-safe exact-binding explicit intent і zero/one/many Operation-local spatial bindings з exact opaque profile/payload snapshots; два current Objective labels синхронізовано з Canonical status без зміни Operation semantics;
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
- AD-016D `0.5.0` обирає G2 всередині C/L2 і дозволяє підготовку лише окремого OCP-009 T4 draft; merge цього draft, інші T4 кандидати та другий micro-wave потребують власних Board gates;
- перший T4 act встановлює OCP-009 і Capability `1.0.0 / Canonical` та атомарно оновлює OCP-000/OCP-002 до `1.1.0`; exact definition identity/resolution, non-redirecting supersession, domain admission boundary і всі non-equivalence rules зберігаються без consumer rebinding;
- AD-016 `0.6.1` зберігає прийнятий AD-016E J8 scope і передає active AB-063 ownership до AD-017 без promotion authority; жоден другий T4 candidate ще не готовий або авторизований;
- OCP-008 `1.0.0 / Canonical` стабілізує AD-017B A+D: будь-яка зміна stored normative statement створює новий Objective, display лишається implementation-local, duplicate identity відхиляється, а old Operation/assessment exact-bind prior Objective; lifecycle, hierarchy, amendment, display та advanced assessment extensions лишаються окремо routed;
- AD-016F `0.7.0` заново обчислює Objective B/S/C на exact post-implementation baseline: B-item закритий, S-exclusions і C-cleanup обмежені, K8 є лише провідною гіпотезою; окремий AD-016G Board act обов'язковий до будь-якого другого T4 draft;
- AD-016G `0.8.0` обирає K8 як scope підготовки одного OCP-008/Objective lifecycle draft з atomic projections і bounded OCP-004 `0.8.1` cleanup; сам selection act не змінює жодного status і не авторизує merge draft;
- AD-016H `0.9.0` фіксує preflight stop через два stale Capability status views і обирає окремий Q1 correction PATCH; OCP-003 `0.6.1` та OCP-004 `0.8.1` виправляють лише ці current labels без semantic/status/dependency змін, після чого K8 може бути заново обчислений на новому baseline;
- другий T4 act встановлює OCP-008/Objective `1.0.0 / Canonical`, атомарно оновлює OCP-000/OCP-002 до `1.2.0`, OCP-004 до `0.8.2` та current map/accounting без record migration, consumer rebinding, нового graph edge або achievement authority;
- AD-016I `0.10.0` заново оцінює remaining T4 scope: OCP-003/OCP-007 лишаються blocked, M0 — fail-safe, а M3 Resource stable-surface discovery є лише провідною гіпотезою до окремого AD-016J Board selection;
- AD-016J `0.11.0` обирає M3 лише як підготовку окремого AD-018 Resource stable-surface discovery з outcome-fair R0/RI/RE/RS/RX comparison; OCP-003/OCP-007, AB-006/AB-052 та lifecycle state не змінюються;
- AD-018 `0.1.0 / Discovery` порівнює R0/RI/RE/RS/RX на exact Resource consumer і fixture evidence; RS in-place stable kernel є лише провідною гіпотезою до окремого AD-018A Board selection, без OCP-правок або taxonomy authority;
- AD-018A `0.2.0 / Accepted` обирає RS лише як підготовку окремої OCP-003 `0.7.0 / Draft` remediation: один normative stable kernel, explicit exclusions і non-governed working catalog; OCP/Concept lifecycle та AB-006/AB-052 не змінюються;
- OCP-003 `1.0.0 / Canonical` стабілізує RS bounded Resource contract: §§1–12 positive kernel, §13 exclusions і non-governed §14 catalog; exact OCP-009 binding, `Capability ≠ Readiness`, Organization separation та directional interchangeability збережено без data migration або semantic consumer change;
- AD-016K `0.12.0 / Accepted` виконує fresh post-remediation Resource audit: current semantic B-item у bounded kernel не виявлено, N3 ten-file lifecycle proposal є лише рекомендацією, а AD-016L лишається окремим Board gate;
- AD-016L `0.13.0 / Accepted` обирає N3 лише як підготовку exact ten-file OCP-003/Resource governance-lifecycle proposal з трьома consumer status-view PATCHes; жоден status у selection act не змінюється;
- третій T4 act встановлює OCP-003/Resource `1.0.0 / Canonical`, атомарно оновлює OCP-000/OCP-002 до `1.3.0`, OCP-004 до `0.8.3`, OCP-005/OCP-006 до `0.2.3` та current map/accounting; OCP-007, AB-006/AB-052, fixtures, checker і Resource operational lifecycle не змінюються;
- AD-016M `0.14.0 / Accepted` заново оцінює post-Resource remaining-T4 boundary: OCP-007 є єдиним T4 кандидатом, але continuity, classification, class/type та scheme/exception authority лишаються B; O7D є лише discovery-рекомендацією до окремого AD-016N Board selection;
- AD-016N `0.15.0 / Accepted` обирає O7D лише як підготовку окремого outcome-fair AD-019 Organization stable-surface discovery; selection не редагує OCP-007, не обирає semantic outcome, не вирішує Organization backlog і не відкриває T5;
- AD-019A `0.2.0 / Accepted` обирає Q2 (`H2 + C2 + K3 + T2 + S1 + E1 + Y1 + R1 + U0 + M0`) лише як напрям підготовки одного OCP-007 `0.4.0 / Draft` remediation: одна human-readable authority з двома bounded surfaces, exact kind-profile envelope, fail-safe identity/record resolution і explicit composition/mapping exclusions; implementation та lifecycle лишаються окремими воротами;
- OCP-007 `0.4.0 / Draft` реалізує Q2 як дві читабельні поверхні під одним власником: exact Organization identity з unresolved material-event continuity та optional opaque classification, а також локальний OrganizationRelationshipRecord з exact external kind-profile envelope, scope-local structural partitions, unconditional multiple-superior rejection і history-only branching supersession без registry, mapping або head election;
- AD-016O `0.16.0 / Accepted` виконує fresh post-Q2 Organization audit: current semantic B-item у bounded compatibility promise не виявлено, O7C seven-file lifecycle proposal є лише рекомендацією, а AD-016P лишається окремим Board gate;
- AD-016P `0.17.0 / Accepted` незалежно закриває п'ятнадцять commissioned targets негативно, але target 12 позитивно виявляє live eighth lifecycle projection у checker guide; O0 обрано як hold, exact seven-file O7C відхилено без implied expansion, і жоден lifecycle/topology proposal не авторизовано;
- AD-016Q `0.18.0 / Accepted` виконує повний read-only exact-head audit усіх current Organization lifecycle projections: вісім projection-bearing/current-roadmap файлів плюс AB-062 accounting утворюють evidence-only candidate U9; OCP-005 §4 містить stale `Organization: Proposed` проти registry `Accepted` і потребує окремого repair act, outcome не обрано, O0 лишається чинним, а lifecycle/topology proposal не авторизовано;
- AD-016R `0.19.0 / Accepted` rule-based audit виявляє шість stale registered-Concept views у current peer tables OCP-005/OCP-006 і обирає O7V лише як підготовку окремого synchronization-and-guardrail PATCH; O0 лишається Organization lifecycle-рішенням, а implementation і post-repair comparison мають власні exact-head gates;
- O7V peer-status synchronization PATCH встановлює OCP-005/OCP-006 `0.2.4 / Draft`, синхронізує шість registered-Concept rows з OCP-000 і додає bounded `STATUS_PEER_VIEW_MISMATCH` guardrail без lifecycle або semantic authority; O0 лишається чинним до fresh post-repair Board comparison;
- AD-016S `0.20.0 / Accepted` заново перевіряє post-O7V evidence: усі governed peer rows синхронізовані, rule-based sweep незалежно виводить exact nine-file O9C candidate і не демонструє tenth current Organization projection; O9C є лише рекомендацією до окремого AD-016T Board selection, O0 лишається чинним;
- AD-016T `0.21.0 / Accepted` незалежно повторює projection/consumer/non-Markdown sweep і всі sixteen targets та обирає O9C лише як підготовку exact nine-file OCP-007/Organization lifecycle proposal; selection не змінює status і не переносить merge authority на proposal;
- AB-011 / AD-008 Resource interchangeability, AB-003 consumer profile та AB-058 workflow-evidence scope завершено через Accepted OCP-013–OCP-015; залишкові visibility-policy та agreement-semantics питання обліковуються окремо в AB-059;
- checker не є production validator, persistence schema або незалежним нормативним джерелом;
- reference suite містить 120 non-sensitive fixtures і 172 unit tests;
- не-нормативна оцінка загальної foundation-готовності після третього T4 micro-wave — **≈70%**; три Concepts Canonical, п’ять лишаються Accepted, а OCP-007 remediation та кожен наступний audit/lifecycle act потребують власних Board gates.

Детальна не-нормативна оцінка та послідовність робіт наведені в [Foundation Roadmap](backlog/roadmap.md).
