---
Document-ID: OCP-018
Title: Operation Authorization Source Contract
Version: 0.2.1
Status: Accepted
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
- malformed fixture shape, invalid source-profile shape and an unresolved profile reference;
- duplicate decision IDs and an invalid eligibility-binding result;
- expired decision evidence that cannot remain accepted;
- an ineligible authorizer result that fails safe;
- an unresolved Capability version that cannot satisfy a profile level;
- malformed Organization/Capability registry entries and a malformed historical lineage member;
- an explicit denial that cannot masquerade as acceptance;
- a wrong decision level;
- branching conflicting successor heads; and
- forbidden mandatory-Order/concept coupling.

Every declared validation rule ID has direct fixture evidence. Focused unit tests replay every fixture, require exact error sets, check decision-order independence and assert manifest completeness. The general fixture harness executes every file in both PR and main contexts.

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

## 17. Authority and incorporated contract body

Architecture Board accepts OCP-018 revision `0.2.0` as the governed Route C non-Concept contract selected by AD-021 Outcome AC and the bounded resolution of AB-017.

The complete externally reviewed Draft is preserved byte-for-byte in [`reviewed-contract-v0.1.0.md`](reviewed-contract-v0.1.0.md). Sections 1–14 and the migration/replay constraints of §15 are incorporated into this Accepted specification without semantic alteration. The snapshot frontmatter, Draft lifecycle claims, pre-acceptance rollback wording and §16 review questions remain historical review evidence only; this README is the sole current lifecycle and acceptance authority.

The original numbered §§1–16 remain in this primary README. Every existing `OCP-018 §N` rule-manifest source therefore continues to resolve directly to the same numbered semantic owner; the acceptance bridge begins at §17 and creates no competing owner. No `source:` row changes.

Acceptance means that the Board accepts the current semantics as a basis for dependent specifications under OCP-001. It does not make OCP-018 Canonical, promise `1.x` stability, authenticate a source owner, legitimize a production source profile or grant permission to perform an Operation.

## 18. Repository-derived acceptance contract

On the exact acceptance base, the method enumerated every primary `docs/*/README.md` and selected `Status: Accepted`, independently of `Concept-Status`. The complete base comparison set was OCP-011, OCP-012, OCP-013, OCP-014, OCP-015 and OCP-017; Draft OCP-005, OCP-006 and OCP-010 were excluded even though their Concepts are Accepted.

All six Accepted OCPs, without exception, preserve the externally reviewed Draft in a sibling `reviewed-contract-v0.1.x.md` and make the primary README the sole current authority. Each first Draft acceptance used `0.2.0 / Accepted`, recorded the accepted baseline or compatibility promise, external review evidence, Board act and authority/non-transfer boundary, and kept exact-head review, Codex adjudication, green CI and owner authorization as separate gates. Migration and rollback treatment is contract-specific rather than universal; OCP-018 requires both because its Draft already owns identified decision history, exact evidence bindings and an explicit migration/rollback boundary. A standalone `architecture/reviews/*` memo is not invariant and is not required here.

OCP-001 defines Accepted as a Board-approved semantic basis for dependents, distinct from Canonical and from a `1.x` stability guarantee. The current byte-identical snapshot, the PR #138 adversarial review record and the bounded evidence below satisfy that lifecycle contract without requiring production adoption evidence.

Draft §15 bundled three distinct stops. They are adjudicated separately for acceptance:

1. **Production-facing source evidence remains unproven.** OCP-001 does not make production adoption a prerequisite for Accepted; the unchanged `Review-After` field and §§4, 12 and 28 keep the first production profile separately gated. No source legitimacy or usability in a real environment is claimed.
2. **Migration evidence is complete as a no-migration result.** The semantic body, rules, checker, tests and fixtures are unchanged; the exact Draft is preserved; no non-synthetic, externally bound or production record, source profile, consumer reference or representation exists to rewrite. The synthetic fixtures remain evidence and require no migration because their bytes and semantics are unchanged. Only document lifecycle and current repository projections move.
3. **External evidence is split correctly.** PR #138 adversarially reviewed the full semantic body and executable behavior. This acceptance candidate adds the repository-derived lifecycle proof and must itself pass fresh exact-head external review, Codex adjudication, green CI and owner authorization before merge.

## 19. Accepted compatibility surface

The incorporated contract retains one finite shared source envelope:

- one exact versioned `OperationAuthorizationSourceProfile`, source contract and source owner;
- one exact OCP-004 Operation, authorizer Organization, OCP-009 Capability version, contract-local decision level and input snapshot;
- one independently identified `OperationAuthorizationDecisionRecord` under `P-001@0.1.0` Modules A and C;
- exact effectivity and history-preserving, acyclic, unique-head supersession;
- exact OCP-017 authorization-evidence binding equality; and
- deterministic `accepted | denied | indeterminate` derivation in which stored state, newest timestamp, list order, source count, issuer count or caller identity has no authority.

Missing, malformed, unresolved, stale, ineligible, wrong-level, conflicting or forbidden input cannot derive `accepted`. An explicit effective denial derives only `denied`; it never masquerades as acceptance.

The source profile remains a defining versioned profile, not a second P-001 record family. A changed profile publishes a new exact version. Independently addressed profile records, cross-profile equivalence or a production source registry require a separate route and reviewed act.

## 20. Preserved authority boundary

The exact source owner owns its concrete profile and the exact authorizer owns only its attributable decision. OCP-018 validates the finite envelope and derivation; it does not authenticate either Organization, infer legitimacy, invent a command chain or decide which real organization may authorize.

The Organization + Capability binding does not make Organization an OCP-012 CapabilityClaimRecord holder and does not resolve AB-006 or AB-052. Decision levels are contract-local references; list order, labels, Organization relations or an asserted superior/subordinate relation cannot create a universal hierarchy.

OCP-018 does not create or imply an `Authority`, `Approval`, `Policy`, `Authorization`, `DecisionLevel` or `Order` Concept. It does not make Order mandatory, resolve AB-002, evaluate a Constraint, select a Resource, authenticate a caller, move an Operation lifecycle stage, mutate an Assignment or authorize production use.

OCP-000, OCP-002, every `Concept-Status`, the Concept graph, foundation map, OCP-004, OCP-007, OCP-017 and P-001 remain unchanged by this acceptance act.

## 21. Executable conformance and safety

The accepted `operation-authorization-rules.yaml`, checker module and sixteen OCP-018 fixtures remain byte-unchanged. Their direct negative evidence covers all twelve validation rule IDs and material fixture-shape, profile, source, duplicate, eligibility, Organization, Capability, lineage, effectivity, denial, level, conflict and forbidden-coupling failures. Focused tests preserve exact error sets, order independence and manifest equality.

The repository lower bound remains `201/201` unit tests and `141/141` fixtures in both PR and main audit contexts. The checker remains a finite reference validator, not a production schema, permission service, authenticator, policy engine or independent normative owner. Green evidence cannot select lifecycle status.

Every example and fixture is synthetic. This act adds no operational example or fixture and contains no real operation, coordinate, frequency, unit designator, person, credential, key, token or operational window. No material was copied from another project or repository.

The separately recorded observation that manifest-to-fixture coverage is achieved but not mechanically enforced remains open as a possible hygiene act. Acceptance does not close it or authorize that act.

## 22. External review evidence

Fable externally reviewed the complete Draft on exact head `ecc8b782eca1ef940618512fcc1f3a28bbe42e62` against exact base `cdf5e1af329a363132aeca28257cf187a077d0f6`. Iteration 2 of 5 approved the contract for Architecture Board outcome comparison with zero open Blocking, Major, Moderate or Minor findings after direct fixture evidence closed the only iteration-1 Minor.

That review independently reproduced `201/201` tests, `141/141` fixtures in both contexts, direct `12/12` validation-rule fixture coverage, full anchor chains, structural sweeps and synthetic-only safety. Pavlo separately authorized the unchanged head, and PR #138 squash-merged as `308a8f4db64cd4408b4002ca79b5303cb033c070` with `reference-checker` green.

Those gates accepted AD-021's AC selection and prepared this Draft; they do not authorize this lifecycle transition. This `0.2.0 / Accepted` candidate requires its own fresh four gates on one unchanged exact head.

## 23. Exact acceptance baseline and anchor method

The acceptance baseline is exact `main@308a8f4db64cd4408b4002ca79b5303cb033c070`. For every row, the Git object was resolved first, reverse-matched through `git ls-tree -r` to exactly one path, checked against the declared state inside the object and independently hashed from raw blob bytes.

