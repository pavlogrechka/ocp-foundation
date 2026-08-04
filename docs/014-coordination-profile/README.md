---
Document-ID: OCP-014
Title: Coordination Consumer Profile
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-003, OCP-004, OCP-006, OCP-009, OCP-012, OCP-013
Used-By: AB-003, Coordination Workflows
Last-Review: 2026-08-04
Review-After: External adversarial review and Architecture Board decision
---

# OCP-014 — Coordination Consumer Profile

## 1. Людське пояснення

Цей профіль відповідає на вузьке запитання:

> Хто має право сформулювати точну потребу координаційного контексту, яку OCP-013 може перевірити для одного candidate Resource?

Відповідь: governed Coordination consumer, визначений цим профілем і прийнятий Architecture Board. Він може описати потребу конкретної Operation або іншого exact coordination context. Він не може через цю потребу оголосити Resource доступним, авторизованим, обраним чи призначеним.

Наприклад, coordination consumer може вимагати exact Capability versions і condition sets для relay participant у визначеній Operation та часовому інтервалі. OCP-013 може повернути `positive` лише як evidence відповідності candidate цій потребі. Окреме рішення все одно потрібне для authorization, selection, reservation та Assignment.

## 2. Вузький мандат Draft

OCP-013 `0.2.0` вимагає, щоб перший Coordination profile:

1. встановив легітимний governed consumer `owner_ref`;
2. вимагав exact contextual requirement;
3. не переносив до OCP-013 authority щодо availability, authorization, ranking, selection, replacement або Assignment mutation.

Цей Draft реалізує лише цей мандат. Він не визначає повну Coordination Model, workflow погодження, conflict handling, visibility, command, approval, reservation або lifecycle coordination.

## 3. Governed consumer identity

Після окремого прийняття цього документа Architecture Board, єдиним owner reference цього профілю є:

```text
ocp-coordination-consumer@0.1.0
```

Цей reference означає нормативний consumer contract, а не Organization, caller, user, service account, incumbent Resource або checker. Draft status ще не надає йому accepted authority.

Owner має право лише формулювати потребу одного exact coordination context у формі OCP-013 `ResourceInterchangeabilityRequirement`. Він не є джерелом об'єктивної Capability truth, Constraint decision або operational permission.

Нова semantics owner contract потребує нової версії. Alias, display name, caller identity або newest-version lookup не замінює exact owner reference.

## 4. Exact contextual requirement profile

Кожна вимога цього профілю має бути окремим immutable OCP-013 record:

```text
CoordinationResourceRequirement
- requirement_id
- version
- owner_ref: ocp-coordination-consumer@0.1.0
- context_ref
- effective_from
- effective_until [optional]
- capability_bindings[]
  - capability_ref
    - namespace
    - capability_id
    - version
  - condition_set_ref
- provenance_ref
```

`requirement_id@version` exact-identifies одну revision. `context_ref` exact-identifies одну Operation або інший окремо governed coordination context. Bare label, Organization identity, operational area, incumbent Assignment або current context не є exact context reference.

Owner, context, effectivity, Capability version, condition set або provenance semantics не можна переписати in place. Зміна будь-якого з них потребує нової requirement version. Omitted або unresolved binding fail safe і не може бути доповнений caller default.

## 5. Authority chain

Authority залишається розділеною:

- Architecture Board приймає або відхиляє цей consumer profile і тим самим вирішує легітимність exact `owner_ref`;
- coordination consumer формулює лише потребу exact context;
- OCP-012 claimant відповідає лише за attributable Capability claim;
- OCP-006 evaluator відповідає лише за candidate-specific Constraint result;
- OCP-013 rule mechanically derives directional eligibility з exact inputs;
- окремі майбутні contracts мають визначити authorization, selection, reservation та Assignment action.

Жодна ланка не успадковує authority іншої. Timestamp, list order, label, record count, incumbent status або newest revision не обирає authoritative input.

## 6. Direction and non-equivalence

Evaluation зберігає форму:

```text
candidate Resource → exact Coordination requirement
```

`positive` не створює edge між двома Resources. Він не є symmetric або transitive, не змінює Resource identity і не доводить загальну взаємозамінність. Інший context, requirement version, candidate або evaluation time потребує нового evaluation.

## 7. Required fail-safe cases

Coordination consumer не може вважати requirement придатним для OCP-013 evaluation, якщо:

1. `owner_ref` не дорівнює exact accepted profile version;
2. `context_ref` відсутній, ambiguous або не exact-resolves;
3. context поза requirement effectivity interval;
4. Capability або condition-set binding не exact;
5. provenance відсутній або не належить revision;
6. requirement містить availability, authorization, approval, ranking, selection, reservation, replacement чи Assignment-mutation directive;
7. caller намагається підставити owner, context, incumbent або newest record за замовчуванням.

Такі випадки дають no authoritative requirement. Вони не стають `negative` щодо Resource.

## 8. Explicitly not defined

OCP-014 не визначає:

- Coordination як новий fundamental Concept або Concept graph edge;
- command, control, delegation чи Organization hierarchy;
- negotiation, approval, consensus або disagreement workflow;
- shared operational area чи автоматичний обов'язок координуватися;
- Resource availability, readiness, capacity, reservation або allocation;
- authorization, ranking, selection чи replacement;
- Assignment creation, amendment, revocation або lifecycle transition;
- production schema, API, persistence, UI, service або policy engine.

Ці межі не є прихованими TODO всередині цього профілю. Кожна потребує окремого accepted mandate.

## 9. External review questions

Fable review має спробувати спростувати, що:

1. exact owner reference справді називає governed consumer contract, а не caller-controlled identity;
2. requirement profile завжди bind-ить один exact context та immutable revision;
3. Architecture Board acceptance профілю не перетворюється на authorization конкретного Resource;
4. claimant, Constraint evaluator, OCP-013 rule і coordination consumer зберігають окремі authority;
5. жодне поле не smuggle-ить availability, authorization, ranking, selection, replacement або Assignment mutation;
6. directionality не створює Resource equality, symmetry, transitivity або новий graph edge;
7. fail-safe cases не перетворюються на durable negative про Resource;
8. текст залишається зрозумілим без checker code.

## 10. Draft status

Revision `0.1.0` є Draft для external adversarial review. Він не активує `ocp-coordination-consumer@0.1.0`, не вирішує AB-003 і не надає production authority. Прийняття потребує exact-head Fable approval, Codex adjudication, green CI та окремої explicit Pavlo/Architecture Board authorization; дозволений merge method — squash.
