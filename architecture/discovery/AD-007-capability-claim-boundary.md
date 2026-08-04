---
Decision-ID: AD-007
Title: Capability Claim Boundary
Version: 0.2.0
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

That accepted mandate governs the semantic shape of every admissible AD-007 outcome. It does not require one persistence technology, storage location or materialized projection, and it does not invoke P-001 automatically. It does require the holder claim to retain stable identity distinct from Resource identity and Capability-definition identity, with an exact endpoint, provenance, authority and replay contract. A local or derived representation is admissible only as a materialization of that separate identified-record contract. Rejecting separate claim identity would reopen AD-005C and requires an explicit superseding Architecture Board act supported by new evidence; AD-007 does not perform that reopening.

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

> What separate identified-record contract may assert that one exact Resource has, lacks or may provide one exact Capability definition under stated conditions, evidence, authority and time; which stored, local or derived representation is authoritative for that contract; and how does it avoid turning the assertion into readiness, availability, authorization, admissibility or Resource identity?

The discovery must determine:

1. whether the mandated identified claim record is stored directly, materialized locally or derived reproducibly from governed snapshots;
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

All admissible outcomes preserve the AD-005C semantic mandate: the holder-specific claim remains a separate identified record. Storage and derivation choices may vary, but a Resource field, current view or evidence set cannot replace independent claim identity. The former pure-attribute and no-record forms remain falsification controls only; selecting either would require an explicit reopening of AD-005C before AD-007 outcome selection.

### Outcome A — Resource-local materialization of an identified claim record

The separate identified claim record is materialized within or alongside a Resource representation while retaining its own stable claim identity, exact endpoints, provenance, authority and history.

This outcome avoids a separate Core claim store but risks mutable history, hidden disagreement and collapse of Resource identity with a time-varying claim projection.

It is admissible only if Resource-local placement is a storage choice rather than the semantic authority: multiple attributable claims remain representable, claim identity does not derive from Resource identity, and Resource mutation cannot rewrite claim history.

### Outcome B — single CapabilityClaimRecord

A P-001 identified record binds one exact Resource to one exact Capability definition under stated conditions, authority, evidence, time and proposition.

This outcome must define whether the record is declaration, evaluation or both, and prove that one record does not conflate claimant assertion with independent verification.

Likely P-001 modules to evaluate: A for temporal effectivity, C for supersession, and B only if lifecycle is necessary. No module is selected by this discovery.

### Outcome C — CapabilityAssessmentRecord

The holder claim exists as a separate identified attributable evidence-based evaluation record. A dedicated assessment record binds Resource, exact Capability, criterion, snapshots, evaluator and conclusion and is authoritative only for the exact evaluated proposition.

This outcome may provide strong fail-safe semantics but risks calling every declaration an assessment and duplicating OCP-011 without sharing its Objective-only target contract.

It must justify why the term `claim` remains useful and whether declarations without evaluation are excluded or represented elsewhere.

### Outcome C-prime — extend the OCP-011 assessment contract

The holder claim is a separate identified assessment record implemented by extending accepted OCP-011 with a governed Capability-holder target and assessment profile, such as `capability-holder@1`, rather than introducing a new assessment family.

This outcome reuses exact target, criterion, evidence snapshot, input snapshot, evaluator, fail-safe conclusion and Module C machinery. It is admissible only if external comparison proves that:

- the target contract exact-binds one Resource and one exact OCP-009 Capability version without inventing a hidden universal holder Concept;
- Capability-claim conclusions fit a governed assessment-kind profile without treating `achieved`, `not_achieved` or other Objective vocabulary as universal;
- evidence kinds and authoritative projections remain semantically narrow;
- OCP-011 does not become a generic assessment container or silently establish Readiness, authorization, admissibility or Resource interchangeability.

A dedicated CapabilityAssessmentRecord is justified only if those semantics demonstrably do not fit OCP-011 without diluting its accepted evidence and authority contract.

### Outcome D — declaration plus assessment records

A CapabilityClaimRecord captures an attributable holder assertion, while a separate CapabilityClaimAssessmentRecord evaluates that assertion or the underlying Resource/Capability proposition.

This outcome preserves issuer and evaluator separation and contradictory evidence, but increases record and resolution complexity. It must define which layer AB-011 may consume and whether an unevaluated declaration has any operational authority.

Each record requires its own complete semantic owner and P-001 invocation if selected.

### Outcome E — derived materialization of an identified claim record

