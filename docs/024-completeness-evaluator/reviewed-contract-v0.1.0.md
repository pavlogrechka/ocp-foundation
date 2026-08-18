---
Document-ID: OCP-024
Title: Assignment-Set Completeness Evidence Recognition
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: AD-042, AD-043, OCP-001, OCP-016, OCP-023
Used-By: Resource occupancy completeness-evidence review and synthetic reference validation
Last-Review: 2026-08-17
---

# OCP-024 — Assignment-Set Completeness Evidence Recognition

## 1. Status and route

This is a `0.1.0 / Draft` Route D domain-local recognition contract. It does not amend Core, introduce a Concept, name a production system or activate any result. Draft is required because this exact body has not yet completed an acceptance act or acquired a reviewed snapshot.

OCP-016 G4 does not apply to authoring this non-activated reference envelope. G4 remains mandatory for any future activation of assignment-set completeness: OCP-023 supplies an Accepted consumer, while the exact activation baseline, protected rule version, input snapshot, evaluation context and legitimate production owner/evaluator remain absent.

## 2. One question and explicit non-activation

The sole question is: under which producer-independent properties may evidence be recognized as supporting

`assignment_set_complete_for_resource(resource_ref, evaluation_time, snapshot_ref)`?

This document recognizes only a synthetic reference proof. It does not assert that any real Assignment set is complete, derive occupancy, authenticate `SYNTH-COMPLETE-*`, or authorize an evaluator.

## 3. Independence test and honest limit

The recognition envelope can be stated without naming a database, protocol, vendor, organization or operator: exact subject, exact coverage, temporal validity, provenance/authority binding, uniqueness and fail-safe behavior are independently meaningful properties.

Actual legitimacy cannot be established from those properties alone. A producer-independent checker can verify that evidence points to an authority basis; it cannot prove that a real authority delegated the named evaluator or that a real source observed the whole subject. The Architecture Board's governance ownership is not a substitute. Therefore this contract admits only `SYNTH-EVALUATOR-*` with `SYNTH-AUTHORITY-*` in its reference proof. A real evaluator remains unresolved and requires a separate act grounded in an external domain authority.

## 4. Recognition properties

Evidence is recognized by the reference proof only when all properties hold:

1. **Provenance and authority binding:** exactly one evaluator profile binds the evaluator, domain, subject kind, authority-basis reference and validity interval. A reference is necessary but does not itself establish real delegation.
2. **Exact subject:** the evidence and request bind the same Resource, evaluation time and Assignment snapshot.
3. **Exact coverage:** the evidence claims `all-assignments-for-resource-at-time`; a subset, sample or unspecified collection is not sufficient.
4. **Temporal validity:** the profile is valid at evaluation time and evidence is produced no later than that time.
5. **Uniqueness and consistency:** the requested profile and evidence each resolve exactly once; conflicting claims are invalid.
6. **Fail-safe:** missing, malformed, stale, mismatched, unauthorized, ambiguous or conflicting evidence yields `indeterminate`, never completeness and never `occupied=false`.

## 5. Reference envelope

The dataset contains exactly:

- one `recognition_request` binding rule, Resource, evaluation time, Assignment snapshot, evaluator profile, completeness evidence and stored result;
- `evaluator_profiles`, whose records bind evaluator, domain, subject kind, authority basis and validity interval; and
- `completeness_evidence`, whose records bind profile, Resource, evaluation time, Assignment snapshot, production time, coverage kind and claim.

Unknown activation fields and fields for conflict, priority, capacity, reservation, allocation, permission, lifecycle mutation or action recommendations are rejected.

## 6. Derivation

`derive_completeness_evidence_recognition(dataset)` returns `synthetic-reference-recognized` only when the envelope is exact, both references resolve uniquely and every property in §4 holds with the synthetic evaluator and authority namespaces.

All other inputs return `indeterminate`. The derivation has no `false` result because invalid evidence cannot prove absence or completeness.

## 7. Failure semantics

Validation distinguishes malformed request/profile/evidence, unresolved or ambiguous references, subject mismatch, scope mismatch, invalid time, unresolved authority, conflicting evidence, forbidden activation/coupling and stored-result mismatch. These failures do not fall back to a permissive result.

A production-shaped evaluator or authority value is rejected as unresolved rather than accepted by resemblance. This is the executable boundary between properties of a legitimate envelope and actual legitimacy of a real producer.

## 8. Executable evidence

`tools/ontology_checker/ocp_checker/completeness_evaluator.py`, its manifest, focused tests and synthetic fixtures implement the envelope. The valid fixture proves only reference coherence. Stale, ungrounded, conflicting, activation-bearing and adjacent-semantics fixtures remain indeterminate and fail validation.

Every declared field, result token, namespace, error code, derivation and defensive-list value has individual fixture or mutation evidence. Existing fixtures are unchanged.

## 9. Non-implications

This contract does not:

- activate completeness or resource occupancy;
- name a real owner, evaluator, completeness source, system or protocol;
- change OCP-023 or OCP-005;
- establish conflict, priority, capacity, reservation, allocation, permission or authorization;
- remove an Assignment blocker, create a Concept, alter the graph, choose a promotion candidate or start a cycle.

## 10. Version, migration and rollback

`0.1.0` is the first bounded Draft of this Route D contract. It adds no migration duty because no production representation is activated. Rollback removes OCP-024, AD-043, the isolated module, manifest, tests, fixtures and current accounting together; partial rollback would leave registered evidence without its owner.

Acceptance of this exact body, naming a real authority relation, or activation of completeness each requires a separate mandate and fresh gates. None is implied here.
