---
Document-ID: OCP-007
Title: Organization Concept
Version: 1.1.1
Status: Canonical
Concept-Status: Canonical
Defines-Concepts: Organization
Concept-Depends-On: []
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, AD-001, P-001
Uses-Patterns: P-001@0.1.0
Used-By: Organization Model, Coordination Model, Operational Ontology
Last-Review: 2026-08-09
---

# OCP-007 — Organization Concept

## 1. Purpose

This document defines the fundamental Concept `Organization` and one local identified-record contract for relations between Organizations.

It deliberately presents two readable surfaces under one owner:

1. Organization identity and record lifecycle; and
2. `OrganizationRelationshipRecord`, including kind binding, effectivity, structural validation and supersession history.

Organization answers:

> Which represented organizational entity does this exact identifier denote in this resolution scope?

It does not answer whether that entity is currently active, capable, ready, available, authorized, assigned, participating, interchangeable with another entity, or identical to a Resource.

## 2. Decision basis and exact remediation baseline

AD-019 `0.2.0 / Accepted` selects Q2 for this bounded remediation:

```text
Q2 := H2 + C2 + K3 + T2 + S1 + E1 + Y1 + R1 + U0 + M0
```

Q2 means one OCP-007 owner with two explicit surfaces; stable exact references without automatic merger/split continuity; optional opaque classifications; exact externally owned relationship kinds bound to coarse Core classes; dataset-local structural partitions; unconditional multiple-superior rejection; finite record lifecycle; history-only branching supersession; and no composition or Organization/Resource mapping.

The remediation starts from `main@d32f679e5c74d2cd5d8777cf89dedae02d151a96`, tree `11e2f5ca864e4319d5d282d6e9a9393c3ba84607`. Exact baseline SHA-256 anchors are:

| Surface | SHA-256 |
|---|---|
| AD-019 | `51319816b9613b2ac2ced22559c739b96ad2b5e685d45ecba904b067cea0ad3c` |
| OCP-007 `0.3.2` | `93fdf3e2e71e844888306b22da4f46468418ed30f3a2a62b8a39a98e7c6b387b` |
| P-001 | `cf6fb3501a1a5504aa873c372e97436813725c6e44a7fc682a2db404a7d97b82` |
| OCP-016 | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| Canonical OCP-003 | `f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315` |
| OCP-009 / OCP-012 / OCP-013 | `29362c815cb14f07bfd06775d1398498a27ace5ee5a4acaafde0eb39e902152a` / `d4d5b4441cf2d1f7fea2dae572fcfa60f22b0ebce0e23ae6a86f71d9f4edd122` / `a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74` |
| OCP-014 / OCP-015 | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` / `6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d` |
| Organization checker / rules / tests | `7e1890443abe4f92abd2a5e823ebbc9aa61b34a6471e76e5f176dc49068a0276` / `f33a4dadfe9d98e34698c4c99548a0d15980c35129d74729414ec3b9ae3b90d7` / `ebae2d9675cb67ba558f4ad747a1ceba4e3d03f9eb47f1a143115ada3bb7d17e` |
| primary / graph Organization fixture manifests | `01fff80b7c2f9c1c94a7c830834d49968afb8886c2dba1e4779ec2032da6c44c` / `861ac4bb3e115bd85e1130692ca98d60d071ce46cc7272acbf4857f920e7fd9d` |
| complete 119-fixture manifest | `737d961afffd0e64981021b186861d690b49218dd8a155a5acdef0389e7efd67` |

The baseline sweep has zero normative OCP consumer declaring `Depends-On: OCP-007`, zero Organization Concept graph edges, and exactly five AD records declaring that dependency: AD-005, AD-011, AD-014, AD-018 and AD-019. Those are provenance, discovery or decision consumers; none transfers Organization semantics out of OCP-007.

## 3. Canonical definition

**Organization** is an identified organizational entity represented independently of any particular Operation, Assignment, temporary relation, Resource identity or current descriptive label.

Exact-ID continuity is a useful Core guarantee: an unchanged exact historical reference keeps denoting the same represented Organization record. That guarantee does not decide whether a real-world institution remains the same through merger, split, reorganization or constitutive redesignation.

## 4. Shared Core Boundary

OCP-007 owns Organization identity, its record-recognition lifecycle, the local relationship-record contract, five coarse relationship behavior classes and the shared validation envelope described here.

It does not own a complete organization taxonomy, specialized relationship-kind meaning, real-world institutional continuity, command or delegation authority, composition, Organizational Resource identity, Organization-to-Resource mapping, Capability claims, Readiness or interchangeability.

`Organization ≠ Resource`. A future explicit mapping may relate them without collapsing either identity. OCP-012 continues to permit only exact Resource holders for `CapabilityClaimRecord`; this document does not introduce Organization claims.

# Part I — Organization identity and lifecycle

## 5. Organization record

```text
Organization
- organization_id
- classification_refs [optional opaque annotations]
- display_name [optional]
- transition_history
- created_at
- lifecycle_stage [optional materialized projection]
- established_at [optional materialized projection]
- retired_at [optional materialized projection]
- establishment_provenance_ref [optional materialized projection]
```

The record contains no authoritative universal `parent_id`, `children`, embedded relationship collection, `operation_ref`, `assignment_ref` or `constraint_ref`.

## 6. Exact identity and resolution scope

Within one declared validation dataset and resolution scope, each `organization_id` must identify exactly one record. Duplicate IDs make that dataset ambiguous and invalid independent of record order.

An exact reference never redirects to a later, similar, more-supported or more-frequently issued record. Retiring a record does not invalidate its historical exact references. Display name, commander, personnel, location, current relationships and annotations do not create, merge, split or replace identity.

## 7. Material-event continuity is unresolved

Merger, split, reorganization and constitutive redesignation are real-world continuity questions. Core makes no automatic same-ID or new-ID decision for them.

When evidence conflicts or no governed continuity owner exists, the result is unresolved. Same name, shared personnel, newest timestamp, storage order, similar identifier, issuer count, reviewer count or majority cannot select a survivor or branch. AB-044 remains the reopening owner.

## 8. Classification annotations

`classification_refs` is optional and retained for serialization compatibility. When present it is a list of non-empty opaque values.

Core does not resolve these values and derives no identity, lifecycle, hierarchy, role, composition, mapping, Capability, Readiness, authority or interchangeability conclusion from their presence, absence, equality or disagreement. Two Organizations carrying `organization-type://unit@1` remain two distinct Organizations; the annotation creates neither unit identity nor a Resource.

