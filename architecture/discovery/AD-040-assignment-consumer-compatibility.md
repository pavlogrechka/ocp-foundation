---
Decision-ID: AD-040
Title: Assignment Accepted-Consumer Compatibility Evidence
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-035, AD-037, AD-038, AD-039, OCP-005, OCP-016
Applies-To: AB-062, OCP-005 bounded stable-surface evidence
Review-After: Any Accepted consumer changes its OCP-005 dependency or consumed Assignment behavior, or a moving Assignment surface receives a separately authorized rule
---

# AD-040 — Assignment Accepted-Consumer Compatibility Evidence

## 1. Mandate and result

This act asks one evidence question: does every current Accepted consumer preserve its current behavior if the bounded stable surface discovered by AD-035 is frozen while the seven moving Assignment surfaces remain open?

The answer is **yes for all five current Accepted consumers**. Four consumers preserve negative exclusions and one preserves a positive derivation:

1. OCP-013 continues to return `indeterminate` when an interchangeability evaluation attempts Assignment mutation;
2. OCP-015 continues to turn otherwise positive coordination evidence into `indeterminate` when Assignment mutation is coupled to it;
3. OCP-017 continues to validate the exact current terminal-alignment case and retain `remains_effective_independently` while representative open moving-surface extensions are present but unconsumed;
4. OCP-020's controlled input remains valid while its Assignment-mutation probe is rejected with `QUANTITATIVE_INPUT_FORBIDDEN_COUPLING`; and
5. OCP-021's controlled request remains valid while its Assignment-mutation probe is rejected with the exact request-invalid and forbidden-coupling error set.

Therefore only `ACCEPTED_CONSUMER_COMPATIBILITY_UNPROVEN` is removed from the current AD-035 projection. `AMENDMENT_MODEL_ABSENT`, `TEMPORAL_MODEL_UNRESOLVED` and `PARTIAL_SCOPE_IDENTITY_UNRESOLVED` remain blocking whole-document freeze. No Assignment question closes, Assignment is not selected, no promotion cycle begins and freeze is not declared reachable.

## 2. Criterion declared before enumeration

A current Accepted consumer is any primary OCP document whose live frontmatter has `Status: Accepted` and whose exact `Depends-On` set contains `OCP-005`. That live query yields exactly OCP-013, OCP-015, OCP-017, OCP-020 and OCP-021. OCP-006 remains a direct Draft consumer and is outside this compatibility blocker.

Preservation requires both conditions below:

1. every textually declared element the consumer takes from Assignment maps to one of AD-035's six bounded stable candidates; and
2. a predeclared existing fixture reproduces the consumer's exact current result without adding a field, rule, transition or profile to any contract.

For negative consumers, preservation means Assignment coupling remains fail-safe and non-permissive. For the positive consumer, preservation means the exact current assignment-alignment case remains valid with the same terminal disposition. A moving surface may remain open; the act must neither freeze it nor make its unknown future form part of the proof.

## 3. Gate-first check

The evidence form does not require OCP-016 G4. It adds a replay witness and repository validator, not a positive-capable operational rule, result or profile.

Removing the evidence-debt blocker also does not require G4: the removal follows only after replaying behavior already owned by five Accepted consumers and adds no Assignment behavior. Were any replay to require a new field or rule, that consumer would be unproven and the blocker would remain. The act does not use its own witness as an Accepted consumer and does not activate anything recursively.

## 4. Per-consumer derivation

### 4.1 OCP-013 — negative exclusion

OCP-013 consumes the requirement to retain every exclusion of availability, authorization, ranking, selection, replacement and Assignment mutation. Those obligations lie within AD-035's non-authority and supersession-identity boundaries. The existing `assignment_mutation_is_rejected` case returns `indeterminate`; the positive control remains `positive`. No moving Assignment surface is consumed.

### 4.2 OCP-015 — negative exclusion

OCP-015 consumes preservation of Resource and Assignment identity and its explicit refusal to alter either. Those obligations lie within the identity-reference and non-authority boundaries. The existing positive coordination snapshot returns `positive`; the same snapshot with synthetic `assignment_mutation` returns `indeterminate`. No moving Assignment surface is consumed.

### 4.3 OCP-017 — positive derivation

OCP-017 is the asymmetric case. It consumes exact `operation_ref`, the current Assignment transition/effectivity truth exposed by `assignment_effective_at`, structural role/provenance needed by the Assignment validator and the rule that terminal alignment never edits Assignment history. Those elements lie inside the identity-reference, transition-history, structural-role/provenance and executable Assignment candidates.

The existing valid completed-operation fixture exact-enumerates `ASG-Q3I-ALPHA`, evaluates it at the terminal instant and requires `remains_effective_independently`. The control validates. A copy carrying synthetic amendment, additional-interval, role-governance and partial-scope extension values also validates with the same disposition. This does **not** approve those extension forms: it proves only that OCP-017's current derivation does not consume or decide the moving surfaces. Q2/Q3/Q9/Q4/Q5 and their blockers remain open where applicable.

