---
Decision-ID: AD-017
Title: Objective Editorial-Correction Boundary
Version: 0.2.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-001, OCP-008, OCP-016, P-001, AD-003, AD-016
Applies-To: AB-063, Objective statement correction, OCP-008 Canonical blocker
Review-After: External adversarial review of AD-017A before any Architecture Board selection
---

# AD-017 — Objective Editorial-Correction Boundary

## 1. Trigger and purpose

OCP-008 currently draws a necessary distinction:

- a substantive change of intended outcome creates a new Objective and may use explicit supersession; while
- whitespace, formatting or an orthographic correction may preserve Objective identity only when an applicable domain rule explicitly classifies the change as non-semantic.

The first rule has an immutable-record and supersession contract. The second has no selected authority, evidence, history or replay model. OCP-008 does not say who makes the classification, what exact rule and inputs governed it, how conflicting classifications fail, or which statement a historical consumer saw.

AD-016E selected J8 because this question can be investigated without deciding Organization or Resource identity. It authorized this discovery only; it did not authorize an OCP-008 amendment, an Objective promotion or any particular correction model.

AD-017 opens AB-063 and compares ways to close that gap. Revision `0.1.0` selects no outcome and changes no OCP, Concept, Pattern invocation, consumer reference, registry row, graph edge, schema, checker rule or fixture.

## 2. Exact reviewed baseline

This discovery starts from `main@eef77ea9e2be29d218becbc23a2bffd767634b4d`, after the authorized AD-016E merge.

The exact OCP-008 input is:

- Git blob: `c1a088aff6e61bf553a100ecb2dd9975a3b67657`;
- SHA-256: `35f1a24e7f9d085ca3b9a6300d39544d5aa13d660652a34935a38980e96535a2`;
- document state: `0.2.1 / Draft`;
- Objective state: `Accepted`; and
- Pattern binding: `P-001@0.1.0`, endpoint-free Objective record, Optional Module C.

Hashes identify the reviewed input. They do not make Git order, timestamp recency or a content hash the authority for semantic equivalence.

## 3. Inherited mandates

Every admissible outcome must preserve the following accepted rules.

From OCP-008:

1. Objective identifies an intended outcome, condition or effect; it is not an Operation, Order, Task, Result or achievement assertion.
2. `objective_id` is stable and does not depend on an Operation, author, plan name or consumer count.
3. A substantive change creates a new Objective; the old Objective is never silently rewritten.
4. `supersedes_objective_ref` is explicit, acyclic, may branch and does not update consumer references automatically.
5. Prior and successor Objectives remain valid identified records; Core does not choose a current one by recency.
6. `provenance_ref` supplies attributable creation or replacement provenance, not authorization by implication.
7. An Operation outside `Draft` exact-resolves each Objective reference to one valid Objective instance.
8. Objective carries no achievement, authorization, lifecycle-effectivity or universal-current-state conclusion.

From P-001:

- the Objective record has stable record identity, one semantic owner, explicit provenance, validation and authority declarations;
- Optional Module C supersession never rewrites the prior record;
- P-001 supplies form only and cannot supply Objective equivalence, correction or domain meaning; and
- a new identified amendment record would require its own complete exact-version invocation rather than inheriting the Objective invocation.

From OCP-001, OCP-016 and AD-016E:

- evidence must remain outcome-fair;
- Core, Core-envelope, domain and implementation authority must not overlap;
- ambiguity is non-permissive and cannot be resolved by newest timestamp, record order, editor or issuer count, majority or similarity score;
- strict immutability is the fail-safe control when immutable replay cannot be preserved; and
- resolving this discovery still does not authorize OCP-008 promotion. A fresh blocker, stability and compatibility audit plus a new Board scope act remain mandatory.

## 4. Terms that must remain distinct

| Term | Meaning in this discovery | Not implied |
|---|---|---|
| Objective identity | the governed identity of one intended outcome under OCP-008 | a mutable document whose latest text replaces history |
| stored normative statement | the statement payload that participates in Objective semantics and historical replay | rendered whitespace, typography or UI layout |
| display representation | a non-authoritative presentation of an exact normative statement | permission to change the normative statement |
| editorial correction | a proposed change claimed not to alter intended outcome, condition or effect | proven semantic equivalence merely because the change is small |
| semantic change | a change that alters the governed intended outcome, condition or effect | a conclusion derivable from edit distance alone |
| equivalence decision | an attributable result under one exact domain rule, version and input pair | universal truth or a Core language model |
| correction evidence | immutable material sufficient to replay what changed and why it was classified | authority merely because evidence exists |
| Objective supersession | a new Objective explicitly replacing a prior Objective after substantive change | same-identity amendment or automatic consumer rebinding |
| record revision | an immutable representation version, if such a layer is selected | Objective identity by default |

The word “editorial” is a claim to be evaluated, not a privileged edit class that may bypass evidence.

## 5. Current authority and replay gap

