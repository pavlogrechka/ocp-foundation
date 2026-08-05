---
Document-ID: OCP-004
Title: Operation Concept
Version: 0.8.2
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-008, AD-014
Used-By: Assignment Concept, Operation Lifecycle, Coordination Model, Business Rules, Domain Model
Defines-Concepts: Operation
Concept-Depends-On: [Objective]
Concept-Status: Accepted
Last-Review: 2026-08-06
---

# Operation Concept

## 1. Definition

**Operation** — ідентифікована, цілеспрямована та обмежена контекстом операційна діяльність, яка створює спільний контекст для участі Resource, координації, обмежень, подій і результатів.

Operation є універсальним Concept для представлення координованої діяльності незалежно від предметної спеціалізації.

Місія БпС, операція РЕБ, розвідувальна або логістична дія можуть бути предметними спеціалізаціями Operation. Їхні спеціальні правила визначаються відповідними domain або capability modules і не входять до Core Operation автоматично.

## 2. Purpose

Operation є центральним контекстом, у якому OCP пов’язує:

- операційний намір і Objective;
- Resource та Assignment;
- планові й фактичні часові межі;
- нуль, одну або кілька локальних просторових прив’язок;
- Constraint;
- координаційні зв’язки;
- Event та окремі outcome assessments.

Operation дає змогу відповісти на питання: **що виконується, навіщо, де, коли, ким, за яких умов і з яким результатом**.

## 3. Scope

Operation описує координовану операційну діяльність як ціле.

Operation не визначає сама по собі:

- штатну або командну належність Resource;
- повноваження користувача інформаційної системи;
- технічну конфігурацію предметного засобу;
- детальні правила конкретного domain або capability module;
- готовність чи доступність Resource;
- джерело повноваження або процедуру погодження;
- модель доступу до даних.

Моделі командних повноважень, наказів, погоджень і політик будуть визначені окремо після явного рішення Architecture Board.

## 4. Concept Status and Dependencies

`Operation` має статус `Accepted` у реєстрі OCP-000 на підставі рішення Architecture Board про схвалення PR-0003.

Цей документ використовує такі зареєстровані Concept:

| Concept | Status | Використання в OCP-004 |
|---|---|---|
| Resource | Accepted | елемент, що залучається до Operation |
| Assignment | Accepted | авторитетний контекст участі Resource; OCP-005 |
| Objective | Canonical | intended outcome, condition або effect; OCP-008 |
| Constraint | Accepted | обмеження Operation та Assignment; OCP-006 |
| Event | Accepted | значущий occurrence або change; OCP-010 |
| Order | Proposed | можливе джерело авторизації; не визначене цим документом |
| Coordination | Proposed | модель взаємодії між Operation |
| Capability | Canonical | reusable definition layer; OCP-009 |
| Readiness | не зареєстрований окремо | AD-011 R0; не виводиться з Operation |
| State | не зареєстрований окремо | AD-011 S0; lifecycle Operation не є shared State |

`OutcomeAssessmentRecord` за OCP-011 може оцінювати exact Objective, але не є Concept, дочірнім об’єктом Operation або полем її успіху. Фундаментальний `Result` відхилено AD-006C.

Правила, що залежать від Concept у статусі `Proposed`, є робочими й підлягають уточненню у відповідних специфікаціях. Цей документ не передає нормативну відповідальність незареєстрованим поняттям; описові слова `state`, `readiness`, `area` або `environment` не створюють shared authority.

## 5. Identity

Кожна Operation має власну стабільну ідентичність, незалежну від назви, класифікації, шаблону або повторюваності.

Дві Operation з однаковою метою, районом і складом учасників залишаються різними, якщо вони створені як окремі заплановані або фактичні виконання.

Шаблон операції не є Operation. Шаблон може бути джерелом початкових даних, але не представляє окрему заплановану чи фактичну діяльність.

## 6. Working Structure

Робоча структура Operation використовує лише зареєстровані Concept і внутрішні властивості Operation:

```text
Operation
├── Identity
├── Intent
│   └── Objective [Canonical]
├── Temporal Context
│   ├── Planned Bounds
│   └── Actual Bounds
├── Spatial Context
│   └── Local Spatial Binding [Operation-owned structure]
├── Participation
│   └── Assignment [Accepted]
├── Constraints
│   └── Constraint [Accepted]
└── Outcome
    ├── Event [Accepted]
    └── OutcomeAssessmentRecord [Accepted record contract; not a Concept]
```

