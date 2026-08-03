---
Document-ID: OCP-007
Title: Organization Concept
Version: 0.3.0
Status: Draft
Concept-Status: Under Review
Defines-Concepts: Organization
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, AD-001, P-001
Uses-Patterns: P-001@0.1.0
Used-By: Organization Model, Coordination Model, Operational Ontology
Last-Review: 2026-08-03
---

# OCP-007 — Organization Concept

## 1. Purpose

This document defines the fundamental Concept `Organization` and the local modeling contract for identified relations between Organization instances.

Organization answers:

> Which organizational entity exists?

It does not answer who currently commands, supports, coordinates with, owns, controls or participates in an Operation.

## 2. Canonical definition

**Organization** is an identified organizational entity that exists independently of any particular Operation, Assignment or temporary organizational relation.

## 3. Ontological boundary

Organization owns organizational identity, classification references, display designation, lifecycle, and provenance of establishment and retirement.

Organization does not define participation in Operation, Assignment, Constraint, Capability, Readiness, command authority, personnel, Resource ownership, or embedded organizational relations.

`Organization ≠ Resource`. A future explicit mapping may relate them without redefining either identity.

## 4. Identity

Each Organization has one stable `organization_id`, independent of display name, commander, personnel, location, current relations, Operation, Assignment and classification changes that preserve identity continuity.

Continuity through reorganization, merger, split or redesignation remains open under AB-044.

## 5. Organization structure

```text
Organization
- organization_id
- classification_refs
- display_name
- transition_history
- created_at
- lifecycle_stage [optional materialized projection]
- established_at [optional materialized projection]
- retired_at [optional materialized projection]
- establishment_provenance_ref [optional materialized projection]
```

The Organization record does not contain an authoritative universal `parent_id`, `children`, `operation_ref`, `assignment_ref`, `constraint_ref` or arbitrary relationship collection.

## 6. Organization lifecycle

Allowed paths:

```text
Draft
Draft → Established
Draft → Established → Retired
Draft → Cancelled
```

`transition_history` is authoritative. Optional lifecycle fields are projections from that history.

`Established` does not imply readiness, availability, capability or participation. `Retired` preserves identity and history.

## 7. OrganizationTransitionRecord

```text
transition_id
organization_ref
from_stage
to_stage
occurred_at
provenance_ref
```

Transition history is linear, temporally non-decreasing and refers only to the same Organization.

## 8. Relationship modeling decision

AD-001 defines Relationship as a governed modeling pattern rather than a universal fundamental Concept.

OCP-007 defines `OrganizationRelationshipRecord` as a local structure. It is not registered as a separate Concept in OCP-000.

## 9. OrganizationRelationshipRecord

```text
relationship_id
relationship_class
relationship_type_ref
source_organization_ref
target_organization_ref
scheme_ref [required for structural records]
validity_start
validity_end [optional]
transition_history
created_at
lifecycle_stage [optional projection]
established_at [optional projection]
terminal_at [optional projection]
establishment_provenance_ref [optional projection]
supersedes_relationship_ref [optional]
```

`relationship_class` is mandatory for Established, Closed and Revoked lineage and must be one of the governed initial classes: `structural`, `operational`, `administrative`, `support`, `coordination`.

`relationship_type_ref` identifies a governed versioned kind using the convention `<identifier>@<version>`. Class/type semantic alignment remains a future taxonomy rule; unknown or missing classes are never treated as non-structural by default.

Each relationship kind defines directionality, source role, target role, endpoint types, reflexivity, graph constraints, temporal rules, and any symmetry or transitivity semantics.

## 10. Initial relationship classes

- **structural** — formal organization structure in an explicit structural scheme;
- **operational** — temporary operational subordination or control without rewriting structural identity;
- **administrative** — administrative affiliation or management without automatic operational command;
- **support** — explicit support that does not imply command, ownership or structural subordination;
- **coordination** — explicit coordination obligation or channel that does not imply command.

A shared operational area does not automatically create a coordination relation.

## 11. Relationship lifecycle

Allowed paths:

```text
Draft
Draft → Established
Draft → Established → Closed
Draft → Established → Revoked
Draft → Cancelled
```

Transition history is authoritative. `Closed` means normal completion, `Revoked` early withdrawal and `Cancelled` that a Draft relation was never established. No `Active` stage is defined.

## 12. Derivation rules

### 12.1 organization_established_at

```text
organization_established_at(o, t) :=
    established_at(o) is defined
    AND established_at(o) <= t
    AND (retired_at(o) is absent OR t < retired_at(o))
```

### 12.2 organization_relationship_effective_at

```text
organization_relationship_effective_at(r, t) :=
    established_at(r) is defined
    AND established_at(r) <= t
    AND validity_start(r) <= t
    AND (validity_end(r) is absent OR t < validity_end(r))
    AND (terminal_at(r) is absent OR t < terminal_at(r))
```

Both derivations use projections from authoritative transition history and never trust independently stored materialized values.

### 12.3 structural graph validation

Dataset-level validation evaluates structural invariants over every interval in which the effective graph can remain constant.

The finite breakpoint set contains all structural-record timestamps that may change effectivity: establishment, `validity_start`, `validity_end`, and terminal timestamps. The graph is checked at each breakpoint and at one deterministic point strictly inside every adjacent open interval. A single caller-supplied `reference_time` may be used only for a targeted diagnostic fixture and does not replace the complete sweep.

## 13. Business Rules