| Existing statement | What it safely establishes | What remains unresolved |
|---|---|---|
| non-semantic correction may preserve identity | identity preservation is not categorically forbidden | the selected representation and historical authority |
| applicable domain rule decides equivalence | Core need not own language/domain meaning | exact rule identity, version, owner, inputs and result evidence |
| Objective instance is authoritative | an ungoverned derived view cannot override the record | whether a base record, amendment chain or exact revision is authoritative after correction |
| `provenance_ref` records creation/replacement provenance | creation and substantive replacement are attributable | same-identity correction provenance and conflict handling |
| Operation references one Objective instance | zero/multiple resolution fails | whether a historical reference binds a statement snapshot or may resolve through later correction |
| P-001 Module C governs supersession | prior Objective history is not rewritten | same-identity amendments or record versions are not supplied by Module C |

Without a selected answer, two repositories may both claim OCP-008 conformance while returning different historical text for the same `objective_id`. That is the blocker; spelling convenience is not.

## 6. Decision questions

AD-017 must answer:

1. Is any change to the stored normative `statement` compatible with one Objective identity?
2. If yes, what exact object is immutable: the Objective, an amendment record, a statement revision or a composite snapshot?
3. Who owns the non-semantic classification, and how is the exact domain rule, version and evaluator bound?
4. What evidence records the before value, after value, rule inputs, result, provenance and decision time without making time authoritative?
5. Which representation is authoritative when a base Objective, correction record, materialized statement and derived view disagree?
6. How does a consumer replay the exact normative statement used by an earlier Operation or assessment?
7. Are same-identity corrections linear, may they branch, and how do conflicting corrections fail?
8. Can a later rule version reclassify an earlier correction, or must historical evaluation remain bound to its original rule and inputs?
9. Does an outcome require a new P-001 invocation, a remapping of the current Objective invocation, or no Pattern change?
10. How are current OCP-008 Objectives migrated without inventing a latest revision or rewriting references?
11. Which differences are display-only and therefore outside the stored normative statement altogether?
12. What exact evidence forces a claimed editorial correction to become a new superseding Objective?
13. What remains domain-owned, and what minimal Core or Core-envelope behavior is needed for exact replay and ambiguity rejection?
14. Can the outcome be rolled back without making previously recorded Objective references ambiguous?

## 7. Non-negotiable semantic boundary

No admissible outcome may permit silent in-place mutation of the historical normative statement.

In particular:

- the same `objective_id` does not mean “return whichever text is newest”;
- a correction label, author role, approval count or successful spell-check does not establish equivalence;
- a domain equivalence result does not grant command, policy or approval authority;
- a correction never updates Operation, assessment or other consumer references automatically;
- a correction or supersession does not establish achievement, Readiness, availability, admissibility or authorization;
- missing, conflicting, unknown-version or unreplayable evidence cannot preserve identity by default; and
- implementation caches and display layers cannot become a second semantic owner.

An unversioned mutable-row model is therefore a falsification control, not an admissible outcome.

## 8. Candidate outcomes

### A — strict immutability

Every change to the stored normative `statement` creates a new Objective with a new `objective_id`. A successor may exact-reference the prior Objective through the existing supersession contract. Display-only rendering can change outside the record because it is not stored normative content.

This outcome uses the current authoritative Objective record and P-001 Module C without a new record family. Its main cost is identity churn and explicit consumer decisions even for a harmless stored typo. Its strength is that replay and rollback already have one authority.

### B — identified editorial-amendment record

Objective identity remains stable. A separate immutable `ObjectiveEditorialAmendmentRecord` exact-targets one Objective and records the governed before/after statement evidence plus the classification provenance. OCP-008 would have to define whether the amendment history or a deterministic derivation over that history is authoritative.

This outcome preserves a visible correction history without turning every correction into a new Objective. Its main risks are a second authority over Objective text, branching/conflicting amendments and an incomplete P-001 invocation. The record name is provisional and creates no artifact or authority in this discovery.

### C — exact versioned Objective snapshot

One logical Objective identity may have multiple immutable statement snapshots. Each snapshot has its own stable revision identity, exact rule/evidence binding and deterministic relation to the logical Objective. Historical consumers bind an exact revision rather than a floating Objective head.

This outcome makes replay explicit. Its main risks are changing the current meaning of `objective_id` as the P-001 record identity, requiring consumer-reference migration and inventing a default latest revision. A positive comparison must explain whether the record identity becomes composite or gains a distinct `objective_revision_id`.

### D — stored normative statement excludes display-only variation

OCP-008 defines a canonical normative payload boundary. Whitespace, typography, wrapping and other display-only representation stay outside `statement`; changing them does not change an Objective because no normative data changed. A change to the stored normative statement—including an orthographic change inside that payload—falls back to A unless a separately selected B or C mechanism governs it.

This is the smallest representational outcome and may also be a common safeguard for A, B or C. Its main risk is claiming to resolve the blocker while a real stored-text correction remains unanswered. D is a complete final outcome only if evidence shows that every same-identity use case is truly display-only; otherwise it is an adjunct, not a substitute for A, B or C.

