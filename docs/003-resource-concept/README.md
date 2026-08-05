---
Document-ID: OCP-003
Title: Resource Concept
Version: 0.6.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, AD-014
Used-By: Operation Concept, Assignment Concept, Organization Model, Capability Model, Domain Model
Defines-Concepts: Resource
Concept-Depends-On: []
Concept-Status: Accepted
Last-Review: 2026-08-05
---

# Resource Concept

## 1. Definition

**Resource** — ідентифікований керований елемент реального операційного середовища, який може бути доступний, призначений, залучений або використаний для виконання `Operation`.

Resource може бути людиною, групою людей, технічним засобом, інфраструктурним об’єктом, ідентифікованим матеріальним запасом або іншим операційно значущим елементом.

## 2. Purpose

Resource надає OCP єдину модель для представлення сил, засобів та інших елементів, що можуть брати участь в операційній діяльності.

Єдина модель потрібна, щоб однаково описувати:

- призначення на операцію;
- доступність;
- спроможності;
- обмеження;
- належність;
- фактичне використання;
- історію участі.

## 3. Scope

Resource описує **те, що може бути залучене до операції**.

Resource не визначає:

- штатну або оперативну вертикаль управління;
- повноваження користувача в інформаційній системі;
- роль у конкретній операції;
- саму операційну діяльність;
- правила координації.

Організаційна належність визначається `Organization`. Участь у конкретній операції визначається `Assignment` та `Operation`. Моделі посад, командних повноважень, управління доступом і нормативного управління будуть визначені окремими специфікаціями після їх розгляду Architecture Board.

## 4. Identity

Кожен екземпляр Resource має стабільну ідентичність на визначеному рівні операційного управління та може бути відрізнений від інших Resource того самого типу.

Для дискретних Resource ідентичність належить конкретному об’єкту або групі, наприклад:

- конкретній особі;
- конкретному екіпажу або розрахунку;
- конкретному борту;
- конкретному засобу РЕБ;
- конкретному ретранслятору;
- конкретному майданчику запуску.

Для взаємозамінних або витратних матеріалів ідентифікується керований запас, партія, контейнер, комплект або інша облікова одиниця, а не кожна фізична частка матеріалу.

Приклад: `Fuel Stock FS-001` є Resource, а значення `120 l` є його вимірюваною характеристикою. Абстрактний літр пального не є Resource.

Тип Resource не замінює його ідентичність. Два однотипні борти, два екіпажі або два окремі запаси пального є різними Resource.

## 5. Working Taxonomy

```text
Resource
├── Human Resource
│   ├── Person
│   ├── Crew
│   └── Duty Team
├── Organizational Resource
│   └── Unit
├── Technical Resource
│   ├── Platform
│   ├── Equipment
│   ├── Communication Asset
│   └── EW Asset
├── Infrastructure Resource
│   ├── Position Site
│   ├── Launch Site
│   └── Relay Site
└── Consumable Resource
    ├── Fuel Stock
    ├── Energy Stock
    └── Other Consumable Stock
```

Ця класифікація є робочою і не має статусу Canonical до окремого рішення Architecture Board.

### 5.1 Human Resource

Людина або визначена група людей, яка може діяти, виконувати функцію чи бути призначена до Operation.

`Actor` не є окремим фундаментальним Concept. Actor — це контекстна характеристика Resource, який виконує дію.

### 5.2 Organizational Resource

Організаційна одиниця або визначений її елемент, який розглядається як єдине ціле під час планування чи виконання Operation.

`Organization` та `Organizational Resource` не є тотожними:

- `Organization` описує структуру, належність і відносини;
- `Organizational Resource` описує операційне залучення організаційної одиниці як цілого.

До рішень AB-006 та AB-052 статус `Unit` у цій гілці й точний mapping `Organization ↔ Organizational Resource` залишаються відкритими питаннями.

### 5.3 Technical Resource

Матеріальний технічний засіб, обладнання або платформа, що має операційне застосування.

Предметно-специфічні типи, наприклад FPV-борт, VTX або засіб РЕБ, належать відповідним Capability і не визначаються в Core Ontology.

