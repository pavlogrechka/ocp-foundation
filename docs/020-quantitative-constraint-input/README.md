---
Document-ID: OCP-020
Title: Quantitative Constraint Input Contract
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-025, OCP-001, OCP-003, OCP-005, OCP-006, OCP-016
Used-By: Quantitative Constraint input review, Consumable measurement review, Audit
Last-Review: 2026-08-10
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

Eighteen synthetic fixtures include exact demand and consumed totals, a valid non-aggregated `capacity_limit`, and separate malformed-shape, malformed-profile, unresolved-profile, ambiguous-profile, wrong-owner, missing-unit, non-canonical-value, cross-bound, stale, duplicate-operand, selected-capacity-limit, mixed-unit, mixed-dimension, mismatched-result and forbidden-coupling cases. Tests require exact expected error sets, fail-closed derivation for every semantic negative, rejection when the declared `capacity_limit` role is removed, order invariance, isolation from valid unreferenced bindings and exact equality between the manifest and exported rule sets.

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

## 15. Authority and incorporated reviewed body

Architecture Board accepts OCP-020 revision `0.2.0` as the governed Route C non-Concept quantitative-input contract selected by AD-025 Outcome QC and the bounded resolution of AB-037.

The complete externally reviewed `0.1.0 / Draft` is preserved byte-for-byte in [`reviewed-contract-v0.1.0.md`](reviewed-contract-v0.1.0.md). Its numbered §§1–12 and the semantic, evidence and non-implication boundaries of §§13–14 are incorporated here without alteration. Snapshot frontmatter, Draft lifecycle wording, pre-acceptance rollback wording and pre-merge gate wording remain immutable historical review evidence; this README is the sole current lifecycle and acceptance authority.

The original §§1–14 remain in this primary README with unchanged text and numbering. Existing manifest sources therefore continue to resolve to the same OCP-020 sections, with no competing semantic owner and no `source:` change.

Acceptance means the Board approves the incorporated semantics as a basis for dependent specifications under OCP-001. It does not make OCP-020 Canonical, promise `1.x` stability, authenticate a measurement-profile owner or legitimize a production measurement profile.

## 16. Acceptance basis and bounded prerequisite effect

OCP-001 defines `Accepted` as Board approval of current semantics for dependent specifications, distinct from Canonical status and from a `1.x` stability guarantee. The exact Draft body was adversarially reviewed on PR #143, its executable evidence was reproduced, and the semantic surface is unchanged in this act.

AD-025 §8 item 3 states that partial or quantitative reservation depends on an **accepted** input and still requires its own object-form and OCP-016 G4 decision. This lifecycle transition satisfies only that named input-status prerequisite. It does not establish the missing Accepted capacity-result consumer, positive rule, legitimate owner/evaluator, object form, reservation identity or merge authority for a later act.

Whole-Resource exclusivity remains independently adjudicable because it may not depend on quantity. AB-025 remains Open for both branches until a separately mandated comparison and four fresh gates decide them.

## 17. Accepted compatibility and authority surface

The accepted compatibility surface is exactly the incorporated Draft surface:

- roles remain `demand | capacity_limit | consumed`, while only `demand | consumed` are aggregatable;
- `exact-unit-quantity-sum@1` remains the only derivation rule;
- exact profile, owner, unit, dimension, context, snapshot and operand bindings remain mandatory;
- canonical non-negative decimal lexical values and same-unit/same-dimension aggregation remain exact;
- malformed, missing, ambiguous, stale, cross-bound, mixed-unit, mixed-dimension, result-mismatched and forbidden-coupled inputs remain fail-safe; and
- a total remains neutral arithmetic, never a capacity-sufficiency, availability, reservation, allocation, permission, lifecycle, Risk or Conflict result.

The result shape, validation IDs, rule manifest and checker module are unchanged. OCP-020 still has no `Uses-Patterns`; acceptance neither invokes P-001 nor creates an independently identified record family.

