---
Decision-ID: AD-002
Title: State and Readiness Review
Version: 0.2.1
Status: Accepted
Owner: Architecture Board
Depends-On: ADR-DRAFT-007, OCP-004, OCP-005, OCP-006
Applies-To: State, Readiness and subsequent Foundation Concepts
Review-After: A separately accepted AD-011 reopening mandate supplies new State identity evidence or a concrete Readiness consumer with legitimate criterion, target and freshness owners
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

## 9. Post-AD-011 Review-After correction — v0.2.1

The prior `Review-After` named Accepted Operation and Assignment plus available Constraint and executable fixtures. Those conditions triggered AD-002 and were later fully adjudicated by AD-011; retaining them as a future trigger would present completed evidence as an open review gate.

Version `0.2.1` therefore aligns `Review-After` with the accepted independent reopening rule in AD-011 §25.3. It creates no State or Readiness Concept, record, conclusion, authority or positive-capable result; does not change AD-011 S0/R0, the negative identity verdicts, deregistration, AB-007 or any OCP; and keeps `Capability ≠ Readiness`. Either axis may reopen only through a separately accepted mandate carrying the exact new evidence and legitimate owners already required by AD-011.
