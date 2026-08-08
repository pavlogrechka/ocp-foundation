---
Document-ID: OCP-005
Title: Assignment Concept
Version: 0.2.6
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-004
Used-By: Operation Lifecycle, Resource Availability Model, Readiness Model, Coordination Model, Constraint Model, Domain Models
Defines-Concepts: Assignment
Concept-Depends-On: [Resource, Operation]
Concept-Status: Accepted
Last-Review: 2026-08-08
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

`Assignment` має статус `Accepted` у реєстрі OCP-000 на підставі рішення Architecture Board про схвалення PR-0004.

| Concept | Status | Використання в OCP-005 |
|---|---|---|
| Resource | Canonical | елемент, що залучається |
| Operation | Canonical | контекст залучення |
| Organization | Canonical | не створює Assignment автоматично |
| Capability | Canonical | може перевіряти відповідність ролі |
| Constraint | Accepted | може обмежувати одночасні чи часові Assignment |
| Event | Accepted | можливе джерело історії Assignment |
| Readiness | не зареєстрований окремо | AD-011 R0; не виводиться з Assignment |
| State | не зареєстрований окремо | AD-011 S0; lifecycle Assignment не є shared State |

Поняття зі статусом `Proposed` використовуються лише в межах явно позначених робочих правил. Описові слова `state` або `readiness` не створюють shared foundation authority.

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
- transition_history [authoritative local records]
- lifecycle_stage [derived or materialized projection]
- created_at
- established_at [derived projection; exactly for Established lineage]
- terminal_at [derived projection; exactly for Closed or Revoked]
- provenance_ref [derived establishment provenance]
- supersedes_assignment_ref [optional]
```

`Established lineage` означає lifecycle stages `Established`, `Closed` або `Revoked`.

`transition_history` є авторитетним джерелом lifecycle. Поля `lifecycle_stage`, `established_at`, `terminal_at` і `provenance_ref` можуть бути матеріалізовані для пошуку або інтеграції, але не є незалежними джерелами істини та повинні однозначно відтворюватися з transition history.

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

Establishment provenance зберігається в transition record `Draft → Established`. Матеріалізований `provenance_ref` Assignment, якщо він використовується, повинен дорівнювати `provenance_ref` цього transition record.

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
- transition_id
- assignment_ref
- from_stage
- to_stage
- occurred_at
- provenance_ref
```

### 7.6 Authoritative transition history

Transition history одного Assignment повинна утворювати рівно один із допустимих лінійних шляхів:

```text
[]
[Draft → Established]
[Draft → Established, Established → Closed]
[Draft → Established, Established → Revoked]
[Draft → Cancelled]
```

Порожня history означає поточний stage `Draft`.

Для одного Assignment:

- `Draft → Established` і `Draft → Cancelled` є взаємовиключними;
- після `Draft → Established` може існувати не більше одного terminal transition;
- `Established → Closed` і `Established → Revoked` є взаємовиключними;
- `from_stage` наступного record дорівнює `to_stage` попереднього;
- `occurred_at` records не зменшується;
- поточний `lifecycle_stage` дорівнює `to_stage` останнього record або `Draft`, якщо history порожня.

Проєкції визначаються однозначно:

```text
established_at(Assignment)
    := occurred_at of the unique Draft → Established record

terminal_at(Assignment)
    := occurred_at of the unique Established → Closed
       or Established → Revoked record

provenance_ref(Assignment)
    := provenance_ref of the unique Draft → Established record
```

Якщо відповідного transition record немає, відповідна проєкція відсутня.

## 8. Temporal Effectivity

Assignment є ефективним для моменту `t`, якщо одночасно виконуються умови:

```text
assignment_effective_at(Assignment, t) :=
    established_at(Assignment) is defined
    AND established_at(Assignment) <= t
    AND applicability_start <= t
    AND (applicability_end is absent OR t < applicability_end)
    AND (terminal_at(Assignment) is absent OR t < terminal_at(Assignment))
```

Derivation використовує проєкції з авторитетної transition history, а не незалежно введені timestamps або stage.

`terminal_at` означає час `Closed` або `Revoked`. Поточний terminal lifecycle stage не скасовує історичну ефективність до `terminal_at`.

До окремого рішення про ретроактивне Establishment Assignment не може бути ефективним для часу раніше `established_at`.

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