Назви `Intent`, `Temporal Context`, `Spatial Context`, `Participation`, `Constraints` і `Outcome` у цій структурі є секціями моделі Operation, а не автоматично окремими фундаментальними Concept.

Не всі елементи мають бути повністю визначені під час створення Operation. Мінімальна повнота залежить від lifecycle stage і буде формалізована окремими правилами.

## 7. Intent and Objective

Operation має рівно одне активне представлення операційного наміру поза lifecycle stage `Draft`:

1. один або більше `objective_refs`, кожен з яких однозначно резолвиться у валідний Objective за OCP-008; або
2. один локальний `ExplicitIntentRecord` з авторитетним immutable validation evidence за цим розділом.

```text
Operation pursues Objective
```

Objective описує intended outcome, condition або effect і не дорівнює самій Operation. Нормативна семантика Objective визначена в [OCP-008 — Objective Concept](../008-objective-concept/README.md).

### 7.1 Semantics of plural `objective_refs`

`objective_refs` є списком непорожніх унікальних Objective identifiers. Кожен член списку є незалежним affirmative-твердженням, що ця Operation переслідує відповідний Objective. Усі перелічені Objective активні для snapshot; список не означає вибір будь-якого одного Objective як достатнього.

Для Operation поза `Draft` кожен identifier повинен резолвитися рівно в один валідний Objective instance. Один валідний елемент не компенсує нерезолвлений, неоднозначний або невалідний інший елемент.

Сам факт членства у списку не кодує:

- priority або weighting;
- sequencing або dependency;
- hierarchy або decomposition;
- contribution strength;
- equivalence між Objective;
- aggregation achievement, success або completion.

Domain або Coordination rules можуть додавати явні структури для цих семантик, але не можуть мовчки переінтерпретувати bare `objective_refs`. Альтернативне переслідування потребує окремо визначеного явного представлення.

### 7.2 Explicit intent record

Рішення AD-004C не вводить окремий фундаментальний Concept `Operational Intent`. Локальний `ExplicitIntentRecord` залишається Operation-owned fallback-структурою:

```text
ExplicitIntentRecord
- intent_id
- intent_version_ref
- statement
- validation_rule_ref
- input_snapshot_ref
- validation_status: not_evaluated | passed | failed  # optional derived projection
- validation_records:
  - validation_id
  - intent_version_ref
  - validation_rule_ref
  - input_snapshot_ref
  - evaluated_at
  - evaluator_ref
  - result: not_evaluated | passed | failed
```

`intent_version_ref` та `validation_rule_ref` є непрозорими exact-version references. Кожне посилання повинно однозначно розрізняти identity та immutable version; нормативна модель не приписує delimiter або wire encoding. `input_snapshot_ref` непрозоро ідентифікує точний evaluated input snapshot.

Нормалізований `statement` повинен містити щонайменше один символ літери або цифри. Значення, що складаються лише з пробілів, розділових знаків або службових заповнювачів, не є валідним statement.

Для використання explicit intent поза `Draft` має існувати один або більше структурно валідних validation records, які одночасно збігаються з поточними:

1. `intent_version_ref`;
2. exact-version `validation_rule_ref`;
3. `input_snapshot_ref`.

Усі records із цим exact binding утворюють effective evidence set. Evidence є однозначним, якщо всі exact-binding records мають один і той самий `result`. Повторні immutable records з однаковим result є допустимими; порядок списку та `evaluated_at` не обирають авторитетний record. Якщо exact-binding records містять різні results, evidence є conflicting.

Кожен record повинен містити валідні `validation_id`, `evaluated_at`, `evaluator_ref` і `result`. Non-Draft explicit-intent branch є валідною лише тоді, коли effective evidence set дає один однозначний `result = passed`.

`intent_version_ref` позначає immutable version усього binding-relevant змісту explicit intent, включно зі `statement`. Будь-яка substantive зміна statement або іншої binding-властивості, версії validation rule чи evaluated input snapshot повинна створювати нову version/reference value та інвалідовує попередній `passed`. Повторне використання старого version token після зміни змісту порушує цю semantic rule незалежно від того, чи здатний reference checker виявити таке зловживання.

