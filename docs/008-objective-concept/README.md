---
Document-ID: OCP-008
Title: Objective Concept
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, AD-003
Used-By: Operation Concept, Planning, Coordination Model, Event Model, Result Model
Defines-Concepts: Objective
Concept-Depends-On: []
Concept-Status: Under Review
Last-Review: 2026-08-03
---

# Objective Concept

## 1. Definition

**Objective** — ідентифікований intended outcome, condition або effect операційної діяльності.

Objective є семантично повним без наявної Operation. Він може існувати до планування першої Operation та може бути спільним для кількох Operation.

Objective не описує саму діяльність, не надає повноваження на її виконання і не засвідчує досягнення intended outcome.

## 2. Purpose

Objective надає стабільну identity для операційного наміру, на який можуть посилатися Operation, planning та coordination workflows, а майбутні Event і Result — подавати evidence або evaluation.

Objective дозволяє відокремити:

- intended outcome від діяльності Operation;
- provenance створення від authorization semantics;
- формулювання наміру від evidence його досягнення;
- спільний outcome від окремих Operation, що його підтримують.

## 3. Boundary

Objective не є автоматично:

- Order;
- Task;
- Operation;
- Assignment;
- Constraint;
- Capability;
- Event;
- Result;
- `ExplicitIntentRecord`;
- доказом achievement, success, completion або failure.

Objective не створює Assignment, command relation, authorization або Operation hierarchy.

## 4. Identity

Кожен Objective має стабільний непорожній `objective_id`.

Objective identity не залежить від Operation, Organization, автора, назви плану або кількості споживачів.

Семантична зміна intended outcome, condition або effect створює новий Objective instance. Новий instance може містити `supersedes_objective_ref`, що однозначно посилається на попередній Objective.

Зміна пробілів, форматування або орфографічне виправлення, що не змінює нормалізованого змісту, може зберігати identity лише як явно класифікована non-semantic editorial correction. Визначення предметної еквівалентності залишається відповідальністю застосовного domain rule.

Objective не може supersede сам себе. Supersession не означає автоматичного оновлення Operation references.

## 5. Minimal Structure

Мінімальна структура Objective:

```text
Objective
- objective_id
- statement
- created_at
- provenance_ref
- supersedes_objective_ref [optional]
```

### 5.1 objective_id

`objective_id` є стабільною непорожньою identity Objective.

### 5.2 statement

`statement` описує intended outcome, condition або effect.

Нормалізований `statement` повинен містити щонайменше один символ літери або цифри. Значення лише з пробілів, розділових знаків або службових placeholder невалідні.

Statement не містить вбудованого achievement status. Формулювання на кшталт «досягнуто», «виконано» або «успішно» не перетворює Objective на Result, але domain review повинен перевірити, чи воно справді описує intended, а не observed outcome.

### 5.3 created_at

`created_at` є валідним timestamp створення Objective instance.

### 5.4 provenance_ref

`provenance_ref` є непорожнім opaque reference на attributable source або act of creation.

Наявність provenance не означає authorization, approval, command authority або validity такого джерела. OCP-008 не визначає Authority, Order, Approver, Policy чи Commander.

### 5.5 supersedes_objective_ref

`supersedes_objective_ref` є опційним посиланням на попередній Objective, identity якого замінюється через substantive change.

Це поле не створює Objective hierarchy, decomposition або parent/child semantics.

## 6. Operation Integration

Нормативний snapshot contract активного intent належить OCP-004 §7.

```text
Operation pursues Objective
```

Operation поза `Draft` може задовольнити intent requirement через непорожній список `objective_refs`, якщо кожен identifier:

1. є непорожнім і унікальним у списку;
2. резолвиться рівно в один Objective instance;
3. посилається на Objective, що задовольняє інваріанти OCP-008.

Objective не залежить від Operation. OCP-004 декларує `Operation → Objective` як нормативну Concept dependency, оскільки Operation contract використовує Objective validity та resolution semantics.

## 7. Objective and ExplicitIntentRecord

Objective і локальний `ExplicitIntentRecord` є різними представленнями.

На stage `Draft` Operation може тимчасово містити обидва як authoring state. Жодне не має автоматичного пріоритету.

Поза `Draft` активні representations взаємовиключні:

- або `objective_refs`;
- або валідний `ExplicitIntentRecord`.

Якщо обидві гілки присутні, Operation snapshot невалідний. Core не намагається порівнювати їхній текст, визначати приховану precedence або обирати «кращий» intent.

