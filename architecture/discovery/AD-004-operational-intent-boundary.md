---
Decision-ID: AD-004
Title: Operational Intent Boundary
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-004, OCP-008
Applies-To: AB-014, AB-022, Operation intent model
Review-After: External adversarial boundary review
---

# AD-004 — Operational Intent Boundary

## 1. What does operational intent mean today?

In the current Core, **operational intent** is a semantic requirement of an Operation snapshot, not an established fundamental Concept.

Outside lifecycle stage `Draft`, OCP-004 requires exactly one active representation:

1. one or more resolvable `objective_refs`; or
2. one valid local `ExplicitIntentRecord`.

The lowercase phrase `operational intent` names the requirement satisfied by one of those branches. The capitalized term `Operational Intent` denotes a candidate Concept only where this discovery discusses that option explicitly.

The boundary question is whether there is an independently identifiable domain object behind those representations, or whether the existing Operation contract is already sufficient.

## 2. What is Operational Intent not?

Operational Intent is not automatically:

- Objective;
- `ExplicitIntentRecord`;
- Operation;
- Order or Task;
- authorization, approval, command authority or policy;
- lifecycle stage, readiness or state;
- Result, Event, evidence or proof of achievement;
- a validation result;
- a universal container for free text;
- an implicit hierarchy, grouping or weighting of Objectives.

A set of Objective references does not become a new Concept merely because it jointly satisfies an Operation completeness rule.

A valid `ExplicitIntentRecord` does not become authoritative authorization merely because a validation rule marked it `passed`.

## 3. Does Operational Intent require independent identity?

The initial hypothesis is **no**: a new fundamental Concept is not justified while operational intent exists only as an Operation-owned validity requirement and can be represented completely by the current two branches.

Independent identity becomes plausible only if evidence shows at least one material property that cannot be owned safely by Operation, Objective or a local record, for example:

- reuse by multiple Operations without copying or identity collapse;
- amendment or supersession independent of an Operation snapshot;
- provenance that is neither Objective provenance nor Operation authoring provenance;
- domain invariants over a governed composition of multiple Objectives;
- consumers outside Operation that must resolve the same intent identity;
- lifecycle, temporal effectivity or audit continuity independent of any single Operation.

The discovery must reject a candidate Concept whose only purpose is to rename the current disjunction or to wrap fields already governed by OCP-004 and OCP-008.

## 4. Who creates, owns and uses operational intent?

The current model has no separate creation act for Operational Intent:

- Objective is created independently under OCP-008;
- `ExplicitIntentRecord` is created and owned inside an Operation snapshot under OCP-004;
- choosing the active branch is an explicit Operation authoring act.

Candidate consumers include planning, validation, coordination and audit workflows. Consumer use does not itself establish a fundamental Concept or a normative `Concept-Depends-On` edge.

AD-004 does not introduce Authority, Commander, Approver, Order or Policy. Provenance and validation remain distinct from authorization.

## 5. Which representation outcomes are admissible?

External review must evaluate four admissible outcomes rather than assuming a new Concept.

### Outcome A — retain the current dual-branch contract

No new Concept is introduced. Operational intent remains an Operation validity requirement represented by either Objective references or one local `ExplicitIntentRecord`.

Concept graph impact: none. The current normative edge remains `Operation → Objective`.

### Outcome B — governed local identified record

A future OCP-004 revision may replace the current fallback structure with an Operation-owned identified record, potentially invoking P-001.

This record would not automatically be a fundamental Concept. The specification would need to justify stable identity, provenance, validation authority, endpoint-free or endpoint-bearing form, selected P-001 modules and ownership by Operation.

Concept graph impact: none unless a genuine fundamental dependency is separately justified.

### Outcome C — fundamental Operational Intent Concept

A separate Concept is introduced only if independent identity and cross-Operation semantics survive falsification.

A defining specification would have to establish:

- identity independent of any one Operation;
- boundary from Objective and `ExplicitIntentRecord`;
- whether it contains, references or derives from Objectives;
- provenance, amendment and supersession rules;
- consumers and justified Concept dependencies;
- a graph that remains explicit and acyclic.

