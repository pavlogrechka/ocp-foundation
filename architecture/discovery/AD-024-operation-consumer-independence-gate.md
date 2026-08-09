---
Decision-ID: AD-024
Title: Operation Consumer Independence Gate
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-023, OCP-001, OCP-004, OCP-006, OCP-014, OCP-015, OCP-016, OCP-017, OCP-019
Applies-To: AB-018
---

# AD-024 — Operation Consumer Independence Gate

## 1. Blocking independence test and result

The mandated first step is to state the proposed profile's reason to exist without relying on the later ontology question or its current gate artifacts:

> An Operation-planning consumer needs a replayable decision about whether one exact snapshot-local claimed-incompatibility value is sufficiently exact, attributable, current and criterion-bound for the consumer's own handling decision.

The sentence is intelligible, but the exact baseline does not establish its subject. No current governed artifact names that Operation-planning consumer, declares its protected handling decision, or assigns the criterion to a legitimate semantic owner and evaluator. OCP-004 supplies the local value and structural boundaries; it does not supply the downstream responsibility asserted by the sentence.

The independence test therefore **fails**. Preparing a profile would manufacture the missing consumer and owner in order to reopen AB-018, which OCP-019 §3 forbids. The act stops with a negative result: no profile, route selection, semantic rule, result vocabulary, manifest or positive checker branch is created.

## 2. Exact baseline and anchor chain

The act starts from exact `main@c8cf29d1a5b643f8d06205ecb37b5c1ca381dbf0`, tree `4948b88c45106c94e391d0c8b4339503f7d03b58`.

Each blob was resolved at that commit, reverse-resolved to the listed path and SHA-256 checked from raw blob bytes.

| Input | Git blob | SHA-256 |
|---|---|---|
| AD-023 | `a8d76355b592310156f03b5d655edc52aee3c19f` | `a5d59f8d618cc80c502dadeae5110f010d3e71d3df3eb687eda480560afa9c0d` |
| architecture backlog | `6ccbf84ff736bc46375a9d57fee012bc5c4cfb01` | `1bcae3f18de0a1c8087beb45a7a7e5c3be70b01f9087dc288308477400a63257` |
| OCP-004 | `1ff548a1f213b574472a90a8b3cfe014f6c1ce11` | `9c9173d3a3dec044e2cae2eb8fd5b66d07a106318f497a973409fedf4677155b` |
| OCP-006 | `5d7404717e500c66c0c017263678ae0a1a405c7d` | `e0469604b1d8e6c2156c35e85017129eaca1fb929633a8be0287af4ef67a88aa` |
| OCP-014 | `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` |
| OCP-015 | `ea60634e54faedabb8c5e08b036030c2f0e4e20b` | `6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d` |
| OCP-016 | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-017 | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| OCP-019 | `092770b40541de5959c18b37664b179c7dcb7880` | `8689327a770eecccd40a7d43dd147659c24eb2e1dc0cd117dfe3e75114676bec` |
| Conflict checker | `e1afc840b4523ca783d126742c03b1f98b113102` | `2a5edadc43c0e4a903e422f8de583f41a8765e73c43fedf4a5a9821d2d1c1bca` |
| Conflict tests | `75e2f4fa068fb19a92b196270c1c9a5b056b6176` | `2ae2e56fb9bc6a9045c6b973e07e9fea8c70b3a3fc3c2825cc03b9ef9f13bbd9` |
| Conflict manifest | `640408c10844dd25416efe18ae6926f63292343c` | `44684a5bf48f9c1c79a0379da723179120cc3e867c8b1a1848a5087d5e4ef65d` |

The anchors establish the reviewed absence boundary only. They cannot turn a generic metadata label or a proposed profile into an operational consumer.

## 3. Existing responsibility and the missing step

OCP-004 §11.2 already owns everything presently justified for the local value:

- exact source and target Operation references;
- a closed relation kind and normalized tuple uniqueness;
- non-empty provenance explaining why the value is present; and
- rejection of hidden record identity, history, supersession and current-head semantics.

The same section says the value denotes a **claimed** incompatibility and grants no permission or precedence. It creates no workflow agreement, Constraint applicability, Assignment, Event, outcome, authorization or Concept graph edge. OCP-004's generic `Used-By` labels do not declare an exact consumer need or criterion authority.

A separate profile would therefore need evidence of a distinct handling responsibility beyond OCP-004's existing structural validation. No such obligation appears in the current Operation, lifecycle, Coordination profile or Coordination workflow contracts.

## 4. Reproducible consumer-candidate inventory

The inventory uses the same rule as AD-023 §5. After excluding governance/routing/registry artifacts, OCP-006 as an upstream-only evidence provider and OCP-019 self-consumption, a surface enters when it meets at least one condition: it owns a structural Conflict field or open relation for its governed subject; it is an Accepted consumer/profile/workflow/lifecycle surface that names conflict handling, a responsibility pointer or conflict-shaped input; or it is the Draft defining contract of an Accepted Concept with its own normative Conflict boundary or open question. Mere generic `Used-By` metadata does not qualify.

Exactly seven surfaces meet that rule:

| Candidate | Existing authority | Independence disposition |
|---|---|---|
| OCP-004 | Canonical owner of Operation and the snapshot-local relationship value | defines the value and its structural checks; does not consume a separately governed result |
| OCP-005 | Draft defining contract for Accepted Assignment; §§13–14 and §19.8 describe simultaneous incompatibility through applicable Constraint and keep its representation open | records an open boundary only; declares no exact handling decision, accepted consumer or owner/evaluator |
| OCP-008 | Canonical Objective identity contract with an undefined relation surface | declares no consumer, protected use, rule or criterion authority |
| OCP-010 | Draft defining contract for Accepted Event with an explicit Constraint/Conflict/Risk boundary | preserves non-implications and declares no exact downstream handling decision or owner/evaluator |
| OCP-014 | Accepted Resource-requirement consumer profile | explicitly excludes disagreement handling and cannot transfer its owner reference |
| OCP-015 | Accepted proposal/response workflow evidence | explicitly does not settle disagreement and declares no Operation relationship-use decision |
| OCP-017 | Accepted Operation lifecycle contract | consumes completeness, authorization-source and terminal-alignment evidence; no transition consumes this claimed relationship |

OCP-006 is adjudicated separately as upstream evidence: it owns Constraint applicability and evaluation records, while `evaluator_ref` identifies an implementation or service and does not own a new aggregation criterion. Generic `Operation Planning`, `Coordination Model`, `Business Rules` and `Domain Model` labels are descriptive metadata, not exact governed consumers, protected uses, semantic owners or evaluators.

AD-023 §7 called an OCP-004 profile the shortest *direction* and expressly denied authority to create it in that act. A recommendation is not the independent responsibility missing here.

## 5. Owner and evaluator adjudication

No legitimate exact semantic owner or evaluator can be named on this baseline:

- `Architecture Board` owns document lifecycle and admission decisions, but OCP-019 §3 disqualifies it from substituting for the operational consumer or criterion owner;
- OCP-006 `evaluator_ref` is attributable evaluation provenance, not authority for a new relationship-use criterion;
- the OCP-014 owner is exact to a Resource requirement and cannot be transferred;
- a new profile reference naming itself as owner and evaluator would be self-supply; and
- caller, checker, service label, implementation, timestamp, majority or newest version cannot establish legitimacy.

The missing elements are therefore named as absences: **concrete operational consumer**, **protected handling decision**, **legitimate criterion owner**, and **legitimate criterion evaluator**. Inventing exact strings for them would not close the evidence gap.

## 6. OCP-016 stop before route selection

