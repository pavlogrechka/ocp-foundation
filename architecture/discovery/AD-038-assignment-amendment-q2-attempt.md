---
Decision-ID: AD-038
Title: Assignment Q2 Negative Closure Attempt
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-035, OCP-001, OCP-005, OCP-013, OCP-015, OCP-016, OCP-017, OCP-020, OCP-021
Applies-To: AB-026, OCP-005 §19.2
Review-After: Accepted consumer need and a separately authorized positive Assignment amendment proposal satisfying OCP-016 G4
---

# AD-038 — Assignment Q2 Negative Closure Attempt

## 1. Mandate, hypothesis and result

The separately authorized question is whether OCP-005 §19.2 can close negatively without new semantics: no separate amendment model is needed because every post-Establishment role or applicability change already occurs through a new Assignment carrying `supersedes_assignment_ref`.

The hypothesis is **not established**. Current OCP-005 permits a new Assignment and an optional supersession reference, but does not make established role/applicability values immutable and does not require supersession when either value changes. Its finite transition history records lifecycle changes, not field-value changes. Closing Q2 negatively would therefore add rules rather than expose an existing boundary.

Q2 remains open and unstruck. `AMENDMENT_MODEL_ABSENT` remains a whole-document-freeze blocker. AB-026 remains Open. OCP-005 remains `0.2.8 / Draft`; Assignment remains `Accepted`.

## 2. Gate-first result before evidence form

OCP-016 G4 does not apply to this negative discovery evidence: AD-038 records that the proposed boundary cannot be derived and produces no operational rule, positive result, profile or activation.

The hypothetical closure is different. To make supersession the only lawful post-Establishment path it would need positive owner rules for role immutability, applicability immutability, required successor binding and change provenance. Those rules determine valid Assignment mutation and replay. They are positive-capable and require G4, including a concrete Accepted consumer need, exact rule/version, snapshot/context and legitimate owner/evaluator. None may be self-supplied by this attempt.

The chosen form is therefore Route I governance/discovery evidence: one witness, drift validation and gap probes. It does not become the missing amendment model.

## 3. Criterion fixed before application

The hypothesis passes only if all four conditions already hold in the exact owner text and current executable behavior:

1. established role and applicability values are immutable;
2. changing either value requires a distinct Assignment with `supersedes_assignment_ref`;
3. the successor and prior Assignment preserve an attributable trace of what changed; and
4. every current Accepted direct consumer remains compatible without an in-place amendment capability.

The result is all-or-nothing for Q2. A merely available new-Assignment path cannot prove it is the only path. Consumer compatibility cannot manufacture missing owner rules.

## 4. Owner-text derivation

The live owner contract fails conditions 1–3.

| Surface | What current OCP-005 says | Consequence |
|---|---|---|
| Minimum contract | `supersedes_assignment_ref [optional]`; role and applicability values are required for Established lineage | presence and structural validity do not make those values immutable |
| §6.1 and invariant 4 | only `resource_ref` and `operation_ref` are immutable after `Draft → Established` | endpoint immutability cannot be generalized to role/applicability |
| §7 | transition history permits only Establishment, Cancellation, Closure and Revocation | no transition record identifies a role/applicability value change |
| §12 | Resource replacement may use a new Assignment; supersession is replacement intent and does not terminate the prior Assignment | the section neither owns role/applicability change nor requires supersession for it |
| §14 item 6 | role/applicability change must be traceable and the final amendment model remains open | the obligation is explicit while its mechanism is absent |
| §19 item 2 | asks which amendment model is needed | the question still names the missing choice directly |

The mandate referred to traceability as “§18.6”; on the exact base the live normative statement is §14 item 6, while §18 is Non-Examples. AD-038 follows the current object rather than transferring a stale section coordinate.

Example B shows that two distinct Assignments may carry different roles and intervals for the same Resource/Operation, but it does not establish replacement or require supersession. Example D uses supersession for replacement of a Resource, not amendment of role or applicability. Neither example closes the rule gap.

The four rules missing from the proposed boundary are individually named in `assignment-amendment-q2-attempt.yaml`:

- `ROLE_VALUE_IMMUTABILITY_AFTER_ESTABLISHMENT`;
- `APPLICABILITY_VALUE_IMMUTABILITY_AFTER_ESTABLISHMENT`;
- `SUPERSESSION_REQUIRED_FOR_ROLE_OR_APPLICABILITY_CHANGE`; and
- `AMENDMENT_PROVENANCE_BINDING`.

Adding any of them to OCP-005 would be semantic work outside this mandate.

