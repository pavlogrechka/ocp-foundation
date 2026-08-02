---
Document-ID: OCP-006
Title: Constraint Concept
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-004, OCP-005
Used-By: Assignment Conflict Model, Operation Planning, Coordination Model, Readiness Review, Domain Models, Conflict Engine
Defines-Concepts: Constraint
Concept-Status: Proposed
Last-Review: 2026-08-02
---

# Constraint Concept

## 1. Definition

**Constraint** — ідентифікована декларативна умова, яка визначає межі допустимості, сумісності або обов’язкової відповідності для одного чи більше операційних елементів у визначеному контексті та часі.

Constraint описує **що повинно залишатися істинним або не повинно відбутися**, але не є самою Operation, Resource, Assignment, Policy, Risk чи Conflict.

Constraint може застосовуватися до:

- Resource;
- Operation;
- Assignment;
- зв’язку або множини таких елементів;
- локального контексту, визначеного domain module.

## 2. Purpose

Constraint надає OCP єдину модель для формального представлення обмежень, необхідних для:

- перевірки одночасних Assignment;
- ексклюзивності;
- місткості та лімітів;
- допустимості кількох ролей;
- часової сумісності;
- допустимого overlap або gap під час replacement;
- предметних правил без включення їх до Core Concept напряму;
- пояснюваної derivation рішень про допустимість.

Constraint дає змогу відокремити:

- факт або планований стан моделі;
- правило, яке до нього застосовується;
- результат оцінювання правила;
- рішення про допустимість;
- майбутню модель Conflict.

## 3. Scope

Constraint визначає правило допустимості або відповідності.

Constraint не визначає сама по собі:

- організаційне або командне повноваження;
- Policy як окремий фундаментальний Concept;
- причину виникнення правила;
- право користувача інформаційної системи;
- Readiness або availability;
- Capability Resource;
- Risk;
- Conflict як окремий факт чи Concept;
- спосіб автоматичного усунення порушення;
- конкретну мову виконуваних виразів;
- UI, API або схему зберігання.

Constraint може бути джерелом derivation для цих моделей лише після окремого прийнятого правила.

## 4. Concept Status and Dependencies

`Constraint` має статус `Proposed` у реєстрі OCP-000 та визначається цим документом для review у PR-0005.

| Concept | Status | Використання в OCP-006 |
|---|---|---|
| Resource | Accepted | можливий subject або учасник оцінювання |
| Operation | Accepted | можливий контекст або subject |
| Assignment | Accepted | основний subject для перевірки сумісності та залучення |
| Capability | Proposed | можливий вхід перевірки відповідності; не визначається тут |
| Event | Proposed | можливе evidence або trigger повторного оцінювання |
| Risk | Proposed | не виводиться автоматично з порушення |
| Conflict | не зареєстрований окремо | порушення Constraint не канонізує Conflict |
| Readiness | Deferred | може залежати від оцінювань, але не визначається тут |
| State | Deferred | evaluation outcome не є фундаментальним State |
| Order | Proposed | можливе provenance джерело, але не обов’язкове |

Поняття зі статусом `Proposed` або `Deferred` не отримують нормативної відповідальності через цей документ.

## 5. Identity

Кожен Constraint має власну стабільну identity.

Ідентичність Constraint не дорівнює:

- тексту правила;
- `predicate_code`;
- набору subject references;
- результату конкретного оцінювання;
- implementation function або database query.

Два Constraint можуть використовувати однаковий predicate, але мати різні:

- subjects;
- параметри;
- applicability intervals;
- enforcement specification;
- provenance;
- domain namespace.

Після Establishment зміна predicate, target specification або enforcement semantics створює новий Constraint. Новий Constraint може посилатися на попередній через `supersedes_constraint_ref`.

## 6. Minimum Structural Contract

```text
Constraint
- constraint_id
- target_specification
- predicate_specification
- enforcement_specification
- validity_start [optional]
- validity_end [optional]
- transition_history [authoritative local records]
- lifecycle_stage [derived or materialized projection]
- established_at [derived projection]
- retired_at [derived projection]
- establishment_provenance_ref [derived projection]
- supersedes_constraint_ref [optional]
```

Це логічний контракт Concept, а не схема БД чи API.

### 6.1 TargetSpecification

`TargetSpecification` є локальною структурою:

```text
TargetSpecification
- explicit_subject_refs [zero or more]
- subject_selector [optional]
- operation_context_ref [optional]
- relation_scope [optional]
```

Constraint повинен мати щонайменше один `explicit_subject_ref` або непорожній `subject_selector`.

`subject_selector` описує правило вибору subject за типом, класифікацією, зв’язком або domain namespace. Конкретна selector language не визначається OCP-006.

