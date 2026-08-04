---
Document-ID: OCP-014
Title: Coordination Consumer Profile
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-003, OCP-004, OCP-006, OCP-009, OCP-012, OCP-013
Used-By: AB-003, Coordination Workflows
Last-Review: 2026-08-04
Review-After: AB-058 separate Coordination workflow mandate
---

# OCP-014 — Coordination Consumer Profile

## 1. Authority and incorporated contract body

Architecture Board accepts OCP-014 revision `0.2.0` as the first governed Coordination consumer profile and the narrow resolution of AB-003's consumer-identity question.

The complete externally reviewed contract body is preserved verbatim in [`reviewed-contract-v0.1.0.md`](reviewed-contract-v0.1.0.md). Sections 1–9 of that immutable artifact are incorporated into this Accepted specification without semantic alteration. Its frontmatter, Draft wording and §10 remain historical review evidence only; this README governs lifecycle and acceptance.

The accepted owner reference is:

```text
ocp-coordination-consumer@0.1.0
```

It identifies the governed consumer contract that may formulate one exact contextual requirement. It does not identify or authenticate the caller that submits a record.

## 2. Accepted normative baseline

Each `CoordinationResourceRequirement` remains an immutable OCP-013 requirement with exact `requirement_id@version`, the accepted owner reference, one exact `context_ref`, effectivity, exact Capability-version and condition-set bindings, and attributable provenance.

The profile grants only authority to state the need of that exact context. It does not make a caller, Organization, service account, incumbent Resource or checker authoritative. Actor authentication and authorization require a separate future contract; caller identity cannot supply, replace or override `owner_ref` or any other requirement binding.

The authority chain remains separated among Architecture Board profile acceptance, the Coordination consumer's requirement, the OCP-012 claimant, the OCP-006 evaluator and the OCP-013 mechanical rule. None inherits another layer's authority.

## 3. Fail-safe exact-owner binding

A requirement presented as this profile is authoritative only when `owner_ref` exactly equals `ocp-coordination-consumer@0.1.0`. A missing, aliased, caller-supplied, newest-selected or different owner reference yields no authoritative Coordination requirement; it does not produce a negative conclusion about a Resource.

The reference checker now exercises this profile-specific exact-owner invariant. That finite check does not establish actor identity, signature validity, delegation, authorization or operational permission.

All other reviewed fail-safe cases remain unchanged: unresolved context, out-of-interval evaluation, inexact Capability or condition bindings, missing provenance, forbidden coupling and caller defaults fail safe.

## 4. Preserved authority boundary

An OCP-013 `positive` result remains directional evidence that one candidate satisfies one exact requirement at one evaluation time. It does not create Resource equality, symmetry, transitivity or a Resource-to-Resource graph edge.

OCP-014 does not define availability, readiness, capacity, authorization, approval, ranking, selection, reservation, allocation, replacement, Assignment mutation, command, control, negotiation, consensus, disagreement handling or a complete Coordination workflow.

No new fundamental Concept or Concept dependency edge is introduced. Coordination workflow semantics require a separate accepted mandate.

## 5. External review evidence

Fable externally reviewed exact semantic head `32597004d9a39e192dc9566ed5f691d902434dbb` and approved it with two non-blocking observations at iteration 1 of 5. Codex independently accepted the recommendation while preserving the merge gates, and Pavlo explicitly authorized squash merge. The reviewed Draft was squash-merged in PR #51 as `7fef7376246c99aeccf4f4e9c850c2a36f60d659` with green exact-head CI and no unresolved review threads.

The accepted follow-ups are incorporated here: an executable wrong-owner counterexample now binds this profile's exact accepted owner reference, and the actor-binding clarification explicitly keeps caller authentication and authorization outside the profile.

## 6. Architecture Board decision

On 2026-08-04, Architecture Board:

1. accepts OCP-014 revision `0.2.0` and activates `ocp-coordination-consumer@0.1.0` as this profile's only exact owner reference;
2. accepts the exact contextual requirement shape incorporated from the reviewed contract;
3. requires profile-specific owner mismatch to fail safe without treating caller identity as authority;
4. preserves separate consumer, claimant, Constraint-evaluator and OCP-013 rule authority;
5. prohibits any inference of availability, authorization, approval, ranking, selection, reservation, replacement or Assignment mutation;
6. preserves Resource identity and introduces no new fundamental Concept or Concept graph edge;
7. resolves AB-003 only for the governed consumer-profile question; the remaining vertical-agreement and workflow scope is tracked by AB-058; and
8. requires a separate mandate before any Coordination workflow cycle.

## 7. Next normative cycle

OCP-014 does not pre-authorize the next Coordination workflow scope. Under AB-058, the next cycle must first select a separate accepted mandate and may not infer negotiation, approval, conflict handling, visibility, command, reservation or lifecycle semantics from this consumer profile.