Missing, stale, conflicting або structurally invalid evidence не задовольняє intent invariant і fail-safe робить non-Draft Operation невалідною.

`validation_status`, якщо матеріалізований, є лише derived non-authoritative projection. Якщо effective evidence set має один однозначний result, projection повинна дорівнювати цьому result. Якщо однозначного effective result немає через missing, stale, conflicting або structurally invalid evidence, нормативна projection дорівнює `not_evaluated`; матеріалізований `passed` або `failed` є mismatch. Stored `passed` без точного evidence binding або всупереч evidence не має нормативної сили.

Змістовні критерії достатності визначаються domain validation rule, але validation не означає authorization, approval або command authority.

### 7.3 Coexistence and precedence contract

На stage `Draft` `objective_refs` і `ExplicitIntentRecord` можуть тимчасово співіснувати як authoring state. Жодне представлення не має автоматичного пріоритету, а Draft може не мати жодного з них. Draft також може містити неповний або ще не evaluated explicit-intent record.

Поза `Draft` співіснування заборонене: Operation повинна обрати рівно одну активну гілку. Якщо присутні і `objective_refs`, і `ExplicitIntentRecord`, snapshot є невалідним незалежно від змістовної узгодженості між ними.

Перехід від `ExplicitIntentRecord` до Objective не є автоматичною promotion. Objective створюється як окремий instance з власною identity та provenance, після чого активний snapshot Operation перемикається на `objective_refs`. Попередній explicit intent може зберігатися лише в audit history поза активними intent fields і не має нормативного пріоритету над Objective.

Operation може існувати без валідованого активного наміру лише на lifecycle stage `Draft`.

## 8. Temporal Context

Operation має плановий і, після початку виконання, може мати фактичний часовий контекст.

Планові й фактичні часові твердження повинні зберігатися окремо та мати явний тип:

```text
planned_start
planned_end
actual_start
actual_end
```

Ці властивості не створюють окремий Concept `Time Interval`. Остаточна модель часу буде визначена окремо.

## 9. Spatial Context

AD-014B обрав найменшу достатню модель: Operation може мати **нуль, одну або багато локальних просторових прив’язок**. Така прив’язка є versioned structured value всередині exact Operation snapshot, а не окремим `Operational Area` Concept, P-001 record, Resource чи graph node.

```yaml
spatial_context:
  context_version_ref: OP-001-SPATIAL@2
  bindings:
    - binding_id: LOCAL-WORK-AREA
      binding_version_ref: LOCAL-WORK-AREA@2
      purpose_ref: work-area@1
      representation_profile_ref: synthetic.opaque-spatial@1
      payload_snapshot_ref: SYNTH-SPATIAL-SNAPSHOT-A@2
      temporal_scope: planned-context
      provenance_ref: ACT-SPATIAL-BINDING-002
```

`binding_id` має identity лише в межах owning Operation. Нормативний subject прив’язки — пара `(operation_id, binding_id)`; однакові локальні IDs, labels, payloads, footprints або geometries у різних Operation не створюють reusable area identity, equality чи cross-Operation relation.

`context_version_ref` exact-bind-ить увесь активний spatial context Operation. `binding_version_ref` exact-bind-ить binding-relevant зміст конкретної локальної прив’язки. `purpose_ref` є exact profile-owned кодом призначення, наприклад synthetic `work-area@1` або `transit-corridor@1`; Core не тлумачить цей код самостійно.

`representation_profile_ref` повинен однозначно резолвитися в exact domain-owned profile з явним owner. `payload_snapshot_ref` повинен однозначно резолвитися в immutable snapshot з тим самим exact profile, opaque versioned payload reference і provenance. Core валідовує binding/profile/snapshot envelope, але не координати, geometry, CRS, topology, overlap або containment. Fixture-синтаксис `identity@version` є serialization convention checker-а, а не обов’язковим wire format продукту.

```yaml
spatial_representation_profile:
  profile_ref: synthetic.opaque-spatial@1
  profile_owner_ref: domain://synthetic-spatial
spatial_payload_snapshot:
  snapshot_ref: SYNTH-SPATIAL-SNAPSHOT-A@2
  representation_profile_ref: synthetic.opaque-spatial@1
  opaque_payload_ref: synthetic://spatial-payload/a@2
  provenance_ref: ACT-SPATIAL-PAYLOAD-002
```

