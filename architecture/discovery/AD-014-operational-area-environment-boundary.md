---
Decision-ID: AD-014
Title: Operational Area and Environment Boundary
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: OCP-001, OCP-002, OCP-003, OCP-004, OCP-005, OCP-006, OCP-007, OCP-014, OCP-015, AD-010
Applies-To: AB-008, Operational Area candidate, Environment taxonomy category, Infrastructure Resource boundary
Review-After: external comparison demonstrates an independently identified spatial or environmental owner and complete fail-safe evidence
---

# AD-014 — Operational Area and Environment Boundary

## 1. Trigger and purpose

The current foundation uses three related ideas without yet giving them one accepted boundary:

- OCP-003 classifies a concrete Position Site, Launch Site or Relay Site as an `Infrastructure Resource` when it is an identified managed object that can be assigned or used;
- OCP-004 says an Operation may occur in one or more `Operational Area`, but Operational Area remains a Proposed candidate without an identity or reference contract; and
- OCP-002 contains `Environment` as a taxonomy category, not as a defined Concept.

These statements are compatible only while the terms remain informal. They become unsafe when a product or domain module must decide whether one real thing is a Resource, a spatial context, an environmental observation, a reusable identified area or only a derived view.

AD-014 opens the boundary discovery required by AB-008 and the next unchecked Milestone 1 item. Revision `0.1.0` does not select an outcome, create a Concept or record family, define geometry, add a graph edge, invoke P-001, amend OCP-003/OCP-004, or change the status of Operational Area, Operational Space, Environment or Spectrum.

## 2. Inherited mandates

AD-014 must preserve the following accepted rules.

From OCP-003:

- Resource identity belongs to a concrete managed element at a stated management granularity;
- a concrete launch site may be an Infrastructure Resource and its use in an Operation is represented through Assignment;
- Resource type does not replace instance identity;
- spatial or temporal characteristics do not yet define a Core location model.

From OCP-004 and OCP-005:

- Operation identity is independent of its spatial context;
- Assignment links one exact Resource to one exact Operation;
- sharing an area, time interval or route does not create Operation composition, coordination or Assignment;
- an Operation may be Draft without a finalized spatial binding.

From OCP-006, OCP-007, OCP-014, OCP-015 and AD-010:

- spatial overlap does not create a Constraint result without an explicit accepted rule and inputs;
- a shared operational area does not create an Organization relation or coordination obligation;
- a bare operational-area label is not an exact Coordination context reference;
- visibility, agreement, authorization, selection and commitment require their own governed owners;
- missing or ambiguous references cannot be made permissive through record order, timestamp recency or source count.

From OCP-001 and OCP-002:

- a taxonomy category is not a Concept automatically;
- a new fundamental Concept requires a separate Board decision, status synchronization and graph accounting;
- if an outcome uses P-001, it requires a separate complete invocation;
- executable evidence must be outcome-fair and must not assume a layer rejected by the selected outcome.

## 3. Current evidence and unresolved tension

The repository currently supports these observations:

| Existing statement | Safe reading | Unresolved question |
|---|---|---|
| a concrete launch site is an Infrastructure Resource | the managed site has Resource identity | is its footprint a property, another identified object or a referenced area? |
| Operation may occur in Operational Area | space is part of Operation context | is the area reusable and independently identified, or local to one Operation snapshot? |
| Environment is a taxonomy category | some concepts may be grouped as environmental | is there any real-world entity with one shared Environment identity? |
| observations may describe conditions | an attributable statement may report a condition | does the reported condition identify an environment, or only evidence about one context? |
| two Operations may share a region | their spatial bindings may overlap | no coordination, visibility, agreement or authority follows automatically |

The same physical extent can participate in several different descriptions without those descriptions becoming identical. A managed site, its legal or operational boundary, an Operation's area of interest, an observed weather condition and a radio-frequency condition may be co-located while retaining different identity, authority, time and provenance.

## 4. Decision questions

AD-014 must answer:

