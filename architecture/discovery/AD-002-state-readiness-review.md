---
Decision-ID: AD-002
Title: State and Readiness Review
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: ADR-DRAFT-007, OCP-004, OCP-005, OCP-006
Applies-To: State, Readiness and subsequent Foundation Concepts
Review-After: Accepted Operation and Assignment; Constraint and executable fixtures available
---

# AD-002 — State and Readiness Review

## 1. Trigger

The review trigger recorded for ADR-DRAFT-007 has now occurred:

- Operation is Accepted;
- Assignment is Accepted;
- Constraint is Accepted;
- executable lifecycle and derivation fixtures under `tools/ontology_checker/fixtures/` exist.

Continuing Wave 2 without reviewing the deferred State/Readiness decision would create governance drift.

## 2. Question

Determine whether `State` and `Readiness` should be:

1. separate fundamental Concepts;
2. one Concept plus a derived view;
3. domain-specific models rather than Core Concepts;
4. represented primarily through Constraint and time-bounded observations.

## 3. Non-blocking sequencing

AD-002 runs in parallel with Objective boundary discovery. It does not block Objective because Objective has no semantic dependency on the State/Readiness decision.

No new State or Readiness semantics are introduced by this decision.

## 4. Required evidence

The review must use at least:

- Operation lifecycle and state-like properties;
- Assignment effectivity and lifecycle projections;
- Constraint admissibility and indeterminate handling;
- concrete readiness examples for both Resource and Organization;
- counterexamples showing false conflation of capability, availability, admissibility and readiness.

## 5. Guardrails

- `Capability ≠ Readiness`.
- `Constraint satisfied ≠ Ready` unless a defining rule explicitly says so.
- lifecycle stage is not automatically operational State.
- absence of negative evidence is not positive readiness.
- no decision may create a generic state container without independent domain semantics.

## 6. Candidate outcomes

- Accept State and Readiness as separate Concepts.
- Accept Readiness and reject generic State.
- Accept a constrained State pattern but not a Concept.
- Keep both Deferred with explicit missing evidence and a new review trigger.

No candidate outcome is selected by AD-002 itself. AD-002 accepts the review mandate, evidence contract and guardrails under which the later decision must be made.

## 7. External review target

Attempt to falsify each candidate by constructing cases where it collapses identity, time, capability, admissibility or observation semantics.

## 8. Architecture Board decision

The Architecture Board accepts this review mandate after external adversarial review. State and Readiness remain `Deferred` until a subsequent decision evaluates the required evidence and selects or rejects a candidate outcome.
