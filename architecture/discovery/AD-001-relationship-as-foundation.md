# AD-001 — Relationship as Foundation

- Status: Discovery
- Owner: Architecture Board
- Created: 2026-08-02
- Review target: before `PR-0007 — Define Organization Concept`
- Decision effect: none until explicitly accepted by Architecture Board

## 1. Question

Should `Relationship` become:

1. a fundamental OCP Concept;
2. a shared modeling pattern used by domain Concepts;
3. or remain a set of local relationship models defined independently by each Concept?

## 2. Context

OCP already avoids hiding operational semantics inside simple attributes:

- `Assignment` explicitly represents contextual participation of a Resource in an Operation;
- `Constraint` explicitly represents an admissibility condition;
- lifecycle and provenance are represented through structured records rather than untracked fields.

The next planned Concept, Organization, requires multiple simultaneous and time-dependent relations:

- structural or штатне підпорядкування;
- operational subordination;
- administrative subordination;
- support;
- coordination;
- horizontal interaction between organizations belonging to different verticals in a shared operational area.

A single `parent_id` cannot represent these relations without semantic loss.

## 3. Problem

If every Concept defines relations independently, OCP may duplicate:

- identity rules;
- directionality;
- temporal effectivity;
- lifecycle;
- provenance;
- supersession;
- validation and graph constraints.

If one universal Relationship is introduced too early, it may become an untyped container that weakens Concept boundaries and replaces specialized domain semantics.

## 4. Options

### Option A — Local relationships only

Each defining document owns its local relation structures and rules.

Examples:

- Organization defines organizational relations;
- Resource defines composition relations;
- Operation defines operation dependencies.

Advantages:

- strong local semantics;
- low abstraction cost;
- fewer universal contracts.

Risks:

- duplicated lifecycle, time and provenance models;
- inconsistent graph semantics;
- repeated implementation and validation patterns.

### Option B — Relationship as a fundamental Concept

Relationship becomes an identified domain entity connecting source and target subjects.

A candidate shared structure could include:

```text
relationship_id
source_ref
target_ref
relationship_type_ref
directionality
effectivity interval
lifecycle history
provenance_ref
supersedes_relationship_ref [optional]
```

Advantages:

- one common graph-edge contract;
- consistent temporal and provenance semantics;
- relations can have identity and history.

Risks:

- generic container anti-pattern;
- domain semantics may be reduced to arbitrary type codes;
- overlap with Assignment, Constraint and future specialized Concepts;
- every relation may be over-modeled as an entity.

### Option C — Relationship as a governed modeling pattern

Relationship is not itself a fundamental domain Concept. OCP-001 defines criteria for when a local relation must be represented as an identified relation record rather than a simple reference.

Each defining Concept remains responsible for:

- relation meaning;
- allowed source and target types;
- directionality;
- lifecycle and temporal rules;
- invariants and derivations.

Shared tooling may provide reusable technical structures, but those structures do not become an independent normative Concept.

Advantages:

- preserves domain ownership of semantics;
- allows shared validation patterns;
- avoids premature universalization;
- specialized Concepts such as Assignment remain independent.

Risks:

- some duplication remains;
- common contracts may emerge slowly;
- requires governance rules to prevent inconsistent local models.

## 5. Candidate principles

### CP-1 — Semantics remain domain-owned

A generic relation mechanism must not invent semantics. Relationship meaning is defined by the owning Concept or specification.

### CP-2 — Specialized Concepts are not reduced to generic relationships

`Assignment`, `Constraint`, and any future Concept with independent domain meaning remain separate Concepts even if they connect other entities.

### CP-3 — No arbitrary relationship type strings

Normative relationship kinds require a defining specification, stable identifier and explicit source/target contract.

### CP-4 — Reification threshold

A relation should be represented as an identified record when at least one of the following is required:

- independent identity;
- temporal effectivity;
- lifecycle or transition history;
- provenance or evidence;
- supersession or amendment history;
- relation-specific attributes;
- relation-specific authorization or constraints.

A relation that has none of these properties may remain a direct reference or derived edge.

### CP-5 — One normative home

Each relationship kind has one normative defining location. Shared tooling may implement it but does not redefine it.

### CP-6 — Derived edges are not authoritative records

A derived graph edge must identify the authoritative record or rule from which it is derived.

## 6. Evaluation against existing OCP

### Assignment

Assignment passes the reification threshold and remains a specialized Concept. It must not be replaced by generic Relationship.

### Constraint

Constraint is not a relationship. It evaluates admissibility relative to a target and context and remains a specialized Concept.

### Resource composition

A simple immutable containment reference may remain local. If containment requires effectivity, provenance or amendment history, the Resource specification may introduce an identified local relation record.

### Operation relationships

Parent/child, dependency and coordination relations may require different semantics. They should not be forced into one generic type until their domain rules are defined.

### Organization

Organization itself should not contain one universal `parent_id`. Structural, operational, administrative, support and coordination relations must be explicitly typed and independently representable.

## 7. Preliminary recommendation

Adopt **Option C — Relationship as a governed modeling pattern** for PR-0007.

Do not register `Relationship` as a fundamental Concept at this stage.

PR-0007 may define a local identified structure such as `OrganizationRelationshipRecord`, provided that:

- its semantics remain inside the Organization defining document;
- relation kinds are closed or governed, not arbitrary strings;
- source and target are Organization instances;
- temporal, provenance and lifecycle contracts are explicit;
- the structure is not presented as a universal OCP Relationship Concept.

## 8. Falsification criteria

The preliminary recommendation should be reconsidered if two or more independent defining Concepts require materially identical normative contracts for:

- relation identity;
- endpoints;
- lifecycle;
- temporal effectivity;
- provenance;
- supersession;
- validation and derivation.

Similarity of implementation classes alone is insufficient. The domain semantics must also be meaningfully shared.

## 9. Consequences for PR-0007

PR-0007 should:

1. define Organization independently of its relations;
2. prohibit a single generic `parent_id` as the authoritative organization model;
3. define explicit local organization relation records;
4. distinguish structural hierarchy from operational, administrative, support and coordination relations;
5. define whether structural relations form a tree, forest or constrained DAG;
6. allow horizontal relations between organizations from different verticals;
7. include temporal effectivity and provenance where required;
8. add executable fixtures for accepted invariants and counterexamples.

## 10. Open questions

- Are all Organization relations directed?
- Which relation kinds may be reciprocal or symmetric?
- Does structural subordination require exactly one effective parent at a time?
- Can operational subordination overlap with structural subordination?
- Can one Organization participate in multiple operational chains simultaneously?
- Does coordination require a separate future Coordination Concept rather than an Organization relation?
- Which Organization relations are authoritative records and which are derived views?
- What cycle constraints apply separately to structural, operational and coordination graphs?

## 11. Decision required

Architecture Board must choose one:

- `Accept Option A — local relationships only`;
- `Accept Option B — Relationship as fundamental Concept`;
- `Accept Option C — Relationship as governed modeling pattern`;
- `Continue Discovery`.

Until that decision, AD-001 is non-normative and Relationship is not added to OCP-000 or OCP-002.
