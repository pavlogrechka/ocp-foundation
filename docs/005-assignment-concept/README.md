---
Document-ID: OCP-005
Title: Assignment Concept
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-004
Used-By: Operation Lifecycle, Resource Availability Model, Readiness Model, Coordination Model, Constraint Model, Domain Models
Defines-Concepts: Assignment
Concept-Status: Under Review
Last-Review: 2026-08-02
---

# Assignment Concept

## 1. Definition

**Assignment** — ідентифікований контекстний зв’язок, який установлює участь рівно одного `Resource` у рівно одній `Operation`, визначає його операційну роль, часову застосовність та умови залучення.

Assignment є авторитетним Core-представленням участі Resource в Operation.

```text
Assignment assigns Resource to Operation
```

## 2. Purpose

Assignment відокремлює:

- постійну ідентичність і базовий тип Resource;
- організаційну належність Resource;
- конкретну операційну участь;
- роль Resource у визначеній Operation;
- часові межі та умови цієї участі.

Завдяки Assignment той самий Resource може виконувати різні ролі в різних Operation або мати кілька явно відокремлених залучень у межах однієї Operation.

## 3. Scope

Assignment визначає **хто або що залучається, до якої Operation, у якій ролі та в яких часових межах**.

Assignment не визначає сама по собі:

- штатну чи командну належність Resource;
- право власності на Resource;
- повноваження користувача інформаційної системи;
- готовність, доступність або технічну справність Resource;
- достатність Capability для виконання ролі;
- авторизацію самої Operation;
- ексклюзивне резервування Resource;
- кількість, резервування або споживання Consumable Resource;
- факт успішного виконання Operation.

Assignment може бути підставою для перевірки цих аспектів, але не замінює відповідні моделі та правила.

## 4. Concept Status and Dependencies

`Assignment` має статус `Under Review` у реєстрі OCP-000 та визначається цим документом.

| Concept | Status | Використання в OCP-005 |
|---|---|---|
| Resource | Accepted | елемент, що залучається |
| Operation | Accepted | контекст залучення |
| Organization | Proposed | не створює Assignment автоматично |
| Capability | Proposed | може перевіряти відповідність ролі |
| Constraint | Proposed | може обмежувати одночасні чи часові Assignment |
| Event | Proposed | можливе джерело історії Assignment |
| Readiness | Deferred | не виводиться з Assignment автоматично |
| State | Deferred | не визначається цим документом |

Поняття зі статусом `Proposed` або `Deferred` використовуються лише в межах явно позначених робочих або відкладених правил.

## 5. Identity

Кожен Assignment має власну стабільну ідентичність, відмінну від ідентичності Resource та Operation.

Пара `Resource + Operation` не є ідентичністю Assignment. Для тієї самої пари можуть існувати різні Assignment, якщо вони мають різні ролі, часові межі, умови або представляють повторне залучення.

Приклади різних Assignment для тієї самої пари:

- екіпаж як виконавець у першому часовому інтервалі;
- той самий екіпаж як резерв у наступному інтервалі;
- технічний засіб спочатку як основний, а після заміни — як резервний.

Після встановлення Assignment його `resource_ref` і `operation_ref` не змінюються. Заміна Resource або перенесення до іншої Operation створює новий Assignment.

## 6. Minimum Structural Contract

Локальний структурний контракт Assignment:

```text
Assignment
- assignment_id
- resource_ref [required after Establishment]
- operation_ref [required after Establishment]
- role_specification [required after Establishment]
- applicability_start [required after Establishment]
- applicability_end [optional]
- lifecycle_stage
- created_at
- established_at [required for Established lineage]
- terminal_at [required for Closed or Revoked]
- provenance_ref [required for Established lineage]
- supersedes_assignment_ref [optional]
```

`Established lineage` означає lifecycle stages `Established`, `Closed` або `Revoked`.

Цей перелік визначає мінімальні перевірні поля Concept, але не є схемою бази даних чи API.