## 9. Outcome interaction and completeness

A, B and C are competing authorities for a changed stored normative statement. They cannot be active simultaneously for the same correction class without an explicit precedence rule and proof that no dual authority results.

D operates at the representation boundary. It may reduce the number of cases that reach A, B or C, but cannot classify a changed stored payload as equivalent by itself.

External comparison must also test whether a concrete case exists that none of A–D can represent. A new outcome is admissible only when it names a distinct authority and closes such a case without weakening §7. UI convenience, common database practice or model popularity is not evidence of incompleteness.

## 10. Conditional Core Boundary routing ledger

| Candidate object | Primary route hypothesis | Owner | Consumer and non-implication |
|---|---|---|---|
| Objective identity/correction invariant under A–D | F — existing fundamental Core Concept boundary | OCP-008 | all Objective consumers; does not create a new Concept |
| amendment record under B | C — Core non-Concept, if shared evidence proves it necessary | OCP-008 or a separately justified exact owner | correction replay; does not become an Objective or universal approval act |
| Objective revision identity under C | F — part of existing Objective identity/invariant semantics | OCP-008 | exact Objective consumers; does not create a second fundamental Concept |
| domain equivalence rule used by B or C | D by default; E only if a concrete Core consumer proves a minimal exact-binding envelope | named domain owner; any envelope owned by its exact Core contract | no best-effort translation or universal equivalence |
| display rendering under D | I — implementation-local | renderer/product | cannot alter stored normative semantics |
| normative display/payload separation under D | F — Objective invariant boundary | OCP-008 | all Objective consumers; does not standardize a UI format |

These are route hypotheses for the candidate objects, not admission decisions. If an outcome cannot name one non-overlapping primary route and legitimate owner for each object it uses, it remains Discovery.

No route field, admission registry, score, P-002, schema or checker projection is requested.

## 11. P-001 impact by outcome

### 11.1 Outcome A

The current `P-001@0.1.0` Objective invocation and Optional Module C may remain unchanged. The new Objective is the immutable successor record; the prior record is not rewritten.

### 11.2 Outcome B

A separately identified amendment record would require its own full P-001 applicability and invocation decision. If invoked, the later defining contract must map all seven Required Elements and every selected Optional Module. The Objective invocation does not satisfy those obligations by inheritance.

### 11.3 Outcome C

The current Objective invocation must be reconciled with logical identity and revision-record identity. A later contract must state exactly which identifier satisfies P-001 stable record identity and how Objective supersession differs from same-Objective revision history. Silence is not a partial invocation.

### 11.4 Outcome D

Display representation requires no P-001 invocation. If stored normative content changes, D supplies no amendment semantics and therefore uses A or a separately selected positive mechanism.

P-001 never supplies the domain equivalence rule in any outcome.

## 12. Mandatory consumer scenarios

Every admissible outcome must give one deterministic answer for each scenario:

1. An Operation references an Objective before a later claimed spelling correction; an audit must recover the exact statement used by that Operation.
2. A whitespace-only UI reflow changes no stored normative bytes or normalized payload.
3. A spelling change fixes a harmless typo but changes the stored normative statement.
4. A one-character edit removes a negation or changes a number and is incorrectly labelled editorial.
5. Two actors propose different corrections from the same baseline.
6. One equivalence rule accepts a change and a second applicable rule rejects it.
7. A historical equivalence decision references a rule version that can no longer be resolved.
8. A newer rule version would classify an old correction differently.
9. A materialized current statement disagrees with the authoritative amendment or revision history.
10. A consumer supplies only `objective_id` where the selected model requires an exact revision.
11. A correction is rolled back after another consumer has used it.
12. A substantive replacement and an alleged editorial correction branch from the same Objective.

The scenarios use synthetic text and opaque identifiers only. They require no operational data.

## 13. Mandatory counterexamples

External review and the later comparison must reject these conclusions:

1. The newest statement is authoritative because its timestamp is later.
2. File, record or list order selects the effective correction.
3. More editors, reviewers, issuers or matching tools prove equivalence.
4. A similarity score or equal hash after ad hoc normalization proves semantic identity.
5. Equal `objective_id` permits a store to overwrite the prior statement without replay evidence.
6. The word “editorial” makes a change non-semantic without an exact rule and attributable result.
7. Current `provenance_ref` automatically records same-identity correction authority.
8. P-001 Module C automatically supplies amendment or revision semantics.
9. Outcome B may omit a complete Pattern invocation because Objective already invokes P-001.
10. Outcome C may expose a floating latest revision while claiming exact replay.
11. Outcome D may treat a changed stored typo as display-only merely because a UI renders it similarly.
12. A correction may rewrite historical Operation or assessment evidence automatically.
13. A missing, ambiguous or conflicting rule result may preserve identity as a permissive default.
14. A later rule version may silently re-evaluate old correction history.
15. Resolving AB-063 makes Objective Canonical or authorizes its promotion.
16. A correction record, revision or display layer creates achievement, approval, authorization or universal current-state semantics.

## 14. Unconditional evidence obligations