1. What exact test distinguishes a managed Infrastructure Resource from a spatial extent or environmental context?
2. Does Operational Area have identity independent of one Operation and one geometry snapshot?
3. If an area is reused, what owns its identifier, boundary revision, time applicability and provenance?
4. Is `Environment` only a taxonomy category, a family of domain-owned contexts, a reusable identified object, or a derived view?
5. How are ambient conditions kept separate from observations, assessments and the entity or context they describe?
6. Can an Operation-local spatial binding satisfy Core needs without a reusable area registry?
7. Which outcome supports exact replay when a boundary or condition changes?
8. What may Core validate without choosing a coordinate reference system, geometry engine, map provider or sensitive dataset?
9. How do domain-specific spatial/environment models interoperate without making labels or geometric similarity authoritative?
10. Which questions belong to AB-008, and which must remain for the separate Core Boundary specification, Spectrum decision or future location model?

## 5. Terms that must remain distinct

| Term | Working meaning in this discovery | Not implied |
|---|---|---|
| managed site | a concrete facility, prepared place or infrastructure object managed as one Resource | every polygon or region is a Resource |
| site footprint | a spatial description associated with a managed site | a second Resource or an Operational Area automatically |
| Operational Area | a spatial context relevant to one or more Operations | Operation identity, ownership, authority or coordination |
| spatial binding | an exact Operation reference to a local or reusable spatial description | a stored graph edge before an outcome is selected |
| Environment category | a taxonomy grouping for environment-related models | a fundamental Environment Concept |
| environmental condition | a condition attributable to a place/context and time | a stable entity identity or universal State |
| observation | an attributable statement about an occurrence or condition | truth, current state or ownership of the observed subject |
| boundary revision | one exact historical representation of a spatial extent | newest or most authoritative boundary by timestamp |
| overlap | a result of one explicit geometry rule over exact inputs | coordination, conflict, visibility or permission |

## 6. Independent-identity tests

An Operational Area or Environment candidate can receive positive identity only if external evidence demonstrates all applicable tests:

1. **Independent reference:** users must refer to the same thing across more than one Operation without relying only on equal geometry or label.
2. **Independent continuity:** the thing remains identifiable when its boundary, description or observed conditions change.
3. **Independent lifecycle or revision:** change, correction and retirement have an owner distinct from an Operation lifecycle and Resource lifecycle.
4. **Independent relations:** useful relations cannot be reduced to an Operation-local field, Resource characteristic, Constraint input or observation.
5. **Independent authority:** an accepted actor or registry owns identity and revisions; the caller cannot invent authority by supplying a label.
6. **Non-duplication:** the candidate is not merely a concrete Resource, a geometry value, a condition snapshot, an ObservationRecord or a local domain profile.

Passing only “has a name”, “has coordinates”, “is shown on a map” or “is used by several Operations” is insufficient. Equal geometry does not prove equal identity, and changed geometry does not by itself prove a new identity.

## 7. Candidate outcomes

### A — Operation-local spatial binding; Environment remains a category

Operational Area is not independently stored in Core. Each Operation exact-binds an immutable local spatial description or opaque spatial reference inside its own governed snapshot. Managed sites remain Resource. Environment remains a taxonomy category and domain input.

This is the smallest no-new-identity outcome. Its main risk is duplicated area descriptions and weak reuse when several Operations intentionally depend on the same governed boundary.

### B — reusable OperationalArea identified record

Core defines one separate identified record for a reusable area and its exact boundary revision. Operations reference an exact area revision. The record is not a fundamental Concept unless independent Concept evidence is later accepted.

This makes reuse and history explicit without promoting a taxonomy category. Its main risks are premature record authority and an incomplete P-001/time/revision contract. A later implementation must either invoke P-001 completely or give a reviewed reason why the record is outside P-001.

### C — Operational Area as a fundamental Concept

Operational Area receives its own accepted identity, lifecycle, owner and explicit relationships. Operation may then depend on it through a separately approved graph edge.

This is admissible only if §6 is satisfied. Its main risk is turning a frequently local geometry/context value into a universal Core entity and duplicating Resource, Constraint or domain geography models.

