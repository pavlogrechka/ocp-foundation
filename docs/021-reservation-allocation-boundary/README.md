---
Document-ID: OCP-021
Title: Reservation and Allocation Establishment Boundary
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: AD-026, OCP-001, OCP-003, OCP-005, OCP-006, OCP-016, OCP-020
Used-By: Reservation and Allocation review, Constraint composition review, Audit
---

# OCP-021 — Reservation and Allocation Establishment Boundary

## 1. Route and Draft status

OCP-021 is a Route C Core non-Concept contract under OCP-016. It owns one shared composition boundary: exact Resource, Assignment and Constraint evidence—and, for branch Q, Accepted quantitative input—does not by itself establish authoritative Reservation or Allocation.

This `0.1.0` artifact is `Draft`. It creates no Reservation, Allocation or Capacity identity, record family or Concept status. Its only authoritative results are negative establishment results and `indeterminate`.

## 2. Existing normative basis

OCP-005 §13 states that Assignment does not automatically create exclusive Resource reservation, block other Assignments or reserve a quantity. OCP-006 §§11–14 own exact Constraint evaluation and working exclusive-Assignment/capacity patterns, but do not make a blocking result into Reservation. OCP-020 §§9–10 and §16 make exact quantitative input neutral and remove only the accepted-input prerequisite for branch Q.

OCP-021 does not amend those owners. It governs only their composition boundary and preserves their exact references for replay.

## 3. Branch E authority boundary

Branch E is whole-Resource exclusivity and blocking of other Assignments. A positive rule that establishes reservation, Allocation, exclusivity permission or an Assignment effect is positive-capable under OCP-016 G4. No current Accepted consumer, consumer-owned result need, exact positive rule, activation snapshot/context, legitimate owner/evaluator or object form supplies that gate.

E therefore uses `whole-resource-reservation-allocation-boundary@1`. It accepts no quantitative contract or quantitative snapshot reference and returns only an E-specific negative result or `indeterminate`. An Assignment reference, several simultaneous Assignment references, a ConstraintEvaluation reference or their combination cannot be renamed into reservation or Allocation authority.

## 4. Branch Q authority boundary

Branch Q is partial or quantitative reservation/allocation. It exact-requires `OCP-020@0.2.0` and one quantitative input snapshot reference. That proves only that the accepted upstream input prerequisite is named; OCP-021 does not revalidate quantities, compare demand with a limit or derive sufficiency.

Q uses `quantitative-reservation-allocation-boundary@1`. The exact baseline still lacks the positive G4 consumer, result need, rule, activation, legitimate owner/evaluator and object form. Accepted OCP-020 input cannot self-supply any of them.

## 5. Exact evidence envelope

```text
ReservationBoundaryDataset
- establishment_request
- resource_snapshots [zero or more]

ResourceEvidenceSnapshot
- snapshot_ref
- resource_ref
- context_ref
- evidence_state = current | stale
- assignment_refs [one or more, unique]
- constraint_evaluation_refs [zero or more, unique]
- quantitative_input_snapshot_ref [required only for Q]
```

The request exact-resolves one snapshot by `resource_snapshot_ref`. Zero matches fail unresolved; several matches fail ambiguous. Selected `resource_ref` and `context_ref` must exact-match the request, and evidence must be current. `assignment_refs` contains one or more unique opaque exact pointers; `constraint_evaluation_refs` may be empty and otherwise contains unique opaque exact pointers. Their truth remains owned by OCP-005/OCP-006; list order and unreferenced snapshots have no effect.

## 6. Branch E request and derivation

```text
ReservationEstablishmentRequestE
- request_id
- branch = whole_resource_exclusivity
- action = reservation | allocation
- rule_ref = whole-resource-reservation-allocation-boundary@1
- resource_ref
- context_ref
- resource_snapshot_ref
- quantitative_contract_ref = null
- stored_result
```

`derive_whole_resource_reservation_boundary` returns:

- `indeterminate` for any malformed, missing, ambiguous, stale, cross-bound, quantitative-coupled, self-supplied or positive-authority input;
- `whole_resource_reservation_not_established` for an exact current `reservation` request; or
- `whole_resource_allocation_not_established` for an exact current `allocation` request.

The negative result means that this contract has no legitimate positive establishment authority. It does not state that the Resource is unreserved, unallocated, available or safely shareable.

## 7. Branch Q request and derivation

```text
ReservationEstablishmentRequestQ
- request_id
- branch = partial_quantitative
- action = reservation | allocation
- rule_ref = quantitative-reservation-allocation-boundary@1
- resource_ref
- context_ref
- resource_snapshot_ref
- quantitative_contract_ref = OCP-020@0.2.0
- stored_result
```

`derive_quantitative_reservation_boundary` requires the selected snapshot to carry an exact non-empty `quantitative_input_snapshot_ref` and returns:

- `indeterminate` for any malformed, missing, ambiguous, stale, cross-bound, missing/wrong-prerequisite, self-supplied or positive-authority input;
- `quantitative_reservation_not_established` for an exact current `reservation` request; or
- `quantitative_allocation_not_established` for an exact current `allocation` request.

