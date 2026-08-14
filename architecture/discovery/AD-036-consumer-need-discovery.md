---
Decision-ID: AD-036
Title: Positive Consumer-Need Discovery
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-022, AD-025, AD-026, AD-027, AD-030, AD-035, OCP-001, OCP-016
Applies-To: OCP-016 G4 consumer-need boundary
Review-After: A current Accepted or Canonical consumer states a protected obligation that cannot complete without one exact positive result
---

# AD-036 — Positive Consumer-Need Discovery

## 1. One question and exact result

The act asks one question on exact `main@f64b3a23419092649cfb4059d4853eabd93fbbc2`:

> Does any current Accepted or Canonical repository document state an unmet need for a positive result, and if so where?

The complete status-derived inventory and the predeclared test in §3 yield a negative answer:

> **No current Accepted or Canonical document states an unmet positive consumer need.**

This does not say that positive models are impossible or useless. It says that this exact tree supplies no qualifying consumer obligation. The result activates no model, profile, Concept, rule, status, graph edge, promotion cycle, Assignment remediation or later act.

## 2. G4 before form

The OCP-016 G4 question is answered before selecting the evidence form. This act creates a discovery map and a repository drift validator. Neither emits an operational result, activates a positive-capable rule or profile, nor becomes a consumer contract. G4 therefore does not apply to the discovery output, and the act cannot recursively manufacture the consumer it is looking for.

A form that created a positive Conflict, capacity, reservation/allocation, precedence/override/waiver, Order or Assignment-remediation result would require the missing G4 consumer. That form is excluded rather than compared as an output.

## 3. Criterion declared before the scan

The inventory uses current primary frontmatter, not prose labels. A lifecycle document or Pattern enters when its current primary has `Status: Accepted` or `Status: Canonical`. An Architecture Decision enters the separately identified governance-act inventory when its current frontmatter is `Accepted`. Draft primaries, reviewed-contract snapshots and baseline objects are not current eligible consumers.

A statement is an **unmet positive consumer need** only if all three conditions hold together:

1. it is a current normative statement of the eligible artifact rather than historical review/baseline evidence;
2. it names an exact positive result rather than only an absent owner, open question or later route; and
3. the artifact cannot complete one of its own current obligations without that result.

The following fail the test:

- a negative boundary already sufficient for the current contract;
- a future, optional, open or separately governed mention with no current dependency;
- a positive output already defined and executable by the artifact;
- a governance act that records a gate but is not an operational consumer contract; and
- a historical baseline, accepted-act account or immutable reviewed snapshot.

Usefulness, symmetry, architectural completeness and “would be convenient” are not evidence of need.

## 4. Complete status-derived scope

The live scan contains **49** eligible artifacts: **19** lifecycle documents/Pattern and **30** Accepted governance acts.

### 4.1 Current lifecycle documents and Pattern

| Status | Exact set |
|---|---|
| Canonical (10) | OCP-000, OCP-001, OCP-002, OCP-003, OCP-004, OCP-007, OCP-008, OCP-009, OCP-010, OCP-016 |
| Accepted OCP (8) | OCP-011, OCP-012, OCP-013, OCP-014, OCP-015, OCP-017, OCP-018, OCP-020 |
| Accepted Pattern (1) | P-001 |

The five current Draft OCP primaries—OCP-005, OCP-006, OCP-019, OCP-021 and OCP-022—are deliberately excluded even where their Concepts are Accepted or their negative boundaries are executable. A Draft defining document cannot self-supply the Accepted consumer required by G4.

### 4.2 Accepted governance acts

The separate governance inventory is AD-002–AD-022 with absent IDs preserved as absent, plus AD-025–AD-030 and AD-032–AD-034: exactly the 30 entries serialized in `architecture/consumer-need-discovery.yaml`. Each is scanned because its accepted prose may contain a claim about consumers, but `Owner: Architecture Board` and accepted decision status do not turn it into the operational consumer or legitimate evaluator demanded by G4.

## 5. Candidate mentions adjudicated individually

The scan does find positive-looking text. Each occurrence below is assessed under the same §3 test.

