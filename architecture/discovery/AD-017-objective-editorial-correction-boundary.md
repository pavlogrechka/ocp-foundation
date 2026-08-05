---
Decision-ID: AD-017
Title: Objective Editorial-Correction Boundary
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-001, OCP-008, OCP-016, P-001, AD-003, AD-016
Applies-To: AB-063, Objective statement correction, OCP-008 Canonical blocker
Review-After: External adversarial outcome comparison before any Architecture Board selection
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