OCP-016 G3 keeps specialized semantics domain-local unless a concrete consumer proves a different minimal route. G4 requires an Accepted consumer, baseline, rule version, input snapshot, evaluation context and legitimate owner/evaluator for each positive-capable activation.

The independence failure occurs before route comparison. Selecting Route D for a newly named `operation-planning` domain would invent the domain owner; selecting Route C or E would additionally overstate shared or interoperability responsibility; Route F would contradict OCP-004's local-value boundary; Route I cannot own semantic truth. The lawful outcome is **no profile**, not a route chosen by elimination.

## 7. Executable negative evidence

Three fully synthetic fixtures exercise the three tempting self-supply paths:

1. a future-gate-only profile declares itself Draft consumer and criterion owner;
2. a generic `Used-By` label is promoted into a claimed Accepted consumer; and
3. OCP-004's existing local value is treated as if it also declared the downstream protected use.

Each fixture deliberately supplies a structurally complete activation attempt. Focused tests require the declared independence gap for every case, exact invalid validation, and the existing `indeterminate` result. They also require that no attempt derives the forbidden positive result even when all six G4-shaped field groups are caller-supplied.

This grows the baseline from `210` to at least `212` tests and from `163` to at least `166` fixtures. The existing checker and manifest remain byte-identical because they already reject positive authority; the new tests prove the admission gap rather than pretending a machine can decide legitimate ownership.

## 8. Three-act minimum remains future work

A later lawful attempt still requires at least three separately mandated and freshly gated acts:

1. an independent consumer-admission act that first proves a pre-existing operational responsibility and prepares a separate Draft profile without changing OCP-004;
2. a distinct acceptance act, following the OCP-018 Draft/Accepted precedent, that legitimizes the exact consumer, criterion owner and evaluator; and
3. a later positive-model act that may retry OCP-019 §9 and compare object forms only after the Accepted consumer exists.

AD-024 performs none of these acts and does not reserve their IDs, owners, evaluator references, route or result vocabulary.

## 9. Preserved boundaries and backlog disposition

- OCP-004 remains byte-identical at `1.0.0 / Canonical`; no separate profile document is created.
- OCP-006 §13 remains exact: violation does not automatically create Conflict, change lifecycle, cancel Assignment or create Risk, and any aggregation preserves ConstraintEvaluationRecord references.
- OCP-019 remains byte-identical at `0.1.0 / Draft`, with only `conflict_not_established | indeterminate` and no positive authority.
- OCP-016 G3/G4, OCP-004 §11.2 local-value semantics and AD-023's closed gate remain exact.
- AB-018 remains Open because no positive model is compared or selected.
- AB-005 remains Open because no Risk taxonomy or derivation is introduced.
- AB-002, AB-036 and AB-037 remain Open and outside scope.
- No Concept, Concept status, registry row, taxonomy projection, graph edge, foundation map, P-001 invocation or `Review-After` changes.
- `Policy`, `Authority` and `Approval` are not introduced as Concepts.

## 10. Version, rollback and exact-head gates

AD-024 is `0.1.0 / Discovery`: it is the first exact-baseline independence audit for this proposed consumer path and selects no semantic contract. Making it Accepted while AB-018 remains Open would falsely state a resolved Board outcome.

Rollback removes AD-024 and the three independence fixtures/tests, restoring the prior evidence count. It does not remove a profile or authority because neither exists in either tree.

All new fixtures use only `SYNTH` identifiers, opaque snapshots and fixed future synthetic instants. They contain no geometry, coordinates, corridors, sectors, operational windows, callsigns, unit identifiers, personal data, credentials or material copied from another project.

Merge requires exact-head Fable review, Codex adjudication, green required CI and a fresh explicit Pavlo authorization naming the unchanged head. This mandate authorizes preparation and review only; it does not authorize merge, OCP-019 acceptance, a consumer profile, a positive model, production use, Y10D, a normative `Review-After` act, YR or T6.