| Artifact | Declared state on the exact base | Git blob | SHA-256 |
|---|---|---|---|
| OCP-018 Draft | `0.1.0 / Draft` | `f7e8528e252a01a1b45d1ac07cc211705f229d0f` | `7b60d478ac15ced656eaee2d6a7062ca1c0291e6dadc6dccae85787f700df077` |
| AD-021 | `0.1.0 / Accepted`; AC selected | `93275d1a8d831c93157701953a05edcae0067388` | `112507362fbaea77894e9d2c0ca8d7dc53a8e74bb13c06d9e8a07a3a939383cb` |
| OCP-001 | `1.0.0 / Canonical` | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-016 | `1.0.0 / Canonical` | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-017 | `0.2.0 / Accepted` | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| P-001 | `0.1.0 / Accepted` | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| AD-016 | `0.27.0 / Accepted` | `07243dd51eda18a789e1256056fc9234b594a327` | `c0975fa9a57ef706e04355950218367f2de8bcf919e25673fb2d482fed5aff04` |

The new snapshot has the same SHA-256 as the anchored OCP-018 Draft. Hash agreement proves byte identity and evidence provenance; it does not supply semantic or merge authority.

## 24. P-001 structured-metadata recount

The recount reads only primary frontmatter `Uses-Patterns: P-001@0.1.0`; prose, table-row count, newest file and consumer count cannot add an invoker. On the exact base the nine primary invokers are OCP-004, OCP-007, OCP-008, OCP-010, OCP-011, OCP-012, OCP-015, OCP-017 and OCP-018. The four immutable snapshot carriers are OCP-011, OCP-012, OCP-015 and OCP-017.

Acceptance changes the same primary README's status/version but not its exact Pattern binding, so primary invokers remain **9**. The new byte-identical OCP-018 snapshot carries the same structured binding, so immutable carriers change **4 → 5**. Binding-bearing files change **13 → 14**; including P-001 itself, the mechanical surface changes **14 → 15**.

All candidate-tree bindings remain exact `P-001@0.1.0`. The `track-current` policy continues to resolve the current Pattern version and distinguish primary artifacts from immutable reviewed snapshots. P-001's blob, version, Required Elements, modules, T3 ledger and §17.3 accounting rule remain byte-identical.

## 25. Bounded lifecycle-carrier counter subsets and debt registration

Two bounded detectors inspect two named syntactic subsets of the mandated carrier-count class without treating every number as a repository count. The Accepted-contract detector searches tracked Markdown for a standalone English/Ukrainian word-number or digit, followed in prose or across a Markdown table-cell separator by `Accepted` and optional `non-Concept`/`OCP` before `contract(s)`. The P-001-carrier detector searches for a standalone English/Ukrainian cardinal, ordinal or digit directly governing `primary invoker(s)`, `primary contract(s)`, `reviewed[-contract] snapshot(s)`, `snapshot carrier(s)` or `binding-bearing file(s)`; a second clause admits `N files` only when the same clause names the mechanical P-001 or `track-current` surface/footprint. Negative lookarounds exclude identifier, version and path fragments. These forms cover prose and Markdown table cells, word-numbers, ordinals and digits inside those two subsets; they make no completeness claim over arbitrary natural-language carrier counts.

Before either repository-wide scan, the relevant detector had to reproduce a known positive on the exact base: AD-016 §1 for the Accepted-contract form and AD-016 §243 for `eight current primary invokers` plus `three reviewed-contract snapshots`. Any failed known-positive match or non-zero search exit stopped the audit rather than being treated as an empty result. The complete exact-base Accepted-contract scan returned two prose/word-number hits and zero prose/digit, table/word-number or table/digit hits.

Each Accepted-contract hit is adjudicated separately:

1. AD-016 §1 says the foundation “now” has six Accepted non-Concept OCP contracts. It is a recurring current-state statement. The same sentence's eight Accepted Concepts and Accepted Core Boundary wording are already false on the base: the current distribution is five Canonical and three Accepted Concepts, and OCP-016 is Canonical. AD-016 `0.27.1` repairs the class by time-anchoring the sentence to the original `0.1.0` trigger instead of replacing one live counter with another.
2. AD-016 §38 records five Accepted non-Concept contracts on exact `main@645b22b27be8ff004bd98e4b918403335f300278`. It is historical baseline evidence and remains byte-identical. No debt is created.

