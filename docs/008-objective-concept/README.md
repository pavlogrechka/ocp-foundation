---
Document-ID: OCP-008
Title: Objective Concept
Version: 0.3.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, AD-003, AD-017, P-001
Uses-Patterns: P-001@0.1.0
Used-By: Operation Concept, Planning, Coordination Model, Event Model, Result Model
Defines-Concepts: Objective
Concept-Depends-On: []
Concept-Status: Accepted
Last-Review: 2026-08-06
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

## 4. Identity and supersession

Кожен Objective має стабільний непорожній `objective_id`.

Objective identity не залежить від Operation, Organization, автора, назви плану або кількості споживачів.

Будь-яка зміна stored normative `statement` value створює новий Objective instance з новим `objective_id`, навіть якщо автор вважає зміну лише виправленням пробілів, орфографії або граматики. Новий instance може містити `supersedes_objective_ref`, що однозначно посилається на попередній Objective.

Це правило застосовується до значення після exact decoding, а не до байтів YAML/JSON serialization. Exact normalization або canonical-input rule, якщо домен використовує його, застосовується до створення Objective і є attributable input rule. Він не може повторно нормалізувати історичний record, переписати `statement` або встановити semantic equivalence після збереження.

Wrapping, typography, font, color, layout та інші display-only choices залишаються поза stored normative `statement`. Renderer може показати те саме значення інакше без зміни Objective. Якщо rendered або corrected form записується назад у `statement`, це вже нове stored value і тому новий Objective.

Domain equivalence opinion може інформувати людське рішення про створення або supersession, але не може зберегти, об’єднати чи перенаправити Core Objective identity. Equal або near-equal statements не колапсують дві Objective identity.

Objective не може supersede сам себе. Граф `supersedes_objective_ref` є ациклічним і перевіряється на рівні повного dataset.

Supersession може розгалужуватися: кілька нових Objective можуть явно supersede один ширший попередній Objective. Це не створює hierarchy або decomposition semantics.

Overlap і gaps між попереднім та новими Objective дозволені, оскільки Core Objective не визначає temporal effectivity. Попередній і новий Objective залишаються валідними identified records; Core не обчислює, який із них «чинний». Operation references не оновлюються автоматично.

`provenance_ref` нового Objective є authoritative provenance його створення та, коли присутній `supersedes_objective_ref`, рішення про заміну. Окремий replacement-act record у Core не вимагається.

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

Після створення `statement` є immutable stored normative value. OCP-008 не визначає display metadata або renderer fields; вони не можуть бути записані у `statement` як спосіб обійти створення нового Objective.

Statement не містить вбудованого achievement status. Формулювання на кшталт «досягнуто», «виконано» або «успішно» не перетворює Objective на Result, але domain review повинен перевірити, чи воно справді описує intended, а не observed outcome.

### 5.3 created_at

`created_at` є валідним timestamp створення Objective instance.

### 5.4 provenance_ref

`provenance_ref` є непорожнім opaque reference на attributable source або act of creation.

Наявність provenance не означає authorization, approval, command authority або validity такого джерела. OCP-008 не визначає Authority, Order, Approver, Policy чи Commander.

### 5.5 supersedes_objective_ref

`supersedes_objective_ref` є опційним посиланням на попередній Objective, який новий Objective явно замінює. Stored statement change завжди створює нову identity, але не зобов’язує Core автоматично оголошувати supersession.

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

На stage `Draft` Operation може тимчасово містити обидва як authoring state. Нерезолвлені, але структурно коректні `objective_refs` також дозволені в `Draft`, оскільки referenced Objective може бути створений пізніше. Жодна гілка не має автоматичного пріоритету.

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
6. Граф `supersedes_objective_ref` між Objective є ациклічним.
7. Будь-яка зміна stored normative `statement` value створює новий Objective identity; попередня identity не мутує приховано.
8. Objective validity не залежить від наявності Operation.
9. Objective не містить authoritative achievement evaluation.
10. Supersession не оновлює Operation references автоматично.
11. Кожен Objective reference, який використовується Operation поза `Draft`, резолвиться однозначно у валідний Objective instance.
12. У межах dataset кожен `objective_id` належить рівно одному Objective record; однаковий ID для equal, near-equal або різних statements невалідний.

