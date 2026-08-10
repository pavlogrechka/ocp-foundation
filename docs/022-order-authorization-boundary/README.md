---
Document-ID: OCP-022
Title: Order Authorization Establishment Boundary
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: AD-030, OCP-001, OCP-004, OCP-016, OCP-017, OCP-018
Used-By: Order authorization review, Operation authorization review, Audit
---

# OCP-022 — Order Authorization Establishment Boundary

## 1. Route and Draft status

OCP-022 is a Route C Core non-Concept contract under OCP-016. It owns one shared negative boundary: current Core evidence does not establish that an `Order` is mandatory, sufficient or an admissible source of Operation authorization.

This `0.1.0` artifact is `Draft`. It does not define Order identity, fields, lifecycle, issuer, owner, evaluator or profile. It creates no Concept, record family, registry row, `Concept-Status`, taxonomy projection or graph edge. The existing OCP-000 `Order | Proposed | AB-002` marker remains byte-unchanged.

## 2. Existing normative basis

OCP-017 `0.2.0 / Accepted` owns the consumer-side requirement that a transition to `Authorized` exact-bind accepted authorization evidence. It expressly cannot issue an Order, prove source-owner legitimacy or grant permission.

OCP-018 `0.2.1 / Accepted` owns a general Route C source-profile and decision contract without Order. Its §§3 and 12 state that Order is neither mandatory nor sufficient and may become one source profile or evidence kind only after a separate AB-002 act. OCP-022 preserves that contract unchanged and does not reinterpret a generic OCP-018 source as an Order source.

OCP-004, OCP-005, OCP-006 and OCP-008 retain their existing separations between provenance, authorization and Order. An opaque provenance reference that happens to name an Order does not establish authorization semantics.

## 3. G4 authority boundary

Making Order mandatory, sufficient or positively admissible is positive-capable under OCP-016 G4. OCP-017 supplies a generic Accepted authorization-evidence consumer and OCP-018 supplies a generic Accepted source contract, but the exact current baseline supplies no Order-specific protected consumer need, versioned positive rule, activation snapshot/context, legitimate source owner/evaluator or admitted object form.

OCP-022, AB-002, the Architecture Board and a caller-declared activation cannot self-supply those missing elements. The current negative boundary may proceed because it never establishes authorization, permission or Order status.

## 4. Questions and result vocabulary

The three questions remain mechanically distinct:

| Question | Exact rule | Negative result |
|---|---|---|
| `mandatory_order` | `mandatory-order-establishment-boundary@1` | `mandatory_order_not_established` |
| `sufficient_order` | `sufficient-order-establishment-boundary@1` | `sufficient_order_authorization_not_established` |
| `admissible_order_source` | `admissible-order-source-establishment-boundary@1` | `admissible_order_source_not_established` |

The only other result is `indeterminate`. Each negative result means that this contract has no legitimate positive establishment authority for that exact question. It does not prove that no Order exists in reality or prohibit a future separately governed Order profile.

## 5. Evidence snapshot

```text
OrderAuthorizationEvidenceSnapshot
- snapshot_ref
- subject_operation_ref
- source_contract_ref = OCP-018@0.2.1
- source_owner_ref
- input_snapshot_ref
- evaluation_context_ref
- evidence_state = current | stale
- source_result = accepted | denied
- order_candidate_ref
```

The snapshot preserves the exact generic authorization evidence context used by the inquiry. `source_owner_ref`, input and evaluation context are attributable evidence only; OCP-022 does not authenticate them. `order_candidate_ref` is an opaque inquiry token. It is not resolved as a Core entity and does not create Order identity.

An `indeterminate` OCP-018 result cannot support a complete negative inquiry. Accepted and denied generic source results both remain insufficient to establish any of the three Order propositions.

## 6. Boundary request

```text
OrderAuthorizationBoundaryRequest
- request_id
- question
- rule_ref
- subject_operation_ref
- authorization_snapshot_ref
- stored_result
```

One request exact-resolves one snapshot. The subject Operation must match. Zero or several snapshot matches fail closed. Unreferenced snapshots and list order have no effect.

The dataset also contains a `claims` map solely so the reference checker can reject named positive, Concept-coupled, convenience-selected, self-supplied or side-effect assertions. Unknown implementation claims remain outside this bounded checker slice unless they collide with a named prohibition; production schemas may be stricter.

## 7. Exactness and non-selection rules

The exact source contract is `OCP-018@0.2.1`. A different, missing or newest-selected contract is invalid. The selected snapshot must be current and carry a definitive OCP-018 result. Subject mismatch, malformed fields, stale evidence, duplicate resolution or stored-result disagreement yields `indeterminate`.

Timestamp, record order, source count, issuer count and caller identity cannot make an Order proposition true. A generic accepted authorization result does not retroactively classify its evidence as an Order, and a denied result does not prove an Order absent.