## 9. Organization lifecycle

Allowed paths are:

```text
Draft
Draft → Established
Draft → Established → Retired
Draft → Cancelled
```

`transition_history` is authoritative. Every `OrganizationTransitionRecord` has a unique `transition_id` within the dataset and carries `organization_ref`, `from_stage`, `to_stage`, `occurred_at` and `provenance_ref`.

These stages describe record recognition and historical existence only:

- `Established` says the record was established; it does not mean active, participating, capable, ready, available, admissible or authorized.
- `Retired` preserves identity and history; it is not deletion and does not elect a successor.
- `Cancelled` says a Draft record was not established; it does not make a different ID the winner.

Provenance attributes a transition. Its label alone grants no actor authority, continuity decision or precedence.

## 10. Organization derivation

### 10.1 `organization_established_at`

```text
organization_established_at(o, t) :=
    established_at(o) is defined
    AND established_at(o) <= t
    AND (retired_at(o) is absent OR t < retired_at(o))
```

The derivation uses projections from authoritative history, never an independently stored lifecycle field.

## 11. Organization semantic rules

1. An exact ID is stable even when display data or relations change.
2. Exact record continuity does not decide material-event continuity.
3. Classification is optional annotation, not semantic authority.
4. A universal hierarchy field is not an authoritative Organization property.
5. Lifecycle is about record recognition/existence, not operational state.
6. Historical references remain exact after retirement.
7. No name, time, order, source count or provenance label supplies identity authority.

## 12. Verifiable Organization invariants

1. `organization_id` is present and non-empty.
2. IDs are unique within the declared dataset.
3. If `classification_refs` is present, it is a list containing only non-empty opaque values.
4. `transition_history` matches one allowed linear path.
5. Every transition has all required fields.
6. Every transition refers to the same `organization_id`.
7. Transition IDs are unique within the record and dataset.
8. Transition timestamps are non-decreasing.
9. Optional `lifecycle_stage` equals the history projection.
10. Optional `established_at` equals the history projection.
11. Optional `retired_at` equals the history projection.
12. Optional `establishment_provenance_ref` equals the establishment transition provenance.
13. `created_at` is not later than the first transition.
14. No governed universal hierarchy field is present.

## 13. P-001 invocation — OrganizationTransitionRecord

OCP-007 invokes `P-001@0.1.0`, Module B:

- stable identity: `transition_id`;
- semantic owner: OCP-007 §§9–12;
- governed kind: `from_stage → to_stage` under §9;
- provenance: `provenance_ref`;
- authority: `transition_history`;
- projections and validation: §§10 and 12.

P-001 supplies identified-record form only. It supplies no Organization identity, continuity, classification or authority semantics.

# Part II — local Organization relationship records

## 14. OrganizationRelationshipRecord

AD-001 defines Relationship as a governed modeling pattern, not a universal fundamental Concept. OCP-007 therefore owns this local structure without registering a second Concept:

```text
OrganizationRelationshipRecord
- relationship_id
- relationship_class
- relationship_type_ref
- source_organization_ref
- target_organization_ref
- scheme_ref [required for structural established lineage]
- validity_start
- validity_end [optional]
- transition_history
- created_at
- lifecycle_stage [optional projection]
- established_at [optional projection]
- terminal_at [optional projection]
- establishment_provenance_ref [optional projection]
- supersedes_relationship_ref [optional]
```

The record is directed and identified independently of both endpoint identities.

## 15. Exact externally owned kind profile

Every established, closed or revoked relationship binds `relationship_type_ref` exactly once to an `OrganizationRelationshipKindProfile` supplied in the declared resolver context:

```text
OrganizationRelationshipKindProfile
- kind_ref                 # exact versioned value
- profile_owner_ref        # external/domain semantic owner attribution
- relationship_class       # one compatible coarse OCP-007 class
```