Інваріанти 6 і 12 є dataset-level. Інваріант 11 застосовується лише до Operation поза `Draft`. Display exclusion є semantic rule у §§4–5, а не структурним інваріантом над відсутнім display layer.

## 11. Examples

### Example A — shared outcome

Objective `OBJ-001` описує створення визначеного безпечного коридору. Дві незалежні Operation можуть посилатися на `OBJ-001`, не стаючи однією Operation і не утворюючи parent/child автоматично.

### Example B — substantive replacement

Objective `OBJ-002` змінює intended outcome `OBJ-001` не редакційно, а семантично. `OBJ-002.supersedes_objective_ref = OBJ-001`. Existing Operation references не переписуються автоматично.

### Example C — split replacement

Objective `OBJ-010` і `OBJ-011` можуть обидва supersede ширший `OBJ-009`. Усі три records зберігають власну identity; Core не виводить hierarchy або temporal effectivity з такого branching.

### Example D — opaque provenance

`provenance_ref = SOURCE-17` забезпечує traceability створення Objective, а для replacement Objective також простежуваність рішення про заміну. OCP-008 не робить SOURCE-17 наказом, authority або approval.

### Example E — stored spelling correction

Objective `OBJ-020` містить `Establish safe transit corridor`. Виправлена stored form `Establish a safe transit corridor` створює `OBJ-021` з власними `created_at` і `provenance_ref`; вона може містити `supersedes_objective_ref = OBJ-020`.

Operation або assessment, що вже exact-reference `OBJ-020`, продовжує бачити попередній immutable statement. Ні пізніший timestamp, ні текстова схожість не перенаправляють reference на `OBJ-021`.

### Example F — display-only rendering

UI може переносити рядок `OBJ-020.statement`, змінювати font або показувати typographic quotation marks без зміни stored value. Якщо UI або editor записує змінену форму назад у `statement`, це не display-only дія і потребує нового Objective ID.

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
- твердження про фактичне досягнення без intended outcome semantics;
- mutable row, у якому той самий `objective_id` отримує виправлений stored statement;
- amendment head, latest revision або rendered text, що підміняє exact Objective record.

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
- temporal effectivity або canonical Objective lifecycle;
- same-identity amendment чи Objective revision model;
- universal language-equivalence, spelling або text-normalization authority;
- display schema, renderer, typography чи transport serialization.

## 14. P-001 conformance

OCP-008 invokes `P-001@0.1.0` for the endpoint-free identified Objective record.

### 14.1 Required Elements

- stable identity: `objective_id`;
- semantic owner: OCP-008 §§1–14;
- endpoint contract: explicitly endpoint-free; Objective is an assertion of intended outcome, not a relation record;
- governed kind: one governed Core record kind, `Objective`; no free-form kind field is normative;
- provenance: `provenance_ref` records attributable creation and, for a superseding Objective, the replacement decision;
- validation: invariants 10.1–10.12, positive Objective and historical-consumer fixtures, negative duplicate-identity evidence, and supersession-cycle evidence;
- authority: the exact immutable Objective instance is authoritative; no correction head, latest revision, display view, lifecycle, effectivity or achievement projection is authoritative in Core.

### 14.2 Selected Optional Module C — Supersession

- superseded record reference: `supersedes_objective_ref`;
- self-supersession: prohibited by invariant 10.5;
- acyclicity: required by invariant 10.6 and dataset validation;
- branching: allowed; multiple successor Objective may supersede one prior Objective;
- overlap and gaps: allowed because Module A is not selected and Objective has no Core effectivity interval;
- record effective during overlap: not defined; prior and successor records remain valid identified Objectives;
- replacement provenance: `provenance_ref` of the new Objective is authoritative; no separate replacement-act record is required;
- prior history and consumer references: never rewritten automatically;
- stored statement change: represented only by another Objective record with another `objective_id`; Module C may link that record but never mutates the prior one.

