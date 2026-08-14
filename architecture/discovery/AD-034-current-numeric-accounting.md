---
Decision-ID: AD-034
Title: Current Numeric Accounting Hygiene
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-016, AD-028, AD-029, AD-032, AD-033
Applies-To: Repository current-state accounting only
---

# AD-034 — Current Numeric Accounting Hygiene

## 1. Decision, gate-first result and boundary

The Architecture Board authorized one hygiene act on exact `main@dfa783c7ed1609f8f4347b333aa532b3b55f6f42`: repair stale current numeric accounting and make the mechanically derivable subset follow live repository sources without changing any lifecycle state.

Gate-first is resolved before choosing the form. This act creates no positive-capable operational rule, result, source profile or consumer activation, so OCP-016 G4 does not apply and no Accepted activation consumer is required. The selected form is an AD-owned finite accounting declaration plus an advisory repository checker. It introduces no domain semantics and does not displace OCP-000, OCP-001 or OCP-002 authority.

## 2. Exact base and full-chain anchors

The exact base tree is `3a06def8379c5a094b147f41db314d137811b420`. Every row was resolved by Git blob, reverse-resolved through `git ls-tree -r`, checked for the stated base condition inside the object and SHA-256 hashed over raw blob bytes.

| Input | Reverse-resolved path | Base state | Git blob | SHA-256 |
|---|---|---|---|---|
| repository README | `README.md` | 293 tests / 274 fixtures; stale current `5 Canonical / 3 Accepted` Concept prose | `aa46c0ae1b3881572a5294a6476f574aac83284e` | `3776028e40c084b166fd889b713f04bf0f1bfa5a912c9f5b5a33fc0e33c74232` |
| Concept registry | `docs/000-operational-ontology/README.md` | six Canonical / two Accepted current Concept rows; historical T0 accounting retained | `d09841be088ac9c1fffed42e4b8874094cba299c` | `120071c48f398d59b283ff71c8bb18fd0467f5e87e90dcef43ea8ad3f1af3dbe` |
| Concept taxonomy | `docs/002-concept-taxonomy/README.md` | exact current status projection; historical T3 accounting retained | `295512bdfaffd679ae021d0876072cdbcb2be75e` | `d49e9f896508d246994fd954174f04c69e0b4d32dfacc1dd612659263118df77` |
| accepted-snapshot map | `architecture/accepted-document-snapshot-map.yaml` | eight current Accepted entries plus retained OCP-016 evidence | `1918a4d400f475f5035622ee1571dec24cc4e435` | `5461ace22d4dc82622710b189a4cb11c82f2627bdaf0120ecad7c9204c8996ca` |
| promotion gate | `architecture/foundation-promotion-gate.yaml` | schema 5; one completed Event cycle and no active cycle | `78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1` | `ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd` |
| P-001 | `patterns/P-001-identified-record-pattern.md` | `0.1.0 / Accepted`; immutable historical ledger | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| checker entry point | `tools/ontology_checker/check.py` | no current numeric-accounting validation | `d92d99b3b2b7d386f24d43ba5d3b735028382b08` | `c2fe24d25d69c6a8b94eb8aa91cacc4c8d780b1ddae7d96f7f8ab70a69c5321c` |
| artifact governance | `tools/ontology_checker/ocp_checker/artifact_governance.py` | validates statuses and versions, not prose counts | `021b0c2da482d1d6b09cfd8f76d9da2feeecb031` | `3bd03d57e574bffd28eb0630b45afdd424c0eb06d3a37600aa62acfaac6feb13` |
| checker guide | `tools/ontology_checker/README.md` | no numeric-accounting rule | `f0580458f9626a2bd8e30c4646ae514ec2d3bcb7` | `3f3dc479e34d2a6e253219acd289a590863b61761693e1536d3fe5e8ced3a0ae` |
| roadmap | `backlog/roadmap.md` | non-formula readiness percentages; stale current T6–T10 range | `e6debd423e3b4bcb5ff8146946daf5a91c79c749` | `f6802841a9ac655f358606b4cda886aa226aea80414878db8e50fdce4117d1a2` |
| AB-062 accounting | `backlog/architecture-backlog.md` | Planned; completed Event cycle, next cycle absent | `e5ca6847c5ced9bb5b6154560df00900ed16f66e` | `704aaa734e731acd657cf75f45c82bf49ae085c1956ad1460d4f9546e7717de4` |

Anchors prove reviewed inputs. They do not create a status, candidate, cycle or permission.

## 3. Predeclared numeric-accounting criterion

The criterion was fixed before the repository scan.

1. A numeric-accounting assertion contains an explicit digit or cardinal word that quantifies a finite repository population or a status/category partition: documents, Concepts, fixtures, tests, reviewed snapshots, Pattern invokers, carriers, fields, questions, candidates, steps or cycles. Versions, identifiers, section numbers, rule suffixes, list ordinals, hashes and example payload values are not counts.
2. A claim is **current** when it describes the repository now, uses current/present-tense language, or appears in a central current accounting/roadmap surface without an exact historical base.
3. A claim is **historical** when it is explicitly bound to a commit, date or version, or describes the measured result of one named completed act on its own reviewed tree. Historical counts remain byte-unchanged even when the live tree later differs.
4. A percentage explicitly labelled non-normative and lacking a repository formula is a Board judgement, not a derivable count. It is registered, not reverse-engineered.
5. Machine enforcement is claimed only for the finite central current line declared by `architecture/current-numeric-accounting.yaml`; arbitrary natural-language number extraction is not claimed.

