---
Decision-ID: AD-025
Title: Quantity, Demand and Capacity Input Model
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-001, OCP-003, OCP-005, OCP-006, OCP-009, OCP-013, OCP-014, OCP-015, OCP-016, OCP-019, P-001
Applies-To: AB-037
---

# AD-025 — Quantity, Demand and Capacity Input Model

## 1. Decision

The Board selects **QC**, a Route C non-Concept quantitative input contract, and prepares OCP-020 `0.1.0 / Draft`. QC owns exact profile/unit bindings, snapshot-local quantity inputs and exact-unit addition. It deliberately does not compare demand with capacity, derive availability, or reserve or allocate a Resource.

AB-037 is Resolved as the selection of this bounded units/input/aggregation model. A positive capacity result remains gated future work. AB-025 remains Open: whole-Resource reservation can be assessed independently, while partial or quantitative reservation requires an accepted quantity input and its own object-form and OCP-016 G4 decision.

## 2. Exact baseline and anchor chain

The act starts from exact `main@24d8ec8a9d1fdfa58d3ebf1eb097c51cefa0f1af`, tree `e73aca41e966f1e98538b678c97626145c3acfdf`. It does not reuse a merged feature branch as a semantic baseline.

Each anchor was resolved at that commit, reverse-resolved to its path and SHA-256 checked over raw blob bytes.

| Input | Reverse-resolved path | Declared state at baseline | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-000 | `docs/000-operational-ontology/README.md` | `1.5.0 / Canonical`; named Concepts exclude all four candidates | `7da7d7aad6ba505603cfbfa98ff1349c84892720` | `3f76ae4b55f01ce388bd865330f386c3ec0a6f6416e1aaed522145df96cfb7d6` |
| OCP-003 | `docs/003-resource-concept/README.md` | `1.0.0 / Canonical`; quantity is not identity and needs a separate accepted contract | `71485bb337cfd59def2e0f1b18b474a7959bd30c` | `f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315` |
| OCP-004 | `docs/004-operation-concept/README.md` | `1.0.0 / Canonical`; capacity rules deferred to Constraint | `1ff548a1f213b574472a90a8b3cfe014f6c1ce11` | `9c9173d3a3dec044e2cae2eb8fd5b66d07a106318f497a973409fedf4677155b` |
| OCP-005 | `docs/005-assignment-concept/README.md` | `0.2.6 / Draft`, Assignment Concept `Accepted`; consumption quantity unresolved | `6e78d6d54d53260fb42f4ef67776e3cf8b11daa7` | `fd77fbdc47d1d436a95c95c6a211521d65dd5261633ccd2eee17f9a761fef3ba` |
| OCP-006 | `docs/006-constraint-concept/README.md` | `0.2.5 / Draft`, Constraint Concept `Accepted`; separate quantitative input required | `5d7404717e500c66c0c017263678ae0a1a405c7d` | `e0469604b1d8e6c2156c35e85017129eaca1fb929633a8be0287af4ef67a88aa` |
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; Route C and G4 gates current | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-019 | `docs/019-conflict-derivation-boundary/README.md` | `0.1.0 / Draft`; positive authority absent and quantity/capacity coupling forbidden | `092770b40541de5959c18b37664b179c7dcb7880` | `8689327a770eecccd40a7d43dd147659c24eb2e1dc0cd117dfe3e75114676bec` |
| P-001 | `patterns/P-001-identified-record-pattern.md` | `0.1.0 / Accepted`; binding only when invoked | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| architecture backlog | `backlog/architecture-backlog.md` | AB-025 and AB-037 both `Open` | `94c294116f7cf5301347270649fdb28cd915c1ae` | `c234017cac31c08fe44d320728ef53eede0328584d465fc37c55a403bce63810` |
| checker dispatch | `tools/ontology_checker/ocp_checker/__init__.py` | existing fixture classes only; no quantitative dispatch | `edf05a890f6aa05a3abdb4626f679a7e8b3c4f06` | `2bf6ba4dee5b441837ff9f0c1de1fda36ad3d05c9b93d5019e4b24f43e8c191e` |
| direct fixture-coverage test | `tools/ontology_checker/tests/test_manifest_fixture_coverage.py` | complete manifests require direct validation-ID fixture coverage | `1a8321cbd394db568302ceb9a2c80be5e42695a9` | `1168905eda069766da62a43008a9b2ab7ed6fb68ffa7083246c2e149cc63ce51` |

