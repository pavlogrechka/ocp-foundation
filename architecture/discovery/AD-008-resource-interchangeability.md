---
Decision-ID: AD-008
Title: Resource Interchangeability Boundary
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-003, OCP-004, OCP-005, OCP-006, OCP-009, OCP-012, AD-002, AD-007
Applies-To: AB-011, Resource interchangeability, Resource substitution
Review-After: External adversarial boundary review
---

# AD-008 — Resource Interchangeability Boundary

## 1. Trigger and accepted mandate

AB-011 is the next normative cycle after acceptance of OCP-012. The accepted mandate is narrow: determine Resource interchangeability from exact Capability claims, applicable Constraint results and operational context without losing Resource identity.

OCP-012 now supplies only a fail-safe attributable claim projection. It deliberately does not say that a claim is objectively true, that a Resource is ready or available, or that two Resources may substitute for one another. OCP-006 supplies contextual admissibility decisions, but those decisions do not grant authorization and do not choose a Resource. OCP-005 preserves each Assignment and Resource identity when a replacement occurs.

AD-008 opens the missing decision boundary. It introduces no interchangeability verdict, stored relation, automatic replacement, ranking algorithm, availability model, authorization model, Assignment amendment or new Concept.

## 2. Boundary question

AD-008 asks:

> Under which exact operational context may one identified Resource be considered a candidate substitute for another identified Resource or for an explicitly defined requirement, using fail-safe Capability-claim input and applicable Constraint results, while preserving both Resource identities and keeping admissibility, availability, authorization, selection and replacement execution separate?

The discovery must determine:

1. whether interchangeability is a directional contextual conclusion or a symmetric Resource relation;
2. whether the comparison target is an incumbent Resource, an exact requirement, or both through separately governed modes;
3. which exact context and time bind one evaluation;
4. how required Capability versions and condition sets are identified;
5. how OCP-012 attributable claim projections may be consumed without becoming verified truth;
6. how applicable OCP-006 Constraint results gate, qualify or block a conclusion;
7. which indeterminate, missing, stale, ambiguous or conflicting inputs fail closed;
8. whether a conclusion is derived, stored as an attributable assessment, or represented by another governed form;
9. which authority, if any, may select and execute a replacement after a positive conclusion;
10. which executable counterexamples a downstream contract must provide.

## 3. Terms that must remain distinct

- **Resource identity** — the stable identity defined by OCP-003.
- **Capability definition** — a reusable holder-independent definition from OCP-009.
- **Capability claim** — an attributable OCP-012 statement about one exact Resource and Capability version.
- **requirement** — an exact context-owned statement of what a candidate must provide; its normative owner is not selected here.
- **admissibility** — the OCP-006 decision over applicable Constraint evaluations for one exact candidate context.
- **interchangeability** — a contextual conclusion that one Resource may be considered as a substitute under a stated comparison contract.
- **equivalence** — a stronger assertion of sameness that AD-008 does not assume.
- **availability** — whether a Resource can be considered for use at a time; not yet defined by Core.
- **Readiness** — evidence-based preparedness under AD-002; still Deferred.
- **authorization** — permission to select, assign, reserve or use a Resource.
- **selection** — choosing one candidate among alternatives.
- **ranking or optimization** — ordering candidates by preferences or costs.
- **replacement execution** — changing participation through governed Assignment or another future workflow.

A positive interchangeability conclusion is not any of the other layers. In particular:

```text
interchangeable(candidate, target, context, time)
  does not imply
same_identity(candidate, target)
  or available(candidate, time)
  or ready(candidate, context, time)
  or authorized(candidate, context)
  or selected(candidate, context)
  or assigned(candidate, operation)
```

## 4. Identity and directionality boundary

Distinct Resources remain distinct before, during and after comparison. Matching type, label, Capability claims or Constraint outcomes never merge identities, copy history or redirect references.

