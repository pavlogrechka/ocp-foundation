---
Document-ID: OCP-002
Title: Concept Taxonomy
Version: 1.6.0
Status: Canonical
Owner: Architecture Board
Depends-On: OCP-000, OCP-001
Used-By: Domain Model, Knowledge Graph, Architecture
Concept-Statuses:
  Resource: Canonical
  Operation: Canonical
  Assignment: Accepted
  Constraint: Accepted
  Organization: Canonical
  Objective: Canonical
  Capability: Canonical
  Event: Canonical
Last-Review: 2026-08-13
---

# Concept Taxonomy

## Мета та межа повноважень

OCP-002 є людськочитаною синхронізованою проєкцією статусів визначених фундаментальних Concept. Він допомагає читачеві орієнтуватися в ontology, але не є другим Concept registry або defining source доменної семантики.

Повноваження розподілені так:

- OCP-000 володіє membership активного Concept registry та status value кожного registry row;
- OCP-001 володіє lifecycle, atomic status choreography і canonicalization rules;
- `Concept-Statuses` у frontmatter цього документа є exact projection визначених Concepts;
- defining OCP володіє identity, responsibility, invariants, exclusions і Concept dependencies;
- generated Foundation map відображає current dependencies, але не створює їх; і
- Architecture Board володіє кожним admission, status, deregistration або reopening act.

Жодна category tree, prose summary, порядок секцій, document version, timestamp або checker result не може змінити ці повноваження.

## Канонічна поверхня `1.x`

OCP-002 `1.x` гарантує:

1. `Concept-Statuses` містить усі й лише Concepts, що мають defining OCP з `Defines-Concepts` і `Concept-Status`;
2. кожен projection key exact-match-ить Concept name у OCP-000 та defining metadata;
3. кожне projected status value exact-match-ить OCP-000 і defining metadata;
4. missing, duplicate, extra або contradictory projection є governance defect, а не дозволом вибрати найновіше чи найзручніше джерело;
5. Concept status change атомарно оновлює OCP-000, OCP-002, defining document і будь-яку generated current-state projection за OCP-001;
6. Proposed registry marker без defining OCP не входить до `Concept-Statuses` і не отримує identity через відсутність або присутність у category view;
7. non-Concept record, local structure, Pattern, rule, profile або category label не входить до `Concept-Statuses`; і
8. усі category/subtype/decomposition/relation trees нижче є ненормативними curated views, явно виключеними з `1.x` compatibility surface.

`Canonical` стабілізує projection contract, а не поточний status кожного Concept назавжди. OCP-002 `1.0.0 / Canonical` не робить projected Concepts канонічними за implication і не приймає жоден Proposed registry candidate; кожна пізніша status change лишається окремим атомарним lifecycle act.

Після `1.0.0`:

- PATCH уточнює prose, link або ненормативний view без зміни projection set/status чи authority boundary;
- MINOR синхронно додає або змінює projection у окремо authorized Concept lifecycle act, не послаблюючи exactness і category exclusions;
- MAJOR змінює projection owner/scope, дозволяє missing/extra/mismatch, робить category view нормативним, надає category label Concept identity/status/dependency або відокремлює OCP-002 update від атомарного lifecycle act.

Version OCP-002 не є версією жодного Concept, category tree або defining OCP. Споживач exact-bind-ить потрібний defining contract окремо.

## Exact Concept status projection

Authoritative projection domain визначається repository state, а не вручну обраним списком: це exact set усіх Concept names із primary OCP metadata `Defines-Concepts`. Для кожного такого імені `Concept-Status` defining document, OCP-000 status і `Concept-Statuses` value тут повинні збігатися.

OCP-000 може містити Proposed candidate marker без defining OCP. Такий marker лишається registry question і не входить до цієї projection, доки окремий lifecycle act не створить defining contract та не виконає атомарну синхронізацію.

Checker перевіряє duplicate keys і set/value exactness, але не вирішує, чи Concept заслуговує статусу, чи достатня його семантика, чи має Board авторизувати перехід. Відсутність machine finding не є admission act.

