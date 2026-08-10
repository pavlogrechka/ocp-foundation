---
Document-ID: OCP-020
Title: Quantitative Constraint Input Contract
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: AD-025, OCP-001, OCP-003, OCP-005, OCP-006, OCP-016
Used-By: Quantitative Constraint input review, Consumable measurement review, Audit
---

# OCP-020 — Quantitative Constraint Input Contract

## 1. Route and Draft status

OCP-020 is a Route C Core non-Concept contract under OCP-016. It owns one shared structural input boundary for exact quantities used by more than one downstream surface: profile-owned unit declarations, snapshot-bound quantitative bindings and exact-unit aggregation.

This `0.1.0` artifact is `Draft`. It does not create `Quantity`, `Capacity`, `Reservation` or `Allocation` identity and adds no row to the Concept registry. Acceptance, a positive capacity rule and any reservation model require separate Board acts.

## 2. Existing normative basis

OCP-003 §§5.2 and 13 distinguish Resource identity from amount, consumption, remaining capacity and unit of measure, and require a separate accepted consumable/measurement contract. OCP-005 §§13–14 permit a separate model after Constraint and leave quantity of consumption unresolved. OCP-006 §14.2 names quantity, unit, aggregation and measurement as a separate input contract for later capacity evaluation; §§22–23 keep capacity consumption and partial reservation deferred.

OCP-020 supplies only that separate input. It does not amend the three defining documents or inherit semantic authority from their examples and open questions.

## 3. G4 boundary before object form

OCP-016 G4 applies when a proposed specialization would produce an authoritative positive result for Assignment reservation/allocation, Constraint capacity sufficiency or a combined capacity-reservation decision. The exact baseline has no Accepted consumer that owns such a result need, rule and legitimate evaluator. OCP-005 and OCP-006 are Draft defining documents; the Accepted OCP-013, OCP-014 and OCP-015 consumers explicitly exclude capacity, reservation or allocation authority.

The neutral sum defined here does not decide whether demand fits a capacity limit. It is arithmetic over exact declared operands, not an operational positive result. A caller cannot combine the word `capacity_limit` with a total to claim that G4 has opened.

## 4. Identity, ownership and authority boundary

`QuantitativeBinding` is an inline input shape, not a durable governed record family. `MeasurementProfile` is an exact external reference owned outside this Draft. Neither has lifecycle, history, supersession, current-head selection or P-001 identity here.

The profile owner is attribution and an agreement key. The checker does not authenticate that owner, approve a production profile or grant authority. No implementation label, caller assertion, timestamp, count, order or newest version can establish a legitimate capacity or reservation decision.

## 5. Measurement profile and quantitative binding

```text
MeasurementProfile
- profile_ref
- profile_owner_ref
- units [one or more]
  - unit_ref
  - dimension_ref

QuantitativeBinding
- binding_key
- subject_ref
- role = demand | capacity_limit | consumed
- magnitude_lexeme
- unit_ref
- dimension_ref
- measurement_profile_ref
- profile_owner_ref
- context_ref
- input_snapshot_ref
- provenance_ref
- evaluator_ref
```

Each reference is non-empty and exact. Within the selected profile, `unit_ref` resolves exactly one declaration whose `dimension_ref` matches the binding. A magnitude is a finite non-negative canonical base-10 lexical value: `0`, a non-zero integer without a leading zero, or a decimal without trailing fractional zeroes. Binary floating-point interpretation, implicit precision, unit conversion and inferred dimensions are prohibited.

`role` is a classification of the input only. `capacity_limit` does not mean available capacity, admissibility or permission, and this version never aggregates it.

## 6. Snapshot and binding exactness

```text
QuantitativeInputSnapshot
- snapshot_ref
- context_ref
- evidence_state = current | stale
- bindings [zero or more]
```

An aggregation request exact-binds one snapshot, context, measurement profile and profile owner. Every selected binding repeats those exact values and its input snapshot. A reference resolves one binding by `binding_key`; absence and duplicate resolution fail closed. Stale evidence, cross-context data, cross-snapshot data and owner/profile mismatch fail closed.

Unreferenced bindings have no effect. Reordering the same bindings or operand references has no effect. The contract never chooses a newest snapshot or a list-order winner.

## 7. Exact-unit aggregation

```text
QuantitativeAggregationRequest
- contract_ref = OCP-020@0.1.0
- rule_ref = exact-unit-quantity-sum@1
- input_snapshot_ref
- context_ref
- measurement_profile_ref
- profile_owner_ref
- role = demand | consumed
- operand_keys [one or more, unique]
- stored_total

QuantitativeTotal
- magnitude_lexeme
- unit_ref
- dimension_ref
```

