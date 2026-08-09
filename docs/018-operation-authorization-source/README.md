---
Document-ID: OCP-018
Title: Operation Authorization Source Contract
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: AD-012, AD-021, OCP-001, OCP-004, OCP-006, OCP-007, OCP-009, OCP-016, OCP-017, P-001
Uses-Patterns: P-001@0.1.0
Used-By: OCP-017 authorization-evidence acceptance, Operation authorization review, Audit
Last-Review: 2026-08-09
Review-After: First production-facing authorization-source proposal or evidence that source ownership, authorizer eligibility, decision-level resolution, effectivity, supersession or OCP-017 binding is incomplete
---

# OCP-018 — Operation Authorization Source Contract

## 1. Route, authority and Draft status

OCP-018 is a **Route C Core non-Concept contract** under OCP-016. It defines the shared minimum by which a separately governed source can produce one attributable, replayable decision about one exact OCP-004 Operation and by which OCP-017 can accept that decision as authorization evidence.

This `0.1.0` artifact is `Draft`. It creates neither a Concept nor a general power to authorize. A concrete source profile remains owned by its exact `source_owner_ref`; OCP-018 validates the finite envelope and derivation but does not authenticate the owner, invent a command chain or decide which real organization is legitimate.

AD-021 compares the outcome space and proposes this route in the same atomic act. The proposal becomes the Board selection only if the exact reviewed tree is separately authorized and merged. Draft preparation, external review and green CI do not authorize use in production.

## 2. Purpose in plain language

OCP-017 already knows how to ask whether exact authorization evidence was accepted before an Operation enters `Authorized`. It deliberately does not say who made the decision, at which governed level, under which Capability, or whether the evidence is still usable.

OCP-018 fills only that source-side gap. It makes four questions explicit and replayable:

1. which exact Organization made the decision and which exact Capability version the source profile requires;
2. which contract-local decision level was resolved when the source profile defines more than one;
3. which independently identified decision record is the evidence; and
4. whether that decision is the unique effective head at the requested evaluation time.

The contract does not claim that an Organization *has* a Capability in the OCP-012 holder sense. OCP-012 permits only Resource holders. Here the exact Capability definition scopes the source-owned eligibility evidence; it is not a holder claim, certification, availability statement or universal Organization-Capability edge.

## 3. Explicit boundary and non-implications

OCP-018 does not define or grant:

- fundamental Concepts `Authority`, `Approval`, `Policy`, `Authorization`, `DecisionLevel` or `Order`;
- a Concept registry row, `Concept-Status`, taxonomy entry or Concept graph edge;
- actor authentication, credentials, access control, command authority or a universal organization hierarchy;
- Organization possession of Capability or an OCP-012 Organization holder;
- Order as mandatory or sufficient authorization evidence;
- lifecycle state, an OCP-017 transition, Assignment mutation, Constraint truth, selection, Readiness or execution;
- a global evidence lifetime or a cross-consumer freshness default;
- source-owner legitimacy from timestamp, list position, issuer count, source count or caller identity; or
- a production schema, wire encoding, database table or API.

OCP-014 need evidence does not become permission. OCP-015 confirmation does not become authorization, selection or Assignment mutation. AD-010 visibility/agreement and AD-011 State/Readiness no-new-authority outcomes remain unchanged.

## 4. Terms and dependency boundary

**Source profile** — a versioned, separately governed description of one source contract, its exact Organization owner, its level-resolution rule, its freshness rule and the finite decision levels with their exact Capability requirements.

**Authorization decision** — an attributable `authorize` or `deny` statement about one exact Operation under one exact source profile, input snapshot, authorizer Organization, Capability and decision level.

**Eligibility binding** — source-profile evidence that the named Organization was eligible under the named Capability requirement for the exact input snapshot. It is authoritative only inside the named source contract. It is not an OCP-012 CapabilityClaimRecord and does not assert general possession.

**Level binding** — source-profile evidence that one exact decision level was resolved by one exact rule and input snapshot. It does not derive level from Organization relationship labels or structural superiority.

**Effective head** — the unique non-superseded decision in one exact source/owner/Operation lineage whose half-open interval contains the evaluation time.

