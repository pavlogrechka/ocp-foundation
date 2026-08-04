---
Document-ID: OCP-012
Title: Capability Claim Record Contract
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-009, AD-007, P-001
Uses-Patterns: P-001@0.1.0
Used-By: AB-011, Resource Matching, Coordination, Audit
Last-Review: 2026-08-04
---

# OCP-012 — Capability Claim Record Contract

## 1. Людське пояснення

Capability definition відповідає на запитання: **що означає певна здатність?**

CapabilityClaimRecord відповідає на інше запитання: **хто, про який конкретний Resource, яку саме Capability version і за яких умов заявив?**

Наприклад, запис може означати:

> Джерело `SOURCE-001`, у межах своєї визначеної authority, заявило, що Resource `R-001` має Capability `mobility/navigate@v1` за умов `field-context@1`.

Цей запис робить твердження відтворюваним та attributable. Він не перетворює його на об'єктивну істину і не доводить, що Resource готовий, доступний, авторизований або взаємозамінний з іншим Resource.

## 2. Definition

**CapabilityClaimRecord** — окремий identified record, який зберігає одну attributable claim-пропозицію визначеного claimant про один exact Resource та одну exact OCP-009 Capability version, під одним governed claim kind, одним exact condition set і визначеною часовою застосовністю.

OCP-012 реалізує Outcome B, прийнятий AD-007C. CapabilityClaimRecord не є фундаментальним Concept і не додає Concept graph edge.

## 3. Purpose

Контракт не дозволяє holder claim розчинитися у:

- mutable полі Resource;
- membership у Capability Registry;
- поточному UI view;
- newest record або порядку зберігання;
- неатрибутованому derived boolean;
- assessment, certification або Readiness label;
- припущенні, що однакові claims роблять Resources взаємозамінними.

Окрема identity дозволяє exact historical resolution, часову застосовність, withdrawal, branching corrections, evidence snapshots та fail-safe проєкцію без переписування попередніх заяв.

## 4. Ontological boundary

CapabilityClaimRecord є authoritative лише щодо вузького факту attribution:

> визначений claimant, під визначеною authority і provenance, записав визначену claim-пропозицію.

Він не є автоматично authoritative щодо:

- objective truth або independent verification;
- Capability definition чи registry membership;
- Resource identity, class або equality;
- Readiness, availability, capacity або current fitness;
- authorization, qualification чи operational admissibility;
- Assignment eligibility або Operation success;
- Resource interchangeability;
- assessment або certification.

Evidence підтримує attribution та інтерпретацію claim. Воно не змінює record на CapabilityAssessmentRecord і не створює оцінку, якої claimant не робив.

## 5. Initial holder and Capability boundary

Початковий direct holder type:

```text
resource@1
```

`holder_ref` exact-resolves рівно в один valid OCP-003 Resource. Organization holder не допускається до окремого рішення AB-006 та AB-052.

`capability_ref` має exact OCP-009 binding:

```text
namespace
capability_id
version
```

Resolver не переходить на newest або superseding Capability version. Unresolved, malformed чи ambiguous exact reference робить claim неавторитетним.

## 6. Minimal record

```text
CapabilityClaimRecord
- claim_id
- claim_kind_ref
- holder_kind_ref
- holder_ref
- capability_ref
  - namespace
  - capability_id
  - version
- claimant_ref
- condition_set_ref
- assertion
- evidence_bindings[]
  - evidence_kind_ref
  - evidence_ref
- evidence_snapshot_ref [required when evidence_bindings is non-empty]
- support_state
- authority_ref
- effective_from
- effective_until [optional]
- recorded_at
- provenance_ref
- supersedes_claim_ref [optional]
```

## 7. Field semantics

### 7.1 Identity and kind

`claim_id` — stable non-empty record identity, unique in the claim dataset. Однакові holder, Capability, claimant, timestamps або assertion не створюють identity equality.

Початковий governed `claim_kind_ref`:

```text
holder-capability@1
```

Claim kind визначає форму пропозиції, але не її polarity і не authority precedence.

### 7.2 Holder, Capability and claimant

`holder_kind_ref` дорівнює `resource@1`; `holder_ref` exact-resolves Resource.

`capability_ref` exact-resolves OCP-009 definition version. Supersession definition v1 by v2 не переписує historical claim, bound до v1.

`claimant_ref` визначає source, якому належить assertion. Кількість claimants, newest timestamp або record order не визначають, хто має більшу authority.

### 7.3 Conditions

