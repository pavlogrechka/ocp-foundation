---
Decision-ID: AD-039
Title: Assignment Temporal and Partial-Scope Negative Boundary Attempts
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-035, AD-038, OCP-003, OCP-005, OCP-016
Applies-To: AB-009, AB-029, OCP-005 §§8, 11, 19.3, 19.5, 19.9
Review-After: Accepted consumer need and separately authorized positive Assignment temporal or partial-scope proposals satisfying OCP-016 G4
---

# AD-039 — Assignment Temporal and Partial-Scope Negative Boundary Attempts

## 1. Mandate and independent results

The authorized question is whether current OCP-005 already prohibits the unresolved outcomes behind two Assignment freeze blockers:

1. Q3/Q9 — retroactive Establishment and more than one applicability interval, represented by `TEMPORAL_MODEL_UNRESOLVED`; and
2. Q5 — a separate scope for part of a composite Resource without a new Resource, represented by `PARTIAL_SCOPE_IDENTITY_UNRESOLVED`.

The zones are evaluated independently. Both proposed closures are **not established**, but for different exact gaps. The current contract already makes an Assignment ineffective before its recorded `established_at`; it does not say when that establishment fact was recorded, forbid later backdating of the transition, or close the set of applicability-interval fields. The composition boundary rejects automatic component Assignment inference; it does not forbid an explicit partial-scope extension or define what subject such an extension would identify.

Q3, Q9 and Q5 remain open and unstruck. Both blockers remain whole-document-freeze blockers. OCP-005 remains `0.2.8 / Draft`; Assignment remains `Accepted`. `ACCEPTED_CONSUMER_COMPATIBILITY_UNPROVEN` also remains unchanged, so no promotion conclusion follows even under a counterfactual where both semantic blockers fell.

## 2. Gate-first result before evidence form

The evidence form does not require OCP-016 G4. AD-039 is negative discovery: it records that two proposed prohibitions cannot be derived and adds no operational result, profile, schema or activation.

Each hypothetical closure is different:

- temporal closure would need a recording-time axis, a retroactivity rule and closed interval-cardinality/representation rules;
- partial-scope closure would need a prohibition or admitted field shape, subject-identity semantics and provenance/derivation rules for a composite part.

Those additions would determine valid Assignment state and derived participation. They are positive-capable rules and require G4, including a concrete Accepted consumer need, exact rule/version and context, plus legitimate owner and evaluator. This act cannot self-supply any of them.

The chosen form is Route I governance/discovery evidence: one two-zone witness, current-tree drift validation, one isolating control and three gap probes. The witness is not an Assignment extension contract.

## 3. Criterion fixed before application

A zone closes negatively only if all applicable conditions already hold in both owner text and executable behavior:

1. the prohibited outcome is named or logically forced by the current contract, not merely omitted from its minimum field list;
2. the current validator rejects an otherwise valid Assignment that attempts the outcome;
3. the negative result does not require a new field, rule, lifecycle transition, subject identity or consumer activation; and
4. the current AD-035 projection can remove the corresponding moving surface and blocker without rewriting its historical baseline.

The temporal zone additionally distinguishes two propositions that must not be collapsed: “not effective before the recorded establishment instant” and “the establishment instant cannot be recorded retroactively.” Passing the first does not prove the second.

## 4. Q3/Q9 temporal owner-text derivation

### 4.1 Existing boundary that does hold

OCP-005 §8 defines `assignment_effective_at` with `established_at <= t` and states that, pending a separate retroactivity decision, Assignment cannot be effective before `established_at`. The executable derivation enforces that exact boundary. With applicability starting at `09:50`, establishment at `09:55` and query time `09:54`, the Assignment remains structurally valid but derives ineffective.

This is a useful control, not a Q3 answer. `established_at` is itself the `occurred_at` value of the unique `Draft → Established` record. The transition record has no recording timestamp, ingestion timestamp, correction lineage or predecessor value. The contract therefore cannot distinguish an original `09:52` occurrence from a later edit that backdates `09:55` to `09:52` while keeping the materialized projection synchronized.

### 4.2 Q3 gap

The exact valid fixture is cloned. Its establishment transition and matching `established_at` projection are changed together from `09:55` to `09:52`, after `created_at` and before applicability. The current validator accepts both records. This does not authorize retroactive Establishment. It proves that the current evidence axis cannot detect the operation whose legality Q3 asks about.

Closing Q3 would require at least:

- `ESTABLISHMENT_RECORDING_TIME_AXIS`; and
- `RETROACTIVE_ESTABLISHMENT_PROHIBITION_OR_RULE`.

The existing pre-establishment effectivity boundary cannot be generalized into either obligation.

### 4.3 Q9 gap

