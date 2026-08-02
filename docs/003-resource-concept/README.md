---
Document-ID: OCP-003
Title: Resource Concept
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002
Used-By: Operation Concept, Assignment Concept, Organization Model, Capability Model, Domain Model
Canonical-Concepts: Resource
Last-Review: 2026-08-02
---

# Resource Concept

## 1. Definition

**Resource** — ідентифікований елемент реального операційного середовища, який може бути доступний, призначений, залучений або використаний для виконання `Operation`.

Resource може бути людиною, групою людей, технічним засобом, інфраструктурним об’єктом, матеріальним запасом або іншим операційно значущим елементом.

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

Ці аспекти визначаються іншими Concept, зокрема `Organization`, `Position`, `Assignment`, `Operation` і `Governance`.

## 4. Identity

Resource має власну операційну ідентичність і може бути відрізнений від інших ресурсів того самого типу.

Приклади:

- конкретна особа;
- конкретний екіпаж або розрахунок;
- конкретний борт;
- конкретний засіб РЕБ;
- конкретний ретранслятор;
- конкретний майданчик запуску;
- визначений матеріальний запас.

Тип ресурсу не замінює його ідентичність. Два однотипні борти або два екіпажі є різними Resource.

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
    ├── Energy Supply
    ├── Fuel
    └── Other Consumable
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

До завершення Organization Concept статус `Unit` у цій гілці залишається відкритим питанням.

### 5.3 Technical Resource

Матеріальний технічний засіб, обладнання або платформа, що має операційне застосування.

Предметно-специфічні типи, наприклад FPV-борт, VTX або засіб РЕБ, належать відповідним Capability і не визначаються в Core Ontology.

### 5.4 Infrastructure Resource

Відносно стаціонарний або підготовлений об’єкт, який може використовуватися для забезпечення Operation.

Термін `Position Site` використовується тимчасово, щоб не змішувати інфраструктурну позицію з Concept `Position` як посадою.

### 5.5 Consumable Resource

Матеріальний ресурс, кількість або придатність якого зменшується внаслідок використання.

Детальна модель кількості, одиниць вимірювання, партій і списання не входить до цього документа.

## 6. Roles and Assignment

Resource не має сталої операційної ролі.

Роль Resource у конкретній Operation визначається через `Assignment`.

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
Resource participates_in Assignment
Assignment assigns Resource to Operation
Operation uses Resource through Assignment
```

### Capability and constraints

```text
Resource has Capability
Resource is_subject_to Constraint
```

### Spatial and temporal

```text
Resource may_be_located_in Operational Area
Resource may_be_available_during Time Interval
```

Точна семантика просторових, часових і стано-залежних зв’язків буде уточнена в окремих Concept.

## 8. Composition

Resource може бути складеним.

Приклади:

- екіпаж складається з осіб;
- комплекс може складатися з платформи, антен, джерела живлення та обладнання;
- мобільна група може складатися з людей, транспорту і технічних засобів.

Композиція Resource не дорівнює організаційному підпорядкуванню.

Включення дочірнього Resource до складеного Resource не повинно автоматично знищувати його власну ідентичність.

## 9. Lifecycle

На цьому етапі фіксується лише загальний життєвий цикл існування Resource:

```text
Identified → Registered → Active → Retired
```

`Available`, `Assigned`, `In Use`, `Unavailable`, `Ready` та подібні значення не фіксуються як етапи життєвого циклу. Вони можуть бути станами або похідними оцінками й розглядатимуться після `Operation` та `Assignment` відповідно до `ADR-DRAFT-007`.

## 10. Invariants

1. Resource має власну ідентичність.
2. Resource має визначений тип або класифікацію.
3. Resource не бере участі в Operation без Assignment.
4. Операційна роль Resource визначається Assignment, а не його базовим типом.
5. Належність до Organization не означає участі в Operation.
6. Один Resource може брати участь у декількох Operation, якщо це не порушує часові, ресурсні або інші Constraint.
7. Складений Resource не скасовує ідентичність його складових Resource, якщо інше не встановлено окремим правилом.
8. Capability Resource не гарантує його готовність, доступність або фактичне призначення.
9. Предметно-специфічна класифікація Resource не повинна потрапляти до Core без проходження Core Boundary Test.

## 11. Examples

### Example A — UAV crew

Екіпаж є Human Resource. Під час однієї Operation він може бути виконавцем, а під час іншої — резервом. Роль визначається окремими Assignment.

### Example B — EW asset

Конкретний засіб РЕБ є Technical Resource. Його діапазони, режими й інші спеціалізовані характеристики визначаються EW Capability, а не Core Resource Concept.

### Example C — battalion

Батальйон є Organization. Якщо батальйон або визначена його частина залучається до Operation як єдине ціле, може знадобитися представлення як Organizational Resource. Остаточне правило буде прийняте після Organization Concept.

### Example D — launch site

Конкретний майданчик запуску є Infrastructure Resource. Його використання в конкретній Operation оформлюється через Assignment або інший зв’язок, який буде уточнено після Operation Concept.

## 12. Non-Examples

Не є Resource самі по собі:

- роль «виконавець»;
- статус «готовий»;
- тип операції;
- частота як значення;
- наказ;
- ризик;
- маршрут;
- дозвіл користувача в системі.

## 13. Open Questions

1. Чи має `Unit` одночасно бути Organization і Resource, чи потрібна окрема проєкція Organization у Resource?
2. Чи всі інфраструктурні об’єкти є Resource, чи частина з них належить Environment?
3. Чи потрібен окремий Concept `Resource Group` для тимчасового об’єднання ресурсів?
4. Яким Concept описується поточна доступність Resource?
5. Яким Concept описується готовність Resource?
6. Чи Assignment є єдиним механізмом залучення інфраструктурних і витратних ресурсів до Operation?
7. Як моделюється взаємозамінність однотипних Resource?
8. Де проходить межа між Resource і Capability?

## 14. Deferred Decisions

До завершення `Operation Concept` та `Assignment Concept` відкладаються:

- модель доступності;
- модель готовності;
- модель поточного використання;
- конфлікти одночасного призначення;
- остаточна роль `State`;
- остаточний lifecycle операційного стану Resource.
