# AD-001 — Relationship as Foundation

- Status: Accepted
- Owner: Architecture Board
- Created: 2026-08-02
- Decision-Date: 2026-08-03
- Decision: Option C — Relationship as a governed modeling pattern
- Applies-To: PR-0007 and subsequent Concept specifications

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

If every Concept defines relations independently, OCP may duplicate identity, directionality, temporal effectivity, lifecycle, provenance, supersession, validation and graph constraints.

If one universal Relationship is introduced too early, it may become an untyped container that weakens Concept boundaries and replaces specialized domain semantics.

## 4. Considered options

### Option A — Local relationships only

Each defining document owns its local relation structures and rules.

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

Relationship is not itself a fundamental domain Concept. Each defining Concept remains responsible for relation meaning, allowed endpoint types, directionality, lifecycle, temporal rules, invariants and derivations.

Shared tooling may provide reusable technical structures, but those structures do not become an independent normative Concept.

Advantages:

- preserves domain ownership of semantics;
- allows shared validation patterns;
- avoids premature universalization;
- specialized Concepts such as Assignment remain independent.

Risks:

- some duplication remains;
- common contracts may emerge slowly;
- governance is required to prevent inconsistent local models.

## 5. Decision

Architecture Board accepts **Option C — Relationship as a governed modeling pattern**.

`Relationship` is not registered as a fundamental Concept in OCP-000 or OCP-002.

A defining Concept may introduce a local identified relationship record when the relation requires independent identity, temporal effectivity, lifecycle, provenance, supersession, relation-specific attributes, authorization or constraints.

The local record remains part of the defining Concept model and does not become a universal OCP Relationship Concept.

## 6. Governing principles

### GP-1 — Semantics remain domain-owned

A generic technical mechanism must not invent relationship semantics. Meaning is defined by the owning Concept or specification.

### GP-2 — Specialized Concepts are not reduced to generic relationships

`Assignment`, `Constraint`, and future Concepts with independent domain meaning remain separate Concepts even if they connect other entities.

### GP-3 — No arbitrary relationship type strings

Normative relationship kinds require a stable identifier, defining specification, version and explicit endpoint contract.

### GP-4 — Reification threshold

A relation should be represented as an identified record when one or more of the following are required:

- independent identity;
- temporal effectivity;
- lifecycle or transition history;
- provenance or evidence;
- supersession or amendment history;
- relation-specific attributes;
- relation-specific authorization or constraints.

A relation that has none of these properties may remain a direct reference or derived edge.

### GP-5 — One normative home

Each relationship kind has one normative defining location. Shared tooling may implement it but does not redefine it.

### GP-6 — Derived edges are not authoritative records

A derived graph edge must identify the authoritative record or derivation rule from which it is derived.

## 7. Consequences for PR-0007

PR-0007 shall:

1. define Organization independently of its relations;
2. prohibit one generic `parent_id` as the authoritative organization model;
3. define explicit local `OrganizationRelationshipRecord` structures where reification criteria are met;
4. distinguish structural hierarchy from operational, administrative, support and coordination relations;
5. define graph constraints separately for each governed relationship kind;
6. allow horizontal relations between organizations belonging to different verticals;
7. include temporal effectivity and provenance contracts;
8. include executable fixtures for accepted invariants and counterexamples.

## 8. Non-consequences

This decision does not:

- require every direct reference to become a record;
- introduce one universal relationship lifecycle;
- define a universal relationship type registry;
- convert Assignment or Constraint into relationship subtypes;
- decide Organization identity continuity or organizational classification.

## 9. Reconsideration criteria

The decision may be reviewed if two or more independent defining Concepts require materially identical normative contracts for relation identity, endpoints, lifecycle, temporal effectivity, provenance, supersession, validation and derivation.

Similarity of implementation classes alone is insufficient. Shared domain semantics must also be demonstrated.