| Document and exact token | Named result | Can the document perform its current obligation without a new result? | Disposition |
|---|---|---:|---|
| OCP-003 §13: `окремий accepted consumable/measurement contract` | quantitative input | yes | OCP-020 now supplies the accepted neutral input; this is not an unmet positive predicate |
| OCP-009 §12: `Operation requirement representation ... мають окремих normative owners` | Operation-requirement contract | yes | ownership separation, not a current dependency of Capability identity |
| OCP-010 §17: `A future positive relation requires a separately mandated owner act` | Operation↔Event relation | yes | explicitly future and excluded from Canonical Event semantics |
| OCP-013 §4: `A positive result remains eligibility evidence only` | contextual interchangeability | yes | the positive result is already defined and executable |
| OCP-014 §3: `Actor authentication and authorization require a separate future contract` | actor authentication/authorization | yes | explicitly outside the accepted contextual-requirement profile |
| OCP-015 §6: `AB-059 is the next normative cycle named by this acceptance act` | visibility/agreement semantics | yes | deferred next cycle; the accepted proposal/response evidence contract is complete without it |
| OCP-016 §5: `G4 consumer activation remains binding for positive-capable rules, results and profiles` | none | yes | an admission rule, not a consumer need |
| OCP-017 §9: `A concrete domain must govern those responsibilities separately` | production-domain source legitimacy | yes | production responsibility is deferred; the accepted evidence-envelope contract already performs its bounded function |
| OCP-018 §30: `Any future production profile must name its own legitimate owner` | production source profile | yes | future production adoption, not an Accepted prerequisite |
| OCP-020 §3: `The exact baseline has no Accepted consumer that owns such a result need` | capacity/reservation result | yes | explicit negative boundary; neutral exact-unit input remains complete |

No row meets condition 3 with `false`. Therefore the qualifying `unmet_positive_needs` set is empty.

## 6. Existing positive outputs are not unmet needs

The negative result is not obtained by treating every positive result as suspect. Six current Accepted contracts already define bounded positive-capable behavior:

| Contract | Existing result |
|---|---|
| OCP-011 | exact criterion-bound outcome conclusion |
| OCP-012 | activated evidence-backed Capability claim projection |
| OCP-013 | contextual directional interchangeability `positive` |
| OCP-015 | attributable confirmation `positive` projection |
| OCP-017 | effective/passed lifecycle evidence binding |
| OCP-018 | effective `authorize → accepted` source result |

Their current rules, manifests, tests and fixtures already govern those results. An established result is not an unmet need for a new result, and its existence cannot be transferred to a different subject.

## 7. The repeated negative gates remain evidence, not consumers

The five accepted negative-boundary acts are reproduced exactly:

| Subject | Exact accepted absence |
|---|---|
| Conflict / AD-022 | every positive option lacks a concrete Accepted consumer |
| capacity / AD-025 | no positive form may bypass its missing Accepted consumer |
| reservation/allocation / AD-026 | no Accepted artifact owns the protected quantitative result |
| precedence/override/waiver / AD-027 | no Accepted consumer need, positive rule or legitimate activation owner exists |
| Order / AD-030 | the generic authorization consumer does not state an Order-specific need |

Those acts constrain later proposals. They do not themselves become the missing consumers, and their `Accepted` status cannot be used as self-supply.

## 8. Baseline anchors

Each anchor was resolved as `baseline:path → blob`, reverse-resolved with `git ls-tree -r`, checked against the claimed path and SHA-256 recomputed from raw blob bytes.