## 18. Reviewed-snapshot convention and registered governance debt

The exact base contains seven `Status: Accepted` primary OCP documents—OCP-011, OCP-012, OCP-013, OCP-014, OCP-015, OCP-017 and OCP-018—and each has exactly one sibling `reviewed-contract-vX.Y.Z.md`. Canonical OCP-016 also has exactly one such snapshot. No base `Status: Draft` primary OCP has one. OCP-020 follows that complete repository convention by preserving its `0.1.0` Draft under the same sibling naming form.

The convention is not a normative repository-wide obligation. OCP-001 mentions reviewed-contract snapshots only as historical instances of the same artifact identity, while artifact governance checks no required presence, naming, digest or primary-to-snapshot mapping. Therefore a different acceptance proposal without a snapshot could remain mechanically green.

This act registers that gap rather than adding an ad hoc OCP-020-only rule or silently expanding OCP-001. A general guard first needs a separately reviewed governance definition, structured primary-to-snapshot mapping, treatment of heterogeneous pre-acceptance versions and a migration rule covering both Accepted OCPs and Canonical OCP-016. Its required mutation proof is explicit: removing the mandated snapshot from an otherwise Accepted candidate must fail. That cross-OCP governance work exceeds a semantic-no-change OCP-020 acceptance and is not authorized here.

## 19. Exact acceptance baseline and anchor chain

The acceptance baseline is exact `main@da2bce1f3ec76f4d59fb3c9d0efa76bf4ce4fc11`, tree `14c424d28053e0255065ad519ee0ece148daccb7`. Every blob below was resolved at that commit, reverse-resolved through `git ls-tree -r` to the listed path, checked against the declared state inside the object and independently SHA-256 hashed from raw bytes.

| Artifact | Reverse-resolved path | Declared state on exact base | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-020 Draft | `docs/020-quantitative-constraint-input/README.md` | `0.1.0 / Draft`; §§1–14 reviewed semantic body | `f1f65eadb6a6c7c4fb80d6fd15b36a4c147a9603` | `05992f1006dee9c2dca137e6145f3c5c70ce57746bb0febb79a3ca9598146bb8` |
| AD-025 | `architecture/discovery/AD-025-quantitative-constraint-input.md` | `0.1.0 / Accepted`; QC selected, AB-037 resolved, AB-025 Open | `cd4e320be2db6398d758c6fa3ae49e0a0f520df5` | `dae3ee9ea8ffbe0fb62df127fa53920705d59f50ec793cb41cb6ca3c10642d46` |
| OCP-001 | `docs/001-ontology-governance/README.md` | `1.0.0 / Canonical`; Accepted and atomic lifecycle contract | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; G4 and non-transfer gates | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| quantitative module | `tools/ontology_checker/ocp_checker/quantitative_input.py` | roles, exact-unit derivation and fail-safe validation | `8ec2f14d509841266eb3368657a9c0e2fbbd6a57` | `0ab868c5c0bd7d964cd206996ee70295095c90efdead559a3985253a2ecf8515` |
| quantitative manifest | `tools/ontology_checker/quantitative-input-rules.yaml` | thirteen validation IDs plus one derivation ID | `26cdf92b5a14fcacae5a35b4b8024e4766a89777` | `13b7e697c336d35b9df542893199de499a00d4434bdba4cb312f10566226c3a5` |
| focused tests | `tools/ontology_checker/tests/test_quantitative_input.py` | six test methods; role-removal regression included | `d003eff324550414ef7b0b30fa6927abffb94357` | `e773754a22495789c57773d2c62bfdf8b2aa4cba8f305802d8dcc57d134c14ff` |

The new snapshot has Git blob `f1f65eadb6a6c7c4fb80d6fd15b36a4c147a9603` and SHA-256 `05992f1006dee9c2dca137e6145f3c5c70ce57746bb0febb79a3ca9598146bb8`, exactly equal to the anchored Draft. Blob, digest, byte count and direct comparison establish byte identity; they do not supply lifecycle or merge authority.

