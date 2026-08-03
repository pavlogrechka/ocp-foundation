---
Decision-ID: AD-004
Title: Operational Intent Boundary
Version: 0.3.1
Status: Under Review
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

Outcomes are not required to be mutually exclusive across time. The Architecture Board may select an explicit sequenced composite, for example Outcome A now with a governed sunset trigger toward Outcome D, or Outcome B as a transitional form followed by Outcome D. A sequenced choice must state the transition trigger, migration contract, interim and target authority, executable evidence, and Concept-graph impact at every stage; an unspecified blend of outcomes is not a decision.

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
- semantics of plural `objective_refs`, including whether the references express joint or conjunctive pursuit, alternative or disjunctive pursuit, or an unordered contextual set;
- equivalence between an Objective set and an `ExplicitIntentRecord` statement;
- automatic promotion, conversion or text comparison;
- authorization or command semantics;
- a validation-rule language;
- domain-specific sufficiency criteria;
- Event, Result, State or Readiness semantics;
- storage, API or UI representation;
- any new current Concept dependency.

The Architecture Board decision must explicitly route plural-Objective semantics to a normative owner: Core Operation, a future Coordination or domain rule, or a restriction that removes the ambiguity. Until that routing is accepted, list membership alone does not imply conjunction, alternative, priority, weighting, contribution or governed composition.

## 7. AB-022 validation-contract deliverables

Whichever outcome is selected, the downstream normative change must make the explicit-intent validation contract complete rather than leaving `validation_status = passed` as an opaque success flag.

Existing house precedents constrain the downstream design unless an explicit reviewed justification establishes a stricter alternative:

- OCP-006 §§9–12 and Business Rules 5 and 8 bind authoritative evaluation to the exact rule version and input snapshot; missing, stale or contradictory evidence cannot become a permissive success;
- OCP-001 invariant criterion 10 prohibits a contradictory stored result from producing a more permissive derivation than a missing or `indeterminate` result.

Therefore immutable exact-snapshot validation evidence and fail-safe degradation are the default. A mutable projection may exist only as a derived, non-authoritative view; absence, staleness or conflict must never normalize to `passed` or otherwise make the Operation more permissive.

The downstream contract must define:

1. the authority and version identity of `validation_rule_ref`;
2. the exact input snapshot evaluated;
3. the meaning of `not_evaluated`, `passed` and `failed`;
4. the immutable authoritative validation evidence and any derived mutable projection, unless a stricter reviewed alternative is justified;
5. which changes invalidate or require revalidation;
6. how stale, missing or conflicting validation degrades fail-safe rather than to `passed`;
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
- Outcome D must include a migration fixture proving that removal of the fallback does not silently invalidate accepted non-Draft Operations;
- any sequenced composite must prove both its interim state and its transition trigger without weakening accepted Operations silently.

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
10. a proposed P-001 invocation is incomplete or used only to disguise a semantic container;
11. plural Objective references imply conjunction or alternative pursuit without an authoritative owner;
12. a sequenced outcome changes target state without an explicit trigger or migration proof.

## 10. Exit criteria

AD-004 is ready for Architecture Board decision when:

- all six boundary questions have survived external adversarial review;
- one of Outcomes A–D, an explicit sequenced composite, or an equally explicit alternative is selected;
- any sequenced composite has an explicit trigger, migration contract, interim and target authority, evidence, and graph impact;
- the independent-identity threshold has a clear verdict;
- AB-014 receives a resolved direction: no Concept, local record or fundamental Concept;
- AB-022 receives an explicit downstream validation-contract mandate constrained by OCP-006 and OCP-001 fail-safe precedents;
- plural `objective_refs` semantics receive an explicit normative owner or ambiguity-removal rule;
- proposed dependencies are explicit and acyclic;
- no authorization, Objective-composition or achievement semantics are introduced by implication;
- unresolved semantics are recorded as backlog items rather than hidden in implementation.

## 11. Proposed Architecture Board decision — AD-004B

This section is a decision proposal. It does not change AD-004 from `Under Review` to `Accepted` until the Architecture Board explicitly approves it.

### 11.1 Selected outcome

Select the explicit sequenced composite:

```text
Outcome A now → separately reviewed sunset decision toward Outcome D
```

The interim authoritative model retains the OCP-004 dual-branch contract. A non-Draft Operation uses exactly one active intent representation:

- one or more resolvable `objective_refs`; or
- one valid local `ExplicitIntentRecord` governed by the AB-022 contract.