OCP-005 §6.3 gives one `applicability_start` and optional `applicability_end`, while §6 expressly says the list is a minimum verifiable contract and not a database/API schema. Q9 directly asks whether one Assignment may carry several non-contiguous intervals or needs a separate Assignment per interval. No current invariant says “exactly one interval representation” or rejects additional interval-bearing structure.

The exact valid fixture is cloned with an additional synthetic `applicability_intervals` value containing two separated intervals. The current validator accepts it because it checks the required single interval but has no closed-world or extra-interval rule. This acceptance does not admit the field. It proves that current executable behavior cannot enforce the proposed “one interval only” negative boundary.

Closing Q9 would require at least:

- `CLOSED_WORLD_APPLICABILITY_INTERVAL_CARDINALITY`; and
- `MULTI_INTERVAL_REPRESENTATION_OR_SEPARATE_ASSIGNMENT_RULE`.

Q3 and Q9 therefore remain open. `TEMPORAL_MODEL_UNRESOLVED` remains blocking.

## 5. Q5 partial-scope owner-text derivation

OCP-005 §6.1 requires exactly one directly referenced Resource and Operation. For group involvement it permits a Resource that represents the group or separate Assignment per Resource. Section 11 says a composite-Resource Assignment does not automatically create Assignment for components and that explicit inheritance or mass creation may be defined separately.

These are reference-cardinality and non-inheritance boundaries. They prevent an inferred child Assignment; they do not decide whether the one referenced composite Resource may be narrowed by an explicit local scope, whether a part must first become a Resource, or what identity/provenance such a scope would carry. Q5 keeps that choice open by name.

The exact valid fixture is cloned with a synthetic `resource_scope` identifying one synthetic component while leaving the single `resource_ref` unchanged. The current validator accepts it because no rule recognizes or rejects the extension. This acceptance does not authorize partial scope. It proves that non-inheritance is not an executable prohibition on an explicit partial-scope field.

Closing Q5 would require at least:

- `PARTIAL_SCOPE_FIELD_PROHIBITION_OR_SCHEMA`;
- `COMPOSITE_PART_SUBJECT_IDENTITY_RULE`; and
- `PARTIAL_SCOPE_DERIVATION_AND_PROVENANCE`.

Q5 remains open. `PARTIAL_SCOPE_IDENTITY_UNRESOLVED` remains blocking.

## 6. Executable evidence and preserved projection

`assignment-temporal-scope-attempt.yaml` binds the two independent zone results, six owner-text evidence groups, seven missing obligations, one isolating temporal control, three gap probes, the unchanged Q3/Q9/Q5 projection and both unchanged blockers.

The checker fails if:

- any question is struck, removed or reclassified;
- either moving surface or blocker disappears;
- an owner-text token changes;
- the known pre-establishment effectivity boundary stops holding;
- any gap probe stops reproducing;
- the witness claims either closure does not require G4; or
- a new promotion cycle starts.

The required test `test_every_defensive_value_is_individually_fixture_and_mutation_live` removes or mutates each declared defensive value individually. No fixture coverage is claimed. The existing fixture remains byte-identical and is only an exact probe input.

AD-035 and `assignment-stable-surface.yaml` remain byte-identical historical discovery objects. AD-039 validates their live projection without changing their baseline.

## 7. Outcome-fair comparison

The same axes are applied separately to every candidate result: owner-text derivability, executable rejection, G4 legality, migration and rollback.

### 7.1 Temporal zone

| Outcome | Owner text / probe | G4 and migration | Disposition |
|---|---|---|---|
| T0 — close Q3 and Q9 from existing §8 | §8 rejects pre-establishment effectivity, not later backdating or an extra interval representation; both gap probes pass | would hide new temporal rules | rejected |
| T1 — close Q3 only | no recording-time axis; synchronized backdate passes | needs positive history/retroactivity contract | rejected |
| T2 — close Q9 only | minimum singular interval is not closed-world; additional two-interval value passes | needs positive cardinality/representation contract | rejected |
| TH — retain both questions and blocker | exact match to owner text and executable behavior | no migration or activation | selected discovery result |

### 7.2 Partial-scope zone

| Outcome | Owner text / probe | G4 and migration | Disposition |
|---|---|---|---|
| S0 — non-inheritance already forbids partial scope | conflates no automatic component Assignment with no explicit local scope; probe passes | would hide a new subject-identity rule | rejected |
| S1 — one Resource reference forces a new Resource for every part | grouping guidance does not define part identity | needs positive identity and reference migration contract | rejected |
| SH — retain Q5 and blocker | exact match to open question and executable gap | no migration or activation | selected discovery result |

No future temporal or scope model is selected.

## 8. Exact baseline and full-chain anchors