Promotion з explicit intent в Objective не відбувається автоматично. Потрібно створити окремий Objective instance, зафіксувати його provenance та явно перемкнути активний Operation snapshot. Старий record може залишатися лише в audit history поза активними intent fields.

## 8. Relationships

Поточний Core визначає лише:

```text
Operation pursues Objective
Objective supersedes Objective [optional explicit reference]
```

Objective decomposition, hierarchy, contribution, support, conflict та equivalence relations не визначені.

Якщо майбутня модель таких relations використовуватиме identified relationship records, вона повинна окремо обґрунтувати invocation P-001 та визначити endpoints, type version, provenance і validation contract.

## 9. Achievement and Evidence

Objective не має полів `achieved`, `success`, `failure`, `completed_at` або еквівалентного authoritative achievement status у Core.

Факт виконання Operation не означає досягнення Objective.

Оцінювання досягнення, evidence, confidence, partial satisfaction та conflicting assessments належать майбутнім Event/Result specifications.

## 10. Invariants

1. Кожен Objective має рівно один непорожній стабільний `objective_id`.
2. Нормалізований `statement` містить щонайменше одну літеру або цифру.
3. `created_at` є валідним timestamp.
4. `provenance_ref` є непорожнім opaque reference і не надає authorization semantics.
5. Objective не може посилатися на себе через `supersedes_objective_ref`.
6. Substantive change intended outcome створює новий Objective identity; попередня identity не мутує приховано.
7. Objective validity не залежить від наявності Operation.
8. Objective не містить authoritative achievement evaluation.
9. Supersession не оновлює Operation references автоматично.
10. Кожен Objective reference, який використовується Operation поза `Draft`, резолвиться однозначно у валідний Objective instance.

## 11. Examples

### Example A — shared outcome

Objective `OBJ-001` описує створення визначеного безпечного коридору. Дві незалежні Operation можуть посилатися на `OBJ-001`, не стаючи однією Operation і не утворюючи parent/child автоматично.

### Example B — substantive replacement

Objective `OBJ-002` змінює intended outcome `OBJ-001` не редакційно, а семантично. `OBJ-002.supersedes_objective_ref = OBJ-001`. Existing Operation references не переписуються автоматично.

### Example C — opaque provenance

`provenance_ref = SOURCE-17` забезпечує traceability створення Objective, але OCP-008 не робить SOURCE-17 наказом, authority або approval.

## 12. Non-Examples

Не є Objective самі по собі:

- наказ або дозвіл;
- перелік task;
- план чи Operation;
- факт події;
- Result;
- KPI або measurement record;
- текст без стабільної identity;
- локальний `ExplicitIntentRecord`;
- твердження про фактичне досягнення без intended outcome semantics.

## 13. Explicitly Not Defined

Цей документ свідомо не визначає:

- authorization або command semantics;
- Objective hierarchy чи decomposition;
- priority, weighting або optimization;
- achievement, success, failure або completion evaluation;
- measurement, evidence та confidence;
- Event або Result semantics;
- task allocation;
- inheritance від Operation або Organization;
- automatic conversion з free text;
- domain-specific Objective taxonomy;
- automatic propagation через supersession;
- canonical Objective lifecycle.

## 14. Review Target

Спробувати спростувати специфікацію випадками, де:

1. Objective колапсує в Order, Task або Operation;
2. provenance непомітно стає authorization;
3. achievement semantics просочуються з Event/Result;
4. Objective identity залежить від Operation;
5. substantive change мутує існуючу identity без supersession;
6. Operation поза `Draft` проходить з нерезолвленим Objective reference;
7. Objective та `ExplicitIntentRecord` співіснують поза `Draft` без fail-safe помилки;
8. supersession автоматично переписує споживачів;
9. Objective relationship model неявно вводить hierarchy або P-001 invocation.

## 15. Open Questions

1. Чи потрібна окрема Objective lifecycle після появи Event/Result evidence?
2. Які domain rules визначають semantic equivalence editorial corrections?
3. Чи потрібні typed Objective relations після Coordination?
4. Як представляти partial achievement та conflicting assessments у Result model?
5. Чи потрібна окрема taxonomy для outcome, condition та effect?

## 16. Architecture Board Decision

Поточний статус `Under Review`. Architecture Board decision буде зафіксоване після зовнішнього adversarial review PR-0009.
