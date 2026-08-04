---
Decision-ID: AD-009
Title: Coordination Workflow Boundary
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-014, OCP-013, OCP-012, OCP-006, OCP-005, AB-058
Applies-To: AB-058, Coordination workflows, inter-vertical agreement
Review-After: AB-059 cross-vertical visibility and agreement-semantics review
---

# AD-009 — Coordination Workflow Boundary

## 1. Accepted mandate

AB-058 required one bounded decision before any Coordination workflow could be defined. The accepted decision answers the following question:

> What is the smallest human-readable, replayable workflow contract that lets independent verticals publish, inspect and confirm a coordination proposal while preserving each vertical's authority and without selecting, authorizing, reserving, allocating or mutating an Assignment?

The accepted cycle is deliberately about workflow evidence and agreement boundaries. It is not an implementation plan and does not authorize operational action by itself.

## 2. In scope

The external review must compare narrowly bounded alternatives for:

1. a proposal's identity, version and lifecycle from draft through confirmation or withdrawal;
2. the minimum information that may be visible across independent verticals;
3. explicit confirmation and non-confirmation, including expiry and withdrawal evidence;
4. provenance, actor attribution and replay of the workflow history;
5. fail-safe handling of stale, conflicting, incomplete or unauthorized inputs;
6. the boundary between a coordination record and the authority that owns each underlying decision.

The review must provide human-readable examples and counterexamples for at least two independent verticals and for disagreement between them.

## 3. Explicit exclusions

This mandate does not define or imply:

- authorization, approval, command or control;
- negotiation, consensus, arbitration or conflict-resolution authority;
- availability, readiness, capacity or suitability;
- ranking, selection, reservation, allocation or replacement;
- mutation of an existing Assignment or any Resource identity;
- a new fundamental Concept or Concept-graph edge;
- a universal visibility policy or a permission system;
- automatic promotion of a proposal into an operational commitment.

OCP-014 remains the consumer-profile boundary. Its owner-scoped coordination requirement and the OCP-006, OCP-012 and OCP-013 contracts remain authoritative inputs, not workflow authority.

## 4. Required boundary tests

Any candidate outcome must show that:

- a proposal can be revised without silently rewriting prior evidence;
- a vertical can decline or withdraw without that event becoming an authorization;
- visibility of a fact does not grant permission to act on it;
- confirmation is attributable, time-bounded and distinct from selection or Assignment;
- missing, stale, conflicting or out-of-scope evidence fails closed;
- each normative field has an identified owner, and no field is inferred from labels or record order.

The candidate must identify which portions are deterministic derivation, which are attributable records, and which remain an explicit evidence gap.

## 5. Deliverables and exit condition

The next normative PR must include:

1. one selected workflow boundary with a plain-language rationale;
2. a comparison of rejected alternatives and the authority each would introduce;
3. executable or machine-checkable fixtures for positive, negative, indeterminate and withdrawal cases;
4. updated AB-058 and roadmap pointers that preserve any unresolved semantics;
5. an external adversarial review and an explicit Architecture Board decision.

Until those gates pass, this document remains a draft mandate. It pre-authorizes no Coordination workflow cycle and cannot be used as authority for selection, reservation, replacement or Assignment mutation.

## 6. Outcome comparison

The reviewed mandate can be satisfied through materially different authority shapes:

| Outcome | Shape | Benefit | Main risk | Fair evidence form |
|---|---|---|---|---|
| A — one mutable workflow object | Proposal, responses and current stage share one object. | Simple read model. | One writer can overwrite another vertical's evidence or hide prior states. | Replay every revision and reject any in-place semantic rewrite. |
| B — proposal plus response records | One immutable proposal revision is separate from each vertical's attributable response. | Preserves independent authors and allows disagreement without inventing an arbiter. | Requires exact head resolution for two record families. | P-001 identity, effectivity and supersession fixtures for both families. |
| C — generic event stream | Every proposal and response action is an event in one append-only stream. | Rich audit history. | Stream order can silently become authority, and generic events can hide domain semantics. | Replay from explicit causation and reject timestamp or order as an authority rule. |
| D — derived only | Current workflow state is derived from OCP-014 requirements and downstream activity. | Adds no stored workflow authority. | Withdrawal, disagreement and attributable confirmation have no shared governed home. | Bound snapshot replay plus an explicit evidence-gap result. |
| E — domain-local workflows | Each vertical keeps its own workflow and Core exposes only an envelope. | Preserves domain autonomy. | Cross-vertical meaning can drift or collapse confirmation into permission. | Domain fixtures plus ambiguity detect-and-reject at the envelope boundary. |

### 6.1 Unconditional evidence obligations

Every outcome must prove, in its own form, that:

1. revisions do not rewrite earlier evidence;
2. visibility does not grant permission;
3. confirmation, decline and withdrawal do not authorize or select anything;
4. stale, incomplete, conflicting or unresolved evidence never yields a permissive result;
5. actor and provenance attribution remain visible;
6. no timestamp, list order, label or record count chooses authority; and
7. Resource and Assignment identity remain unchanged.

### 6.2 Outcome-conditional obligations

- A must prove authoritative history and mutual-writer isolation despite one stored object.
- B must prove independent record identity, exact proposal binding, responder-scoped head resolution and history-preserving withdrawal.
- C must prove causation without treating arrival order or newest timestamp as authority.
- D must replay an exact snapshot and return an explicit evidence gap where attributable confirmation or withdrawal is unavailable.
- E must expose domain authority and reject ambiguous cross-domain mappings.

The comparison fails if an evidence obligation assumes a layer rejected by the outcome being tested.

## 7. Accepted AD-009A selection

AD-009A selects Outcome B: one `CoordinationProposalRecord` revision plus separate `CoordinationResponseRecord` assertions.

In plain language, one vertical may publish a proposal without writing another vertical's answer. Every invited vertical answers for itself with a separate attributable record. A new proposal revision supersedes rather than rewrites the previous revision. A response may confirm, decline or withdraw only that responder's earlier response. None of those records grants permission, selects a Resource or changes an Assignment.

Outcome B is accepted because the mandate requires shared, replayable evidence of publication, disagreement and withdrawal. Outcome D cannot retain that evidence; Outcome A concentrates writers; Outcome C adds a generic ordering authority; Outcome E does not by itself guarantee cross-vertical meaning. Exact-head external review, Codex adjudication and explicit Architecture Board authorization completed this selection.

## 8. Accepted contract and effect

Accepted OCP-015 defines the complete record and projection contract. It invokes P-001 separately for proposal and response records and uses only Modules A and C. It does not use Module B: current state is derived from immutable record heads, not a shared mutable lifecycle field.

The accepted effect is:

- AD-009 is `Accepted` at version `0.2.0`;
- OCP-015 is the accepted workflow-evidence boundary;
- AB-058 is `Resolved` for this narrow record-and-projection contract;
- authorization remains under AB-017; selection, reservation and allocation remain under AB-025; conflict resolution remains under AB-018 and AB-038; and Assignment lifecycle alignment remains under AB-028;
- the same acceptance act atomically creates AB-059 for cross-vertical visibility policy and negotiation, consensus or agreement semantics beyond the proposal-response boundary; and
- no new fundamental Concept or Concept graph edge is introduced.

AD-009 and OCP-015 are `Accepted`, AB-058 is `Resolved`, and residual cross-vertical visibility and agreement-semantics questions are owned by AB-059 without expanding this contract.
