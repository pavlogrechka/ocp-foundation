---
Decision-ID: AD-010
Title: Cross-Vertical Visibility and Agreement Boundary
Version: 0.2.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-014, OCP-015, AD-009, AB-059
Applies-To: AB-059, cross-vertical visibility, agreement semantics
Review-After: External adversarial review and Architecture Board outcome selection
---

# AD-010 — Cross-Vertical Visibility and Agreement Boundary

## 1. Trigger and narrow mandate

The acceptance act for AD-009 and OCP-015 names AB-059 as the next normative cycle. That act deliberately leaves two questions open:

1. which evidence may be exposed across independent verticals and under whose policy; and
2. whether OCP needs a governed meaning of agreement beyond one actor's attributable response to one exact proposal revision.

AD-010 opens only that residual boundary. It does not reinterpret historical OCP-015 confirmations and does not preselect a visibility-policy model, an agreement model or a new record family.

The decision question is:

> What is the smallest human-readable and fail-safe contract that can determine whether exact evidence is within a cross-vertical visibility boundary and, separately, whether exact attributable records support any governed agreement conclusion, without turning visibility or confirmation into permission, authorization, consensus, selection, reservation, allocation or Assignment mutation?

## 2. Plain-language boundary

Three statements that sound similar in conversation must remain different:

- **"Vertical B can inspect this proposal evidence"** is a visibility statement.
- **"Vertical B confirmed revision R1"** is an OCP-015 response fact.
- **"The parties have a governed agreement"** would be a separate conclusion or attributable act whose authority is not yet selected.

For example, `relay-ops` may expose proposal `PROP-7-R1` to `airspace`. That exposure does not let `airspace` assign a Resource or authorize an Operation. If `airspace` confirms `PROP-7-R1`, the confirmation remains its own attributable response. It does not prove that every required party agreed, that the agreement is still effective, or that anyone may act.

AD-010 must keep those distinctions understandable without checker code.

## 3. Accepted inputs and inherited limits

AD-010 may consume the following accepted contracts without expanding their authority:

- OCP-014 owns one exact Coordination consumer requirement; it does not authenticate a caller or grant permission.
- OCP-015 owns immutable proposal and response evidence, exact revision binding, effectivity, provenance, history-preserving supersession and fail-safe evidence projection.
- An OCP-015 `positive` projection means only that required attributable confirmations exist for one exact evidence snapshot.
- AD-009 keeps authorization under AB-017, conflict resolution under AB-018 and AB-038, reservation and allocation under AB-025, and Assignment lifecycle alignment under AB-028.

AD-010 may reference those layers, but may not absorb or decide them.

## 4. Terms that must remain distinct

- **publication** — one actor makes an exact evidence item available through a stated mechanism;
- **receipt** — evidence that a recipient obtained or acknowledged an item, not proof that publication was authorized;
- **visibility envelope** — the publisher-declared recipients recorded by OCP-015;
- **visibility policy** — a governed rule or attributable decision about whether exact evidence is within a cross-vertical disclosure boundary;
- **permission or access enforcement** — authority and mechanism that allows or blocks access; not defined by this discovery;
- **confirmation** — one responder's OCP-015 response to one exact proposal revision;
- **agreement evidence** — exact records that may support a conclusion under a separately governed rule;
- **agreement conclusion** — a derived or attributable statement whose model is not yet selected;
- **operational commitment** — an obligation to act; not implied by visibility, confirmation or agreement evidence;
- **authorization** — permission to approve, select, assign, reserve, allocate or execute; outside AD-010;
- **consensus** — a collective decision rule; not assumed from response count or unanimity;
- **disagreement** — attributable non-confirmation or incompatible evidence; it is not automatically a Conflict Concept;
- **withdrawal** — a history-preserving change to one actor's own record, not deletion of another actor's evidence.

## 5. Authority separation

Every candidate outcome must assign narrow authority explicitly.

| Layer | Possible authority | Must not establish |
|---|---|---|
| Evidence publisher | Its own publication statement and declared envelope | recipient permission, agreement or authorization |
| Visibility-policy owner | The exact policy or decision it owns | truth of the disclosed evidence or operational authority |
| Recipient | Its own receipt, response or attributable assertion | another party's response or a shared conclusion by default |
| OCP-015 rule | Projection over exact proposal/response inputs | visibility permission, consensus or commitment |
| Agreement rule or evaluator | Only the exact conclusion selected by AD-010 | authorization, selection, reservation, allocation or Assignment mutation |
| Access-control implementation | Enforcement under a separately accepted contract | new OCP semantics merely because access was technically possible |

