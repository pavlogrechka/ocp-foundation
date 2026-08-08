---
Document-ID: OCP-017
Title: Operation Lifecycle Contract
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: AD-020, OCP-001, OCP-004, OCP-005, OCP-006, OCP-010, OCP-011, OCP-016, P-001
Uses-Patterns: P-001@0.1.0
Used-By: Operation lifecycle review, Operation planning, Assignment alignment, Audit
Last-Review: 2026-08-08
Review-After: First production-facing lifecycle proposal or evidence that a selected owner, path, profile, authorization envelope, terminal alignment or migration boundary is incomplete
---

# OCP-017 — Operation Lifecycle Contract

## 1. Route, authority and scope

OCP-017 is a **Route C Core non-Concept contract** under OCP-016. AD-020A selected Q3I only as the direction for a bounded remediation; a separate owner mandate authorized preparation of OCP-004 `0.9.0 / Draft` and this `0.1.0 / Draft` in one atomic tree.

OCP-017 is the single normative owner of:

- the finite Operation lifecycle stage vocabulary;
- allowed paths between those stages;
- the universal structural minimum and exact domain-profile hook for a transition;
- the evidence-acceptance envelope for entry to `Authorized`;
- authoritative `OperationLifecycleTransitionRecord` history and derived projections; and
- terminal Assignment-alignment evidence.

OCP-004 remains the owner of Operation identity, active intent, temporal/spatial context, composition and bounded IO2 relationship values. OCP-017 depends on that stable identity; OCP-004 does not depend on OCP-017. This direction is intentional and acyclic.

## 2. Purpose in plain language

An Operation answers **what coordinated activity exists and what its context is**. OCP-017 answers a narrower question: **which reviewed transition history supports the Operation's current lifecycle stage, and which exact evidence was checked at each step?**

The distinction matters. A stored label such as `Active` or `Completed` is easy to copy, overwrite or misunderstand. Under this contract the label is never authoritative by itself. A reviewer can follow an explicit predecessor chain, inspect every transition, and reproduce the stage without choosing the newest timestamp, the last YAML item, the most frequent issuer or the most convenient source.

## 3. Explicit boundary and non-implications

OCP-017 does not define or grant:

- a fundamental Concept `Lifecycle`, `State`, `Readiness`, `Authorization` or `Approval`;
- the identity or stable kernel of Operation;
- an authorization source, command mechanism, access-control policy or actor authentication;
- Assignment creation, closure, revocation or mutation;
- Constraint applicability or evaluation truth;
- Event occurrence, causation or automatic generation;
- Objective achievement or outcome assessment;
- Resource availability, suitability, admissibility or interchangeability;
- Organization claims or holder semantics;
- a reusable workflow template; or
- a persistence schema, API, wire format or production validator.

`Authorized` means that the exact evidence envelope required by this contract was accepted for that transition. It does not mean that OCP-017 itself issued permission. `Completed` means lifecycle completion only; it does not mean that an Objective was achieved.

## 4. Lifecycle envelope and Operation endpoint

One lifecycle envelope belongs to exactly one `operation_ref`, which exact-resolves to one OCP-004 Operation. The envelope has no independent lifecycle ID; the Operation remains the subject throughout.

```text
OperationLifecycleEnvelope
- operation_ref
- transition_history [authoritative]
- lifecycle_stage [optional materialized projection]
```

Within one declared dataset:

- every Operation has exactly one envelope;
- every envelope resolves exactly one Operation;
- duplicate or missing envelopes fail closed; and
- extraction never changes, redirects or aliases `operation_id`.

The envelope is not a second record family under P-001. Independent identity belongs to each transition record, not to a wrapper whose subject is already the exact Operation.

## 5. Stages and allowed paths

The closed initial stage vocabulary is:

```text
Draft | Planned | Authorized | Active | Completed | Cancelled | Aborted
```

Allowed transitions are exactly:

```text
Draft      → Planned
Draft      → Cancelled
Planned    → Authorized
Planned    → Cancelled
Authorized → Active
Authorized → Cancelled
Active     → Completed
Active     → Aborted
```

`Completed`, `Cancelled` and `Aborted` are terminal. No transition leaves a terminal stage. `Suspended`, automatic retry, backward transition and stage skipping are absent; adding one requires a separately reviewed revision rather than a free-form value.

An empty history projects `Draft`. Any non-empty valid history begins at `Draft` and follows one unbranched predecessor chain. This stage vocabulary is local to Operation lifecycle and does not create shared State.