The following obligations apply to A–D:

1. preserve deterministic replay of the exact historical normative statement;
2. preserve the distinction between display representation and stored normative content;
3. exact-bind every claimed equivalence to a named owner, rule/version, before/after input pair, result and provenance, or state that no equivalence decision exists;
4. reject missing, conflicting, ambiguous, unknown-version or unreplayable correction evidence;
5. prevent timestamp, order, count, majority, similarity or implementation cache from selecting authority;
6. prevent correction from automatically rebinding any consumer;
7. preserve substantive-change supersession and its acyclic, non-rewriting history;
8. keep correction separate from achievement, authorization, approval, Readiness and current-state semantics;
9. define a rollback that does not make historical references float; and
10. use human-readable synthetic scenarios plus executable evidence when the selected contract becomes mechanically expressible.

No unconditional fixture may require an amendment record, a revision identifier, a mutable current field, a domain registry or an implementation display layer, because at least one admissible outcome rejects each of those mechanisms.

## 15. Outcome-conditional evidence

### 15.1 Outcome A

- prove that every changed stored normative statement receives a new Objective identity;
- replay the prior and successor records independently through explicit supersession;
- show that display-only changes create no record mutation; and
- migrate no existing Objective or consumer reference.

### 15.2 Outcome B

- define amendment identity, exact Objective target, immutable before/after evidence, provenance and authority;
- define branching, conflict, withdrawal/correction and any supersession behavior without latest-record fallback;
- prove the authoritative statement derivation and reject disagreement with any materialized view;
- complete the separate P-001 decision and invocation if P-001 is used; and
- preserve historical consumer replay across multiple amendments.

### 15.3 Outcome C

- define logical Objective identity separately from immutable revision identity;
- exact-bind consumers to the revision needed for historical replay and reject floating latest resolution;
- define revision branching, equivalence evidence, rollback and conflict behavior;
- reconcile the model with the existing P-001 Objective identity and Module C supersession contract; and
- provide an explicit migration for every current unversioned Objective reference.

### 15.4 Outcome D

- define the exact normative-payload/display boundary without choosing a language, UI or transport format;
- prove that several display renderings preserve one unchanged stored normative payload;
- reject any attempt to hide a changed stored statement inside display normalization; and
- demonstrate either that D closes every current use case or that all remaining stored changes fail safe to A or a separately selected mechanism.

## 16. Outcome-fairness audit

External review must reject an evidence plan that assumes its preferred mechanism:

- A and D cannot be required to produce amendment-record lineage;
- A, B and D cannot be required to expose an Objective revision identifier;
- A and D cannot be rejected merely because they provide no same-identity stored edit path;
- B cannot be accepted merely because an audit record is familiar, and cannot inherit P-001 conformance from Objective;
- C cannot be accepted merely because API versioning is familiar, and cannot use a floating latest revision;
- D cannot be credited as a complete correction model while a stored orthographic change remains unresolved;
- B and C must provide replay evidence equivalent to A's immutable-record history;
- A must address user-visible correction cost, but convenience cost alone cannot defeat its fail-safe authority; and
- migration size, implementation effort, reviewer preference or the number of fields cannot substitute for semantic adequacy.

The explicit falsification target is: **evidence obligations assume a record, revision, domain or display layer rejected by the outcome being evaluated**.

## 17. External-review falsification targets

External review must try to disprove:

1. that the existing OCP-008 permission leaves a real authority/replay gap rather than already selecting a mechanism;
2. that A–D cover strict replacement, identified amendment, exact revision and display-only exclusion without hidden preselection;
3. that D is honestly bounded and cannot hide a changed stored statement;
4. that B and C preserve one unambiguous authority and exact historical consumer replay;
5. that all four outcomes fail safe when equivalence evidence is missing or conflicting;
6. that the P-001 impact is complete and outcome-conditional;
7. that the OCP-016 route hypotheses keep Concept, record, domain rule, envelope and implementation authority non-overlapping;
8. that no timestamp, record order, editor/issuer count, majority or similarity score becomes authority;
9. that no outcome creates a new Concept, graph edge, promotion or automatic consumer rebind; and
10. that the boundary is understandable without reading checker code or assuming a storage technology.

## 18. Decision criteria

The Architecture Board should prefer the smallest authority model that:

- preserves immutable replay for the exact statement seen by every historical consumer;
- gives one legitimate owner to classification, evidence and the authoritative representation;
- fails strict when classification or resolution is missing, ambiguous, conflicting or unreplayable;
- keeps display, domain equivalence and Core Objective semantics in non-overlapping homes;
- preserves the accepted substantive supersession contract;
- creates no new record, revision dimension, migration or Pattern invocation beyond demonstrated need; and
- can be rolled back without rewriting history.

A broader mechanism is justified only when a concrete consumer scenario fails under a narrower outcome. If no positive same-identity mechanism preserves replay without new or ambiguous authority, A is the required fail-safe result.

## 19. Exit criteria and next cycle

AD-017 may leave Discovery only when:

1. an external comparison evaluates A–D against every §12 scenario and §13 counterexample;
2. each outcome names its authoritative representation, classification owner, provenance, replay and rollback behavior;
3. P-001 obligations are complete and outcome-conditional;
4. every candidate object has one non-overlapping OCP-016 route or is explicitly rejected;
5. D is classified honestly as either a complete outcome for demonstrated display-only cases or an adjunct to A, B or C;
6. outcome-fair evidence coverage is complete;
7. no unresolved ambiguity receives a permissive default; and
8. outcome selection remains a separate exact-head Architecture Board act from discovery, implementation and promotion.

Revision `0.1.0` moves AB-063 from `Planned` to `Discovery` and records no preferred outcome. A later AD-017A may perform the evidence comparison without selecting an outcome. A later AD-017B may select A, B, C, D or a justified combination, or retain strict immutability and close the positive path.

Any OCP-008 amendment, new record contract, P-001 invocation, consumer migration, schema, fixture, Concept-status change, graph edge or promotion proposal requires a later separately reviewed and authorized PR. Authorization of this discovery cannot transfer to any of those acts.

## 20. AD-017A comparison method

Revision `0.2.0` compares A–D against the exact post-discovery baseline `main@bd2581be95566089b68478d2b8c6c35bfcf6a80f`. OCP-008 remains the same blob and SHA-256 recorded in §2.

The comparison asks five questions in order:

1. **Replay:** can an audit recover the exact normative statement used by a historical consumer?
2. **Identity:** what remains one Objective, and what immutable object changes?
3. **Authority:** who owns classification, evidence, conflict and the authoritative text?
4. **Consumer impact:** can current bare Objective references remain exact, or must they migrate?
5. **Rollback:** can the outcome reverse a correction without floating references or rewritten history?

`Strong` below means the outcome answers the scenario using accepted authority and no unresolved migration. `Conditional` means a named rule, record or reference contract is still missing. `Adjunct` means the outcome helps but cannot answer the stored-statement case alone. `Blocked alone` means the outcome requires another outcome for that scenario.

No outcome receives credit for UI convenience, common database practice, field count, document size or implementation familiarity.

## 21. Current consumer and executable baseline

The repository currently exposes one identity dimension for Objective.

| Surface | Exact current behavior | Consequence for correction |
|---|---|---|
| OCP-008 record | `objective_id` identifies the endpoint-free P-001 record that contains one `statement` | there is no amendment ID, revision ID or correction head |
| OCP-004 Operation | each `objective_refs[]` member is one bare Objective identifier and must resolve to exactly one valid Objective instance | the Operation snapshot does not bind a separate statement revision |
| OCP-011 assessment | `target_kind_ref: objective@1` plus `target_ref` exact-binds one Objective identifier | assessment identity preserves its target ID, not a later text revision |
| P-001 Module C | `supersedes_objective_ref` preserves prior Objective records and allows visible branching | it supplies substantive replacement history, not same-identity correction |
| Objective checker | indexes records by `objective_id`, rejects duplicate/invalid resolution and validates supersession cycles | it has no current-statement, amendment or revision projection |
| synthetic fixtures | exercise exact Objective resolution and supersession safety | no fixture proves a same-identity stored correction model |

The absence of a correction fixture does not prove that positive correction is impossible. It does mean B and C cannot claim compatibility from existing evidence.

There is one unavoidable reference result: if corrected text becomes visible through the same bare `objective_id`, an old consumer silently sees new text; if corrected text does not become visible through that ID, a later consumer needs another exact binding to request it. B and C must therefore define a consumer migration or an equivalent immutable snapshot binding. A does not introduce that ambiguity because changed stored text receives a new Objective ID.

## 22. Scenario-by-scenario findings

### S1 — historical Operation before a spelling correction

A keeps the Operation bound to the old Objective and requires an explicit new reference for corrected text. B needs the Operation or its immutable evidence to bind an exact amendment state; otherwise the bare ID floats. C needs an exact Objective revision. D protects display-only changes but sends a changed stored spelling to A, B or C.

### S2 — whitespace-only UI reflow

D directly separates rendering from normative payload. A also remains safe when the renderer changes outside the stored record. B and C add history that the scenario does not need.

Whitespace already stored inside the normative payload is not automatically display-only. Removing it after storage requires an exact normalization rule and cannot rely on visual similarity.

### S3 — harmless stored typo

A creates a new Objective and explicit supersession. B can preserve logical identity only with an exact amendment record, equivalence result and consumer binding. C can preserve logical identity through an exact immutable revision. D alone cannot handle the changed stored payload and must fail to A or a selected positive mechanism.

This is the strongest positive use case for B or C, but the repository contains no current consumer requirement that the same `objective_id` survive it.

### S4 — a negation or number is changed but labelled editorial

A creates a new Objective regardless of the label. B and C must reject identity preservation when the exact rule does not prove equivalence. D cannot move the changed token into display metadata. This scenario defeats edit distance, token count and spelling-tool success as authority.