Neither `Operation → Operational Intent` nor `Operational Intent → Objective` is approved by this discovery.

### Outcome D — Objective-only target state

The explicit-intent branch is treated as a temporary authoring or migration fallback and is eventually removed from non-Draft Operation snapshots.

This outcome requires evidence that all valid operational intent can be represented by Objective without losing traceability, domain validation or practical authoring workflows.

Concept graph impact: the current `Operation → Objective` edge remains sufficient.

## 6. What is explicitly not defined?

AD-004 intentionally does not define:

- fields for a future Operational Intent record or Concept;
- a lifecycle or temporal-effectivity model;
- Objective composition, hierarchy, order, priority, weighting or contribution semantics;
- equivalence between an Objective set and an `ExplicitIntentRecord` statement;
- automatic promotion, conversion or text comparison;
- authorization or command semantics;
- a validation-rule language;
- domain-specific sufficiency criteria;
- Event, Result, State or Readiness semantics;
- storage, API or UI representation;
- any new current Concept dependency.

## 7. AB-022 validation-contract deliverables

Whichever outcome is selected, the downstream normative change must make the explicit-intent validation contract complete rather than leaving `validation_status = passed` as an opaque success flag.

It must define:

1. the authority and version identity of `validation_rule_ref`;
2. the exact input snapshot evaluated;
3. the meaning of `not_evaluated`, `passed` and `failed`;
4. whether validation records are mutable projections or immutable evidence;
5. which changes invalidate or require revalidation;
6. how stale, missing or conflicting validation fails;
7. why validation does not imply authorization;
8. whether validation belongs to the Operation snapshot, a local identified record or a future independent Concept.

AD-004 names these obligations but does not choose their field model.

## 8. Required evidence for the downstream cycle

The implementation following the Architecture Board decision must preserve executable evidence for:

- a non-Draft Operation valid through resolvable Objective references;
- a non-Draft Operation valid through one valid explicit-intent branch, while that branch remains supported;
- fail-safe rejection of both active branches outside `Draft`;
- permissive authoring coexistence and unresolved Objective references in `Draft`;
- rejection of stale, missing or contradictory explicit-intent validation according to the selected AB-022 contract.

Additional evidence is conditional:

- Outcome B must include P-001 conformance and identified-record counterexamples;
- Outcome C must include identity, cross-Operation reuse, dependency and supersession fixtures;
- Outcome D must include a migration fixture proving that removal of the fallback does not silently invalidate accepted non-Draft Operations.

## 9. Review target

Attempt to falsify the boundary with cases where:

1. Operational Intent merely renames Objective;
2. a local `ExplicitIntentRecord` quietly accumulates independent Concept semantics;
3. multiple Objective references require governed composition that the current model cannot express;
4. a shared intent across Operations cannot be represented without duplication or identity collapse;
5. validation status becomes authorization by implication;
6. promotion from explicit intent to Objective loses provenance or audit continuity;
7. a separate Concept creates a circular dependency with Operation or Objective;
8. Outcome A preserves two representations whose semantics diverge without a detectable failure;
9. Outcome D removes the fallback before Objective authoring can cover real operational cases;
10. a proposed P-001 invocation is incomplete or used only to disguise a semantic container.

## 10. Exit criteria

AD-004 is ready for Architecture Board decision when:

- all six boundary questions have survived external adversarial review;
- one of Outcomes A–D is selected or an equally explicit alternative is justified;
- the independent-identity threshold has a clear verdict;
- AB-014 receives a resolved direction: no Concept, local record or fundamental Concept;
- AB-022 receives an explicit downstream validation-contract mandate;
- proposed dependencies are explicit and acyclic;
- no authorization, Objective-composition or achievement semantics are introduced by implication;
- unresolved semantics are recorded as backlog items rather than hidden in implementation.

## 11. Architecture Board decision

No option is selected yet. Acceptance of this discovery will authorize only the downstream normative work implied by the selected outcome; it will not pre-approve a new Concept, P-001 invocation or OCP field model.