`derive_quantitative_total` returns a total only when every operand resolves exactly, all operands repeat the request bindings, all use the requested role, and all share one exact `unit_ref` and `dimension_ref` declared by the selected profile. It sums canonical decimal values exactly and renders a canonical decimal result.

No conversion is attempted. Mixed units fail even when a caller asserts that they share a dimension. Mixed dimensions fail. `demand` and `consumed` are never aggregated together. A stored total is replay evidence only and must exactly equal the derivation.

## 8. Fail-safe validation

Malformed profile, snapshot, request or binding data is invalid. Missing or ambiguous references, stale evidence, cross-bound inputs, duplicate operands, non-canonical values, mixed units, mixed dimensions and a mismatched stored result are invalid. Any invalidity makes the derivation return no total.

The validator also rejects fields that couple this neutral input to reservation, allocation, availability, capacity sufficiency, admissibility, Assignment mutation, lifecycle transition, permission, authorization, Risk, Conflict, write-off or unit conversion. Renaming such a result or embedding it beneath another object does not confer authority.

## 9. Explicit non-implications

An exact total does not:

- prove capacity sufficiency, remaining capacity or availability;
- reserve or allocate a Resource, whole or partial;
- create, amend, activate, suspend or terminate an Assignment;
- establish Constraint applicability, satisfaction or precedence;
- create Conflict or Risk;
- authorize an Operation or other action;
- establish a production measurement profile, physical unit catalogue or conversion rule; or
- create a `Quantity`, `Capacity`, `Reservation`, `Allocation`, `Authority`, `Approval` or `Policy` Concept.

## 10. Separate positive-model gates

A capacity predicate or result must be a later act that exact-binds a concrete Accepted consumer, its baseline and result need, one versioned rule, one exact input snapshot and context, and a legitimate owner/evaluator under OCP-016 G4. OCP-006 can then consume this contract as input, but cannot self-supply the missing Accepted consumer by being the upstream defining document.

Whole-Resource exclusivity may be assessed separately because it need not depend on quantity. Partial or quantitative reservation/allocation requires this input contract to be accepted first and still requires its own object-form and G4 adjudication. This Draft does not reserve those outcomes.

## 11. Executable evidence

`quantitative-input-rules.yaml` binds every validation and derivation identifier to this document and declares complete direct fixture coverage. The checker implements §§5–8 without comparing demand to capacity.

Sixteen synthetic fixtures include exact demand and consumed totals plus separate malformed-shape, malformed-profile, unresolved-profile, ambiguous-profile, wrong-owner, missing-unit, non-canonical-value, cross-bound, stale, duplicate-operand, mixed-unit, mixed-dimension, mismatched-result and forbidden-coupling cases. Tests require exact expected error sets, fail-closed derivation for every negative, order invariance, isolation from unreferenced bindings and exact equality between the manifest and exported rule sets.

All fixtures use only `SYNTH` references and abstract decimal lexemes. They contain no real quantities, unit names, capacities, coordinates, geometry, sectors, windows, callsigns, organization identifiers, personal data or material from another project.

## 12. Route and form decision

Route C is the minimum shared home because OCP-003 and OCP-006 independently require the same quantity/unit input boundary. Route D would duplicate exactness and aggregation semantics; Route E lacks a named interoperability consumer; Route F lacks identity evidence; Route I cannot own semantic truth.

The selected form is a non-Concept structural input and derived projection. Assignment and Constraint specializations remain legitimate later alternatives, but their positive forms are presently G4-blocked. A Reservation/Allocation record remains a separate object-form decision.

## 13. Migration and rollback

Draft adoption requires no migration. Existing Resource, Operation, Assignment and Constraint artifacts remain valid because none is required to carry an OCP-020 binding. A future consumer opts in only by exact-binding the accepted version after a separate admission act.

Rollback removes this document, its manifest, checker module, fixtures, tests and accounting entries. It changes no Concept registry row, graph edge, canonical identity or stored production data.

## 14. Status and backlog boundary

OCP-020 `0.1.0 / Draft` records the selected AB-037 input direction. AB-037 is resolved only as the bounded units/aggregation model selected by AD-025; acceptance and every positive capacity activation remain future gates. AB-025 remains Open. AB-002, AB-005, AB-018 and AB-036 remain Open and unchanged.

Merge requires exact-head external review, Codex adjudication, green required CI and fresh explicit owner authorization naming the unchanged head. Draft preparation and review do not authorize merge or production use.