### S5 — two corrections from one baseline

A produces visible Objective successors; neither wins by time. B must expose amendment branching or conflict and require an exact selected head. C must expose revision branching or conflict and prohibit a floating latest revision. D alone falls back to A.

### S6 — two applicable equivalence rules disagree

A requires no equivalence decision because both changed statements receive new identities. B and C must return a non-permissive conflict. D cannot erase the disagreement by calling the difference presentational.

### S7 — the historical rule version is unavailable

A replays both Objective records without that rule. B and C cannot preserve same identity for the affected correction because its decision is unreplayable. D handles only unchanged normative payload.

### S8 — a newer rule would classify the old correction differently

A does not reclassify history. B and C must retain the original exact rule/version and inputs; a new evaluation creates new attributable evidence rather than rewriting the old result. D does not create re-evaluation authority.

### S9 — a materialized current statement disagrees with history

A has no authoritative current-statement projection and exact record resolution wins. B and C must reject the materialized field when it differs from their declared history or derivation. D cannot use rendered text as an override.

### S10 — a consumer supplies only `objective_id`

A resolves one immutable record. Under B, the contract must state whether the bare ID means the base record or is insufficient for corrected text; it cannot mean the newest amendment. Under C, a consumer that requires corrected text must supply an exact revision and the bare ID is incomplete. D remains exact only while normative payload is unchanged.

### S11 — rollback after a consumer used the correction

A preserves all Objectives and requires an explicit consumer rebind; the prior Objective remains exact-resolvable. B records an explicit new amendment or withdrawal under one exact lineage, never deletion. C records an exact new revision or explicit branch. D can roll back presentation without normative effect but sends stored changes to another outcome.

### S12 — substantive replacement and alleged correction branch together

A represents both as distinct Objective successors and preserves the branch. B must keep the amendment branch separate from the new-Objective supersession branch and define consumer choice explicitly. C must distinguish same-Objective revision from new-Objective supersession. D cannot decide the stored change.

## 23. Consumer-fit matrix

This matrix contains all 48 scenario/outcome cells. A rating is not an implementation authorization.

| Scenario | A strict | B amendment | C revision | D display boundary |
|---|---|---|---|---|
| S1 historical Operation | **Strong** | Conditional: amendment-state binding | Conditional: revision migration | Adjunct; stored change exits D |
| S2 UI reflow | **Strong** when display is external | Extra | Extra | **Strong** |
| S3 stored typo | **Strong**, new ID | Conditional positive path | Conditional positive path | Blocked alone; fallback required |
| S4 mislabelled semantic edit | **Strong**, new ID | Conditional exact rejection | Conditional exact rejection | Blocked alone; cannot hide token |
| S5 concurrent corrections | **Strong**, visible successors | Conditional branch/head contract | Conditional branch/revision contract | Blocked alone; fallback required |
| S6 rule disagreement | **Strong**, no equivalence needed | Conditional conflict rejection | Conditional conflict rejection | Blocked alone |
| S7 unavailable rule | **Strong**, records replay | Conditional, same identity rejected | Conditional, same identity rejected | Adjunct only |
| S8 newer rule differs | **Strong**, no reclassification | Conditional exact historical pin | Conditional exact historical pin | Adjunct only |
| S9 materialized disagreement | **Strong**, record authority | Conditional projection check | Conditional projection check | Adjunct; renderer cannot override |
| S10 bare `objective_id` | **Strong** | Conditional: base or incomplete, never latest | Conditional: exact revision required | **Strong** only if payload unchanged |
| S11 rollback | **Strong**, explicit rebind/history | Conditional new lineage act | Conditional new exact revision | Adjunct for presentation only |
| S12 mixed branch | **Strong**, Objective branching | Conditional dual-layer separation | Conditional revision/supersession separation | Blocked alone |

The matrix shows two different facts. A is the only currently complete stored-change model because it uses accepted Objective identity and supersession. D is the strongest common representation safeguard, but not a complete stored-change model. B and C remain viable hypotheses, not currently complete contracts.

## 24. Identity, authority and replay comparison

| Question | A strict | B amendment | C revision | D display boundary |
|---|---|---|---|---|
| authoritative normative text | one immutable Objective record | deterministic base-plus-exact-amendment state | one exact immutable Objective revision | unchanged stored Objective payload |
| Objective identity after stored change | new `objective_id` | stable logical Objective ID | stable logical Objective ID | no answer; stored change exits D |
| additional identity | none | amendment record ID | Objective revision ID | none |
| equivalence owner | none required for identity | exact domain rule/result | exact domain rule/result | none for external rendering |
| historical consumer binding | existing bare Objective ID | bare ID plus exact amendment state/snapshot | logical ID plus exact revision | existing bare ID while payload is unchanged |
| conflicts/branching | existing Objective supersession branch | amendment heads or explicit conflict, no newest | revision heads or explicit conflict, no latest | outside D; fallback outcome handles it |
| rollback | explicit old/new Objective reference | new attributable amendment/withdrawal act | new exact revision/branch | presentation rollback only |
| P-001 impact | current Objective Module C unchanged | separate complete invocation decision | remap Objective record identity/history | none |
| current consumer migration | none | required for corrected-text replay | required | none for display only |
| primary risk | duplicate semantic Objectives and authoring cost | dual authority and incomplete head selection | identity redefinition and broad migration | false claim that presentation solves stored correction |