## 6. `OperationLifecycleTransitionRecord`

Each transition is a separately identified LT2 record:

```text
OperationLifecycleTransitionRecord
- record_kind_ref: operation-lifecycle-transition@1
- transition_id
- operation_ref
- predecessor_transition_ref [absent only on the first transition]
- from_stage
- to_stage
- occurred_at
- provenance_ref
- completeness_binding
- authorization_evidence_binding [required only for → Authorized]
- assignment_alignment [required only for terminal targets]
```

`transition_id` is stable and unique across the invoking dataset. `operation_ref` never changes within one history. `predecessor_transition_ref` exact-resolves to the unique immediately preceding transition; it is the chain authority, not a storage-order hint.

`record_kind_ref` is fixed because this contract owns one transition family. `provenance_ref` attributes why the transition was recorded, but it is not an authorization source and cannot compensate for missing completeness, authorization or terminal-alignment evidence.

## 7. Authoritative history and projections

`transition_history` is authoritative. A valid non-empty history has:

1. exactly one root without `predecessor_transition_ref`;
2. exact unique transition IDs;
3. exact predecessor resolution within the same Operation history;
4. no self-predecessor, cycle, branch, disconnected record or competing leaf;
5. `from_stage` of the root equal to `Draft`;
6. `from_stage` of each successor equal to its predecessor's `to_stage`;
7. every pair in the allowed set from §5; and
8. non-decreasing `occurred_at` along the predecessor chain.

The current stage is projected as:

```text
derive_operation_lifecycle_stage(envelope)
    := Draft, when transition_history is empty
    := to_stage of the unique predecessor-chain leaf, otherwise
```

The derivation does not sort records by timestamp or list order. Time only validates order along an already exact chain. A materialized `lifecycle_stage`, whether carried beside the history or in an Operation snapshot, must equal the derivation. A mismatch is invalid; the stored label never overrides history.

No current-head redirection is defined for transition records. The complete history is preserved, and exact historical transition references continue to name the same record.

## 8. G2 structural completeness and domain-profile hook

Every transition carries one `completeness_binding`:

```text
completeness_binding
- profile_ref
- profile_owner_ref
- input_snapshot_ref
- input_state: effective
- result: passed
- provenance_ref
```

The binding exact-resolves `profile_ref` to one declared profile with the same `profile_owner_ref`. Zero, multiple, unknown or owner-incomparable candidates fail closed. Only `input_state: effective` with `result: passed` satisfies the binding; missing, stale, ambiguous, conflicting or incomparable input blocks the transition. Profile ownership is attribution accepted by the consuming domain contract; the checker does not authenticate or elect that owner.

The universal structural minimum supplements, rather than replaces, the profile:

- every non-Draft stage satisfies OCP-004's single active-intent invariant;
- any path that entered `Planned` carries a valid `planned_start` in the Operation snapshot;
- any path that entered `Active` carries a valid `actual_start`;
- `Completed` or `Aborted` carries a valid `actual_end`; and
- the transition and every exact binding required for its target stage are structurally complete.

The initial executable slice requires one exact profile binding on every transition. A domain profile may add stricter fields, but cannot weaken the universal minimum, invent authority or reinterpret a failed/missing result as permissive.

## 9. A1 authorization-evidence acceptance

Only a transition whose target is `Authorized` carries `authorization_evidence_binding`:

```text
authorization_evidence_binding
- source_contract_ref
- source_owner_ref
- evidence_ref
- subject_operation_ref
- input_snapshot_ref
- input_state: effective
- result: accepted
- provenance_ref
```

`source_contract_ref` exact-resolves to one separately governed evidence source with the same `source_owner_ref`. `subject_operation_ref` equals the transition's exact Operation. Evidence, input and provenance refs are non-empty and immutable for that transition.

Missing, duplicate, ambiguous, owner-mismatched, subject-mismatched, conflicting or non-accepted input fails closed. Neither newest evidence, list order, source count, issuer count nor a bare stage label selects authority.

This is an acceptance envelope, not an authorization mechanism. OCP-017 can state that exact evidence met the named source contract; it cannot prove that the source owner is legitimate, issue an Order, grant permission or authorize a user. A concrete domain must govern those responsibilities separately.

Authorization evidence on another transition target is invalid in the bounded `0.1.0` contract. This prevents evidence intended for one decision point from becoming general permission by reuse.