## Ненормативні curated views

Решта документа допомагає людині побачити поточні визначення, можливі групування та межі. Ці views навмисно не входять до Canonical compatibility surface:

- top-level category tree не є закритим або вичерпним classification contract;
- Resource subtype labels не є автоматично Concepts, registry rows або inheritance model;
- Operation decomposition не створює ownership, containment чи dependency edge;
- Actor equation є explanatory role heuristic, а не identity formula;
- relation vocabulary не є універсальним Relationship model; і
- open questions не блокують projection contract, доки не змінюють його в окремому reviewed act.

Якщо майбутній consumer потребує нормативної категоризації, inheritance, reusable subtype identity або classification registry, proposal проходить OCP-001/OCP-016 cycle з legitimate owner, concrete consumer, evidence та окремим Board act. Розташування label у цьому документі не є таким актом.

## Ненормативний навігаційний верхній рівень

```text
Concept Categories
├── Organization
├── Resource
├── Operation
├── Objective
├── Environment
├── Governance
├── Event
└── Information
```

Ця структура є ненормативним навігаційним view. Вона явно виключена з Canonical surface OCP-002 і може уточнюватися без створення Concept, dependency, inheritance або exhaustive classification claim.

Вузол у цій структурі є лише category label. Категорія не вважається визначеним фундаментальним Concept без окремого defining contract, status projection та рішення Architecture Board. Однаковий label category і визначеного Concept не створює inheritance або нової identity; `Governance` є категорією, а не визначеним Concept.

## Organization

Concept `Organization` має статус `Canonical` і визначений у [OCP-007 — Organization Concept](../007-organization-concept/README.md).

Organization представляє сталу організаційну ідентичність. Структурні, оперативні, адміністративні, support і coordination relations моделюються окремими локальними `OrganizationRelationshipRecord` відповідно до AD-001 та P-001; вони не є універсальним фундаментальним Relationship Concept.

`Organization ≠ Resource`. Можливий mapping до Organizational Resource залишається відкритим і не змінює identity жодного Concept.

## Resource

Concept `Resource` має статус `Canonical` і визначений у [OCP-003 — Resource Concept](../003-resource-concept/README.md) на підставі AD-014, AD-018A, AD-016L та окремого третього T4 lifecycle act.

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

Це дерево є ненормативним subtype view. `Human Resource`, `Person`, `Crew`, `Unit`, `Platform`, `Fuel Stock` та інші labels не отримують окремої Core identity, inheritance semantics або registry membership через цю ілюстрацію.

`Fuel`, `energy` або інший матеріал як абстрактний тип чи значення кількості не є окремим Resource. Resource у витратній гілці представляє ідентифікований керований запас, партію, контейнер, комплект або іншу облікову одиницю.

## Capability

Concept `Capability` має статус `Canonical` і визначений у [OCP-009 — Capability Concept](../009-capability-concept/README.md) на підставі AD-005C, первинного прийняття PR-0010 та окремого T4 lifecycle act за AD-016D.

Capability є reusable definition-layer identity, що визначається governed namespace, stable `capability_id` та exact version. Human-readable label не є identity, а registry membership не створює holder claim, Readiness, availability, authorization або admissibility.

Capability не має поточної фундаментальної Concept dependency. Non-normative edge `Resource ⇢ Capability` залишається future intent до окремого holder-claim decision.

## Operation

Concept `Operation` має статус `Canonical` і визначений у [OCP-004](../004-operation-concept/README.md).

Operation є універсальним контекстом координованої діяльності. Предметні типи визначаються domain або capability modules.

```text
Operation
├── Identity
├── Intent
│   └── Objective [Canonical]
├── Temporal Context
├── Spatial Context
│   └── Local Spatial Binding [Operation-owned structure; not a Concept]
├── Participation
│   └── Assignment [Accepted]
├── Constraints
│   └── Constraint [Accepted]
└── Outcome
    ├── Event [Canonical]
    └── OutcomeAssessmentRecord [Accepted record contract; not a Concept]
```