This shared projection contains exactly these three fields; specialized domain payload remains outside Core. OCP-007 owns only this interoperability envelope: exact resolution, one declared owner reference and agreement with one coarse class. The named external/domain owner owns specialized kind meaning, including roles, detailed directionality and domain constraints.

The accepted precedent is OCP-004's exact spatial profile envelope: Core validates the shared shape and binding, while a concrete consumer/domain contract plus external review must accept the named owner's legitimacy. `profile_owner_ref` is attribution, not proof of authentication or authority. A synthetic fixture profile is evidence, never a Core registry or normative owner.

Missing, duplicate, malformed, unknown or class-mismatched resolution rejects. An `@` delimiter, producer label, newest profile, record order, owner count or review count never admits a kind. If a legitimate external/domain owner boundary cannot be stated, remediation returns to H0 rather than inventing a registry.

## 16. Coarse classes and structural partitions

The five coarse OCP-007 classes are mutually non-equivalent shared behavior families, not a complete taxonomy:

- `structural` — formal structure inside one explicit partition;
- `operational` — temporary operational subordination or control without rewriting structural identity;
- `administrative` — administrative affiliation or management without automatic operational command;
- `support` — support without command, ownership or structural subordination;
- `coordination` — explicit coordination obligation or channel without command.

A structural `scheme_ref` is an opaque partition key. The checker compares decoded values by exact equality only inside one declared validation dataset/scope. Equal strings in different scopes establish no shared scheme; different keys authorize no cross-key inference. The key creates no Organization identity, composition, mapping or cross-scheme equivalence.

Within one exact partition, every effective structural cycle rejects and every Organization with more than one effective direct structural superior rejects unconditionally. There is no exception label, waiver field or producer bypass. AB-051 may reopen the partition model; a future multiple-superior exception requires its own legitimate owner, version, effectivity and conflict contract.

## 17. Relationship lifecycle and effectivity

Allowed paths are:

```text
Draft
Draft → Established
Draft → Established → Closed
Draft → Established → Revoked
Draft → Cancelled
```

History is authoritative. `Closed` is normal completion, `Revoked` early withdrawal and `Cancelled` a Draft never established. None selects another record or implies authorization.

### 17.1 `organization_relationship_effective_at`

```text
organization_relationship_effective_at(r, t) :=
    established_at(r) is defined
    AND established_at(r) <= t
    AND validity_start(r) <= t
    AND (validity_end(r) is absent OR t < validity_end(r))
    AND (terminal_at(r) is absent OR t < terminal_at(r))
```

Validity is half-open and each relationship has independent effectivity. Structural validation uses every establishment, validity-start, validity-end and terminal breakpoint plus one deterministic point inside each adjacent open interval. A diagnostic `reference_time` never replaces the complete sweep.

## 18. Supersession is history, not authority

### 18.1 Exact predecessor resolution

`supersedes_relationship_ref` records that a new identified relationship follows one exact predecessor. Its target must resolve exactly once, cannot be self, and the supersession graph must remain acyclic.

### 18.2 Branch visibility and effectivity

One predecessor may have several explicit successors. Branch overlap and gaps are valid; every branch keeps its own lifecycle and effectivity. Supersession never redirects the predecessor, elects a current head or chooses a winner by time, order, provenance, issuer/reviewer count, majority or branch count.

### 18.3 Successor attribution

Successor establishment provenance attributes the replacement decision but does not authorize it or settle branch conflict.

### 18.4 `organization_relationship_successor_ids`

This derivation returns the complete sorted set of exact successor IDs for a predecessor. Sorting makes replay stable; it does not rank or select a head. No current-head derivation exists.

## 19. Verifiable OrganizationRelationshipRecord invariants

1. `relationship_id` is present and non-empty.
2. Relationship IDs are unique within the declared dataset.
3. Established, Closed and Revoked lineage uses one of the five classes.
4. Its `relationship_type_ref` is present and versioned.
5. A matched kind profile has a versioned kind, non-empty owner reference and valid class.
6. The kind resolves exactly once.
7. Its declared profile class equals the record class.
8. Source and target references are present.
9. Each endpoint resolves exactly once in the declared Organization scope.
10. Source and target differ for all five initial classes.
11. History matches one allowed path.
12. Every transition has all required fields.
13. Every transition refers to the same relationship ID.
14. Transition IDs are unique within the record and dataset.
15. Transition timestamps are non-decreasing.
16. Optional `lifecycle_stage` equals the history projection.
17. Optional `established_at` equals the projection.
18. Optional `terminal_at` equals the projection.
19. Optional `establishment_provenance_ref` equals establishment provenance.
20. `validity_start` is present for established lineage.
21. When `validity_end` is present, `validity_start < validity_end`.
22. `created_at` is not later than the first transition.
23. A supersession reference does not target self.
24. Its target resolves exactly once.
25. Supersession is acyclic.
26. Structural established lineage has a non-empty `scheme_ref`.
27. Structural validation has a non-empty declared scope reference.
28. No effective structural cycle exists in one exact partition at any time.
29. No effective multiple direct structural superiors exist in one exact partition at any time.

## 20. P-001 invocation — OrganizationRelationshipRecord

