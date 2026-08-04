---
Decision-ID: AD-007
Title: Capability Claim Boundary
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-003, OCP-009, AD-002, AD-005, P-001
Applies-To: AB-057, AB-011, Capability Claim model, Resource interchangeability
Review-After: External adversarial boundary review
---

# AD-007 — Capability Claim Boundary

## 1. Trigger and current state

AD-005C selected a two-layer model:

1. reusable Capability definition with holder-independent identity;
2. holder-specific claim as a separate identified record.

OCP-009 accepted the definition layer and governed registry contract. It intentionally does not define claim identity, claim authority, holder relation, evidence, temporal applicability, lifecycle, correction, withdrawal, effective projection or P-001 invocation.

The next roadmap dependency hinge is therefore not another Capability definition revision. It is the boundary of a holder-specific claim that can later support Resource interchangeability without collapsing Capability, Resource, Readiness, Assignment, Constraint evaluation or authorization.

Current guardrails already established:

- initial direct claim subject is `Resource` only;
- Organization-specific claims remain deferred by AB-006 and AB-052;
- Capability definition is referenced by exact `(namespace, capability_id, version)`;
- registry membership never proves holder possession;
- Resource type, Assignment role, Operation requirement, successful Event or assessment do not create a standing claim;
- no inheritance, aggregation or transitive possession is implied;
- `Capability ≠ Readiness`;
- a claim must not imply availability, authorization or admissibility;
- AB-011 remains downstream and cannot treat similar Resources as one identity.

AD-007 introduces no claim schema, accepted record, current Concept dependency, P-001 invocation, validator or interchangeability rule.

## 2. Boundary question

AD-007 asks:

> What governed record or derivation may assert that one exact Resource has, lacks or may provide one exact Capability definition under stated conditions, evidence, authority and time, without turning the assertion into readiness, availability, authorization, admissibility or Resource identity?

The discovery must determine:

1. whether a stored holder claim is needed at all;
2. whether a claim is a declaration, an evaluation, or a composition of both;
3. what the claim is authoritative about;
4. whether positive, negative and indeterminate statements share one model;
5. how exact evidence and temporal applicability constrain authority;
6. how correction, withdrawal and contradictory claims preserve history;
7. which P-001 modules, if any, a downstream record must invoke;
8. what AB-011 may consume without turning claim equality into Resource equality or automatic substitution.

## 3. Semantic layers that must remain distinct

The discovery must preserve at least these layers:

- **Capability definition** — reusable holder-independent identity from OCP-009;
- **Resource identity** — the exact candidate holder from OCP-003;
- **claim declaration** — an attributable statement made by a claimant or issuer;
- **claim assessment** — an attributable evaluation of evidence under an exact rule;
- **evidence item** — material cited by a claim or assessment, not automatically true or sufficient;
- **claim authority** — the narrow proposition the record is allowed to establish;
- **temporal applicability** — when the proposition is asserted to apply;
- **claim record effectivity** — whether a record is applicable under its own history and interval semantics;
- **withdrawal or revocation** — termination of reliance on a record, not proof of the opposite proposition;
- **supersession** — explicit replacement or correction that preserves prior history;
- **Readiness** — evidence-based preparedness for a specific context, still deferred;
- **availability** — whether a Resource can be considered for use at a time;
- **authorization** — permission from a separate authority model;
- **admissibility** — result of applicable Constraint evaluation;
- **Assignment** — contextual participation and role in an Operation;
- **Operation Capability requirement** — a requirement reference, not possession;
- **interchangeability decision** — a contextual conclusion about possible substitution, not claim identity.

A useful implementation shortcut is not sufficient reason to collapse these layers.

## 4. Initial subject boundary

The only initially admissible direct subject type is:

```text
resource@1
```

A downstream claim must exact-resolve one Resource identity.

Not admitted by this discovery:

- Organization as direct claim subject;
- Operation as claim subject;
- Assignment as claim subject;
- Resource type or taxonomy class as a holder;
- anonymous group, fleet, unit label or search result as a holder;
- automatic mapping from Organization to Organizational Resource;
- claim inheritance between composite Resource and component Resource.