### D — Environment as a fundamental context Concept

Environment becomes an independently identified context that may own or relate reusable areas and environmental condition histories. Operational Area is a specialization, component or exact reference under that model.

This is the broadest outcome. It must prove that one Environment identity survives changing conditions and is not merely a taxonomy category, spatial container or collection of observations. Its main risk is a “universal context” Concept that absorbs location, weather, spectrum, infrastructure, State and domain semantics without one legitimate authority.

### E — derived-only spatial/environment view

Core stores no area identity. A view derives an Operation footprint or environmental context from exact Operation, Assignment, Resource-location, route and Constraint inputs under one exact rule and snapshot.

This avoids a registry but is admissible only if every input type and derivation owner already exists. Its main risk is inventing a location model the foundation does not yet have or recomputing history from current data.

### F — domain-local models with a Core interoperability envelope

Each domain owns its area/environment identities, geometry rules and condition vocabularies. Core accepts only exact namespace/version/profile bindings and a small fail-safe interoperability envelope.

This protects domain semantics. Its main risks are incompatible identities, ambiguous cross-profile references and moving Core evidence into domain fixtures that cannot demonstrate cross-domain behavior.

## 8. Infrastructure Resource boundary

The initial discriminator is management identity, not mobility or shape.

| Case | Resource reading | Spatial/environment reading |
|---|---|---|
| concrete prepared launch site with an owner and use history | one Infrastructure Resource | its footprint/conditions are separate descriptions |
| relay installation with assignable operational use | one Infrastructure Resource | coverage area is not automatically the installation |
| named region used only to scope an Operation | no Resource identity shown | local or reusable Operational Area candidate |
| weather, terrain or spectrum condition at a place/time | not a Resource merely because it affects use | condition/evidence owned by a selected context model |
| arbitrary polygon drawn for one plan | not a managed object | Operation-local spatial binding under A, or input to another selected outcome |
| managed site and an area with equal geometry | identities remain distinct | equality of geometry creates no identity collapse |

An Infrastructure Resource may be assigned to an Operation. Its surrounding area, footprint, coverage or environmental conditions do not inherit that Assignment. Conversely, referring to an Operational Area does not assign every Resource located there.

## 9. Spatial identity, revisions and time

Any outcome that claims reusable spatial identity must separate:

- stable area identity;
- exact boundary revision or immutable geometry snapshot;
- time for which the boundary is asserted applicable;
- provenance and authority for the revision;
- Operation-local purpose for using the area; and
- any derived overlap or containment result.

A later boundary does not rewrite an earlier Operation snapshot. No rule may choose a boundary by newest timestamp, storage order, largest area, issuer count or label similarity. Zero or multiple exact resolutions are non-permissive.

This discovery does not select polygon, corridor, volume, point, route, altitude, coordinate reference system, precision or topology semantics. Those are implementation/domain questions until a concrete Core consumer proves otherwise.

## 10. Environmental conditions and observations

An environmental condition must not silently become a mutable field on Environment, Operational Area, Resource or Operation.

At minimum, a positive outcome must distinguish:

```text
subject or context reference
condition kind and governed vocabulary
spatial applicability
temporal applicability or observation time
source / observer / evaluator attribution
provenance and evidence
recorded time
correction or supersession history, if stored
```

An ObservationRecord may provide attributable evidence about a condition, but it does not create Environment identity or select truth. A later assessment may evaluate suitability for one use, but that conclusion is not universal Readiness, availability, authorization or permission.

Spectrum remains a separate Proposed question. AD-014 may use spectrum conditions as a counterexample, but cannot decide whether Spectrum belongs to Environment or becomes a Concept.

## 11. Authority gaps

Before any positive selection, these owners must be explicit:

| Binding or conclusion | Current owner or gap | Fail-safe requirement |
|---|---|---|
| managed-site identity | OCP-003 Resource contract | geometry cannot merge or split Resource identity |
| Operation spatial use | OCP-004 states intent but has no exact contract | bare label is unresolved |
| reusable area identity | absent | caller-supplied ID has no Core authority |
| boundary revision | absent | no latest-boundary fallback |
| geometry interpretation | absent/domain-local | unknown profile or CRS is non-comparable |
| environmental subject | absent/unselected | condition cannot float without exact context |
| condition vocabulary | domain-local/unselected | label similarity is not equivalence |
| overlap/containment rule | absent | no implicit geometry conclusion |
| coordination consequence | OCP-014/OCP-015 and AD-010 controls | overlap creates no agreement or obligation |
| suitability/admissibility | named consumer and Constraint/assessment rule required | environmental evidence alone cannot decide it |

## 12. Mandatory counterexamples

Every admissible outcome must address these cases without sensitive coordinates:

1. one managed Launch Site and one Operational Area have equal geometry but distinct identities;
2. a site boundary changes while the Infrastructure Resource identity remains stable;
3. two Operations use the same area reference but have no parent/child or coordination relation;
4. two Operations have overlapping areas but no agreement, visibility or authorization conclusion;
5. one Operation uses two non-contiguous spatial bindings;
6. one reused named area receives a corrected boundary without rewriting earlier Operation evidence;
7. two equal geometries from different authorities do not collapse into one area;
8. one label resolves to zero or multiple area/profile identities and fails closed;
9. a Resource is located in an area but has no Assignment to the Operation;
10. an assigned Infrastructure Resource has a footprint outside the Operation's area without automatic invalidity;
11. an environmental observation is stale, missing, ambiguous or conflicting and cannot create a positive suitability conclusion;
12. a later observation does not mutate an earlier environmental snapshot;
13. an unknown coordinate/profile version cannot be compared by best effort;
14. a derived footprint lacks one historical input and cannot be replayed from current state;
15. domain A and domain B use similar condition labels with different semantics;
16. a shared area does not create an Organization relationship;
17. environmental evidence does not create Readiness, availability, authorization, selection or Assignment;
18. record order, newest timestamp, area size, source count and issuer count never select authority.

## 13. Unconditional evidence obligations

The following obligations apply to A–F:

1. preserve Infrastructure Resource identity independently of all spatial descriptions;
2. preserve Operation identity independently of its spatial context;
3. reject unresolved or ambiguous exact references;
4. preserve historical inputs rather than substituting current geometry or current conditions;
5. keep observation/evidence attribution separate from truth and decision authority;
6. prevent spatial overlap from creating coordination, conflict, visibility, authorization or Assignment;
7. prevent environmental inputs from creating Readiness or another universal conclusion;
8. use only non-sensitive synthetic fixtures and opaque geometry/profile identifiers in Core evidence; and
9. demonstrate every applicable §12 counterexample in human-readable prose plus executable evidence when the selected contract becomes implementable.

No unconditional fixture may require a stored area record, fundamental Concept, geometry engine, domain registry or derived footprint, because at least one admissible outcome rejects each of those layers.

## 14. Outcome-conditional evidence

### 14.1 Outcome A

- prove that the Operation-local snapshot is immutable and replayable;
- prove that equal local geometries do not create a shared identity;
- reject any attempt to reference a local binding as a reusable Core area;
- introduce no placeholder area registry or Environment object.

### 14.2 Outcome B

- define exact area-record identity, revision, effectivity and provenance;
- decide and satisfy the full P-001 invocation boundary;
- prove zero/multiple resolution, branching/correction and historical replay;
- keep area record separate from Resource and environmental condition evidence.

### 14.3 Outcome C

- pass every independent-identity test in §6;
- define lifecycle, owner and non-duplicative relationships before status promotion;
- synchronize OCP-000/OCP-002/defining metadata and graph edges only in the later Concept PR;
- prove why a Concept is necessary beyond B's record contract.

### 14.4 Outcome D

- pass §6 separately for Environment and any Operational Area identity;
- prove that changing conditions do not redefine Environment identity;
- define boundaries between Environment, Resource, ObservationRecord, Constraint and domain models;
- prevent a universal context object from becoming an unowned container for Spectrum, weather, terrain, State or authorization.