OCP-007 invokes exact `P-001@0.1.0` Modules A, B and C:

- stable identity: `relationship_id`;
- semantic owner: OCP-007 §§14–19;
- endpoints: exact `source_organization_ref` and `target_organization_ref`;
- governed kind: exact external `relationship_type_ref` plus one coarse class under §§15–16;
- Module A: half-open temporal effectivity under §17;
- Module B: authoritative transition history and projections under §17;
- Module C: exact, acyclic, branching history under §18;
- provenance: establishment transition provenance, attribution only;
- validation: §19.

P-001 adds no kind owner, partition identity, exception, command, mapping, redirect or branch winner.

## 21. Shared non-implications

1. Structural subordination does not imply operational subordination, composition, command, Resource ownership or mapping.
2. Operational subordination does not rewrite structural identity.
3. Administrative affiliation does not imply operational control.
4. Support does not imply ownership, Assignment or Capability.
5. Coordination does not imply command and is not transitive by default.
6. A shared operational area does not create a coordination relation.
7. Membership or any relationship creates no Assignment, participation or Capability claim.
8. Equal labels or relations create no Resource interchangeability result; OCP-013 remains Resource-specific and directional.
9. Organization names, callers and provenance labels create no Coordination authority under OCP-014/OCP-015.
10. `Capability ≠ Readiness`; exact OCP-009 version binding remains unchanged.

## 22. Deferred and excluded surface

This version explicitly does not define:

- institutional continuity through merger, split, reorganization or constitutive redesignation — AB-044;
- a complete relationship-kind taxonomy — AB-045;
- broader lifecycle compatibility — AB-046;
- composition, organizational units, crews or temporary group identity — AB-047;
- a governed cross-scope structural scheme — AB-051;
- Organization/Organizational-Resource mapping — AB-006 and AB-052;
- commander/personnel Assignment, authority/delegation, State, Readiness or implementation API/database/UI contracts.

These are visible exclusions, not claims that the questions are unimportant. U0 and M0 forbid this remediation from resolving them implicitly.

## 23. Declared dataset and resolver context

A validation dataset contains:

```text
validation_scope_ref
organizations[]
relationships[]
relationship_kind_profiles[]
```

`validation_scope_ref` names only the bounded context in which exact Organization references and structural partition keys are compared. It is not a scheme registry or authority token. Exact resolution means set cardinality equals one; zero and multiple matches both fail. Records outside the declared dataset make no automatic claim about this dataset, and no validation order changes the result.

## 24. Compatibility and migration

This `0.3.2 → 0.4.0` Draft change preserves every current Organization and relationship ID, transition ID, history and exact reference.

- `classification_refs` values stay byte-replayable but become optional opaque annotations; no field deletion is required.
- Current class values retain their coarse meanings.
- Current kind values must resolve through an exact profile context. Both primary relationship fixtures gain exact endpoint context; the valid structural fixture also gains a synthetic kind profile and validation scope. Their record entities are otherwise preserved. This is evidence-envelope migration, not creation of normative kind owners.
- Current `scheme_ref` values are preserved and narrowed to dataset-local exact partition equality.
- The three graph regression fixtures remain records of the same invalid graph conditions.
- No transition, mapping, composition relation, Capability claim or branch winner is synthesized.

Consumers that previously relied only on an `@` delimiter or non-empty endpoints must provide the exact resolver context or receive an explicit failure. That is intentional fail-safe incompatibility within a Draft contract.

## 25. Human scenario disposition

All twenty-five scenarios in AD-019 §37 are incorporated by exact reference and remain binding review evidence for this remediation:

- scenarios 1–8 are implemented by §§6–9 (stable exact IDs, unresolved material-event continuity and opaque optional classification);
- scenarios 9–17 are implemented by §§15–19 and §23 (class agreement, exact kind/endpoint resolution, partition-local graph checks and duplicate rejection);
- scenarios 18–20 are implemented by §§17–18 (visible independent successor branches, provenance as attribution and persistent historical references); and
- scenarios 21–25 are implemented by §§4, 8, 21 and 22 (no unit/composition/mapping, Organization Capability holder, interchangeability or Coordination-authority inference).

The exact expected result of each numbered scenario remains the corresponding AD-019 §37 row. This section neither abbreviates nor overrides those results.

## 26. Executable evidence matrix

The synthetic Q2 contract fixture is finite and manifest-complete for the seventeen AD-019 §36.14 mechanical groups:

| Group | Executable witness |
|---:|---|
| 1 | absent classification is valid; malformed optional annotations reject |
| 2 | equal opaque classifications do not merge distinct IDs |
| 3 | duplicate Organization IDs reject independent of order |
| 4 | duplicate Organization and relationship transition IDs reject |
| 5 | Retired/Cancelled/Closed/Revoked paths and projection mismatches replay |
| 6 | missing and duplicate kind-profile resolution reject |
| 7 | kind/class mismatch rejects |
| 8 | missing, unresolved and ambiguous endpoints reject |
| 9 | duplicate relationship IDs reject |
| 10 | structural scope is required; exact partition equality stays dataset-local |
| 11 | transient and all-time structural cycles reject under the full sweep |
| 12 | multiple direct structural superiors reject unconditionally |
| 13 | unresolved and ambiguous supersession targets reject |
| 14 | supersession cycles reject |
| 15 | overlapping successor branches remain valid and visible |
| 16 | gapped branches retain independent effectivity |
| 17 | record reordering preserves the complete successor set and creates no head |