Two Resources of the same type may have different claims. One Resource may have different claims for different exact Capability versions or conditions.

## 5. Exact Capability binding

Every admissible holder model must bind the exact OCP-009 Capability identity:

```text
namespace
capability_id
version
```

The model must reject:

- label-only references;
- missing version;
- namespace guessing;
- latest-version substitution;
- automatic redirect from a superseded version to its successor;
- reinterpretation of an historical claim after the Capability definition changes.

A claim bound to `v1` remains a claim about `v1`, even when `v2` supersedes it. Whether new claims may reference a superseded Capability version is a separate policy question; resolution must remain exact.

## 6. Claim proposition and polarity

The downstream decision must define the exact proposition represented by a claim.

Candidate polarity vocabularies may distinguish:

- positive assertion — the Resource has or can provide the exact Capability under stated conditions;
- negative assertion — the Resource does not have or cannot provide it under stated conditions;
- indeterminate assertion — evidence is insufficient, stale, ambiguous or conflicting;
- no claim — no authoritative record exists for the exact binding.

These states must not be collapsed:

```text
no claim ≠ negative claim
withdrawn claim ≠ negative claim
expired claim ≠ negative claim
conflicting claims ≠ latest claim wins
indeterminate claim ≠ positive claim
```

The discovery does not accept a vocabulary yet. External review must determine whether negative and indeterminate propositions belong in the same record family or require a separate assessment layer.

## 7. Authority boundary

A holder-specific record may be authoritative only for a narrow attributable proposition, such as:

> a defined claimant or evaluator, under a defined authority and rule, asserted or evaluated that one exact Resource has a stated relation to one exact Capability version under stated conditions and time, based on stated evidence and provenance.

It must not be automatically authoritative for:

- objective truth that the Resource can always perform the Capability;
- current Readiness;
- availability at planning or execution time;
- sufficient quantity, throughput, endurance or capacity;
- authorization or qualification;
- Constraint satisfaction or operational admissibility;
- Assignment eligibility;
- Operation success;
- future performance;
- equivalence with another Resource;
- automatic substitutability.

The downstream model must distinguish `claimant_ref`, `evaluator_ref` and `authority_ref` if more than one of those roles is semantically required. Provenance alone must not silently prove authority.

## 8. Conditions, evidence and evidence state

A claim without conditions risks becoming an unlimited assertion. Candidate condition dimensions include:

- environment or operating envelope;
- configuration or component set;
- domain profile;
- temporal interval;
- required supporting Resource or infrastructure;
- qualification or certification references;
- versioned evaluation rule;
- quantitative thresholds owned outside the claim contract.

The discovery does not accept a condition expression language.

For any evidence-bearing outcome, the downstream contract must decide:

- exact evidence binding kinds;
- immutable evidence snapshot authority;
- exact evaluation or input snapshot;
- evidence time;
- who declares evidence state;
- which evidence states are mechanically derivable;
- fail-safe behavior for missing, stale, ambiguous or conflicting evidence;
- whether one successful Event or one OutcomeAssessmentRecord may be evidence without automatically becoming a standing claim.

Mandatory baseline:

```text
missing | stale | ambiguous | conflicting evidence
must not produce an authoritative positive claim by default
```

Absence of negative evidence is not sufficient positive evidence.

## 9. Temporal semantics

A Capability definition may be stable while a Resource claim changes over time.

The downstream model must distinguish:

- assertion or evaluation time;
- record creation time;
- evidence observation time;
- applicability start and end;
- review or revalidation due time;
- termination time;
- supersession time.

Timestamp order must not select authority automatically.

The discovery must determine whether claim applicability requires P-001 Module A temporal effectivity. If intervals are selected, gaps and overlaps must be explicit, and a single caller-supplied `reference_time` must not hide contradictory effective claims.

Expiry or end of applicability means the record no longer asserts the proposition for later time. It does not prove the opposite proposition.