No fundamental `Operational Intent` Concept is introduced. No P-001 invocation is authorized for `ExplicitIntentRecord` merely by this decision. The current Concept graph remains unchanged: `Operation → Objective`.

Outcome D is a target direction, not an automatically effective future state. Removing the explicit-intent branch requires a separate externally reviewed Architecture Board decision and normative migration PR.

### 11.2 Independent-identity verdict and AB-014

The current evidence does not establish an independently identifiable domain object that cannot be owned safely by Operation, Objective or a local record.

Upon acceptance of AD-004B, AB-014 is resolved as:

> No separate fundamental `Operational Intent` Concept at this time. Reopening requires new evidence satisfying the independent-identity threshold in §3.

### 11.3 Normative owner and semantics of plural `objective_refs`

OCP-004 is the normative owner of the minimum Core semantics for plural `objective_refs`.

For one Operation snapshot, every member of `objective_refs` is an independent affirmative claim that the Operation pursues that Objective. All listed references are active; the list is not a disjunction from which one Objective may be selected as sufficient.

List membership alone does not encode:

- priority or weighting;
- sequencing or dependency;
- hierarchy or decomposition;
- contribution strength;
- equivalence between Objectives;
- aggregation of achievement, success or completion.

Domain or Coordination rules may add explicit structures for those semantics, but they must not reinterpret the bare list silently. Alternative pursuit requires a separately defined explicit representation; it is not inferred from `objective_refs`.

### 11.4 AB-022 mandate

OCP-004 is the normative owner of the downstream explicit-intent validation contract.

The downstream normative PR must require that `passed` is authoritative only when immutable validation evidence binds all of the following:

1. the exact `ExplicitIntentRecord` content or immutable record version;
2. the exact versioned validation rule identified by `validation_rule_ref`;
3. the exact input snapshot evaluated;
4. the evaluation timestamp and attributable evaluator reference;
5. one unambiguous result from `not_evaluated | passed | failed`.

Any substantive change to the intent record, validation rule version or evaluated input snapshot invalidates the prior `passed` result and requires revalidation.

A mutable status projection may exist only as a derived, non-authoritative view. Missing, stale, conflicting or structurally invalid evidence must fail safe and cannot satisfy the non-Draft Operation intent invariant. Validation remains distinct from authorization, approval or command authority.

The downstream PR must implement the executable evidence required by §8, including negative fixtures for stale, missing and contradictory validation evidence.

### 11.5 Sunset gate toward Outcome D

A sunset review toward Objective-only non-Draft Operations may be opened only when all of the following evidence exists:

1. the AB-022 normative contract and its executable fixtures are merged and green;
2. a Board-designated corpus of accepted non-Draft Operations using `ExplicitIntentRecord` has a documented migration result with zero unexplained or silently invalidated records;
3. every migrated record can create or resolve an Objective with attributable provenance while preserving the original explicit intent in audit history;
4. Objective authoring and validation workflows cover every validation-rule category used by the corpus without loss of required semantics;
5. a migration dry run proves deterministic mapping, reports all non-migratable cases, and provides an explicit rollback or remediation path.

Satisfying these conditions does not activate Outcome D automatically. It authorizes a separate externally reviewed Board decision and normative PR that must:

- remove or restrict the fallback explicitly;
- migrate existing accepted snapshots without silent invalidation;
- update OCP-004 and checker fixtures atomically;
- record Concept-graph impact, which is expected to remain `Operation → Objective` unless separately justified.

### 11.6 Acceptance effect

If the Architecture Board approves AD-004B:

- AD-004 becomes `Accepted`;
- AB-014 becomes `Resolved` with the no-Concept verdict in §11.2;
- AB-022 becomes `Planned` for the downstream OCP-004 contract and executable fixtures;
- no new fundamental Concept or current Concept dependency is created;
- the next normative cycle is the compact OCP-004 revision that codifies both the plural `objective_refs` semantics in §11.3 and the AB-022 validation contract in §11.4, together with the executable fixtures required by §8;
- Capability discovery remains next in the Wave 2 Concept queue after that compact normative cycle.

The acceptance commit must atomically update `Status: Accepted`, AB-014 to `Resolved`, and AB-022 to `Planned`; these changes must not be split into later cleanup commits.

Until explicit approval, the document remains `Under Review`, backlog statuses remain unchanged, and no downstream field model is pre-approved.