## 5. Accepted-consumer inventory and compatibility

The enumeration criterion is current structured `Depends-On: OCP-005` plus current `Status: Accepted | Canonical`; prose, snapshots and the historical AD-035 baseline do not add a consumer.

AD-035 originally found four Accepted consumers and Draft OCP-021. After PR #160, the live current inventory has **five** Accepted consumers. The original baseline remains byte-unchanged; this act uses current metadata.

| Consumer | Exact reliance relevant to Q2 | Needs in-place amendment? | Effect of leaving Q2 open |
|---|---|---|---|
| OCP-013 | excludes Assignment mutation/replacement authority | no | its negative boundary remains intact |
| OCP-015 | preserves Assignment identity and excludes workflow mutation | no | no compatibility change |
| OCP-017 | reads current `assignment_effective_at`/transition truth and never edits transition history | no | it can consume current truth but cannot choose an amendment model |
| OCP-020 | explicitly cannot create, amend or terminate Assignment | no | neutral quantitative input remains unchanged |
| OCP-021 | treats Assignment references as upstream truth and forbids mutation/supersession authority | no | its negative Reservation/Allocation boundary remains unchanged |

No Accepted consumer disproves the proposed negative boundary by requiring in-place amendment. Equally, no consumer supplies the three missing owner rules or the provenance binding. Condition 4 passes; conditions 1–3 fail. This separation prevents consumer silence from being mistaken for semantic closure.

## 6. Executable gap proof

The exact valid Established Assignment fixture is evaluated unchanged, then cloned twice while keeping `transition_history`, establishment `provenance_ref` and `supersedes_assignment_ref: null` unchanged:

1. `role_specification.role_code` changes from `executor` to `support`;
2. `applicability_end` changes from `2026-08-02T12:00:00Z` to `2026-08-02T13:00:00Z`.

The current `validate_assignment` accepts the original and both variants. This does not authorize in-place mutation. It proves that current executable behavior sees only alternative static records and has no evidence axis capable of distinguishing a post-Establishment value change. A negative closure that claimed the checker already enforces supersession would therefore be false.

`assignment-amendment-q2-attempt.yaml` binds the owner tokens, all five live consumers, four missing obligations, both probes, the unchanged Q2/moving-surface/blocker projection and the unchanged promotion gate. The checker fails if Q2 is marked resolved, its classification is weakened, the moving surface or blocker is removed, a consumer changes, an evidence token disappears, either probe stops reproducing, or a promotion cycle starts.

The required test `test_every_defensive_value_is_individually_fixture_and_mutation_live` removes or mutates each declared defensive value individually. No fixture coverage is claimed; the existing fixture remains byte-identical and acts only as an exact probe input.

## 7. Outcome-fair comparison

The same axes are applied to every result: owner-text derivability, traceability, consumer compatibility, G4 legality, migration and rollback.

| Outcome | Owner-text result | Consumer result | G4 / cost | Disposition |
|---|---|---|---|---|
| N — close Q2: supersession is already exclusive | fails: optional Resource-replacement mechanism is not role/applicability immutability | compatible but non-authoritative | would hide new positive rules | rejected |
| P — partial close for role only | fails: role is required but mutable; no role-change provenance | no consumer requires amendment | requires a new role amendment rule | rejected |
| T — partial close for applicability only | fails: interval is structurally checked but mutable; no change provenance | OCP-017 consumes current effectivity only | requires a new temporal amendment rule | rejected |
| H — hold Q2 open with exact missing rules | matches current owner text and executable gap | preserves all five consumers | no positive activation; no migration | selected discovery result |

This is not a selection of a future amendment model. It is only the result of the authorized falsification attempt.

## 8. Exact baseline and full-chain anchors

The baseline is `main@448d7d10fe3a3213da8479ce991995e01102cf3b`, tree `7c3e378aefbd3ccb785ee3117ea52805170a50b3`. Every object below was resolved at that commit, reverse-resolved with `git ls-tree -r` to the declared path, checked for its stated role/status and SHA-256 hashed from the same bytes. Every declared path matched its reverse resolution.