Це derivation rule, а не інваріант. OCP-005 §§8–9 є єдиним нормативним місцем визначення цих формул.

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

Supersession означає намір замінити попередній Assignment у визначеному контексті, але саме по собі не завершує, не відкликає та не змінює його temporal effectivity.

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
8. Якщо новий Assignment має `supersedes_assignment_ref`, replacement process повинен містити явний terminal transition попереднього Assignment відповідно до replacement policy. Допустимий порядок, overlap або gap між Establishment нового та terminal transition попереднього визначаються Constraint або amendment rule; supersession не створює цей перехід автоматично.

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
10. Матеріалізовані `lifecycle_stage`, `established_at`, `terminal_at` і `provenance_ref` є проєкціями transition history та не можуть редагуватися незалежно від неї.

## 16. Invariants

1. Кожен Assignment має рівно один непорожній стабільний `assignment_id`.
2. Два різні Assignment не мають одного й того самого `assignment_id`.
3. Кожен Assignment у stage `Established`, `Closed` або `Revoked` має рівно один resolvable `resource_ref` і рівно один resolvable `operation_ref`.
4. Після transition `Draft → Established` значення `resource_ref` та `operation_ref` є незмінними.
5. Кожен Assignment у stage `Established`, `Closed` або `Revoked` має RoleSpecification, нормалізований `role_code` якого містить щонайменше одну літеру або цифру.
6. Кожен Assignment у stage `Established`, `Closed` або `Revoked` має `applicability_start`.
7. Якщо `applicability_end` заданий, `applicability_start < applicability_end`.
8. Кожен AssignmentTransitionRecord має непорожні `transition_id`, `assignment_ref`, допустимі `from_stage` і `to_stage`, валідний `occurred_at` та непорожній `provenance_ref`.
9. Transition history кожного Assignment дорівнює одному з п’яти допустимих лінійних шляхів, визначених у §7.6; розгалуження, повторний вихід з одного stage і одночасні взаємовиключні переходи заборонені.
10. Матеріалізований `lifecycle_stage` дорівнює `to_stage` останнього transition record або `Draft`, якщо history порожня.
11. `established_at` заданий тоді й лише тоді, коли history містить `Draft → Established`, і дорівнює `occurred_at` цього єдиного record.
12. `terminal_at` заданий тоді й лише тоді, коли history завершується `Established → Closed` або `Established → Revoked`, і дорівнює `occurred_at` цього єдиного terminal record.
13. Матеріалізований establishment `provenance_ref` заданий тоді й лише тоді, коли history містить `Draft → Established`, і дорівнює provenance цього record.
14. `created_at` не пізніший за `occurred_at` першого transition record, а timestamps transition history не зменшуються.
15. Якщо `terminal_at` заданий, `established_at <= terminal_at`.
16. Assignment не може supersede сам себе, а граф `supersedes_assignment_ref` є ациклічним.

## 17. Examples

### Example A — UAV crew executor

Assignment `A-001` пов’язує Crew Resource `R-CREW-07` з Operation `OP-101`, установлює роль `executor` та часову застосовність. Участь екіпажу в OP-101 виводиться з A-001 лише для часу, коли Assignment ефективний.

### Example B — reserve role

Той самий Crew Resource може мати Assignment `A-002` до тієї самої Operation з роллю `reserve` та іншим applicability interval. A-001 і A-002 залишаються окремими Assignment.

### Example C — EW support

Technical Resource засобу РЕБ отримує Assignment до Operation БпС з роллю `support`. Це не робить операції parent/child і не змінює організаційну належність засобу.

### Example D — replacement

Після відмови борта створюється Assignment `A-011` для іншого Resource з `supersedes_assignment_ref = A-010`. Окремий replacement process явно переводить A-010 до `Revoked`; порядок переходів визначається Constraint або amendment rule.

### Example E — consumable stock

Fuel Stock `FS-001` може бути пов’язаний з Operation через Assignment. Кількість зарезервованого або фактично спожитого пального не визначається самим Assignment.

### Example F — invalid silent termination

Assignment у stage `Established` із довільно заповненим `terminal_at`, але без terminal transition record, є невалідним. Такий запис не може мовчки припинити `derived_participates_in`.

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
11. Яка replacement policy визначає допустимі overlap і gap між старим та новим Assignment?

## 20. Deferred Decisions

До Constraint Concept відкладаються:

- конфлікти одночасного залучення;
- ексклюзивність;
- capacity rules;
- допустимість кількох ролей;
- допустимі overlap і gap під час replacement.

До Capability Concept відкладаються:

- перевірка відповідності Resource ролі;
- substitutability;
- автоматичний підбір заміни.

До перегляду ADR-DRAFT-007 після Constraint відкладаються:

- Readiness і availability;
- operational status Resource;
- derived State Assignment або участі.

До окремих рішень Architecture Board відкладаються:

- Reservation / Allocation;
- Role Taxonomy;
- amendment model;
- quantity model для Consumable Resource;
- provenance taxonomy.

## 21. PATCH accounting — v0.2.3

Revision `0.2.3` синхронізує лише volatile current-status rendering Resource у §4 з окремим Resource lifecycle act: row тепер показує Resource як `Canonical`. Review date і ця accounting note входять до того самого PATCH.

Документ лишається `Draft`, Assignment — `Accepted`. `resource_ref`, exact Resource binding, Assignment identity/lifecycle, participation derivation, role semantics, dependencies, Concept status, graph edges, P-001 invocation і всі інваріанти лишаються незмінними; existing Assignment records не потребують rebinding.

Corrective rollback повертає цей status rendering разом з OCP-003, OCP-000, OCP-002, двома іншими consumer views, generated map і repository accounting через новий reviewed act. Ізольована зміна row або переписування Assignment/Resource history заборонені.


## 22. PATCH accounting — v0.2.4

Revision `0.2.4` синхронізує лише volatile current-status renderings у §4 з чинним OCP-000: Organization, Constraint і Event тепер показані як `Accepted`, а Capability — як `Canonical`. Review date і ця accounting note входять до того самого PATCH.

Документ лишається `Draft`, Assignment — `Accepted`. Жоден оновлений status cell не створює Assignment, участь, authority, availability, Readiness, Organization/Resource mapping, Capability holder або interchangeability inference. Assignment identity/lifecycle, exact Resource/Operation binding, role/applicability semantics, dependencies, Concept status, graph edges, P-001 invocation та existing records/references лишаються незмінними.

Mechanical peer-view validation звіряє тільки registered-Concept rows у current `Concept Status and Dependencies` tables з OCP-000. Воно не визначає статус, не охоплює історичні tables або ASCII `[Status]` tree labels і не замінює Board lifecycle act.

Corrective rollback є новим reviewed synchronization act, виведеним із тодішнього authoritative registry. Він не може відновити stale value, переписати lifecycle history або надати checker незалежний authority.


## 23. PATCH accounting — v0.2.5

Revision `0.2.5` синхронізує лише volatile current-status rendering Organization у §4 з окремим O9C lifecycle act: row тепер показує Organization як `Canonical`. Дата review вже збігається з датою акта; ця accounting note входить до того самого PATCH.

Документ лишається `Draft`, Assignment — `Accepted`. Organization Canonical status не створює Assignment, участь, authority, availability, Readiness, Organization/Resource mapping, Capability holder або interchangeability inference. Assignment identity/lifecycle, exact Resource/Operation binding, role/applicability semantics, dependencies, Concept status, graph edges, P-001 invocation та existing records/references лишаються незмінними.

Mechanical peer-view validation exact-sync-ить цей registered-Concept row з OCP-000, але не визначає статус і не замінює окремий Board lifecycle act. Corrective rollback є новим reviewed atomic synchronization act; він не може ізольовано відновити stale value або переписати Assignment/Organization history.

## 24. PATCH accounting — v0.2.6

Revision `0.2.6` синхронізує лише volatile current-status rendering Operation у §4 з окремим T5 WJ lifecycle act: row тепер показує Operation як `Canonical`. Review date і ця accounting note входять до того самого PATCH.

Документ лишається `Draft`, Assignment — `Accepted`. Operation Canonical status та OCP-017 acceptance не створюють Assignment, participation, role, terminal mutation, authorization, availability, Readiness, outcome або Event inference. Assignment identity/lifecycle, exact Resource/Operation binding, role/applicability semantics, dependencies, Concept status, graph edges, P-001 invocation та existing records/references лишаються незмінними.

Mechanical peer-view validation exact-sync-ить тільки current registered-Concept status із OCP-000; воно не визначає status і не замінює Board act. Corrective rollback повертає цей row лише разом з повним twelve-file WJ projection unit через новий reviewed act.
