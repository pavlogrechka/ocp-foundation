---
Document-ID: OCP-004
Title: Operation Concept
Version: 0.6.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-008
Used-By: Assignment Concept, Operation Lifecycle, Coordination Model, Business Rules, Domain Model
Defines-Concepts: Operation
Concept-Depends-On: [Objective]
Concept-Status: Accepted
Last-Review: 2026-08-02
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
- Operational Area та інші просторові прив’язки;
- Constraint;
- координаційні зв’язки;
- Event і Result.

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
| Objective | Under Review | intended outcome, condition або effect; OCP-008 |
| Operational Area | Proposed | просторовий контекст |
| Constraint | Accepted | обмеження Operation та Assignment; OCP-006 |
| Event | Proposed | значущий факт або зміна |
| Result | Proposed | наслідок або підсумок виконання |
| Order | Proposed | можливе джерело авторизації; не визначене цим документом |
| Coordination | Proposed | модель взаємодії між Operation |
| Capability | Proposed | межа предметної спеціалізації |
| Readiness | Deferred | не визначається цим документом |
| State | Deferred | не визначається цим документом |

Правила, що залежать від Concept у статусі `Proposed`, є робочими й підлягають уточненню у відповідних специфікаціях. Цей документ не передає нормативну відповідальність незареєстрованим поняттям.

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
│   └── Objective [Under Review]
├── Temporal Context
│   ├── Planned Bounds
│   └── Actual Bounds
├── Spatial Context
│   └── Operational Area [Proposed]
├── Participation
│   └── Assignment [Accepted]
├── Constraints
│   └── Constraint [Accepted]
└── Outcome
    ├── Event [Proposed]
    └── Result [Proposed]
```

Назви `Intent`, `Temporal Context`, `Spatial Context`, `Participation`, `Constraints` і `Outcome` у цій структурі є секціями моделі Operation, а не автоматично окремими фундаментальними Concept.

Не всі елементи мають бути повністю визначені під час створення Operation. Мінімальна повнота залежить від lifecycle stage і буде формалізована окремими правилами.

## 7. Intent and Objective

Operation має рівно одне активне представлення операційного наміру поза lifecycle stage `Draft`:

1. один або більше `objective_refs`, кожен з яких однозначно резолвиться у валідний Objective за OCP-008; або
2. один локальний `ExplicitIntentRecord`, що пройшов змістовну перевірку.

```text
Operation pursues Objective
```

Objective описує intended outcome, condition або effect і не дорівнює самій Operation. Нормативна семантика Objective визначена в [OCP-008 — Objective Concept](../008-objective-concept/README.md).

`objective_refs` є списком непорожніх унікальних Objective identifiers. Для Operation поза `Draft` кожен identifier повинен резолвитися рівно в один валідний Objective instance. Нерезолвлене, неоднозначне або невалідне посилання не задовольняє вимогу операційного наміру.

Локальний `ExplicitIntentRecord` не вводиться як фундаментальний Concept. Він є fallback-структурою перевірки повноти Operation:

```text
ExplicitIntentRecord
- intent_id
- statement
- validation_status: not_evaluated | passed | failed
- validation_rule_ref
- validated_at
```

Нормалізований `statement` повинен містити щонайменше один символ літери або цифри. Значення, що складаються лише з пробілів, розділових знаків або службових заповнювачів, не є валідним statement.

Для використання explicit intent поза `Draft` запис повинен мати `validation_status = passed`, непорожній `validation_rule_ref` і валідний `validated_at`. Змістовні критерії достатності визначаються domain validation rule, на який посилається `validation_rule_ref`.

### 7.1 Coexistence and precedence contract

На stage `Draft` `objective_refs` і `ExplicitIntentRecord` можуть тимчасово співіснувати як authoring state. Жодне представлення не має автоматичного пріоритету, а Draft може не мати жодного з них.

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

Operation може мати одну чи більше Operational Area, маршрутів, точок або інших просторових прив’язок.

```text
Operation occurs_in Operational Area
```

Operational Area є контекстом Operation, а не частиною її ідентичності.

Маршрут або точка без операційного наміру самі по собі не є Operation.

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
Operation occurs_in Operational Area
Operation is_subject_to Constraint
Operation produces Result
Operation generates Event
```

Кожен Concept у цих зв’язках має статус, наведений у розділі 4.

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

Parent/child використовується лише тоді, коли дочірня Operation є частиною спільного операційного наміру і її виконання або Result впливає на батьківську Operation.

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

Ці значення є lifecycle stages, визначеними локально для Operation. Вони не є значеннями фундаментального Concept `State`, статус якого відкладено в ADR-DRAFT-007.

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

Можливий stage `Suspended` не вводиться цим документом. Остаточна state machine буде винесена до Operation Lifecycle після Constraint і перегляду ADR-DRAFT-007.

## 14. Result, Completion and Events

Operation та Result не є тотожними.

Operation описує діяльність, а Result — зафіксований наслідок, ефект або підсумок виконання.

```text
Operation produces Result
Result evaluates Objective
```

`Result evaluates Objective` є робочим зв’язком до прийняття специфікацій Objective і Result.