“Stable logical Objective ID” in B or C is not free continuity. It is a new rule that must coexist with immutable record identity and exact consumer evidence.

## 25. P-001 and consumer migration proof

### 25.1 A

The existing Objective record remains the P-001 record. A correction creates another conforming Objective and may use the already selected Module C. OCP-004 and OCP-011 continue to bind exact `objective_id` values. No schema or fixture migration is logically required.

### 25.2 B

The amendment is an independently identified assertion about one Objective and crosses the P-001 applicability threshold through identity, provenance and correction history. A later positive contract must either invoke exact P-001 completely or give an externally reviewed reason for a different form.

An amendment cannot alter what every old bare `objective_id` means without rewriting consumer history. Therefore a positive B contract needs one of:

- an exact amendment-state reference in each consumer snapshot that uses corrected text; or
- an immutable consumer-side Objective statement snapshot with an exact derivation back to amendment history.

“Resolve the latest amendment” is not a third option.

### 25.3 C

C makes the logical Objective different from the immutable P-001 revision record. It must add a stable revision identity or exact composite identity, then update every corrected-text consumer to bind it. Treating several rows with the same `objective_id` as distinct records violates current unique resolution; treating one mutable row as several revisions violates immutable replay.

### 25.4 D

D requires no new record or Pattern invocation. It must define which representation data is never part of the stored normative statement. It may not normalize away a stored token after the fact merely because a renderer treats the token as insignificant.

## 26. Core Boundary route and authority cost

| Outcome | Route F effect | Additional route | Authority synchronization | Reopening pressure |
|---|---|---|---|---|
| A | narrow OCP-008 invariant: all stored changes create new Objective | none | one Objective record authority | low; current consumers and P-001 remain exact |
| B | OCP-008 must define how amendment affects Objective text | Route C amendment record; Route D rule, with E only if an envelope is proved | base record, amendment history, domain result and consumer snapshot | high if any layer can select a head independently |
| C | OCP-008 must split logical identity from revision-record identity | Route D equivalence rule; E only if exact Core binding is proved | Objective, revision, domain result and every consumer reference | high because current P-001 and consumer contracts change |
| D | OCP-008 defines normative-payload exclusion only | Route I renderer | stored payload remains sole semantic authority | low as adjunct; unresolved if claimed as standalone stored correction |

All routes remain hypotheses until AD-017B. A route count is not a score, but every additional authority must have a concrete consumer and fail-safe synchronization rule.

## 27. Complete counterexample mapping

Each cell states how the outcome must defeat the corresponding §13 counterexample. The table contains all 64 cells.

| # | A strict | B amendment | C revision | D display boundary |
|---:|---|---|---|---|
| 1 | exact Objective ID, never time | exact amendment binding, never newest | exact revision, never newest | unchanged payload, never render time |
| 2 | record order irrelevant | head/conflict derived explicitly | branch/revision exact | render order irrelevant |
| 3 | counts cannot change identity | counts cannot select amendment | counts cannot select revision | display-tool count irrelevant |
| 4 | new ID regardless of similarity | exact domain result required | exact domain result required | no ad hoc normalization |
| 5 | prior record never overwritten | base plus immutable amendments | immutable revisions | stored payload unchanged |
| 6 | label has no effect; new ID | exact rule/result required | exact rule/result required | label cannot move stored data to display |
| 7 | creation/replacement provenance only | separate correction provenance | revision-specific provenance | no correction provenance needed for render |
| 8 | Module C used only for Objective supersession | separate amendment modules explicit | revision history mapped explicitly | no amendment/revision semantics |
| 9 | no new invoker | full independent invocation decision | current invocation remapped, not inherited | no invocation |
| 10 | one exact record, no head | exact amendment state, no latest | exact revision, no latest | no revision exists |
| 11 | changed stored typo creates new ID | typo remains stored and governed | typo remains stored and governed | cannot call stored typo display-only |
| 12 | consumers rebind explicitly | consumers bind exact amendment state | consumers bind exact revision | display change needs no rebind |
| 13 | new ID on uncertainty | conflict/missing rejects same identity | conflict/missing rejects same identity | stored ambiguity exits D |
| 14 | no equivalence re-evaluation | original exact rule/result preserved | original exact rule/result preserved | renderer cannot reclassify stored history |
| 15 | no promotion implication | no promotion implication | no promotion implication | no promotion implication |
| 16 | no new conclusion authority | amendment is correction evidence only | revision is representation only | renderer is implementation only |

## 28. Outcome-conditional executable plan

AD-017A adds no fixture because no outcome has been selected. A later implementation must add only the selected block plus the unconditional evidence in §14.

### 28.1 A

