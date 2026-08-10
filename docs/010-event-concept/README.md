---
Document-ID: OCP-010
Title: Event Concept
Version: 0.2.1
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, OCP-008, AD-006, P-001
Uses-Patterns: P-001@0.1.0
Used-By: Operation Evidence, Objective Achievement Assessment, Coordination Model, Audit, AB-056
Defines-Concepts: Event
Concept-Depends-On: []
Concept-Status: Accepted
Last-Review: 2026-08-10
---

# OCP-010 — Event Concept

## 1. Definition

**Event** — ідентифікована occurrence або change в операційному світі, identity якої не залежить від конкретного observation, report, Operation, Objective, assessment або порядку зберігання records.

OCP-010 реалізує обраний Architecture Board outcome `E3` з AD-006C:

1. occurrence має reusable Event identity;
2. observation є окремим attributable identified record;
3. observation не є самим Event і не визначає істину автоматично.

Event може мати zero, one або many observations. Нуль observations не скасовує Event identity.

## 2. Purpose

Event надає стабільний cross-domain reference для occurrence, на яку можуть посилатися observations, Operations, evidence sets, audits та майбутні OutcomeAssessmentRecord без identity collapse.

OCP-010 відокремлює:

- occurrence від observation/report;
- Event identity від label, kind та timestamp;
- час occurrence від часу observation і recording;
- attributable assertion від authoritative truth;
- correction history від mutation;
- Event від Operation lifecycle transition;
- Event evidence від Objective achievement assessment;
- occurrence relevance від Capability, Readiness, authorization або Conflict.

## 3. Boundary

Event не є автоматично:

- ObservationRecord або report;
- evidence sufficiency decision;
- OutcomeAssessmentRecord або fundamental Result;
- Operation lifecycle transition;
- Constraint evaluation record або result;
- Conflict, Risk, State або Readiness;
- Capability claim;
- authorization, admissibility або approval;
- causal conclusion;
- aggregation of similar labels or nearby timestamps.

Створення Event record не робить кожний пов'язаний observation істинним. Створення observation не доводить occurrence або Objective achievement.

## 4. Event identity

Кожен Event має стабільний непорожній `event_id`.

`event_id` є єдиною Core identity Event. До identity не входять:

- `event_kind_ref`;
- `occurred_at`;
- human-readable description;
- Operation reference;
- observer або source;
- кількість observations;
- newest observation;
- storage position.

Два Event з однаковим kind і однаковим або близьким timestamp не є одним Event без явного identity resolution поза межами OCP-010.

OCP-010 не визначає автоматичну occurrence deduplication. Domain correlation може пропонувати candidate linkage, але не має права мовчки змінювати Event identity.

## 5. Minimal Event structure

```text
Event
- event_id
- event_kind_ref
- registered_at
- identity_provenance_ref
- occurred_at [optional]
```

### 5.1 event_id

Стабільна непорожня identity occurrence.

### 5.2 event_kind_ref

Opaque exact-version reference на governed Event kind у Core або domain namespace.

Kind допомагає інтерпретувати occurrence, але не входить до Event identity. Однаковий kind не означає однакову occurrence.

OCP-010 не визначає wire encoding exact-version reference. Reference checker використовує `identity@version` лише як checker-envelope convention.

### 5.3 registered_at

Валідний timestamp створення Event identity у governed dataset.

`registered_at` не є occurrence time і не визначає truth або precedence.

### 5.4 identity_provenance_ref

Непорожній opaque reference на act або source, який встановив Event identity у dataset.

Ця provenance забезпечує traceability identity establishment, але не є універсальною оцінкою істинності всіх observations або достатності evidence.

### 5.5 occurred_at

Опційний timestamp occurrence, якщо точний instant представлений.

Відсутність `occurred_at` не робить Event identity невалідною. OCP-010 не визначає interval, uncertainty range, timezone policy або canonical temporal model за межами валідності поданого timestamp.

## 6. ObservationRecord

**ObservationRecord** — attributable assertion, що observer або source сприйняв, виміряв чи повідомив occurrence або condition.

ObservationRecord:

- має власну identity;
- може посилатися на один Event;
- може залишатися без `event_ref`, коли occurrence linkage unresolved;
- може бути delayed, incomplete, duplicate, mistaken, conflicting або corrected;
- не стає Event через однаковий label чи timestamp;
- не визначає truth за source count, newest timestamp або list order.