The exact-base P-001-carrier scan returned **36 direct counter tokens across 23 matching lines**. The mechanical-file clause added no new carrier line beyond the two lines already matched directly. Every matching line is adjudicated here; multiple counters on one line share the stated disposition:

| Location | Detected carrier-count form(s) | Adjudication |
|---|---|---|
| root README T3 milestone | six primary contracts | completed T3 act effect; historical and unchanged |
| AD-016 §38 | six current primary invokers | exact `main@645b22b...` baseline; historical and unchanged |
| AD-016 §243 | eight current primary invokers; three reviewed-contract snapshots | recurring current-state wording, false on the acceptance base and additionally stale for the new snapshot; repaired in `0.27.1` by binding the complete paragraph to exact AD-016W baseline `main@e9ce8beb...` and using past tense |
| AD-016 §252 | ninth primary invoker; fourth immutable reviewed-snapshot carrier | exact AD-016X candidate-effect record for OCP-017; historical and unchanged |
| AD-016 §254 | eight primary invokers | numbered replay of the AD-016W target; historical and unchanged |
| AD-016 §257 | eight primary invokers; fourth immutable reviewed-snapshot binding | mandatory contract for the later WJ proposal; historical and unchanged |
| AD-016 §266 | eight primary invokers; four immutable reviewed snapshots; thirteen-file surface | exact §263-baseline audit result; historical and unchanged |
| AD-016 §276 | eight primary invokers; four immutable reviewed snapshots | exact §273-baseline frontier audit; historical and unchanged |
| AD-016 §279 | eight primary and four snapshot carriers | replay result for §272 target 6; historical and unchanged |
| AD-020 §28 | six current primary invokers | discovery accounting on its reviewed baseline; historical and unchanged |
| AD-020 §30 | quoted six-current-invoker ledger | explicit implementation-risk quotation, not current authority; historical and unchanged |
| AD-020 §33 target 25 | six current invokers; three immutable snapshots | Board-selection target on the selected baseline; historical and unchanged |
| AD-020 §37 | quoted six-current-invoker ledger | explicit future-remediation stop; historical and unchanged |
| OCP-004 §25 | nine binding-bearing files; six primary contracts; three snapshots; seventh/eighth invokers | completed Q3I remediation delta; historical act evidence and unchanged |
| OCP-004 §30 | eight primary invokers | exact WJ baseline anchor; historical and unchanged |
| OCP-004 §31 | eight primary invokers; three prior snapshots; fourth carrier; ninth-invoker negation | completed atomic T5 act effect; historical and unchanged |
| OCP-017 §21 | fourth carrier; ninth-invoker negation; eight invokers; three earlier snapshots | completed OCP-017 acceptance evidence; historical and unchanged |
| P-001 §16 | six primary invokers; three reviewed snapshots | named T3 acceptance act; historical and unchanged |
| P-001 §17 exact-tree sentence | six primary invokers | explicitly bound to the correction act's exact tree; historical and unchanged |
| P-001 §17 footprint sentence | three snapshots; nine files; six primary artifacts | explicitly bound to that exact tree; historical and unchanged |
| P-001 §17 mismatch counterfactual | six invokers; three snapshots | counterfactual replay of a Pattern-only version change; historical and unchanged |
| P-001 §17 preservation list | six invoker files; three snapshots | rollback preservation of the correction baseline; historical and unchanged |
| checker guide Pattern policy | two primary invokers | bounded pair OCP-004/OCP-017 added by the named remediation, not a total repository count; correct and unchanged |

Candidate structured metadata independently derives the current values recorded in §24: nine primary invokers, five immutable snapshot carriers, fourteen binding-bearing files and fifteen files including P-001. No prose counter supplies those values. The repaired AD-016 §243 retains its original eight/three facts as historical evidence rather than replacing them with another live total.

Known prose outside both syntactic subsets was registered, not silently treated as a negative scan: AD-016 §23 said `six current invokers`; §218 said both `Exactly six primary OCP artifacts invoke` and `all six invokers`; §234 said `all six current invokers remain`. All four statements—§23, both statements in §218 and §234—were unanchored current-facing statements and false against the nine-invoker acceptance base. AD-022 time-anchors each statement to its own historical baseline without replacing six by nine. The registered carrier-counter debt is closed; no broader natural-language completeness claim is made.