### 4.4 OCP-020 — negative exclusion

OCP-020 consumes the non-authority boundary: it cannot create, amend, activate, suspend or terminate Assignment and existing Assignment artifacts do not require an OCP-020 binding. A controlled copy of the existing fixture, with its native forbidden key removed and exact stored total supplied, is valid. A separate copy replaces the native key with `assignment_mutation` and yields exactly `QUANTITATIVE_INPUT_FORBIDDEN_COUPLING`. No moving Assignment surface is consumed.

### 4.5 OCP-021 — negative exclusion

OCP-021 consumes opaque Assignment identity references whose truth remains with OCP-005 and explicitly cannot create, block, cancel, supersede or mutate Assignment. Those obligations lie within the identity-reference, non-authority and supersession-identity boundaries. Removing the mutation coupling and supplying the derived stored boundary result makes the controlled request valid; the unchanged assignment-mutation fixture reproduces the exact request-invalid plus forbidden-coupling error set. No moving Assignment surface is consumed.

## 5. Outcome-fair comparison

Every outcome is compared on the same axes: current-consumer completeness, stable/moving separation, executable replay, G4 legality, migration and rollback.

| Outcome | Consumer evidence | G4 / migration | Disposition |
|---|---|---|---|
| C0 — remove blocker from prose only | no executable preservation | would leave the original debt intact | rejected |
| C1 — prove only the four consumers recorded by the old blocker | omits newly Accepted OCP-021 | current inventory would be false | rejected |
| C2 — treat every consumer as a negative exclusion | erases OCP-017's positive `assignment_effective_at` dependency | conflates distinct proof classes | rejected |
| C3 — freeze moving surfaces to make proof easy | changes Assignment semantics and questions | positive G4 work, unauthorized | rejected |
| C4 — replay five consumers by class and remove only the evidence blocker | complete inventory, exact fixture results, moving surfaces remain open | no semantic migration | selected discovery result |

The selected discovery result is not an Assignment selection or freeze recommendation.

## 6. Executable witness and projection

`architecture/assignment-consumer-compatibility.yaml` records the predeclared criterion, five independently classified consumers, their exact text tokens, stable-surface membership, any open moving-surface exposure, fixture, control and probe result. Its validator derives the Accepted consumer set from live metadata rather than trusting the map.

The checker fails if:

- any Accepted `Depends-On: OCP-005` consumer is added, removed or changes status;
- a consumed text token changes;
- a control or probe changes result;
- one of the six stable or seven moving surfaces disappears;
- the removed compatibility blocker returns;
- any of the three semantic blockers disappears;
- any new promotion cycle starts; or
- a declared anchor, gate, result or defensive value changes.

The required `test_every_defensive_value_is_individually_fixture_and_mutation_live` mutates every declared defensive value individually. Separate mutation tests alter each consumer fixture and prove the corresponding replay fails. All five existing consumer fixtures remain byte-identical in the repository.

AD-035 remains a byte-identical historical discovery record. Its YAML witness is explicitly a current projection: only the now-proven compatibility blocker is removed; its `baseline`, `baseline_evidence_objects`, questions, consumers, candidates and moving surfaces remain untouched.

## 7. Exact baseline and full-chain anchors

The exact baseline is `main@747d5aa2e71bd87c4e024d62f80d8cfa122d8279`, tree `4c9f52685c5891179a3242263d00c101127a90de`. Every row below was resolved at that commit, reverse-resolved from blob through `git ls-tree -r` to the declared path, checked for its stated role/status and SHA-256 hashed from those same bytes. Every declared path matched its reverse resolution.

