---
Document-ID: OCP-008
Title: Objective Concept
Version: 1.0.0
Status: Canonical
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, AD-003, AD-017, P-001
Uses-Patterns: P-001@0.1.0
Used-By: Operation Concept, Planning, Coordination Model, Event and Observation Model, Outcome Assessment Model
Defines-Concepts: Objective
Concept-Depends-On: []
Concept-Status: Canonical
Last-Review: 2026-08-06
---

# Objective Concept

## 1. Definition

**Objective** — ідентифікований intended outcome, condition або effect операційної діяльності.

Objective є семантично повним без наявної Operation. Він може існувати до планування першої Operation та може бути спільним для кількох Operation.

Objective не описує саму діяльність, не надає повноваження на її виконання і не засвідчує досягнення intended outcome.

## 2. Purpose

Objective надає стабільну identity для операційного наміру, на який можуть посилатися Operation, planning та coordination workflows. Event і ObservationRecord за OCP-010 можуть бути evidence, а OutcomeAssessmentRecord за OCP-011 — зберігати окрему attributable evaluation без мутації Objective.

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

Окреме оцінювання досягнення належить governed `OutcomeAssessmentRecord` за OCP-011. Event і ObservationRecord за OCP-010 можуть бути exact evidence, але не встановлюють achievement самі по собі. Confidence, aggregation і advanced partial-satisfaction views не стають полями Objective.

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
- Event occurrence та ObservationRecord semantics, owned by OCP-010;
- OutcomeAssessmentRecord та achievement-evaluation semantics, owned by OCP-011;
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
3. achievement semantics просочуються з Event, ObservationRecord або OutcomeAssessmentRecord;
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

1. Чи потрібна окрема Objective lifecycle/effectivity model, якщо конкретний consumer доведе таку потребу?
2. Чи з’явиться concrete consumer evidence, достатнє для reopening amendment/revision outcomes за AD-017B §35?
3. Чи потрібні typed Objective relations після Coordination?
4. Які additional target, criterion, aggregation або partial-satisfaction views мають розширити OCP-011?
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

## 19. Current lifecycle bridge

Sections 17–18 are preserved historical act records. Their statements that OCP-008 was `Draft`, Objective was `Accepted` and another lifecycle proposal was still required describe the state in which those acts were reviewed; they do not override the current frontmatter or §§19–26.

The current contract keeps the semantic surface in §§1–16. This lifecycle act corrects stale future-facing references to Event/Result ownership, makes the stable compatibility promise explicit and changes status only through the atomic unit in §24. It does not add an Objective field, identity rule, lifecycle/effectivity model, current-head projection or achievement authority.

## 20. Canonical compatibility surface `1.x`

OCP-008 `1.x` preserves these guarantees:

1. Objective is one identified intended outcome, condition or effect and is semantically independent of any Operation.
2. Each `objective_id` names exactly one Objective record with the minimal stored fields `objective_id`, `statement`, `created_at`, `provenance_ref` and optional `supersedes_objective_ref`.
3. The stored normative `statement` is immutable: every changed decoded value creates another Objective and another `objective_id`.
4. Decoded stored value, serialization bytes and display rendering are distinct; formatting-only presentation does not change identity, while writing a changed rendering back creates a new Objective.
5. `provenance_ref` provides attributable creation/replacement traceability and never grants authorization, approval or command authority.
6. Optional P-001 Module C supersession rejects self-reference and cycles, permits visible branching, overlap and gaps, preserves every record and never redirects an exact reference.
7. Existing Operation and OutcomeAssessmentRecord references continue to resolve the exact historical Objective they name; no supersession or lifecycle act rebinds them automatically.
8. Core derives no current/latest Objective and gives no authority to timestamp, record order, text similarity, issuer/reviewer count or consumer count.
9. Objective hierarchy, decomposition, contribution, lifecycle, temporal effectivity, achievement, Readiness and authorization do not arise by implication.
10. OCP-008 continues to invoke exact `P-001@0.1.0` for one endpoint-free identified record and selects only Optional Module C.
11. `Concept-Depends-On: []` remains exact; OCP-004 continues to own the only current Concept edge `Operation → Objective`.
12. The scoped exclusions in §21 remain explicit, and same-identity amendment/revision may reopen only through the evidence gates in AD-017 §35.

`Canonical` is a versioned human-readable compatibility promise over these guarantees. It is not production readiness, observed truth, authorization, complete domain coverage, a claim that every consumer is Canonical or a promise that the contract can never change.

## 21. Scoped exclusions and reopening owners

The following extensions remain outside Objective `1.x` without weakening a current consumer guarantee:

| Scoped extension | Current boundary | Required reopening owner |
|---|---|---|
| hierarchy, decomposition, contribution, support, conflict or equivalence relations | no current Objective identity or exact consumer requires them | separate OCP-001/OCP-016 cycle with a relation semantic owner; explicit P-001 decision if identified records are proposed |
| Objective lifecycle or temporal effectivity | Objective validity and exact resolution have no current/effective projection | separate OCP-008 lifecycle model with authority, history, overlap/gap and fail-safe derivation |
| same-identity amendment or versioned revision | changed stored value creates another exact Objective ID | AD-017 §35 evidence, explicit Board reopening and a complete identity/consumer migration contract |
| domain taxonomy for outcome, condition and effect | the current definition does not claim a closed classification tree | domain-owned taxonomy or a separately routed Core taxonomy act with a concrete consumer |
| automatic free-text conversion, language normalization or semantic equivalence | any attributable input rule runs before Objective creation and cannot rewrite history | separate input/tooling contract; Route I for implementation-only display/editor behavior |
| display metadata and renderer behavior | display is excluded from stored Objective semantics | Route I implementation contract unless concrete evidence justifies another OCP-016 route |
| advanced achievement, aggregation or partial-satisfaction views | OCP-011 owns exact assessment records; Objective has no mutable achievement state | compatible OCP-011 target/criterion/activation extension with its own evidence and authority |

Canonical status neither solves these questions nor forbids them forever. A proposal must use the named route and owner; convenience, age of the document or completed implementation work is not reopening evidence.

## 22. Versioning after `1.0.0`

SemVer applies to the compatibility surface in §20:

- **PATCH** may correct prose, links, examples or review/accounting evidence without changing identity, stored fields, authority, exact resolution, supersession, consumer replay or a non-implication.
- **MINOR** may add a backward-compatible optional clarification or extension only when every existing valid Objective and exact consumer reference retains the same interpretation and all twelve guarantees remain true.
- **MAJOR** is required when a proposal changes the identity key or minimal required structure, permits same-ID stored-value mutation, weakens exact historical resolution, changes provenance authority or Module C behavior, introduces a current/latest selector, invalidates existing consumer replay or removes a §20 non-implication.

A relation, lifecycle/effectivity, taxonomy or amendment proposal is not automatically MINOR merely because it adds fields. It must first pass OCP-001/OCP-016 routing and use MAJOR whenever it weakens or reinterprets the `1.x` guarantees.

OCP document version `1.0.0` is not an Objective record revision, does not rewrite `objective_id` and does not create a common version clock for Objective instances.

## 23. Dependencies, consumers and evidence boundary

The direct OCP dependencies satisfy L2 in the atomic post-act state:

- OCP-000 `1.2.0 / Canonical` owns registry membership and the synchronized Objective row;
- OCP-001 `1.0.0 / Canonical` owns lifecycle, atomicity, L2 and authorization choreography; and
- OCP-002 `1.2.0 / Canonical` owns the exact Concept-status projection.

AD-003 and AD-017 remain Accepted decision provenance under their own artifact lifecycle. OCP-008 retains exact `P-001@0.1.0`; Pattern status remains `Accepted`, and invocation imports only the identified-record form rather than Objective semantics or Canonical status.

Current consumers require no semantic or data migration:

| Consumer | Result of this act |
|---|---|
| OCP-004 Operation `0.8.1 → 0.8.2` | only its two current Objective status renderings change; exact `objective_refs` and `Operation → Objective` remain unchanged |
| OCP-010 Event `0.2.0 / Draft` | byte-unchanged; Event/Observation identity and evidence boundaries remain independent of Objective status |
| OCP-011 OutcomeAssessmentRecord `0.3.0 / Accepted` | byte-unchanged; `target_ref` continues to resolve the exact historical Objective without mutation or redirect |

The existing checker and fixtures witness the mechanically expressible subset: unique Objective IDs, immutable-history correction examples, self/cycle rejection, visible branching, exact historical Operation/assessment resolution, status synchronization, L2 and graph acyclicity. No new fixture is needed because this act introduces no new record behavior. Green checks cannot prove semantic completeness or authorize Canonical status.

## 24. Exact baseline, atomic migration and rollback

The recomputed pre-act baseline is `main@7f59b9b8b6193fa4fb21064562486c082dc4ce42`, tree `3fb6a2ff27de5cd2c02d951df095584f9370fb1f`:

| Input | Version / status | Git blob | SHA-256 |
|---|---|---|---|
| OCP-008 | `0.3.0 / Draft`; Objective `Accepted` | `07756e9129a4f11a826b646831dde01939d89336` | `6965cb2f3fbd695a33b16f5eca061f87b33123ee4321aaa8742f709537e1d2e0` |
| OCP-000 | `1.1.0 / Canonical` | `2d17bcba1062cb4e1dfe9a96d395ddcbea2a646d` | `15b1d096f937a9efae46935e99a6253acbf2889d1f75edf646a5d8c588e511cd` |
| OCP-002 | `1.1.0 / Canonical` | `43632bccf76c6be5d2ef1c6127b560e7ef553925` | `fb7540bca35aba7b7e14561a22f2e1b2ea65bdd37f9840f7501e70dee3996911` |
| OCP-004 | `0.8.1 / Draft`; Operation `Accepted` | `c95d05df6059a964df40b1467db1cc17979f3db7` | `f2c15053af5aad6f51a27e45c08978472b2c4199b723bed0e117721cbe4da4f4` |