Мінімальна структура:

```text
ObservationRecord
- observation_id
- observer_ref
- observation_kind_ref
- statement
- observed_at
- recorded_at
- provenance_ref
- event_ref [optional]
- supersedes_observation_ref [optional]
```

### 6.1 observation_id

Стабільна непорожня identity attributable assertion.

### 6.2 observer_ref

Непорожній opaque reference на observer, sensor, reporting source або іншу attributable source identity.

OCP-010 не визначає source reliability, trust score, authorization або qualification.

### 6.3 observation_kind_ref

Opaque exact-version reference на governed observation kind.

Observation kind не є Event kind і не створює occurrence identity.

### 6.4 statement

Змістовне assertion. Нормалізований statement містить щонайменше одну літеру або цифру.

Statement не є автоматично authoritative truth або positive achievement evidence.

### 6.5 observed_at and recorded_at

`observed_at` — timestamp сприйняття або вимірювання source.

`recorded_at` — timestamp створення attributable record.

Обидва timestamps є окремими від Event `occurred_at` та assessment `evaluated_at`. Якщо обидва представлені точно, `observed_at <= recorded_at`.

### 6.6 provenance_ref

Непорожній opaque reference на record creation source або act.

### 6.7 event_ref

Опційний exact reference на `event_id`.

Якщо `event_ref` присутній, він повинен однозначно резолвитися рівно в один valid Event у dataset. Якщо відсутній, observation залишається attributable unresolved assertion; Core не створює приховану occurrence identity з label, statement або timestamp similarity.

### 6.8 supersedes_observation_ref

Опційне посилання на попередній ObservationRecord, який corrected, amended або replaced цим record.

Supersession:

- не дозволяє self-reference;
- target повинен існувати;
- graph повинен бути acyclic;
- branching дозволений, щоб зберігати незалежні correction paths;
- prior record не мутує і залишається історичним evidence;
- newest record не стає truth автоматично;
- OCP-010 не визначає один current observation під час branching або disagreement.

## 7. P-001 authority boundary

OCP-010 invokes `P-001@0.1.0` для ObservationRecord, а не для фундаментального Event.

ObservationRecord є authoritative лише щодо attributable assertion:

> визначений observer/source створив визначене assertion у визначений час з визначеною provenance.

ObservationRecord не є authoritative щодо:

- факту occurrence;
- causal relation;
- Objective achievement;
- Operation success;
- source reliability;
- Capability, Readiness або authorization.

Event dataset є authoritative для exact `event_id` resolution. Він не обирає authoritative observation або truth projection.

## 8. Exact Event resolution

Reference derivation:

```text
resolve_event(events, event_ref)
```

Resolver повертає один valid Event, `event_id` якого exact-equal requested reference.

Malformed, missing, zero-candidate або multiple-candidate reference не дає authoritative resolution.

Resolver:

- не використовує kind;
- не використовує `occurred_at` або `registered_at` як tie-break;
- не використовує description або observation statement;
- не обирає newest record;
- не виконує fuzzy matching або deduplication.

## 9. Observation collection derivation

Reference derivation:

```text
observations_for_event(observations, event_ref)
```

Derivation повертає всі structurally valid ObservationRecord, exact `event_ref` яких дорівнює requested Event identity.

Повернення collection не означає consensus, source weighting або truth. List order не має нормативної сили.

## 10. Operation boundary

Event identity не залежить від Operation.

Один Event може бути relevant до zero, one або many Operations. Operation може завершитися без Event, якщо її domain contract це допускає, а Event може існувати поза будь-якою Operation.

OCP-010 не вводить current Concept edge `Event → Operation` або `Operation → Event`.

Operation lifecycle transition не стає Event автоматично. Domain може створити Event для independently identified occurrence, пов'язаної з transition, але transition record та Event зберігають різні identities і authority.

`Completed`, `Cancelled` або `Aborted` не є Objective achievement assessment.

## 11. Objective and assessment boundary

Event або ObservationRecord може бути evidence input майбутнього `OutcomeAssessmentRecord`, але не доводить achievement сам по собі.