No layer inherits another layer's authority through labels, transport, caller identity, timestamps, record order or data possession.

## 6. Exact context obligations

Every admissible visibility or agreement outcome must explain how it binds, or explicitly declines to own, all of the following:

```text
evidence subject and exact revision
publisher or asserting actor
intended recipients or parties
operational context or purpose
policy or rule identifier and exact version
evaluation time and effectivity
input evidence snapshot
provenance
withdrawal or supersession history
```

If an accepted owner does not exist for a required field, the outcome must return an explicit evidence gap or assign that field to a separately reviewed downstream profile. Labels, Organization names, service accounts and implicit "current policy" are not valid substitutes.

This discovery does not accept a schema. The list is an obligation for comparing authority models.

## 7. Visibility-policy outcomes to compare

### V0 — publisher envelope only

Core retains the OCP-015 `visible_to_refs[]` declaration and adds no shared visibility-policy authority. A consumer can inspect what the publisher declared, but cannot present that declaration as permission or policy compliance.

This is the minimum-authority control. Its main risk is that independent verticals may interpret the same envelope incompatibly.

### V1 — deterministic governed policy evaluation

A versioned rule evaluates an exact evidence item, publisher, recipient, context, time and policy snapshot and returns a fail-safe result. The rule does not prove delivery and does not grant operational authorization.

This model is replayable, but it is admissible only if every input and precedence rule has a governed owner. Hidden local policy inside checker code invalidates the outcome.

### V2 — attributable disclosure decision

An identified record states that an accountable actor evaluated one exact disclosure under one exact policy and context. Correction and withdrawal preserve history.

This model can retain legitimate judgment, but the record must not become a universal permission token or allow one actor to speak for the recipient.

### V3 — domain-owned policy behind a Core envelope

Core governs only the exact input envelope and fail-safe minimums; each domain owns its visibility decision. The domain and policy version remain explicit in every result.

This model limits Core authority, but must reject cross-domain semantic mismatch rather than treating unlike domain decisions as interchangeable.

## 8. Agreement-semantics outcomes to compare

### A0 — no agreement authority beyond OCP-015

Core retains proposal and response evidence only. Consumers may say which exact actors confirmed, declined or withdrew, but cannot emit a canonical agreement conclusion.

This is the minimum-authority control. It is valid if no shared agreement invariant is demonstrated.

### A1 — deterministic agreement-evidence projection

A governed rule derives a narrowly named evidence result from exact proposal, response, party-set, effectivity and rule snapshots. Even a positive result means only that the selected evidence conditions are satisfied. It is not consensus, authorization or commitment.

This model is replayable, but the party-set owner and decision rule must be explicit. "All visible responders confirmed" is not a valid shortcut unless visibility and party membership are separately governed.

### A2 — attributable agreement record

One or more actors create identified records that bind the exact subject, parties, terms or proposal revision, effectivity, provenance and supersession history. The model must show how each party speaks only for itself and how a shared conclusion, if any, is formed without one writer impersonating the others.

This model preserves accountable acts, but risks being mistaken for approval or an operational commitment.

### A3 — domain-owned agreement profile

Core defines an interoperability envelope while a named domain owns agreement meaning and lifecycle. Cross-domain consumers must exact-bind the profile and fail safely on a profile mismatch.

This model supports domain-specific agreements, but may be rejected if it cannot preserve a shared minimum meaning across independent verticals.

## 9. Axes may not collapse into one another

Visibility and agreement are separate decision axes. Selecting one visibility outcome does not select an agreement outcome.

In particular:

```text
visible(evidence, recipient)
  does not imply
recipient_is_party
  or recipient_confirmed
  or agreement_exists
  or action_is_authorized
```

Likewise, an actor's historical confirmation does not prove that the evidence remains visible, that another actor agreed, or that a later proposal revision inherits the response.

Any combined model must justify why coupling is necessary, keep both authorities inspectable and provide counterexamples that fail if either side is missing or indeterminate.

## 10. Fail-safe result obligations

AD-010 does not yet accept a result vocabulary. Every candidate, including V0 and A0, must nevertheless distinguish:

- positive evidence under the exact selected contract;
- known negative or non-matching evidence;
- missing, stale, expired, ambiguous, conflicting, unresolved or out-of-scope evidence;
- a separately attributable review requirement, if human judgment is legitimate; and
- absence of a governed conclusion.

No candidate may collapse `indeterminate`, `review required` or `no governed conclusion` into a permissive result. Newest timestamp, list order, response count, majority and data possession never choose authority unless an independently accepted policy explicitly owns that rule.