`condition_set_ref` — exact-version reference на governed набір умов інтерпретації. Навіть unconditional claim використовує явне значення, наприклад:

```text
unconditional@1
```

OCP-012 не визначає універсальну condition expression language. Domain owner може визначати condition sets, але не може замінити exact binding поточним implicit context під час replay.

### 7.4 Assertion and withdrawal

Початковий vocabulary:

```text
positive
negative
indeterminate
withdrawn
```

- `positive` — claimant заявив наявність Capability за bound conditions;
- `negative` — claimant заявив відсутність Capability за bound conditions;
- `indeterminate` — claimant не робить ні positive, ні negative assertion;
- `withdrawn` — claimant відкликав попередню заяву в тій самій lineage.

Withdrawal не дорівнює negative polarity. `withdrawn` потребує `supersedes_claim_ref`, але не означає, що Resource не має Capability.

### 7.5 Evidence and support state

Початкові evidence kinds:

```text
event@1
observation-record@1
outcome-assessment-record@1
```

Evidence binding exact-resolves governed record. Duplicate bindings та list-order semantics заборонені.

Якщо `evidence_bindings` непорожній, `evidence_snapshot_ref` exact-resolves immutable snapshot з тим самим normalized binding set. Late evidence створює новий snapshot і новий claim record або successor; попередній snapshot не мутує.

`support_state` описує достатність support для attributable projection, а не objective Capability truth:

```text
declared
sufficient
missing
stale
ambiguous
conflicting
```

`declared` означає пряму claimant declaration без окремого evidence set. Вона може бути authoritative як attributable claim, але не як independent verification.

`missing`, `stale`, `ambiguous` і `conflicting` завжди дають non-permissive effective projection `indeterminate`, навіть якщо stored assertion є `positive`.

### 7.6 Authority, time and provenance

`authority_ref` exact-identifies governed basis, у межах якого claimant має право зробити саме attributable assertion. Наявність authority не сертифікує truth.

`effective_from` та optional `effective_until` утворюють half-open interval `[from, until)`. Відсутній start або invalid interval не є permissive.

`recorded_at` — час створення record; він не є precedence rule. `provenance_ref` зберігає creation act/source.

## 8. P-001 invocation

OCP-012 invokes `P-001@0.1.0` з Modules **A** і **C**.

### 8.1 Required Elements mapping

- stable record identity: `claim_id`;
- owning semantics: OCP-012;
- endpoint contract: directed record-to-Resource `holder_ref` та exact `capability_ref`;
- governed kind: `claim_kind_ref`;
- provenance: `claimant_ref`, `authority_ref`, `recorded_at`, `provenance_ref`;
- validation: OCP-012 invariants, manifest і fixtures;
- authority: attributable record plus fail-safe derivations below.

### 8.2 Module A — Temporal Effectivity

Selected because the same claimant proposition may apply only during a stated interval. Derivation:

```text
capability_claim_effective_at(claim, t)
```

returns true only when `t` belongs to the valid half-open interval.

### 8.3 Module C — Supersession

Selected to preserve correction and withdrawal history.

- self-supersession is invalid;
- target must exact-resolve;
- graph is acyclic;
- branching is allowed so disagreement remains visible;
- successor preserves claim kind, holder, exact Capability version, claimant and condition-set binding;
- prior record remains exact-resolvable;
- timestamp, order or claimant count never chooses a winning head.

### 8.4 Why Module B is not selected

CapabilityClaimRecord has no universal Draft/Active/Closed lifecycle. `positive`, `negative`, `indeterminate` and `withdrawn` describe attributable claim state, not administrative lifecycle stages. Module A governs applicability; Module C preserves replacement history. Adding transition history now would duplicate those contracts without a distinct lifecycle responsibility.

## 9. Exact resolution and heads

```text
resolve_capability_claim(claims, claim_ref)
```

returns exactly one structurally valid record with that identity or no authoritative result.

```text
capability_claim_heads(... exact binding ..., as_of_time)
```

returns all unsuperseded applicable heads for one exact binding:

```text
claim kind + Resource + Capability version + claimant + condition set
```

Historical as-of replay ignores successors whose effectivity has not started. Branches remain visible and sorted output has no authority meaning.

## 10. Fail-safe effective projection

```text
effective_capability_claim(... exact binding ..., as_of_time)
```

returns:

- the one shared assertion when every applicable head has permissive attributable support (`declared` or `sufficient`) and all heads agree;
- `withdrawn` when the applicable agreed head explicitly withdraws the prior claim;
- `indeterminate` for zero heads, conflicting assertions or any `missing`, `stale`, `ambiguous` or `conflicting` support state.

