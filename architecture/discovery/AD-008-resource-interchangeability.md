---
Decision-ID: AD-008
Title: Resource Interchangeability Boundary
Version: 0.3.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-003, OCP-004, OCP-005, OCP-006, OCP-009, OCP-012, AD-002, AD-007
Applies-To: AB-011, Resource interchangeability, Resource substitution
Review-After: External review of proposed AD-008C outcome selection
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

## 17. Outcome comparison working analysis

All five models answer the same narrow question: who, if anyone, may state that one Resource is a candidate substitute for an incumbent Resource or an exact requirement in one bound context. They do not decide availability, Readiness, authorization, selection or replacement execution.

This section is a working comparison for external review. It does not select an outcome.

### 17.1 Human-readable comparison

| Model | What it means in plain language | Main advantage | Main risk | Working assessment |
|---|---|---|---|---|
| A — deterministic derived eligibility | A governed rule recomputes the answer from exact requirements, effective Capability claims and candidate-specific Constraint results. | Adds the least new authority and is replayable when every input is governed. | A missing requirement owner or judgment call can be hidden inside code and presented as deterministic. | Leading minimum-authority model if the first consumer can supply a complete governed input envelope. |
| B — attributable interchangeability assessment | An identified record says who evaluated the candidate, against which target and evidence, and what conclusion they reached. | Preserves accountable judgment, correction and competing assessments. | The assessment may be mistaken for permission to select or replace the Resource. | Strong alternative when legitimate evaluator judgment remains after deterministic checks. |
| C — derivation plus attributable assessment | A deterministic result is retained as evidence and a separate evaluator records the contextual conclusion. | Makes the difference between computation and judgment explicit. | Introduces two authorities and a reconciliation problem before either is shown to a consumer. | Justified only when the first consumer demonstrably needs both layers. |
| D — domain-owned decision behind a Core envelope | Core defines safe inputs and fail-closed states, while a domain owns the actual conclusion. | Keeps domain-specific suitability rules outside Core. | Different domains may use the same envelope for incompatible meanings of substitution. | Viable only if the envelope exposes the domain authority and mechanically rejects semantic mismatch. |
| E — no interchangeability authority | Core exposes claims and Constraint decisions; each consumer decides outside the Foundation model. | Adds no new record or shared decision authority. | Coordination consumers may make incompatible decisions and cannot exchange a reusable conclusion. | Control outcome if no shared invariant or first cross-domain consumer can be demonstrated. |

### 17.2 First consumer scenario

A non-sensitive Coordination scenario provides the comparison pressure:

> A communications Operation has an incumbent relay Resource `relay-A`. A separately governed Coordination consumer asks whether candidate `relay-B` may be considered for the same exact relay requirement during a bound interval. The requirement names exact Capability versions and condition sets. OCP-012 supplies attributable claim projections for `relay-B`; OCP-006 supplies candidate-specific Constraint results for the same evaluation time. An external workflow reports that a replacement candidate is needed, but availability, authorization, final selection and Assignment changes remain outside this decision.

The scenario deliberately does not assume that the current Assignment owns the requirement. Until a normative owner for the exact relay requirement and its condition bindings is accepted, no model may return an authoritative automatic `positive` result. A proposed consumer envelope can be reviewed as evidence, but an implicit role label such as “relay” is insufficient.

For this scenario, every model must explain the following cases:

1. `relay-B` has all exact positive claim inputs and an admissible Constraint decision;
2. one claim binds the wrong condition set;
3. the candidate Constraint snapshot is missing or belongs to `relay-A`;
4. two evaluators disagree despite identical governed input snapshots;
5. the same candidate is compared in another Operation or at another time;
6. the comparison is positive but the candidate is unavailable or not authorized;
7. a consumer attempts to replace `relay-A` by editing its existing Assignment.

Cases 2–3 must not produce `positive`. Cases 5–7 must preserve the original comparison and Assignment history without implying that the Resources share identity.