OCP-018 depends downstream on OCP-017 because it produces evidence for OCP-017's existing acceptance envelope. OCP-017 remains unchanged and does not depend back on OCP-018; the dependency direction is acyclic. Other source contracts may remain possible, and OCP-017 does not silently prefer this Draft.

## 5. Dataset and resolution envelope

The executable reference evaluates one declared dataset containing:

```text
OperationAuthorizationSourceDataset
- operations
- organizations
- capabilities
- source_profiles
- decisions
- evaluation_time
- authorization_evidence_binding
```

Every reference resolves exactly once inside the declared dataset or an exact resolver accepted by the consumer. Zero, duplicate, unknown or version-ambiguous resolution is non-permissive. Whitespace normalization may remove surrounding serialization whitespace; it does not select newest versions or equivalent labels.

The checker validates OCP-007 Organization structure and OCP-009 Capability registry structure in the executable slice. OCP-004 Operation validity and OCP-017 transition history remain owned by their existing validators; this module exact-resolves only the subject Operation identity required by the source decision.

## 6. `OperationAuthorizationSourceProfile`

The source profile has this bounded form:

```text
OperationAuthorizationSourceProfile
- profile_kind_ref: operation-authorization-source-profile@1
- source_contract_ref
- source_owner_ref
- level_rule_ref
- freshness_rule_ref: operation-authorization-effective@1
- decision_levels
  - decision_level_ref
  - required_capability_ref
    - namespace
    - capability_id
    - version
```

`source_contract_ref`, `level_rule_ref` and every `decision_level_ref` are exact versioned references. `source_owner_ref` exact-resolves one valid OCP-007 Organization. Every `required_capability_ref` exact-resolves one OCP-009 Capability version; matching label or namespace alone is insufficient.

Decision-level references are source-contract-local governed values, not fundamental subjects and not a universal rank. The profile may contain one or several levels. Each level appears once. The level rule, not list order, Organization relationship shape or a “highest” label, resolves the required level.

The source profile is a defining profile rather than a second P-001 record family: its identity is the exact versioned contract reference, it has no instance lifecycle or supersession history in OCP-018, and a changed profile publishes a new exact version. A future need for independently addressed profile records or cross-profile equivalence requires a separate route review.

## 7. `OperationAuthorizationDecisionRecord`

```text
OperationAuthorizationDecisionRecord
- record_kind: operation-authorization-decision@1
- decision_id
- source_contract_ref
- source_owner_ref
- subject_operation_ref
- authorizer_organization_ref
- authorizer_capability_ref
  - namespace
  - capability_id
  - version
- decision_level_ref
- input_snapshot_ref
- level_binding
- eligibility_binding
- decision: authorize | deny
- effective_from
- effective_until
- recorded_at
- provenance_ref
- supersedes_decision_ref [optional]
```

`decision_id` is stable, non-empty and unique in the invoking dataset. Same source, owner, Operation, authorizer, decision, times or payload never collapse two identities. `subject_operation_ref` exact-resolves one Operation. `source_contract_ref` resolves one profile and `source_owner_ref` equals that profile's exact owner.

`decision` records the source's attributable result. `authorize` can derive `accepted` only after every rule below passes. `deny` derives `denied` and can never satisfy an OCP-017 binding whose stored result is `accepted`. The record does not itself move the Operation lifecycle.

## 8. Authorizer, Capability and decision-level bindings

The exact level binding is:

```text
level_binding
- rule_ref
- input_snapshot_ref
- result_level_ref
- result: resolved
- evidence_ref
- provenance_ref
```

`rule_ref` equals the source profile's exact level rule. `input_snapshot_ref` equals the decision input. `result_level_ref` equals the decision's level and resolves one profile level. The decision's exact Capability equals that level's required Capability. Missing, unknown, mismatched, multiple or non-resolved level evidence is `indeterminate` for authorization use.

The exact eligibility binding is:

```text
eligibility_binding
- authorizer_organization_ref
- capability_ref
- input_snapshot_ref
- result: eligible | ineligible | indeterminate
- evidence_ref
- provenance_ref
```

