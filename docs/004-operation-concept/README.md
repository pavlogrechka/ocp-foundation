---
Document-ID: OCP-004
Title: Operation Concept
Version: 0.2.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003
Used-By: Assignment Concept, Operation Lifecycle, Coordination Model, Business Rules, Domain Model
Defines-Concepts: Operation
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

`Operation` має статус `Under Review` у реєстрі OCP-000.

Цей документ використовує такі зареєстровані Concept:

| Concept | Status | Використання в OCP-004 |
|---|---|---|
| Resource | Accepted | елемент, що залучається до Operation |
| Assignment | Proposed | робочий механізм участі Resource |
| Objective | Proposed | представлення бажаного ефекту або мети |
| Operational Area | Proposed | просторовий контекст |
| Constraint | Proposed | обмеження Operation |
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
│   └── Objective [Proposed]
├── Temporal Context
│   ├── Planned Bounds
│   └── Actual Bounds
├── Spatial Context
│   └── Operational Area [Proposed]
├── Participation
│   └── Assignment [Proposed]
├── Constraints
│   └── Constraint [Proposed]
└── Outcome
    ├── Event [Proposed]
    └── Result [Proposed]
```

Назви `Intent`, `Temporal Context`, `Spatial Context`, `Participation`, `Constraints` і `Outcome` у цій структурі є секціями моделі Operation, а не автоматично окремими фундаментальними Concept.

Не всі елементи мають бути повністю визначені під час створення Operation. Мінімальна повнота залежить від lifecycle stage і буде формалізована окремими правилами.

## 7. Intent and Objective

Operation має операційний намір, представлений описом наміру та/або одним чи більше Objective.

```text
Operation pursues Objective
```

Objective описує бажаний ефект або мету, але не дорівнює самій Operation.

Operation може існувати без повністю визначеного Objective лише на lifecycle stage `Draft`.

Остаточна семантика Objective буде визначена окремою специфікацією.

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

У поточній робочій моделі участь Resource в Operation представляється через Assignment:

```text
Assignment assigns Resource to Operation
```

Assignment має визначити роль, часову застосовність, обсяг та інші умови участі. Детальна семантика буде визначена в `OCP-005 — Assignment Concept`.

Operation не володіє Resource і не змінює його організаційну чи командну належність.

До прийняття OCP-005 правила участі через Assignment є provisional contract між OCP-003 і OCP-004.

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

Ці зв’язки не виникають автоматично через просторове або часове перекриття. Джерело кожного встановленого зв’язку повинно бути простежуваним до правила, рішення або результату обчислення.

Точна семантика буде визначена Coordination Model.

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

Остаточні правила композиції залишаються відкритим питанням.

## 13. Working Lifecycle

Робочі lifecycle stages Operation:

```text
Draft → Planned → Authorized → Active → Completed
                         ↘ Cancelled
                         ↘ Aborted
