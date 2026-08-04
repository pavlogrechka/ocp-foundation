---
Decision-ID: AD-005
Title: Capability Boundary
Version: 0.3.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-003, OCP-007, AD-002
Applies-To: AB-004, AB-011, Capability model and registry
Review-After: External adversarial boundary review
---

# AD-005 — Capability Boundary

## 1. Trigger and current state

Capability is present in the Foundation roadmap and future-intent map, but it is not yet a defined fundamental Concept.

Current accepted artifacts already use the word in several distinct senses:

- Resource descriptions refer to what a Resource may be able to do;
- domain and capability modules classify specialized Resource and Operation types;
- planning may need to compare an Operation need with what a Resource or Organization can provide;
- AD-002 explicitly states `Capability ≠ Readiness`;
- AB-004 asks for the boundary of a Capability Registry;
- AB-011 postpones Resource interchangeability until Capability and Constraint are understood.

These uses do not yet establish one identity model, one registry authority, a holder relationship, aggregation semantics, or a current Concept dependency.

The non-normative future edge `Resource ⇢ Capability` remains planning intent only. AD-005 does not promote it into the current Concept graph.

## 2. Boundary question

AD-005 asks whether Capability should be:

1. a fundamental reusable Concept with identity independent of any holder;
2. a holder-specific identified assertion or assessment;
3. a two-layer model separating reusable Capability definitions from holder claims;
4. a domain-owned descriptor governed only by a Core interoperability pattern;
5. rejected as a Core abstraction because existing Resource, Assignment, Constraint, Readiness and domain models are sufficient.

The discovery must distinguish at least three semantic layers that are often collapsed:

- **Capability definition** — what function, effect or class of performance is being described;
- **capability claim** — an attributable statement that a subject has or can provide that capability under stated conditions;
- **current usability** — whether the subject is available, ready, authorized and admissible in a specific operational context.

No layer is selected as a fundamental Concept merely because all three are useful to planning.

## 3. Initial semantic hypothesis

A candidate Capability definition represents an ability or potential to perform a function or produce a class of effect under stated conditions.

This is a boundary hypothesis, not an accepted definition.

A Capability definition may justify independent identity when it is reused by multiple Resources, Organizations, Operations, requirements, constraints or domain modules without copying its meaning into each consumer.

A statement that a particular subject has a Capability is not automatically the Capability itself. It may instead require a local or identified claim record with provenance, evidence, applicability and validation semantics.

## 4. What Capability is not

Capability is not automatically:

- a Resource type or taxonomy node;
- a Resource instance;
- an Organization;
- an operational role;
- an Assignment;
- an Operation type;
- an Objective or intended outcome;
- an Event or Result;
- current availability;
- Readiness;
- lifecycle State;
- quantity, throughput, stock, capacity or remaining endurance;
- authorization, permission or command authority;
- qualification, certification or accreditation;
- a Constraint or proof that applicable Constraints are satisfied;
- an API feature, software module, service or user permission;
- evidence that a claimed effect was actually achieved.

A Resource can possess a Capability while being unavailable, unready, unauthorized or inadmissible for a particular Operation.

A Resource can be assigned a role without satisfying the Capability required for that role unless an explicit validation rule establishes the match.

A successful Result does not automatically establish a persistent Capability claim for future contexts.

## 5. Independent identity test

A fundamental Capability Concept is justified only if external review confirms material identity independent of a particular holder or use.

Evidence for independent identity may include:

- reuse of the same governed Capability definition across multiple Resources or Organizations;
- references from multiple Operations or requirements without copying semantic content;
- stable namespaced identity and versioning independent of holder records;
- amendment or supersession of the definition without changing holder identity;
- domain ownership of specialized semantics while preserving Core reference integrity;
- validation rules that distinguish definition validity from holder-claim validity;
- consumers that need to resolve the same Capability identity across planning, matching, constraints and audit.

Evidence against a fundamental Concept includes:

- the candidate only renames a Resource class;
- identity is always reducible to `subject + local attribute`;
- the definition has no semantics outside one domain module;
- all useful meaning belongs to current readiness, capacity, Assignment role or Constraint evaluation;
- a registry would merely centralize labels without governed identity or version semantics.

## 6. Holder boundary

Candidate subjects of capability claims include Resource and Organization.

AD-005 does not approve a universal `has_capability` relationship or a current Concept dependency.

The downstream decision must determine whether:

- a Resource may hold a direct Capability claim;
- an Organization may hold an independent organizational Capability claim;
- an Organization Capability can be derived from members or subordinate Resources;
- a composite Resource inherits Capability from components;
- a component inherits Capability from a composite Resource;
- an Operation declares required Capability without itself possessing Capability;
- an Assignment role may reference a required Capability without granting it.

Default rule for this discovery: **no inheritance, aggregation or transitive possession is implied**.

The presence of capable members does not by itself prove an organizational Capability. The Capability of a composite Resource is not automatically the union of component capabilities. Any derivation requires an explicit normative owner, conditions and counterexamples.

Claim-subject typing inherits the unresolved `Organization ↔ Organizational Resource` boundary recorded in AB-006 and AB-052. AD-005 does not decide whether a unit is referenced as Organization, Organizational Resource or through an explicit mapping; the downstream Capability decision must bind that subject type without identity collapse.

## 7. Capability, Readiness, availability and admissibility

AD-002 supplies a mandatory guardrail:

```text
Capability ≠ Readiness
```

The boundary must preserve the following distinctions:

- Capability describes what may be possible under governed conditions;
- availability describes whether the subject can be considered for use at a time;
- Readiness, if later defined, describes evidence-based preparedness for a context;
- Constraint evaluation determines admissibility under explicit rules;
- Assignment establishes contextual participation and role;
- authorization permits an action or transition under a separate authority model.

None of these states may be derived solely from the absence of negative evidence.

A valid Capability claim must not silently normalize to `ready`, `available`, `authorized`, `assigned` or `admissible`.

## 8. Conditions, evidence and time

A reusable Capability definition may be relatively stable, while a holder claim may depend on changing conditions.

Candidate claim dimensions include:

- subject reference;
- exact Capability definition reference;
- applicability conditions;
- provenance and attributable claimant or evaluator;
- evidence reference and evidence time;
- validation rule and version;
- validity or review interval;
- confidence, level or qualification where a domain requires it;
- supersession or withdrawal.

AD-005 does not approve these as fields.

Qualification, certification or accreditation may be evidence input to a holder claim where a domain rule requires it. They are never part of Capability identity and never create an authoritative positive Capability claim automatically.

The downstream model must decide which dimensions are part of identity, which are immutable evidence, which are derived projections and which remain domain-specific.

Missing, stale or conflicting evidence must not become a permissive positive Capability claim by default. The exact fail-safe contract belongs to the selected downstream outcome.

## 9. Registry boundary and namespaces

AB-004 uses the term Capability Registry. A registry is justified only if it governs resolvable identities rather than maintaining an uncontrolled list of labels.

A candidate registry may need to govern:

- Capability identifier and namespace;
- owning specification or domain authority;
- human-readable name and definition;
- version and supersession;
- lifecycle or publication status;
- compatibility and specialization rules;
- reference resolution;
- validation authority for holder claims.

Core must not enumerate every domain Capability such as platform-specific payloads, radio profiles, sensor modes, spectrum effects or mission techniques.

Domain modules may own specialized Capability definitions under governed namespaces. Core may define only the minimum identity and interoperability contract needed for cross-domain resolution.

A registry entry does not prove that any Resource or Organization currently has the Capability.

## 10. Admissible outcomes

External review must evaluate explicit outcomes rather than assume that Capability is one object.

### Outcome A — domain-local descriptors only

No fundamental Capability Concept is introduced.

Domain modules define local capability descriptors. Core may provide a minimal naming or reference convention, but no universal Capability registry or holder model exists.

Concept graph impact: none.

This outcome is valid only if cross-domain planning and reference integrity can be supported without duplicated or ambiguous semantics.

### Outcome B — reusable Capability definition Concept

Capability is a fundamental reusable definition with identity independent of holders.

Resource and Organization possession is represented by local claim or assessment records owned by their defining specifications or a later pattern.

Concept graph impact: no edge is approved by AD-005. A later defining specification must justify each current dependency explicitly.

This outcome must prove that a Capability definition is more than a taxonomy label and remains semantically complete without any holder.

### Outcome C — holder-specific Capability Concept

Each Capability instance represents a subject-specific ability under conditions and therefore includes or references the holder as part of its identity.

This outcome risks collapsing Capability into a claim, assessment, readiness statement or relationship record. It must justify why a local or P-001 identified record is insufficient.

Concept graph impact: potentially Resource or Organization to Capability, but no edge is approved by this discovery.

