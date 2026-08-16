---
Document-ID: OCP-023
Title: Resource Occupancy Derivation
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: AD-041, OCP-001, OCP-003, OCP-005, OCP-016
Used-By: Resource occupancy domain review and synthetic reference validation
Last-Review: 2026-08-17
---

# OCP-023 — Resource Occupancy Derivation

## 1. Route D and Draft status

OCP-023 is a governed **Route D domain-local** document under OCP-016. The named domain is Resource occupancy: it owns only the meaning of the derived statement “Resource `R` is occupied at instant `t`” and the exact Assignment references that witness that statement. It does not redefine Resource or Assignment, change a Core contract, create a Concept or claim Core placement.

This first exact body is `0.1.0 / Draft`. The Architecture Board selected the narrow domain scope and authorized preparation, not acceptance of text that did not yet exist. OCP-001 requires external review and a separate explicit lifecycle action before `Accepted`; no reviewed-contract snapshot is due for a Draft under AD-029. Draft status also makes the reference rule non-activating.

## 2. Exactly one derived statement

The sole derived value is:

> `occupied(resource_ref, evaluation_time)` is true exactly when at least one Assignment in the exact complete Assignment snapshot for that Resource is effective at the evaluation instant. Its witness set is every such Assignment reference.

False means no Assignment in that exact complete snapshot is effective at the instant. Witness references are sorted by Assignment identity, so input order conveys no priority or selection.

This document derives no Conflict, conflict establishment, priority, ordering, capacity, remainder, reservation, allocation, permission, authorization, Assignment lifecycle change or action recommendation.

## 3. Gate-first: Route and G4 are separate questions

Route D is the minimum route. The statement is domain-local Resource-state interpretation, has one named domain, and neither changes a shared Core envelope nor supplies cross-domain Core semantics. Route C would wrongly move the meaning into Core; Route E lacks an interoperability profile; Route F would require a new fundamental Concept; Route I cannot own semantic truth. `not Core` therefore does not mean invalid.

Route D does **not**, however, erase OCP-016 G4. AD-015 §35.2 and current OCP-016 §5 apply G4 activation to positive-capable rules, results and profiles in the route that owns the protected use, including domain-local work. `occupied=true` is positive-capable. Activation would require an exact Accepted consumer, baseline, protected need, rule version, input snapshot, evaluation context and legitimate owner/evaluator.

No such activation exists on the baseline. OCP-023 is itself Draft and cannot self-supply an Accepted consumer; the Architecture Board's governance ownership is not a substitute for the future legitimate domain evaluator. The executable module and fixtures are therefore a synthetic reference proof only. Activation fields are rejected, and this act does not claim an operational result.

## 4. Direct unmet Core input need

The document's intended Resource-wide statement cannot be derived from the current Core surface alone. OCP-005 and the checker expose `assignment_effective_at(assignment, at)` for one Assignment; `derived_participates_in` filters a caller-provided set further by one Operation. Neither owner provides the exact positive result:

> **`assignment_set_complete_for_resource(resource_ref, evaluation_time, snapshot_ref)`** — the named snapshot contains every Assignment whose current truth must be considered for that Resource and instant.

Without that result, one effective Assignment can witness `occupied=true`, but an empty or non-effective caller-provided list cannot justify `occupied=false`: an omitted effective Assignment would reverse the answer. OCP-023 therefore cannot discharge its own declared Resource-wide obligation without a completeness result. This is a current inability, not “may be useful”, an open-question label or a claim that absence is already proven.

The Draft does not define that Core result, authenticate its producer or activate it. Synthetic fixtures carry `SYNTH-COMPLETE-*` evidence solely to test the proposed derivation. A non-synthetic completeness contract and its G4 binding require separate acceptance and activation work.

## 5. Exact reference envelope