Interchangeability is not assumed to be symmetric or transitive. A candidate may satisfy the exact needs of one target in one context while the reverse comparison fails because the target has different capabilities, conditions or constraints. Two positive comparisons against the same target do not make the candidates interchangeable with each other.

The discovery must test at least these competing relation shapes:

- **directional substitution:** candidate `B` may substitute for incumbent `A` in context `C` at time `t`;
- **requirement satisfaction:** candidate `B` may satisfy exact requirement set `Q` in context `C` at time `t`;
- **symmetric equivalence:** `A` and `B` are interchangeable in context `C`.

The symmetric form is admissible only if evidence shows that it adds legitimate Core authority and does not hide two directional evaluations. Global, timeless `A interchangeable-with B` is outside the accepted mandate.

## 5. Exact comparison context

Every admissible outcome must bind a finite, replayable context. At minimum the decision must account for:

```text
comparison mode
candidate Resource reference
incumbent Resource reference or exact requirement-set reference
Operation or other explicit operational-context reference
evaluation time
required Capability references and exact versions
Capability-claim condition-set bindings
applicable Constraint set and evaluation snapshot
provenance of the conclusion
```

The discovery does not yet declare all fields mandatory or choose a schema. It requires each outcome to explain how implicit current context, latest-version lookup and evaluator-local assumptions are prevented.

All time-dependent inputs, including claim effectivity, the Constraint evaluation snapshot and the requirement version, must align to the same bound evaluation time. A mismatch between those temporal planes yields `indeterminate` by default.

Changing the Operation, role, time, requirement version, claim condition set or applicable Constraint snapshot creates a different evaluation context. A prior conclusion must not silently migrate to the new context.

## 6. Capability input boundary

AD-008 may consume only OCP-012 claim heads or `effective_capability_claim` for exact bindings. It may not read Capability registry membership, labels, Resource type, Assignment role or past success as proof that a Resource has a Capability.

For an automatic positive input:

- each required Capability reference must resolve exactly under OCP-009;
- the relevant Resource claim must bind the same exact Capability version and the exact condition set required by the context;
- the claim projection must be positive under the accepted OCP-012 fail-safe contract;
- the claimant and authority remain visible; an attributable declaration must not be displayed as independent verification;
- zero heads, withdrawal, negative assertion, branch conflict or non-permissive support cannot be converted into a positive claim input.

The discovery must decide whether an attributable positive declaration is sufficient for any interchangeability outcome or whether a concrete consumer requires the independently assessed path preserved by AD-007C §24.3. If assessment is required, AD-008 must name that evidence gap; it may not silently reinterpret OCP-012.

## 7. Constraint and admissibility boundary

Capability similarity is necessary only when the selected outcome says so; it is never sufficient by itself. The candidate context must also use the accepted OCP-006 applicability and decision contract.

At minimum:

- applicable blocking Constraint violations yield no positive automatic conclusion;
- applicable indeterminate results follow their governed disposition and cannot be treated as satisfied by default;
- contradictory stored `not_applicable` results normalize to `indeterminate` under OCP-006;
- `review_required` remains distinct from `inadmissible` and from a positive conclusion;
- advisory findings remain visible and do not silently become ranking weights;
- `constraint_set_decision = admissible` does not prove availability, authorization, Readiness or interchangeability on its own.

The comparison must bind the candidate-specific Constraint context. Reusing the incumbent Resource's evaluation for the candidate is invalid unless a future normative rule explicitly proves that the evaluated subjects and snapshot are identical.

## 8. Operational-context boundary

Interchangeability is meaningful only relative to an explicit need. An admissible context may include an Operation, intended role, applicability interval, condition set and exact requirement set. The discovery must identify the normative owner of every required input rather than inventing hidden fields inside the interchangeability decision.

AD-008 must not use an existing Assignment as proof that its Resource is suitable. Assignment establishes participation and role, not Readiness, availability or suitability. Replacing an assigned Resource does not mutate `resource_ref`; OCP-005 requires a new Assignment and a separately governed replacement process.