The checker proves only mechanically expressible shape, exact resolution, history, projection, effectivity and graph results. It does not prove a profile owner's real-world legitimacy or decide institutional continuity.

## 27. Counterexample disposition

All twenty-eight counterexamples in AD-019 §38 remain rejected by exact reference. §§6–8 reject identity, classification, newest/count and continuity shortcuts; §§15–20 reject syntax-only kinds, hidden owner selection, cross-scope inference, exception labels, endpoint-presence shortcuts and supersession heads; §§21–22 reject composition, mapping, Capability, Readiness, authority and interchangeability implications; §§2, 29 and 31 reject approval/CI/authorization transfer.

The exact numbered AD-019 §38 statement controls if this summary is ever ambiguous.

## 28. Relocation ledger from OCP-007 0.3.2

| Former surface | Current disposition |
|---|---|
| §§1–4 Purpose, definition, boundary, identity | §§1, 3–7; C2 material-event limit made explicit |
| §5 Organization structure | §5; classification made optional and universal hierarchy exclusion retained |
| §§6–7 Organization lifecycle/transition | §§9–13; Y1 meanings, duplicate IDs and P-001 Module B completed |
| §8 relationship modeling decision | §14; retained as local record, no new Concept |
| §9 relationship structure | §§14–15, 17–19; delimiter/presence checks replaced by T2/exact resolution/R1 |
| §10 initial classes | §16; coarse behavior retained without claiming complete taxonomy |
| §11 relationship lifecycle | §17; Y1 terminal and historical behavior completed |
| §12 derivations/graph sweep | §§10, 17 and 19; full breakpoint rule retained |
| §§13–14 business/semantic rules | §§11, 16, 18 and 21; ownerless multiple-superior exception removed |
| §§15–16 invariants | §§12 and 19; K3/T2/S1/E1/Y1/R1 completed |
| §17 P-001 | §§13 and 20; Module B and A/B/C slots preserved and completed locally |
| §18 examples | §§24–26; current examples retained as fixture/scenario evidence |
| §§19–20 excluded/open | §22; U0/M0 and backlog owners made visible |
| §21 review target | §32; remains falsification evidence only |

The former Organization field ledger relocates line by line:

| Field | Current location and treatment |
|---|---|
| `organization_id` | §§5–6, 12.1–12.2; exact dataset identity and duplicate rejection |
| `classification_refs` | §§5, 8 and 12.3; compatible optional opaque annotation |
| `display_name` | §§5–7; optional designation with no identity or continuity authority |
| `transition_history` | §§5, 9–13; authoritative Y1/P-001 Module B history |
| `created_at` | §§5 and 12.13; creation time, never priority authority |
| `lifecycle_stage` | §§5, 9 and 12.9; optional exact history projection |
| `established_at` | §§5, 9–10 and 12.10; optional exact history projection |
| `retired_at` | §§5, 9–10 and 12.11; optional exact history projection |
| `establishment_provenance_ref` | §§5, 9 and 12.12; optional attribution projection only |

The former relationship field ledger relocates line by line:

| Field | Current location and treatment |
|---|---|
| `relationship_id` | §§14 and 19.1–19.2; exact dataset record identity |
| `relationship_class` | §§14–16 and 19.3; one coarse shared behavior family |
| `relationship_type_ref` | §§14–15 and 19.4–19.7; exact external profile binding and class agreement |
| `source_organization_ref` | §§14 and 19.8–19.10; directed exact endpoint |
| `target_organization_ref` | §§14 and 19.8–19.10; directed exact endpoint |
| `scheme_ref` | §§14, 16, 19.26–19.29 and 23; opaque dataset-local partition key |
| `validity_start` | §§14, 17 and 19.20–19.21; branch-local half-open effectivity |
| `validity_end` | §§14, 17 and 19.21; optional branch-local half-open end |
| `transition_history` | §§14, 17, 19.11–19.19 and 20; authoritative Y1/P-001 Module B history |
| `created_at` | §§14 and 19.22; creation time, never branch/head priority |
| `lifecycle_stage` | §§14, 17 and 19.16; optional exact history projection |
| `established_at` | §§14, 17 and 19.17; optional exact history projection |
| `terminal_at` | §§14, 17 and 19.18; optional exact history projection |
| `establishment_provenance_ref` | §§14, 17–18 and 19.19; optional attribution projection only |
| `supersedes_relationship_ref` | §§14, 18 and 19.23–19.25; exact acyclic branching history, no head |

The former transition-field ledger relocates line by line:

| Field | Current location and treatment |
|---|---|
| `transition_id` | §§9, 12.7, 17 and 19.14; exact dataset identity and duplicate rejection |
| `organization_ref` | §§9, 12.6 and 13; exact same-Organization reference |
| `relationship_ref` | §§17, 19.13 and 20; exact same-relationship reference |
| `from_stage` | §§9, 13, 17 and 20; one allowed Y1 path source |
| `to_stage` | §§9, 13, 17 and 20; one allowed Y1 path target |
| `occurred_at` | §§9, 12.8, 17 and 19.15; non-decreasing time, never winner authority |
| `provenance_ref` | §§9, 13, 17–18 and 20; required attribution, never authorization |