### 5.4 Infrastructure Resource

Відносно стаціонарний або підготовлений об’єкт, який може використовуватися для забезпечення Operation.

Термін `Position Site` використовується тимчасово, щоб не змішувати інфраструктурний об’єкт із можливим майбутнім поняттям посади.

AD-014B уточнює identity discriminator: конкретний managed Position Site, Launch Site або Relay Site з власною стабільною identity, owner/management boundary та use history є Infrastructure Resource. Його footprint, coverage, навколишня area або environmental conditions є окремими descriptions/inputs і не входять до identity Resource.

Довільний polygon, route, point, named region або condition snapshot не стає Resource лише тому, що використовується в Operation. OCP-004 може exact-bind-ити такий opaque spatial payload локально; рівність payload або geometry не merge-ить Resource з binding і не створює Assignment.

### 5.5 Consumable Resource

Ідентифікований керований запас, партія, контейнер, комплект або інша облікова одиниця матеріалу, кількість чи придатність якого зменшується внаслідок використання.

Consumable Resource не представляє окрему фізичну частку матеріалу або саме значення кількості.

Детальна модель кількості, одиниць вимірювання, партій, переміщення та списання не входить до цього документа.

## 6. Roles and Assignment

Resource не має сталої операційної ролі.

Роль Resource у конкретній Operation визначається через `Assignment`, модель якого має статус `Accepted` і визначена в [OCP-005 — Assignment Concept](../005-assignment-concept/README.md).

```text
Resource + Assignment + Operation Context = Operational Role
```

Той самий Resource може бути:

- виконавцем;
- координатором;
- засобом забезпечення;
- резервом;
- спостерігачем;
- відповідальним за погодження;
- іншим учасником, визначеним Assignment.

Належність Resource до Organization не означає його автоматичної участі в Operation.

## 7. Relationships

### Structural

```text
Resource belongs_to Organization
Resource may_be_part_of Resource
Resource may_contain Resource
```

### Operational

```text
Assignment assigns Resource to Operation
```

Окремий авторитетний зв’язок `Resource participates_in Operation` цим документом не визначається. Участь є похідною від ефективного Assignment відповідно до нормативного правила OCP-005 §§8–9.

### Capability and constraints

`Capability` і `Constraint` мають статус Accepted. Resource-specific Capability proposition представляється окремим `CapabilityClaimRecord` за OCP-012; definition та claim не стають властивістю Resource identity.

```text
CapabilityClaimRecord targets Resource
Resource is_subject_to Constraint
```

Positive Capability claim не створює Readiness, availability, authorization, selection або Assignment.

### Spatial and temporal

Resource може мати просторові й часові характеристики, але цей документ не визначає location model, availability або geometry authority. Operation-local spatial binding за OCP-004 не є Resource location, footprint ownership чи доказом участі.

`Environment` лишається taxonomy category і можливим domain input, а не alternative identity class для managed Infrastructure Resource. Site boundary може змінитися без зміни Resource identity; area, coverage або environmental evidence не успадковує його Assignment.

## 8. Composition

Resource може бути складеним.

Приклади:

- екіпаж складається з осіб;
- комплекс може складатися з платформи, антен, джерела живлення та обладнання;
- мобільна група може складатися з людей, транспорту і технічних засобів.

Композиція Resource не дорівнює організаційному підпорядкуванню.

Якщо складова моделюється як окремий Resource, включення до складеного Resource не скасовує її власну ідентичність.

## 9. Lifecycle

На цьому етапі фіксується лише загальний життєвий цикл існування Resource:

```text
Identified → Registered → Active → Retired
```

`Available`, `Assigned`, `In Use`, `Unavailable`, `Ready` та подібні значення не фіксуються як етапи життєвого циклу. AD-011 прийняв no-shared-State/no-shared-Readiness controls; availability і Resource-local health/lifecycle projections потребують окремих exact owners і не виводяться з цього lifecycle за implication.

## 10. Business Rules