| Path | Blob | SHA-256 |
|---|---|---|
| `docs/003-resource-concept/README.md` | `71485bb337cfd59def2e0f1b18b474a7959bd30c` | `f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315` |
| `docs/009-capability-concept/README.md` | `31163eacb0ca2a78b17b9d2466d99ef0c8b2d272` | `29362c815cb14f07bfd06775d1398498a27ace5ee5a4acaafde0eb39e902152a` |
| `docs/010-event-concept/README.md` | `a9de19a0873a6616d4c77614acf48d17e1b06bad` | `51023373a39056ac70f80d97cea3c529938f82a01c9a1ee1f83410d34ae4f3ed` |
| `docs/011-outcome-assessment-record/README.md` | `ff2608a372c6305db4c290f05c15e961ca96e6f6` | `1fb08e18fab560e671b468585d699a7d70bd55ed5be674315cb780a48bc70cc5` |
| `docs/012-capability-claim-record/README.md` | `cd2df0f1961b6d03eea0db66c8fdfce1f97cb235` | `d4d5b4441cf2d1f7fea2dae572fcfa60f22b0ebce0e23ae6a86f71d9f4edd122` |
| `docs/013-resource-interchangeability/README.md` | `658a291b4c3b9a0229aba09d485c1137723fe70b` | `a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74` |
| `docs/014-coordination-profile/README.md` | `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` |
| `docs/015-coordination-workflow/README.md` | `ea60634e54faedabb8c5e08b036030c2f0e4e20b` | `6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d` |
| `docs/016-core-boundary/README.md` | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| `docs/017-operation-lifecycle/README.md` | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| `docs/018-operation-authorization-source/README.md` | `dc3148869f47af2bb27eb2fa74a188136d5fb568` | `e105e9c230277b6865721192ef4044ee77d9bfbff73505d164d7760c8ac31779` |
| `docs/020-quantitative-constraint-input/README.md` | `0e1e7d0947ab3c7d1c0355258651179f618636a2` | `1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c` |
| `architecture/discovery/AD-022-conflict-derivation-boundary.md` | `daba3472caaa650c41231437bddba1a70d895230` | `a52f0fb9cab2bdd32f23e5f2c529c4c76db1ffd8efe1ae6046fc3dda23747d54` |
| `architecture/discovery/AD-025-quantitative-constraint-input.md` | `cd4e320be2db6398d758c6fa3ae49e0a0f520df5` | `dae3ee9ea8ffbe0fb62df127fa53920705d59f50ec793cb41cb6ca3c10642d46` |
| `architecture/discovery/AD-026-reservation-allocation-boundary.md` | `ad109d1003af32a019e6b525b4552db2c6e323b2` | `e258d714d242a5065b23c296a413a6d0d8c52e72d967b42798153888f6d872bd` |
| `architecture/discovery/AD-027-constraint-interaction-boundaries.md` | `fa49556df4f06aa039df23d9cc244587411b2d5e` | `8d62725e4f8b1513c85fd24d59017215da94ddef8cda5244f300a6f25a0ee442` |
| `architecture/discovery/AD-030-order-authorization-boundary.md` | `01b7a6f01065b57130f8c0572242d683bcd22108` | `6ab90174bc1db423f403ac28a87d9eb0e1f84a7685cce881d94596a2fb9989bf` |

## 9. Executable evidence and falsification

`architecture/consumer-need-discovery.yaml` records the 49-artifact status inventory, ten candidate mentions, six established positive outputs, five prior negative gates, the empty qualifying result and forbidden outcomes. The validator independently derives every eligible current primary and Accepted AD from live frontmatter, verifies every exact token and rejects status, inventory, criterion, result, gate-history, anchor or promotion-state drift.

The focused suite includes `test_every_defensive_value_is_individually_fixture_and_mutation_live`. Every defensive set member and every scalar in the candidate, existing-output, gate-history and anchor dictionaries is removed or mutated individually and must make validation fail. Additional mutations prove:

- one Accepted primary changed to Draft changes the scope;
- one Accepted governance act changed to Discovery changes the scope;
- deleting any candidate, positive-output or gate-history token fails;
- inserting a synthetic unmet need or declaring G4 applicable fails; and
- starting an Assignment promotion cycle fails.

No fixture is added: this is governance discovery over repository artifacts, not a new operational record behavior. The fixture baseline remains 274.

## 10. Version, rollback, safety and gates

AD-036 begins at `0.1.0 / Discovery`. It is the first complete current-status consumer-need audit and selects no semantic outcome, so neither Accepted nor a revision of an existing OCP is justified. The executable map/module are new governance evidence, not an OCP semantic version change.

Rollback removes AD-036, its map, validator, tests and descriptive accounting. It changes no operational contract or stored data because none was introduced. All evidence is repository metadata or synthetic mutation; no geometry, operational window, unit identifier, personal data, credential or material from another project is present.

AB-018 and AB-005 remain Open. The promotion gate remains schema 5 with only completed `EVENT_T6` and `active_cycle_id: null`. OCP-005/OCP-006 remain Draft with Accepted Concepts; no status, registry, taxonomy, graph, P-001 byte, fixture, reviewed snapshot, baseline witness or AB status changes.

Merge requires exact-head Fable review, Codex adjudication, green required CI and fresh explicit Pavlo authorization naming the unchanged head. Preparation and review do not authorize activation, remediation, selection, promotion or a next act.