No field silently changes owner.

## 29. Repository evidence and authority limits

The reference implementation is limited to the Organization checker module, Organization rule manifest, dedicated tests, Organization fixture trees and minimal routing/import glue. Human checker documentation and mechanical count/accounting projections may also change.

OCP-003, OCP-009, OCP-012–OCP-015, P-001, registries, taxonomy, foundation map, schemas, every Concept status and all non-Organization checker semantics remain byte-unchanged. Rule-manifest completeness is exact set equality and fails closed.

The fixture profile owner names are synthetic non-sensitive test attribution. Neither the checker, the fixture nor a green CI run authenticates those owners or authorizes production use.

## 30. Rollback and stop conditions

Rollback reverts OCP-007, Organization checker/rules/tests/documentation, Organization fixtures and mechanical counts as one unit. It does not delete records, merge identities, rebind references, restore an ownerless exception, invent classifications/transitions or elect a newest successor.

Remediation stops at H0 and requires a fresh Board comparison if review finds a missing normative consumer or graph edge; a current dependency on material-event continuity, classification meaning, cross-scope scheme identity or a multiple-superior exception; no legitimate external/domain kind owner boundary; a need for a registry, new Concept, Pattern, mapping, Organization Capability holder, joint Resource edit or head election; duplicate semantic owners; unreadable prose dependent on checker code; or non-replayable migration.

No apparently small diff waives a stop.

## 31. Status and next gate

This document remains `0.4.0 / Draft`; Organization remains `Accepted`; `Concept-Depends-On: []` and every current dependency remain unchanged. AB-006, AB-044–AB-047, AB-051 and AB-052 remain Open; AB-062 remains Planned.

Completion or failure of this remediation triggers a fresh exact blocker/stability/consumer/Pattern/route/migration audit and a separate Board act before any OCP-007 `1.0.0`, Organization lifecycle transition or T5 proposal. Review, CI and merge authorization for AD-019A do not transfer to this proposal or any later act.

## 32. Review target

External review should try to falsify the two-surface readability, exact C2 identity limit, K3 opacity, T2 one-owner envelope, S1 scope locality, unconditional E1 rejection, Y1 record-only lifecycle, R1 branching history, P-001 completeness, U0/M0 exclusions, finite evidence matrix, data replay and absence of any registry, graph edge, mapping, Organization Capability holder, head election or authority-by-time/order/count.

## 33. O9C lifecycle bridge and canonicalization act

OCP-007 and Organization are now `1.0.0 / Canonical` under the separately reviewed O9C lifecycle act selected by AD-016T. Sections 1–32 remain byte-identical to the bounded Q2 contract reviewed at `0.4.0 / Draft`.

Section 31 is a preserved historical act record. Its statement that this document remained `0.4.0 / Draft` and Organization remained `Accepted` describes the pre-O9C state in which Q2 remediation was reviewed; it does not override the current frontmatter or this §33. Its second paragraph's fresh-audit and separate-Board gates were satisfied by AD-016S, AD-016T and this separately gated lifecycle act.

### 33.1 Exact baseline and atomic unit

The exact proposal baseline is `main@66a81b26115e404ad5bb6443ae6df60033cb28a5`, tree `495d12661eb10b3518bde482ee3b1fd185d81128`.

| Input / atomic member | Baseline object | SHA-256 |
|---|---|---|
| AD-016T selection | blob `124e1535db06dcfa60b579dd49ecea5292d0c687` | `32b91265723ec2a8a2408a9078537e5f3bf33fc0c81bd7ad06eaffcbb4c6f3e7` |
| OCP-007 / Organization | blob `dceb5d57c66d180cd5298f4e3ad48d02831a4f23` | `55834d6da1b1b984140020e0e4613ea578b6c83e721d1b81688c12ffa8375a3f` |
| OCP-000 registry | blob `547ccae7f417cf3d0bff92db20e0ccb9933cc8c5` | `a088d0b9c73035270480ddc266abbd3b5f847625053fef7744468eb667753332` |
| OCP-002 projection | blob `3b676afcff63ac4b600fb382a67283d67f766c7f` | `e0112f751b7922904d7217c76102cc8d5e3382ce49f13d94e99c31af1275669e` |
| OCP-005 guarded peer view | blob `3223ba69e289c38530d93965c2faa8cf280c1239` | `da599b71ea8fb26cde3f57921a6bee07a8ddf75aaad0f6e9e2387ee499bda11b` |
| generated foundation map | blob `38011129ab9bf2e0362df2255a57fa15d3c90e54` | `f8af51e97e193820d24323cd0db5262d4fe0d353cb93c9bec910834e3e7b70e8` |
| checker guide | blob `74c4195c182d076e62a3ef1d8b8897db83cc177d` | `5ff2c58dcb3a9b0daee7458329e0b9eaef6ff4fa2864c5045c82c133827140b5` |
| repository README | blob `a3e005f0cacce5b742c18842d9220a8d23f144b9` | `499d13693bfa3b7f0ee7406432df621d3b88fc1f6c9a7049613a6a6e232be33f` |
| foundation roadmap | blob `ca0be71419dd0d50b4e4d18415be3531d7cfeb25` | `8d124d8410c28ec693246f9ba0f47a9b706cdc226f12a7240d8b2542f8f550fa` |
| architecture backlog | blob `6d73ff60344cdc19fc28ddbf45f8fa4b64d6e99d` | `60cba188912e6ea2c465423340c0c926ea014ec7f39bbbfa53a542eccd240bd2` |

