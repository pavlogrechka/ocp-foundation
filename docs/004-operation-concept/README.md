---
Document-ID: OCP-004
Title: Operation Concept
Version: 1.0.1
Status: Canonical
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-008, AD-014, P-001
Uses-Patterns: P-001@0.1.0
Used-By: Assignment Concept, Operation Lifecycle, Coordination Model, Business Rules, Domain Model
Defines-Concepts: Operation
Concept-Depends-On: [Objective]
Concept-Status: Canonical
Last-Review: 2026-08-13
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
| Resource | Canonical | елемент, що залучається до Operation |
| Assignment | Accepted | авторитетний контекст участі Resource; OCP-005 |
| Objective | Canonical | intended outcome, condition або effect; OCP-008 |
| Constraint | Accepted | обмеження Operation та Assignment; OCP-006 |
| Event | Canonical | значущий occurrence або change; OCP-010 |
| Order | Proposed | можливе джерело авторизації; не визначене цим документом |
| Coordination | Proposed | модель взаємодії між Operation |
| Capability | Canonical | reusable definition layer; OCP-009 |
| Readiness | не зареєстрований окремо | AD-011 R0; не виводиться з Operation |
| State | не зареєстрований окремо | AD-011 S0; lifecycle Operation не є shared State |

`OutcomeAssessmentRecord` за OCP-011 може оцінювати exact Objective, але не є Concept, дочірнім об’єктом Operation або полем її успіху. Фундаментальний `Result` відхилено AD-006C.

OCP-004 exact-invoke-ить `P-001@0.1.0` окремо для двох endpoint-free record families: `OperationExplicitIntentRecord` і `OperationIntentValidationEvidenceRecord`. Pattern визначає лише форму; OCP-004 лишається єдиним власником їхньої Operation-specific семантики. Lifecycle transitions належать downstream OCP-017 і не є третьою record family цього документа.

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
├── Lifecycle Reference
│   └── OCP-017 transition history [Route C non-Concept contract]
└── Outcome
    ├── Event [Canonical]
    └── OutcomeAssessmentRecord [Accepted record contract; not a Concept]
```

Назви `Intent`, `Temporal Context`, `Spatial Context`, `Participation`, `Constraints` і `Outcome` у цій структурі є секціями моделі Operation, а не автоматично окремими фундаментальними Concept.

Не всі елементи мають бути повністю визначені під час створення Operation. Мінімальна повнота й допустимість переходів належать OCP-017; OCP-004 визначає стабільний Operation kernel, який ці правила перевіряють.

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
- record_kind_ref: operation-explicit-intent@1
- intent_id
- intent_version_ref
- statement
- authoring_provenance_ref
- validation_rule_ref
- input_snapshot_ref
- validation_status: not_evaluated | passed | failed  # optional derived projection
- validation_records:
  - validation_id
  - record_kind_ref: operation-intent-validation@1
  - intent_version_ref
  - validation_rule_ref
  - input_snapshot_ref
  - evaluated_at
  - evaluator_ref
  - provenance_ref
  - result: not_evaluated | passed | failed
```

`record_kind_ref` має відповідне фіксоване значення для кожної з двох record families. `intent_version_ref` та `validation_rule_ref` є непрозорими exact-version references. Кожне посилання повинно однозначно розрізняти identity та immutable version; нормативна модель не приписує delimiter або wire encoding. `input_snapshot_ref` непрозоро ідентифікує точний evaluated input snapshot. `authoring_provenance_ref` атрибутує створення exact intent version, а `provenance_ref` — exact validation record; жодне з них саме по собі не є authorization.

Нормалізований `statement` повинен містити щонайменше один символ літери або цифри. Значення, що складаються лише з пробілів, розділових знаків або службових заповнювачів, не є валідним statement.

Для використання explicit intent поза `Draft` має існувати один або більше структурно валідних validation records, які одночасно збігаються з поточними:

1. `intent_version_ref`;
2. exact-version `validation_rule_ref`;
3. `input_snapshot_ref`.

Усі records із цим exact binding утворюють effective evidence set. Evidence є однозначним, якщо всі exact-binding records мають один і той самий `result`. Повторні immutable records з однаковим result є допустимими; порядок списку та `evaluated_at` не обирають авторитетний record. Якщо exact-binding records містять різні results, evidence є conflicting.

Кожен record повинен містити фіксований kind, валідні `validation_id`, `evaluated_at`, `evaluator_ref`, `provenance_ref` і `result`. Non-Draft explicit-intent branch є валідною лише тоді, коли effective evidence set дає один однозначний `result = passed`.

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

Кожен inter-operation relationship у current Operation snapshot є локальним structured value, а не незалежно identified record:

```text
InterOperationRelationshipValue
- source_operation_ref
- relation_type: coordinates_with | depends_on | supports | conflicts_with
- target_operation_ref
- provenance_ref
```

`source_operation_ref` дорівнює identity owning Operation. `target_operation_ref` exact-resolve-иться рівно в одну іншу Operation у declared resolution scope. `relation_type` належить закритому OCP-004-owned набору; довільний kind неприпустимий. `provenance_ref` є непорожнім посиланням на правило, рішення, Event, результат обчислення або інший доказ, що пояснює наявність value у snapshot, але не надає permission або precedence.

Нормалізований tuple `(source_operation_ref, relation_type, target_operation_ref)` у межах snapshot є унікальним. Value не має власного ID, зовнішньої адресації, effectivity, transition history, supersession або current-head projection. Якщо конкретний consumer потребує хоча б однієї з цих властивостей, реалізація зупиняється й reopen-ить IO1/IO3 за AD-020A §41; додавати прихований record заборонено.

Ці чотири values позначають coordination relevance, operational dependency, claimed support direction або claimed incompatibility. Вони не створюють workflow agreement, Constraint applicability, Assignment, Event, outcome, authorization чи Concept graph edge. Саме відсутність independent record semantics пояснює, чому IO2 не invoke-ить P-001.

### 11.3 Authorization references

Operation може потребувати авторизації перед виконанням. OCP-017 визначає лише exact evidence-acceptance envelope для переходу до `Authorized`; джерело й механізм авторизації лишаються окремо governed. `Order` є зареєстрованим кандидатом на одне з можливих джерел, але OCP-004 та OCP-017 не обирають його автоматично.

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

`parent_operation_ref`, якщо наявний, exact-resolve-иться рівно в одну іншу Operation у declared dataset. Self-parent і будь-який цикл parent/child заборонені. Parent/child не успадковує Assignment, Constraint, local spatial context, outcome, authorization або lifecycle transition.