Where no accepted owner exists for an exact requirement or operational input, the outcome must either:

1. define a narrowly scoped downstream owner subject to external review; or
2. return an explicit evidence gap and remain non-authoritative.

Human-readable labels and evaluator memory are not valid substitutes for governed context.

## 9. Fail-safe result vocabulary

Every outcome must distinguish at least:

- **positive** — the selected comparison contract is satisfied for the exact candidate, target, context and time;
- **negative** — a known required condition is not satisfied;
- **indeterminate** — required evidence is missing, stale, ambiguous, conflicting, unresolved or not governed;
- **review required** — automation cannot decide and a separate review workflow is explicitly required.

`negative` and `indeterminate` must not be collapsed. Absence of a positive result is not proof that substitution is impossible. `review required` does not grant temporary permission.

No outcome may select a winner by record order, newest timestamp, claimant count, source count or majority unless a future normative authority defines that precedence explicitly.

## 10. Candidate authority models

The discovery must compare at least these models.

### A — deterministic derived eligibility

A reproducible derivation consumes exact requirements, OCP-012 projections and OCP-006 decisions and returns a fail-safe contextual result. It stores no new authoritative interchangeability record.

This model is compact and replayable, but it requires every input and decision rule to be deterministic and governed. It cannot represent accountable human judgment without a separate record.

### B — attributable interchangeability assessment

A governed identified record attributes a contextual conclusion to an evaluator and binds the exact candidate, target, rules, evidence snapshot, time and provenance. It may reuse an OCP-011 profile only if target and criterion semantics fit without weakening OCP-011 invariants.

This model preserves reviewable judgment and correction history, but it introduces record lifecycle and authority questions. It must not become authorization or selection.

### C — derivation plus attributable assessment

A deterministic result is preserved as input evidence, while a separate assessment records accountable interpretation. The two authorities remain visible.

This model best exposes automation and judgment, but it has the highest contract and reconciliation cost. It must define how disagreement fails safely without letting either layer silently override the other.

### D — domain-owned decision behind a Core input envelope

Core governs exact inputs, identity preservation and fail-safe minimums; a domain owns the actual interchangeability conclusion.

This model limits Core scope, but it must still prevent label matching, identity collapse and permissive handling of unresolved inputs across domains.

### E — no interchangeability authority

Core exposes exact claims and Constraint decisions only; consumers keep all substitution decisions outside the Foundation model.

This is the minimum-authority control. It is acceptable only if the Board finds no shared invariant beyond existing contracts. It must explain how Coordination consumers avoid incompatible local meanings.

## 11. Questions that separate the models

External review and Board comparison must answer:

1. Does any Foundation consumer require an authoritative reusable conclusion rather than recomputing eligibility?
2. Can the conclusion be deterministic from governed inputs, or does legitimate evaluator judgment remain?
3. Is an incumbent Resource necessary, or is exact requirement satisfaction the primary comparison?
4. Does a positive declaration under OCP-012 carry enough authority for the consumer, or is independent assessment mandatory?
5. Which artifact owns the exact Capability requirement set and its condition bindings?
6. Are Constraint results evaluated for the complete candidate context and replayable snapshot?
7. Must the conclusion support correction or supersession history?
8. Can a domain-owned conclusion remain interoperable without a Core record family?
9. What consumer behavior is allowed for `indeterminate` and `review required`?
10. Which model adds the least authority while still supporting the first concrete Coordination use case?

If these questions do not separate the models, AD-008 must remain in Discovery rather than convert implementation preference into a Board decision.

## 12. Mandatory counterexamples

Every admissible outcome must explain and assign executable evidence for:

1. two Resources with matching positive claims but different identities;
2. matching Capability labels bound to different exact versions;
3. a candidate with a positive claim but a blocking Constraint violation;
4. a candidate with missing or stale claim support;
5. conflicting claim heads for the candidate;
6. an incumbent admissibility result incorrectly reused for the candidate;
7. the same Resource pair producing different results in two Operations or times;
8. `B` substituting for `A` while `A` cannot substitute for `B`;
9. two candidates positive against one requirement but not interchangeable with each other;
10. an admissible candidate that is unavailable or unauthorized;
11. replacement attempted by mutating an existing Assignment's `resource_ref`;
12. a domain label or Resource type used as an implicit requirement.
13. a positive claim under condition set `X` evaluated against a requirement that binds condition set `Y`; the result is negative or `indeterminate` under the selected contract, never positive.

These examples must contain no sensitive operational data.

## 13. Forbidden shortcuts

AD-008 must reject any outcome that:

1. equates Resource identities because claims or types match;
2. assumes symmetry or transitivity without an exact normative proof;
3. treats registry membership as holder possession;
4. treats an attributable claim as independently verified truth;
5. redirects an exact Capability version to latest;
6. ignores claim condition-set binding;
7. treats missing, stale, ambiguous, conflicting or unresolved input as positive;
8. treats `admissible` as interchangeable, available, ready or authorized;
9. reuses a Constraint result across different candidate contexts implicitly;
10. edits an Assignment reference to perform replacement;
11. ranks or selects candidates without a separate normative owner;
12. derives authority from timestamps, list order or source counts;
13. embeds Readiness, availability, reservation, capacity or authorization semantics;
14. creates a permanent Resource-to-Resource equality edge;
15. depends on hidden labels, implicit current context or evaluator memory.

## 14. Explicitly not defined

AD-008 does not define:

- a production matching, ranking or optimization engine;
- Resource equality, merging, deduplication or identity aliases;
- Readiness, availability, capacity, reservation or allocation;
- authorization, approval or command authority;
- automatic Assignment creation, revocation or amendment;
- a universal Operation Capability-requirement schema;
- Constraint expression language, precedence, waiver or freshness;
- claimant trust ranking or independent Capability assessment;
- Organization holder semantics;
- procurement equivalence or inventory substitution;
- API, persistence, wire schema or migration format;
- a new fundamental Concept or current Concept graph edge.

## 15. Evidence obligations

Before Board outcome selection, the discovery must provide:

- at least one concrete non-sensitive Coordination or replacement scenario;
- an explicit input/output contract for every compared model;
- an authority table separating claim, assessment, admissibility, interchangeability, authorization, selection and Assignment execution;
- replay behavior for historical time and changed context;
- resolution of the requirement-owner question;
- a falsification result for directionality, symmetry and transitivity;
- handling of all fail-safe states from §§6–9;
- executable fixtures assigned to their downstream normative owners;
- confirmation that no new Concept or graph edge is smuggled in;
- external adversarial review of the human-readable contract before Board acceptance.

## 16. Exit criteria

AD-008 is ready for Architecture Board decision when:

- one authority model is selected, or named missing evidence keeps the AD in Discovery;
- the comparison target and directionality are explicit;
- exact requirements, context, time and input snapshots are governed;
- OCP-012 attribution remains visible and fail-safe;
- OCP-006 admissibility remains candidate-contextual and separate;
- Resource and Assignment identities remain unchanged;
- availability, Readiness, authorization, selection and execution remain separate;
- negative, indeterminate and review-required outcomes are not collapsed;
- mandatory counterexamples have owners and executable evidence plans;
- the first consumer scenario can be explained without hidden fields or domain assumptions;
- unresolved semantics are recorded in Architecture Backlog.

## 17. Discovery status

Revision `0.1.0` opens AD-008 in `Discovery` for external adversarial boundary review. AB-011 remains `Planned` while the discovery compares outcomes; this preserves the accepted upstream AD-005C and AD-007C accounting that already names AB-011 as downstream work.

This revision does not select an outcome. Board acceptance requires exact-head external review, resolution of blocking findings, green checks and a separate explicit owner or Board authorization.