The atomic lifecycle unit changes exactly nine files: OCP-007, OCP-000, OCP-002, OCP-005, the generated foundation map, checker guide, repository README, roadmap and architecture backlog. AD-016T is read-only selection evidence, not a tenth changed file.

### 33.2 Preserved compatibility promise

Canonical status stabilizes the Q2 surface; it does not expand it. In particular:

- Organization identity remains exact and distinct from Resource identity;
- merger, split, reorganization and constitutive redesignation continuity remain external decisions;
- `classification_refs` remain optional opaque annotations without taxonomy authority;
- OrganizationRelationshipRecord remains a local identified record under exact P-001 invocation, not a new fundamental Concept;
- Core owns only the exact external kind-profile envelope and shared behavior-class agreement, not specialized kind meaning;
- structural partition equality remains dataset-, scope- and `scheme_ref`-local;
- multiple direct structural superiors remain unconditionally rejected inside one exact partition;
- branching supersession preserves history without redirect, current-head election or authority by time/order/count; and
- composition, Organization/Resource mapping and Organization Capability holders remain excluded and separately governed.

Organization Canonical status does not imply activity, readiness, availability, authorization, admissibility, Assignment, participation, suitability, interchangeability or operational command. CapabilityClaimRecord holders remain Resource-only and exact-bind one explicit OCP-009 Capability version under OCP-012.

### 33.3 Evidence, migration, rollback and authority

The proposed tree passes the complete unit-test and fixture suite, peer-view synchronization, registry/taxonomy/defining-document equality, L2 dependency floors, artifact governance, process audit, Concept graph and generated-map drift. Those checks witness finite consistency only; they do not grant lifecycle status or real-world authority.

No Organization, relationship, transition or profile record changes shape or identity. No exact reference, history, resolver context or consumer requires migration or rebinding. Record-stage fixture values such as `Draft`, `Established`, `Cancelled`, `Closed` and `Revoked` remain Q2 record-lifecycle evidence and are not Concept-status projections.

Corrective rollback is a new reviewed nine-file lifecycle act derived from its then-current baseline. It cannot delete records, redirect exact references, rewrite history, elect a relationship head, infer mapping or restore stale peer values.

This lifecycle becomes authoritative only after Fable exact-head review, Codex adjudication, green required CI, fresh explicit Pavlo/Architecture Board authorization for the same unchanged head and squash merge. AD-016T authorization is consumed and does not transfer. This act does not resolve AB-006, AB-044–AB-047, AB-051 or AB-052, authorize T5, select the next T4 candidate or create production authority.

## 34. Post-canonical versioning correction act

OCP-007 `1.1.0 / Canonical` closes one governance gap left by the `1.0.0` lifecycle act: the stable Organization surface had no document-local rules for classifying later `1.x` changes as PATCH, MINOR or MAJOR. The generic OCP-001 ladder remains binding, but it cannot by itself name which OCP-007 guarantees a proposal preserves, extends or breaks.

Section 33 remains the preserved O9C lifecycle-act record. Its statement that OCP-007 and Organization were then `1.0.0 / Canonical` records the first Canonical transition; it does not override the current frontmatter or this §34.

This correction adds that local rule without changing Organization semantics. Section 33.2 remains the exact compatibility promise; §§1–33 retain their existing meaning; Organization remains `Canonical`; and every identity, record, field, invariant, exclusion, dependency, Pattern invocation and non-implication remains unchanged.

### 34.1 Exact baseline and bounded unit

The exact proposal baseline is `main@6c33b7c111296966616184368e81c0a67f5e9278`, tree `822aac10b3d8440bfb290547402edb4faffc841c`.