Historical results bind their exact policy or rule version and input snapshot. A policy change, proposal revision, party-set change, withdrawal, expiry or context change creates a new evaluation context and does not rewrite prior evidence.

## 11. Mandatory examples and counterexamples

Every admissible outcome must explain, and assign executable evidence for where applicable:

1. a publisher exposes one exact proposal to an invited responder without granting permission to act;
2. an observer may inspect evidence but is not a party and cannot be counted toward agreement;
3. an invited responder confirms revision R1, while revision R2 receives no inherited confirmation;
4. every invited responder confirms, but no authorization or operational commitment exists;
5. one required party declines while another confirms;
6. a responder withdraws its own response without deleting the historical confirmation;
7. a publisher changes a visibility envelope through a valid superseding proposal revision without erasing evidence already received;
8. policy inputs are missing, stale, conflicting or bound to the wrong version;
9. an agreement rule receives an unresolved or changing party set;
10. one actor attempts to create a record that claims another actor agreed;
11. two domain profiles use the same label with incompatible meanings;
12. a transport or service account exposes data even though no governed visibility conclusion exists;
13. a positive visibility result is incorrectly reused as authorization, selection, reservation or allocation;
14. response count, timestamp or list order is incorrectly used to manufacture agreement; and
15. the same exact evidence snapshot replays identically regardless of input record order.

Examples must remain non-sensitive and understandable without implementation code.

## 12. Forbidden shortcuts

AD-010 must reject any outcome that:

1. treats `visible_to_refs[]` as permission or proof of delivery;
2. treats receipt or technical access as policy compliance;
3. treats one actor's confirmation as another actor's statement;
4. treats all confirmations as consensus, authorization or commitment by default;
5. infers parties from visibility, Organization labels or transport recipients;
6. carries a response across proposal revisions or contexts;
7. deletes historical evidence when visibility, response or agreement changes;
8. resolves conflicting evidence by newest timestamp, majority, list order or source count;
9. hides policy ownership or agreement meaning inside code;
10. uses an opaque "current policy" or latest-version lookup;
11. lets a domain-specific result masquerade as a Core-wide conclusion;
12. creates selection, reservation, allocation or Assignment authority;
13. creates a new fundamental Concept or Concept graph edge without a separate identity decision; or
14. stores or introduces sensitive operational data into Foundation examples.

## 13. Explicitly not defined

AD-010 does not define:

- authentication, delegation, signatures or identity federation;
- data classification, releasability labels or a universal information-security taxonomy;
- production access control, encryption, transport, delivery, notification or audit infrastructure;
- approval, command, authorization or operational commitment;
- voting, quorum, consensus, arbitration or conflict-resolution policy;
- availability, Readiness, capacity, ranking or selection;
- reservation, allocation, replacement or Assignment amendment;
- a production API, persistence schema or workflow engine;
- a new fundamental Concept or Concept graph edge.

If a candidate needs any excluded authority, it must name the separate backlog owner rather than importing it into AB-059.

## 14. Evidence obligations and exit criteria

Before an Architecture Board outcome selection, this discovery must provide:

1. a fair comparison of V0–V3 and A0–A3, including the no-new-authority controls;
2. one non-sensitive scenario with at least two independent verticals and one observer;
3. an authority table for every normative field and result;
4. exact input, replay, expiry, withdrawal and supersession behavior;
5. a decision on whether visibility and agreement remain independent contracts;
6. explicit handling of every fail-safe state and mandatory counterexample;
7. an executable-evidence plan assigned to each downstream normative owner;
8. separate accounting for every unresolved authentication, authorization, security, consensus or conflict question;
9. confirmation that conceptual meaning remains clear without checker code; and
10. external adversarial review of the exact head before any acceptance act.

AD-010 remains `Discovery` if evidence cannot distinguish the models, if a required authority owner is implicit, or if a candidate depends on an excluded layer. Acceptance additionally requires Codex adjudication, green exact-head CI and explicit Pavlo or Architecture Board authorization before squash merge.

## 15. Questions for external adversarial review

Fable should try to falsify whether:

1. visibility, receipt, confirmation, agreement and authorization remain genuinely separate;
2. V0 and A0 receive fair evidence rather than being treated as incomplete implementations;
3. every non-control model names a legitimate authority owner;
4. a visibility result can be misread as access permission;
5. an agreement result can be misread as consensus or operational commitment;
6. party membership can drift or be inferred from visibility;
7. withdrawal and policy change preserve historical evidence;
8. conflicting or unresolved inputs fail closed without timestamp, order or majority authority;
9. domain-owned models expose semantic mismatch; and
10. the document remains human-readable and does not broaden beyond AB-059.