The anchors prove the exact inputs and checker baseline. They do not authorize a production measurement profile or a positive capacity decision.

## 3. Declared inventory rule

The inventory rule is fixed before examining candidates. After including OCP-000, OCP-001, OCP-002, OCP-016 and P-001 as governance/form controls, an artifact enters the semantic set when it does at least one of the following: owns Resource, Assignment or Constraint structure; names quantity, measure, demand, consumption, capacity, reservation or allocation; declares a consumer/profile that could use such input; or defines a result/non-implication boundary that a quantitative model could accidentally cross. Every current primary OCP is still listed so exclusion is explicit rather than inferred.

## 4. Complete current-artifact inventory

| Artifact | Rule result | Adjudication |
|---|---|---|
| OCP-000 | governance control | registry proves `Quantity`, `Reservation`, `Allocation` and `Capacity` are absent; it remains byte-identical |
| OCP-001 | governance control | admission and non-implication boundary applies; no semantic input supplied |
| OCP-002 | governance control | projection remains byte-identical because no Concept status changes |
| OCP-003 | included | §§5.2 and 13 separate Resource identity from amount/consumption/capacity/unit and name a separate accepted contract |
| OCP-004 | included | §21 defers capacity rules to Constraint; it neither owns units nor consumes a capacity result |
| OCP-005 | included | §§13–14.7 permit a separate post-Constraint model and leave quantity of consumption open; Draft is not an Accepted G4 consumer |
| OCP-006 | included | §14.2 requires a separate quantity/unit/aggregation/measurement input; §§22–23 defer consumption and partial reservation; Draft is not an Accepted G4 consumer |
| OCP-007 | excluded | Organization identity/relationship contract owns no qualifying quantitative field, consumer or unresolved relation |
| OCP-008 | excluded | Objective identity/statement contract owns no qualifying quantity, capacity or reservation surface |
| OCP-009 | included boundary | Capability examples do not turn capacity into Capability or supply a capacity-result consumer |
| OCP-010 | excluded | Event occurrence/observation contract owns no qualifying quantitative decision surface |
| OCP-011 | included boundary | assessment records demonstrate a governed result form but do not consume capacity or reservation evidence |
| OCP-012 | excluded | Capability claims own holder evidence, not resource quantity or capacity decisions |
| OCP-013 | included consumer check | Accepted interchangeability consumer explicitly excludes capacity/reservation/allocation authority |
| OCP-014 | included consumer check | Accepted requirement profile explicitly excludes capacity and reservation decisions |
| OCP-015 | included consumer check | Accepted workflow evidence does not reserve, allocate or decide capacity |
| OCP-016 | governance/form control | Route C and G4 applicability are decided before selecting the form |
| OCP-017 | included consumer check | Accepted lifecycle owner consumes completeness/authorization/terminal evidence, not a capacity result |
| OCP-018 | included boundary | Accepted authorization-source result cannot be reused as capacity or reservation authority |
| OCP-019 | included boundary | Draft negative Conflict boundary forbids quantity/capacity coupling and supplies no positive consumer |
| P-001 | form control | identified-record form is considered but not invoked by the selected inline/projection form |

The semantic candidates are therefore not selected by term frequency. Each included artifact either provides a governing boundary or tests whether a legitimate consumer already exists; each excluded artifact fails the declared rule by name.

## 5. G4 applicability before form choice

The gate is evaluated separately for each possible outcome:

| Outcome capability | G4? | Exact-baseline result |
|---|---|---|
| structural magnitude/unit binding | no | neutral input exactness creates no positive operational result |
| exact-unit sum of `demand` or `consumed` operands | no | arithmetic projection alone decides no sufficiency, permission or reservation |
| Assignment specialization that reserves or allocates | yes | no Accepted consumer owns the reservation/allocation result need and evaluator |
| Constraint specialization that declares capacity sufficient/exceeded | yes | OCP-006 is an upstream Draft definition, not a separate Accepted consumer |
| combined reservation/capacity decision | yes | the same consumer gap remains and the combination increases coupling |
| identified Reservation/Allocation record | yes for its operational positive meaning | no Accepted consumer, owner/evaluator or admitted object identity exists |

OCP-013, OCP-014, OCP-015 and OCP-017 are Accepted but explicitly own different outcomes. Their status cannot be transferred. Consequently the positive alternatives remain full comparison outcomes but are **currently impassable**, not silently discarded.

## 6. Outcome criteria

The following criteria are declared before scoring:

1. **C1 — demonstrated identity need:** introduce identity only when independent reference/history/ownership is required;
2. **C2 — non-overlap:** do not redefine Resource, Assignment or Constraint ownership;
3. **C3 — G4 honesty:** no positive-capable form may bypass its missing Accepted consumer;
4. **C4 — deterministic replay:** exact version, profile, snapshot, unit and operand binding without newest/list-order choice;
5. **C5 — fail-safe behavior:** malformed, ambiguous, stale or cross-bound evidence yields no total or positive decision;
6. **C6 — no authority by label or checker:** metadata, owner strings and executable code prove structure only;
7. **C7 — minimum migration:** existing governed artifacts remain valid without new required fields; and
8. **C8 — explicit non-implications:** quantity input cannot imply capacity, availability, reservation, Allocation, Assignment mutation, Risk, Conflict or authorization.

## 7. Outcome-fair comparison

| Outcome | Form and route | Strengths | Costs / gate result | Verdict |
|---|---|---|---|---|
| Q0 | no new contract | no new authority or migration | leaves explicit OCP-003/OCP-006 input gap and AB-037 unresolved | rejected |
| QF | fundamental `Quantity`/`Capacity` Concept, Route F | globally addressable identity | C1 unsupported; registry/graph change is a different act; conflates values with identity | rejected |
| QA | Assignment specialization | colocates reservation with participation | positive reservation/allocation requires G4 and no consumer exists; overlaps Assignment | blocked, not selected |
| QK | Constraint specialization | colocates later capacity evaluation | needs the separate input OCP-006 already demands; positive result is G4-blocked | blocked, not selected |
| **QC** | Route C non-Concept input plus neutral total | satisfies the shared upstream gap, exact replay and zero migration without positive authority | cannot itself answer capacity or reservation questions | **selected** |
| QE | Route E measurement envelope/profile | could support interoperability | no named interoperability consumer or production profile; would overclaim scope | rejected now |
| QR | identified Reservation/Allocation decision record | could preserve independent history and provenance | C1 and G4 evidence absent; object form and consumer must be separate future decisions | blocked, not selected |

The comparison gives blocked forms their intended operational benefit rather than penalizing them for being richer. Their failure is exact: the current baseline lacks the Accepted consumer and legitimate owner/evaluator required for that positive authority.

## 8. Selection and split sequencing

QC is the smallest lawful first act. OCP-020 defines exact input roles `demand | capacity_limit | consumed`, but aggregates only `demand | consumed`; it never compares either total to `capacity_limit`. This distinction is normative, not an implementation omission.

The sequence is deliberately split:

1. prepare and separately accept the quantitative input contract;
2. admit a concrete Accepted capacity-result consumer and exact positive rule before any sufficiency model;
3. adjudicate reservation independently: whole-Resource exclusivity may not need quantity, whereas partial/quantitative reservation depends on the accepted input and still requires its own G4/object-form decision.