Один Event може бути relevant до кількох Objective assessments. Один Objective може використовувати evidence від кількох Events і Operations.

OCP-010 не додає `achieved`, `success`, `failure` або assessment fields до Objective чи Event.

General OutcomeAssessmentRecord contract належить AB-056 і не визначається цим документом.

## 12. Constraint, Conflict and Risk boundary

Constraint evaluation record не є Event автоматично.

Constraint violation може бути evidence для domain Event або future Conflict, але:

- violation не створює Event без окремої occurrence identity;
- Event не створює Conflict або Risk автоматично;
- кілька observations або violations не агрегуються в один Event за замовчуванням;
- `indeterminate` Constraint result не стає positive Event evidence.

## 13. Capability, Readiness and State boundary

Event, ObservationRecord або positive domain finding не створює автоматично:

- Capability definition;
- holder-specific Capability claim;
- current availability;
- Readiness;
- authorization;
- admissibility;
- State.

Будь-яке таке inference потребує окремого exact, attributable і reviewed rule.

## 14. Integrated non-sensitive scenario contract

OCP-010 вводить перший integrated non-sensitive checker fixture, який поєднує:

- one Objective;
- one completed Operation, що переслідує цей Objective;
- two Resources;
- two Established Assignments;
- one applicable Constraint;
- one Event occurrence;
- two attributable conflicting ObservationRecord;
- one checker-local assessment envelope з conclusion `indeterminate`.

Scenario використовує нейтральний приклад перевірки стану generic infrastructure asset і не містить coordinates, real unit names, personal data або operationally sensitive details.

Checker-local assessment envelope існує лише для доказу AD-006 fail-safe boundary:

```text
ScenarioAssessmentEnvelope
- assessment_id
- target_objective_ref
- rule_ref
- evidence_observation_refs
- evidence_snapshot_ref
- evaluator_ref
- evaluated_at
- conclusion: achieved | not_achieved | partial | indeterminate
- provenance_ref
```

Ця envelope не є normative OutcomeAssessmentRecord contract, не invok-ить P-001 і не завершує AB-056.

Scenario validator повинен довести:

1. усі сім попередньо Accepted Concepts проходять власні чинні validators;
2. Operation `Completed` не примушує conclusion `achieved`;
3. conflicting observations залишаються видимими;
4. evidence references exact-resolve;
5. conflicting evidence не дозволяє authoritative positive conclusion;
6. Event relevance не створює Capability, Readiness, authorization або Conflict;
7. дві Assignment не collapse-яться в participation без їхніх власних identities;
8. Constraint result не стає universal Result;
9. кожний Assignment exact-reference existing Resource та scenario Operation і створює effective participation через `derived_participates_in` у evaluation time;
10. Constraint target/context references exact-resolve у scenario, а `constraint_applicable_to` та `effective_constraint_result` повертають expected governed results.

## 15. Semantic rules

1. Event identity дорівнює exact `event_id`, а не комбінації kind, label або timestamp.
2. Event може існувати з zero observations.
3. ObservationRecord є assertion, а не occurrence.
4. Similar labels, statements або nearby timestamps не створюють Event equality.
5. Source count, newest timestamp і list order не визначають truth.
6. Correction створює new ObservationRecord або explicit supersession; prior record не мутує.
7. Unresolved observation не отримує hidden occurrence identity.
8. Event не є Operation lifecycle stage або transition.
9. Event або observation не є sufficient Objective achievement evidence за замовчуванням.
10. Missing, stale, ambiguous або conflicting evidence не дає authoritative positive conclusion.
11. Event або observation не створює Conflict, Risk, Capability, Readiness, State, authorization чи admissibility.
12. Parent/child або multi-Operation Event aggregation не відбувається автоматично.

## 16. Invariants