Modules A and B are intentionally not selected: OCP-008 defines neither temporal effectivity nor lifecycle transition history. P-001 supplies record form only; all Objective semantics remain defined here.

## 15. Review Target

Спробувати спростувати специфікацію випадками, де:

1. Objective колапсує в Order, Task або Operation;
2. provenance непомітно стає authorization;
3. achievement semantics просочуються з Event/Result;
4. Objective identity залежить від Operation;
5. substantive change мутує існуючу identity без supersession;
6. supersession graph утворює цикл або branching не має визначеної семантики;
7. Operation поза `Draft` проходить з нерезолвленим Objective reference;
8. Objective та `ExplicitIntentRecord` співіснують поза `Draft` без fail-safe помилки;
9. supersession автоматично переписує споживачів або мовчки створює effectivity;
10. Objective relationship model неявно вводить hierarchy або неповне P-001 invocation;
11. editorial label, text similarity або newest timestamp дозволяє той самий `objective_id` з іншим stored statement;
12. display renderer записує змінений text назад у `statement` без створення нового Objective.

## 16. Open Questions

1. Чи потрібна окрема Objective lifecycle після появи Event/Result evidence?
2. Чи з’явиться concrete consumer evidence, достатнє для reopening amendment/revision outcomes за AD-017B §35?
3. Чи потрібні typed Objective relations після Coordination?
4. Як представляти partial achievement та conflicting assessments у Result model?
5. Чи потрібна окрема taxonomy для outcome, condition та effect?

## 17. Architecture Board Decision

Architecture Board прийняла Objective як `Accepted` після зовнішньої реверифікації PR-0009. Це рішення приймає поточну boundary, P-001 conformance, supersession contract, Operation integration і executable evidence як основу подальшої роботи; воно не надає статусу `Canonical` і не визначає відкладені Event/Result, hierarchy, effectivity чи lifecycle semantics.

## 18. AD-017B strict-immutability implementation

AD-017B selected A+D: strict stored-statement immutability plus exclusion of display representation. The exact pre-implementation OCP-008 baseline is Git blob `c1a088aff6e61bf553a100ecb2dd9975a3b67657`, SHA-256 `35f1a24e7f9d085ca3b9a6300d39544d5aa13d660652a34935a38980e96535a2`.

Revision `0.3.0` implements that decision as a MINOR contract change because it removes the former permission for a stored orthographic correction to preserve identity. It:

- makes every changed stored normative value a new Objective identity;
- keeps presentation outside Objective semantics and closes the rendered-text write-back loophole;
- retains the exact minimal field set, P-001 binding and Module C supersession model;
- adds AD-017 as the exact decision-provenance dependency without changing the Concept dependency graph;
- adds dataset-level duplicate-identity rejection and synthetic branching/consumer replay evidence;
- keeps OCP-004 Operations and OCP-011 assessments exact-bound to their historical Objective IDs; and
- resolves AB-063 without changing Objective status, any Concept projection, dependency, graph edge, other OCP, Pattern version or promotion scope.

The checker proves only finite structural cases: duplicate identity rejection, exact prior consumer resolution, visible branching and order independence. It does not decide semantic equivalence, choose a current Objective or validate a UI renderer.

`ObjectiveCorrectionEvidence` is only a synthetic fixture envelope that composes existing Objective, Operation and OutcomeAssessmentRecord validators. It is not a Concept, record kind, relationship, graph node or reusable authority.

OCP-008 remains `Draft` and Objective remains `Accepted`. A fresh blocker/stability/compatibility audit and a new Board scope act are required before any promotion proposal. This implementation takes effect only after exact-head Fable review, Codex adjudication, green CI, separate explicit Pavlo/Architecture Board authorization and squash merge; AD-017B authorization cannot be reused.