Це дерево є читабельною decomposition summary, а не containment schema. Нормативні identities, records, local structures і dependencies належать exact defining contracts, на які посилаються підписи.

Event не є Operation lifecycle transition або Operation-owned result field. Operation-to-Event relevance залишається explicit downstream relation/reference question і не створює current Concept dependency.

OutcomeAssessmentRecord не є Operation child object або success field. Він exact-bind-ить незалежний target, criterion, evidence/input snapshots та evaluator за Accepted OCP-011.

AD-014B відхилив current-scope fundamental identity для `Operational Area` і не ввів `Environment` Concept. OCP-004 `0.8.0` представляє spatial context як zero/one/many local versioned bindings owning Operation. Local binding не є P-001 record або graph node; однакові payload, label чи geometry в різних Operation не створюють shared identity.

`Environment` у верхньорівневому дереві лишається **категорією класифікації**, а не зареєстрованим Concept. Environmental conditions можуть бути domain-owned inputs або attributable observations, але не набувають identity, truth, suitability, authorization чи Readiness authority через розташування в taxonomy.

## Objective

Concept `Objective` має статус `Canonical` і визначений у [OCP-008 — Objective Concept](../008-objective-concept/README.md) на підставі AD-003, AD-017, AD-016G та окремого другого T4 lifecycle act.

Objective представляє intended outcome, condition або effect операційної діяльності. Objective має власну identity, не є Operation, Order, Task або `ExplicitIntentRecord`.

Оцінка досягнення Objective належить Accepted governed OutcomeAssessmentRecord у [OCP-011 — Outcome Assessment Record Contract](../011-outcome-assessment-record/README.md) за AD-006C / AB-056. Objective не отримує mutable authoritative achievement status.

Objective не має поточної фундаментальної Concept dependency. Operation нормативно залежить від Objective лише через явну `Concept-Depends-On` декларацію OCP-004.

## Event

Concept `Event` має статус `Canonical` і визначений у [OCP-010 — Event Concept](../010-event-concept/README.md) на підставі outcome E3 у AD-006C, окремого document-promotion act AD-016AD та Event Concept canonicalization act AD-032.

Event представляє reusable occurrence або change identity, незалежну від конкретного report, observer, Operation, Objective або assessment. Event може мати zero, one або many observations.

`ObservationRecord` є окремим attributable identified record за P-001. Він не є фундаментальним Concept, не визначає truth автоматично та може мати optional unresolved Event linkage.

Event має `Concept-Depends-On: []`. Current graph не містить `Operation → Event` або `Event → Operation`; такі зв'язки потребують окремого normative owner.

## OutcomeAssessmentRecord

OutcomeAssessmentRecord має Accepted document contract в OCP-011 як P-001 identified record і **не входить до `Concept-Statuses`**.

Прийнятий baseline contract:

- target kind — exact Objective;
- exact assessment kind і criterion;
- exact Event/ObservationRecord evidence bindings;
- immutable evidence та input snapshots;
- attributable evaluator і provenance;
- fail-safe evidence state та conclusion;
- history-preserving Module C supersession з дозволеним branching;
- жодного latest-record truth selection.

AD-006C відхилив fundamental Result identity. Architecture Board завершила AB-056 прийняттям OCP-011 та видаленням тимчасового `Result: Proposed` marker з OCP-000 і generated Foundation map. `Result` не є Accepted, Deprecated або Archived Concept і не входить до цього taxonomy projection.

## Assignment

Concept `Assignment` має статус `Accepted` і визначений у [OCP-005](../005-assignment-concept/README.md).

Assignment є ідентифікованим контекстним зв’язком рівно одного Resource з рівно однією Operation. Участь Resource в Operation є похідною від ефективного Assignment.

## Constraint

Concept `Constraint` має статус `Accepted` і визначений у [OCP-006](../006-constraint-concept/README.md).