### Outcome D — two-layer definition and claim model

A reusable Capability definition is separated from an identified Capability claim or assertion that binds one subject to one exact definition under conditions and evidence.

The definition may be a fundamental Concept. The claim may be a binding-when-invoked record, potentially using P-001, without becoming a fundamental Concept.

This outcome must define authority, endpoint contract, version binding, evidence, temporal semantics and the boundary from Readiness and authorization.

Concept graph impact: determined only after the two layers and their owners are accepted.

### Sequenced or alternative outcome

The Architecture Board may select another explicit outcome or a sequenced transition, but it must state:

- interim and target semantic owners;
- migration and compatibility rules;
- graph impact at each stage;
- registry authority;
- evidence required before the transition;
- treatment of existing domain descriptors.

An unspecified blend of outcomes is not a decision.

## 11. Required downstream deliverables

Any selected outcome must define:

1. whether Capability has independent identity;
2. the boundary between definition and holder claim;
3. the allowed holder types;
4. whether Operation expresses Capability requirements and where those requirements live;
5. registry ownership, namespace and version rules;
6. the relationship to Resource taxonomy and domain specialization;
7. provenance and validation authority;
8. temporal applicability, staleness and fail-safe behavior where claims are supported;
9. aggregation, composition and non-inheritance rules;
10. the boundary from Readiness, availability, capacity, Assignment, Constraint and authorization;
11. exact Concept dependencies and graph acyclicity;
12. migration treatment for existing domain capability labels.

No downstream specification may infer a positive claim from a type label alone unless an explicit reviewed rule owns that derivation.

## 12. Required executable counterexamples

The downstream cycle must include executable or mechanically reviewable evidence for the selected outcome.

At minimum, for every outcome that supports holder claims:

- two Resources of the same type can have different Capability claims;
- a Resource with a valid Capability claim can be unavailable or unready;
- an Assignment role does not create a Capability claim;
- an Operation requirement does not grant Capability to an assigned Resource;
- stale, missing or conflicting claim evidence cannot produce an authoritative positive result;
- an Organization does not automatically inherit the union of member capabilities;
- a composite Resource and its components do not inherit capabilities bidirectionally by default;
- a successful Event or Result does not automatically create a standing Capability claim.

Additional evidence is outcome-specific:

- Outcome A must prove interoperability without a Core Concept or central semantic registry and must detect and reject cross-domain reference ambiguity rather than accepting an unresolved label match;
- Outcomes B, C and D must prove that a domain Capability reference resolves through the selected governed namespace and exact-version contract;
- Outcomes B, C and D must prove that changing a Capability definition does not silently reinterpret historical exact-version claims;
- Outcomes B, C and D must prove that the same human-readable label in two namespaces with different semantics remains two distinct identities and that label equality never substitutes for identity resolution;
- Outcome B must prove independent reusable definition identity;
- Outcome C must prove why a local identified claim record is insufficient;
- Outcome D must prove separation of definition, claim, readiness and authorization and complete P-001 conformance if invoked.

## 13. What is explicitly not defined

AD-005 intentionally does not define:

- Capability fields or storage schema;
- a complete Capability taxonomy;
- proficiency, maturity or confidence scales;
- quantitative capacity, throughput, range, duration, stock or consumption;
- availability or Readiness rules;
- certification, qualification or authorization workflows;
- Operation-to-Capability matching or optimization algorithms;
- procurement, inventory or force-development processes;
- Objective achievement or Result evaluation;
- domain-specific Capability catalogs;
- API, database or UI contracts;
- any current Concept edge;
- any P-001 invocation;
- any automatic aggregation or inheritance.

These topics must remain explicit follow-up decisions rather than hidden assumptions in a Capability registry.

## 14. External review target

Attempt to falsify the boundary with cases where:

1. Capability merely renames Resource type;
2. a holder claim is mistaken for the reusable definition;
3. Capability silently becomes Readiness or availability;
4. a role or Assignment grants Capability by implication;
5. a successful Result is treated as permanent Capability proof;
6. organizational Capability is computed as an unjustified union of member capabilities;
7. capability inheritance through Resource composition produces false positives;
8. a Core registry becomes a universal catalog of domain labels;
9. version changes silently reinterpret existing claims;
10. conditions, evidence or staleness are omitted from a holder-specific model;
11. certification or authorization is embedded into Capability identity;
12. Capability and capacity are collapsed;
13. a proposed Concept graph introduces a circular dependency among Resource, Organization, Operation and Capability;
14. a P-001 claim record is used as a semantic container without complete conformance;
15. the selected model cannot support AB-011 interchangeability without treating distinct Resources as the same identity.