1. Кожен Event має непорожній `event_id`.
2. `event_id` є унікальним у Event dataset.
3. `event_kind_ref` є непорожнім exact-version reference.
4. `registered_at` є валідним timestamp.
5. `identity_provenance_ref` є непорожнім opaque reference.
6. `occurred_at`, якщо присутній, є валідним timestamp; його відсутність допустима.
7. Event structure не містить embedded ObservationRecord, truth selection, source count або authoritative achievement fields.
8. Кожен ObservationRecord має непорожній unique `observation_id`.
9. `observer_ref`, `observation_kind_ref`, `statement`, `observed_at`, `recorded_at` і `provenance_ref` є структурно валідними.
10. Якщо `observed_at` і `recorded_at` представлені точно, `observed_at <= recorded_at`.
11. `event_ref`, якщо присутній, exact-resolves рівно в один valid Event.
12. Absence of `event_ref` є explicit unresolved linkage і не створює hidden Event identity.
13. `supersedes_observation_ref`, якщо присутній, посилається на existing other ObservationRecord.
14. Observation supersession graph є acyclic.
15. Duplicate Event identity або ambiguous Event reference fail closed незалежно від record order.
16. Integrated scenario з conflicting observations не може мати authoritative positive assessment conclusion.
17. Integrated scenario Assignment references exact-resolve до scenario Resource та Operation і є effective у scenario evaluation time.
18. Integrated scenario Constraint target/context references exact-resolve, а applicability/effective-result derivations не можуть бути замінені декоративними fixture fields.

Інваріанти 2, 11, 13–18 є dataset-level або scenario-level.

## 17. Executable evidence

Reference checker повинен містити щонайменше:

- valid Event з zero observations;
- two observations referencing one Event without observation identity collapse;
- two Events with equal kind and timestamp that remain distinct identities;
- duplicate Event identity fixture, order-independent and fail-closed;
- unresolved Event reference fixture;
- ObservationRecord without `event_ref`, що залишається valid unresolved assertion;
- invalid observation time order;
- observation self-supersession and supersession-cycle fixtures;
- conflicting observations that remain simultaneously visible;
- integrated neutral scenario with completed Operation and `indeterminate` assessment;
- negative integrated scenario where conflicting evidence attempts `achieved` and fails closed;
- negative integrated scenario with dangling Assignment reference;
- normalization regression for whitespace-equivalent Event and Observation references.

Кожен emitted validation code входить до `ERROR_CODES`, має source у `rules.yaml` і бере участь в exact manifest equality. `resolve_event` та `observations_for_event` входять до `DERIVATION_RULES`.

## 18. Examples

### Example A — zero observations

Event `EV-001` має governed identity та може бути referenced audit record до появи attributable observations. Empty observation collection не видаляє або invalid-ує Event.

### Example B — conflicting observations

Observation `OBS-001` і `OBS-002` exact-reference `EV-002`, але містять несумісні assertions. Обидва records залишаються видимими; newest або source count не визначає truth.

### Example C — equal timestamps, distinct Events

`EV-010` і `EV-011` мають один kind та однаковий `occurred_at`. Вони залишаються двома Event, бо identity визначається `event_id`.

### Example D — unresolved observation

Observation `OBS-020` не має `event_ref`. Це не створює anonymous Event і не дозволяє correlation за label або timestamp.

## 19. Non-examples

Не є Event самі по собі:

- lifecycle transition record;
- Constraint evaluation result;
- observation або report;
- log line без occurrence identity;
- human-readable label + timestamp;
- KPI measurement;
- software function return;
- Objective achievement assessment;
- absence of negative evidence;
- inferred Conflict без окремого normative model.

## 20. P-001 conformance for ObservationRecord

### 20.1 Required elements

- stable record identity: `observation_id`;
- semantic owner: OCP-010 §§6–20;
- endpoint contract: optional directed `event_ref` from ObservationRecord to Event; absence explicitly means unresolved occurrence linkage;
- governed kind: exact-version `observation_kind_ref`;
- provenance: `observer_ref`, `observed_at`, `recorded_at`, `provenance_ref`;
- validation: invariants 16.8–16.18 and executable fixtures in §17;
- authority: ObservationRecord is authoritative only for attributable assertion, never occurrence truth or achievement.

### 20.2 Selected Optional Module C — Supersession

- superseded reference: `supersedes_observation_ref`;
- self-supersession: prohibited;
- target existence: required;
- acyclicity: required;
- branching: allowed;
- overlap and gaps: allowed because Module A is not selected;
- authoritative record during overlap: no automatic current/truth selection is defined;
- replacement provenance: provenance of successor ObservationRecord;
- prior history: preserved and never rewritten.

Modules A and B are intentionally not selected. Observation timestamps describe observation and recording, not record temporal effectivity or lifecycle.