Organization, Capability and input snapshot equal the decision fields. Only `eligible` permits further derivation. `ineligible`, `indeterminate`, missing evidence or ambiguity yields `indeterminate` authorization use. The binding is an attributable source-contract result; OCP-018 does not convert it into Capability possession, certification or general authority.

The same Organization may appear in multiple source profiles without equivalence or precedence. Multiple Organizations or levels are not votes. The exact source profile and level rule must resolve one decision context.

## 9. Effectivity, freshness and supersession

OCP-018 selects P-001 Module A. Every decision carries a valid half-open interval:

```text
operation_authorization_effective_at(decision, t) :=
    effective_from <= t < effective_until
```

Both bounds are required in `0.1.0`. Missing, invalid, reversed or expired bounds are non-permissive. The fixed contract-local `operation-authorization-effective@1` rule is an AD-012 F1/A1 activation for this consumer only; it creates no global lifetime and does not change any other consumer.

OCP-018 also selects P-001 Module C. `supersedes_decision_ref`, when present, exact-resolves one prior decision with the same source contract, source owner and subject Operation. Self-supersession, unresolved predecessors, cycles or branching are invalid. A successor does not rewrite the prior record.

At an evaluation time, the source/owner/Operation lineage must have exactly one effective head. Zero heads, competing heads, invalid lineage or a binding to a superseded head yields `indeterminate`. Newest timestamp, list order and record count never choose a winner.

The word `indeterminate` preserves the accepted fail-safe shape used elsewhere but does not invoke or redefine OCP-006 Constraint evaluation or its `indeterminate_disposition`.

## 10. OCP-017 evidence-acceptance binding

The existing OCP-017 binding remains:

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

For OCP-018 evidence, `evidence_ref` exact-resolves one `decision_id`. Source contract, owner, subject Operation and input snapshot equal the decision fields. All fields are non-empty; `input_state` is exactly `effective`; stored `result` is exactly `accepted`; and the OCP-018 derivation independently returns `accepted`.

A structurally valid `deny` decision remains auditable but cannot satisfy this binding. A stale, ineligible, wrong-level, conflicting, unknown or forbidden-coupling decision also cannot satisfy it. Stored `accepted` never overrides derived `denied` or `indeterminate`.

## 11. Authoritative derivation and invariants

```text
derive_operation_authorization_result(dataset) :=
    accepted
        if evidence_ref resolves exactly one decision
        AND source profile, owner, Operation, Organization and Capability resolve exactly once
        AND source owner, subject and input snapshot match the OCP-017 binding
        AND level binding resolves the decision's exact level and Capability
        AND eligibility result = eligible
        AND decision is the unique effective lineage head
        AND decision = authorize
    denied
        if every condition above holds AND decision = deny
    indeterminate
        otherwise
```

Normative invariants:

1. Every decision has one unique `decision_id` and exact fixed kind.
2. Source profile and owner resolve exactly once and match the decision.
3. Subject Operation, authorizer Organization and Capability version resolve exactly once.
4. The level rule, level result, Capability and input snapshot agree exactly.
5. Eligibility is exact-snapshot attributable evidence and only `eligible` is permissive.
6. Effectivity uses the explicit half-open interval; wall-clock “current” is never substituted.
7. Supersession preserves source/owner/Operation identity and has one linear head.
8. A unique effective `authorize` head derives `accepted`; a unique effective `deny` head derives `denied`.
9. Missing, stale, ambiguous, conflicting or structurally invalid input derives `indeterminate`.
10. OCP-017 stored acceptance equals the derivation and cannot make it more permissive.
11. Timestamp, record order, source count, issuer count and caller identity carry no precedence.
12. Every reference used by a positive result is exact-versioned where its owner supports versions.

## 12. Forbidden coupling and stop rules

The executable envelope rejects materialized fields that would smuggle unresolved authority or side effects:

```text
authority_concept_ref
approval_concept_ref
policy_concept_ref
order_required
authorization_granted
lifecycle_stage
assignment_mutation
readiness
```

`Order` may later be one source profile or evidence kind if AB-002 separately defines it. OCP-018 neither requires nor excludes that future result. Any proposal that makes Order mandatory, introduces one of the prohibited Concepts, infers level from Organization superiority, or mutates lifecycle/Assignment must stop for its own Board act.