Constraint є ідентифікованою декларативною умовою, яка обмежує допустимість або сумісність операційного context. Constraint violation не є автоматично Event, Conflict, Risk, Readiness, State або OutcomeAssessmentRecord.

## Ненормативна рольова евристика

`Actor` не виділяється в окрему фундаментальну гілку. Діяч є Resource, який отримує роль у конкретному контексті через Assignment.

```text
Resource + Assignment + Operation Context = Operational Role
```

Формула є поясненням поточного role view, а не identity, derivation або admission rule. Нормативні Resource, Assignment та Operation contracts мають перевагу.

## Ненормативна relation vocabulary

Перелік нижче є taxonomy vocabulary, а не універсальною моделлю Relationship:

- Structural;
- Operational;
- Constraint;
- Spatial;
- Temporal;
- Dependency;
- Information.

Конкретна семантика relation належить defining Concept або governed Pattern invocation.

## Питання до наступного рев’ю

Питання нижче належать майбутнім semantic cycles і не входять до OCP-002 `1.x` projection contract:

- Межа Organization / Organizational Resource.
- Organization identity continuity.
- Taxonomy organization relationship kinds.
- Який normative owner визначить Operation-to-Event relevance records?
- Чи потрібні окремі Concept Reservation, Allocation, Role Taxonomy або Conflict?
- Які additional target/evidence kinds та freshness rules мають розширити Accepted OCP-011?

## Fail-safe контрприклади

1. `Environment: Proposed` додається без defining OCP або `Resource` повторюється двічі — extra/duplicate projection відхиляється; category view і YAML overwrite не створюють authority.
2. Defining document оголошує Concept, але projection key відсутній — lifecycle act неатомарний.
3. OCP-000, OCP-002 і defining metadata містять різні status values — mismatch не вирішується timestamp, file order або majority.
4. OCP-002 стає Canonical, а його projected rows інтерпретуються як `Canonical` — document status не передається Concept.
5. `Person` або `Unit` із Resource view використовується як Core subtype identity — illustration не надає inheritance semantics.
6. Operation decomposition використовується для створення implicit `Operation → Event` edge — view не є graph authority.
7. OutcomeAssessmentRecord додається до `Concept-Statuses`, бо має Accepted contract — non-Concept record не стає Concept.
8. Checker проходить, а category placement використовується як Board admission — machine success не є semantic act.
9. Авторизація цього OCP-002 act повторно використовується для P-001 — два T3 lifecycle acts мають окремі gates.
10. Завершення OCP-002 або обох T3 acts автоматично відкриває T4 — хибно; AD-016C/AD-016D були окремими gates, а прийнятий AD-016D дозволяє лише OCP-009 preparation без merge transfer.

## T3 OCP-002 canonicalization act

Pre-T3 OCP-002 `0.17.0 / Draft` baseline має Git blob `ff3a3f56fe7499623758a18c45268eb59ce3cd9e` і SHA-256 `4cfd95df5eb66b5c995eecf533e77a65242082891eefc3564b48a4a94d1a9845`.

T3 обирає **explicit exclusion**, дозволений AD-016B §33: Canonical contract охоплює exact Concept status projection і category-vs-Concept boundary, тоді як working category, subtype, decomposition, role та relation views лишаються ненормативними. Stable-kernel extraction в окремий artifact не потрібний, бо межа читабельно й однозначно проведена in place з одним defining location.

Direct dependencies задовольняють L2:

- OCP-000 `1.0.0 / Canonical` постачає registry membership/status;
- OCP-001 `1.0.0 / Canonical` постачає lifecycle, atomicity та authorization choreography.

На T3 baseline цей act зберіг exact вісім `Accepted` projection rows і не змінив OCP-000, defining metadata або generated map. Він додав fail-safe extra-row validation та regression evidence, але не створив Concept, category registry, inheritance, graph edge, schema, route або production authority. Пізніші окремі lifecycle acts можуть змінювати projected status за Canonical contract вище.