```text
ResourceOccupancyDataset
- occupancy_request
- assignment_snapshots [zero or more]

OccupancyRequest
- request_id
- rule_ref = resource-occupancy-at@0.1.0
- resource_ref
- evaluation_time
- assignment_snapshot_ref
- stored_occupied = true | false
- stored_witness_assignment_refs [zero or more, unique]

AssignmentSnapshot
- snapshot_ref
- resource_ref
- completeness_evidence_ref = SYNTH-COMPLETE-* (reference fixtures only)
- assignments [zero or more complete OCP-005 Assignment values]
```

The request exact-resolves one snapshot. Zero matches are unresolved; several are ambiguous. Snapshot and request Resource references must match. Every Assignment must independently satisfy the current OCP-005 reference validator, exact-bind the requested Resource and have a unique `assignment_id`.

## 6. Derivation

`derive_resource_occupancy` first validates the exact reference envelope and rejects any activation or forbidden adjacent coupling. It then applies the existing `assignment_effective_at` truth to every Assignment in the selected snapshot at the exact `evaluation_time`.

- one or more effective values → `occupied=true` and the sorted complete tuple of their `assignment_id` values;
- no effective values in the complete snapshot → `occupied=false` and an empty witness tuple;
- malformed, unresolved, ambiguous, cross-bound, incomplete, invalid, duplicate, activating or forbidden input → `occupied=None` and no witnesses.

`None` is fail-safe reference behavior, not a second domain statement. Stored boolean and witness values must equal the derivation exactly.

## 7. Time and multiplicity boundaries

OCP-023 reuses OCP-005 time semantics without amendment: the applicability start is inclusive, the applicability end and terminal instant are exclusive, and Establishment must have occurred no later than the evaluated instant. It neither defines retroactivity nor multiple applicability intervals.

Several effective Assignments for one Resource make occupancy true and all are retained as witnesses. Their coexistence does not establish Conflict, select one Assignment, rank them or mutate either record.

## 8. Executable evidence

`resource-occupancy-rules.yaml` exact-binds the validation and derivation identifiers to this document. The checker module implements §§5–7 without changing the existing single-Assignment functions.

Six new, fully synthetic fixtures cover: no Assignment, one effective Assignment, two overlapping effective Assignments, two non-overlapping Assignments evaluated in their gap, the inclusive start boundary and the exclusive end boundary. Focused tests require exact stored results, every overlap witness independent of input order, completeness before false, fail-safe invalid behavior and exact manifest equality.

The suite includes `test_every_defensive_value_is_individually_fixture_and_mutation_live`. It removes or mutates every dataset/request/snapshot field, activation field, forbidden field, rule reference, synthetic completeness prefix, validation identifier and derivation identifier individually. No declared value is protected only as a category.

All references and times are synthetic (`R-001`, `OP-001`, `A-001`, `2026-08-02T10:00:00Z`). No coordinates, routes, units, real operational records, personal data, credentials, tokens or material from another project is used.

## 9. Explicit non-implications

No request, snapshot, result or witness in OCP-023:

- establishes or denies Conflict;
- grants priority, chooses an Assignment or orders competing evidence;
- proves availability, capacity, remainder, exclusivity, reservation or allocation;
- grants permission or authorization;
- creates, transitions, supersedes, closes or revokes an Assignment;
- recommends an Operation or any other action;
- creates a Resource Occupancy, Conflict, Capacity, Reservation or Allocation Concept; or
- activates a production rule, consumer, owner, evaluator or completeness source.

## 10. Version, migration, rollback and gates

`0.1.0` is the first exact surface of a new Route D OCP document. PATCH/MINOR/MAJOR revision classification is inapplicable because no earlier version exists. `Accepted` would overstate the absent exact-body review and G4 activation evidence; `Canonical` would additionally overstate stability and Core significance.

No existing artifact or stored data migrates. Rollback removes OCP-023, its manifest, module, tests, six new fixtures and descriptive accounting. It cannot alter Resource, Assignment or any Core truth because all existing documents, fixtures, snapshots, patterns, registries, graphs and promotion gates remain byte-identical.

Merge requires exact-head external review, Codex adjudication, green required CI and fresh explicit Pavlo authorization naming the unchanged head. Preparation or merge of this Draft authorizes neither acceptance, G4 activation nor a next act.
