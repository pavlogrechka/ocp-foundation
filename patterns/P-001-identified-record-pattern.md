---
Pattern-ID: P-001
Title: Identified Record Pattern
Version: 0.1.0
Status: Draft
Normative-Level: binding-when-invoked
Owner: Architecture Board
Depends-On: AD-001, OCP-001
Last-Review: 2026-08-03
---

# P-001 — Identified Record Pattern

## 1. Purpose

P-001 defines a reusable modeling contract for a relation, assertion or contextual record that requires independent identity and one or more governed lifecycle, temporal, provenance or supersession properties.

P-001 defines form. It does not define domain meaning.

## 2. Invocation

A normative artifact invokes this pattern through versioned metadata:

```yaml
Uses-Patterns: P-001@0.1.0
```

Invocation is optional. Once invoked, all Required Elements are binding, and every selected Optional Module brings its stated obligations.

The invoking artifact remains the only normative home for domain semantics, endpoint meaning, allowed kinds and domain-specific invariants.

## 3. Applicability threshold

An identified record should be considered when a modeled relation or assertion requires at least one of:

- independent identity;
- explicit endpoint contract;
- temporal effectivity;
- lifecycle or transition history;
- provenance or evidence;
- supersession or amendment history;
- record-specific attributes;
- record-specific authorization or constraints.

A direct reference or derived edge may remain simpler when none of these properties is required.

## 4. Required Elements

Every P-001 invoker defines:

1. **Stable record identity** — a non-empty identifier unique in the invoking model.
2. **Owning semantic specification** — one normative location for the record's meaning.
3. **Endpoint contract** — named endpoint fields, allowed endpoint types and unambiguous directionality when endpoints exist.
4. **Governed kind reference** — a stable, versioned kind or type reference when multiple semantic kinds are permitted; arbitrary free-form type strings are not normative.
5. **Provenance contract** — the minimum provenance structure required to establish or authorize the record.
6. **Validation contract** — verifiable invariants, including at least one invalid counterexample for each material rule where expressible.
7. **Authority declaration** — which stored record or derivation is authoritative when the same semantics has multiple representations.

Not every identified record must connect two endpoints. An invoker may declare an endpoint-free assertion form, but must do so explicitly.

## 5. Optional Module A — Temporal Effectivity

When selected, the invoker defines:

- start boundary;
- optional end boundary;
- interval inclusivity or exclusivity;
- treatment of absent bounds;
- the exact `effective_at(record, t)` derivation;
- behavior for invalid or incomplete timestamps.

A stored convenience field must not silently create a more permissive effective result than missing or indeterminate authoritative data.

## 6. Optional Module B — Transition History and Projections

When selected:

1. allowed lifecycle stages and paths are explicit;
2. transition history is either declared authoritative or explicitly secondary;
3. every transition record has identity, record reference, source stage, target stage, occurrence time and provenance;
4. transition timestamps are ordered under a defined rule;
5. current stage and lifecycle timestamps are deterministic projections;
6. materialized projections are optional unless the invoker explicitly requires them;
7. when present, materialized projections equal authoritative derivations;
8. invalid branching or mutually exclusive paths are prohibited.

The invoker defines the exact projection names and lifecycle semantics.

## 7. Optional Module C — Supersession

When selected, the invoker defines:

- the superseded record reference;
- prohibition of self-supersession;
- whether supersession is one-to-one or may branch;
- whether overlap or gaps are allowed;
- which record is effective during overlap;
- provenance for the replacement decision.

Supersession does not rewrite the history of the prior record.

## 8. Optional Module D — Defense in Depth

P-001 does not create a separate universal defense-in-depth doctrine. Invokers follow the invariant requirements already defined in OCP-001.

Where invalid stored data can bypass validation, a derivation may independently normalize it to a non-permissive result. Such duplication must be documented as intentional and tested at both layers.

## 9. Anti-patterns

### AP-1 — Pattern as semantic container

Do not move domain meaning into P-001 or into generic type strings. Shared form is not shared semantics.

### AP-2 — Universal relationship object

Do not reduce Assignment, Constraint or another specialized Concept to a generic record merely because it has endpoints.

### AP-3 — Hidden authoritative convenience field

Do not allow a materialized lifecycle or effectivity field to override the declared authoritative history or derivation.

### AP-4 — Invocation without version

Do not declare `Uses-Patterns: P-001` without a version reference.

### AP-5 — Partial invocation by silence

An invoker may omit an Optional Module, but may not use that module's fields while avoiding its obligations.

## 10. Conformance statement

A conforming invoking artifact documents:

- the P-001 version;
- selected optional modules;
- mapping from P-001 elements to local field names;
- domain-specific rules and invariants;
- positive and negative fixtures where the executable reference supports them.

## 11. Current evidence

P-001 is extracted from repeated, independently reviewed structures in Assignment and Constraint and is intended for explicit invocation by Organization relationship records after PR-0006A is accepted.

Similarity of implementation helpers alone does not justify a new pattern. Future patterns require repeated independent use, stable form, demonstrated drift reduction and absence of domain semantics.
