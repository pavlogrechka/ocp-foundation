---
Document-ID: OCP-013
Title: Contextual Resource Interchangeability Contract
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-003, OCP-005, OCP-006, OCP-009, OCP-012, AD-008
Used-By: AB-011, Coordination
Last-Review: 2026-08-04
---

# OCP-013 — Contextual Resource Interchangeability Contract

## 1. Людське пояснення

Цей контракт відповідає на вузьке запитання:

> Чи задовольняє визначений Resource одну точну, версіоновану вимогу в одному контексті та в один момент часу?

Відповідь обчислюється з exact requirement, fail-safe Capability-claim inputs і candidate-specific Constraint decision. Вона не каже, що два Resources однакові, загалом еквівалентні, доступні, авторизовані, обрані або вже замінені в Assignment.

Наприклад, `relay-B` може отримати `positive` проти requirement для ролі incumbent `relay-A` о 09:00. Це означає лише: за rule version та input snapshot цього обчислення `relay-B` задовольнив точну вимогу. Зворотний напрямок, інша Operation або 09:30 є окремими обчисленнями.

## 2. Accepted mandate implemented by this Draft

OCP-013 пропонує перший AB-011 normative contract у напрямку Model A, прийнятому AD-008C. Він визначає:

- consumer-owned exact requirement;
- deterministic directional eligibility derivation;
- exact binding до candidate, context, time, claim heads, Constraint snapshot і rule version;
- outcomes `positive`, `negative`, `indeterminate` та `review_required`;
- fail-safe replay та executable counterexamples.

Це Draft для зовнішнього adversarial review. Він не активує Model B assessment path і не надає production authority.

## 3. Defined terms

**ResourceInterchangeabilityRequirement** — версіонований consumer-owned contract, який описує точні Capability versions і condition sets, потрібні в одному governed context та interval.

**contextual eligibility** — відтворюваний результат порівняння одного candidate Resource з одним exact requirement. Це не relation між Resources.

**input snapshot** — exact binding до inputs, використаних одним прогоном. Поточний стан repository або newest record не підставляється під час replay.

## 4. Authority boundary

Requirement owner має authority визначити лише потребу конкретного consumer context. OCP-012 claimant залишається authority лише для attributable Capability claim. OCP-006 evaluator залишається authority для candidate-specific Constraint result. OCP-013 rule authority може лише механічно поєднати ці inputs.

Жоден із цих шарів через OCP-013 не отримує authority щодо:

- Resource identity або equality;
- Readiness, availability, capacity чи reservation;
- authorization, approval, ranking або selection;
- Assignment creation, mutation, revocation чи replacement execution;
- objective Capability truth або independent assessment.

Поля, що намагаються вбудувати ці рішення в requirement чи evaluation envelope, є forbidden coupling і fail safe.

## 5. Directionality and comparison target

Primary comparison має форму:

```text
candidate Resource → exact contextual requirement
```

Requirement може назвати `comparison_target_ref` для пояснення, чию operational need він представляє. Цей reference не перетворює результат на Resource-to-Resource edge.

`B` positive проти requirement `A` не доводить `A` positive проти requirement `B`. Два candidates, positive проти одного requirement, не стають interchangeable між собою. Symmetry і transitivity відсутні, якщо окремий майбутній контракт їх не доведе.

## 6. Requirement envelope

```text
ResourceInterchangeabilityRequirement
- requirement_id
- version
- owner_ref
- comparison_target_ref [optional]
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

Requirement identity є парою `requirement_id@version`. Owner, context, interval, Capability version або condition-set change потребує нової version; in-place semantic rewrite заборонений.

## 7. Requirement field semantics

### 7.1 Identity and version

`requirement_id` стабільно ідентифікує requirement lineage. `version` ідентифікує одну immutable semantics revision. Label, role code або Resource type не є requirement reference.

### 7.2 Owner and provenance

`owner_ref` називає окремо governed consumer contract, який має право сформулювати цю operational need. Caller, incumbent Assignment, Capability Registry чи checker не стають owner за замовчуванням. `provenance_ref` зберігає act, яким revision було створено.

### 7.3 Context and time

`context_ref` exact-identifies Operation або інший governed consumer context. Interval є half-open `[effective_from, effective_until)`. Інший context або час потребує окремого evaluation; результат не переноситься.

### 7.4 Capability bindings

Кожен binding містить exact OCP-009 namespace, Capability identity, version та exact `condition_set_ref`. Duplicate binding invalid. Label matching, newest-version redirect та implicit current condition заборонені.

## 8. Exact resolution

```text
resolve_interchangeability_requirement(requirements, requirement_ref)
```

повертає рівно один structurally valid exact `requirement_id@version` або no authoritative result. Zero чи multiple matches fail closed. `comparison_target_ref`, якщо присутній, exact-resolves окремий Resource, але не змінює його identity.

## 9. Evaluation input

Один deterministic run bind-ить:

```text
- rule_ref
- requirement_ref
- candidate_ref
- context_ref
- evaluation_time
- input_snapshot_ref
- claim_inputs[]
  - holder_ref
  - exact capability_ref
  - condition_set_ref
  - claimant_ref
  - claim_head_refs[]
  - projection
  - input_state
  - effective_at