### 6.1 Resource and Operation references

- `resource_ref` посилається рівно на один існуючий Resource;
- `operation_ref` посилається рівно на одну існуючу Operation;
- один Assignment не може групувати кілька Resource або кілька Operation.

Для групового залучення використовується:

- один Resource, який сам представляє визначену групу; або
- окремий Assignment для кожного Resource.

### 6.2 RoleSpecification

`RoleSpecification` є локальною структурою Assignment, а не окремим фундаментальним Concept:

```text
RoleSpecification
- role_code
- role_namespace [optional]
- role_parameters [optional]
```

Нормалізований `role_code` повинен містити щонайменше один символ літери або цифри. Значення та допустимі параметри визначаються Core або domain classification rules.

Приклади робочих ролей:

- executor;
- coordinator;
- support;
- reserve;
- observer;
- payload;
- relay.

Цей список не є канонічною Role Taxonomy.

### 6.3 Applicability interval

Assignment Established lineage має часову застосовність:

```text
applicability_start
applicability_end [optional]
```

`applicability_end` може бути відсутнім лише коли завершення не визначено. Якщо воно задане, воно повинно бути пізнішим за `applicability_start`.

Applicability interval не є lifecycle Assignment і не вводить окремий Concept `Time Interval`.

### 6.4 Provenance

`provenance_ref` є непорожнім непрозорим посиланням на рішення, правило, Event, Order, системну дію або інший доказ установлення Assignment.

Наявність provenance перевіряє простежуваність, але цей документ не визначає окремий фундаментальний Concept джерела повноваження.

## 7. Working Lifecycle

Дозволені переходи робочого lifecycle запису Assignment:

```text
Draft → Established
Draft → Cancelled
Established → Closed
Established → Revoked
```

Lifecycle запису не дорівнює часовій чинності Assignment і не є значенням фундаментального Concept `State`.

### 7.1 Draft

Assignment створений, але може мати неповні поля або ще не бути авторитетним твердженням про залучення.

### 7.2 Established

Assignment має повний мінімальний контракт, зафіксоване джерело встановлення та може бути використаний для derivation участі у визначених часових межах.

`Established` не означає, що Resource зараз готовий, доступний або фактично виконує дію.

### 7.3 Closed

Assignment завершений у нормальному порядку. Його історична чинність зберігається для часу до завершення.

### 7.4 Cancelled

Draft Assignment скасований до встановлення. Він може залишатися неповним, але зберігає identity та запис переходу `Draft → Cancelled`.

### 7.5 Revoked

Established Assignment достроково припинений. Його історична чинність зберігається до моменту відкликання.

Кожна зміна lifecycle представляється локальним записом:

```text
AssignmentTransitionRecord
- from_stage
- to_stage
- occurred_at
- provenance_ref
```

## 8. Temporal Effectivity

Assignment є ефективним для моменту `t`, якщо одночасно виконуються умови:

```text
assignment_effective_at(Assignment, t) :=
    lifecycle_stage in {Established, Closed, Revoked}
    AND established_at is defined
    AND applicability_start <= t
    AND (applicability_end is absent OR t < applicability_end)
    AND (terminal_at is absent OR t < terminal_at)
```

`terminal_at` означає час `Closed` або `Revoked`. Поточний lifecycle stage не скасовує історичну ефективність до `terminal_at`.

Точна модель часових значень і часових зон буде визначена окремо. OCP-005 фіксує лише логічні межі derivation.

## 9. Participation Derivation

Авторитетна участь Resource в Operation виводиться через ефективний Assignment:

```text
derived_participates_in(Resource, Operation, t) :=
    exists Assignment a such that
        a.resource_ref = Resource
        AND a.operation_ref = Operation
        AND assignment_effective_at(a, t)
```

Це derivation rule, а не інваріант.

Пряме авторитетне ребро:

```text
Resource participates_in Operation
```