Unknown extra implementation fields are outside this reference slice unless they collide with a forbidden coupling. Production schemas may be stricter but may not weaken the normative derivation.

## 13. P-001 conformance

OCP-018 exact-invokes `P-001@0.1.0` for `OperationAuthorizationDecisionRecord`:

| P-001 Required Element | OCP-018 mapping |
|---|---|
| stable record identity | globally unique non-empty `decision_id` |
| owning semantic specification | OCP-018 §§6–12 |
| endpoint contract | exact directed `subject_operation_ref`; the decision concerns only that Operation |
| governed kind | fixed `operation-authorization-decision@1` |
| provenance | source/owner, authorizer, exact evidence bindings, `recorded_at`, `provenance_ref` |
| validation | exact resolution, level/eligibility, effectivity, lineage and OCP-017 equality rules |
| authority | unique effective lineage head plus the deterministic derivation; no convenience field overrides it |

Selected Optional Modules are A and C. Module A is completely mapped in §9. Module C is completely mapped in §9. Module B is not selected because `authorize`/`deny` are attributable decision values, not a universal administrative lifecycle. Module D is not selected; independent stored/derived checks already arise from the existing OCP-017 binding contract and are tested without declaring a reusable defense doctrine.

Adding this exact invoker does not edit P-001's time-anchored T3 ledger. Current invoker authority remains structured `Uses-Patterns` metadata under the accepted `track-current` policy.

## 14. Executable evidence and synthetic-only safety

`tools/ontology_checker/operation-authorization-rules.yaml` is the complete source-bound rule manifest. `operation_authorization.py` implements the finite reference derivation. Fixtures include:

- one accepted exact authorize decision with a prior superseded denial;
- expired decision evidence that cannot remain accepted;
- an ineligible authorizer result that fails safe;
- an unresolved Capability version that cannot satisfy a profile level;
- malformed Organization/Capability registry entries and a malformed historical lineage member;
- an explicit denial that cannot masquerade as acceptance;
- a wrong decision level;
- branching conflicting successor heads; and
- forbidden mandatory-Order/concept coupling.

Focused unit tests replay every fixture, require exact error sets, check decision-order independence and assert manifest completeness. The general fixture harness executes every file in both PR and main contexts.

All examples and fixtures are invented for this repository. They contain only synthetic identifiers, synthetic future timestamps and abstract capability/profile values. They contain no real operations, coordinates, frequencies, unit designators, personnel, credentials, operational windows or material copied from another project.

## 15. Version, migration and rollback

`0.1.0 / Draft` is the first compatible contract surface. It adds one Route C non-Concept artifact and one exact P-001 invoker without changing any existing OCP or Pattern version. It cannot be PATCH because no earlier OCP-018 exists; it cannot be Accepted because a production-facing source, migration and external evidence remain unproven.

No migration is implied. Existing OCP-017 evidence bound to another separately governed source remains historical under that source contract. A future adopter may bind only exact OCP-018 records that already satisfy the full source profile and derivation; it may not invent missing owners, Capability bindings, decision levels, input snapshots, effectivity or provenance.

Rollback removes the Draft contract, its module, manifest, tests and fixtures atomically and restores AB-017 to `Open`. It does not rewrite OCP-004/OCP-017 history or change a lifecycle stage. Once external artifacts bind OCP-018, rollback instead requires a separately reviewed version/retirement act preserving exact historical references.

## 16. External review questions

1. Does Route C own only shared source/decision guarantees while leaving legitimacy and domain meaning to exact profiles?
2. Does the Organization + Capability binding avoid an OCP-012 Organization-holder claim?
3. Can multiple decision levels be expressed without a universal hierarchy or list-order precedence?
4. Is the independently identified decision record justified by audit, effectivity, supersession and OCP-017 evidence use?
5. Do stale, denied, ineligible, wrong-level and conflicting records always fail non-permissively?
6. Can any stored field, timestamp, source count, issuer count or caller identity override the derivation?
7. Does any field make Order mandatory or introduce Authority, Approval or Policy as a Concept?
8. Do the checker rules and synthetic fixtures cover every mechanically expressible material invariant?