## 16. Outcome comparison working analysis

This revision compares the two decision axes for external review. It does not select a visibility outcome, an agreement outcome, a combined pair or a result vocabulary.

The comparison uses four rules:

1. V0 and A0 are full no-new-authority controls, not incomplete implementations.
2. Each non-control model must expose a legitimate owner for every conclusion and input it adds.
3. A model is compared against observable behavior and counterexamples, not against record count or implementation convenience.
4. A visibility verdict and an agreement verdict are recorded separately. A strength or weakness on one axis cannot decide the other.

The working verdicts below mean only:

- **admissible control** — safe when no shared conclusion is justified, but intentionally unable to emit one;
- **leading hypothesis** — the smallest currently plausible shared model, subject to the named evidence gates;
- **conditional alternative** — admissible only if a concrete need for its additional authority is demonstrated; and
- **not admissible under the stated condition** — the model fails closed rather than importing an implicit owner or excluded authority.

These are comparison results for falsification. They are not Architecture Board selections.

## 17. First cross-vertical scenario

A non-sensitive scenario supplies the comparison pressure:

> The independent `relay-ops` vertical publishes exact proposal revision `PROP-7-R1` for a shared coordination window. The independent `airspace-control` vertical is an invited responder. The `safety-audit` vertical may inspect some evidence as an observer but is not a party. `relay-ops` declares a visibility envelope containing both other verticals. `airspace-control` confirms R1; `safety-audit` records receipt only. No accepted contract yet says that the declared envelope is permitted by policy or that the response records constitute a governed agreement.

Every model must explain at least these changes without rewriting history:

1. `PROP-7-R2` supersedes R1 but receives no inherited response;
2. a policy snapshot expires or two policy inputs conflict;
3. `airspace-control` declines or withdraws its own response;
4. the observer can inspect evidence but remains outside the party set;
5. a service account delivers evidence even though no governed visibility conclusion exists;
6. every invited responder confirms, but no authorization or operational commitment exists; and
7. the same exact inputs are replayed in a different record order.

The scenario deliberately separates four questions: what the publisher declared, what a recipient technically received, what visibility policy concludes and what agreement evidence supports. No model may answer an unselected question by reusing a label from another layer.

## 18. Visibility-axis comparison and verdicts

All visibility models answer one narrow question: who, if anyone, may state that one exact evidence item is within a governed cross-vertical disclosure boundary for one recipient, context, time and policy snapshot. None grants access, proves delivery or authorizes action.

### 18.1 Human-readable comparison

| Model | Plain-language meaning | Added authority | Main advantage | Main risk | Separate working verdict |
|---|---|---|---|---|---|
| V0 — publisher envelope only | Consumers can report whom the publisher named, but cannot call that declaration policy compliance or permission. | None beyond the publisher's attributable declaration. | Smallest authority footprint; exactly preserves OCP-015. | Independent consumers may need a shared visibility conclusion that V0 deliberately cannot provide. | **Admissible control.** It remains the correct outcome if no shared policy invariant and owner are demonstrated. |
| V1 — deterministic governed policy evaluation | A versioned rule evaluates exact evidence, publisher, recipient, context, time and policy inputs. | The accepted rule owner may emit one replayable policy result. | Same exact inputs replay to the same result; missing inputs can fail closed mechanically. | Hidden precedence, implicit current policy or an unowned input can masquerade as deterministic authority. | **Leading hypothesis** when every input, precedence rule and policy version has an accepted owner. Otherwise it is **not admissible** and V0 remains the safe control. |
| V2 — attributable disclosure decision | An accountable actor records its decision for one exact disclosure under one exact policy and context. | That actor may state only its own attributable disclosure conclusion. | Preserves legitimate judgment, provenance, correction and withdrawal. | The record can be mistaken for recipient permission or reused outside its exact context. | **Conditional alternative** when legitimate non-deterministic judgment must be retained. It is not justified merely to cache a V1 result. |
| V3 — domain-owned policy behind a Core envelope | A named domain evaluates visibility under its own versioned policy while Core governs exact bindings and fail-safe minimums. | The named domain owns only its domain result. | Keeps domain-specific releasability meaning outside Core. | Structurally similar results may carry incompatible meanings across domains. | **Conditional alternative** when domain ownership is essential and profile mismatch is mechanically rejected. It is **not admissible** as an unlabeled Core-wide result. |

### 18.2 Visibility decision-separating evidence

External review should distinguish the models with these questions:

- Is a shared, replayable visibility-policy conclusion required by a concrete cross-vertical consumer, or is V0 sufficient?
- Can every policy input and precedence rule be exact-bound and governed without evaluator judgment?
- If judgment remains, does a consumer need the attributable V2 decision later, or only a non-authoritative review request?
- Does a domain genuinely own different visibility meaning, and can V3 reject rather than normalize cross-domain mismatch?
- Can the chosen model explain why receipt, successful transport and caller access do not prove its conclusion?

V1 is the current minimum-authority hypothesis for a shared visibility conclusion. That hypothesis fails if the policy owner, exact version, context or precedence rule is implicit. V2 becomes preferable only when accountable judgment is a demonstrated part of the contract. V3 remains viable only for a named domain boundary with explicit mismatch behavior. V0 remains fully valid if no shared conclusion is needed.

## 19. Agreement-axis comparison and verdicts

All agreement models answer a different question: who, if anyone, may state a governed conclusion from exact attributable proposal, response, party-set, effectivity and rule evidence. None creates consensus, approval, authorization or an operational commitment.

### 19.1 Human-readable comparison

| Model | Plain-language meaning | Added authority | Main advantage | Main risk | Separate working verdict |
|---|---|---|---|---|---|
| A0 — OCP-015 evidence only | Consumers may report each actor's exact response, but there is no canonical agreement conclusion. | None beyond existing proposal and response evidence. | Adds no party-set, consensus or shared-conclusion authority. | Consumers may invent incompatible local meanings of “agreement.” | **Admissible control and current default.** It remains correct until a governed shared conclusion and its owner are demonstrated. |
| A1 — deterministic agreement-evidence projection | A versioned rule tests exact evidence against an exact governed party set and returns a narrowly named evidence result. | The accepted rule owner may emit only the selected evidence conclusion. | Replayable and small when party membership, rule inputs and effectivity are fully governed. | Visibility or response count can silently become party-set or consensus authority. | **Leading hypothesis for a shared conclusion**, but only after the party-set owner, rule owner and result wording are accepted. Without them A1 is **not admissible** and A0 remains the default. |
| A2 — attributable agreement record | Each actor records only its own act; any shared conclusion has a separately governed formation rule and provenance. | Identified actors may state their own acts; a distinct accepted owner would be required for any shared conclusion. | Can preserve accountable intent, correction, withdrawal and legitimate judgment. | One writer may appear to speak for all parties, or the record may be mistaken for approval or commitment. | **Conditional alternative** when a concrete consumer requires attributable agreement acts beyond OCP-015 responses. It is not justified by confirmation alone. |
| A3 — domain-owned agreement profile | A named domain owns agreement meaning and lifecycle inside an exact Core interoperability envelope. | The domain owns only the exact profile result. | Supports legitimate domain-specific meaning without making it universal Core semantics. | Identical labels can hide incompatible party, effectivity or withdrawal rules. | **Conditional alternative** when shared Core meaning would be false and exact profile mismatch fails closed. It is **not admissible** as an unlabeled cross-domain conclusion. |

### 19.2 Agreement decision-separating evidence

External review should distinguish the models with these questions:

- Does any accepted consumer require more than a list of attributable OCP-015 responses?
- Who owns the exact party set, and can it change without being inferred from visibility or transport recipients?
- Is the desired result a deterministic evidence conclusion, a party's attributable act, or both through separately reviewed layers?
- Can A1 name a result that cannot reasonably be read as consensus, approval, authorization or commitment?
- Can A2 prove that each actor speaks only for itself and that correction or withdrawal never rewrites another actor's record?
- Can A3 reject incompatible domain profiles before a consumer compares their results?

A0 is the current default because OCP-015 already preserves the evidence and no further agreement authority has been accepted. A1 is the current minimum-authority hypothesis only if a concrete consumer needs a shared conclusion and separately accepted owners exist for the party set and rule. A2 requires demonstrated accountable acts not already represented by OCP-015. A3 requires genuinely domain-specific meaning plus exact profile binding.

## 20. Axis independence and pair behavior

No V/A pair is selected by this comparison. Every visibility model can coexist with every agreement model only if both contracts remain independently inspectable.

Examples:

- V1 + A0 may provide a governed visibility conclusion while retaining proposal and response evidence without an agreement conclusion.
- V0 + A1 may derive a governed agreement-evidence conclusion from evidence already held under a separate access contract while Core adds no visibility-policy conclusion.
- V2 + A2 creates two attributable records with different owners; neither record may stand in for the other.
- V3 + A3 may use different domain profiles and versions. A shared domain label does not prove that the profiles or authorities match.

A combined implementation is admissible only if removing either axis changes only that axis's result. If a missing visibility result changes party membership, or a positive agreement result grants visibility, the implementation has coupled the contracts and must fail review.