у Core не зберігається незалежно від Assignment. Воно може бути матеріалізованим похідним представленням, якщо зберігає посилання на Assignment або може бути однозначно перебудоване з Assignment.

## 10. Operational Role Derivation

Операційна роль Resource у контексті Operation виводиться з `role_specification` кожного ефективного Assignment:

```text
derived_operational_role(Resource, Operation, t)
    := role_specification of every effective Assignment
       linking the same Resource and Operation at t
```

Resource може мати більше однієї ролі в одній Operation, якщо це представлено окремими Assignment і не заборонено застосовними Constraint.

Базовий тип Resource не визначає його операційну роль.

## 11. Composition and Non-Inheritance

Assignment застосовується лише до Resource та Operation, указаних безпосередньо в його references.

За замовчуванням:

- Assignment складеного Resource не створює Assignment для його складових Resource;
- Assignment Resource до parent Operation не створює Assignment до child Operation;
- Assignment до child Operation не створює Assignment до parent Operation;
- належність Resource до Organization не створює Assignment;
- однакова Capability не створює взаємозамінний Assignment.

Механізми явного успадкування або масового створення Assignment можуть бути визначені окремими правилами, але повинні створювати простежувані Assignment або derivation records.

## 12. Replacement and Supersession

Заміна Resource в Operation не змінює `resource_ref` існуючого Established Assignment.

Новий Assignment може містити:

```text
supersedes_assignment_ref
```

Це означає, що новий Assignment замінює попередній у визначеному контексті. Попередній Assignment має бути Closed або Revoked відповідно до фактичного завершення.

Supersession не видаляє історію та не змінює ідентичність попереднього Assignment.

## 13. Relationship to Reservation and Capacity

Assignment не означає автоматично:

- ексклюзивне резервування Resource;
- блокування інших Assignment;
- резервування кількості Consumable Resource;
- підтверджену доступність або Readiness.

Одночасні Assignment можуть бути допустимими або конфліктними залежно від Constraint, Capability, часової застосовності та предметних правил.

Окрема модель Reservation, Allocation або Capacity може бути запропонована після Constraint Concept. Цей документ не вводить ці терміни як фундаментальні Concept.

## 14. Business Rules

1. Assignment у lifecycle stage `Established`, `Closed` або `Revoked` повинен мати повний мінімальний структурний контракт.
2. Resource або Operation в Established Assignment не можуть бути замінені редагуванням references; створюється новий Assignment.
3. Семантична допустимість `role_code` визначається відповідною classification rule.
4. Одночасність кількох Assignment не є автоматичною помилкою; конфлікт визначається застосовними Constraint.
5. Встановлення Assignment не підтверджує Readiness, availability, достатність Capability чи авторизацію Operation.
6. Зміна ролі або applicability після Establishment повинна бути простежуваною. Остаточна amendment model залишається відкритою.
7. Assignment для Consumable Resource визначає залучений керований запас, але не кількість споживання.

## 15. Semantic Rules

1. Assignment є контекстом операційної ролі, а не властивістю базового Resource.
2. Organization membership не створює Assignment.
3. Assignment не змінює Organization membership або ownership Resource.
4. `Established` Assignment не означає поточну участь без виконання temporal effectivity rule.
5. `Closed` або `Revoked` Assignment може залишатися ефективним для історичного часу до `terminal_at`.
6. Assignment не успадковується автоматично через composition Resource або Operation.
7. Assignment не гарантує результат Operation.
8. Materialized participation є похідним представленням і не може бути незалежним джерелом істини.
9. Cancelled Assignment не входить до Established lineage та не використовується в derivation участі.

## 16. Invariants

