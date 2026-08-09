---
Document-ID: OCP-019
Title: Conflict Derivation Boundary
Version: 0.1.0
Status: Draft
Owner: Architecture Board
Depends-On: AD-022, OCP-001, OCP-006, OCP-016
Used-By: Conflict derivation review, Audit
---

# OCP-019 — Conflict Derivation Boundary

## 1. Route and Draft status

OCP-019 is a Route C Core non-Concept contract under OCP-016. It governs one shared negative boundary: what exact OCP-006 evaluation evidence is insufficient to establish an authoritative Conflict. It does not define a `Conflict` identity, a positive Conflict result or a persisted Conflict record.

This `0.1.0` artifact is `Draft`. Its semantic result vocabulary is intentionally limited to `conflict_not_established | indeterminate`. `conflict_not_established` means only that this contract has no legitimate positive derivation authority; it does not assert that no conflict exists in reality.

## 2. Existing normative inputs

OCP-006 §11 owns `ConstraintEvaluationResult = satisfied | violated | indeterminate | not_applicable` and the local `ConstraintEvaluationRecord`. OCP-006 §13 already requires any later aggregation to preserve references to the evaluation records used and states that a violation does not automatically change lifecycle, cancel Assignment, create Risk, become a fundamental Conflict or determine remediation.

OCP-019 consumes those boundaries without changing them. It does not consume `constraint_set_decision` as Conflict evidence: `inadmissible`, `review_required` and `admissible` remain OCP-006 decisions with no automatic Conflict meaning.

## 3. Authority boundary

No current Accepted consumer and no exact legitimate criterion owner satisfy OCP-016 G4 for a positive Conflict-capable activation. The Architecture Board, AB-038 and OCP-019 cannot self-supply that missing operational consumer.

Therefore this Draft:

- never returns `conflict` or `no_conflict`;
- rejects stored or requested positive Conflict authority;
- carries no `Conflict` Concept, record, lifecycle or P-001 invocation;
- gives count, order, timestamp and mere co-occurrence no authority; and
- fails safe when evidence is missing, duplicated, contradictory, stale, malformed or cross-bound.

## 4. Result vocabulary

```text
ConflictEstablishmentBoundaryResult
- conflict_not_established
- indeterminate
```

`conflict_not_established` is available only for a complete exact request whose referenced OCP-006 evaluations are well formed, unambiguous, current and exact-bound. It remains a negative authority result even when every referenced evaluation is `violated`.

`indeterminate` is required when the request, rule, record set, reference resolution, binding, freshness or stored result is incomplete or contradictory, or any referenced evaluation itself is `indeterminate`.

## 5. Preserved OCP-006 evaluation evidence

Each input evaluation reproduces the OCP-006 §11 fields needed by this boundary:

```text
ConstraintEvaluationRecord
- evaluation_id
- constraint_ref
- constraint_version_ref
- context_ref
- input_snapshot_ref
- evaluated_at
- result
- evidence_refs [zero or more]
- evaluator_ref
```

Every `evaluation_ref` must resolve exactly one record. The derivation request preserves the complete reference list; neither validation nor derivation may replace it with a count, summary or newest-record choice.

## 6. Derivation request

```text
ConflictBoundaryDerivationRequest
- request_id
- rule_ref = conflict-establishment-boundary@1
- context_ref
- input_snapshot_ref
- evaluation_refs [one or more, unique]
- derived_at
- evidence_state = current | stale
- stored_result
```

The request is an invocation envelope, not an independently governed record family. It has no history, supersession or endpoint contract, is not exposed as a shared durable identity and therefore does not invoke P-001.

## 7. Exactness and ambiguity rules

All selected evaluations must exact-match the request's context and input snapshot. Evaluation identifiers and request references are unique. For one `constraint_version_ref + context_ref + input_snapshot_ref`, multiple different results are ambiguous regardless of file order or timestamps. An evaluation after `derived_at` and an explicitly stale evidence state are non-current.

Unreferenced evaluations have no effect. Reordering the same exact evidence has no effect. An additional violation has no effect unless explicitly referenced, and even when referenced it cannot create positive Conflict authority.

## 8. Normative derivation

```text
derive_conflict_establishment_result(dataset) :=
    indeterminate
        if the request or any selected evaluation is malformed
        OR a reference is missing, duplicated or ambiguous
        OR context or input snapshot differs
        OR evidence is stale or temporally inconsistent
        OR any selected evaluation result = indeterminate
        OR a prohibited positive/coupled field is present

    conflict_not_established
        otherwise
```

The second branch includes one violated evaluation, several violated evaluations and mixtures of definitive OCP-006 results. It does not aggregate them into Conflict.

## 9. Positive activation reopening gate

A later positive-capable model must be a separate Board act. Before comparison it must exact-bind one concrete Accepted consumer, that consumer's baseline and result need, one versioned positive rule, one exact input snapshot and context, and one legitimate rule owner/evaluator as required by OCP-016 G4. It must also decide whether the result is a projection, an independently identified P-001 record or evidence for a separately admitted fundamental Concept.

Until every element exists, missing evidence returns `indeterminate`; a violation count or Board preference cannot substitute for the gate.

## 10. Explicit exclusions and backlog disposition

- AB-018 remains Open. This Draft clarifies the lower boundary but does not decide the identity or admission of a fundamental Conflict Concept.
- AB-005 remains Open. No Risk taxonomy or automatic Risk derivation is introduced.
- AB-036 remains Open and outside scope. No precedence, override, exception or waiver rule is defined.
- AB-037 remains Open and outside scope. No quantity, unit, demand or capacity meaning is defined.
- AB-002 remains Open. No Order semantics or authorization are inferred.
- `Policy` is not introduced as a Concept.

No result changes Operation or Assignment lifecycle, cancels an Assignment, creates Risk, authorizes an action, chooses remediation or opens T6.

## 11. Neighbouring governed families

OCP-011 owns attributable outcome assessment, not Conflict. OCP-013 owns resource interchangeability results, not Conflict. OCP-015 owns proposal/response evidence and treats disagreement or decline as workflow evidence, not Conflict. Their record and fail-safe shapes demonstrate that a governed non-Concept result can exist, but OCP-019 does not reuse their result vocabularies or authority.

## 12. Executable evidence

`conflict-derivation-rules.yaml` binds every validation and derivation identifier to this document. The checker validates exact references and bindings and implements §8. Synthetic fixtures include valid one-violation, multi-violation, definitive mixed and indeterminate cases plus separate malformed, duplicate, unresolved, contradictory, cross-bound, stale, mismatched-result, positive-authority and forbidden-coupling cases.

The manifest declares direct fixture coverage complete. A repository-generic test verifies exact manifest-to-fixture coverage for this contract and OCP-018, closing the previously manual `12/12` OCP-018 link without imposing an untrue repository-wide completeness claim on legacy manifests.

Executable evidence proves the finite boundary only. It cannot prove a real Conflict, legitimate consumer, criterion owner or production profile.

## 13. Safety

All fixtures use synthetic identifiers and abstract snapshots. They contain no real coordinates, geometry, corridors, sectors, time windows, callsigns, unit identifiers, personal data, credentials or copied external-project structures.

## 14. Version, migration and rollback

`0.1.0 / Draft` is the first compatible contract surface. No prior OCP-019 exists, so PATCH or MINOR classification is inapplicable; Accepted or Canonical would overstate absent consumer and production evidence.

There is no data migration. Existing OCP-006 evaluations remain owned by OCP-006 and are not rebound. Rollback removes OCP-019, its manifest, module, tests and fixtures atomically; it does not rewrite evaluation history or restore a positive Conflict authority because none is created.