## 15. Exit criteria

AD-005 is ready for Architecture Board decision when:

- the definition/claim/current-usability distinction survives external adversarial review;
- one explicit outcome is selected or the document returns to Discovery with named missing evidence;
- the independent-identity verdict is explicit;
- AB-004 receives a registry direction rather than a label-only implementation;
- AB-011 receives a clear dependency on the selected Capability model without pre-solving interchangeability;
- Resource and Organization holder semantics are explicit;
- aggregation and non-inheritance defaults are explicit;
- the AD-002 Capability/Readiness guardrail is preserved;
- proposed dependencies are explicit and acyclic;
- conditional executable evidence is assigned to a downstream normative owner;
- unresolved semantics are recorded as backlog items.

## 16. Architecture Board decision — AD-005C

The Architecture Board accepted this decision by act **AD-005C** on **2026-08-04**, after repeated external verification of AD-005 revision `0.2.0` confirmed Findings F1–F4 as resolved and externally verified.

### 16.1 Selected outcome

The Architecture Board selects **Outcome D — two-layer definition and claim model**.

The independent-identity verdict is positive for the reusable Capability definition: it has identity independent of a particular holder, claim or operational use when governed by an owning namespace, exact version and resolution contract.

This decision does not itself register Capability as a fundamental Concept. A downstream normative specification must define the Capability definition, justify its exact Concept dependencies and perform any Concept-status or graph transition explicitly.

A holder-specific Capability claim remains a separate identified record that binds one subject to one exact Capability definition under governed conditions, provenance, evidence and temporal applicability. The claim is not a fundamental Concept by default. Any use of P-001 requires a separate complete invocation in the downstream normative owner.

### 16.2 Staged holder scope

`Resource` is the initial direct claim-subject type authorized for downstream Capability-claim work.

Organization-specific claims remain deferred until AB-006 and AB-052 bind `Organization`, `Organizational Resource` or an explicit mapping without identity collapse.

No inheritance, aggregation or transitive possession is implied. In particular:

- an Organization does not automatically inherit the union of member or subordinate Resource capabilities;
- a composite Resource and its components do not inherit Capability bidirectionally by default;
- a Resource type, Assignment role, successful Event or Result does not create a Capability claim.

### 16.3 Operation requirement boundary

An Operation may express a requirement for an exact Capability definition, but an Operation does not possess Capability and does not grant Capability to an assigned Resource.

The normative owner and representation of Operation Capability requirements remain downstream decisions. This acceptance introduces no requirement field, matching algorithm or current Concept edge.

### 16.4 Registry direction

AB-004 is directed toward a governed registry of reusable Capability definitions rather than a central list of labels.

The downstream registry contract must govern at least identity, namespace ownership, exact versioning, supersession and reference resolution. Domain modules may own specialized Capability definitions under governed namespaces; Core must not become a universal catalog of domain labels.

Registry membership never proves that any Resource or Organization has the Capability and never establishes current readiness, availability, authorization or admissibility.

### 16.5 Resource interchangeability direction

AB-011 is planned as a downstream decision that may evaluate exact Capability claims together with applicable Constraint results and operational context while preserving the identity of each Resource.

Capability similarity or label equality must not collapse distinct Resource identities or authorize automatic substitution.

### 16.6 Acceptance effect

AD-005C has the following effects:

- AD-005 becomes `Accepted` at version `0.3.0`;
- AB-004 moves `Discovery → Planned` for the normative Capability-definition and registry contract;
- AB-011 moves `Open → Planned` for the separate Resource-interchangeability decision;
- AB-006 and AB-052 remain `Open` and continue to bind Organization-holder semantics;
- no Capability OCP specification, holder-claim schema, registry implementation or domain taxonomy is introduced by this act;
- no current Concept graph edge or P-001 invocation is introduced;
- the AD-002 guardrail `Capability ≠ Readiness` and the fail-safe evidence boundary remain mandatory.

The next normative cycle must define the reusable Capability-definition contract and governed registry direction selected here, with executable evidence from §12. Holder-claim semantics and Resource interchangeability remain explicit downstream work and must not be smuggled into that definition cycle.