The lifecycle unit moves or rolls back together:

1. OCP-008 `0.3.0 / Draft → 1.0.0 / Canonical` and defining `Concept-Status: Accepted → Canonical`.
2. OCP-000 `1.1.0 → 1.2.0`, changing only the Objective registry row.
3. OCP-002 `1.1.0 → 1.2.0`, changing its exact Objective projection plus the current Objective paragraph and Operation decomposition label.
4. OCP-004 `0.8.1 → 0.8.2`, changing only the §4 Objective row, the §6 Objective tree label and their local compatibility/rollback note.
5. The generated Foundation map Objective status and README current-status summary/accounting synchronize with the same value.
6. Backlog and roadmap record completion and require a new Board scope act before any third T4 proposal.

These are the complete current Objective status views. Historical Accepted-state act records—including §§17–18, old AD sections and milestone evidence—remain unchanged because they describe their reviewed time.

Existing valid Objective records need no migration. Duplicate-ID data remains invalid or quarantined; this act does not select a winner, merge IDs, synthesize a head, delete history or rebind Operation/assessment references.

Corrective rollback requires a new reviewed act that restores the OCP-008 document/Concept status, OCP-000/OCP-002 values, both OCP-004 renderings, generated map and current repository accounting together. Partial projection rollback is invalid, and rollback cannot rewrite Objective records or consumer history.

## 25. Human counterexamples

1. Objective `OBJ-021` has a later `created_at` than `OBJ-020`, therefore it is the current Objective — false; Core defines no current/latest selector.
2. Two successors supersede one Objective, therefore file order or reviewer count chooses the authoritative branch — false; both branches remain visible exact records.
3. Objective is Canonical, therefore Operation, Event, OutcomeAssessmentRecord or every OCP-011 assessment kind becomes Canonical — false; statuses and compatibility promises do not transfer.
4. A Completed Operation or a positive observation makes its Objective achieved — false; only an exact OCP-011 assessment can state a governed conclusion, and it does not mutate Objective.
5. A renderer fixes spelling and writes the changed text back under the same `objective_id` because display is outside Core — false; write-back changes the stored value and requires a new Objective ID.
6. OCP-008 exact-invokes Accepted P-001, therefore P-001 or another invoker grants Objective semantics or Canonical status — false; Pattern form and domain lifecycle are independent.
7. AD-016G, AD-016H or Q1 was authorized, therefore this lifecycle merge is authorized — false; this exact head requires its own four gates.
8. OCP-000 alone changes Objective to Canonical while OCP-002, OCP-004 or the map remains Accepted — false; that is a non-atomic governance defect.
9. Rollback may change only the generated map because records are untouched — false; every current status projection must roll back together through a new reviewed act.
10. Two Objectives have near-identical statements, therefore they can share one ID or consumer references may redirect by similarity — false.
11. Canonical means hierarchy, lifecycle, taxonomy, display, aggregation and partial satisfaction are complete — false; §21 keeps each extension explicitly scoped and routed.
12. CI is green and all fixtures replay, therefore the lifecycle status is mechanically approved — false; the Architecture Board remains the status authority.

## 26. T4 Objective canonicalization act

This act preserves the Objective semantics in §§1–16 and the historical records in §§17–18. The C cleanup only replaces stale future-facing Event/Result ownership language with the already Accepted OCP-010/OCP-011 boundary. Sections 19–25 make the current lifecycle, compatibility, exclusions, evidence, migration and rollback contracts explicit.

When exact-head reviewed, separately owner-authorized and squash-merged, the act makes OCP-008 `1.0.0 / Canonical` and Objective the second `Canonical` fundamental Concept. Capability remains Canonical; Resource, Operation, Assignment, Constraint, Organization and Event remain Accepted; Proposed registry candidates remain unchanged.

The act adds no Objective record field, Concept, graph edge, schema, checker rule, fixture, display authority, amendment/revision identity, lifecycle/effectivity projection, achievement state or production authority.

AD-016G authorized preparation only; AD-016H and Q1 authorizations are also consumed. Canonical status takes effect only after Fable approval of the exact head, Codex adjudication, green CI, a new explicit Pavlo/Architecture Board authorization specifically for this lifecycle act and squash merge. Its merge does not authorize OCP-003, OCP-007, another T4 candidate or any T5–T10 promotion.
