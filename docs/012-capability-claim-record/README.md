---
Document-ID: OCP-012
Title: Capability Claim Record Contract
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-000, OCP-001, OCP-002, OCP-003, OCP-009, AD-007, P-001
Uses-Patterns: P-001@0.1.0
Used-By: AB-011, Resource Matching, Coordination, Audit
Last-Review: 2026-08-04
Review-After: AB-011 Resource interchangeability review
---

# OCP-012 — Capability Claim Record Contract

## 1. Authority and incorporated contract body

Architecture Board accepts OCP-012 revision `0.2.0` as the governed implementation of Outcome B from AD-007C.

The complete externally reviewed contract body is preserved verbatim in [`reviewed-contract-v0.1.0.md`](reviewed-contract-v0.1.0.md). Sections 1–15 of that immutable review artifact are incorporated into this Accepted specification without semantic alteration. Its frontmatter and §16 preserve the pre-acceptance Draft state as historical review evidence only; where lifecycle language differs, this README is authoritative.

This publication split does not change the reviewed claim semantics, checker contract or ontology boundary. CapabilityClaimRecord remains a governed identified-record contract, not a fundamental Concept.

## 2. Accepted normative baseline

The accepted contract defines one narrowly attributable claim by one claimant about one exact Resource and one exact OCP-009 Capability version under an exact condition set and stated temporal applicability.

The record is authoritative only for the attribution that the claimant made the claim under the recorded authority and provenance. It does not establish objective truth, independent verification, Readiness, availability, authorization, admissibility, Assignment eligibility, Operation success or Resource interchangeability.

The baseline retains:

- exact Resource, Capability-version, claimant, claim-kind, condition-set, authority and provenance bindings;
- `P-001@0.1.0` Modules A and C for half-open temporal applicability and history-preserving supersession;
- immutable evidence snapshots and fail-safe support handling;
- withdrawal distinct from negative polarity;
- visible branching without newest, storage-order, claimant-count or source-count precedence;
- a fail-safe attributable claim-head projection;
- Resource-only initial holders and explicit rejection of Organization holders;
- separate Resource identities even when their applicable claims match.

## 3. Executable conformance

The normative checker manifest, derivations and fixtures introduced with revision `0.1.0` remain the executable evidence for this accepted contract. They cover exact resolution, historical withdrawal replay, conflicting branches, stale support, immutable snapshots, supersession safety, forbidden coupling and identity preservation.

The checker remains a reference validator. Acceptance does not create a production wire schema, persistence API, trust engine, assessment contract or condition-expression language.

## 4. Boundary with assessment and AB-011

CapabilityClaimRecord records an attributable declaration. It does not become a Capability assessment or silently extend OCP-011. A future independently assessed Capability path still requires its own reviewed decision under AD-007C §24.3.

AB-011 may consume only the accepted fail-safe projection of applicable claim heads. Missing, stale, ambiguous, conflicting, unresolved or otherwise invalid inputs cannot yield an authoritative positive input by default. AB-011 must decide contextual Resource interchangeability separately and may not collapse Resource identity.

## 5. External review evidence

External adversarial review examined the semantic contract and executable evidence on exact head `7eb7dd60e5bb4991478694559b8a5511239b100f`. Fable approved that head at iteration 2 of 5, CI was green on the same head, and the reviewed Draft was squash-merged in PR #44 as `ec285c4c0393914717781952a5929c94e9a84a7d`.

This acceptance candidate changes lifecycle and governance projections only. It does not modify the externally reviewed contract body, checker rules, derivations, manifests or fixtures.

## 6. Architecture Board decision

On 2026-08-04, Architecture Board accepts OCP-012 revision `0.2.0` and decides:

1. accept CapabilityClaimRecord as the governed holder-specific claim contract selected by AD-007C Outcome B;
2. retain its authority as a narrow attributable declaration, not objective truth or independent assessment;
3. retain exact bindings, P-001 Modules A/C, withdrawal semantics, visible branching and fail-safe projection;
4. preserve Resource-only initial holders and every accepted non-equivalence boundary;
5. resolve AB-057;
6. keep AB-011 Planned as the next normative cycle and prohibit claim equality from implying Resource equality or automatic substitution;
7. preserve eight Accepted fundamental Concepts because CapabilityClaimRecord remains a non-Concept record contract.