No standing claim materialization is stored. An exact rule produces the separate identified claim record from governed evidence, qualification and immutable snapshots, including a stable derivation identity and attributable authority.

This outcome avoids stale mutable projections but must preserve attribution, replay, historical conclusions, contradictory evidence and deterministic resolution. It must not substitute current data for historical snapshots or reduce the record to an unidentified current view.

### Outcome F — domain-local claims with a Core interoperability envelope

Domain specifications own separate identified claim records and their semantics. Core defines only the interoperability envelope: exact Resource and Capability endpoints, stable record identity, minimum provenance, fail-safe requirements and cross-domain reference rules.

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

1. stable identified claim-record identity and authoritative storage or derivation form;
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

Evidence obligations are outcome-fair: the unconditional core covers semantics shared by every admissible outcome, while representation-, ownership- and Pattern-specific obligations apply only when the selected outcome contains that layer. An equivalent must be named where one outcome realizes a shared semantic guarantee through a different mechanism.

### 18.1 Unconditional claim-contract core

Every selected outcome must prove:

- the claim has stable identity distinct from Resource identity and Capability-definition identity;
- two Resources of the same type may have different claims;
- one Resource may have a claim for Capability v1 but not v2;
- Capability-definition supersession does not reinterpret an exact historical claim;
- registry membership, Resource classification, Assignment role and Operation requirement do not create or grant a holder claim;
- a positive claim does not imply Readiness, availability, authorization or admissibility;
- missing or stale evidence cannot produce an authoritative positive claim;
- ambiguous or conflicting evidence cannot produce an authoritative positive claim or select a winner by newest timestamp, issuer count or list order;
- absence of a claim does not create a negative claim;
- one successful Event or OutcomeAssessmentRecord does not automatically create a standing claim;
- composite/component and Organization claim inheritance are absent by default;
- matching claims do not collapse Resource identities or authorize automatic substitution;
- malformed, unresolved or ambiguous Resource/Capability references fail closed.

### 18.2 Representation-conditional evidence

- Stored or materialized record outcomes must prove that withdrawal or expiry does not create a negative claim, supersession preserves historical exact resolution and contradictory attributable records remain visible.
- Outcome A must prove that Resource-local placement does not derive claim identity from Resource identity, does not make a mutable attribute authoritative and does not prevent multiple conflicting attributable claims.
- Outcome E must prove stable derived record identity, historical replay from immutable snapshots and identical conclusions for identical exact inputs; current evidence must not replace historical inputs, and withdrawal, revocation or applicability end must be represented by governed exact inputs without manufacturing a negative claim.
- Outcome F must provide domain-owned fixtures for claim semantics and Core fixtures that detect and reject missing, ambiguous or incompatible interoperability-envelope bindings.
- Outcome C-prime must prove the OCP-011 target, conclusion-profile, evidence-kind and projection fit without weakening its accepted fail-safe matrix or turning it into a generic assessment container.
- Every outcome that invokes P-001 must prove complete Required Elements, selected-module obligations and exact manifest coverage for emitted validation codes and derivations. An outcome that rejects P-001 must not be required to emit P-001 manifests.

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
19. evidence obligations assume a layer rejected by the selected outcome instead of naming an equivalent;
20. a Resource-local or derived representation removes separate claim identity and silently reopens AD-005C;
21. an OCP-011 extension reuses field shape while diluting target, conclusion, evidence or authority semantics.

## 21. Exit criteria

AD-007 is ready for Architecture Board decision when:

- one explicit outcome or sequenced model survives external adversarial review;
- every admissible outcome conforms to the AD-005C separate identified-record mandate, or an explicit prior reopening act supplies new evidence and supersedes that mandate;
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
- executable evidence is divided into an outcome-independent core and explicit outcome-conditional blocks or semantic equivalents;
- unresolved Organization-holder semantics remain bound to AB-006 and AB-052.

## 22. Architecture Board status

Revision `0.1.0` opened AD-007 and AB-057 as `Discovery`.

Revision `0.2.0` addresses external Findings 1–2 and supplemental governance Finding 3 by restoring outcome-fair evidence, adding the OCP-011 reuse alternative and constraining every admissible outcome to the accepted AD-005C separate identified-record mandate. Findings remain open pending repeated external verification of this exact revision.

No outcome, record schema, P-001 invocation, Concept edge or Resource-interchangeability rule is accepted by revision `0.2.0`.