## 13. Lifecycle boundary

OCP-004 не є власником lifecycle state machine. Єдиний current owner stage vocabulary, allowed paths, structural completeness, transition history, authorization-evidence acceptance, terminal Assignment alignment і lifecycle projections — [OCP-017 — Operation Lifecycle Contract](../017-operation-lifecycle/README.md).

Operation зберігає ту саму `operation_id` на всіх lifecycle stages. Матеріалізований `lifecycle_stage`, якщо він присутній у snapshot, є лише checked projection з authoritative OCP-017 transition history. Stage label, provenance, completeness-profile result або authorization evidence не є другим джерелом істини й не може зробити перехід permissive.

Operation transition не є Event автоматично. Operation lifecycle не є shared State, не визначає Readiness і не змінює Assignment lifecycle. OCP-004 не залежить від OCP-017: downstream lifecycle contract залежить від стабільної Operation identity, а не навпаки.

## 14. Outcome Evidence, Completion and Events

AD-006C відхилив фундаментальний `Result` Concept. Operation описує діяльність, а не mutable success/result object.

OutcomeAssessmentRecord за OCP-011 може exact-bind-ити Objective, criterion, evidence/input snapshots, evaluator і conclusion. Він має власну record identity, не є дочірнім полем Operation і не змінює її lifecycle.

```text
Completed Operation ≠ achieved Objective
OutcomeAssessmentRecord assesses exact Objective
```

Event за OCP-010 має незалежну occurrence identity. Він може бути exact evidence для окремого assessment або lifecycle provenance, але не є lifecycle stage, Operation-owned result, truth чи автоматичним доказом досягнення.

Downstream contract може exact-reference одну Operation як контекст relevance для zero, one або many Event, а один Event може бути relevant до zero, one або many Operation. Така explicit relevance не змінює жодної identity, не означає generation або causation і не додає `Operation → Event` чи `Event → Operation` Concept dependency або graph edge.

## 15. Business Rules

1. Operation може бути неповною лише на stage `Draft`; універсальний structural minimum і exact domain-profile hook для інших stages визначає OCP-017.
2. Допустимість lifecycle transition визначається лише authoritative history за OCP-017.
3. Resource може мати кілька Assignment до різних Operation; допустимість одночасної участі визначається застосовними Constraint.
4. Parent/child допускається лише для Operation зі спільним наміром і залежністю виконання або окремо оціненого outcome; exact dataset graph є ациклічним.
5. Предметні розширення Operation повинні проходити Core Boundary Test.
6. Перехід до `Authorized` потребує exact evidence-acceptance envelope OCP-017, але ні OCP-004, ні evidence binding не визначають зовнішнє джерело permission.
7. Explicit intent може використовуватися поза `Draft` лише коли один або більше authoritative validation records мають exact binding до поточних intent version, validation rule version та input snapshot, усі дають один однозначний result і цей result дорівнює `passed`.
8. Missing, stale, conflicting або structurally invalid explicit-intent evidence fail-safe не задовольняє intent invariant; за відсутності однозначного effective result нормативна projection дорівнює `not_evaluated`, а mutable `validation_status` не може зробити Operation більш permissive.
9. Кожен член plural `objective_refs` є активним affirmative-твердженням pursuit і повинен окремо резолвитися; один валідний Objective не компенсує інший невалідний reference.
10. Поза `Draft` `objective_refs` і `ExplicitIntentRecord` є взаємовиключними активними представленнями; автоматичної precedence або promotion між ними немає.
11. Operation lifecycle та Assignment lifecycle змінюються незалежно; правила їх узгодження повинні бути явними.
12. IO2 relation value exact-resolve-ить обидві Operation, належить owning snapshot, використовує один із чотирьох закритих kinds і не має independent record semantics.

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
4. Non-Draft `OperationExplicitIntentRecord` містить fixed kind `operation-explicit-intent@1`, непорожні `intent_id` та `authoring_provenance_ref`, exact-version `intent_version_ref`, змістовний `statement`, exact-version `validation_rule_ref` і непорожній `input_snapshot_ref`; exact-version references однозначно розрізняють identity та immutable version без нормативно визначеного wire encoding.
5. Кожен `OperationIntentValidationEvidenceRecord` містить fixed kind `operation-intent-validation@1`, непорожні `validation_id` та `provenance_ref`, exact `intent_version_ref`, exact `validation_rule_ref`, exact `input_snapshot_ref`, валідний `evaluated_at`, непорожній `evaluator_ref` і один result із `not_evaluated | passed | failed`.
6. Non-Draft explicit-intent branch є валідною лише коли один або більше structurally valid records точно збігаються з поточними intent version, validation rule version та input snapshot, усі exact-binding records мають один однозначний result і цей result дорівнює `passed`.
7. Missing, stale, conflicting або structurally invalid explicit-intent evidence не задовольняє invariant 6 і fail-safe робить non-Draft Operation невалідною.
8. Матеріалізований `validation_status` є derived non-authoritative projection: вона дорівнює однозначному effective result, а за його відсутності — `not_evaluated`; будь-яке інше матеріалізоване значення є mismatch.
9. Кожне часове твердження Operation класифіковане як `planned` або `actual`, але не одночасно як обидва.
10. Жодна Operation не може бути parent або child самої себе.
11. Граф parent/child між Operation є ациклічним.
12. Lifecycle authority, transition identity, paths and projection invariants належать лише OCP-017; materialized `lifecycle_stage` Operation не може override-ити його history.
13. Кожен IO2 value містить owning `source_operation_ref`, exact `target_operation_ref`, один закритий `relation_type` і непорожній `provenance_ref`; normalized tuple є унікальним, а independent ID/effectivity/history/supersession заборонені.

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

1. Який окремо governed artifact є legitimate authorization source/mechanism для конкретного domain?
2. Які додаткові lifecycle stages або paths мають достатні reopening evidence поза bounded OCP-017 `0.1.0`?
3. Як представляти повторювані Operation без змішування шаблону й instance?
4. Коли bounded IO2 value потребує reopen до independently identified IO1/IO3 record?
5. Чи може окремий authorization contract прийняти декілька незалежних sources без двозначності?
6. Чи потрібен окремий зареєстрований Concept для шаблону Operation?
7. Які additional domain completeness profiles є legitimate owners для конкретних consumers?

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
- розширення bounded parent/child composition поза acyclicity/no-inheritance kernel;
- independently identified conflict або coordination records поза IO2;
- taxonomy provenance для transition та relationship records;
- будь-яке автоматичне завершення або відкликання Assignment після завершення Operation.

## 22. PATCH accounting — v0.8.1

