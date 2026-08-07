---
Decision-ID: AD-020
Title: Operation Stable-Surface Discovery
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-004, AD-006, AD-011, AD-014, AD-016, OCP-001, OCP-004, OCP-005, OCP-006, OCP-008, OCP-010, OCP-011, OCP-014, OCP-016, P-001
Applies-To: AB-062, Operation stable-surface remediation
Review-After: Completion or failure of the selected OCP-004/OCP-017 remediation; then a fresh blocker/stability audit before any lifecycle proposal
---

# AD-020 — Operation Stable-Surface Discovery

## 1. Mandate and purpose

AD-016V selected U4D only as permission to prepare one outcome-fair discovery of the Operation stable surface. It did not select a lifecycle, relationship, dependency, record form or OCP-004 edit.

OCP-004 already contains a strong candidate kernel:

1. one identified purposeful Operation independent of its name, template, participants and outcomes;
2. one exact active intent branch outside `Draft`;
3. planned and actual temporal context kept distinct;
4. an accepted zero/one/many local spatial-binding contract; and
5. explicit non-implications for participation, completion, outcome, authority, Readiness and State.

The same document also combines unresolved responsibilities:

- a working lifecycle whose `Draft → Planned` gate, authorization source and terminal Assignment interaction are open;
- parent/child composition beside independent inter-operation coordination;
- `Operation generates Event` beside an explicit no-edge/no-dependency statement;
- normative references to Assignment, Constraint, Event and outcome assessment whose defining contracts all depend downstream on OCP-004; and
- four record-like structures with materially different identity, evidence and history properties but no P-001 applicability decision.

Completing everything in place could create one oversized authority. Splitting first could fragment the human contract or move unresolved meaning into empty wrappers. Stabilizing only the easy clauses could hide live normative statements outside the promised surface. AD-020 therefore compares layout, semantic ownership and record form independently.

Revision `0.1.0` selects no outcome. It changes no OCP, Concept, Pattern, dependency, graph edge, schema, checker rule, fixture or backlog status.

## 2. Exact baseline

This discovery starts from post-AD-016V `main@2e34015949088fa6aab89d3ab9c91ad148ed07ef`, tree `6db337f58bcd92a5c99d0fed724ad378f4321ecc`.

### 2.1 Governing and semantic anchors

| Input | Exact state | Git blob | SHA-256 |
|---|---|---|---|
| AD-016V | `0.23.0 / Accepted`; U4D selected for discovery only | `1c438f8f68eae1eae6efce5ff44a925f634f2137` | `ba91d586536e2c132bb1f5a767d45e96e0af911ba8960abd5760483ad8fe269d` |
| OCP-001 governance | `1.0.0 / Canonical`; L2, atomicity and separate gates | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-004 Operation | `0.8.3 / Draft`; Operation `Accepted`; no P-001 invocation | `6f6990ed2cef7887af663e7dc806b34bddca6e30` | `aa81d60ef8c9802f40f488390d151b5f6c50d116ece6576c1783da0e48087033` |
| OCP-005 Assignment | `0.2.5 / Draft`; authoritative participation and independent lifecycle | `e5e0a62eda4ac84be081186c005e0167a3ebe288` | `8172173addc797416a151db198dcbea360711b82fb0a93b3732723f7f71154c6` |
| OCP-006 Constraint | `0.2.4 / Draft`; applicability and decision authority | `020c76f2518491beb2b7696e707224809ff26770` | `a604f6b07373741c9bfb25ad2e064b9b77b4c8fd52c9c3075b4865f9f65dfb27` |
| OCP-008 Objective | `1.0.0 / Canonical`; exact Objective identity and statement | `24ed01e0f5d6bc8f349a7aedae4c5f100eb449ee` | `46f1ecb7b956b106f9c66da0626ec4266961e07492059e594110f63736be6f0d` |
| OCP-010 Event | `0.2.0 / Draft`; independent occurrence, zero/one/many Operation relevance, no current edge | `d73bab07acac3c316a9a2a4f4d25cb1f9b1bdc06` | `f66a2deb2bd8748aa464adefe3f4ff5ac35baf6af017fb9c782f9a427d7ac95f` |
| OCP-011 assessment | `0.3.0 / Accepted`; assessment remains outside Operation lifecycle | `ff2608a372c6305db4c290f05c15e961ca96e6f6` | `1fb08e18fab560e671b468585d699a7d70bd55ed5be674315cb780a48bc70cc5` |
| OCP-014 Coordination profile | `0.2.0 / Accepted`; exact context need without operational permission | `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` |
| P-001 | `0.1.0 / Accepted`; binding only when exactly invoked | `f1e95efa055022a9342b16133bf7b3c3db90fa4f` | `cf6fb3501a1a5504aa873c372e97436813725c6e44a7fc682a2db404a7d97b82` |
| AD-004 intent boundary | `0.3.2 / Accepted`; dual branch now, separately gated Objective-only target | `64f4f520bf4c9add82b7212fedc293c74cab13fc` | `489466ec73dd61f0af4ca0e98a47b0f5e43f4d5ea9b0c0fc6bf77e41e4cb1a2e` |
| AD-006 Event/Result boundary | `0.3.0 / Accepted`; occurrence and assessment identities remain separate | `f5ea5cd9256f90a45071d60d50b23b25f6eb1e6c` | `a97bf053efab6e6f4d4f9d05b07715c73115c037f532ab80c68d68ab67aaeaae` |
| AD-011 State/Readiness boundary | `0.3.0 / Accepted`; S0/R0 no-new-authority controls | `cb398157d1941eb39d2585ed02993af924ff8bd7` | `bbf2916294de1c8bdc81b9e5cbdb77856126856b0c33ad11481f9395e0b85cf2` |
| AD-014 spatial boundary | `0.3.0 / Accepted`; Operation-local binding, no Concept/edge | `4e9aad5631d6990c4eb77d9b9060c5a107ba0e1a` | `dedc3c9e7e3e63a4f969faa55e63206f725aac0830301959ab84bc953ec14544` |

### 2.2 Registry, executable and accounting anchors