- add a synthetic harmless-typo pair with two Objective IDs and explicit supersession;
- prove an older Operation and assessment still resolve the prior Objective;
- prove branching successors have no newest winner; and
- keep the existing Objective/P-001/reference schemas unchanged unless another reviewed need appears.

### 28.2 B

- define and validate amendment identity, exact target/baseline, before/after evidence, rule/result/provenance and authoritative derivation;
- test missing, conflicting, branching, withdrawal/rollback and materialized-view mismatch;
- complete the separate P-001 decision; and
- add exact consumer snapshot evidence showing which amendment state was used.

### 28.3 C

- define and validate logical Objective identity, immutable revision identity and exact revision resolution;
- migrate Operation and assessment consumers that use corrected text;
- test missing, duplicate, branching, conflicting and floating-latest failures; and
- distinguish same-Objective revision from new-Objective Module C supersession.

### 28.4 D

- demonstrate several renderings of one byte-/payload-identical normative statement;
- prove renderer metadata cannot enter Objective identity or overwrite `statement`;
- reject a stored spelling or token change as display-only; and
- combine with the selected stored-change outcome when any such case remains in scope.

Executable coverage cannot select the outcome. A green implementation of B or C would prove only that one proposed contract was implemented, not that its additional authority was necessary.

## 29. Evidence-weighted comparison finding

Current evidence establishes:

1. Historical replay is a real requirement because Operation and assessment consumers bind Objective by bare ID.
2. No current consumer requires the same Objective ID to survive a changed stored statement.
3. A closes all twelve scenarios with accepted Objective identity, P-001 Module C and explicit consumer rebinds.
4. D is a valuable common invariant because pure rendering should never enter normative history, but D alone cannot close the stored orthographic case already named by OCP-008.
5. B can preserve same logical identity, but only by adding a second identified authority plus exact consumer correction-state evidence.
6. C provides the clearest positive revision replay, but changes the current P-001 identity model and every corrected-text consumer reference.

Therefore **A with D as its explicit payload/display safeguard is the leading minimal complete hypothesis for AD-017B**. This is not a selection. It is the hypothesis that adds the least new authority while satisfying all current consumers and counterexamples.

B becomes justified if external evidence identifies a consumer that must preserve logical Objective identity across changed stored text and independently needs an attributable amendment record. C becomes justified if the same need exists and exact immutable revisions are required across several consumers. D alone becomes complete only if the stored orthographic-correction permission is removed or every demonstrated same-identity case is proven to leave normative payload unchanged.

External review must attack the leading hypothesis by constructing:

1. a current or necessarily near-term consumer that A+D cannot satisfy without relying only on editing convenience;
2. an accepted mandate that requires identity preservation rather than merely permits it;
3. a B model that changes visible corrected text without floating old bare references or adding an exact consumer binding;
4. a C model that preserves current P-001 record identity and bare consumer compatibility without a floating latest revision;
5. a D-only answer for the stored-typo scenario; and
6. an omitted smaller outcome that preserves replay with less authority than A+D.

If any attack succeeds, AD-017B must not select A+D without resolving it.

## 30. Outcome-fairness closure audit

| Fairness question | A | B | C | D |
|---|---|---|---|---|
| own feasible evidence block | yes, immutable records/supersession | yes, conditional amendment lineage | yes, conditional exact revisions | yes, unchanged-payload/render separation |
| semantic replay equivalent | exact Objective ID | exact amendment state plus base | exact Objective revision | unchanged normative payload; stored change delegated |
| Pattern obligation assumes rejected layer | no | separate invocation only if selected | remapping only if selected | no Pattern layer |
| consumer migration charged explicitly | none | yes | yes | none for display-only |
| fail-safe on absent equivalence | new Objective | reject same-identity amendment effect | reject same-identity revision effect | exit D to strict outcome |
| main weakness stated without disqualification by design | identity duplication/cost | dual authority/branching | identity split/migration | incomplete for stored change |

The §16 falsification target remains closed: no unconditional evidence assumes the amendment, revision, domain or display layer of a competing outcome. B and C receive credit for replay only through their own exact equivalents; A is not penalized for rejecting a same-identity edit path; D is not asked for lineage it does not contain.

## 31. AD-017A status and next act

Revision `0.2.0` completes the initial A–D comparison while AD-017 and AB-063 remain `Discovery`. It changes no OCP-008 text/version/status, Objective status, P-001 invocation, consumer reference, Concept, registry row, graph edge, schema, checker rule, fixture or readiness percentage.

After exact-head external review, a separate AD-017B Board act may:

- select A with D as a representation safeguard;
- select B or C after closing its authority and migration gates;
- select another explicit composition with non-overlapping precedence;
- require another comparison because a viable outcome is missing; or
- retain strict immutability and close the positive same-identity correction path.

AD-017A review or merge does not select an outcome. AD-017B requires its own exact-head Fable review, Codex adjudication, green CI and explicit Pavlo/Architecture Board authorization. Any later OCP-008 implementation and any promotion-scope act remain separate again.