## 20. Executable conformance, unchanged evidence and safety

The quantitative module, manifest, focused tests and eighteen fixtures remain byte-identical to the exact base. No validation ID, derivation ID, role, rule, result shape, expected error set or fixture byte changes. The repository remains at `218/218` unit tests and `184/184` fixtures in both PR and `main` contexts; no test or fixture is added because acceptance introduces no behavior.

The acceptance proof separately compares the new snapshot with the exact base Draft blob and compares the candidate module and manifest blobs with their exact base blobs. These checks establish unchanged evidence rather than granting semantic or Board authority.

The snapshot contains only the already reviewed synthetic material. This act adds no quantity, unit name, capacity, coordinate, geometry, sector, window, callsign, organization identifier, personal data, credential, key, token or material copied from another project.

## 21. Architecture Board acceptance decision

On 2026-08-10, Architecture Board:

1. accepts OCP-020 revision `0.2.0` as the governed QC quantitative-input contract and retains Route C non-Concept form;
2. incorporates the byte-identical `0.1.0` reviewed body without changing roles, rules, results, evidence or non-implications;
3. recognizes that Accepted input removes only the prerequisite named by AD-025 §8 item 3;
4. keeps every capacity predicate/result and every reservation/allocation object-form decision behind its own consumer, rule, G4 and four-gate act;
5. keeps AB-025, AB-018, AB-005, AB-002 and AB-036 Open;
6. changes no Concept, Concept status, registry row, taxonomy projection, graph edge, foundation-map entry, P-001 invocation or `Review-After` field;
7. registers the reviewed-snapshot governance debt without claiming a repository-wide machine guard; and
8. transfers no authority to another act.

This decision becomes effective only after Fable review of one exact unchanged acceptance head, Codex adjudication, green CI on that head, separate explicit Pavlo authorization naming it and squash merge. Until then, this section and the Accepted frontmatter are proposed repository state only.

## 22. Version, migration and rollback

OCP-020 moves `0.1.0 / Draft → 0.2.0 / Accepted`. Under OCP-001 pre-canonical versioning, the lifecycle transition is substantive because it makes the unchanged semantics a Board-approved basis for dependents and satisfies one named AB-025 prerequisite; therefore `Y` increments. PATCH is false because this is not editorial. MAJOR/`1.0.0` is false because no semantic meaning is broken or removed, Canonical status is not granted and no `1.x` stability promise is made.

No quantitative input, measurement profile, owner, unit, binding, snapshot, total, Resource, Assignment, Constraint, consumer, fixture, test or production representation migrates. Existing exact `OCP-020@0.1.0` rule bindings continue to name the incorporated compatibility surface; acceptance does not silently rewrite them to `@0.2.0` or manufacture a production profile.

Rollback requires a separately reviewed act that restores the primary lifecycle to `0.1.0 / Draft`, restores README/backlog/roadmap/checker-guide projections and adjudicates retention of the immutable reviewed snapshot without rewriting historical evidence. Rollback cannot reopen AB-037, resolve AB-025, authorize a capacity result or reinterpret AD-025 by implication.

## 23. Non-transfer and next gates

Operational-rules readiness remains `29%`, machine-readable readiness remains `77%` and overall readiness remains `≈72%`: the Draft already contributed its behavior and evidence, while this act adds lifecycle approval only.

Acceptance stops before Canonicalization, a production measurement profile, positive capacity sufficiency/availability, Reservation/Allocation, AB-025 resolution, AB-018, AB-005, AB-002, AB-036, Y10D, a normative `Review-After` definition act, YR and T6. It authorizes no next PR.

Any later partial/quantitative reservation proposal must obtain its own mandate, prove its concrete Accepted consumer, baseline, exact positive rule, snapshot/context and legitimate owner/evaluator, decide object form under OCP-016, and pass four fresh exact-head gates.