The detector and this adjudication grant no repair authority over `Review-After`, bare-integer section references or `source:` rows. No existing `Review-After` value or trigger is edited. The mandatory byte-identical snapshot does physically repeat the Draft's historical field, so exact-frontmatter carriers change **31 → 32** and repository-wide field-shaped carriers change **32 → 33**; this is registered as immutable historical evidence, not a new trigger or repaired counter. Prior inventories remain historical records. Bare-integer references and `source:` rows remain byte-unchanged.

## 26. Architecture Board decision

On 2026-08-09, Architecture Board:

1. accepts OCP-018 revision `0.2.0` as the governed AC authorization-source contract and retains it as a Route C non-Concept;
2. incorporates the reviewed source-profile, decision-record, authorizer, Capability, level, effectivity, supersession and OCP-017 binding semantics without alteration;
3. preserves the complete fail-safe derivation, P-001 Modules A/C mapping and synthetic executable evidence;
4. preserves all exclusions of source legitimacy, authentication, permission, Order requirement, lifecycle/Assignment mutation and production adoption;
5. keeps AB-017 Resolved while leaving AB-002 Open;
6. changes no Concept or Concept status and introduces no Authority, Approval or Policy Concept;
7. accepts the AD-016 `0.27.1` time-anchoring repairs for §1 and §243 current-facing prose, preserves every historical count adjudicated inside the two named syntactic subsets and registers the out-of-form carrier-counter debt without repairing it; and
8. transfers no authority to another act.

This decision becomes effective only after Fable review of the exact unchanged acceptance head, Codex adjudication, green CI on that head, separate explicit Pavlo authorization naming it and squash merge. Until then, this section and the Accepted frontmatter are proposed repository state only.

## 27. Version, migration and rollback

OCP-018 moves `0.1.0 / Draft → 0.2.0 / Accepted`. Under OCP-001 pre-canonical versioning, the lifecycle change is substantive because Accepted makes the current semantics a Board-approved basis for dependents, so `Y` increments. PATCH is insufficient because this is not merely editorial; MAJOR/`1.0.0` is false because no contract meaning is broken or removed and the document is not Canonical.

AD-016 moves `0.27.0 → 0.27.1` by PATCH. Its original trigger facts and AD-016W P-001 ledger facts are time-anchored without changing any decision, candidate, selection, reopening rule or future obligation.

No record, source profile, Organization, Capability, decision, evidence binding, Operation, Assignment, consumer or production representation migrates. Existing exact OCP-018 evidence remains bound to the same semantics. Acceptance does not rebind another source or manufacture missing provenance.

Complete rollback requires a separately reviewed act that restores the primary OCP-018 lifecycle to `0.1.0 / Draft`, restores current README/backlog/roadmap/checker-guide projections, restores AD-016 `0.27.0` plus its prior §1 and §243 bytes, and adjudicates retention of the immutable review snapshot without rewriting historical records. A future rollback may retain AD-016 `0.27.1` only by explicitly re-authorizing both time-anchoring corrections as an independent hygiene result; silent partial rollback is invalid. Rollback cannot remove or reinterpret AD-021's AC selection, reopen AB-017 by implication, legitimize another source or partially rewrite evidence history.

## 28. Non-transfer and next gates

This acceptance stops before Canonicalization, any production-facing source profile, AB-002, Y10D Event discovery, a normative `Review-After` definition act, YR and T6. It does not authorize a schema, implementation, deployment, policy, approval model or next PR.

Any future production profile must name its own legitimate owner, exact contract, evidence, migration and rollback and pass a separate OCP-001/OCP-016 cycle with four fresh exact-head gates. Any future change to P-001 form/version must atomically treat all then-current primary invokers and immutable snapshot carriers under `track-current`.

## 29. Carrier-counter registry clarification

Revision `0.2.1 / Accepted` incorporates only the §25 debt-registry clarification required by AD-022. It replaces the ambiguous phrase “the latter two” with an explicit enumeration of all four AD-016 statements and records their time-anchored closure. The authorization-source contract, lifecycle, dependencies, P-001 binding, executable rules and production boundaries remain unchanged.

Under OCP-001 pre-canonical versioning this is a PATCH: current semantics and obligations are compatible, while retaining `0.2.0` over changed authoritative bytes would conceal the mandated editorial correction. No source profile, decision, evidence binding or consumer migrates. Rollback of this clarification must restore §25 and `0.2.0` together; it cannot alter the historical OCP-018 acceptance act.