## 21. Explicitly not defined

OCP-010 свідомо не визначає:

- canonical Event taxonomy;
- truth, confidence, trust або source-reliability scale;
- occurrence deduplication або entity resolution algorithm;
- causal inference;
- event interval або uncertainty representation;
- automatic Event creation from lifecycle or Constraint records;
- Operation-to-Event relationship record;
- Objective achievement semantics;
- normative OutcomeAssessmentRecord contract;
- Result registry resolution;
- Conflict, Risk, State або Readiness model;
- Capability claim rule;
- authorization, approval або admissibility;
- database, API, UI, transport або message schema.

## 22. Open questions and resolved boundaries

- Чи потребує Event окремого temporal interval module після появи canonical time model?
- Який normative owner визначить Operation-to-Event relationship record, якщо direct references стануть недостатніми?
- Які domain correlation rules можуть пропонувати candidate Event linkage без зміни Core identity?
- Чи потрібна governed Event-kind registry або достатньо exact domain references?
- ~~Як AB-056 визначить allowed assessment targets, conclusions, supersession та authority?~~ OCP-011 §§2–8 приймає exact target/criterion/evidence/input/evaluator/time/provenance bindings, bounded conclusions і history-preserving supersession without generic assessment authority.

## 23. External review target

Attempt to falsify OCP-010 with cases where:

1. Event silently collapses into observation;
2. zero-observation Event becomes invalid;
3. equal kind/timestamp collapses Event identities;
4. newest observation or source count selects truth;
5. unresolved observation manufactures hidden occurrence identity;
6. correction mutates prior attributable evidence;
7. lifecycle transition or Constraint result becomes Event automatically;
8. Event implies Objective achievement, Capability, Readiness або Conflict;
9. P-001 invocation omits endpoint, provenance, authority або supersession obligations;
10. integrated scenario cannot reuse current Concept validators and derivations;
11. checker-local assessment envelope silently becomes the normative AB-056 contract;
12. current Concept graph gains an unjustified cycle.

## 24. Architecture Board decision — PR-0012

Architecture Board прийняла OCP-010 і Concept `Event` **4 серпня 2026 року** після повторного зовнішнього review head `7f00bb0`, яке підтвердило закриття findings F1–F2, відповідність outcome E3 у AD-006C та виконуваність інтегрованого non-sensitive scenario.

Рішення Board:

- прийняти occurrence-layer Event identity та governed ObservationRecord contract, визначені OCP-010;
- встановити `Concept-Status: Accepted` на версії `0.2.0`;
- завершити AB-055 як `Resolved`;
- зберегти Event як isolated Concept без current dependency edge;
- прийняти zero-observation validity, exact `event_id` resolution, відсутність automatic dedup/latest-truth та history-preserving ObservationRecord supersession з дозволеним branching;
- прийняти інтегрований scenario як перший наскрізний виконуваний доказ композиції восьми Accepted Concepts, де з'єднання перевіряються чинними `derived_participates_in`, `constraint_applicable_to` та `effective_constraint_result` derivations;
- не вводити Operation-to-Event relation, truth/consensus model, normative OutcomeAssessmentRecord, fundamental Result, Conflict, Risk, State, Readiness, Capability claim, authorization або production schema;
- залишити AB-056 окремим наступним normative cycle для OutcomeAssessmentRecord та атомарної резолюції registry entry `Result`.

`Accepted` не означає `Canonical`. Подальші зміни Event identity, ObservationRecord authority, supersession contract або occurrence/observation boundary потребують нового явного normative cycle.

## 25. PATCH accounting — v0.2.1

Revision `0.2.1` synchronizes the fifth §22 prompt with Resolved AB-056 and the Accepted OCP-011 contract. It keeps the original question visible as a struck historical prompt and adds the exact current owner rather than deleting evidence of the earlier boundary.

The first four questions remain open because AB-055 accepted Event/ObservationRecord identity and evidence only; it did not select a canonical time model, Operation-to-Event relation owner, domain correlation rule or Event-kind registry.

This PATCH changes no Event or ObservationRecord identity, structure, lifecycle, derivation, Concept status, dependency, graph edge, P-001 invocation, checker behavior, rule manifest or fixture.