```

Ці значення є lifecycle stages, визначеними локально для Operation. Вони не є значеннями фундаментального Concept `State`, статус якого відкладено в ADR-DRAFT-007.

### 13.1 Draft

Operation зареєстрована, але її намір, контекст або склад можуть бути неповними.

### 13.2 Planned

Operation має мінімальний плановий контекст, достатній для перевірки та підготовки. Точні критерії переходу залишаються відкритими.

### 13.3 Authorized

Для Operation зафіксовано необхідне підтвердження дозволу на виконання відповідно до застосовних правил.

Цей stage не визначає, який саме Concept або артефакт є джерелом дозволу.

### 13.4 Active

Зафіксовано початок фактичного виконання Operation.

### 13.5 Completed

Зафіксовано завершення фактичного виконання Operation.

### 13.6 Cancelled

Operation завершена без переходу до фактичного виконання.

### 13.7 Aborted

Operation припинена після початку фактичного виконання або через неможливість продовження.

Можливий stage `Suspended` не вводиться цим документом. Остаточна state machine буде винесена до Operation Lifecycle після OCP-005 і перегляду ADR-DRAFT-007.

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

## 16. Semantic Rules

1. Наявність Operation classification не визначає автоматично її Resource, ролі, авторизацію або Result.
2. `Completed` означає завершення виконання, але не означає автоматичного досягнення Objective.
3. Просторове або часове перекриття Operation не означає автоматично coordination або conflict.
4. Належність Resource до Organization не означає його участі в Operation.
5. Operation не змінює організаційну чи командну належність Resource.
6. Шаблон операції не є Operation instance.
7. Предметна спеціалізація Operation визначається domain або capability module; вона не є екземпляром Concept Capability лише через свою спеціалізацію.
8. Readiness і State не виводяться з lifecycle stage Operation без окремого прийнятого правила.

## 17. Invariants

1. Кожен Operation instance має рівно одну стабільну identity.
2. Кожна Operation, lifecycle stage якої відрізняється від `Draft`, має щонайменше один Objective reference або непорожній explicit intent statement.
3. Для кожного зв’язку участі між Resource і Operation існує щонайменше один Assignment, що пов’язує той самий Resource з тією самою Operation.
4. Кожне часове твердження Operation класифіковане як `planned` або `actual`, але не одночасно як обидва.
5. Жодна Operation не може бути parent або child самої себе.
6. Граф parent/child між Operation є ациклічним.
7. Кожен запис переходу lifecycle містить попередній stage, наступний stage, час переходу та джерело переходу.
8. Кожен встановлений зв’язок `coordinates_with`, `depends_on`, `supports` або `conflicts_with` має простежуване джерело.

## 18. Examples

### Example A — UAV mission

Конкретний виліт є Operation. Маршрут, часові межі, екіпаж, борт, зв’язок і Objective формують її контекст. Спеціальні параметри визначаються UAV domain або capability module.

### Example B — EW activity

Запланована робота конкретного засобу РЕБ у визначеному районі та часі є Operation. Засіб і оператор залучаються через Assignment; спеціальні режими визначаються EW domain або capability module.

### Example C — coordinated independent operations

Місія БпС і робота РЕБ можуть бути окремими Operation різних вертикалей. Вони не стають parent/child лише через спільний час або район. Координаційний зв’язок повинен бути встановлений окремо та мати джерело.

## 19. Non-Examples

Не є Operation самі по собі:

- шаблон операції;
- Resource;
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
2. Чи потрібен окремий Concept `Operational Intent`, чи достатньо Objective та explicit intent statement?
3. Чи всі Operation повинні мати Operational Area?
4. Чи потрібен `Suspended` у канонічному lifecycle?
5. Як представляти повторювані Operation без змішування шаблону й instance?
6. Які точні правила визначають parent/child?
7. Чи може одна Operation мати декілька незалежних джерел авторизації?
8. Який мінімальний набір даних потрібен для переходу `Draft → Planned`?
9. Коли conflict між Operation є збереженим фактом, а коли — похідним результатом?
10. Чи має Operation власну Readiness, окрему від Readiness залучених Resource?
11. Чи потрібен окремий зареєстрований Concept для шаблону Operation?

## 21. Deferred Decisions

До завершення `OCP-005 — Assignment Concept` відкладаються:

- остаточні правила участі Resource;
- конфлікти одночасного залучення;
- часові межі Assignment відносно Operation;
- ролі резерву, підтримки, координації та погодження;
- правила заміни Resource в Active Operation.

До перегляду `ADR-DRAFT-007` відкладаються:

- остаточна модель State;
- розмежування lifecycle stage, operational status і derived state;
- онтологічна природа Readiness Operation;
- правила збереження та обчислення поточного стану.

До окремих рішень Architecture Board відкладаються:

- моделі авторизації, наказів і погоджень;
- окремий Concept Operational Intent;
- канонічна модель композиції Operation;
- канонічна модель conflict і coordination.