### 20.1 Fail-safe behavior by axis

| Evidence condition | Visibility-axis behavior | Agreement-axis behavior |
|---|---|---|
| Exact complete evidence satisfies the selected contract | V1–V3 may emit only their exact selected visibility result; V0 reports the declaration and `no governed visibility conclusion`. | A1–A3 may emit only their exact selected agreement-evidence result; A0 reports attributable responses and `no governed agreement conclusion`. |
| Known governed mismatch | A selected rule may return its narrowly defined negative result; it does not revoke evidence or prove access denial. | A selected rule may return its narrowly defined negative result; it does not manufacture disagreement, Conflict or authorization. |
| Missing required input or owner | `indeterminate` for V1–V3; V0 remains declaration-only. | `indeterminate` for A1–A3; A0 remains evidence-only. |
| Stale, expired or wrong-version input | A new evaluation context is required; the historical result remains bound to its old snapshot. | A new evaluation context is required; historical responses and results are not rewritten. |
| Ambiguous, conflicting or unresolved input | Non-permissive `indeterminate`, or `review required` only when the selected contract owns such a route. | Non-permissive `indeterminate`, or `review required` only when the selected contract owns such a route. |
| Out-of-scope recipient, party, domain or profile | No cross-boundary conclusion; profile mismatch must be explicit. | No shared conclusion; party or profile mismatch must be explicit. |
| Human judgment is legitimate but no evaluator authority is accepted | `review required` or `no governed conclusion`, never an inferred V2 result. | `review required` or `no governed conclusion`, never an inferred A2 result. |

No state in this table grants temporary access or action. `Negative`, `indeterminate`, `review required` and `no governed conclusion` remain different outcomes.

## 21. Normative authority accounting

The following table accounts for every exact-context obligation from §6. “Unselected” is an explicit evidence gap, not permission for an implementation to choose an owner.

| Binding or result | Visibility-axis owner | Agreement-axis owner | Fail-safe obligation |
|---|---|---|---|
| Evidence subject and exact revision | OCP-015 evidence publisher and exact proposal/record identity | OCP-015 proposal and response identities | Zero, multiple or cross-revision matches cannot yield a positive result. |
| Publisher or asserting actor | Publisher for its own declaration; V2 decision actor for its own record | Each OCP-015 responder or A2 actor speaks only for itself | Caller identity, service accounts and Organization labels cannot replace attribution. |
| Intended recipients | OCP-015 publisher owns only the declared envelope; V1–V3 need a separately accepted policy owner for a policy conclusion | Not a party-set source | Visibility never establishes party membership. |
| Intended parties | Not a visibility-policy conclusion | Party-set owner is **unselected** for A1–A3 | A0 remains the default and A1–A3 remain non-authoritative until ownership is accepted. |
| Operational context or purpose | Selected V1 rule owner, V2 decision profile owner or V3 domain profile owner | Selected A1 rule owner, A2 record profile owner or A3 domain profile owner | An implicit caller context or free-text label is insufficient. |
| Policy or rule identifier and exact version | None under V0; selected V1/V2/V3 contract under its named owner | None under A0; selected A1/A2/A3 contract under its named owner | “Current” or latest-version lookup cannot reinterpret history. |
| Evaluation time and effectivity | Selected visibility contract, using exact evidence and policy effectivity | Selected agreement contract, using exact proposal, response, party-set and rule effectivity | Temporal mismatch is `indeterminate`, not positive. |
| Input evidence snapshot | Selected rule or decision contract must bind the finite OCP-015 and policy inputs | Selected rule or record contract must bind the finite proposal, response, party-set and rule inputs | Record order or later evidence cannot change a historical snapshot. |
| Provenance | Source record owners plus the selected evaluator or decision actor | Source record owners plus the selected rule/evaluator/actor | Provenance does not become authorization. |
| Withdrawal or supersession history | OCP-015 for proposal evidence; V2/V3 owner for any added decision lifecycle | OCP-015 for responses; A2/A3 owner for any added record lifecycle | History is appended or superseded, never erased or reassigned. |
| Visibility result | No governed result under V0; selected V1 rule, V2 actor or V3 domain owns only the exact result | No authority over agreement | A result does not prove delivery, access permission or action authorization. |
| Agreement result | No authority over agreement | No governed result under A0; selected A1 rule, A2 formation contract or A3 domain owns only the exact result | A result does not establish consensus, approval, commitment or action authorization. |

### 21.1 Excluded authority ledger