| Input | Exact state | Git object | SHA-256 / evidence |
|---|---|---|---|
| OCP-000 registry | `1.4.0 / Canonical`; four Canonical and four Accepted Concepts | blob `54d4f9a908c0ef572a4300be1f31e938db5557ef` | `f88a494aafff88bead233a43156435f460df2db0a31f8900465ac7fd7e1f335b` |
| OCP-002 projection | `1.4.0 / Canonical`; Operation `Accepted` | blob `470c7b035be3039065fc76f03bf76ad5fc8d3064` | `0366d50ec5ac21f5cd1e37af0cf7b46035dde38d0859b4fed9785793c5aa802c` |
| OCP-016 Core Boundary | `1.0.0 / Canonical` | blob `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| Operation validator | identity, active intent, self-parent and spatial subset only | blob `4c28e998b27597cd434eb11b5cfdb0c3b825bceb` | `188785b261912d9a6d4f12dd561ccd73fe62d3aee7e7883e0f83cec1ee6c0553` |
| checker rules manifest | current Operation codes and sources | blob `8d00050e32cea2ceb27d13c3d7788b5e8554cc84` | `e861e860f576cf824aff755d99f0da3118256f20d742f25eb4b0434503c6042d` |
| Operation fixtures | 26 primary files | tree `9d22ac7cacafa46506571dec1b425cb08399d5c1` | recursive manifest `d231eeb6cba63c576f0df851b6a180d9d27a42c843a61898b48746f443961b20` |
| complete fixture/test baseline | 120 non-sensitive fixtures; 172 unit tests | checker tree `d93073d35ad7393dad1f4c2bc70af9f6b64cdc20` | finite structural evidence only |
| architecture backlog | Operation questions remain Open/Deferred; AB-062 Planned | blob `92e6abf91ebb482ec0e6869b9848d78c31c2ac03` | `c2dfb1b9c8b4cf8248c5999bd736a5e95049f9717dca530e83d0c62d1f6a301f` |
| roadmap / README | readiness approximately 71%; AD-020 preparation next | blobs `e280106609d1a8626b02de7577e19181fe33452d` / `0e655aa67077314bdf3ae6e23bcd02f447b5e7a2` | `42adbfeb877b0f6c717dec4d5232e7a3af06560d758cf19fe6a2e76efe867664` / `e7ba16aacce0d8cd9a03f021cd597ed15ddb7492eaa45d3f62b9532123a64d91` |

Hashes establish the reviewed input. They do not choose a semantic owner, outcome or Pattern invocation.

## 3. Inherited mandates

Every admissible outcome must preserve all of the following.

1. Operation remains one identified purposeful, context-bounded activity with identity independent of name, template, classification, participants, location, lifecycle stage, Event and assessment.
2. The current Concept edge remains only `Operation → Objective` unless a later explicit Board act proves a different acyclic graph. This discovery adds none.
3. Outside `Draft`, exactly one active intent branch remains required until a separately authorized change to AD-004's sequenced decision.
4. Objective identity, statement authority and correction history remain governed by exact OCP-008 references.
5. Assignment remains the sole authoritative Core representation of Resource participation. Operation composition creates no Assignment or inherited participation.
6. Constraint remains the owner of applicability, evaluation and blocking/advisory semantics. Operation does not duplicate those derivations.
7. Event keeps occurrence identity independent of Operation. A lifecycle transition is not an Event automatically.
8. `Completed Operation != achieved Objective`; OCP-011 remains the separate assessment owner.
9. AD-014's local spatial binding remains an Operation-owned structured value, not a reusable area identity, P-001 record, Resource or graph node.
10. Operational template identity, reusable spatial identity, domain geometry, Conflict and production schemas stay outside this discovery.
11. Authorization-source semantics and mechanisms remain external. A non-empty provenance reference is traceability, not proof of legitimate authority.
12. Readiness and State are not inferred from Operation lifecycle. `Capability != Readiness` remains exact, and equal Capability claims do not make Resources interchangeable.
13. Resource availability, admissibility, selection, reservation, allocation and interchangeability are not Operation lifecycle projections.
14. No Organization Capability holder, Organization/Resource mapping or identity collapse is introduced.
15. Exact OCP-009 Capability version binding remains unchanged wherever Capability is referenced.
16. P-001 remains `0.1.0 / Accepted`, optional until invoked and incapable of supplying Operation semantics.
17. Each proposed P-001 record family must have its own conformance mapping; similarity or record count cannot create invocation.
18. Missing, unresolved, ambiguous, stale, conflicting or incomparable evidence fails safe. Newest timestamp, storage order, issuer/source/reviewer count and majority never select authority.
19. AB-015, AB-016, AB-017, AB-019, AB-020, AB-023 and AB-028 retain their current statuses. Comparing them is not resolving them.
20. Human-readable normative ownership is required even when a checker can enforce a finite structural subset.

## 4. Decision questions

AD-020 asks:

1. Which exact clauses define the Operation identity and responsibility kernel under every admissible layout?
2. Can the current working lifecycle become a complete OCP-004-owned surface without importing Assignment, Constraint, Event or authorization authority?
3. Would a separate non-Concept Operation Lifecycle contract reduce dependency cycles, or merely fragment one readable subject?
4. What exact data are universally required for `Draft → Planned`, and which sufficiency rules remain domain-owned?
5. Who owns the acceptance envelope for authorization evidence while the source/mechanism remains external?
6. What happens when Operation becomes `Completed`, `Cancelled` or `Aborted` while one or more Assignment remain effective?
7. Which parent/child rules belong to Operation identity/composition, and which inter-operation relations belong to future Coordination?
8. Is the current `Operation generates Event` statement a stable direct relation, an imprecise working phrase or a claim requiring a new dependency/edge?
9. Can Event relevance remain downstream and explicit with no new Concept edge?
10. Which dependency direction preserves the accepted owners of participation, applicability, Event occurrence and assessment without a cycle?
11. Is `ExplicitIntentRecord` already an independently identified governed record, or an Operation-owned versioned value pending AD-004's Objective-only sunset gate?
12. Are validation records independently addressable evidence records or immutable nested entries whose identity has only snapshot-local scope?
13. Must retained lifecycle transition history invoke P-001 Module B, and under which owner?
14. Is `InterOperationRelationshipAssertion` independently identified, a nested assertion, or a future Coordination-owned record?
15. Which candidate forms can honestly avoid P-001, and which existing identity/history fields make avoidance impossible?
16. How do all five direct OCP-004 consumers migrate or replay under each layout?
17. Can a stable OCP-004 surface be stated without treating the checker subset as complete semantics?
18. What exact data migration, reference rebinding or historical-wrapper change would each outcome require?
19. Which evidence forces hold rather than silent scope expansion?
20. Which later Board act may select one combined treatment without inheriting authority from this discovery?

## 5. Terms that must remain distinct

| Term | Meaning here | Not implied |
|---|---|---|
| Operation identity | exact identity of one purposeful activity | template, title, participants, lifecycle stage or outcome |
| responsibility kernel | the finite positive rules OCP-004 must own under every layout | every lifecycle, coordination or domain rule |
| completeness envelope | structural facts required before one stage transition | domain sufficiency, authorization or success |
| authorization evidence | exact evidence accepted by a named contract | authority merely because a field is non-empty |
| participation | OCP-005 derivation from effective Assignment | direct Operation-owned Resource edge |
| applicability | OCP-006 decision over exact context and evidence | lifecycle permission or success |
| Event relevance | explicit relation/reference between an independent Event and Operation | Event generation, ownership or automatic occurrence |
| completion | terminal Operation execution stage | Objective achievement or favorable assessment |
| composition | parent/child part-whole between Operation | coordination among independent Operation |
| lifecycle contract | rules for Operation stages and transitions | shared State Concept or authorization mechanism |
| local record | record whose domain meaning is owned in the Operation boundary | exemption from P-001 when independent identity/history exists |
| inline value | part of one owning snapshot with no independent address, lifecycle or supersession | a record renamed to avoid conformance |
| split authority | distinct artifacts with one defining owner per rule and explicit dependency direction | copied prose or dual ownership |
| no-new-edge baseline | existing `Operation → Objective` Concept graph only | denial that downstream exact references may exist |

## 6. Current OCP-004 section ledger

The labels are discovery classifications, not accepted outcomes:

- **K** — candidate retained kernel;
- **B** — unresolved semantic/authority blocker;
- **S** — explicit exclusion or downstream boundary; and
- **C** — cleanup, example or historical accounting.

| Section | Candidate retained content | Current B/S/C boundary |
|---|---|---|
| §§1–3 | identified purposeful context-bounded activity; domain specialization excluded | references to events/results are contextual, not ownership (K/S) |
| §4 | current status table and non-implication boundary | Assignment/Constraint/Event are prose dependencies but not metadata dependencies (B) |
| §5 | stable identity independent of name/template/repetition | exact identity continuity is K; template model remains S |
| §6 | readable Operation context decomposition | Outcome and relationship branches cannot establish owner by diagram (B) |
| §7 | exact Objective branch, dual-branch invariant and fail-safe validation | object class/P-001 of intent and validation evidence is B; AD-004 sunset remains separate |
| §8 | planned and actual time remain distinct | final time model is S |
| §9 | accepted local spatial binding and fail-safe envelope | reusable spatial identity/domain geometry remain S; no reopening evidence found (K/S) |
| §10 | Assignment owns participation; no independent direct edge | dependency direction and terminal alignment remain B; participation rule is K |
| §11.1 | pursuit, participation and applicability boundary vocabulary | `generates Event` conflicts with §14 no-edge position (B) |
| §11.2 | independent coordination does not arise automatically | relation kinds, provenance owner and record class remain B |
| §11.3 | authorization is required in some contexts | source and mechanism are intentionally S; evidence acceptance owner is B |
| §12 | parent/child differs from independent coordination; no Assignment inheritance | exact composition rules are B |
| §13 | finite working stages and no shared State | completeness, authority, transition class and terminal alignment are B |
| §14 | Event and assessment identities stay separate; completion is not achievement | Operation/Event relevance owner and `generates` disposition are B |
| §§15–17 | stable non-implications mixed with open lifecycle/record invariants | each rule must be assigned to K, B or S before remediation |
| §§18–19 | human examples and non-examples | C evidence; cannot create authority |
| §§20–21 | explicit open and deferred questions | B/S ledger; cannot enter a `1.x` promise silently |
| §§22–24 | prior PATCH accounting | historical C only |

No positive outcome may call §§1–24 one stable surface without resolving every B row or explicitly removing it from the current compatibility promise.

## 7. Current structure and field ledger

| Structure / field group | Current contract | Identity/history evidence | Open classification |
|---|---|---|---|
| Operation identity | one stable non-empty `operation_id` | independently exact and Concept-owned | retained K |
| active intent branch | `objective_refs` xor `ExplicitIntentRecord` outside `Draft` | exact Objective resolution or local record/value | retained semantic invariant; form B |
| `ExplicitIntentRecord` | `intent_id`, immutable `intent_version_ref`, statement and exact validation binding | named identity plus independent versions, but no P-001 mapping/provenance field | B |
| validation evidence | `validation_id`, exact intent/rule/input bindings, time, evaluator and result | individually named immutable evidence entries | B |
| temporal context | separate planned/actual bounds | Operation snapshot fields; no separate identity | K as inline values |
| local spatial binding | local `(operation_id, binding_id)` subject and exact versions | explicitly not independently reusable | retained K; P-001 not applicable by AD-014 |
| Assignment participation | exact external Assignment records | authority and effectivity reside in OCP-005 | retained boundary, not Operation record |
| Constraint applicability | external Constraint and evaluation semantics | authority resides in OCP-006 | retained boundary, not Operation record |
| parent/child | direct Operation references with acyclicity claim | self-parent checked; complete graph rule not executable here | B |
| `InterOperationRelationshipAssertion` | source, free enumerated relation type, target and provenance | endpoint/provenance properties but no assertion identity, effectivity or history | B |
| `lifecycle_stage` | optional materialized working stage | no declared authoritative derivation in OCP-004 | B |
| `LifecycleTransitionRecord` | source/target stage, occurrence time and provenance | history-like entry lacks transition identity and Operation record reference | B |
| Event relevance | prose only | no exact relation owner or current edge | B |
| Outcome assessment | external OCP-011 record | never Operation field or lifecycle result | retained S boundary |

The field name `Record` does not decide P-001. Conversely, removing that suffix cannot erase independent identity, endpoint, evidence or history requirements.

## 8. Consumer and executable evidence

### 8.1 Exact primary consumers

A fresh `Depends-On` scan of all seventeen primary OCP documents yields exactly five OCP-004 consumers:

| Consumer | Current use of Operation | Rebinding risk |
|---|---|---|
| OCP-005 Assignment | exact `operation_ref`, participation derivation and no-inheritance rules | any Operation identity or terminal-coupling change |
| OCP-006 Constraint | Operation as context/subject and transition precondition target | any lifecycle or composition propagation rule |
| OCP-010 Event | independent Operation boundary and integrated scenario | any Event edge/dependency reversal or lifecycle-to-Event rule |
| OCP-011 assessment | integrated completed-Operation evidence context | any completion-to-outcome authority change |
| OCP-014 Coordination profile | exact Operation or other governed context reference | any context identity or authorization inference |

The consumer count measures migration surface only. It cannot choose an outcome.

### 8.2 Executable boundary

The current Operation validator and 26 primary fixtures demonstrate:

- a required non-empty Operation identity;
- self-parent rejection, but not complete multi-record acyclicity;
- the `objective_refs`/explicit-intent exclusive branch outside `Draft`;
- exact Objective resolution;
- immutable exact-binding validation evidence and fail-safe projection; and
- the accepted local spatial-binding envelope and transition replay.

They do not demonstrate:

- complete lifecycle paths or authoritative stage projection;
- `Draft → Planned` completeness;
- authorization-source legitimacy;
- terminal Assignment alignment;
- complete parent/child acyclicity across a dataset;
- inter-operation relationship kind, identity, effectivity or provenance authority;
- Operation/Event relevance or a Concept edge; or
- P-001 conformance for any OCP-004 structure.

Green runs are necessary regression evidence, not semantic completeness or Board authority.

## 9. Authority and dependency baseline

The acyclic baseline is responsibility-directed:

```text
OCP-004 owns Operation identity and Operation-local invariants.
OCP-005 depends on OCP-004 and owns participation.
OCP-006 depends on OCP-004/OCP-005 and owns applicability/constraint decisions.
OCP-010 depends on OCP-004 and owns Event occurrence identity.
OCP-011 depends on OCP-004/OCP-006/OCP-010 and owns assessment.
OCP-014 depends on OCP-004/OCP-006 and owns its exact consumer requirement.
```

OCP-004 can cite downstream boundaries descriptively without taking their formulas as its own. Making OCP-004 depend directly on OCP-005, OCP-006 or OCP-010 would create a cycle unless a separately reviewed topology change moves or removes an existing dependency. Prose cannot hide that graph consequence.

## 10. Top-level authority/layout outcomes

### H0 — hold

Keep OCP-004 `0.8.3 / Draft`, Operation `Accepted` and every current dependency unchanged. Record the unresolved classifications and require a concrete reopening trigger. H0 adds no layer and performs no migration.

### H1 — one complete in-place surface

Make OCP-004 the single readable owner of the complete Operation kernel, lifecycle, composition and local record semantics. Downstream contracts retain participation, applicability, Event and assessment authority. Every B item must be completed before a stable promise; none may be hidden as “future work.”

### H2 — two bounded in-place surfaces under one owner

Keep one OCP-004 authority but separate a stable Operation identity/context surface from a stable Operation-support surface for lifecycle, composition and selected local records. The boundary must be normative and readable; two headings cannot disguise overlapping authority.

### H3 — stable Operation kernel plus separate lifecycle authority

Keep Operation identity/context and parent/child boundary in OCP-004. Move the complete lifecycle, transition history, stage completeness and terminal-alignment contract to one downstream non-Concept Operation Lifecycle artifact that depends on OCP-004 and any exact consumers it uses. Independent coordination remains separately bounded.

### H4 — stable Operation kernel plus separate lifecycle and coordination authorities

Keep only the Operation kernel and cross-contract boundaries in OCP-004. Give lifecycle and inter-operation relationship semantics to distinct downstream non-Concept contracts, each with one owner and explicit dependencies. H4 has the largest fragmentation and migration burden.

Extraction never creates a fundamental Concept automatically. A separate artifact must pass OCP-016 routing and cannot self-admit through this discovery.

## 11. Outcome completeness

A top-level outcome is complete only when it specifies:

1. one owner for every current normative OCP-004 statement;
2. the exact lifecycle treatment L0/L1/L2;
3. completeness, authorization-evidence and terminal-alignment treatments;
4. composition versus coordination ownership;
5. Event relevance and graph/dependency consequences;
6. authority direction for all five consumers;
7. one object-form result for each of the four record-like structures;
8. exact P-001 conformance wherever invoked;
9. current data/reference migration and historical replay;
10. human scenarios, executable evidence, rollback and stop conditions; and
11. explicit exclusions and unresolved backlog preservation.

An unspecified blend such as “mostly H2 with some extraction” is not an outcome.

The ten AD-016V §233 axes map into this discovery as follows:

| §233 axis | AD-020 treatment |
|---:|---|
| 1 — identity/responsibility kernel | §§6–7 and provisional guarantees §18 |
| 2 — lifecycle location | H0–H4 and L0–L2 in §§10 and 12.1 |
| 3 — completeness, authorization source and terminal Assignment | G0–G2, A0–A2 and T0–T2 in §§12.2–12.4 |
| 4 — composition versus coordination | C0–C2 in §12.5 |
| 5 — Event statement, relevance and graph | E0–E3 in §12.6 |
| 6 — cross-contract authority/dependency | D1–D3 in §§9 and 12.7 |
| 7 — object class/P-001 applicability | four separate ledgers in §§7 and 13 |
| 8 — retain-local, exact invocation and inline alternatives | F/V/LT/IO outcomes plus full mappings in §§13–14 |
| 9 — consumers and migration/rebinding | exact five-consumer ledger §8 and migration questions §24 |
| 10 — explicit exclusions | inherited mandates §3, kernel §18 and counterexamples §20 |

## 12. Orthogonal semantic axes

### 12.1 Lifecycle location

| Outcome | Treatment | Burden |
|---|---|---|
| L0 | retain the bounded working lifecycle and keep OCP-004 Draft | snapshot replay and exact reopening trigger |
| L1 | complete lifecycle in OCP-004 | full state machine, transition authority, completeness and terminal rules without importing downstream authority |
| L2 | define a separate downstream non-Concept lifecycle contract | exact relocation, dependency direction, one current owner and human-readable cross-reference |

### 12.2 `Draft → Planned` completeness

| Outcome | Treatment | Boundary |
|---|---|---|
| G0 | retain the question unresolved under hold | no permissive default |
| G1 | OCP-004 owns a universal structural minimum; exact domain profiles may require more | domain sufficiency cannot weaken the Core minimum |
| G2 | the selected lifecycle owner defines the structural minimum and profile hook | OCP-004 still owns Operation identity and active-intent invariants |

Neither G1 nor G2 authorizes a domain profile merely by label or newest version.

### 12.3 Authorization evidence

| Outcome | Treatment | Boundary |
|---|---|---|
| A0 | retain opaque provenance with no complete acceptance owner | hold only; cannot support a stable `Authorized` promise |
| A1 | lifecycle owner validates one exact evidence envelope from a separately governed source | validates binding/traceability, not the external authorization mechanism |
| A2 | OCP-004 defines authorization source/mechanism | inadmissible in current mandate unless a later Board act explicitly reopens the exclusion |

### 12.4 Terminal Operation and unfinished Assignment

| Outcome | Treatment | Boundary |
|---|---|---|
| T0 | lifecycles remain independent and terminal alignment remains unresolved | hold only; no silent termination |
| T1 | lifecycle owner requires explicit alignment evidence or a named fail-safe disposition | no Assignment mutation; OCP-005 remains authoritative |
| T2 | Operation terminal transition automatically closes/revokes Assignment | inadmissible because it overrides OCP-005 ownership and AB-028's open question |

### 12.5 Composition and independent coordination

| Outcome | Treatment | Boundary |
|---|---|---|
| C0 | retain current acyclic/no-inheritance working rules under hold | exact graph semantics remain unresolved |
| C1 | OCP-004 owns parent/child composition only; independent coordination is external | shared intent/dependency criteria and dataset acyclicity must become exact |
| C2 | one downstream relationship contract owns both composition and coordination | must prove that part-whole and independent relations do not collapse |

### 12.6 Event relevance

| Outcome | Treatment | Graph consequence |
|---|---|---|
| E0 | preserve the `generates`/no-edge seam under hold | no change; cannot enter a stable promise |
| E1 | retire or narrow `generates`; keep explicit downstream relevance and no new edge | current graph remains `Operation → Objective` only |
| E2 | a downstream non-Concept relation contract owns exact Operation/Event relevance | no Concept edge unless separately proved; relation owner depends on both endpoints |
| E3 | make `Operation generates Event` a direct Concept dependency/edge | requires explicit edge semantics and resolution of the current OCP-010 → OCP-004 cycle consequence |

E1 is the no-new-edge baseline. E3 is not forbidden from comparison, but it cannot be implemented by prose or by deleting a dependency silently.

### 12.7 Cross-contract authority/dependency

| Outcome | Treatment | Risk |
|---|---|---|
| D1 | downstream defining owners depend on OCP-004; OCP-004 states only boundaries | weakest cycle risk; requires careful non-duplication |
| D2 | separate lifecycle/relation contracts depend on all exact endpoint owners | additional artifacts and coordinated versioning |
| D3 | OCP-004 directly depends on OCP-005/006/010/011 | immediate cycle/topology burden; inadmissible without a separate graph repair |

## 13. Record-form outcome axes

### 13.1 `ExplicitIntentRecord`

| Outcome | Treatment |
|---|---|
| F0 | retain current local form under hold; no P-001 conformance claim |
| F1 | keep an Operation-owned endpoint-free identified record and invoke exact P-001 |
| F2 | use only an inline Draft authoring value and migrate non-Draft use to exact Objective under AD-004's separately gated sunset |

F2 is not “rename the record.” It requires removal of independent `intent_id` semantics from the inline value and a proven migration for every accepted non-Draft explicit-intent snapshot.

### 13.2 Validation evidence

| Outcome | Treatment |
|---|---|
| V0 | retain current named evidence entries under hold; no P-001 conformance claim |
| V1 | define a separate endpoint-free identified validation-evidence family under exact P-001 |
| V2 | make evidence entries snapshot-local inline values with no independent address/history |
| V3 | move the evidence family to a separate validation contract with its own owner and exact reference back to intent version |

V2 is admissible only if `validation_id` ceases to be an independently resolvable identity. List order still cannot select evidence.

### 13.3 `LifecycleTransitionRecord`

| Outcome | Treatment |
|---|---|
| LT0 | retain incomplete working history under hold |
| LT1 | complete an Operation-owned P-001 Module B invocation in OCP-004 |
| LT2 | complete the same separate invocation in a downstream lifecycle contract |
| LT3 | retain only current-stage snapshot fields with no authoritative transition history |

LT3 loses current audit/replay intent and therefore carries a migration and governance burden; changing the name alone is not enough.

### 13.4 `InterOperationRelationshipAssertion`

| Outcome | Treatment |
|---|---|
| IO0 | retain the current incomplete assertion under hold |
| IO1 | define an Operation-owned exact P-001 identified assertion |
| IO2 | define a snapshot-local inline direct relation with no independent identity, effectivity, history or supersession |
| IO3 | move a complete identified relation family to a downstream non-Concept Coordination/relationship contract |

IO2 must remove independent record semantics and explain why endpoint/provenance-bearing nested data is not separately addressable. IO3 cannot infer a Coordination Concept or authority from the current Proposed registry label.

## 14. Full candidate P-001 invocation mappings

Every candidate below is a separate invocation decision. A future artifact may carry one metadata value `Uses-Patterns: P-001@0.1.0`, but it must publish an independent conformance statement for each selected family.

### 14.1 F1 — OperationExplicitIntentRecord

| P-001 obligation | Candidate mapping |
|---|---|
| exact version | `P-001@0.1.0`; invoking owner is OCP-004 |
| stable identity | non-empty `intent_id`; `intent_version_ref` identifies immutable content version, not a newest winner |
| semantic owner | OCP-004 intent surface; P-001 supplies form only |
| endpoints | explicitly endpoint-free; owning `operation_id` is containment context, not a second Concept endpoint |
| governed kind | one fixed `operation-explicit-intent@1`; no free kind field is required |
| provenance | add exact immutable authoring provenance; validation evidence is not authorization provenance |
| validation | exact statement/rule/input binding, exclusive active branch and fail-safe evidence |
| authority | exact active Operation snapshot plus immutable version/evidence; timestamp/order/count cannot elect authority |
| modules | none unless a later outcome adds temporal effectivity, transitions or supersession explicitly |

### 14.2 V1 — OperationIntentValidationEvidenceRecord

| P-001 obligation | Candidate mapping |
|---|---|
| exact version | separate family conformance under `P-001@0.1.0`; invoking owner is OCP-004 or the exact V3 contract |
| stable identity | non-empty `validation_id` |
| semantic owner | exact intent-validation contract, not P-001 or the evaluator |
| endpoints | endpoint-free assertion with exact references to intent version, rule version and input snapshot |
| governed kind | one fixed `operation-intent-validation@1` |
| provenance | `evaluator_ref`, `evaluated_at` and a named immutable provenance requirement; evaluator identity alone grants no authority |
| validation | exact binding, allowed result, structural validity, conflict detection and fail-safe projection |
| authority | all structurally valid exact-binding records form the evidence set; no newest/order/count winner |
| modules | none; `evaluated_at` is occurrence time, not temporal effectivity |

### 14.3 LT1/LT2 — OperationLifecycleTransitionRecord

| P-001 obligation | Candidate mapping |
|---|---|
| exact version | separate family conformance under `P-001@0.1.0`; owner is OCP-004 for LT1 or the exact lifecycle artifact for LT2 |
| stable identity | add non-empty `transition_id` unique in the lifecycle model |
| semantic owner | selected lifecycle owner defines stages, paths and transition meaning |
| endpoints | one exact `operation_ref`; source/target stages are governed values, not Concept endpoints |
| governed kind | one fixed `operation-lifecycle-transition@1` |
| provenance | exact non-empty provenance envelope with source-owner boundary; no label-only authorization |
| validation | allowed path, unique IDs, complete history, deterministic projection, ordered-time rule and invalid-branch rejection |
| authority | transition history is authoritative; materialized `lifecycle_stage` is a checked projection |
| modules | Module B; no A or C unless later fields actually introduce effectivity or supersession |

### 14.4 IO1/IO3 — InterOperationRelationshipRecord

| P-001 obligation | Candidate mapping |
|---|---|
| exact version | separate family conformance under `P-001@0.1.0`; owner is OCP-004 for IO1 or the exact downstream contract for IO3 |
| stable identity | add non-empty `relationship_id` unique in the owning model |
| semantic owner | selected relationship owner defines each relation meaning; P-001 does not |
| endpoints | exact directed `source_operation_ref` and `target_operation_ref`, each resolving once; reflexivity rules explicit |
| governed kind | exact versioned `relationship_kind_ref` with one legitimate owner; current free enum is insufficient as external authority |
| provenance | exact establishment provenance; source count or label does not authorize the relation |
| validation | endpoint resolution, allowed direction/reflexivity, duplicate identity and kind-specific invariants |
| authority | exact stored record is authoritative for its assertion; no derived/newest/current-head winner |
| modules | none for the minimum current form; Module A/B/C becomes mandatory only if the selected outcome adds effectivity, lifecycle or supersession |

For every selected invocation, repository `track-current` means the invoking artifact binds the current exact Pattern version. A future P-001 version change must update all then-current invokers atomically and explicitly classify immutable reviewed snapshots. AD-020 changes neither the six current invokers nor their historical snapshots.

## 15. Common comparison axes

External review and the later Board act must compare every complete outcome on:

1. human readability and number of normative owners;
2. exact Operation identity preservation;
3. lifecycle completeness and projection determinism;
4. authorization-evidence honesty;
5. Assignment/Constraint/Event/assessment authority preservation;
6. graph acyclicity and dependency direction;
7. composition/coordination non-collapse;
8. P-001 completeness per record family;
9. fail-safe handling of unknown/conflicting evidence;
10. consumer migration and exact historical replay;
11. current data/schema impact and reversibility;
12. checker/fixture coverage versus human-only obligations;
13. explicit exclusions and backlog preservation; and
14. ability to state a bounded `1.x` compatibility promise without concealed B items.

## 16. Preliminary layout comparison

| Layout | Strongest evidence | Main unresolved burden | Preliminary disposition |
|---|---|---|---|
| H0 | maximally reversible; honest when any owner is unknown | leaves all current B items and blocks T5 | mandatory fail-safe |
| H1 | one place to read and version; no relocation | large mixed responsibility and risk of importing downstream authority | viable, high concentration risk |
| H2 | one owner plus readable internal boundary; minimal cross-file migration | both surfaces must become complete; headings cannot solve owner gaps | viable |
| H3 | follows current promise of a separate lifecycle contract; avoids OCP-004 → downstream cycles | lifecycle fragmentation, transition migration and exact cross-reference burden | leading layout hypothesis |
| H4 | clearest separation of lifecycle and coordination meanings | most artifacts, most rebinding and greatest human navigation cost | viable only if H3 cannot bound coordination honestly |

No score, option order, consumer count or AD-016V recommendation chooses this table.

## 17. Provisional combined hypothesis — Q3

The current evidence makes the following combination the leading hypothesis for attack, not an accepted result:

```text
Q3 := H3 + L2 + G2 + A1 + T1 + C1 + E1 + D1
      + F1 + V1 + LT2 + IO3