The baseline is `main@94820489c7e6de17bc7eb1439a1c3dd78bfbc14f`, tree `b17dfceb0a0b8d698943141406f640f6ce42afa8`. Each object below was resolved at that commit, reverse-resolved through `git ls-tree -r` to the declared path, checked for its stated role/status and SHA-256 hashed from the same bytes. Every declared path matched its reverse resolution.

| Evidence | Reverse-resolved path / declared state | Git blob | SHA-256 |
|---|---|---|---|
| OCP-005 | `docs/005-assignment-concept/README.md`; `0.2.8 / Draft`, Assignment `Accepted`, Q3/Q9/Q5 open | `6e6c00e723b15a348e7610d4ca5a1ae23526c52b` | `a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065` |
| OCP-016 | `docs/016-core-boundary/README.md`; `1.0.0 / Canonical`, G4 | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| AD-035 | `architecture/discovery/AD-035-assignment-stable-surface.md`; `0.1.0 / Discovery` | `81ed1c4981c97a0d0a4511e4492741bf5382ce05` | `85a10e965faaa7ba65484efe08e985b7a04bf06712553c914673d65faf1df805` |
| AD-038 | `architecture/discovery/AD-038-assignment-amendment-q2-attempt.md`; `0.1.0 / Discovery` | `1f1d6ef3bed85ee2910d93072e3e394da7453b4c` | `3e9311901a261bb297c13c93616f3c65421757e6a8468ef013875106a22df1c9` |
| Assignment witness | `architecture/assignment-stable-surface.yaml`; schema 1, both blockers live | `ae8a2ff5bf493182d4cd51e897afe736ed36cd5d` | `617af7d0598bbdd756fd890a6dcd38f0324d6c481abf2f72c5a871c439a6bcc8` |
| Assignment checker | `tools/ontology_checker/ocp_checker/checker.py`; static Assignment validation/effectivity | `120ada9dd00b1df0b46cf3060aef2b0c290948b1` | `3a093f0d76113bb5dd2799c7d0aaf73b51b752569dc13de145bb3d158a7b4a47` |
| Probe fixture | `tools/ontology_checker/fixtures/assignment/valid-established.yaml`; valid Established Assignment | `354de6880fe59429c40179eedd4037e52ff5208a` | `3f2ea38f35292b821a7297ed4604a1764efd12c5399ee61a64ea7a2aa5b91117` |
| Promotion gate | `architecture/foundation-promotion-gate.yaml`; schema 5, only `EVENT_T6` complete, no active cycle | `78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1` | `ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd` |
| Architecture backlog | `backlog/architecture-backlog.md`; AB-009/AB-029 Open | `83d47b71c0fa582a4986ad6550d5fb38caf19d83` | `c3ecd26b67234571ee329a28ff6e65c5bdbae63fb77470b4240f13f902d6aeae` |

Hashes identify evidence, not authority. No duplicate-content path substitutes for a declared primary.

## 9. Version, accounting, migration and rollback

AD-039 begins at `0.1.0 / Discovery`: it is a new two-zone falsification record, not a semantic decision or OCP lifecycle change. `assignment-temporal-scope-attempt.yaml` begins at schema 1 because it introduces a new evidence language. OCP-005 does not change version because its semantics, questions and blockers do not change.

The checker module/tests add governance proof only. Unit-test accounting increases derivationally; fixture accounting remains unchanged. README, roadmap, backlog descriptions and checker documentation are non-authoritative projections without artifact SemVer.

There is no Assignment data, reference, lifecycle, interval, scope, Resource, consumer, schema or fixture migration. Rollback removes AD-039, its witness/module/tests/check integration and accounting/documentation entries as one reviewed unit. It cannot close a question or remove a blocker.

## 10. Protected state and lawful continuation

OCP-005, OCP-000, OCP-002, every Concept status, graph edge, P-001 byte, fixture, reviewed snapshot, AD-035, every historical `baseline_*` object and the promotion gate remain unchanged. OCP-005 stays `0.2.8 / Draft`; Assignment stays `Accepted`; the gate retains only completed `EVENT_T6` with `active_cycle_id: null`.

AB-009, AB-029, AB-018 and AB-005 retain their statuses. No candidate is selected, no cycle begins, no T7 opens and no later act is authorized.

The shortest lawful continuation for either zone is not another negative restatement. A separately mandated positive proposal must name the exact temporal or subject-identity rule, its replay/provenance model, a concrete Accepted consumer need and a complete G4 binding. Until then Q3/Q9/Q5 and both blockers remain current.

## 11. Exact-head gates

AD-039 becomes repository evidence only after Fable review of one exact unchanged head, Codex adjudication, green CI on that same head, fresh explicit Pavlo authorization naming it and squash merge. Any head change resets all four gates.