## 10. Correction, withdrawal and contradiction

The downstream model must preserve attributable history.

At minimum it must distinguish:

- correction or replacement of a prior claim;
- withdrawal by the claimant;
- revocation by an authorized authority;
- natural expiry or applicability end;
- a new independent claim under different conditions;
- contradictory concurrent claims from different authorities or evidence sets.

Candidate P-001 Module C supersession may preserve corrections, but supersession must not silently change:

- Resource subject;
- exact Capability identity;
- claim kind or proposition family;
- governed condition identity if conditions are part of the lineage binding.

Branching may be required when independent successors disagree. Newest timestamp, issuer count, storage order or confidence-like labels must not choose a winner without a reviewed authority rule.

Withdrawal or revocation terminates reliance on one record; it does not manufacture a negative claim and does not erase the prior attributable assertion.

## 11. Lifecycle question

The discovery must decide whether claim records need an explicit lifecycle.

Possible lifecycle semantics include draft publication, establishment, withdrawal, revocation or expiry. If lifecycle is selected, P-001 Module B transition history and projections must be invoked completely rather than represented by mutable status fields.

A simpler model may use immutable publication plus Module A effectivity and Module C supersession without a lifecycle. External review must test whether that is sufficient for withdrawal, revocation and audit.

No lifecycle is selected in revision `0.1.0`.

## 12. Non-inheritance and composition boundary

Default rules:

- Resource type does not grant a claim;
- Assignment role does not grant a claim;
- Operation requirement does not grant a claim;
- successful Event does not create a standing claim;
- OutcomeAssessmentRecord does not create a standing claim automatically;
- certificate or qualification record is evidence at most, not claim identity;
- composite Resource does not inherit all component claims;
- component Resource does not inherit composite claims;
- one Resource claim does not propagate to another Resource;
- Organization does not inherit the union of member Resource claims;
- claim similarity does not establish Capability equivalence.

Any future derivation must name its normative owner, exact inputs, conditions, authority and counterexamples.

## 13. Boundary from adjacent operational semantics

### 13.1 Readiness

A positive Capability claim may be a prerequisite input to future Readiness evaluation. It is never Readiness itself.

### 13.2 Availability

A valid claim may remain true while the Resource is unavailable. Availability requires separate time and allocation semantics.

### 13.3 Capacity

A claim may state qualitative ability without proving current quantity, throughput, stock, range, duration or remaining endurance. Capacity remains governed by AB-037 and related quantitative work.

### 13.4 Authorization and qualification

Authorization, certification and qualification may constrain who may issue or rely on a claim. They are not part of Capability definition identity and do not automatically create a positive claim.

### 13.5 Constraint and admissibility

A valid claim does not prove that the Resource is admissible in an Operation context. Applicable Constraints remain separate inputs.

### 13.6 Assignment

Assignment records participation and role. It neither grants Capability nor proves that the Resource satisfies a role requirement.

### 13.7 Operation requirements

An Operation may reference an exact required Capability through a future normative owner. Requirement satisfaction and matching are not defined by AD-007.

### 13.8 Outcome evidence

Past successful performance may be evidence. It does not establish permanent future capability without an exact reviewed claim rule.

## 14. Admissible outcomes

External review must compare explicit outcomes.

### Outcome A — Resource-local attribute

Capability possession is represented as a local attribute or exact Capability reference embedded in Resource.

This outcome avoids a separate record but risks mutable history, missing provenance, no conflicting assertions and collapse of Resource identity with a time-varying claim.

It is admissible only if it can preserve attributable history, exact evidence, temporal applicability, disagreement and fail-safe semantics without turning Resource into an unbounded semantic container.

### Outcome B — single CapabilityClaimRecord

A P-001 identified record binds one exact Resource to one exact Capability definition under stated conditions, authority, evidence, time and proposition.

This outcome must define whether the record is declaration, evaluation or both, and prove that one record does not conflate claimant assertion with independent verification.