| Evidence | Reverse-resolved path / declared state | Git blob | SHA-256 |
|---|---|---|---|
| OCP-005 | `docs/005-assignment-concept/README.md`; `0.2.8 / Draft`, Assignment `Accepted` | `6e6c00e723b15a348e7610d4ca5a1ae23526c52b` | `a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065` |
| OCP-013 | `docs/013-resource-interchangeability/README.md`; `0.2.0 / Accepted` | `658a291b4c3b9a0229aba09d485c1137723fe70b` | `a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74` |
| OCP-015 | `docs/015-coordination-workflow/README.md`; `0.2.0 / Accepted` | `ea60634e54faedabb8c5e08b036030c2f0e4e20b` | `6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d` |
| OCP-017 | `docs/017-operation-lifecycle/README.md`; `0.2.0 / Accepted` | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| OCP-020 | `docs/020-quantitative-constraint-input/README.md`; `0.2.0 / Accepted` | `0e1e7d0947ab3c7d1c0355258651179f618636a2` | `1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c` |
| OCP-021 | `docs/021-reservation-allocation-boundary/README.md`; `0.2.0 / Accepted` | `bae4ac5de36b5d2a2d0c9182e5f1208c14593a35` | `6289378b6d9f785e24abca39dbd6d3da550ccb21a43b3d1632e8c5de4894a89e` |
| OCP-016 | `docs/016-core-boundary/README.md`; `1.0.0 / Canonical`, G4 | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| AD-035 | `architecture/discovery/AD-035-assignment-stable-surface.md`; `0.1.0 / Discovery` | `81ed1c4981c97a0d0a4511e4492741bf5382ce05` | `85a10e965faaa7ba65484efe08e985b7a04bf06712553c914673d65faf1df805` |
| AD-035 current witness | `architecture/assignment-stable-surface.yaml`; schema 1, compatibility blocker present on baseline | `ae8a2ff5bf493182d4cd51e897afe736ed36cd5d` | `617af7d0598bbdd756fd890a6dcd38f0324d6c481abf2f72c5a871c439a6bcc8` |
| Promotion gate | `architecture/foundation-promotion-gate.yaml`; schema 5, `EVENT_T6` complete, no active cycle | `78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1` | `ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd` |
| OCP-013 fixture | `tools/ontology_checker/fixtures/interchangeability/mandatory-counterexamples.yaml`; valid mandatory counterexamples | `3437e78bbff39a3ac977755ebe9e7af849aed60e` | `6815557ac57854ba3dfa1214462818132595b13cd0594b220cef8a649e7eca66` |
| OCP-015 fixture | `tools/ontology_checker/fixtures/coordination_workflow/mandatory-cases.yaml`; valid mandatory cases | `6ce9ce33cc648ce6825fe8e9009caffdc5a53768` | `16fdfbe2943760435a8030b8558290640b8dbf4abe882ee1cc985821015e2162` |
| OCP-017 fixture | `tools/ontology_checker/fixtures/operation_lifecycle/valid-q3i-completed.yaml`; valid completed terminal alignment | `c85a65e217c7d0ecdbabf8e9adf76f1a88a7faff` | `901ce32b9af2dcf9e664b565c7a6a4fc8919c7329d40d666a38a3115d0fb5672` |
| OCP-020 fixture | `tools/ontology_checker/fixtures/quantitative_input/invalid-forbidden-coupling.yaml`; forbidden-coupling case | `ce9e2a55acb574b0d542e29764ef5ef3f6b43834` | `2ec5f9c2c2893c10cfd14fb25531a1f374d29a166b5f0696a5c374f7a481007e` |
| OCP-021 fixture | `tools/ontology_checker/fixtures/reservation_boundary/invalid-forbidden-coupling.yaml`; Assignment-mutation forbidden coupling | `580df6de3974854d52e3d56df41d16b4f274895c` | `6d66155d4c438304449242def419c1f40078ddbcbe0898c01faeed63c9d24135` |

Hashes identify evidence, not authority. No duplicate-content path substitutes for a declared primary. The executable anchor test repeats blob-to-path reverse resolution and byte hashing for all fifteen objects.

## 8. Version, accounting, migration and rollback

AD-040 begins at `0.1.0 / Discovery` because it introduces a new evidence record and no semantic decision. `assignment-consumer-compatibility.yaml` begins at schema 1 because it introduces a new evidence language. `assignment-stable-surface.yaml` remains schema 1: one current blocker entry disappears without changing the shape or interpretation of the witness. OCP-005 and all five consumers retain their versions because no contract bytes change. README, roadmap, AB-062 and checker documentation are unversioned current projections.

The exact base has 331 unit tests and 274 synthetic fixtures. Eight new governance tests produce 339 tests; fixture count remains 274. Counts are checked by the existing machine-derived accounting guard.

No Assignment, consumer data, reference, lifecycle, role, interval, scope, schema or fixture migration exists. Rollback removes AD-040, its witness/module/tests/check integration and accounting entries, and restores the compatibility blocker in the current AD-035 projection as one reviewed unit. It cannot remove any semantic blocker or close any question.

## 9. Protected state and lawful continuation

OCP-000, OCP-002, every OCP body/version/status, every Concept status, graph edge, P-001 byte, consumer fixture, reviewed snapshot, historical `baseline_*` value and promotion-gate byte remain unchanged. OCP-005 remains `0.2.8 / Draft`; Assignment remains `Accepted`. OCP-006 remains Draft/Accepted. The gate retains completed `EVENT_T6` and `active_cycle_id: null`.

No candidate is selected, no cycle begins, no promotion or canonicalization becomes reachable, no T7 opens and no later act is authorized. The remaining lawful work is still semantic: Q2, Q3/Q9 and Q5 require separately mandated positive proposals with concrete Accepted consumer need and complete OCP-016 G4 bindings. AD-040 supplies no such need or authority.

## 10. Exact-head gates

AD-040 becomes repository evidence only after Fable reviews one exact unchanged head, Codex adjudicates that review, CI is green on the same head, Pavlo freshly authorizes that exact head and the PR is squash-merged. Any head change resets all four gates.