Revision `0.8.1` виправляє лише volatile current-status rendering у §4: Capability тепер правильно позначено як `Canonical`.

Документ лишається `Draft`, Operation — `Accepted`. Це виправлення не змінює definition, identity, fields, lifecycle, domain semantics, dependencies, Concept status, graph edges або P-001 invocation. Поточні Objective status views у §4 та §6 навмисно не змінені: вони належать окремому, заново обчисленому K8 lifecycle proposal.

## 23. PATCH accounting — v0.8.2

Revision `0.8.2` синхронізує лише два volatile current-status renderings із окремим Objective lifecycle act: §4 row та §6 tree label тепер показують Objective як `Canonical`. Речення §22 про навмисно незмінені Objective views описує межу попереднього `0.8.1` Q1 PATCH і не є поточним status source.

Документ лишається `Draft`, Operation — `Accepted`. `objective_refs`, exact resolution, `ExplicitIntentRecord`, Operation lifecycle, `Operation → Objective` Concept edge, domain semantics і всі інваріанти лишаються незмінними; existing Operation references не потребують rebinding.

Corrective rollback є частиною нового reviewed Objective lifecycle rollback: OCP-004 повертає обидва status renderings разом з OCP-008, OCP-000, OCP-002, generated map і repository accounting. Ізольована зміна одного rendering або переписування Operation/Objective history заборонені.

## 24. PATCH accounting — v0.8.3

Revision `0.8.3` синхронізує лише volatile current-status rendering Resource у §4 з окремим Resource lifecycle act: row тепер показує Resource як `Canonical`. Last-Review уже має дату цього lifecycle cycle; ця accounting note завершує bounded PATCH.

Документ лишається `Draft`, Operation — `Accepted`. Resource reference, Assignment ownership, Operation fields/lifecycle, domain semantics, dependencies, Concept status, graph edges, P-001 invocation і всі інваріанти лишаються незмінними; existing Operation data не потребують rebinding.

Corrective rollback повертає цей status rendering разом з OCP-003, OCP-000, OCP-002, двома іншими consumer views, generated map і repository accounting через новий reviewed act. Ізольована зміна row або переписування Operation/Resource history заборонені.

## 25. Q3I stable-surface remediation — v0.9.0

### 25.1 Authority and exact baseline

AD-020A `0.2.0 / Accepted` selected Q3I only as the direction for this bounded remediation. A separate owner mandate authorized preparation of one atomic tree containing OCP-004 `0.9.0 / Draft` and new Route C OCP-017 `0.1.0 / Draft`; neither the selection nor that mandate authorizes merge or Operation lifecycle promotion.

The exact pre-remediation baseline is `main@66d32cb5a996c3796a370e3c54fc56bf7669358c`, tree `86424fec4b81f7b2ebfcc855666222d5f5113491`. On it OCP-004 is `0.8.3 / Draft`, Operation is `Accepted`, OCP-017 does not exist, P-001 is `0.1.0 / Accepted`, all nine structured `Uses-Patterns` bindings exact-resolve, 172 unit tests and 120 fixtures pass, and the Concept graph contains no Operation/Event edge.

### 25.2 Stable `0.x` Operation kernel

Revision `0.9.0` refines, rather than renumbers one-for-one, the fifteen reviewed guarantees in AD-020 §18. The mapping is explicit: §18 points 1–2 are combined in point 1 below, while their `repeated shape` clause remains normative in §5; §18 point 3 maps to point 2 and retains its explicit AD-004 reopening condition; points 4–9 map to points 3–8, with the fail-safe rule that missing, stale or conflicting evidence never becomes `passed` retained in §7.2, §16 point 7 and §17 point 6; point 10 is refined across points 9–10 and §12, which keeps parent/child composition distinct from independent coordination; and points 11–15 map to points 11–15. Point 10 below is an additional Q3I refinement for the newly bounded IO2 value, not a replacement for an inherited guarantee. This mapping uses the refinement permission in AD-020 §18 and weakens none of its terms.

The resulting fifteen guarantees are:

1. one exact `operation_id` identifies one purposeful context-bounded activity independently of name, template, classification, participants, spatial payload, lifecycle, Event and outcome;
2. outside `Draft`, exactly one active intent branch exists: non-empty exact `objective_refs` or one valid explicit-intent record, never both; this remains binding until AD-004 is separately changed by a reviewed act;
3. every Objective reference exact-resolves under OCP-008 and means affirmative pursuit only—never priority, sequence, hierarchy, aggregation or achievement;
4. explicit intent and validation keep immutable exact bindings, conflict-safe evidence-set semantics and no timestamp/order/count winner;
5. planned and actual temporal assertions remain distinct;
6. AD-014 local spatial context remains zero/one/many, snapshot-local, fail-safe and non-reusable;
7. Assignment alone owns authoritative Resource participation; composition and IO2 create none;
8. Constraint alone owns applicability and blocking/advisory semantics;
9. OCP-004 owns exact acyclic parent/child composition without inheritance of participation, applicability, spatial context, outcome or authorization;
10. OCP-004 owns only the bounded IO2 values in §11.2; workflow agreement, permission and caller authorization remain external;
11. Event occurrence and identity remain independent; an Operation transition is not an Event automatically;
12. `Completed Operation != achieved Objective`; OCP-011 remains assessment owner;
13. provenance, profile success, evidence or a stage label never grants authorization by itself;
14. Operation implies no Readiness, State, availability, admissibility, interchangeability, Organization holder or production authority; and
15. historical references replay under their original reviewed contract or stop for explicit lossless migration—never newest-version redirect.

### 25.3 Ownership ledger

| Responsibility | Single normative owner |
|---|---|
| Operation identity, active intent, planned/actual context, local spatial binding, composition, IO2 | OCP-004 |
| Objective identity and statement | OCP-008 |
| Resource participation | OCP-005 Assignment |
| Constraint applicability/evaluation | OCP-006 |
| lifecycle stages, paths, completeness, transition history, authorization-evidence acceptance, terminal alignment | OCP-017 |
| Event occurrence identity | OCP-010 |
| Objective outcome assessment | OCP-011 |
| P-001 record form | P-001; domain meaning stays with each invoker |

OCP-004 adds only P-001 to its direct dependency set. It deliberately does not depend on OCP-017 or any downstream evidence owner. OCP-017 consumes stable Operation identity in the acyclic downstream direction.

### 25.4 P-001 conformance — `OperationExplicitIntentRecord` (F1)

OCP-004 separately invokes `P-001@0.1.0` for the endpoint-free `OperationExplicitIntentRecord` family:

| P-001 Required Element | OCP-004 mapping |
|---|---|
| stable record identity | `intent_id`, unique across the invoking dataset |
| owning semantic specification | OCP-004 §7.2 and this section |
| endpoint contract | endpoint-free assertion owned by exact `operation_id`; no second endpoint |
| governed kind | fixed `record_kind_ref = operation-explicit-intent@1` |
| provenance | immutable `authoring_provenance_ref` for the exact intent version |
| validation | meaningful statement, exact intent/rule/input refs, exclusive active branch and executable negative evidence |
| authority | exact stored intent record plus its exact-binding validation evidence; `validation_status` is only a projection |

No Optional Module is selected. `intent_version_ref` versions binding-relevant content but is not P-001 Module C supersession; `evaluated_at` belongs only to the separate V1 evidence family and is not temporal effectivity of F1.

### 25.5 P-001 conformance — `OperationIntentValidationEvidenceRecord` (V1)

OCP-004 separately invokes the same exact Pattern for endpoint-free validation evidence:

| P-001 Required Element | OCP-004 mapping |
|---|---|
| stable record identity | `validation_id`, unique across the invoking dataset |
| owning semantic specification | OCP-004 §7.2 and this section |
| endpoint contract | endpoint-free evidence exact-bound to `intent_version_ref`, `validation_rule_ref` and `input_snapshot_ref` |
| governed kind | fixed `record_kind_ref = operation-intent-validation@1` |
| provenance | `evaluator_ref`, `evaluated_at` and immutable `provenance_ref` |
| validation | all bindings required; all exact-binding records must agree; missing/stale/conflicting/invalid evidence fails closed |
| authority | the complete exact-binding evidence set; no newest record, list order, evaluator count or issuer count selects a winner |

No Optional Module is selected. `evaluated_at` records when validation occurred; it does not create effectivity and therefore does not select Module A. No supersession field or winner projection selects Module C. Validation establishes conformance to the named rule/input only and never authorization.

One metadata `Uses-Patterns: P-001@0.1.0` imports the common form, but the two tables remain independent conformance statements and do not merge their identities or semantics.

### 25.6 IO2 non-invocation and reopening rule

`InterOperationRelationshipValue` does not invoke P-001 because it has no identity outside the exact owning Operation snapshot, no independently addressable subject, no temporal effectivity, lifecycle, supersession or current-head projection. Its authority is the exact owning Operation snapshot; duplicate tuples reject rather than compete.

Adding `relationship_id`, external reference target, effectivity, independent history, supersession, delegated kind ownership or a current-head selector changes that nature. Such a proposal must stop and reopen IO1/IO3 through a separate Board act instead of evolving IO2 silently.

### 25.7 Migration, replay and rollback

Historical OCP-004 `0.8.3` fixtures and exact references remain valid evidence under that contract. `0.9.0` adds a fixture-only `operation_contract_ref` so executable Q3I datasets can distinguish current conformance from historical replay; it is not a production wire-schema requirement.

Migration may carry forward an existing `operation_id`, exact Objective references and already evidenced intent content. It must not invent missing intent/validation IDs, authoring provenance, validation provenance, lifecycle transition IDs, authorization evidence, relation meaning or passing results. A source snapshot that cannot meet `0.9.0` remains historical or stops migration.

OCP-004 `0.9.0` and OCP-017 `0.1.0` form one atomic ownership tree. Partial merge or rollback of either document alone is invalid. Corrective rollback restores OCP-004 `0.8.3`, removes OCP-017 and its executable module/fixtures together, and restores accounting without rewriting P-001, its invokers, immutable snapshots, historical Operation data or the Concept graph.

### 25.8 Executable evidence boundary

`OperationQ3IContractDataset` is a non-production synthetic harness. It checks the finite structural subset that is mechanically expressible:

- exact current `OCP-004@0.9.0` fixture binding while legacy Operation fixtures still replay;
- unique Operation/F1/V1/LT2 identities;
- fixed F1/V1 kinds and provenance;
- exact parent resolution and acyclicity;
- the closed IO2 tuple, exact target and absence of independent-record fields;
- OCP-017 predecessor-chain history, allowed paths and materialized projection equality;
- exact completeness-profile and authorization-evidence bindings with ambiguity rejection;
- terminal Assignment alignment without Assignment mutation; and
- explicit non-implications for Event generation, outcome, Readiness, State, availability and interchangeability.

Material negative evidence is carried by separate F1, V1, LT2 and IO2 fixtures as well as focused unit attacks. The fixtures execute through `check.py` in both PR and main contexts. The F1, V1 and LT2 cases satisfy the selected record-family fixture obligation in AD-020 §23; all four negative cases, together with the positive Q3I fixture, satisfy the material positive/negative evidence obligation in AD-020A §42 points 4 and 8.

The checker does not authenticate legitimate owners, decide domain completeness, grant permission, evaluate Constraint truth, infer Event relevance, assess Objective achievement, provide a production schema or approve this Draft. Human review remains authoritative for those questions.

### 25.9 SemVer and status

`0.9.0` is a MINOR Draft revision because it adds two exact P-001 conformance surfaces, completes parent/child and IO2 boundaries, and relocates lifecycle authority to a new explicit downstream contract while preserving `operation_id`, Objective references, spatial semantics, consumers and the Concept edge set. PATCH would understate new compatible obligations; `1.0.0 / Canonical` would overstate readiness before a fresh lifecycle audit and separate Board act.

Operation remains `Accepted`; OCP-004 remains `Draft`. AB-015, AB-016, AB-017, AB-019, AB-020, AB-023 and AB-028 retain their prior statuses. This remediation creates no Concept, graph edge, authorization source, Organization claim/holder, Pattern version, production schema or lifecycle promotion.

### 25.10 P-001 evidence-accounting treatment

P-001 §17.3 is binding on this exact baseline: adding invokers of unchanged `P-001@0.1.0` does not edit the T3 evidence ledger. Therefore this remediation does not modify P-001 §11, §13, §16, `Last-Review` or any other byte. The current invoker set is derived only from structured `Uses-Patterns` metadata and exact checker resolution.

The pre-remediation nine binding-bearing files—six primary contracts and three immutable reviewed snapshots—remain byte-identical. This act adds OCP-004 and OCP-017 as seventh and eighth primary invokers without rewriting historical evidence. If Pattern form/obligations or exact track-current binding cannot remain unchanged, remediation stops for a separately gated Pattern-version act.

### 25.11 Exact relocation and consumer ledger