## 8. Normative derivation

```text
derive_order_authorization_boundary(dataset) :=
    indeterminate
        if dataset, request or selected snapshot is malformed
        OR snapshot resolution is zero or multiple
        OR subject, source contract or result binding differs
        OR evidence is stale or non-definitive
        OR question and exact rule disagree
        OR a positive, Concept, selector, self-supply or side-effect claim is present

    mandatory_order_not_established
        if the exact question is mandatory_order

    sufficient_order_authorization_not_established
        if the exact question is sufficient_order

    admissible_order_source_not_established
        if the exact question is admissible_order_source
```

No branch returns `order_required`, `order_sufficient`, `order_admissible`, `authorization_established` or `permission_granted`.

## 9. Fail-safe validation

Malformed request or snapshot shapes, unresolved or ambiguous snapshots, subject mismatch, wrong source contract, stale evidence, non-definitive source result and stored-result mismatch are invalid. Every invalidity makes the derivation `indeterminate`.

The executable boundary separately rejects every named value in five defensive sets: positive authority, Concept/registry/graph coupling, convenience selectors, G4 self-supply and adjacent side effects. No declared set member relies only on category-level prose.

## 10. Explicit non-implications

No OCP-022 request, snapshot or result:

- defines, accepts, canonicalizes, deregisters or deprecates Order;
- makes Order mandatory, sufficient, admissible, preferred or prohibited;
- grants authorization, permission, approval or command authority;
- changes an OCP-017 lifecycle transition or mutates Assignment;
- authenticates an owner, evaluator, issuer or production profile;
- introduces `Authority`, `Approval`, `Policy`, `Exception` or `Waiver` as Concepts; or
- changes OCP-018, its open questions, AB-017 or any existing source decision.

## 11. Positive reopening gate

A future positive proposal requires a separate Board act. Before form selection it must exact-bind one concrete Accepted consumer with an Order-specific protected need, that consumer's baseline, one versioned positive Order rule, one exact input snapshot and evaluation context, a legitimate source owner/evaluator and an admitted object form under OCP-016.

If the proposed form is a fundamental Concept, the act must separately change OCP-000, OCP-002 and the graph atomically. If it is an OCP-018 source profile, a named legitimate profile owner and evaluator must govern it; OCP-018 and OCP-022 cannot self-approve the profile.

## 12. Executable evidence and safety

`order-authorization-boundary-rules.yaml` binds every validation and derivation identifier to this document and declares complete direct fixture coverage. Three valid fixtures cover mandatory, sufficient and admissible-source questions, both definitive OCP-018 results, unreferenced-snapshot isolation and distinct negative results. Thirty-two material negatives cover malformed dataset/request/snapshot, unknown question, unresolved/ambiguous resolution, subject mismatch, wrong source contract, stale/non-definitive evidence, every individual positive-authority, Concept-coupling, convenience-selector and side-effect field, complete self-supply and stored-result mismatch.

Focused tests require exact expected errors, fail-safe derivation, order independence, exact manifest equality and individual mutation evidence for every question, rule, result, source-result value, exact contract reference, required dataset/request/snapshot field and every member of all five defensive sets.

All fixtures are synthetic and abstract. They contain no real order wording, requisites, numbers, issuer positions, organization or unit names, operations, coordinates, geometry, frequencies, windows, personnel, credentials or material copied from another project.

## 13. Route and form decision

Route C is the minimum shared owner because the boundary composes the OCP-017 consumer envelope with the OCP-018 source contract and must be consistent across Operation authorization review. It does not grant positive authority.

Route F lacks independent Order identity evidence and would require a separately authorized registry/taxonomy/graph act. Route E lacks a named interoperability profile and legitimate owner. Route D could own a future source profile but cannot establish a shared Core rule without a named domain consumer. Route I cannot own semantic authorization truth. P-001 is not invoked because no independently identified record is created.

## 14. Version, backlog, migration and rollback

OCP-022 `0.1.0 / Draft` is the first compatible surface of this negative boundary. PATCH/MINOR classification is inapplicable; Accepted or Canonical would overstate absent positive-consumer and production evidence.

AB-002 is Resolved only at the three negative establishment results in §4. Order remains `Proposed` in OCP-000, and a future positive or deregistration proposal must reopen AB-002 through the applicable separate act. AB-017 remains Resolved. AB-018 and AB-005 remain Open.

No data, source profile, authorization decision, Operation, Assignment or provenance reference migrates. OCP-018 remains byte-unchanged. Rollback removes OCP-022, its module, manifest, tests, fixtures and accounting and restores AB-002 Open; rollback does not create positive Order authority.

Merge requires exact-head external review, Codex adjudication, green required CI and fresh explicit owner authorization naming the unchanged head. Preparation and review authorize no production use or next act.
