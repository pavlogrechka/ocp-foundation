---
Document-ID: OCP-013
Title: Contextual Resource Interchangeability Contract
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-003, OCP-005, OCP-006, OCP-009, OCP-012, AD-008
Used-By: Coordination
Last-Review: 2026-08-04
Review-After: Coordination profile review
---

# OCP-013 — Contextual Resource Interchangeability Contract

## 1. Authority and incorporated contract body

Architecture Board accepts OCP-013 revision `0.2.0` as the governed implementation of Model A from AD-008C and the resolution of AB-011.

The complete externally reviewed contract body is preserved verbatim in [`reviewed-contract-v0.1.0.md`](reviewed-contract-v0.1.0.md). Sections 1–15 of that immutable review artifact are incorporated into this Accepted specification without semantic alteration. Its frontmatter and §16 preserve the pre-acceptance Draft state as historical review evidence only; where lifecycle language differs, this README is authoritative.

This publication split does not change the reviewed eligibility rule, fixtures, checker behavior or ontology boundary. Contextual Resource interchangeability remains a directional evaluation against one exact consumer-owned requirement, not identity equality or a Resource-to-Resource graph edge.

## 2. Accepted normative baseline

The accepted contract answers one narrow question:

> Does this exact candidate Resource satisfy this exact, versioned consumer requirement in this governed context and at this evaluation time?

Every evaluation binds the exact requirement, candidate, context, time, Capability-claim heads, candidate-specific Constraint snapshot, aggregate input snapshot and rule version. A change to any binding creates a new evaluation; no result is silently reused.

The accepted baseline retains:

- a consumer-owned immutable `requirement_id@version` with explicit owner, context, effectivity and provenance;
- exact OCP-009 Capability-version and condition-set bindings;
- attributable OCP-012 claim inputs without converting declarations into objective truth;
- an OCP-006 Constraint result for the same candidate, context and evaluation time;
- directional `candidate Resource → exact contextual requirement` evaluation;
- deterministic replay and executable counterexamples;
- separate Resource identities even when candidates satisfy the same requirement.

## 3. Outcomes and fail-safe precedence

The governed outcomes remain:

- `positive` — complete exact inputs show that the candidate satisfies the requirement and its Constraint decision is admissible;
- `negative` — complete governed inputs contain an exact Capability mismatch or inadmissible Constraint decision;
- `review_required` — complete inputs expose a judgment that the mechanical rule cannot make;
- `indeterminate` — an input is missing, stale, ambiguous, conflicting, withdrawn, mismatched or unresolved, the rule version is unknown, or forbidden coupling was attempted.

When inputs point to more than one outcome, precedence remains:

```text
indeterminate > review_required > negative > positive
```

Neither `indeterminate` nor `review_required` becomes a durable negative. A `positive` result remains eligibility evidence only and never becomes permission.

## 4. Authority boundary

The requirement owner may state the need of its governed consumer context. The OCP-012 claimant remains authority only for its attributable Capability claim. The OCP-006 evaluator remains authority for its candidate-specific Constraint result. The OCP-013 rule authority may only combine those exact inputs mechanically.

OCP-013 does not decide or imply Resource identity, equality, Readiness, availability, capacity, reservation, authorization, approval, ranking, selection, Assignment mutation, replacement execution, objective Capability truth or independent assessment.

The reference checker verifies requirement structure and exactness. It cannot establish that an `owner_ref` legitimately represents a governed consumer contract. Architecture Board review of that consumer contract establishes legitimacy; the first required application of this trust boundary is the Coordination profile.

## 5. Executable conformance

The normative rule manifest, derivation and fixtures introduced with revision `0.1.0` remain the executable evidence for this Accepted contract. They exercise all thirteen AD-008 §12 counterexamples, exact-rule replay, unknown-rule failure, clean Constraint review, clean claim review and stale-input precedence over review.

The checker remains a reference validator, not a production evaluator, schema, API, persistence layer, authorization service, selection workflow or replacement mechanism.

## 6. External review evidence

External adversarial review examined the semantic contract and executable evidence on exact head `ec12f24f80b697d1048803545110f0656b4633e3`.

Iteration 1 found a Moderate inconsistency in the `review_required` channel and a Minor omission in the `owner_ref` trust boundary. The exact head resolved both findings by documenting claim-level review, enforcing `indeterminate > review_required > negative > positive`, adding three executable witnesses and naming Architecture Board review as the source of consumer-owner legitimacy.

Fable approved that exact head at iteration 2 of 5, Codex independently accepted the recommendation, the exact-head CI check was green, and Pavlo explicitly authorized squash merge. The reviewed Draft was squash-merged in PR #49 as `5e8f000b919a03233b03eac7f46352967c62f31a`.

This acceptance candidate changes lifecycle and governance projections only. It does not alter the externally reviewed contract body, rules, derivation, manifests or fixtures.

## 7. Architecture Board decision

On 2026-08-04, Architecture Board accepts OCP-013 revision `0.2.0` and decides:

1. accept Model A as a deterministic directional eligibility contract against a consumer-owned exact requirement;
2. retain exact candidate, context, time, claim-head, Constraint-snapshot, input-snapshot and rule-version bindings;
3. retain the four outcomes and their fail-safe precedence;
4. preserve the distinction between attributable claims, candidate-specific Constraint decisions and mechanical derivation;
5. prohibit symmetry, transitivity, Resource identity collapse and any implicit Resource-to-Resource graph edge;
6. retain every exclusion of availability, authorization, ranking, selection, replacement and Assignment mutation;
7. resolve AB-011;
8. keep the number of Accepted fundamental Concepts unchanged because the requirement and evaluation are governed contract structures, not new Concepts.

## 8. Next normative cycle

The next normative cycle is the Coordination profile. Its first OCP-013 obligation is to establish a legitimate governed consumer `owner_ref` and exact contextual requirement without importing availability, authorization, ranking, selection, replacement or Assignment-mutation authority into OCP-013.