OCP-002 `1.0.0 / Canonical` набуває чинності лише після Fable approval exact head, Codex adjudication, green CI, окремої явної Pavlo/Architecture Board authorization саме для цього T3 OCP-002 act та squash merge. Авторизація T2 не може бути повторно використана. До merge цей розділ і frontmatter є proposed act; merge не авторизує окремий T3 P-001 act і не відкриває T4.

## Revision `1.1.0` — Capability status projection

Окремий T4 lifecycle act exact-sync-ить одну projection value: `Capability: Accepted → Canonical`. За SemVer policy OCP-002 це MINOR revision, тому document version синхронно переходить `1.0.0 → 1.1.0`.

Projection owner, exact set/value rules, category exclusions і fail-safe mismatch behavior лишаються незмінними. Revision не надає Capability semantics і не змінює status жодного іншого Concept або Proposed marker.

## Revision `1.2.0` — Objective status projection

Окремий другий T4 lifecycle act exact-sync-ить одну projection value: `Objective: Accepted → Canonical`. За SemVer policy OCP-002 це MINOR revision, тому document version синхронно переходить `1.1.0 → 1.2.0`.

Поряд із frontmatter projection синхронізовано два поточні human-readable views: Objective label у ненормативному Operation decomposition tree та status sentence у секції Objective. Projection owner, exact set/value rules, category exclusions, fail-safe mismatch behavior, `Operation → Objective` edge і status кожного іншого Concept лишаються незмінними.

## Revision `1.3.0` — Resource status projection

Окремий третій T4 lifecycle act exact-sync-ить одну projection value: `Resource: Accepted → Canonical`. За SemVer policy OCP-002 це MINOR revision, тому document version синхронно переходить `1.2.0 → 1.3.0`.

Поряд із frontmatter projection синхронізовано поточне human-readable status sentence у секції Resource. Ненормативне curated subtype tree лишається байт-ідентичним і не отримує Core taxonomy, inheritance, mapping або authority. Projection owner, exact set/value rules, category exclusions, fail-safe mismatch behavior і status кожного іншого Concept лишаються незмінними.

## Revision `1.4.0` — Organization status projection

Окремий четвертий T4 lifecycle act exact-sync-ить одну projection value: `Organization: Accepted → Canonical`. За SemVer policy OCP-002 це MINOR revision, тому document version синхронно переходить `1.3.0 → 1.4.0`.

Поряд із frontmatter projection синхронізовано поточне human-readable status sentence у секції Organization. Ненормативні category/subtype/decomposition trees лишаються байт-ідентичними; вони не містять Organization lifecycle label і не отримують taxonomy, inheritance, mapping або authority. Projection owner, exact set/value rules, category exclusions, fail-safe mismatch behavior і status кожного іншого Concept лишаються незмінними.

## Revision `1.5.0` — Operation status projection

Окремий T5 WJ lifecycle act exact-sync-ить одну projection value: `Operation: Accepted → Canonical`. За SemVer policy OCP-002 це MINOR revision, тому document version синхронно переходить `1.4.0 → 1.5.0`.

Поряд із frontmatter projection синхронізовано поточне human-readable status sentence у секції Operation. Taxonomy authority, category/decomposition trees, registry membership, dependencies, Operation identity, `Operation → Objective`, Event non-edge та всі інші projected values лишаються незмінними. Жоден non-Concept lifecycle contract не додається до taxonomy.

## Revision `1.6.0` — Event status projection

Окремий Event Concept canonicalization act exact-sync-ить одну projection value: `Event: Accepted → Canonical`. За SemVer policy OCP-002 це MINOR revision, тому document version синхронно переходить `1.5.0 → 1.6.0`.

Поряд із frontmatter projection синхронізовано два поточні human-readable views: Event label у ненормативному Operation decomposition tree та status sentence у секції Event. Projection owner, exact set/value rules, category exclusions, fail-safe mismatch behavior, Event identity, empty `Concept-Depends-On`, `Operation → Objective`, відсутність Operation↔Event current edge та всі інші projected values лишаються незмінними.