| Unresolved question | Separate owner or disposition | Why it stays outside AD-010 |
|---|---|---|
| Actor authentication, delegation and signatures | Explicit evidence gap pending a separately accepted identity/security contract | Record attribution does not prove caller identity or delegated authority. |
| Access permission, enforcement, classification and releasability | Separate future security/access-control contract | A visibility-policy conclusion is semantic evidence, not an enforcement token. |
| Operation authorization or approval | AB-017 | Visibility and agreement evidence cannot authorize an Operation. |
| Reservation or allocation | AB-025 | Neither axis selects or reserves a Resource. |
| Assignment lifecycle change | AB-028 | Neither axis creates, amends or revokes Assignment participation. |
| Consensus, voting, quorum or arbitration | No owner selected; requires a separate accepted mandate | Response count or an agreement-evidence result cannot manufacture collective decision authority. |
| Conflict creation or resolution | AB-018 and AB-038 | Decline, mismatch or conflicting evidence is not automatically a Conflict Concept or resolution act. |

## 22. Mandatory counterexample mapping

The complete §11 set is mapped below. A range such as `V0–V3` or `A0–A3` means that every model on that axis must supply the stated behavior; it is not permission to test only one representative model.

| # | Counterexample pressure | Visibility applicability and required verdict | Agreement applicability and required verdict | Downstream executable-evidence owner |
|---|---|---|---|---|
| 1 | Publication to an invited responder grants no permission to act | **V0–V3:** preserve publication or the selected visibility result, but expose no permission or authorization field. | **A0–A3:** invitation alone produces no response or agreement conclusion. | OCP-015 compatibility fixture plus every selected V contract. |
| 2 | An observer can inspect evidence but is not a party | **V0–V3:** observer visibility may be reported under the exact model. | **A0–A3:** observer is excluded unless the independently governed party set includes it; visibility is never party evidence. | Joint V/A boundary fixture owned by the selected contracts; A1–A3 must bind the party-set source. |
| 3 | R1 is confirmed; R2 inherits nothing | **V0–V3:** a new proposal revision is a new evidence subject and evaluation context. | **A0–A3:** only R1 has the response; R2 cannot be positive from inherited evidence. | OCP-015 exact-revision fixture reused by every selected V/A contract. |
| 4 | Every invited responder confirms, but no authorization or commitment exists | **V0–V3:** visibility says nothing about response authority or action. | **A0:** reports confirmations only. **A1–A3:** any positive result is narrowly named and explicitly non-authorizing and non-committing. | Every selected A contract, with a forbidden-coupling assertion in the V contract where applicable. |
| 5 | One required party declines while another confirms | **V0–V3:** both records may remain visible without choosing a winner. | **A0:** reports both facts. **A1–A3:** cannot produce a positive result that requires all parties; no newest/count/majority rule. | OCP-015 mixed-response fixture plus every selected A contract. |
| 6 | A responder withdraws only its own response | **V0–V3:** withdrawal does not erase previously visible evidence or another actor's records. | **A0–A3:** historical confirmation remains; the current exact snapshot reflects withdrawal without turning it into another actor's decline. | OCP-015 withdrawal fixture; A2/A3 add lifecycle evidence if selected. |
| 7 | A superseding proposal changes the declared visibility envelope | **V0:** reports each historical declaration. **V1–V3:** evaluate each exact revision and policy snapshot separately; no retroactive erasure. | **A0–A3:** responses and party conclusions remain bound to their exact proposal revision. | OCP-015 proposal-supersession fixture plus every selected V contract. |
| 8 | Policy inputs are missing, stale, conflicting or wrong-version | **V0:** emits no policy conclusion. **V1–V3:** `indeterminate`, never positive or implicit current-policy fallback. | **A0–A3:** a visibility-policy gap does not alter agreement evidence or results. If an agreement contract has its own missing or mismatched rule/profile input, A1–A3 independently return `indeterminate`. | Each non-control rule/record/profile owner. |
| 9 | Party set is unresolved or changes | **V0–V3:** no inference from recipients or visible actors. | **A0:** reports evidence without a shared conclusion. **A1–A3:** `indeterminate` until an exact governed party-set snapshot exists; change creates a new context. | Every selected A contract; party-set owner must be accepted before positive fixtures. |
| 10 | One actor claims that another actor agreed | **V0–V3:** access to the statement does not validate it. | **A0–A3:** never treat it as the other actor's response or act; only each actor's own exact record may speak for it. | OCP-015 actor-binding fixture; A2/A3 add impersonation rejection if selected. |
| 11 | Two domain profiles reuse a label with incompatible meanings | **V0:** label has no policy authority. **V1/V2:** exact rule/profile mismatch cannot resolve by label. **V3:** must explicitly reject cross-domain mismatch. | **A0:** label has no agreement authority. **A1/A2:** exact rule/profile mismatch fails closed. **A3:** must explicitly reject cross-domain mismatch. | V3/A3 Core-envelope conformance suites; all other selected models test exact version binding. |
| 12 | Transport exposes data without a governed visibility conclusion | **V0:** technical exposure remains distinct from the declaration. **V1–V3:** receipt or transport success cannot manufacture a positive result. | **A0–A3:** possession or receipt cannot establish party status, response or agreement. | Every selected V contract plus an axis-boundary fixture for the selected A contract. |
| 13 | A positive visibility result is reused as authorization, selection, reservation or allocation | **V1–V3:** reject forbidden output coupling; **V0:** declaration cannot be upgraded to a positive policy result. | **A0–A3:** no agreement conclusion may be inferred from the visibility result. | Every selected V contract; AB-017 and AB-025 remain downstream owners of their own authority. |
| 14 | Count, timestamp or list order manufactures agreement | **V0–V3:** no ordering or count authority leaks from visible evidence. | **A0:** reports records only. **A1–A3:** exact rule inputs are order-independent; no newest, majority or count shortcut unless separately accepted. | OCP-015 order fixture plus every selected A contract. |
| 15 | Exact snapshot replay changes when input order changes | **V0:** declaration projection remains identical. **V1–V3:** exact result is identical for the same snapshot and contract version. | **A0:** evidence projection remains identical. **A1–A3:** exact result is identical for the same snapshot, party set and rule/profile version. | Every selected V/A contract, with permutation fixtures owned by its normative checker. |