### 17.3 Authority separation

| Layer | Authoritative input or actor | What it may establish | What it may not establish |
|---|---|---|---|
| Capability claim | OCP-012 claimant and claim authority | An attributable statement about one Resource and one exact Capability binding | Objective truth, suitability or substitution |
| Capability assessment, if required | Future independently governed evaluator path under AD-007C §24.3 | An evidence-based conclusion within its exact assessment contract | Interchangeability, authorization or selection by implication |
| Constraint evaluation | OCP-006 evaluator and applicable Constraint contract | Candidate-contextual findings and admissibility decision | Capability possession, availability or substitution |
| Exact requirement | Unselected; must be supplied by a separately accepted consumer contract | The Capability versions, condition sets and operational need against which a candidate is compared | Selection, Assignment mutation or general Resource type meaning |
| Interchangeability derivation | Model A rule authority, if selected | Reproducible contextual eligibility from governed inputs | Human judgment, authorization, ranking or execution |
| Interchangeability assessment | Model B or C evaluator, if selected | An attributable contextual conclusion with evidence and provenance | Permission to use or replace a Resource |
| Domain conclusion | Model D domain authority, if selected | A conclusion within the named domain contract | A universal Core conclusion or cross-domain equivalence |
| Authorization and selection | Future operational owner outside AD-008 | Permission and choice under its own contract | Rewriting claim, Constraint or interchangeability evidence |
| Replacement execution | OCP-005 Assignment rules and a future replacement workflow | New governed participation history | Mutation of the existing Assignment's `resource_ref` |

The unselected requirement owner is a decision gate, not a field that an interchangeability implementation may invent. If the Board selects A, B or C, the downstream contract must either select that owner explicitly or keep automatic conclusions `indeterminate`.

### 17.4 Comparison by operational scenario

The Architecture Board should compare models against behavior, not record counts alone.

1. **Complete deterministic envelope.** A has the smallest authority footprint when exact requirements, claim projections, Constraint results and time are complete. B adds value only if accountable judgment remains. C is excessive unless both facts are needed. D and E must explain why a shared deterministic conclusion should remain outside Core.
2. **Legitimate evaluator judgment.** B keeps one evaluator's conclusion attributable and reviewable. C additionally preserves the deterministic baseline. A must return `review required` rather than encode an undocumented judgment. D may work when the judgment is inherently domain-specific. E leaves consumers without a shared conclusion.
3. **Disagreement or correction.** B and C can preserve competing or superseded assessments without choosing by time or count. A must produce the same result from the same accepted snapshot and treat rule-version change as a new evaluation context. D must expose domain authority and lifecycle. E offers no shared correction contract.
4. **Missing requirement owner.** A, B and C remain `indeterminate` or non-authoritative. D is viable only if the named domain is the accepted owner, not merely the current caller. E is the safe control until ownership exists.
5. **Cross-domain exchange.** A can interoperate when the entire input and rule contract is shared. B and C can carry provenance but still need common target semantics. D must reject unknown domain meanings. E cannot promise that two consumers mean the same thing by a positive local result.
6. **Historical replay.** A replays exact inputs and rule version. B and C preserve the assessment evidence and correction chain. D must provide equivalent replay guarantees inside its envelope. E can replay claims and Constraints but not the consumer's ungoverned substitution decision.

### 17.5 Working hypothesis for external review

Model A is the leading hypothesis for the first shared contract because it adds the least authority: when the full input envelope is governed, the result is a contextual derivation rather than a standing assertion about either Resource. That preference is conditional on selecting an exact requirement owner and proving that the first consumer needs no legitimate evaluator judgment.

Model A intentionally does not provide a governed home for the human resolution of `review required`. If a later consumer proves that such a resolution must be retained in Foundation, a separate reviewed decision may add Model B's attributable assessment record for that purpose. Selecting A neither requires nor prevents that additive A-to-B path; until it is accepted, a review result cannot become a shared authoritative interchangeability conclusion.