Непорожній `profile_owner_ref` забезпечує attribution, але сам по собі не доводить legitimate authority. Її повинен прийняти exact consumer/domain contract і зовнішній review; checker не автентифікує owner і не обирає його з кількох кандидатів.

`temporal_scope` має одне з трьох значень:

- `operation-context` — прив’язка стосується exact owning Operation snapshot без окремого planned/actual твердження;
- `planned-context` — прив’язка стосується планового контексту і потребує `planned_start` у тому самому Operation snapshot;
- `actual-context` — прив’язка стосується фактичного контексту і потребує `actual_start` у тому самому Operation snapshot.

Відсутність `spatial_context` або порожній `bindings` є валідним zero-binding станом. Просторова присутність не є універсальною умовою навіть поза `Draft`; конкретний consumer або domain rule може вимагати її лише у власному exact contract.

OCP-004 володіє membership локальної прив’язки в одному Operation context і вибором exact active versions. Domain profile володіє лише інтерпретацією opaque payload. Жоден із цих власників не отримує права виводити cross-Operation spatial identity чи cross-profile equivalence.

Zero або multiple exact profile/snapshot resolutions, unknown profile, profile mismatch, incomplete binding, duplicate local binding, missing matching temporal context чи заборонене semantic coupling роблять spatial envelope non-permissive. Checker не обирає authority за newest timestamp, storage order, source count, issuer count, label similarity або payload similarity.

Substantive зміна context або binding вимагає нових exact version references. Попередній Operation snapshot і його payload snapshot зберігаються в audit history; поточні поля не переписують минулі evidence. Outcome A не вимагає stored withdrawal/supersession lineage: якщо binding потребує independent reference, correction history або lifecycle поза owning Operation, реалізація повинна зупинитися й reopen Outcome B за AD-014 §32.

Просторова прив’язка не створює Assignment, Resource identity/equality, Organization relation, coordination, conflict, visibility, overlap consequence, suitability, admissibility, availability, authorization, selection або Readiness. Маршрут, точка, area чи opaque payload без операційного наміру самі по собі не є Operation.

## 10. Participation and Assignment

Авторитетна участь Resource в Operation представляється через Assignment, модель якого визначена в [OCP-005 — Assignment Concept](../005-assignment-concept/README.md).

```text
Assignment assigns Resource to Operation
```

Кожен Assignment пов’язує рівно один Resource з рівно однією Operation, має власну ідентичність, RoleSpecification, applicability interval та lifecycle record.

Нормативні правила часової чинності `assignment_effective_at` і участі `derived_participates_in` визначені лише в OCP-005 §§8–9. Цей документ не повторює їхню формулу.

Окремий авторитетний зв’язок `Resource participates_in Operation` або `Operation uses Resource` у Core не зберігається незалежно від Assignment.

Assignment до parent Operation не створює Assignment до child Operation. Assignment складеного Resource не створює Assignment його складових Resource.

Operation не володіє Resource і не змінює його організаційну чи командну належність.

## 11. Relationships

### 11.1 Core working relationships

```text
Operation pursues Objective
Operation has Assignment
Operation is_subject_to Constraint
Operation generates Event
```

Кожен Concept у цих зв’язках має статус, наведений у розділі 4.

Локальна просторова прив’язка не входить до цього списку Concept relationships. Вона належить structured spatial context owning Operation за §9 і не створює graph edge `Operation → Operational Area` або `Operation → Environment`.

### 11.2 Inter-operation relationships

```text
Operation coordinates_with Operation
Operation depends_on Operation
Operation supports Operation
Operation conflicts_with Operation
```

Ці зв’язки не виникають автоматично через просторове або часове перекриття.

Кожен збережений inter-operation relationship представляється локальним structured assertion record:

```text
InterOperationRelationshipAssertion
- source_operation_id
- relation_type: coordinates_with | depends_on | supports | conflicts_with
- target_operation_id
- provenance_ref
```

`provenance_ref` є непорожнім посиланням на правило, рішення, Event, результат обчислення або інший доказ, що пояснює встановлення зв’язку. Таке посилання не створює нового фундаментального Concept.

