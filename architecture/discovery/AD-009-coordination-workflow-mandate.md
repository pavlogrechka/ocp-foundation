---
Decision-ID: AD-009
Title: Coordination Workflow Boundary
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: OCP-014, OCP-013, OCP-012, OCP-006, OCP-005, AB-058
Applies-To: AB-058, Coordination workflows, inter-vertical agreement
Review-After: External adversarial review and Architecture Board decision
---

# AD-009 — Coordination Workflow Boundary

## 1. Proposed mandate

AB-058 needs one bounded decision before any Coordination workflow is defined. This draft selects the following question for external review:

> What is the smallest human-readable, replayable workflow contract that lets independent verticals publish, inspect and confirm a coordination proposal while preserving each vertical's authority and without selecting, authorizing, reserving, allocating or mutating an Assignment?

The proposed cycle is deliberately about workflow evidence and agreement boundaries. It is not an implementation plan and does not accept a workflow model by itself.

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
