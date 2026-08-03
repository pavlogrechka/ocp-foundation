---
Artifact-Class: DerivedProjection
Artifact-ID: BASELINE-M1
Title: Foundation Milestone M1 Baseline
Version: 0.2.1
Status: Draft
Authority: Architecture Board
Derived-From: OCP-000, OCP-003, OCP-004, OCP-005, OCP-006, OCP-007
Future-Intent-Source: architecture/baselines/foundation-future-edges.yaml
---

# Foundation Milestone M1 Baseline

## 1. Purpose

Record the first Foundation baseline without creating a second source of truth.

This artifact is a derived projection. Current Concept nodes, statuses and dependency edges are generated from authoritative registries and defining-document metadata. Hand editing generated current-state sections is prohibited.

## 2. M1 scope

Accepted Concepts at this baseline:

- Resource — OCP-003;
- Operation — OCP-004;
- Assignment — OCP-005;
- Constraint — OCP-006;
- Organization — OCP-007.

`Accepted` does not mean `Canonical`. Canonical promotion remains a separate Architecture Board process.

## 3. Projection model

### Current graph

The target authority is:

- Concept registry and statuses in OCP-000;
- `Defines-Concepts` and `Concept-Depends-On` in defining OCP documents.

During PR-0008 implementation, `concept-dependencies.yaml` is a migration staging record used to exercise graph validation before the same edges are moved into defining-document frontmatter. The migration is governed by AB-053. The checker rejects simultaneous staging and frontmatter dependency sources, and the staging record must be removed before this baseline leaves Draft.

The generator rejects:

- a dependency on an unregistered Concept;
- a dependency on a Concept without a defining artifact when the edge is normative;
- a cycle in the current Concept dependency graph;
- a generated node not present in OCP-000;
- a defining Concept left in `Under Review` when validation runs in `main` context;
- simultaneous staging and frontmatter dependency sources.

`Under Review` is valid in PR context under the accepted status choreography. It is invalid only in a merged `main` baseline.

### Future graph

Future edges are curated intent records in `foundation-future-edges.yaml`. They must identify a registered Concept or an Architecture Backlog item. They are not current dependencies.

## 4. Required visible findings

The projection must show Organization as currently independent from Resource, Operation and Assignment. The possible Organization-to-Organizational-Resource bridge remains future work under AB-052.

The future layer must include Objective, Capability, Event, Coordination, Conflict, State and Readiness according to their current registry/backlog status, without promoting any of them.

## 5. M1 exit criteria

M1 is complete when:

1. all five M1 Concepts are Accepted;
2. repository validation and Concept graph validation pass;
3. no unresolved blocking review finding exists for the M1 set;
4. the generated map exactly matches authoritative current metadata;
5. future intent is visibly separated from current truth;
6. AB-053 is completed: `Concept-Depends-On` is present in defining documents and the migration staging record has been removed.

## 6. Non-goals

This baseline does not define new domain semantics, add a Concept, resolve State/Readiness, or make future edges normative current dependencies.