`relation_scope` дозволяє оцінювати не лише окремий subject, а й відношення або множину, наприклад кілька ефективних Assignment одного Resource.

TargetSpecification не створює автоматичного успадкування через composition Resource або parent/child Operation.

### 6.2 PredicateSpecification

`PredicateSpecification` є локальною структурою:

```text
PredicateSpecification
- predicate_code
- predicate_namespace
- predicate_version
- input_contract_ref
- parameters [optional]
```

Нормалізовані `predicate_code`, `predicate_namespace`, `predicate_version` та `input_contract_ref` повинні бути непорожніми.

PredicateSpecification описує перевірне правило, але не визначає технологію його виконання.

За однакових input snapshot, часу оцінювання, predicate version і параметрів результат повинен бути детермінованим або явно позначеним `indeterminate`.

### 6.3 EnforcementSpecification

`EnforcementSpecification` є локальною структурою:

```text
EnforcementSpecification
- mode: blocking | advisory
- indeterminate_disposition: block | require_review | allow
```

- `blocking` означає, що порушення впливає на допустимість candidate context;
- `advisory` фіксує finding, але саме по собі не робить candidate context недопустимим;
- `indeterminate_disposition` визначає, як обробляється відсутність достатніх даних.

Значення `allow` для indeterminate є явним рішенням Constraint і не може бути системним припущенням за замовчуванням.

### 6.4 Validity interval

```text
validity_start [optional]
validity_end [optional]
```

Якщо `validity_end` заданий, він повинен бути пізнішим за `validity_start`.

Validity interval описує часову застосовність правила й не є lifecycle Constraint.

## 7. Working Lifecycle

Дозволені переходи:

```text
Draft → Established
Draft → Cancelled
Established → Retired
```

Lifecycle history є авторитетним джерелом поточного stage та lifecycle timestamps.

```text
ConstraintTransitionRecord
- transition_id
- constraint_ref
- from_stage
- to_stage
- occurred_at
- provenance_ref
```

Допустимі history paths:

```text
[]
[Draft → Established]
[Draft → Established, Established → Retired]
[Draft → Cancelled]
```

Проєкції:

```text
established_at(Constraint)
    := occurred_at of the unique Draft → Established record

retired_at(Constraint)
    := occurred_at of the unique Established → Retired record

establishment_provenance_ref(Constraint)
    := provenance_ref of the unique Draft → Established record
```

Матеріалізовані lifecycle fields не можуть редагуватися незалежно від transition history.

## 8. Temporal Effectivity

Constraint є ефективним для моменту `t`, якщо:

```text
constraint_effective_at(Constraint, t) :=
    established_at(Constraint) is defined
    AND established_at(Constraint) <= t
    AND (validity_start is absent OR validity_start <= t)
    AND (validity_end is absent OR t < validity_end)
    AND (retired_at(Constraint) is absent OR t < retired_at(Constraint))
```

Retired Constraint зберігає історичну ефективність для часу до `retired_at`.

## 9. Evaluation Context

Оцінювання Constraint виконується відносно локального `ConstraintEvaluationContext`:

```text
ConstraintEvaluationContext
- context_id
- evaluation_time
- candidate_or_observed: candidate | observed
- subject_refs
- input_snapshot_ref
- operation_context_ref [optional]
```

`input_snapshot_ref` є обов’язковим посиланням на узгоджений набір вхідних фактів, використаних для оцінювання.

Оцінювання candidate context відповідає на питання, чи допустима запропонована зміна. Оцінювання observed context перевіряє вже зафіксований або фактичний стан.

## 10. Applicability

Constraint застосовується до evaluation context, якщо:

```text
constraint_applicable_to(Constraint, Context) :=
    constraint_effective_at(Constraint, Context.evaluation_time)
    AND target_specification matches Context
    AND required predicate inputs are addressable
```

Відсутність необхідних значень input не означає `not_applicable`. Якщо target match існує, але даних недостатньо, результат оцінювання є `indeterminate`.

## 11. Evaluation Result

Результат оцінювання має один із локальних статусів:

```text
ConstraintEvaluationResult
- satisfied
- violated
- indeterminate
- not_applicable
```

Ці значення не є фундаментальним Concept `State`.

Збережене оцінювання представляється локальним record:

```text
ConstraintEvaluationRecord
- evaluation_id
- constraint_ref
- constraint_version_ref
- context_ref
- input_snapshot_ref
- evaluated_at
- result
- evidence_refs [zero or more]
- evaluator_ref
```

`evaluated_at` є часом виконання оцінювання, а `ConstraintEvaluationContext.evaluation_time` — часом моделі, для якого виконано оцінювання. Вони не є взаємозамінними.

## 12. Admissibility Derivation

Локальна blocking effect визначається так:

```text
constraint_blocks(Constraint, Evaluation) :=
    enforcement.mode = blocking
    AND (
        Evaluation.result = violated
        OR (
            Evaluation.result = indeterminate
            AND enforcement.indeterminate_disposition = block
        )
    )
```

Для множини застосовних Constraint:

```text
constraint_set_decision(Context) :=
    inadmissible
        if any applicable Constraint blocks
    review_required
        if none blocks and any applicable indeterminate result
        has indeterminate_disposition = require_review
    admissible
        otherwise
```

Advisory violation залишається finding і не змінює admissibility без окремого правила.

`constraint_set_decision` є derivation rule OCP-006. Воно не замінює authorization, approval або execution decision.

## 13. Violation and Conflict Boundary

`violated` є результатом оцінювання конкретного Constraint відносно конкретного context та snapshot.

Constraint violation:

- не змінює lifecycle subject автоматично;
- не скасовує Assignment автоматично;
- не створює Risk автоматично;
- не є автоматично фундаментальним Conflict;
- не визначає спосіб remediation.

Майбутній Conflict Concept або Coordination Model може агрегувати одне чи більше порушень, але повинен зберігати посилання на ConstraintEvaluationRecord, з якого зроблено висновок.

## 14. Working Constraint Patterns

Наведені нижче patterns є робочими прикладами, а не канонічною taxonomy.

### 14.1 Exclusive Assignment

Перевіряє, чи не існує забороненого overlap ефективних Assignment для визначеного Resource або relation scope.

Одночасність сама по собі не є порушенням. Порушення виникає лише за наявності відповідного Constraint.

### 14.2 Capacity Limit

Перевіряє, чи агреговане demand не перевищує визначений capacity limit.

Quantity, unit, aggregation та measurement semantics повинні бути визначені через окремий input contract. OCP-006 не канонізує модель кількості.

### 14.3 Role Multiplicity

Обмежує кількість або поєднання ефективних Assignment з визначеними `role_code` у конкретному context.

### 14.4 Replacement Continuity

Перевіряє допустимий overlap або gap між попереднім і superseding Assignment.

Сам `supersedes_assignment_ref` не визначає допустимі часові межі; вони задаються параметрами Constraint.

### 14.5 Operation Preconditions

Перевіряє умови, які повинні бути виконані перед визначеним lifecycle transition Operation.

Constraint не виконує transition і не є джерелом авторизації автоматично.

## 15. Composition and Non-Inheritance

За замовчуванням Constraint не успадковується автоматично:

- від складеного Resource до його компонентів;
- від компонента до складеного Resource;
- від parent Operation до child Operation;
- від child Operation до parent Operation;
- через Organization membership;
- через однакову Capability або classification.

Selector або explicit propagation rule може охоплювати такі елементи, але scope повинен бути перевірним і простежуваним.

## 16. Supersession and Change

Established Constraint не змінює незалежно:

- target specification;
- predicate specification;
- enforcement specification;
- параметри, що впливають на результат оцінювання.

Змістовна зміна створює новий Constraint із новою identity та, за потреби:

```text
supersedes_constraint_ref
```

Supersession не Retire попередній Constraint автоматично. Retire виконується явним lifecycle transition.

## 17. Business Rules

1. Constraint поза Draft повинен мати повний minimum structural contract.
2. Blocking Constraint повинен мати явний `indeterminate_disposition`.
3. Відсутність required input при matched target дає `indeterminate`, а не `not_applicable`.
4. Candidate context не може вважатися admissible, якщо хоча б один застосовний Constraint його блокує.
5. Advisory Constraint не блокує candidate context без окремого правила агрегації.
6. Збережене evaluation повинно посилатися на точну версію Constraint та input snapshot.
7. Зміна predicate або enforcement semantics після Establishment створює новий Constraint.
8. Conflict, Risk, Readiness і availability не виводяться з одного violation без окремого прийнятого правила.
9. Domain module може визначати власні predicate namespaces, але не може змінювати Core semantics evaluation results.
10. Constraint не створює lifecycle transition subject автоматично.

## 18. Semantic Rules

1. Constraint описує правило; EvaluationRecord описує результат застосування правила.
2. `satisfied` не означає, що Operation досягне Objective.
3. `violated` не означає автоматично, що фактична дія припинена.
4. `indeterminate` означає недостатність або невизначеність входів, а не відсутність Constraint.
5. `not_applicable` означає, що target або temporal scope не відповідає context.
6. Наявність Constraint не означає наявність Conflict.
7. Відсутність збереженого EvaluationRecord не означає, що Constraint satisfied.
8. Constraint не є Permission, Policy, Order або user access rule.
9. Constraint evaluation не є fundamental State.
10. Constraint не успадковується через composition без явного selector або propagation rule.