## 10. T1 terminal Assignment alignment

Every transition to `Completed`, `Cancelled` or `Aborted` carries one inline `assignment_alignment` evaluated at that transition time:

```text
assignment_alignment
- evaluation_time
- input_snapshot_ref
- dispositions
  - assignment_ref
  - disposition: remains_effective_independently | not_effective_at_transition
  - evidence_ref
```

The alignment exact-enumerates every Assignment whose `operation_ref` names the Operation in the declared dataset. `evaluation_time` equals the terminal transition's `occurred_at`. Each Assignment appears once:

- if OCP-005 `assignment_effective_at` is true at that instant, the only valid disposition is `remains_effective_independently`;
- otherwise the only valid disposition is `not_effective_at_transition`.

Missing, duplicate, unresolved, conflicting or incorrectly classified disposition fails closed. An empty exact set is valid when no Assignment targets the Operation.

The envelope records alignment evidence only. It never edits an Assignment transition history, closes or revokes an Assignment, shortens applicability, or makes an ineffective Assignment effective. Any such lifecycle coordination requires a separate owner and Board act.

## 11. Validation rules

A Q3I lifecycle dataset is valid only when all of these rules hold:

1. every Operation exact-binds the current fixture contract `OCP-004@0.9.0`, while historical fixtures remain replayable under their prior contract;
2. Operation and lifecycle envelope sets have exact one-to-one membership;
3. transition IDs are globally unique and every transition conforms to §§5–7;
4. materialized stage equals the predecessor-chain projection;
5. the OCP-004 universal intent and temporal minimum is satisfied for the derived path;
6. every completeness profile resolves exactly once and returns `passed`;
7. only `→ Authorized` has one exact accepted authorization-evidence binding;
8. every terminal transition has a complete exact Assignment alignment;
9. no transition or envelope asserts authorization granted, Assignment mutation, Event generation, Objective achievement, Readiness, State, availability or interchangeability; and
10. missing, stale, conflicting, ambiguous or structurally invalid evidence is non-permissive.

These rules do not allow one successful binding to compensate for another failed binding.

## 12. Boundaries with dependent contracts

| Dependency | Exact semantic use | What OCP-017 does not own |
|---|---|---|
| AD-020 | Q3I selection, stops and rollback | merge authority or future lifecycle promotion |
| OCP-001 | governance, external review and version discipline | semantic route selection |
| OCP-004 | exact Operation identity, intent and temporal kernel | Operation identity or context |
| OCP-005 | `assignment_effective_at` and Assignment lifecycle truth | Assignment mutation or participation formula |
| OCP-006 | external Constraint applicability/evaluation boundary | copied predicate/effectivity or automatic transition truth |
| OCP-010 | independent Event occurrence and zero/one/many relevance | Event generation, causation or reverse edge |
| OCP-011 | external assessment identity and `Completed != achieved` | outcome conclusion or lifecycle projection |
| OCP-016 | Route C non-Concept classification and no hidden authority | admission or self-approval |
| P-001 | LT2 identified-record form and Module B | lifecycle domain meaning |

Constraint evaluation may appear as exact provenance/evidence owned by OCP-006, but OCP-017 does not reproduce its formula. Event may be exact provenance for a transition, but the transition does not create or prove that Event. OutcomeAssessmentRecord remains independent and cannot change a stage.

All nine direct dependencies are therefore semantically consumed. None is present merely because an earlier document listed it.

## 13. P-001 conformance — LT2

OCP-017 exact-invokes `P-001@0.1.0` for one `OperationLifecycleTransitionRecord` family.

| P-001 Required Element | OCP-017 mapping |
|---|---|
| stable record identity | globally unique non-empty `transition_id` |
| owning semantic specification | OCP-017 §§5–11 |
| endpoint contract | exact directed `operation_ref`; `from_stage → to_stage` applies only to that Operation |
| governed kind | fixed `record_kind_ref = operation-lifecycle-transition@1` plus closed stage/transition sets |
| provenance | non-empty `provenance_ref` and exact target-specific evidence bindings |
| validation | chain/path/time/projection, completeness, authorization and terminal-alignment rules with positive/negative executable evidence |
| authority | complete predecessor-linked `transition_history`; stage labels and timestamps alone never elect current state |

**Selected Optional Module:** B — Transition History and Projections.

Module B mapping is complete:

1. stages and paths are closed in §5;
2. transition history is authoritative in §7;
3. every record has identity, exact Operation reference, source/target stages, occurrence time and provenance;
4. timestamps are non-decreasing along the exact predecessor chain;
5. current stage is the deterministic unique-leaf projection;
6. materialized stage is optional;
7. when present it equals the derivation; and
8. branches, cycles, competing leaves and mutually exclusive paths reject.

Modules A and C are not selected. `occurred_at` orders transition history; it does not define a separate effectivity interval. No `supersedes_ref`, replacement winner or overlap rule exists. If real effectivity or supersession semantics appear, OCP-017 must stop for a separately reviewed P-001 conformance revision.

## 14. Executable evidence

The reference checker adds a bounded `OperationQ3IContractDataset` harness and an `operation-lifecycle-rules.yaml` manifest. The synthetic fixture demonstrates:

- two distinct Operation identities with one IO2 value;
- F1 and V1 fixed kinds, independent IDs, exact bindings and provenance;
- one complete `Draft → Planned → Authorized → Active → Completed` LT2 chain;
- storage-order-independent projection from predecessor links;
- exact completeness-profile and authorization-source resolution;
- one still-effective Assignment explicitly left independent at terminal transition; and
- unchanged replay of the prior OCP-004 `0.8.3` explicit-intent fixture.

Unit attacks cover invalid branching, time order, stage override, missing/ambiguous/failing profiles, invalid/ambiguous authorization evidence, wrong Assignment disposition, hidden IO2 record identity, unresolved/duplicate relations, composition cycle, missing F1/V1 provenance, duplicate record IDs and forbidden outcome/Readiness coupling.

The manifest is an exact projection of emitted rule and derivation IDs. It cites this document and OCP-004 but creates no authority. Passing evidence is necessary for the executable subset, never proof of legitimate owners, complete domain policy, semantic sufficiency, Draft acceptance or production readiness.

## 15. Historical replay, migration and rollback

OCP-004 `0.8.3` snapshots remain historical evidence under their exact prior contract. Migration to Q3I may preserve known Operation identity, temporal context and already supported intent evidence, but it cannot manufacture:

- transition identity or predecessor links;
- occurrence or provenance facts;
- a passing completeness result;
- authorization evidence or a legitimate source owner;
- Assignment alignment evidence; or
- Event, outcome or IO2 meaning.

If one required fact is absent, the snapshot stays historical or migration stops. No newest version, timestamp, list order, source count, issuer count or label similarity may fill the gap.

OCP-004 `0.9.0` and OCP-017 `0.1.0` are one atomic ownership change. Partial merge or rollback is invalid. Corrective rollback restores the prior OCP-004 document and checker interpretation, removes OCP-017 and its manifest/tests/fixture, and restores repository accounting together. It does not rewrite historical data, P-001, its existing invokers, immutable snapshots, Concept statuses or graph edges.

## 16. Version and lifecycle boundary

`0.1.0 / Draft` is appropriate because this is the first governed Route C Operation lifecycle contract. It is readable and executable but has not passed a separate acceptance/canonicalization audit and does not promote Operation.

A compatible later `0.x` MINOR may add evidence or a separately authorized transition/profile rule while preserving every current exact reference and non-implication. Any change to Operation identity, the OCP-004/OCP-017 ownership direction, P-001 form/modules, authorization ownership, Assignment mutation, Event/assessment authority, a Concept edge or historical replay requires a new discovery/Board route before implementation.

OCP-017 is not a Concept and therefore adds no OCP-000 Concept row, OCP-002 status projection or Concept graph node.

## 17. Remediation act and status accounting

This Draft is created only in the atomic Q3I remediation tree with OCP-004 `0.9.0 / Draft`. The act:

- implements the Q3I ownership split without selecting Operation lifecycle promotion;
- adds OCP-004 and OCP-017 as primary exact invokers of unchanged `P-001@0.1.0`;
- leaves P-001 byte-identical under its time-anchored evidence-accounting rule;
- leaves every prior P-001 invoker and immutable reviewed snapshot byte-identical;
- changes no Concept, Concept status or graph edge;
- leaves AB-015, AB-016, AB-017, AB-019, AB-020, AB-023, AB-028 and AB-062 in their prior states; and
- leaves foundation readiness at approximately 71% pending fresh post-remediation audit.

Merge requires exact-head Fable review, Codex adjudication, green CI and a fresh explicit Pavlo/Architecture Board authorization for this unchanged atomic tree. The preparation mandate does not satisfy that gate.
