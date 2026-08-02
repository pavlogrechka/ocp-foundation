---
Document-ID: OCP-006
Title: Constraint Concept
Version: 0.2.0
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

Constraint відокремлює:

- факт або candidate state моделі;
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
| Operation | Accepted | можливий context або subject |
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

Два Constraint можуть використовувати однаковий predicate, але мати різні subjects, parameters, applicability, enforcement або provenance.

Після Establishment зміна predicate, target specification, parameters або enforcement semantics створює новий Constraint. Новий Constraint може посилатися на попередній через `supersedes_constraint_ref`.

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
- created_at
- established_at [derived projection]
- retired_at [derived projection]
- establishment_provenance_ref [derived projection]
- supersedes_constraint_ref [optional]
```

`Established lineage` означає lifecycle stages `Established` або `Retired`.

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

За однакових input snapshot, evaluation time, predicate version і parameters результат повинен бути детермінованим або явно позначеним `indeterminate`.

### 6.3 EnforcementSpecification

`EnforcementSpecification` є локальною структурою:

```text
EnforcementSpecification
- mode: blocking | advisory
- indeterminate_disposition: block | require_review | allow
```

- `blocking` означає, що порушення впливає на допустимість candidate context;
- `advisory` фіксує finding, але саме по собі не робить context недопустимим;
- `indeterminate_disposition` визначає обробку недостатніх даних.

Значення `allow` для indeterminate є явним рішенням конкретного Constraint і не може бути системним припущенням за замовчуванням.

Для `advisory` Constraint відомий результат `violated` залишається finding і сам по собі не змінює admissibility. Результат `indeterminate` з disposition `require_review` може дати `review_required`, оскільки система не має достатніх даних для автоматичного завершення рішення. `review_required` не означає `inadmissible`; це явна передача контексту на ручний або окремо визначений review workflow.

### 6.4 Validity interval

```text
validity_start [optional]
validity_end [optional]
```

Якщо задані обидві межі, `validity_start < validity_end`.

`validity_end` може бути заданий без `validity_start`, щоб обмежити правило лише верхньою часовою межею.

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

Constraint не застосовується ретроактивно до часу раніше Establishment без окремого майбутнього правила.

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
```

Applicability визначається temporal і target scope, а не наявністю всіх predicate inputs.

Якщо target match існує, але required inputs відсутні або непридатні, результат оцінювання є `indeterminate`, а не `not_applicable`.

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

`evaluated_at` є часом виконання оцінювання, а `ConstraintEvaluationContext.evaluation_time` — часом моделі, для якого виконано оцінювання.

`evaluator_ref` є непрозорим посиланням на реалізацію або сервіс оцінювання й не вводить окремий фундаментальний Concept.

Для конкретної пари `constraint_version_ref + context_ref + input_snapshot_ref` authoritative result повинен бути однозначним.

Локальна effective result визначається так:

```text
effective_constraint_result(Constraint, Context) :=
    not_applicable
        if NOT constraint_applicable_to(Constraint, Context)

    authoritative stored or reproducible result
        if constraint_applicable_to(Constraint, Context)
        AND result ∈ {satisfied, violated, indeterminate}
        AND result is for the exact Constraint version and input snapshot

    indeterminate
        if constraint_applicable_to(Constraint, Context)
        AND (
            no current authoritative result exists
            OR stored result = not_applicable
        )
```

Збережений `not_applicable` для applicable Constraint є суперечливим evaluation і не може створити permissive decision. Він нормалізується до `indeterminate` та підлягає обробці через `indeterminate_disposition`.

Відсутність current evaluation ніколи не трактується як `satisfied`.

## 12. Admissibility Derivation

Локальна blocking effect визначається так:

```text
constraint_blocks(Constraint, Context) :=
    constraint_applicable_to(Constraint, Context)
    AND enforcement.mode = blocking
    AND (
        effective_constraint_result = violated
        OR (
            effective_constraint_result = indeterminate
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

Асиметрія є навмисною: відомий advisory violation уже класифікований і може бути переданий domain workflow, тоді як advisory indeterminate з `require_review` зупиняє лише автоматичне рішення через недостатність даних. `review_required` не прирівнюється до `inadmissible`.

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

Наведені patterns є робочими прикладами, а не канонічною taxonomy.

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
- parameters, що впливають на evaluation result.

Змістовна зміна створює новий Constraint із новою identity та, за потреби:

```text
supersedes_constraint_ref
```

Supersession не Retire попередній Constraint автоматично. Retire виконується явним lifecycle transition.

## 17. Business Rules

1. Constraint у stage `Established` або `Retired` повинен мати повний minimum structural contract.
2. Cancelled Constraint може залишатися неповним, але має identity та валідний `Draft → Cancelled` transition.
3. Кожен Constraint повинен мати явний `indeterminate_disposition`.
4. Відсутність required input при matched target дає `indeterminate`, а не `not_applicable`.
5. Відсутність current evaluation для applicable Constraint трактується як `indeterminate`, а не `satisfied`.
6. Candidate context не може вважатися admissible, якщо хоча б один застосовний Constraint його блокує.
7. Advisory Constraint не блокує candidate context без окремого правила агрегації.
8. Збережене evaluation повинно посилатися на точну версію Constraint та input snapshot.
9. Зміна predicate або enforcement semantics після Establishment створює новий Constraint.
10. Conflict, Risk, Readiness і availability не виводяться з одного violation без окремого прийнятого правила.
11. Domain module може визначати власні predicate namespaces, але не може змінювати Core semantics evaluation results.
12. Constraint не створює lifecycle transition subject автоматично.
13. Authoritative result `not_applicable` допускається лише тоді, коли `constraint_applicable_to(Constraint, Context) = false`.
14. Якщо applicable Constraint має збережений result `not_applicable`, effective result нормалізується до `indeterminate`, а не до permissive outcome.
15. Для advisory Constraint відомий `violated` залишається finding, а `indeterminate + require_review` може зупинити лише автоматичне рішення; `review_required` не є `inadmissible`.

## 18. Semantic Rules

1. Constraint описує правило; EvaluationRecord описує результат застосування правила.
2. `satisfied` не означає, що Operation досягне Objective.
3. `violated` не означає автоматично, що фактична дія припинена.
4. `indeterminate` означає недостатність або невизначеність inputs, а не відсутність Constraint.
5. `not_applicable` означає, що target або temporal scope не відповідає context.
6. Наявність Constraint не означає наявність Conflict.
7. Відсутність збереженого EvaluationRecord не означає, що Constraint satisfied.
8. Constraint не є Permission, Policy, Order або user access rule.
9. Constraint evaluation не є fundamental State.
10. Constraint не успадковується через composition без явного selector або propagation rule.
11. Retired Constraint може залишатися applicable для історичного evaluation time до `retired_at`.
12. `not_applicable` описує невідповідність scope, а не помилку або недостатність evaluator.
13. `review_required` означає необхідність окремого review, а не автоматичну заборону context.

## 19. Invariants

1. Кожен Constraint має рівно один непорожній стабільний `constraint_id`.
2. Два різні Constraint не мають одного й того самого `constraint_id`.
3. Кожен Constraint у Established lineage має TargetSpecification з explicit subject або непорожнім selector.
4. Кожен Constraint у Established lineage має повний PredicateSpecification з непорожніми code, namespace, version та input contract reference.
5. Кожен Constraint у Established lineage має валідний EnforcementSpecification.
6. Якщо задані обидві validity bounds, `validity_start < validity_end`.
7. Кожен ConstraintTransitionRecord має непорожні `transition_id`, `constraint_ref`, допустимі stages, валідний `occurred_at` та непорожній `provenance_ref`.
8. Transition history кожного Constraint дорівнює одному з допустимих лінійних paths у §7.
9. Матеріалізований `lifecycle_stage` відповідає останньому transition або `Draft` для порожньої history.
10. `established_at` заданий тоді й лише тоді, коли history містить `Draft → Established`, і дорівнює timestamp цього record.
11. `retired_at` заданий тоді й лише тоді, коли history завершується `Established → Retired`, і дорівнює timestamp цього record.
12. Матеріалізований establishment provenance заданий тоді й лише тоді, коли існує Establishment transition, і дорівнює його provenance.
13. `created_at` не пізніший за перший transition timestamp, а transition timestamps не зменшуються.
14. Кожен ConstraintEvaluationRecord посилається на існуючий Constraint, точну його version, context, input snapshot та evaluator.
15. Result кожного ConstraintEvaluationRecord належить множині `{satisfied, violated, indeterminate, not_applicable}`.
16. Якщо authoritative ConstraintEvaluationRecord має `result = not_applicable`, тоді `constraint_applicable_to(Constraint, Context) = false`.
17. Якщо `constraint_applicable_to(Constraint, Context) = true`, effective result не може бути `not_applicable`; суперечливий stored result нормалізується до `indeterminate`.
18. Для однакових constraint version, context та input snapshot не може існувати два authoritative evaluation results з різними значеннями.
19. Constraint не може supersede сам себе, а граф `supersedes_constraint_ref` є ациклічним.
20. За однакових predicate version, parameters, input snapshot і evaluation time два детерміновані evaluations не можуть мати різні результати.

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

### Example F — missing evaluation

Applicable blocking Constraint не має evaluation для поточного snapshot. Effective result є `indeterminate`, а не `satisfied`.

### Example G — contradictory not_applicable

Target і temporal scope відповідають context, але evaluator зберіг `result = not_applicable`. Такий record суперечить applicability contract. Effective result нормалізується до `indeterminate`, тому помилка evaluator не може мовчки зробити candidate context admissible.

### Example H — advisory uncertainty

Advisory Constraint із відомим `violated` створює finding без автоматичного блокування. Той самий Constraint із `indeterminate_disposition = require_review` та результатом `indeterminate` створює `review_required`, оскільки автоматичне рішення не має достатніх даних. Це не означає `inadmissible`.

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

До `PR-0006 — Add Executable Ontology Checker` відкладаються:

- перші YAML fixtures для Resource, Operation, Assignment і Constraint;
- executable checks для lifecycle consistency та двосторонніх field invariants;
- reference implementations `assignment_effective_at`, `derived_participates_in`, `constraint_applicable_to`, `effective_constraint_result` і `constraint_set_decision`;
- regression fixtures для accepted review counterexamples, включно з contradictory `not_applicable`;
- перші CI checks.

Повна expression language, production evaluator interface, остаточний snapshot format і versioned implementation contracts залишаються наступними етапами machine-readable foundation.