| Evidence | Reverse-resolved path / declared state | Git blob | SHA-256 |
|---|---|---|---|
| OCP-005 | `docs/005-assignment-concept/README.md`; `0.2.8 / Draft`, Assignment `Accepted`, Q2 open | `6e6c00e723b15a348e7610d4ca5a1ae23526c52b` | `a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065` |
| OCP-016 | `docs/016-core-boundary/README.md`; `1.0.0 / Canonical`, G4 | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| AD-035 | `architecture/discovery/AD-035-assignment-stable-surface.md`; `0.1.0 / Discovery` | `81ed1c4981c97a0d0a4511e4492741bf5382ce05` | `85a10e965faaa7ba65484efe08e985b7a04bf06712553c914673d65faf1df805` |
| Assignment witness | `architecture/assignment-stable-surface.yaml`; schema 1, Q2/blocker live | `ae8a2ff5bf493182d4cd51e897afe736ed36cd5d` | `617af7d0598bbdd756fd890a6dcd38f0324d6c481abf2f72c5a871c439a6bcc8` |
| Assignment checker | `tools/ontology_checker/ocp_checker/checker.py`; static Assignment validation | `120ada9dd00b1df0b46cf3060aef2b0c290948b1` | `3a093f0d76113bb5dd2799c7d0aaf73b51b752569dc13de145bb3d158a7b4a47` |
| OCP-013 | `docs/013-resource-interchangeability/README.md`; `0.2.0 / Accepted` | `658a291b4c3b9a0229aba09d485c1137723fe70b` | `a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74` |
| OCP-015 | `docs/015-coordination-workflow/README.md`; `0.2.0 / Accepted` | `ea60634e54faedabb8c5e08b036030c2f0e4e20b` | `6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d` |
| OCP-017 | `docs/017-operation-lifecycle/README.md`; `0.2.0 / Accepted` | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| OCP-020 | `docs/020-quantitative-constraint-input/README.md`; `0.2.0 / Accepted` | `0e1e7d0947ab3c7d1c0355258651179f618636a2` | `1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c` |
| OCP-021 | `docs/021-reservation-allocation-boundary/README.md`; `0.2.0 / Accepted` | `bae4ac5de36b5d2a2d0c9182e5f1208c14593a35` | `6289378b6d9f785e24abca39dbd6d3da550ccb21a43b3d1632e8c5de4894a89e` |
| Promotion gate | `architecture/foundation-promotion-gate.yaml`; schema 5, only `EVENT_T6` complete, no active cycle | `78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1` | `ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd` |
| AB backlog | `backlog/architecture-backlog.md`; AB-026 Open | `21b5052172ad015480475a570f0e2e3797f5e0bd` | `761edb53dcb5062f05a47fab503e651410401f2fcba374dbd6958942e488005c` |
| Gap-probe fixture | `tools/ontology_checker/fixtures/assignment/valid-established.yaml`; valid Established Assignment | `354de6880fe59429c40179eedd4037e52ff5208a` | `3f2ea38f35292b821a7297ed4604a1764efd12c5399ee61a64ea7a2aa5b91117` |

Hashes identify evidence, not authority. No duplicate-content path substitutes for a declared primary.

## 9. Version, accounting, migration and rollback

AD-038 begins at `0.1.0 / Discovery`: it is a new falsification record, not a semantic decision or OCP lifecycle change. `assignment-amendment-q2-attempt.yaml` begins at schema 1 because it introduces a new evidence language. OCP-005 does not change version because neither its semantics nor its question disposition changes.

The checker module/tests add governance proof only. Unit-test accounting increases derivationally; fixture accounting does not change. README, roadmap, backlog description and checker documentation are non-authoritative projections without artifact SemVer.

There is no Assignment data, reference, lifecycle, role, applicability, transition, consumer, schema or fixture migration. Rollback removes AD-038, its witness/module/tests/check integration and accounting/documentation entries as one unit. It cannot close Q2 or remove its blocker.

## 10. Protected state and lawful continuation

OCP-005, OCP-000, OCP-002, every Concept status, graph edge, P-001 byte, fixture, reviewed snapshot, historical `baseline_*` object and promotion-gate byte remain unchanged. OCP-005 stays `0.2.8 / Draft`; Assignment stays `Accepted`. The gate keeps only completed `EVENT_T6` and `active_cycle_id: null`.

AB-026, AB-018 and AB-005 retain their statuses. No candidate is selected, no cycle begins, no T7 opens and no later act is authorized.

The shortest lawful path is not another negative restatement. A separately mandated positive proposal must name which changes are immutable, how successor/prior Assignment are linked, how traceability and replay work, which Accepted consumer needs the result and how G4 is satisfied. Until then Q2 and `AMENDMENT_MODEL_ABSENT` remain current.

## 11. Exact-head gates

AD-038 becomes repository evidence only after Fable review of one exact unchanged head, Codex adjudication, green CI on that same head, fresh explicit Pavlo authorization naming it and squash merge. Any head change resets all four gates.
