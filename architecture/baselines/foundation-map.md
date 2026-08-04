# Foundation Concept Map

> GENERATED FILE. Current-state sections are derived from OCP-000 and defining-document `Concept-Depends-On` metadata.
> Future intent is rendered from `foundation-future-edges.yaml` and is not a current dependency.

## Registered Concepts

| Concept | Status |
|---|---|
| Assignment | Accepted |
| Capability | Accepted |
| Constraint | Accepted |
| Coordination | Proposed |
| Event | Proposed |
| Objective | Accepted |
| Operation | Accepted |
| Operational Area | Proposed |
| Operational Space | Proposed |
| Order | Proposed |
| Organization | Accepted |
| Readiness | Deferred |
| Resource | Accepted |
| Result | Proposed |
| Risk | Proposed |
| Spectrum | Proposed |
| State | Deferred |

## Current normative dependencies

- `Assignment → Operation`
- `Assignment → Resource`
- `Operation → Objective`

## Current isolated defined Concepts

- `Capability`
- `Constraint`
- `Organization`

## Future intent — non-normative

- `Resource ⇢ Capability` — AB-004
- `Constraint ⇢ Conflict` — AB-038
- `Organization ⇢ Resource` (dashed) — AB-052
- `Operation ⇢ Event` — OCP-000 Event Proposed
- `Organization ⇢ Coordination` — AB-003 and OCP-000 Coordination Proposed
- `Operation ⇢ State` — AB-007 and ADR-DRAFT-007
- `Resource ⇢ Readiness` — AB-007 and ADR-DRAFT-007
