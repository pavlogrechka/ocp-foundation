---
Decision-ID: AD-010
Title: Cross-Vertical Visibility and Agreement Boundary
Version: 0.1.0
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