Event фіксує значущий факт або зміну, пов’язану з Operation. Event не замінює lifecycle stage, але може бути джерелом його історії або обчислення.

## 15. Business Rules

1. Operation може бути неповною лише на stage `Draft`; критерії повноти для інших stages повинні бути визначені до канонізації lifecycle.
2. Допустимість переходів lifecycle визначається окремою transition model.
3. Resource може мати кілька Assignment до різних Operation; допустимість одночасної участі визначається застосовними Constraint.
4. Parent/child допускається лише для Operation зі спільним наміром і залежністю виконання або Result.
5. Предметні розширення Operation повинні проходити Core Boundary Test.
6. Перехід до `Authorized` потребує простежуваного підтвердження, але тип підтвердження не визначається цим документом.
7. Explicit intent може використовуватися поза `Draft` лише після проходження змістовної перевірки за domain validation rule; Core перевіряє структурний record і результат перевірки, але не замінює предметну оцінку.
8. Поза `Draft` `objective_refs` і `ExplicitIntentRecord` є взаємовиключними активними представленнями; автоматичної precedence або promotion між ними немає.
9. Operation lifecycle та Assignment lifecycle змінюються незалежно; правила їх узгодження повинні бути явними.

## 16. Semantic Rules

1. Наявність Operation classification не визначає автоматично її Resource, ролі, авторизацію або Result.
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

## 17. Invariants

1. Кожен Operation instance має рівно одну непорожню стабільну identity.
2. Кожна Operation, lifecycle stage якої відрізняється від `Draft`, має рівно одну активну intent-гілку: або непорожній список унікальних `objective_refs`, кожен елемент якого однозначно резолвиться у валідний Objective, або один валідний ExplicitIntentRecord; одночасна наявність обох гілок є невалідною.
3. Кожне часове твердження Operation класифіковане як `planned` або `actual`, але не одночасно як обидва.
4. Жодна Operation не може бути parent або child самої себе.
5. Граф parent/child між Operation є ациклічним.
6. Кожен LifecycleTransitionRecord містить валідні `from_stage`, `to_stage`, `occurred_at` і непорожній `provenance_ref`.
7. Кожен InterOperationRelationshipAssertion містить валідні `source_operation_id`, `relation_type`, `target_operation_id` і непорожній `provenance_ref`.

## 18. Examples

### Example A — UAV mission

Конкретний виліт є Operation. Маршрут, часові межі, екіпаж, борт, зв’язок і Objective формують її контекст. Спеціальні параметри визначаються UAV domain або capability module. Екіпаж і борт залучаються окремими Assignment.

### Example B — EW activity

Запланована робота конкретного засобу РЕБ у визначеному районі та часі є Operation. Засіб і оператор залучаються через Assignment; спеціальні режими визначаються EW domain або capability module.

### Example C — coordinated independent operations

Місія БпС і робота РЕБ можуть бути окремими Operation різних вертикалей. Вони не стають parent/child лише через спільний час або район. Координаційний зв’язок повинен бути встановлений окремо та мати provenance reference.

## 19. Non-Examples

Не є Operation самі по собі:

- шаблон операції;
- Resource;
- Assignment;
- роль виконавця;
- маршрут без операційного наміру;
- окрема частота;
- повідомлення;
- Result;
- Event;
- Order;
- календарний запис без операційного змісту.

## 20. Open Questions

1. Чи є Order обов’язковим механізмом авторизації Operation або лише одним із можливих джерел?
2. Чи потрібен окремий Concept `Operational Intent` для майбутніх domain-моделей, якщо Core уже має взаємовиключні Objective та ExplicitIntentRecord branches?
3. Чи всі Operation повинні мати Operational Area?
4. Чи потрібен `Suspended` у канонічному lifecycle?
5. Як представляти повторювані Operation без змішування шаблону й instance?
6. Які точні правила визначають parent/child?
7. Чи може одна Operation мати декілька незалежних джерел авторизації?
8. Який мінімальний набір даних потрібен для переходу `Draft → Planned`?
9. Коли conflict між Operation є збереженим фактом, а коли — похідним результатом?
10. Чи має Operation власну Readiness, окрему від Readiness залучених Resource?
11. Чи потрібен окремий зареєстрований Concept для шаблону Operation?
12. Які типи provenance повинні бути канонічними для lifecycle transitions та inter-operation relationships?
13. Які правила мають узгоджувати terminal stage Operation з незавершеними Assignment?

## 21. Deferred Decisions

До Constraint Concept відкладаються:

- конфлікти одночасного залучення Resource;
- ексклюзивність і capacity rules;
- допустимість кількох одночасних ролей.

До перегляду `ADR-DRAFT-007` відкладаються:

- остаточна модель State;
- розмежування lifecycle stage, operational status і derived state;
- онтологічна природа Readiness Operation;
- правила збереження та обчислення поточного стану.

До окремих рішень Architecture Board відкладаються:

- моделі авторизації, наказів і погоджень;
- окремий Concept Operational Intent;
- канонічна модель композиції Operation;
- канонічна модель conflict і coordination;
- taxonomy provenance для transition та relationship records;
- правила автоматичного завершення або відкликання Assignment після завершення Operation.