Точна семантика цих зв’язків і типів provenance буде визначена Coordination Model.

### 11.3 Authorization references

Operation може потребувати авторизації перед виконанням. `Order` є зареєстрованим кандидатом на одне з можливих джерел такої авторизації.

Цей документ не вводить окремі Concept `Authority`, `Approval`, `Policy` або `Governance` і не визначає їхні зв’язки з Operation.

## 12. Composition and Decomposition

Operation може бути пов’язана з іншою Operation як батьківська або дочірня:

```text
Operation contains Operation
Operation is_part_of Operation
```

Parent/child використовується лише тоді, коли дочірня Operation є частиною спільного операційного наміру і її виконання або окремо оцінений outcome впливає на батьківську Operation.

Координація між незалежними Operation не створює parent/child автоматично.

Assignment не успадковується між parent і child Operation автоматично.

Остаточні правила композиції залишаються відкритим питанням.

## 13. Working Lifecycle

Робочі lifecycle stages Operation:

```text
Draft → Planned → Authorized → Active → Completed
                         ↘ Cancelled
                         ↘ Aborted
```

Ці значення є lifecycle stages, визначеними локально для Operation. Вони не є значеннями фундаментального Concept `State`; AD-011 прийняв S0 no-shared-State control і superseded історичний ADR-DRAFT-007.

Кожна зафіксована зміна lifecycle представляється локальним structured transition record:

```text
LifecycleTransitionRecord
- from_stage
- to_stage
- occurred_at
- provenance_ref
```

`provenance_ref` є непорожнім непрозорим посиланням на Event, Order, правило, рішення, системну дію або інший доказ переходу. Вимога до `provenance_ref` перевіряє простежуваність запису, але не визначає фундаментальний Concept джерела дозволу чи переходу.

### 13.1 Draft

Operation зареєстрована, але її намір, контекст або склад можуть бути неповними.

### 13.2 Planned

Operation має мінімальний плановий контекст, достатній для перевірки та підготовки. Точні критерії переходу залишаються відкритими.

### 13.3 Authorized

Для Operation зафіксовано необхідне підтвердження дозволу на виконання відповідно до застосовних правил.

Цей stage не визначає, який саме Concept або артефакт є джерелом дозволу. Простежуваність конкретного переходу забезпечується `provenance_ref` у LifecycleTransitionRecord.

### 13.4 Active

Зафіксовано початок фактичного виконання Operation.

`Active` Operation не робить усі пов’язані Assignment ефективними автоматично: для кожного Assignment окремо застосовується temporal effectivity rule OCP-005.

### 13.5 Completed

Зафіксовано завершення фактичного виконання Operation.

### 13.6 Cancelled

Operation завершена без переходу до фактичного виконання.

### 13.7 Aborted

Operation припинена після початку фактичного виконання або через неможливість продовження.

Можливий stage `Suspended` не вводиться цим документом. Остаточна state machine буде винесена до окремого Operation Lifecycle contract; вона не створюватиме shared State abstraction без reopening evidence за AD-011.

## 14. Outcome Evidence, Completion and Events

AD-006C відхилив фундаментальний `Result` Concept. Operation описує діяльність, а не mutable success/result object.

OutcomeAssessmentRecord за OCP-011 може exact-bind-ити Objective, criterion, evidence/input snapshots, evaluator і conclusion. Він має власну record identity, не є дочірнім полем Operation і не змінює її lifecycle.

```text
Completed Operation ≠ achieved Objective
OutcomeAssessmentRecord assesses exact Objective
```

Event за OCP-010 має незалежну occurrence identity. Він може бути exact evidence для окремого assessment або lifecycle provenance, але не є lifecycle stage, Operation-owned result, truth чи автоматичним доказом досягнення.

Operation-to-Event relevance лишається explicit downstream reference/relation question. Цей документ не додає `Operation → Event` Concept dependency або graph edge.

## 15. Business Rules