The negative result remains true for this authority boundary even when the referenced upstream OCP-020 snapshot contains valid exact totals. It does not decide capacity, availability or a permitted quantity.

## 8. Result vocabulary and branch separation

The complete result vocabulary is:

- `whole_resource_reservation_not_established`;
- `whole_resource_allocation_not_established`;
- `quantitative_reservation_not_established`;
- `quantitative_allocation_not_established`; and
- `indeterminate`.

No E result is valid for Q and no Q result is valid for E. `reservation` and `allocation` remain different requested actions with different stored negative results. A branch crossover or result mismatch is invalid.

## 9. Fail-safe validation

Malformed datasets, requests or snapshots are invalid. Missing or ambiguous snapshot resolution, duplicate/malformed evidence references, Resource/context mismatch, stale evidence, unknown branch/action, branch/rule mismatch and stored-result mismatch are invalid.

E rejects any quantitative contract or snapshot coupling. Q rejects a missing, older, unknown or otherwise non-exact quantitative contract reference and a missing quantitative snapshot reference. Every invalidity makes the applicable derivation return `indeterminate`.

## 10. Explicit non-implications

No OCP-021 request or result:

- establishes, denies, creates, changes or terminates a Reservation or Allocation;
- proves availability, exclusivity permission, capacity sufficiency, remaining capacity or admissibility;
- creates, blocks, cancels, supersedes or mutates an Assignment;
- creates or changes a ConstraintEvaluationRecord;
- creates Risk or Conflict;
- authorizes an Operation or other action;
- authenticates a production measurement profile, consumer, owner or evaluator; or
- creates `Reservation`, `Allocation`, `Capacity`, `Authority`, `Approval` or `Policy` as a Concept.

## 11. Positive reopening gate and self-supply prohibition

Each branch can be reopened only by a separate Board act that independently proves and exact-binds one concrete Accepted consumer, its baseline and protected result need, one versioned positive rule, one exact input snapshot and evaluation context, a legitimate owner/evaluator and an admitted object form under OCP-016 G4. Q additionally retains exact Accepted OCP-020 input.

OCP-021, the Architecture Board, an AB identifier, a caller label or an `activation_attempt` object cannot self-supply those elements. Even a syntactically complete caller-declared tuple is non-authoritative and yields `indeterminate`.

## 12. Executable evidence

`reservation-boundary-rules.yaml` binds every validation and derivation identifier to this document and declares complete direct fixture coverage. The checker implements §§5–9 with separate E and Q derivations.

Four valid synthetic fixtures cover every branch/action combination, E with and without ConstraintEvaluation references, and Q with the exact Accepted OCP-020 prerequisite. Seventeen material negatives cover malformed shape/request/snapshot, invalid branch/action, unresolved/ambiguous snapshot, binding mismatch, stale evidence, E quantitative coupling, Q missing/wrong prerequisite, positive authority, complete self-supply in each branch, forbidden adjacent coupling and result crossover.

Tests require exact expected error sets, fail-safe derivation for every material negative, branch non-interchangeability, exact manifest equality and mutation failure for every branch, action, rule mapping, result mapping, exact OCP-020 reference and required request/snapshot field. No declared element is accepted solely by documentation.

All values are abstract `SYNTH` references. Fixtures contain no magnitudes, units, timestamps, intervals, coordinates, geometry, sectors, callsigns, organization/unit identifiers, personal data, credentials, keys, tokens or material from another project.

## 13. Route and form decision

Route C is the minimum owner because the invariant composes Resource identity, Assignment references, ConstraintEvaluation references and, for Q, OCP-020 input. Keeping it only in OCP-005, OCP-006 or OCP-020 would make one upstream owner authoritative over the others; duplicating it across them would split truth.

Route F lacks independent Reservation/Allocation identity evidence. Route E lacks a named interoperability consumer/profile. Route D cannot own the shared cross-artifact invariant. Route I cannot own semantic truth. P-001 is not invoked because OCP-021 creates no independently identified record.

## 14. Version, backlog, migration and rollback

OCP-021 `0.1.0 / Draft` is the first compatible surface of a new bounded contract. PATCH/MINOR classification is inapplicable; Accepted or Canonical would overstate absent positive-consumer and production evidence.

AB-025 is resolved only at the EN/QN negative establishment boundary. AB-037 remains Resolved. AB-018, AB-005, AB-002 and AB-036 remain Open. OCP-019 remains Draft and OCP-020 remains Accepted.

No migration is required. Existing Resource, Assignment, Constraint and quantitative-input artifacts remain valid and are not required to carry OCP-021 data. Rollback removes this Draft, its manifest, module, tests, fixtures and accounting and restores AB-025 Open; it cannot create positive Reservation/Allocation authority by implication.

Merge requires exact-head external review, Codex adjudication, green required CI and fresh explicit owner authorization naming the unchanged head. Draft preparation and review authorize no production use or next act.