Model B is the strongest alternative. It becomes preferable if the Coordination scenario requires accountable interpretation that cannot be reduced to governed inputs without hiding policy in code. Its record must remain an assessment, not authorization, ranking or replacement instruction.

Model C should be selected only if evidence shows that consumers must retain both a deterministic baseline and a separate accountable judgment. Model D is appropriate only when domain ownership is semantically necessary and cross-domain mismatch can fail closed. Model E remains the valid no-new-authority outcome if no shared consumer contract can justify A–D.

The working hypothesis does not authorize implementation. In particular, absence of a selected requirement owner currently prevents a production-positive path under A, B or C.

### 17.6 Evidence required before selection

External outcome comparison must determine:

- whether the proposed Coordination envelope has, or can narrowly define, an accepted normative owner for exact requirements;
- whether all positive inputs can be deterministic and replayable at one evaluation time;
- whether an attributable OCP-012 declaration is sufficient or independent assessment is required;
- whether any legitimate evaluator judgment remains after claim and Constraint handling;
- whether a reusable conclusion is required across consumers or Model E is sufficient;
- whether Model D can reject domain-semantic mismatch rather than merely label its source;
- whether B or C can preserve disagreement and correction without becoming authorization;
- whether Model A can version its rule authority without silently changing historical conclusions;
- which downstream artifact owns executable evidence for every counterexample in §12.

If these questions do not separate A from B, or if the requirement owner remains implicit, AD-008 must remain in `Discovery` rather than convert the working hypothesis into an Architecture Board decision.

## 18. Discovery status

Revision `0.1.0` opened AD-008 in `Discovery` for external adversarial boundary review. Fable reviewed exact head `75e0438`, identified two non-blocking gaps, and approved the boundary after both resolutions were re-reviewed on exact head `290a0fb`.

Revision `0.2.0` adds a human-readable A–E comparison, the first non-sensitive Coordination scenario, an authority-separation table and decision-separating evidence questions. It does not select an outcome or a requirement owner.

AB-011 remains `Planned` while the discovery compares outcomes; this preserves the accepted upstream AD-005C and AD-007C accounting that already names AB-011 as downstream work.

No interchangeability authority, record schema, Concept, graph edge, checker rule, availability model, authorization, selection or replacement workflow is accepted by revision `0.2.0`. Board acceptance requires exact-head external review, resolution of blocking findings, green checks and a separate explicit owner or Board authorization.

## 19. Proposed Architecture Board decision — AD-008C

This section proposes the next Board act. It is not effective while AD-008 remains in `Discovery`. Exact-head external review, resolution of blocking findings, green checks and explicit owner or Board authorization are still required before acceptance.

### 19.1 Proposed selected outcome

AD-008C proposes **Model A — deterministic derived eligibility** for the first shared Resource-interchangeability contract.

In plain language, a governed rule may answer whether one identified Resource is a candidate substitute in one exact context by recomputing the answer from the requirement, the candidate's effective Capability claims and the candidate-specific Constraint decision. The answer is about that comparison only. It is not a statement that the two Resources are equal, generally equivalent, available, authorized, selected or replaced.

Model A is proposed because the reviewed Coordination scenario contains no demonstrated judgment that Foundation must preserve as a separate interchangeability authority. Adding an assessment record before such a consumer exists would create an evaluator and a correction path without evidence that either is needed.

### 19.2 Requirement owner and context boundary

The future AB-011 normative contract must define the exact requirement input consumed by the derivation. That contract, not an existing Assignment, a Resource label, the Capability registry or the derivation rule, owns:

- the requirement's stable identity and version;
- its exact Capability-version and condition-set bindings;
- the Operation or other governed consumer context in which it applies;
- its applicability time or interval; and
- the provenance needed to resolve the requirement without caller memory.