1. Кожен Assignment має рівно один непорожній стабільний `assignment_id`.
2. Два різні Assignment не мають одного й того самого `assignment_id`.
3. Кожен Assignment у stage `Established`, `Closed` або `Revoked` має рівно один resolvable `resource_ref` і рівно один resolvable `operation_ref`.
4. Після переходу до Established значення `resource_ref` та `operation_ref` є незмінними.
5. Кожен Assignment у stage `Established`, `Closed` або `Revoked` має RoleSpecification, нормалізований `role_code` якого містить щонайменше одну літеру або цифру.
6. Кожен Assignment у stage `Established`, `Closed` або `Revoked` має `applicability_start`.
7. Якщо `applicability_end` заданий, `applicability_start < applicability_end`.
8. Кожен Assignment у stage `Established`, `Closed` або `Revoked` має непорожні `established_at` і `provenance_ref`.
9. Кожен Closed або Revoked Assignment має `terminal_at`, і `established_at <= terminal_at`.
10. Cancelled Assignment не має `established_at`.
11. Assignment не може supersede сам себе, а граф `supersedes_assignment_ref` є ациклічним.
12. Кожен AssignmentTransitionRecord містить один із дозволених переходів, валідний `occurred_at` і непорожній `provenance_ref`.

## 17. Examples

### Example A — UAV crew executor

Assignment `A-001` пов’язує Crew Resource `R-CREW-07` з Operation `OP-101`, установлює роль `executor` та часову застосовність. Участь екіпажу в OP-101 виводиться з A-001 лише для часу, коли Assignment ефективний.

### Example B — reserve role

Той самий Crew Resource може мати Assignment `A-002` до тієї самої Operation з роллю `reserve` та іншим applicability interval. A-001 і A-002 залишаються окремими Assignment.

### Example C — EW support

Technical Resource засобу РЕБ отримує Assignment до Operation БпС з роллю `support`. Це не робить операції parent/child і не змінює організаційну належність засобу.

### Example D — replacement

Після відмови борта його Assignment `A-010` відкликається. Новий Assignment `A-011` посилається на інший Resource та `supersedes_assignment_ref = A-010`.

### Example E — consumable stock

Fuel Stock `FS-001` може бути пов’язаний з Operation через Assignment. Кількість зарезервованого або фактично спожитого пального не визначається самим Assignment.

## 18. Non-Examples

Не є Assignment самі по собі:

- належність Resource до Organization;
- роль, записана без Resource та Operation;
- запис доступності Resource;
- запис Readiness;
- дозвіл користувача в інформаційній системі;
- наказ без конкретного зв’язку Resource–Operation;
- пряме непохідне ребро `Resource participates_in Operation`;
- резервування кількості без визначеного Resource та Operation;
- Operation Template.

## 19. Open Questions

1. Чи потрібен окремий фундаментальний Concept `Reservation`, чи це спеціалізація Assignment або Constraint?
2. Яка amendment model потрібна для зміни role або applicability після Establishment?
3. Чи допускається ретроактивне Establishment Assignment?
4. Чи потрібна окрема Role Taxonomy у Core?
5. Чи повинен Assignment мати окремий scope для частини складеного Resource без створення нового Resource?
6. Як представляти кількість Consumable Resource, зарезервовану або спожиту в Operation?
7. Чи потрібен окремий тип Assignment для coordination, approval або observation roles?
8. Як Constraint визначає конфлікт одночасних Assignment?
9. Чи може один Assignment мати кілька неперервних applicability intervals, чи кожен інтервал потребує окремого Assignment?
10. Які provenance types повинні бути канонічними для Establishment, Revocation і Closure?

## 20. Deferred Decisions

До Constraint Concept відкладаються:

- конфлікти одночасного залучення;
- ексклюзивність;
- capacity rules;
- допустимість кількох ролей.

До Capability Concept відкладаються:

- перевірка відповідності Resource ролі;
- substitutability;
- автоматичний підбір заміни.

До перегляду ADR-DRAFT-007 відкладаються:

- Readiness і availability;
- operational status Resource;
- derived State Assignment або участі.

До окремих рішень Architecture Board відкладаються:

- Reservation / Allocation;
- Role Taxonomy;
- amendment model;
- quantity model для Consumable Resource;
- provenance taxonomy.