The derivation is scoped to one claimant. OCP-012 does not collapse different claimants into a truth vote and does not define claimant precedence.

AB-011 may receive head records or this exact-bound fail-safe projection only. It may not infer interchangeability from matching claims.

## 11. Human-readable examples

### Example A — declaration without independent assessment

`SOURCE-A` records a positive claim with `support_state: declared`. The record is authoritative only for “SOURCE-A said this.” It remains usable as attributable input and must not be displayed as “verified.”

### Example B — withdrawal

At 08:00 a claimant records `positive`. At 10:00 the same claimant records a successor with `withdrawn`. Historical replay at 09:00 returns `positive`; replay at 11:00 returns `withdrawn`, not `negative`.

### Example C — conflicting correction branches

Two successors of one prior claim say `positive` and `negative`. Both heads remain visible. Neither newest timestamp nor list order wins; the effective projection is `indeterminate`.

### Example D — same claim, different Resources

Resources `R-A` and `R-B` each have a positive claim for the same Capability version. Their Resource identities remain distinct. OCP-012 does not state that they are interchangeable.

## 12. Normative invariants

1. Every claim has a unique non-empty `claim_id`.
2. Initial claim kind is exact `holder-capability@1`.
3. Initial holder kind is only `resource@1`; holder exact-resolves one Resource.
4. Capability exact-resolves one OCP-009 namespace/id/version definition.
5. Claimant, condition set, authority, provenance and recording time are explicit.
6. Claim condition binding is exact-versioned; current context is not substituted during replay.
7. Evidence bindings are unique, versioned, supported and resolvable.
8. A non-empty evidence set exact-matches an immutable evidence snapshot.
9. Non-permissive support cannot yield an effective positive projection.
10. Withdrawal requires a predecessor and is not converted to negative polarity.
11. Module A interval is valid and fail-closed.
12. Module C target resolves, preserves binding identity and forms no cycle.
13. Branching remains visible; timestamp, order, claimant count and source count select no winner.
14. CapabilityClaimRecord does not carry Readiness, availability, authorization, admissibility, Assignment, verification, certification or interchangeability fields.
15. Matching claims do not collapse Resource identities.
16. Organization holders are rejected.

## 13. Executable evidence

The reference checker provides:

- valid evidence-less claimant declaration;
- exact Resource and exact Capability version resolution;
- historical positive-to-withdrawn replay;
- branching positive/negative heads that fail safe in either order;
- stale support that cannot project positive;
- immutable evidence snapshot comparison;
- supersession binding and cycle rejection;
- Organization-holder rejection;
- forbidden Readiness coupling rejection;
- two matching claims that preserve two Resource identities;
- complete validation/derivation manifest equality.

These fixtures test the initial checker envelope, not a production storage schema or universal evidence/trust engine.

## 14. Explicitly not defined

OCP-012 does not define:

- Organization claims;
- a Capability assessment record or extension of OCP-011;
- objective verification, certification or trust scoring;
- claimant precedence or authority aggregation;
- newest-wins, record-order or issuer-count rules;
- Readiness, availability, capacity, authorization or admissibility;
- Assignment eligibility or Operation success;
- Resource interchangeability or AB-011 decision;
- condition expression language;
- production wire schema, persistence API or migration format;
- a new fundamental Concept or Concept graph edge.

## 15. External review questions

External review must try to falsify at least:

1. whether `declared` preserves legitimate unevaluated claims without implying verification;
2. whether `authority_ref` is narrow enough to avoid becoming objective-truth authority;
3. whether withdrawal remains distinct from negative polarity in historical replay;
4. whether Module A plus Module C is sufficient without Module B lifecycle;
5. whether exact condition binding is useful without prematurely defining a condition language;
6. whether the evidence catalog is too narrow or accidentally assessment-shaped;
7. whether branching and multiple claimants always fail safely without timestamp, order or count precedence;
8. whether AB-011 input remains attributable and cannot imply interchangeability;
9. whether any field silently reintroduces Readiness, availability, authorization or Organization holders;
10. whether the document remains understandable to a human reader before checker details.

## 16. Draft status

Revision `0.1.0` is a Draft normative contract for external adversarial review. It does not resolve AB-057 and is not Accepted or Canonical.

Architecture Board acceptance requires exact-head external review, resolution of blocking findings, green checks and a separate explicit owner/Board authorization.