## 23. Executable-evidence plan by candidate owner

This discovery does not add checker code. It assigns future evidence so that outcome selection cannot leave a positive authority without a falsification owner.

| Candidate | Required downstream normative owner and evidence |
|---|---|
| V0 | OCP-015 compatibility suite: exact declared-envelope projection, revision history, technical-receipt separation and order independence. |
| V1 | A selected visibility-rule contract: exact policy/input manifest, positive/negative/indeterminate cases, version replay, precedence rejection and all applicable §22 fixtures. |
| V2 | A selected disclosure-decision profile: actor binding, exact policy/context snapshot, correction/withdrawal history, impersonation rejection and forbidden permission-token reuse. |
| V3 | A selected Core envelope plus each participating domain profile: exact domain/profile binding, unknown-profile rejection and incompatible-meaning fixtures. |
| A0 | OCP-015 compatibility suite: exact response attribution, mixed responses, withdrawal, cross-revision rejection and order independence. |
| A1 | A selected agreement-evidence rule contract: exact party-set and rule manifests, effectivity, deterministic replay, fail-safe states and forbidden consensus/authorization coupling. |
| A2 | A selected attributable-record profile: self-only actor authority, any separately governed formation rule, immutable history, correction/withdrawal and impersonation rejection. |
| A3 | A selected Core envelope plus each participating domain profile: exact agreement-profile binding, lifecycle semantics, unknown-profile rejection and cross-domain mismatch fixtures. |

The Architecture Board may select no downstream contract on either axis. In that case V0 or A0 remains the accepted control and no placeholder schema, evaluator or fixture family is created merely to make the repository look complete.

## 24. Comparison status and next decision gate

Revision `0.1.0` opened AD-010 and AB-059 in `Discovery`. Fable reviewed exact head `0ce5544`, found no blocking issue, and recommended acceptance with two non-blocking observations: map all fifteen counterexamples to every applicable model and record separate verdicts for the V and A axes. Codex accepted those observations as obligations of this comparison stage.

Revision `0.2.0` supplies that comparison, the independent-vertical scenario, per-axis working verdicts, exact authority accounting, fail-safe behavior and the full counterexample-to-owner map. It does not record an Architecture Board outcome selection.

External adversarial review must now try to falsify the comparison on its exact head. Before any later selection, the review must determine separately:

1. whether V0 remains sufficient or a concrete consumer justifies V1, V2 or V3;
2. whether A0 remains sufficient or a concrete consumer justifies A1, A2 or A3;
3. whether every positive-capable candidate has an accepted owner for all exact inputs and results;
4. whether the full §22 map is fair to the controls and executable for each applicable model; and
5. whether either axis still imports receipt, permission, party membership, consensus, authorization, selection, reservation, allocation, Conflict or Assignment authority.

If the evidence does not distinguish models on one axis, that axis remains in `Discovery` even if the other axis is ready for selection. A later Board act must name separate V and A outcomes, including V0 or A0 where appropriate. Exact-head Fable approval, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization remain mandatory before squash merge of any selection act.