```

Under Q3:

- OCP-004 keeps the Operation identity/context kernel, Objective/intent boundary, temporal/spatial context, parent/child semantics and all cross-contract non-implications;
- one downstream non-Concept lifecycle contract owns stages, structural completeness, exact authorization-evidence acceptance, authoritative transition history and explicit terminal-alignment evidence;
- OCP-004 owns parent/child composition, while a future downstream contract owns independently coordinated inter-operation relations;
- `Operation generates Event` is removed or narrowed out of the stable kernel; Event relevance remains explicit and downstream with no new Concept edge;
- participation, applicability, Event occurrence and assessment keep their current downstream owners and dependency direction;
- retained independently identified intent and validation evidence families each receive separate exact P-001 conformance;
- lifecycle transitions receive Module B under the lifecycle owner; and
- an identified inter-operation record, if retained, belongs to the downstream relationship owner and receives its own P-001 conformance.

Q3 is attractive because it follows the current downstream dependency direction, makes the Event seam explicit and gives history-bearing structures honest form. Its principal risk is fragmentation: four normative locations could make one Operation lifecycle harder for a person to understand, and IO3 currently lacks a separately accepted Coordination owner. If the later Board cannot name finite artifacts and one owner per statement, Q3 fails to H2 or H0.

## 18. Provisional kernel retained by every positive outcome

Every positive outcome must preserve at least these guarantees:

1. one exact stable `operation_id` identifies one purposeful activity;
2. name, template, classification, repeated shape, participants, spatial payload, lifecycle stage, Event and outcome do not define that identity;
3. outside `Draft`, exactly one active intent branch exists until AD-004 is separately changed;
4. each `objective_ref` exact-resolves to one OCP-008 Objective and list membership implies no priority, hierarchy or achievement;
5. missing/stale/conflicting explicit-intent evidence never becomes `passed`;
6. planned and actual temporal statements remain distinct;
7. AD-014 local spatial-binding identity and fail-safe semantics remain exact;
8. Assignment alone owns authoritative participation; no composition inheritance exists;
9. Constraint alone owns applicability/evaluation semantics;
10. parent/child and independent coordination remain distinct;
11. Event occurrence and Operation lifecycle identities remain distinct;
12. completion never establishes Objective achievement;
13. authorization evidence never becomes authorization by label, timestamp, order or count;
14. no Readiness, State, availability, interchangeability or production authority is inferred; and
15. every current/historical exact reference remains replayable or receives an explicit migration.

The later Board act may refine this list. It may not silently weaken it.

## 19. Mandatory human scenarios

Every positive combined outcome must give a readable deterministic treatment for:

1. two separately created Operation with the same template, Objective, participants and spatial payload;
2. one Draft Operation with neither active intent branch;
3. one Planned Operation with two exact Objective references;
4. one non-Draft Operation with both intent branches;
5. one explicit-intent snapshot with stale validation evidence;
6. two exact-binding validation records with conflicting results and different times;
7. an explicit-intent change reusing the old version token;
8. a `Draft → Planned` candidate that meets Core structure but fails a domain profile;
9. a Planned candidate whose domain profile has zero, two or incomparable owners;
10. an `Authorized` candidate with a non-empty but ownerless provenance label;
11. an authorization evidence envelope with exact binding but no claim that the lifecycle contract grants permission;
12. an Active Operation with one not-yet-effective Assignment;
13. a Completed Operation with an effective unfinished Assignment;
14. a terminal Operation where the selected alignment evidence is missing or conflicting;
15. a parent Operation and child Operation with no inherited Assignment;
16. a self-parent and a three-Operation composition cycle;
17. two independent Operation that coordinate but share no parent/child relation;
18. two Operation that overlap in time/space but have no coordination assertion;
19. an independently identified Event relevant to zero Operation;
20. one Event relevant to several Operation without an Event identity change;
21. an Operation lifecycle transition for which no Event exists;
22. a Completed Operation with an `indeterminate` assessment;
23. a Constraint that blocks one transition without becoming a lifecycle stage;
24. one relationship kind with zero or multiple legitimate owners;
25. a relation assertion whose endpoint resolves to zero or multiple Operation;
26. one current transition history with duplicate transition IDs or invalid branching;
27. a historical Operation reference before and after a form migration;
28. a consumer that still expects an exact Operation identity after lifecycle extraction;
29. a local spatial binding proposed as an inter-operation relation; and
30. a Capability/Readiness or Resource-interchangeability inference proposed from Operation context.

All scenarios remain synthetic and non-sensitive.

## 20. Mandatory counterexamples

External review and the later Board act must reject these conclusions:

1. Operation is the only remaining candidate whose L2 floor passes, therefore it must become Canonical.
2. AD-016V selected discovery, therefore Q3 or any semantic answer is authorized.
3. A section is long or called “working,” therefore it may sit outside the compatibility promise without classification.
4. One file automatically means one semantic owner; multiple files automatically mean clean ownership.
5. `Operation generates Event` creates a graph edge even though metadata and §14 deny one.
6. Deleting `generates` proves that Event is irrelevant to Operation.
7. Event depends on Operation, therefore Operation may depend on Event without a cycle.
8. A lifecycle transition is an Event because both have occurrence time and provenance.
9. Completed means Objective achieved, successful, ready or admissible.
10. An effective Assignment authorizes Operation or must terminate automatically with it.
11. Parent/child composition propagates Assignment, Constraint, spatial binding, outcome or authorization.
12. Time or space overlap creates coordination, conflict or parent/child.
13. A non-empty `provenance_ref` proves a legitimate authorization source.
14. Order is Proposed, therefore it is the mandatory authorization mechanism.
15. Domain validation success authorizes a lifecycle transition.
16. The checker accepts a Planned fixture, therefore minimum Planned completeness is complete.
17. `Record` in a name automatically invokes P-001.
18. Removing `Record` or an ID automatically avoids P-001 applicability.
19. Four record-like structures justify one shared record family or one shared invocation.
20. P-001 supplies Operation stages, relationship kinds, authorization or validation meaning.
21. `evaluated_at` makes validation evidence temporally effective under Module A.
22. A version reference silently creates Module C supersession.
23. Newest transition, validation, relationship or provenance wins a conflict.
24. More validators, issuers, consumers or records make one assertion authoritative.
25. A fixed list order defines the active intent, lifecycle head or relation.
26. Local spatial `binding_id` is reusable record identity or evidence for F1/V1/LT2/IO3.
27. Coordination profile ownership authorizes an Operation or caller.
28. Equal Capability claims make Resources interchangeable in an Operation.
29. Organization identity, label or membership creates participation or authority.
30. Discovery approval resolves any named AB item.
31. Green CI selects Q3 or proves semantic completeness.
32. Authorization for AD-016V transfers to AD-020, AD-020A, remediation or lifecycle.

## 21. Unconditional evidence obligations

These obligations apply to H0–H4 and every semantic/form combination:

1. exact-anchor the then-current baseline and every comparison input;
2. account for every current OCP-004 section and field without silent deletion;
3. preserve the §18 kernel or identify a concrete contradiction and stop;
4. reproduce the exact five-consumer sweep and classify every changed binding;
5. name one defining owner for every lifecycle, composition, relevance, record and projection rule—or retain hold;
6. preserve the acyclic no-new-edge baseline unless a separate topology burden is satisfied explicitly;
7. preserve Assignment, Constraint, Event and assessment authority without formula duplication;
8. classify each record-like structure independently against P-001;
9. preserve fail-safe evidence and forbid timestamp/order/count authority;
10. provide human scenarios, counterexamples, migration and rollback;
11. distinguish checker-enforced rules from review-only semantic obligations;
12. preserve all explicit exclusions and exact OCP-009/Capability boundaries; and
13. require a separate Board selection before any OCP, Pattern, dependency, fixture or schema edit.

No unconditional fixture may require lifecycle extraction, in-place completion, a new edge, a P-001 invocation or a Coordination owner. At least one admissible outcome rejects each mechanism.

## 22. Layout-conditional evidence and equivalents

| Layout | Conditional evidence | Equivalent for shared guarantees |
|---|---|---|
| H0 | byte-exact snapshot replay, named unresolved owners and concrete reopening trigger | unchanged data/reference behavior replaces migration evidence |
| H1 | one complete rule/field ledger with no downstream-authority duplication | single complete owner replaces relocation evidence |
| H2 | two normative surface ledgers, no overlap and one OCP-004 owner | explicit internal boundary replaces cross-artifact dependencies |
| H3 | lifecycle relocation ledger, exact wrapper/dependencies, historical replay and atomic rollback | one downstream lifecycle owner replaces in-place lifecycle completeness |
| H4 | separate lifecycle and relationship relocation ledgers, two exact owners and no duplicated prose | exact owner resolution replaces a one-file contract |

Outcome fairness fails if H0 must fabricate a new layer, H1/H2 are required to prove extraction mechanics, or H3/H4 are allowed to leave copied current prose authoritative in OCP-004.

## 23. Form-conditional evidence and equivalents

| Form outcome | Conditional evidence | Required equivalent |
|---|---|---|
| F0/V0/LT0/IO0 | exact current replay and unresolved-classification stop | no conformance claim or silent stabilization |
| F1/V1/LT1/LT2/IO1/IO3 | complete §14 family-specific mapping, exact metadata owner, positive and material negative fixtures | P-001 conformance replaces the rejected inline explanation |
| F2 | complete explicit-intent-to-Objective migration and historical replay | Objective exact identity replaces local intent-record identity |
| V2 | no independently resolvable `validation_id`, exact parent-snapshot binding and conflict-safe set evaluation | parent snapshot identity replaces record identity |
| V3 | exact owner, moved family, reference/authority mapping and rollback | one external evidence owner replaces local storage |
| LT3 | explicit rejection of authoritative transition history plus projection/migration semantics | snapshot authority replaces history replay; lost audit claims must be removed |
| IO2 | no record ID/effectivity/history/supersession, exact nested scope and endpoint/provenance rules | owning Operation snapshot replaces record identity |

An invoking outcome cannot satisfy its burden with the non-invoking equivalent, and a non-invoking outcome cannot retain independent record semantics while citing storage locality.

## 24. Migration and rollback questions

The later Board act must answer at least:

1. Does the selected surface change any current Operation identity or exact reference? The default answer is no.
2. Does an in-place split change only document ownership, or also serialized field meaning?
3. Which current lifecycle fields/records move, and can old snapshots replay without newest-version redirect?
4. Does adding `transition_id`, `operation_ref`, record provenance or governed kind require data backfill? Unknown values must not be invented.
5. Does F2 invalidate accepted non-Draft explicit-intent Operations, and what exact migration preserves intent/audit history?
6. Can V2 remove `validation_id` without losing deduplication or historical evidence references?
7. Can IO2 remain nested without an external consumer referencing the assertion independently?
8. Which five consumers require semantic change, reference rebinding, status-only accounting or no change?
9. Does any candidate require OCP-010 dependency removal or a new edge? That requires its own exact migration/topology act.
10. Can rollback restore the prior owners, metadata, data interpretation and historical references atomically?

No migration may synthesize authorization, provenance, record identity, relationship kind or evidence from timestamps, order or counts.

## 25. Falsification targets

Attempt to demonstrate each of the following before selection:

1. the exact baseline or five-consumer set is wrong;
2. a sixth primary OCP-004 consumer exists;
3. the candidate kernel loses an accepted identity or non-implication guarantee;
4. one B item can enter a stable surface without a legitimate owner;
5. H1 necessarily creates an OCP dependency cycle;
6. H2 cannot distinguish its two surfaces normatively;
7. H3 cannot state lifecycle rules without duplicating Operation identity;
8. H4 creates more than one current owner for a relationship statement;
9. H0 cannot replay a current accepted Operation snapshot;
10. `Draft → Planned` has one existing complete authoritative rule that the discovery omitted;
11. a current accepted contract names the mandatory Operation authorization source;
12. terminal Assignment alignment is already complete and uniquely owned;
13. parent/child and independent coordination are semantically inseparable;
14. `Operation generates Event` already has an exact non-cyclic owner and edge;
15. E1 loses a current consumer-required Event guarantee;
16. E3 can be added without dependency reversal, cycle or Event semantic change;
17. D1 duplicates a downstream authoritative formula in OCP-004;
18. one record-form classification is inferred only from its name or storage location;
19. F1 lacks a P-001 Required Element or secretly needs a module;
20. V1 lacks a P-001 Required Element or evaluator identity is treated as authority;
21. LT1/LT2 omits a Module B obligation;
22. IO1/IO3 lacks a legitimate relationship-kind owner;
23. F2/V2/LT3/IO2 retains independent identity/history despite claiming inline form;
24. one proposed invocation requires a P-001 version change rather than exact `0.1.0` use;
25. a current invoker or reviewed snapshot would be silently changed;
26. one consumer requires migration omitted by the selected layout;
27. the checker proves a semantic claim beyond its finite implementation;
28. evidence obligations assume a layer rejected by the selected outcome;
29. a proposed result introduces a forbidden Concept, edge, authority or production schema; or
30. Q3 remains preferred only because AD-016V selected Operation discovery or because split contracts look architecturally tidy.

One demonstrated target stops selection or forces an explicit revised outcome. “Not demonstrated” means only that the attack failed on the exact evidence; it does not mean impossible.

## 26. Preliminary recommendation

AD-020 recommends that a separate `AD-020A` Board act compare all complete outcomes and attack Q3 first, with H2 as the strongest in-place alternative and H0 as the mandatory fail-safe.

The evidence favoring Q3 is concrete but incomplete:

- OCP-004 itself already promises a separate lifecycle contract;
- current dependency direction keeps downstream owners dependent on Operation and avoids cycles;
- Event's own contract supports independent occurrence, zero/one/many relevance and no current edge;
- history/evidence-bearing local structures expose real P-001 applicability questions; and
- lifecycle and inter-operation coordination have different owners and failure modes.

The evidence against premature Q3 selection is equally material:

- no accepted standalone lifecycle or Coordination artifact yet exists;
- four P-001 family mappings could create excessive ceremony or migration;
- explicit intent remains under AD-004's sequenced sunset rather than a permanent-form decision; and
- a person must still be able to understand one Operation without reconstructing semantics from several documents.

Therefore Q3 is a falsifiable leading hypothesis only. If its owners, artifacts or migration cannot be named exactly, the later act must select H2 or H0 rather than infer missing structure.

## 27. Exit criteria and mandatory next Board act

AD-020 is ready for Board comparison only when external review confirms that:

1. the baseline anchors and five-consumer sweep reproduce;
2. all OCP-004 sections and record-like fields are accounted for;
3. H0–H4 are distinct, complete and outcome-fair;
4. all ten AD-016V §233 axes appear explicitly;
5. hold, in-place and split-authority outcomes each have real evidence;
6. every P-001-invoking candidate has a complete separate mapping and track-current treatment;
7. every non-invoking candidate explains the absence of independent record semantics;
8. the Event seam and graph consequences are explicit under E0–E3;
9. migration, rollback and consumer burdens are outcome-specific;
10. all scenarios, counterexamples and thirty falsification targets are reviewable;
11. no Operation backlog item is marked resolved; and
12. no semantic answer, OCP edit or merge authority is implied.

The next act must be separate, for example:

```text
AD-020A — Compare and Select the Operation Stable-Surface Outcome
```

AD-020A must re-anchor then-current `main`, adjudicate every falsification target and external finding, compare complete combinations rather than layout names alone, and select exactly one governed result or explicit hold. It may authorize preparation of a later remediation; it may not implement that remediation in the same selection act.

Any later remediation, lifecycle contract, P-001 invocation, dependency/edge change or lifecycle proposal receives its own exact-head external review, Codex adjudication, green CI and fresh Pavlo/Architecture Board authorization.

## 28. Discovery status and accounting

While this document is `0.1.0 / Discovery`:

- OCP-004 remains `0.8.3 / Draft` and Operation remains `Accepted`;
- the current Concept graph remains unchanged;
- OCP-004 continues to invoke no Pattern;
- P-001 remains `0.1.0 / Accepted` with all six current primary invokers unchanged;
- all five OCP-004 consumers, 120 fixtures and 172 tests remain read-only evidence;
- AB-015, AB-016, AB-017, AB-019, AB-020, AB-023 and AB-028 remain Open or Deferred exactly as before;
- AB-062 remains `Planned`;
- foundation readiness remains approximately 71%; and
- no data, reference, record, projection, checker rule, schema or production authority changes.

Merge of this discovery, if separately reviewed and authorized, records only the comparison space and evidence obligations. It cannot select Q3, create AD-020A, edit OCP-004, invoke P-001, add/remove an edge, resolve a backlog item or authorize any downstream merge.

## 29. AD-020A Board question and exact baseline

AD-020A decides whether the reviewed discovery supports one complete Operation stable-surface remediation direction. It does not perform that remediation, edit OCP-004, create a lifecycle document, invoke P-001, change the Concept graph or resolve an Operation backlog item.

The exact decision baseline is `main@cb9cf0bdcf4db812e917df2f7769127be8e5cc12`, tree `b3dda9d8dc7ee5fd38c88ffd3b168f9799c6c443`. On that baseline:

- AD-020 is `0.1.0 / Discovery`, blob `3266f047dadb7bc1febd4c814f948ed73bac5295`, SHA-256 `fc76ba840860261f5f7aa27470870edd38d6cf78ac4dd5090893e68cb863d5b2`;
- the current README projection is blob `96089f6fdcf4e60a0a44aba7974415059e71f0e8`, SHA-256 `aa0081d29d53284fb9c23a891f28ca3c1391987ba4f873b1a16667c1fde6514d`;
- the architecture backlog is blob `859c98c1599e913ebedcf4d48574637887b64e1e`, SHA-256 `88a592330a7accf7e2d51dc49c7fd31e7174deb6c4118b3eda82dea297943ab5`;
- the roadmap is blob `567a5b01afdbd7424ceaacefef7de4ab89cf4a4a`, SHA-256 `a0c1e6fed773ec640b68ff4bf342e717011ed92fd6ca862ea70b8f082b71ae00`;
- every semantic and executable anchor in §2 remains byte-identical to the discovery baseline;
- OCP-004 remains blob `6f6990ed2cef7887af663e7dc806b34bddca6e30`, SHA-256 `aa81d60ef8c9802f40f488390d151b5f6c50d116ece6576c1783da0e48087033`;
- P-001 remains blob `f1e95efa055022a9342b16133bf7b3c3db90fa4f`, SHA-256 `cf6fb3501a1a5504aa873c372e97436813725c6e44a7fc682a2db404a7d97b82`;
- a fresh frontmatter scan of all seventeen primary OCP documents again yields exactly five direct OCP-004 consumers: OCP-005, OCP-006, OCP-010, OCP-011 and OCP-014; and
- OCP-004 remains `0.8.3 / Draft`, Operation remains `Accepted`, the graph remains unchanged, P-001 has six current primary invoking contracts on this baseline, and no OCP-017 artifact exists.

Fable externally reviewed discovery head `33aebc9b5dfc0c9778e22dcd9e37d14177bd70cf` and approved iteration 2/5 with no open findings after the `Applies-To` acceptance path was made executable. The authorized discovery squash-merged as `cb9cf0bdcf4db812e917df2f7769127be8e5cc12`; its tree is byte-identical to the reviewed head, CI succeeded, and the post-merge runs returned 172/172 unit tests plus 120/120 fixtures in both contexts.

The Board question is narrow: **does one complete H0–H4/semantic/form combination survive all thirty attacks strongly enough to authorize preparation of a bounded remediation, or must the result remain H0?** The preliminary Q3 label, authoring effort, review approval, option order, readiness estimate, hashes and green CI are evidence inputs or controls; none is selection authority.

## 30. Board treatment of the discovery

AD-020A accepts the discovery with the following adjudications.

1. **The fifteen-guarantee kernel is retained.** No evidence contradicts §18, and no selected rule may weaken it by relocation or omission.
2. **The five-consumer baseline is complete for the current tree.** A later OCP-017 would become a new sixth consumer by explicit creation; it is not evidence that the baseline scan missed one.
3. **H0, H1, H2, H3 and H4 are materially distinct.** Their differences are authority placement, dependency direction, migration burden and record form—not merely file count.
4. **The provisional Q3 is not internally complete.** H3 promises one separate lifecycle authority while independent coordination stays separately bounded, but Q3 also selects IO3 and therefore requires a second separate relationship authority. As written, Q3 crosses into H4 without naming that owner.
5. **Falsification target 22 succeeds against provisional Q3.** The current free relation enum points only to a future Coordination Model; no exact accepted relationship-kind owner or contract exists. That result defeats Q3 as written rather than defeating all split-lifecycle outcomes.
6. **A revised H3 combination remains viable.** Keeping inter-operation relations as bounded IO2 values under OCP-004 removes the unowned IO3 extraction while preserving the lifecycle split. The revised combination is named Q3I so that the change cannot be mistaken for discovery momentum.
7. **P-001 is applicable per family, not per file or suffix.** F1, V1 and LT2 retain independent identity/evidence/history and therefore require three separate conformance statements. IO2 rejects independent identity, effectivity, lifecycle and supersession and therefore supplies the non-invoking equivalent instead.
8. **P-001's evidence ledger is a named implementation risk.** Its §13 says “six current primary invokers,” while §16 frames that ledger as evidence for the T3 acceptance act and §13 denies registry status. AD-020A does not amend or reinterpret P-001 silently; §42 makes truthful treatment of that prose a non-waivable stop.
9. **The Event seam is resolved only to E1.** OCP-010 §10 already supplies independent identity, zero/one/many relevance and no current edge. The stable Operation surface can retire `generates` without denying relevance.
10. **Selection remains preparation-only.** None of these adjudications changes a current document, runtime object, Pattern invocation, dependency or status outside AD-020 itself.

## 31. Complete-combination comparison

Each row below supplies every §11 axis. A layout name without the rest of the row is not an outcome.

| Candidate | Complete combination | Human-readable ownership | Board disposition |
|---|---|---|---|
| Q0 | `H0 + L0 + G0 + A0 + T0 + C0 + E0 + D1 + F0 + V0 + LT0 + IO0` | current OCP-004 remains the bounded working owner; every B item stays explicitly unresolved | admissible fail-safe; not selected because exact owners can be bounded without inventing semantic facts |
| Q1 | `H1 + L1 + G1 + A1 + T1 + C1 + E1 + D1 + F1 + V1 + LT1 + IO1` | OCP-004 owns identity, lifecycle, composition and identified local relationships; downstream contracts retain participation, applicability, occurrence and assessment | coherent but rejected: one document would accumulate four P-001 families plus lifecycle, authorization-evidence and terminal-alignment obligations |
| Q2 | `H2 + L1 + G1 + A1 + T1 + C1 + E1 + D1 + F1 + V1 + LT1 + IO2` | one OCP-004 owner with separate identity/context and lifecycle/support surfaces | strongest in-place alternative; rejected because the promised separate lifecycle contract and transition-history burden have concrete evidence, not merely editorial separation needs |
| Q3 | `H3 + L2 + G2 + A1 + T1 + C1 + E1 + D1 + F1 + V1 + LT2 + IO3` | lifecycle would move, and an unnamed future owner would also receive identified inter-operation relations | rejected as written: IO3 turns H3 into an unnamed H4-like split and target 22 succeeds |
| Q3I | `H3 + L2 + G2 + A1 + T1 + C1 + E1 + D2 + F1 + V1 + LT2 + IO2` | OCP-004 owns the stable Operation kernel, composition and bounded inline relation values; one Route C lifecycle contract owns lifecycle and transition history | **selected for remediation preparation**; it repairs Q3's owner gap while keeping one readable Operation document and one separately readable lifecycle owner |
| Q4 | `H4 + L2 + G2 + A1 + T1 + C1 + E2 + D2 + F1 + V1 + LT2 + IO3` | OCP-004 plus separate Board-owned Route C lifecycle and Operation-relationship/relevance contracts, each depending on its exact endpoints | coherent if the second contract defines the legitimate relationship-kind owner; rejected now because no consumer or record-history requirement justifies that extraction and migration cost |

Q0 remains the immediate fallback. Q1 remains the concentration alternative, Q2 the in-place alternative and Q4 the extraction alternative. Q3 is retained as a falsified historical hypothesis; Q3I is not a silent relabeling of it.

## 32. Board disposition of the discovery ledgers

### 32.1 OCP-004 section disposition

| Current section | AD-020A disposition |
|---|---|
| §§1–3 | retain the exact identified purposeful activity, scope and specialization exclusions in OCP-004 |
| §4 | retain current Concept status/dependency reporting; replace any relationship prose that overstates a Concept edge |
| §5 | retain exact Operation identity independence in OCP-004 |
| §6 | retain the readable context decomposition only after lifecycle and relationship ownership match §§35–37 |
| §7 | retain the exclusive active-intent invariant; complete F1 and V1 as separate OCP-004 P-001 families without changing AD-004's sunset gate |
| §8 | retain planned/actual temporal separation as Operation-owned context |
| §9 | retain AD-014 local spatial bindings byte-semantically; they remain inline, non-reusable and outside P-001 |
| §10 | retain only the OCP-005 participation boundary and no-inheritance rules; no Assignment formula is copied |
| §11.1 | retain pursuit/Assignment/Constraint boundary vocabulary; remove `Operation generates Event` from the stable relation list under E1 |
| §11.2 | replace the future-owner placeholder with the exact IO2 local-value envelope in §37; OCP-004 owns only that bounded assertion vocabulary |
| §11.3 | move authorization-evidence acceptance to OCP-017 under A1; OCP-004 keeps the statement that authorization source/mechanism is external |
| §12 | complete parent/child composition in OCP-004 under C1; independent coordination, shared time/space and participation inheritance remain excluded |
| §13 | move stage vocabulary, paths, completeness, transition history, authorization-evidence acceptance and terminal alignment to OCP-017; OCP-004 keeps one readable cross-reference and non-implications |
| §14 | retain Event/assessment identity and completion non-implications; state E1 downstream relevance and no new edge positively |
| §§15–17 | retain Operation identity/context rules; relocate lifecycle rules to OCP-017 and remove any duplicate current owner |
| §§18–19 | retain human examples/non-examples as evidence after updating them to the selected owners |
| §§20–21 | keep every named Operation question and exclusion visible; selection resolves none of their backlog statuses |
| §§22–24 | retain as historical PATCH accounting; they do not become current semantic owners |

Every current B item is assigned to OCP-004, OCP-017, an exact downstream owner or an explicit exclusion. The remediation may not hide one in an example, checker rule or “future work” paragraph.

### 32.2 Structure and field disposition

| Structure / field group | Selected treatment |
|---|---|
| `operation_id` | OCP-004 stable Concept identity; never changed or redirected by lifecycle extraction |
| `objective_refs` | exact OCP-008 references and affirmative pursuit semantics remain OCP-004-owned |
| `ExplicitIntentRecord` | F1 endpoint-free identified family under OCP-004 and exact P-001; AD-004 sunset remains separate |
| validation evidence | V1 endpoint-free identified evidence family under OCP-004 and a separate exact P-001 mapping; evaluator identity is not authority |
| planned/actual temporal context | OCP-004 inline context, with no shared Time Concept |
| local spatial binding | unchanged AD-014 inline value; never reused as a relationship or P-001 identity |
| Assignment participation | OCP-005 remains the only authoritative owner |
| Constraint applicability | OCP-006 remains the only authoritative owner |
| parent/child | OCP-004 C1 composition with exact acyclicity and no inherited Assignment, Constraint, context, outcome or authorization |
| inter-operation assertion | IO2 nested value in the exact owning Operation snapshot under §37; no independent record identity/history |
| `lifecycle_stage` | optional checked projection from OCP-017 history, not an OCP-004 authority |
| lifecycle transition | LT2 identified record under OCP-017 and P-001 Module B |
| Event relevance | E1 explicit downstream reference/relation, no `Operation → Event` Concept edge and no automatic Event generation |
| outcome assessment | unchanged external OCP-011 record; never an Operation lifecycle projection |

## 33. Commissioned falsification closure

AD-020A re-attempts all thirty §25 targets against the exact baseline and complete combinations:

| # | Exact evidence rechecked | Board result |
|---:|---|---|
| 1 | commit/tree, §2 objects and frontmatter scan | baseline and five-consumer set reproduce; error not demonstrated |
| 2 | all seventeen primary OCP `Depends-On` fields | no sixth current consumer exists; future OCP-017 would be an explicit new consumer |
| 3 | §18 against Q3I §§35–37 | all fifteen guarantees remain explicit; loss not demonstrated |
| 4 | §32 owner ledger | every B statement has one proposed owner or exclusion; any unassigned statement is a remediation stop |
| 5 | Q1 dependency sketch | in-place completion need not create a cycle; attack fails, though concentration cost remains |
| 6 | Q2 two-surface ledger | identity/context and lifecycle/support can be stated distinctly; attack fails |
| 7 | Q3I OCP-004/OCP-017 split | lifecycle rules refer to exact Operation identity without redefining it; attack fails |
| 8 | Q4 relocation rule | two extracted contracts need not duplicate one relation statement; attack fails conditionally, but owner/migration burden remains |
| 9 | current fixtures and exact historical references | H0 replays current snapshots byte-exactly; attack fails |
| 10 | OCP-004 §§13, 15 and 20 | no complete authoritative `Draft → Planned` rule exists |
| 11 | OCP-004 §11.3 and repository owner sweep | no accepted mandatory Operation authorization source exists |
| 12 | OCP-004/OCP-005 terminal rules and AB-028 | terminal alignment remains incomplete and not uniquely owned |
| 13 | OCP-004 §§11.2 and 12 | composition and independent coordination are distinguishable; attack fails |
| 14 | OCP-004 §11.1 versus §14 and OCP-010 §10 | `generates` has no exact non-cyclic current owner or edge |
| 15 | all five consumers plus OCP-010 §10 | no consumer-required generation guarantee is lost by E1 |
| 16 | OCP-010 → OCP-004 dependency and current graph | a direct reverse Concept dependency would introduce topology/semantic work; easy E3 addition is not demonstrated |
| 17 | Q1/Q2 D1 ledgers | OCP-004 can state boundaries without copying downstream formulas; duplication is not necessary |
| 18 | all four field ledgers and P-001 applicability | classification follows identity/effectivity/history properties, not names or storage |
| 19 | §14.1 versus P-001 §§4–8 | F1 maps all seven Required Elements and selects no unsupported module |
| 20 | §14.2 versus P-001 §§4–8 | V1 maps all elements; evaluator/time/order/count never elect authority |
| 21 | §14.3 versus P-001 Module B | LT2 includes transition identity, operation reference, paths, ordered history, projections and branch rejection |
| 22 | current free enum, owner sweep and provisional Q3 | **demonstrated against Q3/IO3**: no legitimate exact relationship-kind owner is named; Q3 is rejected and Q3I selects IO2 |
| 23 | Q3I IO2 envelope | no relationship ID, independent reference, effectivity, history or supersession remains; appearance of one reopens IO3 |
| 24 | P-001 `0.1.0` §§4–8 and §12 | selected families require no new Pattern obligation or module; exact `0.1.0` use is sufficient, subject to the §42 ledger stop |
| 25 | six current invokers and three immutable snapshots | selection changes none; future remediation must preserve their exact bindings and cannot rewrite snapshots |
| 26 | OCP-005/006/010/011/014 contracts | no Operation identity rebinding is required; lifecycle evidence dependencies and historical wrappers still require explicit accounting |
| 27 | checker implementation versus §§8.2–8.3 | checker proves only the finite structural subset; no semantic overclaim is accepted |
| 28 | §§21–23 obligations by Q0/Q1/Q2/Q3I/Q4 | each rejected layer has an explicit replay or owner equivalent; outcome-fairness failure not demonstrated |
| 29 | Q3I route, graph and exclusions | it adds no Concept, Concept edge, authorization source, Organization holder or production schema in this act |
| 30 | counterfactual comparison Q0/Q1/Q2/Q4 | original Q3 fails despite being recommended; Q3I wins on named owner and bounded migration evidence, not momentum or aesthetics |

“Not demonstrated” remains narrower than “impossible.” Target 22 is a positive result and permanently distinguishes Q3I from Q3. Targets 4, 21, 23, 24, 25, 26, 28 and 29 become non-waivable remediation stops; success of any one returns immediately to Q0 and Board review.

## 34. Architecture Board selection — Q3I

AD-020A selects this complete remediation direction:

```text
Q3I := H3 + L2 + G2 + A1 + T1 + C1 + E1 + D2
       + F1 + V1 + LT2 + IO2