## 19. Invariants

1. Кожен Constraint має рівно один непорожній стабільний `constraint_id`.
2. Два різні Constraint не мають одного й того самого `constraint_id`.
3. Кожен Constraint у Established lineage має TargetSpecification з explicit subject або непорожнім selector.
4. Кожен Constraint у Established lineage має повний PredicateSpecification з непорожніми code, namespace, version та input contract reference.
5. Кожен Constraint у Established lineage має валідний EnforcementSpecification.
6. Якщо `validity_end` заданий, `validity_start < validity_end`.
7. Transition history кожного Constraint дорівнює одному з допустимих лінійних paths у §7.
8. Матеріалізований `lifecycle_stage` відповідає останньому transition або `Draft` для порожньої history.
9. `established_at` заданий тоді й лише тоді, коли history містить `Draft → Established`, і дорівнює timestamp цього record.
10. `retired_at` заданий тоді й лише тоді, коли history завершується `Established → Retired`, і дорівнює timestamp цього record.
11. Матеріалізований establishment provenance заданий тоді й лише тоді, коли існує Establishment transition, і дорівнює його provenance.
12. Кожен ConstraintEvaluationRecord посилається на існуючий Constraint, точну його версію, context, input snapshot та evaluator.
13. Result кожного ConstraintEvaluationRecord належить множині `{satisfied, violated, indeterminate, not_applicable}`.
14. Evaluation з result `not_applicable` не може одночасно бути використане як blocking violation.
15. Constraint не може supersede сам себе, а граф `supersedes_constraint_ref` є ациклічним.
16. За однакових predicate version, parameters, input snapshot і evaluation time два детерміновані evaluations не можуть мати різні результати.

## 20. Examples

### Example A — exclusive Resource use

Blocking Constraint застосовується до множини effective Assignment конкретного Resource і забороняє overlap у визначеному context. Без цього Constraint сам факт кількох Assignment не є порушенням.

### Example B — shared capacity

Constraint порівнює агрегований demand кількох Assignment із capacity, визначеним input contract. EvaluationRecord зберігає snapshot та версію predicate.

### Example C — replacement overlap

Constraint дозволяє короткий overlap між попереднім і superseding Assignment, але блокує overlap, більший за параметризований limit.

### Example D — advisory finding

Advisory Constraint повертає `violated`. Candidate context залишається admissible, але finding повинен бути показаний або оброблений за domain workflow.

### Example E — insufficient data

Target match існує, але потрібний input відсутній. Результат — `indeterminate`; подальша дія визначається `indeterminate_disposition`.

## 21. Non-Examples

Не є Constraint самі по собі:

- результат `violated`;
- повідомлення про помилку;
- Conflict;
- Risk;
- permission користувача;
- роль Assignment;
- Capability Resource;
- lifecycle stage Operation;
- запит до бази даних;
- UI validation без онтологічного правила;
- числове значення без predicate та target scope.

## 22. Open Questions

1. Чи потрібен окремий фундаментальний Concept `Conflict`, чи достатньо агрегованого evaluation model?
2. Яка канонічна expression або rule language потрібна для PredicateSpecification?
3. Як визначаються precedence, override та exception між Constraint?
4. Чи допускаються contextual waivers, і яким Concept вони представлені?
5. Яка модель quantity, unit, demand і capacity потрібна для кількісних Constraint?
6. Який строк актуальності має ConstraintEvaluationRecord для dynamic inputs?
7. Чи повинні всі blocking evaluations зберігатися, чи частина може бути відтворюваною derivation?
8. Як Constraint взаємодіє з authorization Operation?
9. Чи є Reservation окремим Concept або результатом Assignment та blocking Constraint?
10. Які Constraint повинні впливати на майбутню Readiness або availability model?
11. Чи потрібна окрема taxonomy constraint kinds у Core?
12. Як виражати Constraint над геометричними, часовими та спектральними relations без включення domain semantics до Core?

## 23. Deferred Decisions

До quantity model відкладаються:

- одиниці вимірювання;
- агрегування demand;
- capacity consumption;
- часткове резервування Consumable Resource.

До Coordination та Conflict models відкладаються:

- канонічний Conflict;
- remediation workflows;
- negotiation та approval між незалежними вертикалями;
- aggregation кількох violations.

До Capability Concept відкладаються:

- capability requirements;
- substitutability;
- automatic matching Resource до role.

До перегляду ADR-DRAFT-007 після Constraint відкладаються:

- availability;
- Readiness;
- operational status;
- межа між derived evaluation та фундаментальним State.

До machine-readable schemas відкладаються:

- expression language;
- evaluator interface;
- snapshot format;
- linter rules;
- deterministic replay contract.