| `0.8.3` location / field | `0.9.0` / OCP-017 treatment | Identity or authority effect |
|---|---|---|
| OCP-004 §§1–5 | retained in OCP-004; §4 adds only Pattern/lifecycle ownership explanation | no `operation_id`, Concept or consumer change |
| OCP-004 §6 | readable kernel retained; lifecycle branch now points to OCP-017 | no new stored child object or edge |
| OCP-004 §§7–10 | intent/temporal/spatial/participation semantics retained; F1/V1 gain fixed kinds and provenance | intent/validation IDs remain their own identities; Assignment owner unchanged |
| `ExplicitIntentRecord.intent_id` | `OperationExplicitIntentRecord.intent_id` plus fixed kind and `authoring_provenance_ref` | same intent identity; no automatic Objective promotion |
| validation entry `validation_id` | `OperationIntentValidationEvidenceRecord.validation_id` plus fixed kind and `provenance_ref` | same evidence-set authority; no newest winner |
| OCP-004 §11.1 `Operation generates Event` | removed; positive zero/one/many downstream relevance is in §14 and OCP-017 §12 | no Event identity change and no graph edge |
| OCP-004 §11.2 record-like placeholder | exact snapshot-local IO2 value in §11.2 | `source_operation_id`/`target_operation_id` become exact `*_ref` fields; no relationship ID is migrated or invented |
| OCP-004 §11.3 authorization prose | boundary retained; evidence acceptance moves to OCP-017 §9 | no authorization source/mechanism selected |
| OCP-004 §12 | completed in place with exact parent resolution, acyclicity and no inheritance | parent/child stays OCP-004-owned and distinct from IO2 |
| OCP-004 §13 stages and incomplete local transition | sole current owner becomes OCP-017 §§4–10 | old stage values remain historical; new LT2 identity/provenance/evidence cannot be invented |
| `LifecycleTransitionRecord` without ID/ref | `OperationLifecycleTransitionRecord` with `transition_id`, exact `operation_ref` and predecessor chain | new LT2 record family; Module B only |
| materialized `lifecycle_stage` | optional checked projection from OCP-017 unique chain leaf | no label, time or storage-order authority |
| OCP-004 §§14–17 | current boundaries/rules retained, with lifecycle ownership removed and IO2/F1/V1 made exact | no duplicate lifecycle owner |
| OCP-004 §§18–19 | examples and non-examples retained verbatim | no example is reclassified and no ownership claim is added |
| OCP-004 §20 questions 3 and 8 | retained verbatim as current questions 3 and 6 | repeated-instance and separate-template-Concept questions remain open |
| OCP-004 §20 questions 1, 2 and 5 | reformulated as current questions 1, 2 and 5 | authority moves from an `Order` presumption to a separately governed source/mechanism; `Suspended` becomes the broader evidence-gated stage/path question; multiple sources remain open only inside a separate ambiguity-safe authorization contract |
| OCP-004 §20 question 4 | closed in place by §12 | exact parent resolution, acyclicity and no-inheritance form the bounded kernel; only extensions beyond that kernel remain deferred |
| OCP-004 §20 question 6 | closed for the bounded route by OCP-017 §8 | exact structural and owner-bound completeness is required; additional legitimate domain profiles remain current question 7 |
| OCP-004 §20 question 7 | closed only for the selected IO2 storage boundary by §11.2; current question 4 preserves the IO1/IO3 reopening gate | IO2 is a snapshot-local OCP-004-owned value; independently identified conflict/coordination records remain deferred and AB-018 remains Open |
| OCP-004 §20 question 9 | closed for the LT2 minimum by OCP-017 §6 | every transition needs non-empty provenance; a canonical provenance taxonomy remains deferred |
| OCP-004 §20 question 10 | closed for bounded terminal alignment by OCP-017 §10 | exact Assignment dispositions are required without mutation; automatic Assignment completion/revocation remains deferred |
| OCP-004 §21 composition decision | narrowed from a wholly open canonical model to extensions beyond the §12 acyclicity/no-inheritance kernel | the bounded kernel is current; broader composition is not implied |
| OCP-004 §21 conflict/coordination decision | narrowed from a wholly open canonical model to independently identified records beyond IO2 | bounded IO2 is current; no record identity, conflict ontology or coordination Concept is implied |
| OCP-004 §21 Assignment decision | sharpened from rules for automatic completion/revocation to the explicit prohibition of any such automatic action without a later Board act | OCP-017 terminal alignment records evidence and never mutates Assignment |
| AB-015, AB-016, AB-017, AB-019, AB-020, AB-023 and AB-028 | no status or resolution change | all seven backlog statuses remain unchanged; this document ledger does not substitute for backlog authority |
| OCP-004 §§22–24 | retained verbatim as historical PATCH accounting | cannot override current `0.9.0` semantics |

Five pre-existing direct consumers remain byte-identical in the proposed tree:

| Consumer | Baseline/current Git blob | SHA-256 |
|---|---|---|
| OCP-005 Assignment | `e5e0a62eda4ac84be081186c005e0167a3ebe288` | `8172173addc797416a151db198dcbea360711b82fb0a93b3732723f7f71154c6` |
| OCP-006 Constraint | `020c76f2518491beb2b7696e707224809ff26770` | `a604f6b07373741c9bfb25ad2e064b9b77b4c8fd52c9c3075b4865f9f65dfb27` |
| OCP-010 Event | `d73bab07acac3c316a9a2a4f4d25cb1f9b1bdc06` | `f66a2deb2bd8748aa464adefe3f4ff5ac35baf6af017fb9c782f9a427d7ac95f` |
| OCP-011 assessment | `ff2608a372c6305db4c290f05c15e961ca96e6f6` | `1fb08e18fab560e671b468585d699a7d70bd55ed5be674315cb780a48bc70cc5` |
| OCP-014 coordination profile | `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` |

OCP-017 is the one explicit new downstream consumer. Its `operation_ref: OP-Q3I-ALPHA` resolves the same `operation_id` that OCP-004 owns; no rebinding wrapper or successor ID is introduced. By contrast, a legacy stage-only snapshot has no defensible `transition_id` or predecessor chain and therefore remains under `0.8.3` rather than receiving fabricated LT2 history.

### 25.12 Complete scenario and rejection coverage

Every AD-020A §39 scenario has an explicit current address:

| Scenario set | Current contract/evidence | Result retained |
|---|---|---|
| 1–4 | OCP-004 §§5, 7 and 17.1 | identities stay distinct; Draft may be incomplete; non-Draft intent is exact and exclusive |
| 5–7 | OCP-004 §§7.2, 25.4–25.5; legacy and Q3I intent tests | stale/conflicting/reused-version evidence rejects without time/order winner |
| 8–9 | OCP-017 §§8, 11; profile failure/ambiguity tests | failure, zero/multiple owner or incomparable binding blocks transition |
| 10–11 | OCP-017 §§3, 9; authorization mismatch/ambiguity tests | ownerless evidence rejects; accepted evidence never grants permission |
| 12–14 | OCP-017 §10; terminal-alignment tests | Assignment effectivity stays OCP-005-owned; missing/wrong disposition rejects; no mutation |
| 15–18 | OCP-004 §§11.2, 12; composition/IO2 tests | no inheritance, self/cycle reject, IO2 creates no composition, overlap creates no relation |
| 19–23 | OCP-004 §14 and OCP-017 §§3, 12 | Event may have zero/many relevance; transition need not be Event; completion/assessment/Constraint remain separate |
| 24–26 | OCP-004 §11.2 and OCP-017 §§5–7; IO2/LT2 tests | closed kinds, exact target, unique IDs and unbranched history fail closed |
| 27–28 | §§25.7, 25.11 and unchanged five-consumer hashes | historical replay and exact Operation endpoint are preserved |
| 29–30 | OCP-004 §§9, 16–17, 25.2 and OCP-017 §3 | spatial value never becomes IO2 identity; no Capability/Readiness/interchangeability inference |

All thirty-two AD-020A §40 rejection classes also remain active:

| Rejection classes | Remediation control |
|---|---|
| 1–4 | §25.1 and OCP-017 §17 keep discovery/order/file count/review evidence non-authoritative and preserve four fresh merge gates |
| 5–8 | OCP-004 §§13–14 and OCP-017 §§3, 12 forbid prose-created edge, relevance erasure, free reverse dependency and transition/Event collapse |
| 9–16 | OCP-004 §§14–17 and OCP-017 §§8–10 separate completion, Assignment, composition, provenance, Order, domain profile and checker success from achievement/authorization/completeness authority |
| 17–22 | §§25.4–25.6 and OCP-017 §§7, 13 derive form/module use from identity/history semantics, never names, storage, counts, times or version labels |
| 23–26 | OCP-004 §§7.2, 9, 11.2 and OCP-017 §7 prohibit timestamp/order/count/list-position and local spatial identity from electing another record or family |
| 27–30 | OCP-004 §§3–4, 10–11, 16 and OCP-017 §3 preserve no permission/interchangeability/participation/Organization/backlog implication |
| 31–32 | §§25.1, 25.9 and OCP-017 §17 state that green CI neither selects Q3I nor transfers authorization to merge or later lifecycle work |

Machine evidence covers the finite material subset listed in §25.8; the remaining ownership, legitimate-authority, topology, readability and migration claims stay human-review obligations. Grouped coverage is not evidence that one successful scenario compensates for another failed one.

## 26. Current lifecycle bridge

OCP-004 `1.0.0 / Canonical` incorporates the complete human-readable Operation contract reviewed as `0.9.0 / Draft`. Sections 1–25 remain unchanged from baseline blob `591f1006e1a2faff135ecdbdadad4c63a666860b` with SHA-256 `ca5ce624ab180e4d97e86c534f03b3e9a1975244a7dd73edabc6e0c095e008a3`; the pre-wrapper body beginning at `# Operation Concept` has SHA-256 `d23834ebefd86c69fe21f2f470c8253b9ead30c28058194e53624a076c7916d8`.

Historical statements in §25 that describe `0.9.0 / Draft`, Operation `Accepted`, a future lifecycle audit or a not-yet-authorized WJ proposal record the state in which the Q3I remediation was reviewed. They do not override the current frontmatter, this bridge or §§27–31.

`Canonical` here means a stable, versioned compatibility promise for Operation identity and the bounded kernel owned by this document. It does not mean production readiness, operational authorization, completion of every Operation backlog question, proof of a current lifecycle stage, Objective achievement, Event occurrence, Resource availability or Readiness.

OCP-017 `0.2.0 / Accepted` remains the sole Route C owner of the extracted Operation lifecycle contract. OCP-004 does not gain a reverse dependency on OCP-017: the ownership direction remains downstream and acyclic.

## 27. Canonical compatibility surface `1.x`

OCP-004 `1.x` stabilizes the following fifteen guarantees already reviewed in §25.2:

1. one exact `operation_id` identifies one purposeful context-bounded activity independently of name, template, classification, participants, spatial payload, lifecycle, Event and outcome;
2. outside `Draft`, exactly one active intent branch exists: non-empty exact `objective_refs` or one valid explicit-intent record, never both; this remains binding until AD-004 is separately changed by a reviewed act;
3. every Objective reference exact-resolves under OCP-008 and means affirmative pursuit only—never priority, sequence, hierarchy, aggregation or achievement;
4. explicit intent and validation keep immutable exact bindings, conflict-safe evidence-set semantics and no timestamp/order/count winner;
5. planned and actual temporal assertions remain distinct;
6. AD-014 local spatial context remains zero/one/many, snapshot-local, fail-safe and non-reusable;
7. Assignment alone owns authoritative Resource participation; composition and IO2 create none;
8. Constraint alone owns applicability and blocking/advisory semantics;
9. OCP-004 owns exact acyclic parent/child composition without inheritance of participation, applicability, spatial context, outcome or authorization;
10. OCP-004 owns only the bounded IO2 values in §11.2; workflow agreement, permission and caller authorization remain external;
11. Event occurrence and identity remain independent; an Operation transition is not an Event automatically;
12. `Completed Operation != achieved Objective`; OCP-011 remains assessment owner;
13. provenance, profile success, evidence or a stage label never grants authorization by itself;
14. Operation implies no Readiness, State, availability, admissibility, interchangeability, Organization holder or production authority; and
15. historical references replay under their original reviewed contract or stop for explicit lossless migration—never newest-version redirect.

The ownership ledger in §25.3, the F1/V1 conformance statements in §§25.4–25.5, the IO2 non-invocation boundary in §25.6, all Q3I exclusions and every reopening condition remain part of this promise. OCP-017 acceptance does not import its transition records into Operation identity or turn a lifecycle stage into mutable OCP-004 authority.

## 28. Versioning after `1.0.0`

SemVer applies to the guarantees in §27 and their exact ownership, exclusion and replay boundaries:

- **PATCH** may correct prose, links, examples or accounting without changing a guarantee, owner, invariant, exact binding, P-001 conformance statement, exclusion or interpretation of an existing Operation;
- **MINOR** may add a backward-compatible optional guarantee or separately governed extension only when every existing Operation identity/reference, all fifteen guarantees, the D2/E1 topology and historical replay retain the same meaning; and
- **MAJOR** is required to remove or weaken a guarantee/exclusion, reinterpret Operation identity or active-intent authority, change the OCP-004/OCP-017 ownership direction, alter F1/V1/IO2 nature incompatibly, admit implicit participation/authorization/Event/outcome authority or rebind historical references.

A new stage, authorization source, independently identified inter-operation relationship, production schema or domain profile is not automatically MINOR because it adds data. It first requires its exact reopening owner and uses MAJOR whenever it weakens or reinterprets the `1.x` promise.

OCP document version `1.0.0` is not an Operation instance version, lifecycle stage, transition record, current-truth marker or authorization result.

## 29. Independent OCP-004 readiness evidence

OCP-004 passes its side of the joint lifecycle review independently of OCP-017:

| Review dimension | OCP-004 evidence and bounded conclusion |
|---|---|
| compatibility | §§1–25 are unchanged; §27 restates all fifteen guarantees without weakening or importing lifecycle authority |
| dependency floor | OCP-000/001/002/003/008 are Canonical; AD-014 is Accepted; exact `P-001@0.1.0` is Accepted, which is the required Pattern floor rather than a fictitious Canonical Pattern |
| consumers and topology | the metadata-derived set remains OCP-005/006/010/011/014/017; OCP-017 is downstream, no reverse dependency exists, the graph is acyclic, `Operation → Objective` is the only outgoing Concept edge and Event remains a non-edge |
| executable evidence | the unchanged `OCP-004@0.9.0` synthetic harness, 191 unit tests and 125 fixtures in both contexts replay the mechanically expressible subset of the unchanged body |
| source integrity | F1, V1 and IO2 normative sections keep their exact rule IDs and material positive/negative evidence; no rule, checker implementation, test or fixture changes |
| migration | no `operation_id`, Objective/consumer reference, F1/V1 record, spatial binding, IO2 value, Assignment, Constraint, Event or production datum is rewritten or rebound; only governed document/status projections change |
| rollback | OCP-004 may return to `0.9.0 / Draft` and Operation to `Accepted` only through a new reviewed rollback of the complete twelve-file unit; isolated projection rollback is invalid |

The executable harness remains exact-bound to `OCP-004@0.9.0`. It is evidence for the unchanged body incorporated here; it is not relabelled as newly generated `1.0.0` evidence and does not grant lifecycle authority.

OCP-004 readiness fails independently if any §27 guarantee is lost, §§1–25 drift, a direct floor fails, a seventh consumer or reverse dependency appears, a migration/rebinding becomes necessary, Pattern form changes, a current projection is omitted or any Q3I reopening gate gains concrete evidence. OCP-017 readiness cannot waive such a failure.

## 30. Exact WJ baseline and evidence anchors

The separately mandated WJ proposal is anchored on post-hygiene `main@e6433fe0955b205199a6be7c3f8cfe28a634c97c`, tree `09986b1af11736cd0d845dc9185ec41d9f035e37`. Every baseline object below was resolved by Git object first, reverse-matched to its path, checked against the state written in the object and hashed independently:

| Artifact | Verified baseline state | Git object | SHA-256 |
|---|---|---|---|
| AD-016 | `0.25.1 / Accepted`; WJ selected only under §§252/257/258 | blob `3c0f3c5e0532090ede9a3f04fe16bc477f3df9eb` | `afd046ee9ed1a2eb92ddc1e0e7bc73b02b293ec1292ff45fb1b9f3217e19d284` |
| OCP-004 | `0.9.0 / Draft`; Operation `Accepted` | blob `591f1006e1a2faff135ecdbdadad4c63a666860b` | `ca5ce624ab180e4d97e86c534f03b3e9a1975244a7dd73edabc6e0c095e008a3` |
| OCP-017 | `0.1.0 / Draft`; Route C non-Concept | blob `4c5fe6361a8f67fa0c7b1746e372d6404b9876a1` | `e3fc44295a8182eb97c3e39cd407daadc3434b49000b74fd4926cfa4e420cb28` |
| OCP-000 | `1.4.0 / Canonical`; Operation `Accepted` | blob `54d4f9a908c0ef572a4300be1f31e938db5557ef` | `f88a494aafff88bead233a43156435f460df2db0a31f8900465ac7fd7e1f335b` |
| OCP-001 | `1.0.0 / Canonical` | blob `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-002 | `1.4.0 / Canonical`; Operation `Accepted` | blob `470c7b035be3039065fc76f03bf76ad5fc8d3064` | `0366d50ec5ac21f5cd1e37af0cf7b46035dde38d0859b4fed9785793c5aa802c` |
| OCP-005 | `0.2.5 / Draft`; Operation peer view `Accepted` | blob `e5e0a62eda4ac84be081186c005e0167a3ebe288` | `8172173addc797416a151db198dcbea360711b82fb0a93b3732723f7f71154c6` |
| OCP-006 | `0.2.4 / Draft`; Operation peer view `Accepted` | blob `020c76f2518491beb2b7696e707224809ff26770` | `a604f6b07373741c9bfb25ad2e064b9b77b4c8fd52c9c3075b4865f9f65dfb27` |
| OCP-010 | `0.2.0 / Draft`; independent Event identity/non-edge | blob `d73bab07acac3c316a9a2a4f4d25cb1f9b1bdc06` | `f66a2deb2bd8748aa464adefe3f4ff5ac35baf6af017fb9c782f9a427d7ac95f` |
| OCP-011 | `0.3.0 / Accepted`; exact Operation target reference | blob `ff2608a372c6305db4c290f05c15e961ca96e6f6` | `1fb08e18fab560e671b468585d699a7d70bd55ed5be674315cb780a48bc70cc5` |
| OCP-014 | `0.2.0 / Accepted`; exact Operation context reference | blob `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` |
| OCP-016 | `1.0.0 / Canonical`; Route C authority | blob `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| P-001 | `0.1.0 / Accepted`; eight primary invokers | blob `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| Operation lifecycle rules | exact Q3I source map | blob `942e227820fb33130b0bcfd00cf118376d9f23a1` | `0e0cd72c4f7eacc49a4b2b4276257c6a52c5346483568b67106643f6b58e3685` |
| foundation map | Operation `Accepted`; only outgoing edge `Operation → Objective` | blob `0b7406d0934f8b2ef1e9698608ac9841aaec1b54` | `6c18c44fbb685a350bc86fbcb3d1a6a391ef63c2700aebb435569ae539daac48` |
| checker guide | Q3I kernel and Draft OCP-017 description | blob `4f7f60dc915682d6ce7aab6304a03f868c188fd2` | `c3b8c1b13c366ea5e7ef15d2be842f7b73f3763779a54cd0eef0f40d725d202f` |
| fixtures | 125 non-sensitive fixtures | tree `e5a2eed1ab0d752d3e0e4b1a31bc4c1fdcf6b108` | recursive manifest `a856ddb65b8ed071b27dda91f9e49cd0a3971003d223f9c658cc4df10ebd24ad` |
| unit-test files | 191 collected tests | tree `21016e8af459eb34ce8f356a6ab53da786d83c56` | recursive manifest `571d1e8256bce8732367dc95f469a65a3cd38f7bb6ca7749691f117b6ed6f754` |
| README / backlog / roadmap | post-hygiene accounting | blobs `1dc6970a0b4ea3f57e7ded734e6d65d74f433b87` / `516fced35353a1a86cb6ae9f4111bc2f6764eb6e` / `019de86714397ac9a5fa359b77b96a3e8039d97e` | `f9b0c0121a9461ba5b6786155b47c50ab18d2177d3771b146141cd1c866c2dee` / `03b981e3b66393772cc7411e9568f700ff67ee0c168f1d2316b56ffe81a245e3` / `a8d34388433edafb82f31ceba0a0053cd3597e8ec4ab3506fd179bd411234b55` |

Hash agreement proves the reviewed input bytes, not lifecycle authority. Newest time, record/document order, reviewer/issuer/consumer count, green CI, effort or a prior recommendation cannot select this transition.

## 31. Atomic T5 lifecycle act, rollback and authorization

The WJ proposal is exactly one twelve-file merge unit:

| # | Exact path | Bounded treatment |
|---:|---|---|
| 1 | `docs/004-operation-concept/README.md` | `0.9.0 / Draft → 1.0.0 / Canonical`; Operation `Accepted → Canonical`; preserve §§1–25 |
| 2 | `docs/017-operation-lifecycle/README.md` | `0.1.0 / Draft → 0.2.0 / Accepted`; preserve Route C non-Concept authority |
| 3 | `docs/017-operation-lifecycle/reviewed-contract-v0.1.0.md` | new immutable byte-identical copy of the reviewed Draft |
| 4 | `docs/000-operational-ontology/README.md` | `1.4.0 → 1.5.0`; exact Operation registry projection/provenance only |
| 5 | `docs/002-concept-taxonomy/README.md` | `1.4.0 → 1.5.0`; exact Operation frontmatter/current-prose projection only |
| 6 | `docs/005-assignment-concept/README.md` | `0.2.5 → 0.2.6`; PATCH-only Operation peer view |
| 7 | `docs/006-constraint-concept/README.md` | `0.2.4 → 0.2.5`; PATCH-only Operation peer view |
| 8 | `architecture/baselines/foundation-map.md` | Operation status projection only; edge set unchanged |
| 9 | `tools/ontology_checker/README.md` | current lifecycle description only; executable implementation unchanged |
| 10 | `README.md` | current lifecycle and readiness accounting only |
| 11 | `backlog/architecture-backlog.md` | AB-062 accounting only; status remains `Planned` |
| 12 | `backlog/roadmap.md` | T5/current-state/next-gate accounting only |

The semantic and projection effects are:

1. OCP-004 becomes `1.0.0 / Canonical` and Operation becomes `Canonical`, with §§1–25 unchanged and this lifecycle wrapper added;
2. OCP-017 becomes `0.2.0 / Accepted`, remains a Route C non-Concept and gains an immutable reviewed `0.1.0` snapshot plus its own lifecycle wrapper;
3. OCP-000 and OCP-002 move `1.4.0 → 1.5.0` by MINOR to project Operation `Canonical` with exact OCP-004/AD-020A/AD-016X/separately authorized WJ provenance;
4. OCP-005 moves `0.2.5 → 0.2.6` and OCP-006 moves `0.2.4 → 0.2.5` by PATCH for the Operation peer-status cell only;
5. the generated map projects Operation `Canonical` without an edge edit;
6. the checker guide changes only its current OCP-017 lifecycle label; and
7. README, architecture backlog and roadmap record the lifecycle/accounting result without resolving any Operation backlog item.

OCP-017 remains absent from OCP-000, OCP-002 and the Concept map. P-001, all eight primary invokers, three prior snapshots, rules, checker implementation, tests and fixtures remain byte-identical. The new OCP-017 snapshot is historical evidence and the fourth immutable `track-current` carrier, not a ninth primary invoker.

There is no stored-record, production-data, identity, reference, consumer, fixture or historical-evidence migration. The only migration is the governed document and current-status projection set above. Every exact consumer continues to bind the same Operation identity.

Corrective rollback requires a new reviewed act that restores the complete twelve-file unit: OCP-004 `0.9.0 / Draft`, Operation `Accepted`, OCP-017 `0.1.0 / Draft`, the prior registry/taxonomy/peer/map/guide/accounting projections and removal of the Accepted wrapper snapshot only as part of that governed rollback. It cannot rewrite historical Operation/LT2 records, P-001, existing snapshots or consumer bindings. Partial promotion or isolated rollback of either side is invalid, but no fixture-tested partial-rollback claim is made.

The act stops before merge if either independent readiness proof fails, the footprint differs from exactly twelve files, a current projection is missing, any byte outside the bounded wrappers/projections changes, a Pattern/rule/checker/test/fixture edit appears, a consumer rebinds, a new edge/dependency is required, the snapshot differs from the reviewed Draft or any `AD-016 §244` reopening route gains concrete evidence. Failure of either side returns the whole proposal to W0; the passing side receives no promotion by default.

When exact-head reviewed, separately authorized and squash-merged, this act completes the T5 Operation lifecycle transition only. It does not authorize T6–T10, change Assignment/Constraint/Event status, resolve AB-015/016/017/018/019/020/023/028, define an authorization source, create a Concept/edge/Pattern/schema or grant production authority. Preparation and external review do not authorize merge: the unchanged head still requires Fable approval, Codex adjudication, green CI and a fresh explicit Pavlo/Architecture Board authorization.

## 32. Current Event Concept-status projection — v1.0.1

Revision `1.0.1` is a PATCH that synchronizes only the volatile current Event status renderings in §4 and the decomposition view with the separately authorized Event Concept canonicalization act. Operation identity, Q3I semantics, all record contracts, consumers, dependencies and graph edges are unchanged. Historical sections and exact-baseline tables that record Event as `Accepted` remain byte-stable statements about their own reviewed baselines.