Thus resolving AB-037 here does not resolve AB-025 and does not promise that one combined model will be selected later.

## 9. Selected Draft contract

OCP-020 `0.1.0 / Draft` defines:

- exact external measurement profiles with owner, unit and dimension references;
- canonical finite non-negative decimal lexemes;
- snapshot/context/profile/owner-bound inline quantitative inputs;
- exact reference resolution, current-evidence and cross-binding checks;
- exact-unit, same-dimension, same-role addition for `demand` or `consumed`;
- exact stored-result replay; and
- rejection of reservation, allocation, capacity-sufficiency and authority coupling.

The profile owner is attribution, not authenticated legitimacy. OCP-020 admits no production unit catalogue or conversion scheme.

## 10. Executable evidence and completeness

The act adds `quantitative-input-rules.yaml`, a dedicated validator/derivation module, eighteen synthetic fixtures and six focused tests. The manifest declares complete direct fixture coverage, and the existing generic guard requires every validation ID to occur in fixture expectations.

Positive fixtures prove exact demand and consumed totals and validate a non-aggregated `capacity_limit` beside exact demand operands. Material negatives separately cover malformed fixture/profile, unresolved and ambiguous profile, wrong owner, missing unit, non-canonical magnitude, cross-bound data, stale snapshot, duplicate operands, a selected `capacity_limit`, mixed units, heterogeneous dimensions, mismatched stored result and forbidden semantic coupling. Tests also prove that deleting the declared `capacity_limit` role fails, plus order invariance, immunity to valid unreferenced bindings, fail-closed negative derivation and manifest/code equality.

The repository floor grows from `212` to `218` tests and from `166` to `184` fixtures. Exact counts are verified in both PR and `main` checker contexts; a green count alone cannot grant production or positive-model authority.

## 11. Backlog disposition

- **AB-037 — Resolved:** AD-025 selects the bounded quantity/unit/input/aggregation direction and OCP-020 records it as Draft. Acceptance and a capacity predicate/result require separate acts.
- **AB-025 — Open:** no Reservation or Allocation Concept, record or semantic rule is selected.
- **AB-002 — Open:** no Order semantics are inferred.
- **AB-005 — Open:** no Risk taxonomy or derivation is introduced.
- **AB-018 — Open:** no Conflict authority is introduced.
- **AB-036 — Open:** no Policy, precedence, override or waiver semantics are introduced.

The registry, taxonomy, Concept graph and generated foundation map remain byte-identical. `Quantity`, `Reservation`, `Allocation`, `Capacity`, `Authority`, `Approval` and `Policy` are not introduced as Concepts. No P-001 invocation or `Review-After` field is added.

## 12. Version classification, migration, rollback and safety

AD-025 is `0.1.0` because it is the first version of this decision identity, and `Accepted` because it makes the Board's bounded outcome selection and resolves AB-037 rather than merely recording discovery. OCP-020 is `0.1.0` because it is a new contract identity, and remains `Draft` because this act prepares but does not perform the separately required acceptance act. The additive checker evidence does not change the version of any existing normative artifact.

There is no migration because OCP-020 is optional Draft evidence and no existing artifact gains required fields. Rollback removes AD-025, OCP-020, the manifest/module, eighteen fixtures, six tests and synchronized accounting, restoring the exact base semantics.

All fixtures are synthetic. They use abstract `SYNTH` references and decimal lexemes only, with no real quantities, unit names, capacities, coordinates, geometry, sectors, windows, callsigns, organization designators, personal data, credentials or material from any other project on this machine.

## 13. Exact-head gates

This act is the first of four gates. Merge requires exact-head Fable external review, Codex adjudication, green required CI on that unchanged head and fresh explicit Pavlo authorization naming it. Any content-changing commit invalidates earlier review, CI and authorization gates.

The mandate authorizes preparation and external review only. It does not authorize merge, OCP-020 acceptance, a production measurement profile, a capacity decision, reservation/allocation, Y10D, a normative `Review-After` act, YR or T6.