## 4. Complete adjudication of the bounded scan

| Carrier/class | Base assertion | Classification and result |
|---|---|---|
| `README.md` current suite line | 274 fixtures / 293 tests | current, correct on the base; moved into the derived claim and updated only by real added tests |
| `README.md` current readiness line | five Canonical / three Accepted Concepts | current and stale; repaired to the live six/two distribution through the derived claim |
| central current primary-OCP distribution | absent | added as 23 total: ten Canonical, eight Accepted, five Draft, derived from every primary frontmatter |
| accepted-snapshot evidence | absent from central accounting | added as nine: eight current Accepted plus one retained historical OCP-016 entry, derived from the governed map |
| P-001 current invokers | absent from central accounting | added as nine, derived only from primary structured `Uses-Patterns` metadata |
| `README.md` / roadmap current `T6–T10` remainder | includes already completed Event T6 | current and stale; repaired to `T7–T10` without opening or completing any milestone |
| README and roadmap `≈72%`; roadmap 100/93/33/77% | non-normative readiness estimates | current Board judgements without a normative formula; registered outside machine derivation and unchanged |
| README AD-028/029/031/032/033 ledger counts | exact result of each named act | historical act-local accounting; unchanged |
| README T3 six Pattern carriers and later time-anchored three snapshots | T3/P-001 acceptance history | historical even though live `Uses-Patterns` now yields nine invokers; unchanged |
| OCP-000 T0 eight Accepted Concepts; OCP-002 T3 eight Accepted projections | explicitly scoped to their lifecycle acts | historical and now numerically different from the live six/two split; unchanged |
| OCP-009 first, OCP-008 second and OCP-003 third Canonical Concept narratives | named completed T4 acts | historical sequence evidence; unchanged |
| AD-016 baseline tables and test/fixture totals | each names an exact base or completed revision | historical evidence, including numbers that differ from the current tree; unchanged |
| AD-033 six/two and 293/274 result | named multicycle act result | historical and still equal to its own head; unchanged |

The scan also sees structured schema versions, rule identifiers, hashes and synthetic example values. Criterion item 1 excludes them because they are not prose repository-population accounting. Current semantic lists that name their members without a numeric claim remain governed by their existing owner and are not silently converted into counters.

## 5. Mechanical contract

`architecture/current-numeric-accounting.yaml` contains no copied expected numbers. It declares one carrier, one exact prose format and five derivation families:

1. every primary OCP `Status` from live frontmatter;
2. every defining `Concept-Status` from live frontmatter;
3. current and retained reviewed-snapshot entries from the governed snapshot map;
4. exact `P-001@0.1.0` primary invocations from structured `Uses-Patterns`;
5. fixture YAML files and parsed `test_*` methods in the executable tree.

The validator derives each number, verifies that all observed document/Concept/snapshot categories are represented, renders the exact central README line and requires it exactly once. It does not read an expected count from the map and then congratulate that same map. A future status change therefore changes the derived value before prose can pass.

## 6. Mutation proof and coverage boundary

The exact test named `test_every_defensive_value_is_individually_fixture_and_mutation_live` removes every declared map key, metric ID, document-status label, Concept-status label and snapshot basis one at a time; every removal fails. Separate isolated-tree attacks prove:

- changing `Status` in each of all 23 primary OCP documents fails until the current claim changes;
- changing `Concept-Status` in each of all eight defining OCP documents fails until the current claim changes;
- removing one snapshot entry, one structured P-001 invocation, one fixture or one parsed test method fails;
- mutating each of the thirteen rendered numeric occurrences independently fails;
- the unmodified repository derives 23 OCP documents (10/8/5), eight Concepts (6/2), nine snapshots (8+1), nine P-001 invokers, 274 fixtures and 299 tests.

This is complete for the declared central claim, not for arbitrary prose. Non-formula readiness percentages remain registered debt by design; enforcing them would invent semantics the repository does not have.

## 7. Version classification, accounting and migration

AD-034 is `0.1.0 / Accepted`, its first governance-hygiene decision. The accounting map is schema 1 because it is a new machine-readable form. The checker module and guide gain a compatible repository check. README, roadmap and AB-062 are unversioned current accounting surfaces. No OCP, Pattern, registry, taxonomy or lifecycle document changes version or body.

The exact base reproduces 293 unit tests and 274 synthetic fixtures. Six real governance tests produce 299 tests; fixtures remain 274. Data, schema, record and reference migration are none. Rollback is atomic across AD-034, the map, checker integration/tests and the central accounting prose; rolling back only prose or only the derivation would recreate drift.

## 8. Explicit non-effects, safety and gates

No `Status`, `Concept-Status` or AB status changes. OCP-005 remains `0.2.8 / Draft`, OCP-006 `0.3.2 / Draft`, OCP-010 `1.0.1 / Canonical`; Assignment and Constraint remain Accepted, Event remains Canonical. OCP-000/OCP-002 content, Concept graph/map, P-001 bytes, all fixtures, reviewed snapshots, historical `baseline_*` objects and promotion-gate state remain byte-identical. `EVENT_T6` is the only completed cycle and `active_cycle_id` remains null.

All repository evidence is synthetic and contains no real operational data, coordinates, unit information, personal data, credentials or material from another project.

Merge requires exact-head Fable review, explicit Codex adjudication, green CI on the same head and fresh Pavlo authorization naming that head. This act selects no candidate, starts no cycle, opens no T7, accepts no OCP-019/OCP-021/OCP-022, opens no AB-018/AB-005 and authorizes no next act.