1. Renaming, relocation, commander change or relation change does not by itself create a new Organization.
2. A universal `parent_id` is not an authoritative representation of organization structure.
3. Structural, operational, administrative, support and coordination relations are independently governed.
4. One relationship kind does not create another unless a specific derivation defines it.
5. Organizations from different structural verticals may coordinate or support each other without changing either vertical.
6. Structural parentage and acyclicity are evaluated within an explicit `scheme_ref`.
7. Replacement creates a new record and may use `supersedes_relationship_ref`; history is not overwritten.

## 14. Semantic Rules

1. `OrganizationRelationshipRecord` is a local OCP-007 structure, not a fundamental Concept.
2. Structural subordination does not imply operational subordination.
3. Operational subordination does not rewrite structural identity.
4. Coordination does not imply command.
5. Support does not imply ownership or control.
6. Coordination is not transitive by default.
7. A coordination cycle is not inherently invalid.
8. Structural cycles are invalid within one structural scheme.
9. Multiple effective direct structural superiors are invalid within one scheme unless an explicit exception rule exists.
10. Missing or unknown `relationship_class` is invalid; it cannot bypass class-specific governance.

## 15. Verifiable invariants — Organization

1. `organization_id` is present and non-empty.
2. `classification_refs` contains at least one non-empty reference for Established or Retired lineage.
3. `transition_history` matches one allowed linear lifecycle path.
4. Every transition record refers to the same `organization_id`.
5. Transition timestamps are non-decreasing.
6. Optional `lifecycle_stage` equals the lifecycle projection.
7. Optional `established_at` equals the establishment projection.
8. Optional `retired_at` equals the retirement projection.
9. Optional `establishment_provenance_ref` equals establishment provenance.
10. `created_at` is not later than the first transition timestamp.
11. The record contains no authoritative universal hierarchy field from the governed machine-readable vocabulary.

## 16. Verifiable invariants — OrganizationRelationshipRecord

1. `relationship_id` is present and non-empty.
2. `relationship_class` is present and belongs to the governed initial class vocabulary for Established, Closed or Revoked lineage.
3. `relationship_type_ref` is present and versioned for Established, Closed or Revoked lineage.
4. Source and target Organization references are present for Established lineage.
5. Source and target differ for the initial relationship classes.
6. `transition_history` matches one allowed linear lifecycle path.
7. Every transition record refers to the same `relationship_id`.
8. Transition timestamps are non-decreasing.
9. Optional materialized lifecycle fields equal authoritative projections.
10. `validity_start` is present for Established lineage.
11. If `validity_end` is present, `validity_start < validity_end`.
12. `created_at` is not later than the first transition timestamp.
13. `supersedes_relationship_ref`, if present, differs from `relationship_id`.
14. Structural records contain a non-empty `scheme_ref`.
15. No effective structural cycle exists within one `scheme_ref` at any time.
16. No Organization has more than one effective direct structural superior in one `scheme_ref` at any time unless an explicit exception rule exists.

Invariants 15 and 16 are graph-level and require complete breakpoint-sweep validation.

## 17. P-001 conformance

OCP-007 invokes `P-001@0.1.0`.

### OrganizationTransitionRecord

- stable identity: `transition_id`;
- semantic owner: OCP-007 §§6–7;
- governed kind: `from_stage → to_stage` under the Organization lifecycle;
- provenance: `provenance_ref`;
- validation: invariants 15.3–15.10;
- authority: `transition_history` is authoritative;
- selected modules: Module B — transition history and projections.

### OrganizationRelationshipRecord

- stable identity: `relationship_id`;
- semantic owner: OCP-007 §§8–16;
- endpoint contract: `source_organization_ref`, `target_organization_ref`;
- governed kind: `relationship_type_ref` plus governed `relationship_class`;
- provenance: establishment transition provenance;
- validation: invariants 16.1–16.16;
- authority: transition history and versioned relationship kind;
- selected modules: A — temporal effectivity; B — transition history and projections; C — supersession.

P-001 supplies record form only. All organizational semantics remain defined here.

## 18. Examples

- `ORG-BN-02 structurally_subordinate_to ORG-BDE-01` in `STRUCTURE-2026-A`.
- Simultaneous structural and operational records are valid because they carry different semantics.
- Horizontal coordination between EW and UAS organizations does not alter either structural vertical.
- `organization.parent_id = ORG-BDE-01` is invalid as an authoritative universal-hierarchy model.
- A record with `relationship_class: strutural` is invalid and cannot disappear from structural graph checks.

## 19. Explicitly Not Defined

OCP-007 does not define a complete organization type taxonomy, identity continuity through merger or split, commander or personnel assignment, staff structure, Resource ownership, Organization-to-Organizational-Resource mapping, operational-control taxonomy, authority or delegation, Coordination as a future Concept, Capability, Readiness, State, classification-specific hierarchy exceptions, or implementation database/API/UI contracts.

## 20. Open questions

- AB-044 — Organizational identity continuity.
- AB-045 — Organization relationship type taxonomy.
- AB-046 — Organization lifecycle review.
- AB-047 — Organization composition and organizational units.
- AB-048 — One Concept — One Responsibility.
- AB-049 — Consolidate OCP Architectural Doctrine.
- AB-050 — Require Explicitly Not Defined section.
- AB-051 — Structural schemes and multiple structural verticals.
- AB-052 — Organization-to-Organizational-Resource mapping.

## 21. Review target

External review should attempt to falsify the Organization/Resource boundary, P-001 conformance, governed class selection, complete temporal graph validation, scheme-scoped hierarchy, and identity independence from current relations.