1. Operation може бути неповною лише на stage `Draft`; критерії повноти для інших stages повинні бути визначені до канонізації lifecycle.
2. Допустимість переходів lifecycle визначається окремою transition model.
3. Resource може мати кілька Assignment до різних Operation; допустимість одночасної участі визначається застосовними Constraint.
4. Parent/child допускається лише для Operation зі спільним наміром і залежністю виконання або окремо оціненого outcome.
5. Предметні розширення Operation повинні проходити Core Boundary Test.
6. Перехід до `Authorized` потребує простежуваного підтвердження, але тип підтвердження не визначається цим документом.
7. Explicit intent може використовуватися поза `Draft` лише коли один або більше authoritative validation records мають exact binding до поточних intent version, validation rule version та input snapshot, усі дають один однозначний result і цей result дорівнює `passed`.
8. Missing, stale, conflicting або structurally invalid explicit-intent evidence fail-safe не задовольняє intent invariant; за відсутності однозначного effective result нормативна projection дорівнює `not_evaluated`, а mutable `validation_status` не може зробити Operation більш permissive.
9. Кожен член plural `objective_refs` є активним affirmative-твердженням pursuit і повинен окремо резолвитися; один валідний Objective не компенсує інший невалідний reference.
10. Поза `Draft` `objective_refs` і `ExplicitIntentRecord` є взаємовиключними активними представленнями; автоматичної precedence або promotion між ними немає.
11. Operation lifecycle та Assignment lifecycle змінюються незалежно; правила їх узгодження повинні бути явними.

## 16. Semantic Rules

1. Наявність Operation classification не визначає автоматично її Resource, ролі, авторизацію або outcome conclusion.
2. `Completed` означає завершення виконання, але не означає автоматичного досягнення Objective.
3. Просторове або часове перекриття Operation не означає автоматично coordination або conflict.
4. Належність Resource до Organization не означає його участі в Operation.
5. Operation не змінює організаційну чи командну належність Resource.
6. Шаблон операції не є Operation instance.
7. Предметна спеціалізація Operation визначається domain або capability module; вона не є екземпляром Concept Capability лише через свою спеціалізацію.
8. Readiness і State не виводяться з lifecycle stage Operation без окремого прийнятого правила.
9. Операційна участь Resource в Operation представляється та виводиться через ефективний Assignment.
10. Нормативні правила участі визначені лише в OCP-005 §§8–9 і не дублюються як інваріанти або незалежні формули Operation.
11. Assignment не успадковується автоматично через композицію Operation або Resource.
12. Наявність Established Assignment не означає фактичної участі поза його applicability interval.
13. Plural `objective_refs` не кодує alternative pursuit, priority, sequence, hierarchy, contribution strength або achievement aggregation.
14. `validation_status` є derived projection: вона дорівнює однозначному effective result або `not_evaluated`, якщо такого result немає; projection не є авторитетним доказом і не може зробити Operation більш permissive.
15. `intent_version_ref` позначає immutable version усього binding-relevant змісту explicit intent; substantive зміна, включно зі зміною `statement`, вимагає нової version/reference value.
16. Локальна просторова прив’язка належить рівно одному Operation context і не має reusable Core identity поза ним.
17. Однаковий profile, payload, label або geometry не робить дві локальні прив’язки одним subject і не пов’язує їхні Operation.
18. Managed Position Site, Launch Site або Relay Site лишається Infrastructure Resource незалежно від рівності його footprint локальній просторовій прив’язці.
19. Просторова прив’язка не успадковує Assignment managed site, а Resource у межах payload не отримує Assignment до Operation.
20. Overlap або containment потребує окремого exact rule та input snapshots; spatial payload сам не створює coordination, conflict, visibility або authority consequence.
21. Unknown, unresolved, duplicate, ambiguous або profile-incomparable input не може бути замінений current value, best effort чи profile similarity.
22. Domain profile не є authority для Operation membership, Resource identity, suitability, authorization, selection або Readiness.
23. Жодне spatial resolution не використовує newest timestamp, record order, source/issuer count, label або area size як правило authority.

## 17. Invariants

### 17.1 Baseline Operation invariants

