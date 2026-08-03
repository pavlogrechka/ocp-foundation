---
Decision-ID: AD-003
Title: Objective Boundary
Version: 0.2.1
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-004
Applies-To: Objective Concept and PR-0009
Review-After: External adversarial boundary review
---

# AD-003 — Objective Boundary

## 1. What is Objective?

Objective is a candidate fundamental Concept representing an intended outcome, condition, or effect of operational activity.

Objective is semantically complete without an existing Operation. An Objective may exist before any Operation is planned and may later be shared by, supported by, or referenced from multiple Operations.

Operation is the primary current consumer considered by this discovery because OCP-004 already defines an `objective_ref` bootstrap branch. Operation is not part of Objective identity or its canonical definition.

This discovery does not yet define Objective fields, lifecycle, hierarchy, achievement semantics, or authorization sources.

## 2. What is Objective not?

Objective is not automatically:

- an Order;
- a Task;
- an Operation;
- an Assignment;
- a Constraint;
- a Capability;
- an Event;
- a Result;
- an `ExplicitIntentRecord`;
- proof that an intended outcome was achieved.

A source that authorizes, requests, or originates an Objective does not become part of Objective identity merely because provenance points to it.

Objective and `ExplicitIntentRecord` are distinct representations. Their coexistence, precedence, conflict handling, and any explicit promotion or replacement rule must be defined by PR-0009 rather than inferred from the current OCP-004 disjunction.

## 3. Who creates Objective?

Creation is described only as an attributable act recorded through opaque provenance.

AD-003 does not introduce `Authority`, `Commander`, `Approver`, `Policy`, or `Order` as required Concepts. The actor, process, or source responsible for creation remains domain-governed until separately defined.

## 4. Who uses Objective?

Candidate consumers include:

- Operation, as a resolvable purpose reference;
- planning and validation workflows;
- future Event and Result models when evaluating observed outcomes;
- Coordination when multiple Operations share, support, conflict with, or depend on intended outcomes.

Use by a Concept does not itself establish a normative `Concept-Depends-On` edge. Such an edge must be justified in the defining specification.

## 5. What does Objective depend on?

The initial hypothesis is that Objective has no mandatory dependency on another current fundamental Concept.

Operation may depend on Objective after PR-0009 closes the existing bootstrap branch for `objective_ref`. Objective does not depend on Operation merely because Operations consume it.

Any Objective relationship or decomposition model must be justified separately. If an identified relation record invokes P-001, it must declare the invoked version, selected modules, semantic owner, endpoints, provenance, and validation contract.

## 6. What is explicitly not defined?

AD-003 intentionally does not define:

- authorization or command semantics;
- Objective decomposition or hierarchy;
- priority, weighting, or optimization;
- achievement, success, failure, or completion evaluation;
- measurement and evidence;
- Event or Result semantics;
- task allocation;
- direct inheritance from parent Operation or Organization;
- automatic conversion of intent text into Objective;
- coexistence or precedence between Objective and `ExplicitIntentRecord`;
- whether a substantive change of intended outcome preserves Objective identity or requires a new Objective plus supersession;
- domain-specific objective taxonomies.

Evaluation of achievement belongs to later Event/Result work and must not be embedded into the Objective boundary by implication.

## 7. Required bootstrap evidence

PR-0009 must include a positive executable fixture in which an Operation outside Draft satisfies its purpose requirement through a resolvable Objective reference rather than an `ExplicitIntentRecord`.

This fixture closes the oldest remaining bootstrap branch introduced during the Operation correction cycle.

PR-0009 must also define the coexistence and precedence contract for OCP-004 invariant 2, including:

- whether Objective and `ExplicitIntentRecord` may both be present;
- the result when they conflict;
- whether either representation supersedes, promotes, or invalidates the other;
- whether the existing disjunction remains unchanged or is revised.

## 8. Review target

Attempt to falsify the boundary by constructing cases where:

1. Objective collapses into Order or Task;
2. provenance silently becomes authorization semantics;
3. achievement evaluation leaks Event or Result semantics into Objective;
4. Objective identity depends unnecessarily on Operation;
5. decomposition creates hidden Assignment, command, or inheritance semantics;
6. the proposed boundary cannot support the Operation bootstrap fixture without adding an undeclared Concept;
7. a substantive change of intended outcome makes Objective identity or supersession ambiguous;
8. Objective and `ExplicitIntentRecord` coexist without a deterministic precedence and conflict contract.

## 9. Exit criteria

Boundary discovery is ready for Architecture Board decision when:

- all six boundary questions have survived external adversarial review;
- no unresolved blocking boundary finding remains;
- dependencies proposed for PR-0009 are explicit and acyclic;
- the bootstrap fixture contract is accepted;
- coexistence and precedence semantics for Objective versus `ExplicitIntentRecord` are explicit PR-0009 deliverables;
- Objective identity under substantive outcome change is an explicit PR-0009 deliverable;
- unresolved semantics are recorded as backlog items rather than hidden in the future specification.

## 10. Architecture Board decision

The Architecture Board accepts this boundary as the governing discovery contract for PR-0009. Acceptance authorizes specification work; it does not pre-approve any Objective fields, lifecycle, relationship model, or achievement semantics.