1. Resource може мати декілька Assignment до різних Operation. Допустимість одночасних Assignment визначатиметься часовими, місткісними, ексклюзивними та іншими застосовними Constraint.
2. Consumable Resource управляється на рівні ідентифікованого запасу, партії, контейнера, комплекту або облікової одиниці.
3. Предметно-специфічна класифікація Resource не включається до Core без проходження Core Boundary Test.

## 11. Semantic Rules

1. Належність Resource до Organization не створює участі в Operation.
2. Наявність Capability не є достатньою підставою для висновку про готовність, доступність або фактичне призначення Resource.
3. Базовий тип Resource не визначає його операційну роль.
4. Кількість, маса, об’єм, заряд або залишок є характеристиками керованого Resource, а не окремими Resource.
5. Операційна участь Resource в Operation представляється та виводиться через Assignment; прямий авторитетний зв’язок участі між Resource та Operation у Core не визначено.
6. Операційна роль є властивістю контексту Assignment, а не сталою властивістю Resource.
7. Assignment складеного Resource не створює Assignment для його складових Resource автоматично.
8. Нормативні правила `assignment_effective_at` і `derived_participates_in` визначені лише в OCP-005 §§8–9; цей документ не створює їх незалежної копії.

## 12. Invariants

1. Кожен Resource має непорожній стабільний ідентифікатор у межах визначеної гранулярності управління.
2. Два різні Resource не мають одного й того самого ідентифікатора.
3. Кожен Resource має щонайменше один визначений тип або класифікацію.
4. Якщо Resource `A` містить Resource `B` і `B` моделюється як Resource, `B` має ідентичність, відмінну від `A`.
5. Кожен Consumable Resource ідентифікує керований запас, партію, контейнер, комплект або облікову одиницю; абстрактний тип матеріалу чи значення кількості не може бути типізоване як Resource.

## 13. Examples

### Example A — UAV crew

Екіпаж є Human Resource. Під час однієї Operation він може бути виконавцем, а під час іншої — резервом. Роль визначається окремими Assignment.

### Example B — EW asset

Конкретний засіб РЕБ є Technical Resource. Його діапазони, режими й інші спеціалізовані характеристики визначаються EW Capability, а не Core Resource Concept.

### Example C — battalion

Батальйон є Organization. Якщо батальйон або визначена його частина залучається до Operation як єдине ціле, може знадобитися представлення як Organizational Resource. Остаточне правило буде прийняте після Organization Concept.

### Example D — launch site

Конкретний майданчик запуску є Infrastructure Resource. Його використання в конкретній Operation оформлюється через Assignment.

### Example E — fuel stock

`Fuel Stock FS-001` є Consumable Resource. Його поточний обсяг є вимірюваною характеристикою цього Resource. Окремі літри не отримують власної ідентичності.

## 14. Non-Examples

Не є Resource самі по собі:

- роль «виконавець»;
- статус «готовий»;
- тип операції;
- частота як значення;
- наказ;
- ризик;
- маршрут;
- дозвіл користувача в системі;
- абстрактний літр пального;
- значення кількості, маси, об’єму, заряду або залишку;
- тип матеріалу без визначеного запасу чи облікової одиниці.

## 15. Open Questions

AD-014B закрив current-scope межу managed infrastructure / Environment: managed site є Resource, а spatial/environment description не є ним за implication. AD-011 окремо прийняв no-shared-Readiness control, OCP-013 визначив contextual interchangeability, а OCP-009/OCP-012 розділили Capability definition і Resource-specific claim.

1. Чи має `Unit` одночасно бути Organization і Resource, чи потрібна окрема проєкція Organization у Resource?
2. Чи потрібен окремий Concept `Resource Group` для тимчасового об’єднання ресурсів?
3. Якою моделлю описується поточна доступність Resource?
4. Чи потрібні окремі механізми масового створення Assignment для складених Resource?

## 16. Deferred Decisions

Окремими майбутніми рішеннями залишаються:

- модель доступності;
- будь-який future Readiness contract після окремого reopening mandate за AD-011;
- модель поточного використання;
- конфлікти одночасного призначення;
- Resource-local lifecycle/health projections без shared State abstraction;
- точна модель кількості, резервування і споживання Consumable Resource.