| Input / atomic member | Baseline object | SHA-256 | Treatment |
|---|---|---|---|
| OCP-007 / Organization | blob `d3258a4d7b4776bfdf25c5b62b0fcfca34e4bb78` | `6706f94a497502651ac9204e6c0510af5bc550781857efecb050e4de0f882bce` | version and this additive §34 |
| OCP-001 governance | blob `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` | read-only generic SemVer authority |
| OCP-003 Resource precedent | blob `71485bb337cfd59def2e0f1b18b474a7959bd30c` | `f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315` | read-only Concept-local precedent |
| OCP-008 Objective precedent | blob `24ed01e0f5d6bc8f349a7aedae4c5f100eb449ee` | `46f1ecb7b956b106f9c66da0626ec4266961e07492059e594110f63736be6f0d` | read-only Concept-local precedent |
| OCP-016 Core Boundary precedent | blob `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` | read-only Canonical contract precedent |
| checker guide | blob `a3a4ec3bc6d1e052138d4b10e1a6e7f997b3bc18` | `90665b646844a18fc3c4007519c9bb7cad7e6fdd38de6e0d2d896c2048fc2469` | current OCP-007 version label only |
| repository README | blob `78219ff6d921f6edfd93553c7be0d4833d509336` | `f8aea9918b598c9a763e98200d922c4c6fa600b655aed481f47abf71e33ff2fd` | current act accounting only |
| foundation roadmap | blob `562c98924879c4c0c0ae4078a6868884088a47ca` | `a0877f21ac6f04bf266338cce4f113f9878ea575dbdd4a54acc71d069388478e` | current version and sequencing accounting |
| architecture backlog | blob `b24c168070b4ab8466ff344ca82602bb41d1efff` | `eb6016d819c936a6f731d75b940803acbd1ef0463c8c736ddf3109874f704920` | AB-062 accounting only; status unchanged |

The atomic correction changes exactly five files: OCP-007, the checker guide, repository README, roadmap and architecture backlog. OCP-001, OCP-003, OCP-008 and OCP-016 are exact read-only classification evidence, not hidden members of the changed unit. Closed PR #122 is non-authoritative comparison material and supplies neither text nor approval to this act.

### 34.2 Revision class and versioning after `1.0.0`

This is a **MINOR** revision, `1.0.0 → 1.1.0`. It adds a backward-compatible normative rule for future OCP-007 revisions. Calling it PATCH would understate a new obligation; calling it MAJOR would falsely imply a break in the §33.2 promise, stored records or consumer interpretation. The [OCP-001 **Canonical документи** SemVer ladder](../001-ontology-governance/README.md#canonical-документи) is the determining authority because it classifies compatible additions of rules as MINOR. OCP-003 `0.6.1 → 0.7.0` is the only version-class precedent; OCP-008 and OCP-016 instead added their local ladders inside their canonicalization acts, so this is the first separate post-canonical correction of this class.

SemVer applies to every guarantee, exclusion and non-implication in §33.2:

- **PATCH** may correct prose, links, examples, review evidence or current accounting without changing an identity, required or optional field, invariant, owner, authority boundary, exact resolution rule, lifecycle path, Pattern binding, kind-profile envelope, structural-partition rule, supersession behavior, exclusion or non-implication.
- **MINOR** may add a backward-compatible optional clarification or extension only when every existing valid Organization, transition record, relationship record, exact profile/reference and consumer binding keeps the same interpretation; all §33.2 guarantees remain true; and no excluded authority is imported.
- **MAJOR** is required to change an identity key or required structure; permit redirect or automatic material-event continuity; reinterpret `classification_refs`; weaken exact resolution, authoritative history or fail-safe ambiguity handling; move specialized kind or scheme authority into Core; allow a previously rejected multiple-superior result; elect a relationship head; weaken an exact P-001 or OCP-009 binding; introduce Organization/Resource mapping or Organization Capability holders by implication; or remove a §33.2 exclusion or non-implication.

A continuity, taxonomy, lifecycle, composition, scheme, exception, mapping or holder proposal is not automatically MINOR merely because it is additive in storage. It first requires its exact reopening owner and OCP-001/OCP-016 route; the effect on the existing `1.x` promise then determines the version.

Adding or changing a specialized relationship-kind profile under its exact external owner does not automatically version OCP-007. It does require an OCP-007 revision if the shared Core envelope, class agreement, exact resolution, graph behavior or an existing consumer interpretation changes.

OCP-007 document version is not an Organization, transition-record, relationship-record, profile or stored-payload version. It does not rewrite an identifier, select a current record or create a common version clock for domain data.

### 34.3 Evidence, migration, rollback and authorization

The proposed tree must pass the complete repository tests, fixtures, status synchronization, artifact governance, process audit, Concept graph and generated-map drift checks in both repository contexts. External review must additionally verify the five-file footprint, all §34.1 anchors, the `1.1.0` MINOR rationale, byte stability of the existing OCP-007 contract apart from frontmatter and additive §34, and absence of any stale current OCP-007 version label. Green CI cannot classify SemVer or grant authority.

No Organization, transition, relationship, profile, resolver, fixture, schema, checker rule, dependency, Concept projection or graph edge changes. No stored record, exact reference or consumer binding requires migration or rebinding. Organization remains Canonical, readiness accounting does not increase, all named Organization backlog questions retain their status and T5 stays closed.

Corrective rollback or replacement is a new reviewed act derived from its then-current baseline. It cannot silently downgrade the document, delete §34 as history cleanup, rewrite records, redirect exact references, infer continuity or mapping, elect a relationship head, expand CapabilityClaimRecord holders or select authority by timestamp, order, count, majority, reviewer, CI or completed effort.

This correction becomes authoritative only after exact-head Fable review, Codex adjudication, green required CI, fresh explicit Pavlo/Architecture Board authorization for the unchanged head and squash merge. Pavlo's instruction to prepare this separate item authorizes authoring and review only. It does not authorize merge, remaining-T4 reassessment, another lifecycle act, T5, backlog resolution or any semantic extension.