1. Кожен Operation instance має рівно одну непорожню стабільну identity.
2. Кожна Operation, lifecycle stage якої відрізняється від `Draft`, має рівно одну активну intent-гілку: або непорожній список унікальних `objective_refs`, або один `ExplicitIntentRecord`; одночасна наявність обох гілок є невалідною.
3. Кожен член non-Draft `objective_refs` є активним affirmative-твердженням pursuit і однозначно резолвиться у валідний Objective; список не означає вибір будь-якого одного елемента як достатнього.
4. Non-Draft `ExplicitIntentRecord` містить непорожні `intent_id`, exact-version `intent_version_ref`, змістовний `statement`, exact-version `validation_rule_ref` і непорожній `input_snapshot_ref`; exact-version references однозначно розрізняють identity та immutable version без нормативно визначеного wire encoding.
5. Кожен validation record містить непорожній `validation_id`, exact `intent_version_ref`, exact `validation_rule_ref`, exact `input_snapshot_ref`, валідний `evaluated_at`, непорожній `evaluator_ref` і один result із `not_evaluated | passed | failed`.
6. Non-Draft explicit-intent branch є валідною лише коли один або більше structurally valid records точно збігаються з поточними intent version, validation rule version та input snapshot, усі exact-binding records мають один однозначний result і цей result дорівнює `passed`.
7. Missing, stale, conflicting або structurally invalid explicit-intent evidence не задовольняє invariant 6 і fail-safe робить non-Draft Operation невалідною.
8. Матеріалізований `validation_status` є derived non-authoritative projection: вона дорівнює однозначному effective result, а за його відсутності — `not_evaluated`; будь-яке інше матеріалізоване значення є mismatch.
9. Кожне часове твердження Operation класифіковане як `planned` або `actual`, але не одночасно як обидва.
10. Жодна Operation не може бути parent або child самої себе.
11. Граф parent/child між Operation є ациклічним.
12. Кожен LifecycleTransitionRecord містить валідні `from_stage`, `to_stage`, `occurred_at` і непорожній `provenance_ref`.
13. Кожен InterOperationRelationshipAssertion містить валідні `source_operation_id`, `relation_type`, `target_operation_id` і непорожній `provenance_ref`.

### 17.2 Local spatial-binding invariants

1. Operation може мати zero, one або many локальних spatial bindings; відсутність `spatial_context` або явний empty binding set є валідними, якщо окремий exact consumer contract не вимагає більшого.
2. Наявний `spatial_context` містить exact-version `context_version_ref` і явний список `bindings`; довільна scalar або incomplete structure є невалідною.
3. Кожна binding містить local `binding_id`, exact `binding_version_ref` того самого local subject, exact `purpose_ref`, exact `representation_profile_ref`, exact `payload_snapshot_ref`, один `temporal_scope` і непорожній `provenance_ref`.
4. `binding_id` і `binding_version_ref` у межах одного active spatial context є унікальними; дві active versions одного local subject не вибираються за порядком.
5. `representation_profile_ref` однозначно резолвиться в exact profile з непорожнім owner reference; zero або multiple candidates є unresolved.
6. `payload_snapshot_ref` однозначно резолвиться в immutable exact snapshot з тим самим profile, opaque versioned payload reference і provenance; zero/multiple resolution або profile mismatch є невалідним.
7. `planned-context` потребує `planned_start`, `actual-context` потребує `actual_start`, а `operation-context` не створює окремого temporal assertion.
8. Spatial transition порівнює snapshots лише тієї самої `operation_id`; substantive зміна context або чинного binding вимагає нових context/binding versions і не переписує previous snapshot.
9. Local binding не містить `Operational Area`, `Environment`, Resource, Assignment, Organization чи іншої reusable subject identity як прихований Core owner.
10. Core володіє лише local membership та exact binding/profile/snapshot envelope; profile owner тлумачить opaque payload, але не встановлює cross-Operation identity або equivalence.
11. Spatial binding не матеріалізує coordinates/geometry у Core fixture і не містить чи не виводить Assignment, Resource equality, coordination, visibility, overlap consequence, suitability, admissibility, availability, authorization, selection або Readiness.

## 18. Examples

### Example A — UAV mission

Конкретний виліт є Operation. Маршрут, часові межі, екіпаж, борт, зв’язок і Objective формують її контекст. Спеціальні параметри визначаються UAV domain або capability module. Екіпаж і борт залучаються окремими Assignment.

### Example B — EW activity

Запланована робота конкретного засобу РЕБ у визначеному районі та часі є Operation. Засіб і оператор залучаються через Assignment; спеціальні режими визначаються EW domain або capability module.

### Example C — coordinated independent operations

Місія БпС і робота РЕБ можуть бути окремими Operation різних вертикалей. Вони не стають parent/child лише через спільний час або район. Координаційний зв’язок повинен бути встановлений окремо та мати provenance reference.