### 14.5 Outcome E

- name every exact input, rule/version, snapshot and query time;
- prove deterministic replay without wall clock or current-state lookup;
- return non-permissive output for missing, ambiguous or incomparable input;
- show that the derivation does not depend on an unaccepted Resource-location model.

### 14.6 Outcome F

- define exact domain/profile namespace and version ownership;
- demonstrate ambiguity detection and rejection across incompatible profiles;
- place domain semantics and sensitive geometry outside Core fixtures while retaining synthetic interoperability evidence;
- prove that Core does not infer equivalence from labels or shape similarity.

## 15. Outcome-fairness audit

External review must reject any evidence plan that assumes the selected answer. In particular:

- A and E cannot be required to demonstrate stored area withdrawal or supersession lineage;
- A, C, D, E and F cannot be required to invoke P-001 merely because B may do so;
- A and F may place spatial semantics outside Core fixtures, but must still satisfy the Core fail-safe envelope;
- B cannot be rejected only because it is not a fundamental Concept;
- C and D cannot pass only because the taxonomy already contains the words Operational Area or Environment;
- E must demonstrate snapshot replayability rather than stored-record lineage; and
- F must demonstrate profile ambiguity detect-and-reject rather than one universal Core vocabulary.

The falsification target is explicit: **evidence obligations assume a layer rejected by the selected outcome**.

## 16. External-review falsification targets

External review must try to disprove:

1. that managed object identity and spatial extent are cleanly separated;
2. that the outcome set includes the smallest no-new-identity controls as well as positive identities;
3. that Environment is not promoted merely from its taxonomy category;
4. that Operational Area identity is tested independently of label and geometry equality;
5. that every reusable outcome has legitimate revision/time/provenance authority;
6. that observations and environmental conditions remain separate from truth and decision authority;
7. that no outcome creates implicit coordination, Organization relation, Assignment or Resource equality;
8. that no outcome decides Spectrum, AB-006, the full Core Boundary specification or a coordinate standard;
9. that §13 is unconditional and §§14–15 remain outcome-fair; and
10. that the discovery is understandable to a human reader without inspecting checker code.

## 17. Decision criteria

The Architecture Board should prefer the smallest outcome that supplies all demonstrated consumers with:

- exact identity or an explicit decision that no reusable identity exists;
- deterministic historical replay;
- a legitimate owner for revisions, rules and vocabularies;
- fail-safe unresolved/ambiguous behavior;
- separation from Resource, Operation, ObservationRecord and Constraint authority;
- cross-domain interoperability only where concrete evidence requires it; and
- no new Concept, record or graph edge whose independent responsibility has not been proven.

A broader outcome is justified only if a narrower outcome fails a concrete consumer or counterexample. Convenience for database design, map display, search, caching or API reuse is not independent ontology evidence.

## 18. Exit criteria

AD-014 may leave Discovery only when:

1. an external comparison has evaluated A–F against §§6, 11 and 12;
2. managed sites, spatial extents, environmental conditions and observations have non-overlapping authority;
3. every outcome has its own feasible evidence block or explicit semantic equivalent;
4. the outcome-fairness falsification target is closed;
5. any positive identity has a named owner, lifecycle/revision model and exact reference boundary;
6. sensitive spatial data is unnecessary for Core validation;
7. the selected direction states what remains domain-local and what Core may reject mechanically; and
8. the Board selection is a separate act from any OCP, Pattern, schema, fixture, Concept-status or graph change.

## 19. Discovery status and next cycle

Revision `0.1.0` opens the boundary and moves AB-008 from `Open` to `Discovery`. It records no preferred outcome.

The next PR should be `AD-014A — Compare Operational Area and Environment Outcomes`. It must add concrete consumer scenarios, authority accounting and complete A–F counterexample mapping without selecting an outcome. A later `AD-014B` Board act may select a direction or retain Discovery. Any OCP amendment, P-001 invocation, Concept registration, graph edge, schema or executable implementation requires a later separately reviewed PR.