```

In human terms:

- OCP-004 remains the single readable owner of Operation identity, intent, temporal/spatial context, parent/child composition and bounded inter-operation assertion values;
- one new Route C, non-Concept `OCP-017 — Operation Lifecycle Contract` is the sole owner of stages, paths, structural completeness, authorization-evidence acceptance, authoritative transition history and terminal-alignment evidence;
- Assignment, Constraint, Event occurrence, Objective and assessment retain their current defining owners;
- `Operation generates Event` leaves the stable surface; explicit downstream Event relevance remains possible without a new Concept edge;
- ExplicitIntentRecord and validation evidence become two separately mapped families under one exact OCP-004 P-001 metadata invocation;
- lifecycle transitions become one OCP-017 P-001 Module B invocation;
- inter-operation assertions become exact nested IO2 values rather than independently identified records; and
- Q0 remains the fail-safe if any selected owner, form, dependency, replay or Pattern obligation cannot be stated exactly.

Q3I is selected because it gives every current statement one bounded owner while creating only the lifecycle authority already required by OCP-004. It is not selected because Q3 led discovery, because split files appear tidy, because CI is green or because Operation is next in T4 order.

## 35. Selected OCP-004 stable surface

The future remediation must make these guarantees readable in OCP-004 itself:

1. One exact `operation_id` identifies one purposeful, context-bounded activity independently of name, template, classification, participants, local spatial payload, lifecycle stage, Event and outcome.
2. Outside `Draft`, exactly one active intent branch exists: non-empty exact `objective_refs` or one valid ExplicitIntentRecord, never both.
3. Every Objective reference exact-resolves under OCP-008; membership means affirmative pursuit only and implies no priority, sequence, hierarchy, aggregation or achievement.
4. Explicit intent and validation keep immutable exact bindings, conflict-safe evidence-set semantics and no timestamp/order/count winner.
5. Planned and actual temporal statements remain distinct.
6. AD-014 local spatial context remains zero/one/many, snapshot-local, fail-safe and non-reusable.
7. Assignment alone owns authoritative Resource participation; parent/child or inter-operation relations create no Assignment.
8. Constraint alone owns applicability and blocking/advisory semantics.
9. OCP-004 owns exact parent/child composition, including dataset acyclicity and no inheritance of participation, applicability, spatial context, outcome or authorization.
10. OCP-004 owns only the bounded IO2 assertion semantics in §37; workflow agreement, permission and caller authorization remain outside it.
11. Event identity and occurrence remain independent; an Operation transition is not an Event automatically.
12. `Completed Operation != achieved Objective`; OCP-011 remains the assessment owner.
13. Authorization evidence, provenance, profile success or a stage label never creates authorization by itself.
14. No Readiness, State, availability, admissibility, interchangeability, Organization holder or production authority is inferred.
15. Every exact current/historical reference replays under its original reviewed contract or has an explicit lossless migration; no newest-version redirect exists.

OCP-004 must expose one concise cross-reference to OCP-017 and one ownership table. A person must be able to learn what an Operation is and what it does not own without reconstructing PR history or checker code.

## 36. Selected OCP-017 lifecycle authority

The future remediation may propose one `OCP-017 — Operation Lifecycle Contract` only as a Route C non-Concept artifact under OCP-016. Its proposed direct dependency set is exactly `AD-020, OCP-001, OCP-004, OCP-005, OCP-006, OCP-010, OCP-011, OCP-016, P-001`; removing an unused dependency is allowed only with line-level evidence that the corresponding semantic boundary is not consumed. It must:

1. depend on exact OCP-004 identity and import OCP-005/OCP-006/OCP-010/OCP-011 only for the evidence or boundary semantics named below;
2. define one finite stage vocabulary and every allowed transition path;
3. own G2's universal structural minimum for each non-Draft stage and one exact fail-safe domain-profile hook;
4. own A1's evidence-acceptance envelope while leaving the authorization source/mechanism to a separately governed owner;
5. reject missing, duplicate, ambiguous, stale, conflicting or incomparable profile/authorization evidence;
6. own T1 terminal-alignment evidence and require a named non-permissive disposition for each still-effective Assignment without mutating OCP-005 records;
7. define LT2 OperationLifecycleTransitionRecord under exact `P-001@0.1.0` and Module B;
8. make transition history authoritative and any materialized stage/time/provenance field a checked projection;
9. keep Constraint evaluation in OCP-006, Event occurrence in OCP-010 and outcome assessment in OCP-011;
10. preserve `Completed != achieved`, lifecycle/Assignment independence and all Readiness/State exclusions; and
11. supply a readable dependency and authority table with no reverse OCP-004 dependency.

The selected D2 topology is downstream and acyclic: OCP-017 depends on OCP-004 and any exact evidence owners it consumes; OCP-004 does not gain dependencies on OCP-005, OCP-006, OCP-010, OCP-011 or OCP-017. OCP-017 is not a Concept, State abstraction, authorization mechanism or production workflow schema.

## 37. Selected record-form and relation contract

### 37.1 F1 and V1

OCP-004 must publish separate conformance statements for OperationExplicitIntentRecord and OperationIntentValidationEvidenceRecord using the complete mappings in §§14.1–14.2. One `Uses-Patterns: P-001@0.1.0` metadata binding may import the shared form, but it cannot merge the two semantic families.

F1 adds exact immutable authoring provenance and keeps `intent_id` independent of `intent_version_ref`. V1 keeps `validation_id`, exact intent/rule/input bindings and conflict-safe set evaluation. Neither family selects a newest record, and validation never becomes authorization.

### 37.2 LT2

OCP-017 must publish the complete §14.3 mapping, including non-empty `transition_id`, exact `operation_ref`, allowed path, ordered occurrence rule, provenance, authoritative history, deterministic projections and invalid-branch rejection. Module B is mandatory; Modules A and C remain absent unless separately justified by actual effectivity or supersession semantics.

### 37.3 IO2

OCP-004 must replace the record-like placeholder with a snapshot-local value having this bounded meaning:

- `source_operation_ref` equals the owning Operation identity;
- `target_operation_ref` exact-resolves once to another Operation under a declared resolution scope;
- `relation_type` is one closed OCP-004-owned value among `coordinates_with`, `depends_on`, `supports` and `conflicts_with`;
- `provenance_ref` attributes why the exact owning snapshot contains the assertion but grants no permission or precedence;
- duplicate normalized `(source, relation_type, target)` values reject without list-order selection; and
- the value has no independent ID, external reference target, effectivity, transition history, supersession or current-head projection.

The four values are deliberately modest: they state coordination relevance, operational dependency, claimed support direction or claimed incompatibility in the owning snapshot. They do not create workflow agreement, Constraint applicability, Assignment, Event, outcome, authority or a Concept edge.

Because the owning Operation snapshot is the only identity and history boundary, IO2 does not invoke P-001. If any consumer needs to address the assertion independently, preserve it across Operation snapshots as the same subject, add effectivity/history/supersession or delegate kind meaning, the remediation must stop and reopen IO1/IO3 rather than add a hidden record.

### 37.4 P-001 ledger boundary

AD-020A changes neither P-001 nor any current invoker. The future remediation must quote P-001 §§13 and 16 and state whether “six current primary invokers” is an acceptance-time evidence statement or requires a Pattern-owned current-prose correction before two new invoking artifacts can merge.

It may not silently leave a false live count, edit P-001 under an unchanged semantic claim, bump P-001 and mass-update invokers, or rewrite immutable snapshots without a separately reviewed justification. If exact-head review cannot establish a truthful no-Pattern-change treatment, the Operation remediation stops; a separate Pattern accounting/version act with its own gates must precede it.

## 38. Consumer, migration and rollback result

Q3I changes no Operation identity or current reference by design.

| Consumer / data surface | Selected treatment |
|---|---|
| OCP-005 Assignment | keeps exact Operation endpoint and participation authority; OCP-017 may read exact Assignment evidence but never mutates it |
| OCP-006 Constraint | keeps applicability/evaluation authority; OCP-017 may require exact evaluation evidence without copying its formula |
| OCP-010 Event | keeps independent occurrence and zero/one/many relevance; no dependency reversal or new edge |
| OCP-011 assessment | keeps exact Objective assessment; no lifecycle projection or rebinding |
| OCP-014 coordination profile | keeps context validation without operational permission; IO2 does not make profile ownership relation authority |
| future OCP-017 | becomes an explicit new downstream OCP-004 consumer and owns only the lifecycle surface |

Historical OCP-004 `0.8.3` snapshots remain replayable under that exact reviewed contract. Migration cannot invent `transition_id`, `operation_ref`, provenance, authorization evidence, relationship meaning or a passing validation result. A current value that cannot satisfy the new contract remains historical or causes migration to stop; it is never repaired by timestamp, list order, nearest label or source count.

The later remediation must provide an exact field relocation ledger, before/after reference examples, unchanged-consumer evidence and an atomic rollback that restores both document ownership and executable interpretation. Partial rollback of OCP-004 without OCP-017, or vice versa, is invalid.

## 39. Selected scenario results

The thirty §19 scenarios have deterministic Q3I treatment:

| # | Q3I result |
|---:|---|
| 1 | both Operation retain distinct `operation_id`; shared context never merges identity |
| 2 | Draft may have neither active intent branch |
| 3 | both exact Objective references are affirmative and must resolve separately |
| 4 | both branches outside Draft reject |
| 5 | stale exact-binding evidence rejects the non-Draft explicit-intent branch |
| 6 | conflicting exact-binding validation results reject; time cannot elect a winner |
| 7 | changed content under the old version token rejects |
| 8 | domain-profile failure blocks the transition despite Core structural completeness |
| 9 | zero, multiple or incomparable profile owners reject |
| 10 | ownerless authorization provenance cannot satisfy A1 |
| 11 | exact evidence binding is traceability only; OCP-017 grants no external permission |
| 12 | Assignment effectivity remains OCP-005-owned and is not implied by Active |
| 13 | Completed with an effective unfinished Assignment requires the exact T1 disposition/evidence; no automatic mutation occurs |
| 14 | missing/conflicting terminal alignment evidence rejects the terminal transition |
| 15 | parent/child creates no inherited Assignment |
| 16 | self-parent and any dataset cycle reject |
| 17 | independent coordination uses IO2 and creates no composition |
| 18 | time/space overlap alone creates no IO2 assertion |
| 19 | Event remains valid with zero Operation relevance |
| 20 | one Event may be relevant downstream to several Operation without identity change |
| 21 | a transition may exist without an Event |
| 22 | Completed and `indeterminate` assessment remain compatible distinct facts |
| 23 | Constraint evidence may block a transition while remaining external to lifecycle stage identity |
| 24 | an ownerless or multiply owned relationship kind cannot become IO3; IO2 uses only the closed OCP-004 values |
| 25 | unresolved or ambiguous target Operation rejects the IO2 value |
| 26 | duplicate transition IDs or invalid branching reject under LT2 Module B |
| 27 | historical exact references replay under their original contract before and after remediation |
| 28 | lifecycle extraction preserves the exact Operation endpoint consumed downstream |
| 29 | local spatial binding cannot be promoted into IO2 or a reusable relation identity |
| 30 | Operation context yields no Capability/Readiness or Resource-interchangeability conclusion |

## 40. Counterexample disposition

All thirty-two §20 counterexamples remain rejected:

- **1–4:** lifecycle order, discovery approval, section length and file count create no semantic owner or selection authority;
- **5–8:** prose cannot create an Event edge, deleting `generates` does not erase relevance, reverse dependency is not free, and a transition is not an Event;
- **9–16:** completion, Assignment, composition, overlap, provenance labels, Order status, domain validation and checker success cannot supply achievement, authorization or completeness authority;
- **17–22:** names, storage, record count, P-001, occurrence time and version references cannot decide applicability or optional modules;
- **23–26:** timestamp, order, count, list position and local spatial identity cannot elect a record or supply another family's identity;
- **27–30:** Coordination profile, Capability equality, Organization data and discovery approval create no operational permission, interchangeability, participation, authority or backlog resolution; and
- **31–32:** green CI does not select Q3I, and no prior authorization transfers to AD-020A or remediation.

These are normative rejection classes, not a substitute for the positive contracts in §§35–37.

## 41. Alternatives not selected and reopening gates

- **Q0** becomes immediate outcome if any selected owner, migration, P-001 mapping or evidence envelope cannot be proved exactly.
- **Q1** may reopen only if a concrete human or consumer need requires one complete in-place lifecycle and the four-family P-001 concentration remains readable.
- **Q2** may reopen if extraction duplicates identity, makes historical replay non-atomic or leaves OCP-004/OCP-017 unreadable together.
- **Q3** cannot reopen unchanged; any identified external relationship family must name its owner and is H4/IO3 evidence.
- **Q4** may reopen only when a concrete consumer needs independent relationship identity/effectivity/history or an exact relationship-kind owner exists.
- **F2** remains gated by AD-004's Objective-only sunset decision and a lossless explicit-intent migration.
- **V2/V3, LT1/LT3 and IO1/IO3** require concrete identity, consumer or migration evidence; architectural symmetry is insufficient.
- **E2/E3 or D3** require their own topology evidence and Board act. Prose in the remediation cannot add an edge or reverse a dependency.

No sunk authoring cost, accepted status of this act, readiness percentage or implementation convenience raises the reopening threshold.

## 42. Mandatory remediation proposal

AD-020A authorizes preparation—not merge—of one atomic proposal with this bounded semantic target:

1. revise OCP-004 to `0.9.0 / Draft` with the §§35 and 37 stable surface, add only P-001 to its current direct dependency set for the selected form invocation, and add no OCP-017/downstream dependency;
2. add one `OCP-017 — Operation Lifecycle Contract` at `0.1.0 / Draft` with the §36 Route C contract;
3. add exact `Uses-Patterns: P-001@0.1.0` metadata and separate F1/V1/LT2 conformance prose only after the §37.4 ledger question is resolved;
4. change only checker code, rule manifest, tests and synthetic non-sensitive fixtures necessary to witness the selected finite rules;
5. update README, backlog and roadmap accounting without changing a Concept registry/taxonomy/map projection;
6. keep all five current consumer identities/references stable and account for OCP-017 as the explicit new consumer;
7. include exact old/new section and field relocation ledgers, historical replay, migration and atomic rollback evidence;
8. cover every §39 scenario, every §40 rejection class and material positive/negative P-001 case;
9. distinguish machine checks from human-only ownership, authority, readability and topology review; and
10. retain every inherited exclusion and backlog status.

The proposal stops and returns to Q0/Board if it discovers:

- a second lifecycle or relationship owner;
- an OCP-004 identity/reference change;
- no exact legitimate owner for the domain-profile or authorization-evidence envelope;
- a need for OCP-004 to depend on OCP-005/006/010/011/017;
- a new Concept, Concept edge, State abstraction, authorization mechanism, registry, Organization holder or production schema;
- an IO2 consumer requiring independent identity, effectivity, lifecycle, supersession or external reference;
- an F1/V1/LT2 mapping missing a P-001 element or using an undeclared module;
- a P-001 current-ledger statement that cannot remain truthful without a separate Pattern act;
- non-replayable historical data or invented migration facts; or
- an edit to any Operation backlog status.

The remediation must receive its own exact-head Fable review, Codex adjudication, green CI and explicit Pavlo/Architecture Board authorization. If the bounded implementation cannot fit one reviewable atomic tree, it must stop rather than split semantic ownership across partially effective merges.

## 43. Authorization boundary

AD-020A selects Q3I only as the preparation direction and authorizes authoring the exact §42 remediation proposal.

It does not edit or approve OCP-004, create or approve OCP-017, invoke P-001, amend P-001, change a dependency or graph edge, create a fixture/schema authority, resolve AB-015/AB-016/AB-017/AB-019/AB-020/AB-023/AB-028, promote Operation or authorize T5/T6/T7 work. It does not decide Assignment/Event ordering or any later lifecycle act.

Authorization for AD-020A cannot merge the remediation. A content change after exact-head review invalidates that review and any head-bound authorization. No authorization transfers across these gates.

## 44. Accepted effect and next gate

When exact-head reviewed, explicitly authorized and squash-merged, AD-020A will:

- set AD-020 to `0.2.0 / Accepted`;
- record the positive target-22 result against provisional Q3;
- select Q3I (`H3 + L2 + G2 + A1 + T1 + C1 + E1 + D2 + F1 + V1 + LT2 + IO2`) only as the Operation stable-surface remediation direction;
- retain Q0 as immediate fail-safe and every reopening gate in §41;
- authorize preparation of one bounded OCP-004 `0.9.0 / Draft` plus OCP-017 `0.1.0 / Draft` proposal under §42;
- keep OCP-004 at `0.8.3 / Draft`, Operation at `Accepted`, P-001 at `0.1.0 / Accepted`, AB-062 `Planned`, all seven Operation AB statuses unchanged and readiness at approximately 71%; and
- change no OCP, Concept, Concept status, Pattern, dependency, registry row, taxonomy projection, foundation-map edge, checker rule, fixture, schema, data, reference or production authority.

The selected remediation remains only a proposal until its own four gates close on one exact head. Completion or failure of that proposal must be followed by a fresh blocker/stability audit before any Operation lifecycle or T5 decision.