### Example D — local multipart spatial context

Одна Operation має дві локальні прив’язки — work area і transit corridor — з різними `binding_id`, але одним exact opaque profile. Інша Operation може мати payload з ідентичним synthetic shape; це не створює shared area identity, coordination або authorization. Зміна першого payload створює нові context, binding і payload-snapshot versions, а попередній Operation snapshot лишається відтворюваним.

## 19. Non-Examples

Не є Operation самі по собі:

- шаблон операції;
- Resource;
- Assignment;
- роль виконавця;
- маршрут без операційного наміру;
- окрема частота;
- повідомлення;
- OutcomeAssessmentRecord;
- Event;
- Order;
- календарний запис без операційного змісту.

## 20. Open Questions

AD-014B закрив питання, чи кожна Operation повинна мати окремий `Operational Area`: ні. OCP-004 використовує zero/one/many local bindings за §9; reusable area identity можна reopen лише за gates AD-014 §32.

1. Чи є Order обов’язковим механізмом авторизації Operation або лише одним із можливих джерел?
2. Чи потрібен `Suspended` у канонічному lifecycle?
3. Як представляти повторювані Operation без змішування шаблону й instance?
4. Які точні правила визначають parent/child?
5. Чи може одна Operation мати декілька незалежних джерел авторизації?
6. Який мінімальний набір даних потрібен для переходу `Draft → Planned`?
7. Коли conflict між Operation є збереженим фактом, а коли — похідним результатом?
8. Чи потрібен окремий зареєстрований Concept для шаблону Operation?
9. Які типи provenance повинні бути канонічними для lifecycle transitions та inter-operation relationships?
10. Які правила мають узгоджувати terminal stage Operation з незавершеними Assignment?

## 21. Deferred Decisions

До Constraint Concept відкладаються:

- конфлікти одночасного залучення Resource;
- ексклюзивність і capacity rules;
- допустимість кількох одночасних ролей.

AD-011 прийняв S0 і R0: Operation lifecycle не є shared State, а foundation не видає Operation Readiness. Новий shared State або Readiness contract потребує окремого reopening mandate з доказами, визначеними AD-011 §25.3; superseded ADR-DRAFT-007 не має current ontology authority.

До окремого accepted reopening act за AD-014 відкладаються:

- reusable area record або fundamental Operational Area identity;
- independent correction/lifecycle history поза owning Operation;
- cross-profile equivalence;
- geometry, CRS, topology, overlap і containment evaluation;
- environmental condition vocabulary та suitability assessment.

До окремих рішень Architecture Board відкладаються:

- моделі авторизації, наказів і погоджень;
- канонічна модель композиції Operation;
- канонічна модель conflict і coordination;
- taxonomy provenance для transition та relationship records;
- правила автоматичного завершення або відкликання Assignment після завершення Operation.

## 22. PATCH accounting — v0.8.1

Revision `0.8.1` виправляє лише volatile current-status rendering у §4: Capability тепер правильно позначено як `Canonical`.

Документ лишається `Draft`, Operation — `Accepted`. Це виправлення не змінює definition, identity, fields, lifecycle, domain semantics, dependencies, Concept status, graph edges або P-001 invocation. Поточні Objective status views у §4 та §6 навмисно не змінені: вони належать окремому, заново обчисленому K8 lifecycle proposal.

## 23. PATCH accounting — v0.8.2

Revision `0.8.2` синхронізує лише два volatile current-status renderings із окремим Objective lifecycle act: §4 row та §6 tree label тепер показують Objective як `Canonical`. Речення §22 про навмисно незмінені Objective views описує межу попереднього `0.8.1` Q1 PATCH і не є поточним status source.

Документ лишається `Draft`, Operation — `Accepted`. `objective_refs`, exact resolution, `ExplicitIntentRecord`, Operation lifecycle, `Operation → Objective` Concept edge, domain semantics і всі інваріанти лишаються незмінними; existing Operation references не потребують rebinding.

Corrective rollback є частиною нового reviewed Objective lifecycle rollback: OCP-004 повертає обидва status renderings разом з OCP-008, OCP-000, OCP-002, generated map і repository accounting. Ізольована зміна одного rendering або переписування Operation/Objective history заборонені.