The owner is therefore the separately reviewed consumer requirement contract selected by AB-011. A Coordination profile may instantiate that contract for the first scenario, but Coordination does not gain authority over general Resource identity, Capability truth, admissibility, authorization or Assignment execution.

Until that downstream contract is accepted, the proposed model has no authoritative automatic `positive` path. A caller-supplied role name, incumbent Assignment or ad hoc list of desired Capabilities is not a governed requirement and must remain `indeterminate`.

### 19.3 Derivation authority and fail-safe outcomes

The downstream rule authority may establish only a reproducible contextual eligibility result from one versioned rule and one complete input snapshot. It must expose enough binding information to replay the result after a requirement, claim, Constraint or rule version changes.

An authoritative `positive` result requires all of the following for the same evaluation context and time:

1. an exactly resolved governed requirement;
2. exactly resolved candidate Resource and Capability references;
3. permissive OCP-012 effective claim inputs for every required Capability binding, with claimant and authority attribution preserved;
4. the applicable OCP-006 candidate-specific Constraint decision and its exact input snapshot; and
5. no unresolved, ambiguous, stale, conflicting or mismatched required input.

Missing or unresolved requirement ownership, missing snapshots, reference ambiguity, conflicting claim heads, condition mismatch, stale inputs or cross-candidate Constraint reuse must not produce `positive`. A governed mismatch may produce a negative result only under the downstream contract's exact rule. Inputs that cannot be decided mechanically remain `indeterminate` or `review required`; those states must not be collapsed into either positive permission or a durable negative claim about the Resource.

Changing the context, requirement version, time, candidate, claim head, Constraint snapshot or rule version creates a new derivation. It must not rewrite the earlier result or transfer it to another Resource or Assignment.

### 19.4 Assessment activation path

Model B remains the named additive path if a concrete consumer later proves that legitimate evaluator judgment must be retained as a shared Foundation conclusion.

That activation requires a separate reviewed decision. It must define the evaluator, assessment authority, evidence and disagreement or correction semantics without changing historical Model A derivations. A human resolution of `review required` has no shared authoritative interchangeability meaning until that additional contract is accepted.

Models C and D are not proposed because the reviewed scenario does not justify two conclusion authorities or domain-specific substitution semantics. Model E remains the fail-safe behavior wherever the governed requirement or shared invariant needed by Model A is absent.

### 19.5 Downstream evidence mandate

If AD-008C is accepted, the next AB-011 normative cycle must define and externally review the deterministic contract without broadening into availability, authorization, selection or replacement workflow. It must provide executable evidence for every counterexample in §12 and, at minimum, prove:

- directionality by evaluating `A → B` separately from `B → A`;
- absence of unproved symmetry and transitivity;
- exact requirement, context, candidate, time, claim, Constraint and rule-version binding;
- fail-safe behavior for every missing, stale, ambiguous, conflicting or mismatched input;
- historical replay after any input or rule is superseded;
- distinct Resource and Assignment identities before and after comparison; and
- the inability of a positive eligibility result to authorize, select or execute replacement.

The reference checker may provide executable examples, but it is not the normative owner of the rule. The accepted downstream contract remains authoritative.

### 19.6 Proposed acceptance effect

If explicitly authorized and merged after exact-head external approval, AD-008C would have these effects:

- AD-008 would become `Accepted` at version `0.3.0`;
- Model A would become the governing direction for the first downstream AB-011 contract, subject to §§19.1–19.5;
- the AB-011 downstream contract would own the exact contextual requirement input and deterministic rule;
- Model B would remain the separately reviewed activation path for demonstrated evaluator judgment;
- AB-011 would remain `Planned` until its normative contract and executable evidence are accepted; and
- the later Coordination cycle would receive only the narrow consumer-profile boundary defined here, not a general substitution or workflow authority.

This proposal does not define a record schema, persistence form, API, production evaluator, availability model, ranking, authorization, selection, reservation, replacement workflow, new Concept or graph edge.
