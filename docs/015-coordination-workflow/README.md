---
Document-ID: OCP-015
Title: Coordination Proposal and Response Record Contract
Version: 0.2.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-001, OCP-005, OCP-006, OCP-012, OCP-013, OCP-014, AD-009
Used-By: AB-059, Coordination workflows
Uses-Patterns: P-001@0.1.0
Last-Review: 2026-08-05
Review-After: AB-059 cross-vertical visibility and agreement-semantics review
---

# OCP-015 — Coordination Proposal and Response Record Contract

## 1. Authority and incorporated contract body

Architecture Board accepts OCP-015 revision `0.2.0` as the governed workflow-evidence contract selected by AD-009 Outcome B and the narrow resolution of AB-058.

The complete externally reviewed contract body is preserved verbatim in [`reviewed-contract-v0.1.0.md`](reviewed-contract-v0.1.0.md). Sections 1–15 of that immutable review artifact are incorporated into this Accepted specification without semantic alteration. Its frontmatter and §16 preserve the pre-acceptance Draft state as historical review evidence only; where lifecycle language differs, this README is authoritative.

This publication split does not change the reviewed proposal/response semantics, checker contract or ontology boundary. `CoordinationProposalRecord` and `CoordinationResponseRecord` remain governed non-Concept records.

## 2. Accepted normative baseline

The accepted contract lets one vertical publish an immutable proposal revision and lets each invited vertical issue its own attributable response to that exact revision. No publisher may write another vertical's response, and no responder may rewrite a proposal.

The baseline retains:

- separate P-001 Modules A and C invocations for proposal and response records;
- exact publisher, responder, context, requirement, time and provenance bindings;
- immutable history with explicit acyclic supersession;
- responder-scoped response heads and exact proposal-revision binding;
- `confirm`, `decline` and history-preserving `withdraw` responses;
- deterministic `positive`, `negative`, `withdrawal` and `indeterminate` projection outcomes;
- fail-safe handling of missing, stale, conflicting, unresolved, cross-revision and forbidden inputs;
- replay independent of record order, revision number, newest timestamp or record count.

A `positive` projection means only that the required attributable confirmations exist for one exact evidence snapshot. It is not authorization, approval, consensus, selection, reservation, allocation, commitment or Assignment mutation.

## 3. Authority boundary

The proposal publisher is authoritative only for publishing the exact proposal record. Each response issuer is authoritative only for its own exact response record. The OCP-015 rule is authoritative only for the mechanical evidence projection over exact inputs.

OCP-014, OCP-013, OCP-012 and OCP-006 retain their separate authorities. OCP-015 does not authenticate actors, define a universal visibility policy, settle disagreement, grant permission, choose a Resource or alter Resource or Assignment identity.

Actor authentication, delegation and signature validation remain an explicit evidence gap. An implementation may not infer authority from labels, Organization names, caller identity, service accounts, timestamps or storage order.

## 4. Executable conformance

The accepted rule manifest, derivation and mandatory fixture cover positive, negative, indeterminate and withdrawal paths; proposal revision; conflicting heads; expiry; forbidden authority coupling; record-order independence; rule-version binding; and whitespace-normalized exact response references.

The explicit whitespace microtest locks the reviewed rule that both `proposal_ref` and `responder_ref` pass through the same textual normalization before exact comparison. It adds no aliasing, fuzzy matching or new semantic authority.

The checker remains a reference validator, not a production API, persistence layer, permission service, authenticator, workflow engine or independent normative owner.

## 5. External review evidence

Fable externally reviewed exact semantic head `3fc7319df87dcff17516b9639b10cc3e0ff117a2` and approved it with non-blocking observations at iteration 2 of 5. Codex independently re-reviewed the exact head, accepted Fable's recommendation, verified green CI and no unresolved review threads, and kept owner authorization as a separate merge gate.

Pavlo explicitly authorized PR #54 for squash merge. The reviewed Draft was squash-merged as `a76b2c6242d53c34495f85f4938a605441ad0aec` with the required `reference-checker` green on that exact head.

## 6. Architecture Board decision

On 2026-08-05, Architecture Board:

1. accepts AD-009 revision `0.2.0` and its Outcome B selection;
2. accepts OCP-015 revision `0.2.0` as the governed proposal/response workflow-evidence contract;
3. retains the independent record authorities, exact bindings, history-preserving supersession and fail-safe projection;
4. preserves every exclusion of authorization, approval, consensus, availability, Readiness, capacity, ranking, selection, reservation, allocation, replacement and Assignment mutation;
5. preserves Resource and Assignment identity and introduces no new fundamental Concept or Concept graph edge;
6. resolves AB-058 for this narrow record-and-projection contract;
7. atomically creates AB-059 for cross-vertical visibility policy and negotiation, consensus or agreement semantics beyond this boundary; and
8. requires any future expansion to proceed through AB-059 without reinterpreting historical OCP-015 evidence.

## 7. Next normative cycle

AB-059 is the next normative cycle named by this acceptance act. It must decide only the residual cross-vertical visibility-policy and agreement-semantics questions with separate authority and fail-safe evidence.

AB-059 may consume OCP-015 records and projections, but it may not turn confirmation into permission, consensus, selection, reservation, allocation or Assignment mutation. Authorization remains under AB-017; conflict resolution remains under AB-018 and AB-038; reservation and allocation remain under AB-025; Assignment lifecycle alignment remains under AB-028.