- constraint_input
  - candidate_ref
  - context_ref
  - evaluated_at
  - input_snapshot_ref
  - decision
```

`claim_inputs` є attributable OCP-012 head projection, не independent truth. `constraint_input` має належати тому самому candidate, context і evaluation time. Snapshot incumbent або іншого candidate не можна повторно використати.

## 10. Deterministic outcome rule

`derive_resource_interchangeability` повертає:

- `positive` — exact requirement resolved; усі required claim projections є exact, effective і positive; candidate-specific Constraint decision є `admissible`; немає unresolved input;
- `negative` — complete governed input містить exact negative Capability mismatch або `inadmissible` Constraint decision;
- `review_required` — complete input прямо повідомляє, що mechanical rule недостатньо;
- `indeterminate` — requirement/owner/snapshot missing, input unresolved, stale, ambiguous, conflicting, withdrawn або mismatched, rule version unknown, чи forbidden coupling attempted.

`indeterminate` і `review_required` не перетворюються на durable negative. `positive` не перетворюється на permission.

## 11. Replay and change

Rule version `resource-interchangeability@1` є частиною derivation context. Exact requirement, candidate, context, time, claim heads, Constraint snapshot та aggregate input snapshot також є bindings.

Зміна будь-якого binding створює новий evaluation. Старий результат не переписується і не переноситься на інший Resource, Assignment, Operation чи час. Unknown rule version fail safe, доки її contract не прийнято окремо.

## 12. Executable evidence

Reference fixture `mandatory-counterexamples.yaml` виконує всі AD-008 §12 counterexamples:

1. matching positive claims зберігають різні Resource identities;
2. однаковий label не приховує різні exact Capability versions;
3. blocking candidate Constraint дає negative;
4. missing або stale claim support дає indeterminate;
5. conflicting claim heads дають indeterminate;
6. incumbent Constraint snapshot не використовується для candidate;
7. інша Operation або time є іншим context;
8. `B → A` і `A → B` обчислюються окремо;
9. два positive candidates не стають interchangeable між собою;
10. positive result не змінює availability чи authorization;
11. Assignment mutation не є допустимим output;
12. role label не замінює governed requirement;
13. condition-set mismatch не дає positive.

Fixture також доводить exact-rule replay та fail-safe behavior для unknown rule version. Checker є executable evidence, а не normative owner або production evaluator.

## 13. Normative invariants

1. Requirement exact-resolves by immutable `requirement_id@version`.
2. Owner, context, effectivity and provenance are explicit.
3. Capability and condition bindings are exact and unique.
4. Candidate Resource identity never changes or merges with target identity.
5. Every claim input binds the candidate, exact Capability, condition, claimant, heads and time.
6. Constraint input binds the same candidate, context and evaluation time.
7. Missing, stale, ambiguous, conflicting, mismatched or unresolved input never yields positive.
8. Negative requires a complete governed mismatch or inadmissible decision.
9. Direction, context, time, snapshots and rule version are not reusable implicitly.
10. No timestamp, list order, label, count or newest-record rule chooses authority.
11. Positive eligibility does not imply availability, authorization, selection or execution.
12. Existing Assignment `resource_ref` is never mutated by this contract.

## 14. Explicitly not defined

OCP-013 does not define a production schema, API, persistence record, cache, ranking engine, availability model, authorization model, selection workflow, replacement workflow, Assignment amendment, Capability truth assessment, Constraint language/freshness, universal requirement language, new fundamental Concept or Concept graph edge.

Model B remains a separate activation path only if a future consumer proves that legitimate evaluator judgment must be retained as shared Foundation evidence.

## 15. External review questions

Fable review should try to falsify whether:

1. the consumer requirement is a sufficiently explicit normative owner rather than caller-controlled data;
2. negative is restricted enough not to become a durable claim about the Resource;
3. `review_required` exposes rather than hides legitimate judgment;
4. claim-head attribution remains visible without treating declarations as truth;
5. candidate-specific Constraint binding prevents incumbent snapshot reuse;
6. directionality, context and rule version make replay unambiguous;
7. all thirteen counterexamples actually exercise the stated boundary;
8. the envelope accidentally smuggles in availability, authorization, ranking, selection or replacement;
9. the contract remains understandable without reading checker code.

## 16. Draft status

Revision `0.1.0` is a Draft normative contract for external adversarial review. AB-011 remains `Planned`; no positive production authority exists until exact-head external approval, blocking-finding resolution, green checks and separate explicit Pavlo/Architecture Board authorization are all present.