Likely P-001 modules to evaluate: A for temporal effectivity, C for supersession, and B only if lifecycle is necessary. No module is selected by this discovery.

### Outcome C — CapabilityAssessmentRecord

The holder relation exists only as an attributable evidence-based evaluation conclusion. A dedicated assessment record binds Resource, exact Capability, criterion, snapshots, evaluator and conclusion.

This outcome may provide strong fail-safe semantics but risks calling every declaration an assessment and duplicating OCP-011 without sharing its Objective-only target contract.

It must justify why the term `claim` remains useful and whether declarations without evaluation are excluded or represented elsewhere.

### Outcome D — declaration plus assessment records

A CapabilityClaimRecord captures an attributable holder assertion, while a separate CapabilityClaimAssessmentRecord evaluates that assertion or the underlying Resource/Capability proposition.

This outcome preserves issuer and evaluator separation and contradictory evidence, but increases record and resolution complexity. It must define which layer AB-011 may consume and whether an unevaluated declaration has any operational authority.

Each record requires its own complete semantic owner and P-001 invocation if selected.

### Outcome E — derived-only holder view

No standing holder claim record is stored. An exact rule derives the current proposition from governed evidence, qualification and snapshots.

This outcome avoids stale mutable claims but must preserve attribution, replay, historical conclusions, contradictory evidence and deterministic resolution. It must not substitute current data for historical snapshots.

### Outcome F — domain-local claims with a Core interoperability envelope

Domain specifications own claim semantics. Core defines only exact Resource and Capability endpoints, minimum provenance, fail-safe requirements and cross-domain reference rules.

This outcome limits Core scope but must prove that AB-011 and cross-domain planning can consume claims without semantic ambiguity or label-based matching.

### Sequenced outcome

The Board may choose a staged combination, but it must name each layer, owner, authority, migration rule and graph effect. An unspecified blend is not a decision.

## 15. P-001 decision matrix

AD-007 does not invoke P-001. A downstream record outcome must explicitly decide:

- stable record identity;
- semantic owner;
- exact Resource endpoint;
- exact Capability endpoint;
- governed record kind or proposition;
- provenance and authority;
- validation and fail-safe rules;
- authoritative statement;
- Module A temporal effectivity, including overlap and gaps;
- Module B lifecycle and authoritative transition history, if any;
- Module C supersession, including branching and binding-identity preservation.

Using a P-001-shaped container without all required elements and selected-module obligations is invalid.

## 16. AB-011 Resource interchangeability boundary

AD-007 must enable but not solve AB-011.

A future interchangeability decision may consume:

- exact Capability claims or evaluated claim conclusions;
- exact Operation Capability requirements;
- applicable Constraint results;
- operational context;
- availability, capacity and Readiness when those models exist.

It must still preserve:

```text
Resource A ≠ Resource B
```

Matching claims do not merge identities, authorize substitution or prove equivalent performance. Interchangeability is contextual and may be asymmetric, conditional and time-bounded.

AD-007 must state which claim projection, if any, AB-011 may treat as authoritative input and how conflicting or absent claims fail closed.

## 17. Required downstream deliverables

Any selected outcome must define:

1. claim or derivation identity;
2. exact Resource and Capability endpoints;
3. proposition and polarity semantics;
4. issuer, evaluator and authority roles;
5. evidence and immutable snapshot contract;
6. evidence-state and fail-safe matrix;
7. condition identity and applicability;
8. temporal effectivity and replay;
9. correction, withdrawal, revocation and supersession;
10. contradiction and multi-head semantics;
11. exact P-001 invocation where records are selected;
12. no-inheritance rules;
13. boundary from Readiness, availability, capacity, authorization, admissibility and Assignment;
14. authoritative projection consumable by AB-011;
15. migration treatment for existing domain holder labels or attributes;
16. executable counterexamples and exact rules manifest.

## 18. Required executable counterexamples

At minimum, a downstream normative cycle must prove:

- two Resources of the same type may have different claims;
- one Resource may have a claim for Capability v1 but not v2;
- supersession of a Capability definition does not rewrite historical claims;
- registry membership does not create a holder claim;
- Resource classification does not create a holder claim;
- Assignment role does not create a holder claim;
- Operation requirement does not grant Capability;
- a positive claim does not imply Readiness or availability;
- a positive claim does not imply authorization or admissibility;
- missing evidence cannot produce an authoritative positive claim;
- stale evidence cannot produce an authoritative positive claim;
- conflicting evidence or claims cannot be resolved by newest timestamp or list order;
- withdrawal or expiry does not create a negative claim;
- absence of a claim does not create a negative claim;
- one successful Event or OutcomeAssessmentRecord does not automatically create a standing claim;
- composite/component Capability inheritance is absent by default;
- Organization claim inheritance is absent;
- matching claims do not collapse Resource identities or authorize automatic substitution;
- malformed, unresolved or ambiguous Resource/Capability references fail closed;
- selected P-001 manifests exactly cover emitted validation codes and derivations.

## 19. Explicitly not defined

AD-007 does not define:

- an accepted CapabilityClaimRecord schema;
- an accepted CapabilityAssessmentRecord schema;
- claim lifecycle or vocabulary;
- confidence, probability, proficiency or maturity scales;
- quantitative capacity or performance model;
- current Readiness or availability;
- authorization, certification or qualification policy;
- Operation Capability requirement representation;
- matching, ranking, optimization or substitution algorithm;
- Organization holder semantics;
- automatic inheritance or aggregation;
- domain-specific Capability evidence catalogs;
- claim persistence, API, eventing, UI or access control;
- cryptographic attestation or non-repudiation;
- any current Concept graph edge;
- any P-001 invocation;
- any AB-011 interchangeability conclusion.

## 20. External review target

Attempt to falsify the boundary with cases where:

1. Resource type or registry membership silently creates possession;
2. claim declaration and independent assessment are conflated;
3. no-claim, negative, expired and withdrawn states collapse;
4. a claim silently becomes Readiness, availability or capacity;
5. authorization, certification or admissibility is embedded into claim identity;
6. missing, stale, ambiguous or conflicting evidence yields a positive claim;
7. latest timestamp, issuer count or storage order selects authority;
8. Capability version supersession rewrites historical claims;
9. claim correction changes Resource, Capability or condition binding identity;
10. withdrawal or revocation erases history or creates the opposite proposition;
11. Resource composition or Organization membership creates unjustified inheritance;
12. successful past performance becomes permanent standing capability;
13. a P-001 record is incomplete or selects modules only nominally;
14. domain-local semantics cannot interoperate across namespaces;
15. AB-011 consumes label equality or claim similarity as Resource identity equality;
16. the model cannot represent two simultaneous contradictory attributable claims without hiding one;
17. temporal intervals allow an unchecked overlap to manufacture a positive effective claim;
18. a claim bound to an unresolved or ambiguous Resource/Capability reference remains permissive.

## 21. Exit criteria

AD-007 is ready for Architecture Board decision when:

- one explicit outcome or sequenced model survives external adversarial review;
- the claim proposition and authority are exact;
- Resource-only initial holder scope remains intact;
- exact Capability version binding is preserved;
- declaration/evaluation separation is explicit;
- no-claim, negative, indeterminate, withdrawn and expired semantics are not collapsed;
- evidence and fail-safe behavior are specified;
- temporal, correction and contradiction semantics are explicit;
- required P-001 modules are selected completely or explicitly rejected;
- no-inheritance defaults survive review;
- boundaries from Readiness, availability, capacity, authorization, admissibility, Assignment and Operation requirements survive review;
- AB-011 receives a precise authoritative input contract without pre-solving substitution;
- downstream normative owner, executable fixtures and manifest obligations are named;
- unresolved Organization-holder semantics remain bound to AB-006 and AB-052.

## 22. Architecture Board status

Revision `0.1.0` opens AD-007 and AB-057 as `Discovery`.

No outcome, record schema, P-001 invocation, Concept edge or Resource-interchangeability rule is accepted by this revision.
