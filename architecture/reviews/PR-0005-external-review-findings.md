# PR-0005 External Review Findings

- Review target: `OCP-006 — Constraint Concept`
- Review source: external Fable 5 review provided to Architecture Board
- Decision date: 2026-08-02
- Resolution branch: `agent/pr-0005-constraint-concept`
- Resolution PR: `PR-0005 — Define Constraint Concept`
- Final Architecture Board decision: `Accepted`

## Finding 1 — Applicable Constraint may retain `not_applicable`

**Status:** Accepted — resolved.

The draft allowed an authoritative `ConstraintEvaluationRecord.result = not_applicable` to coexist with `constraint_applicable_to(Constraint, Context) = true`.

Because the admissibility derivation ignored that contradiction, an evaluator error could produce a more permissive result than a missing evaluation. This violated the fail-safe rules for missing or uncertain evidence.

**Resolution:**

- `not_applicable` is authoritative only when temporal or target scope does not match the context;
- for an applicable Constraint, `effective_constraint_result` cannot be `not_applicable`;
- an applicable stored `not_applicable` is normalized to `indeterminate`;
- a dedicated invariant prohibits the contradictory authoritative record;
- invariant rejection and derivation normalization are intentionally retained as defense-in-depth;
- the counterexample is retained as an example and will become a PR-0006 regression fixture that tests both layers.

## Finding 2 — Advisory violation and advisory uncertainty are asymmetric

**Status:** Accepted as clarification — resolved.

The draft allowed:

- `advisory + violated` to remain a non-blocking finding;
- `advisory + indeterminate + require_review` to produce `review_required`.

This asymmetry is intentional but was not explained.

**Resolution:**

- a known advisory violation is already classified and is delegated to the domain workflow;
- advisory uncertainty may stop only automatic decision completion when the Constraint explicitly requires review;
- `review_required` is not equivalent to `inadmissible`;
- the distinction is now stated in EnforcementSpecification, admissibility derivation, Business Rules, Semantic Rules and examples.

No automatic prohibition of `indeterminate_disposition = block` for advisory Constraint is introduced in this correction. The current `constraint_blocks` formula still requires `enforcement.mode = blocking`, so an advisory Constraint cannot directly produce `inadmissible`.

## Finding 3 — Corrective and Concept cycles appeared bundled in the review snapshot

**Status:** Clarified — resolved by sequencing.

The external reviewer reported that the initial review snapshot showed PR-0004A commits together with PR-0005 changes relative to the then-observed `main`. The current GitHub PR metadata and diff show PR #8 based on the separately merged PR-0004A commit:

```text
PR-0004A merge commit / current PR #8 base:
faacaf7aacfa29de0d4bf642036b603a96097c9b
```

The repository does not retain the reviewer’s exact transient comparison snapshot, so the earlier state should not be labelled factually incorrect. The process concern was valid: corrective and new Concept cycles must remain independently approvable.

**Resolution:**

- PR-0004A was approved and squash-merged separately;
- the current PR #8 diff contains only the Constraint cycle and related governance/roadmap changes;
- PR-0005 cannot merge PR-0004A implicitly;
- the governance precedent remains: corrective cycles and new Concept cycles are separate unless Architecture Board explicitly approves and records an exception;
- future stacked PR review should record the compared base SHA and intended merge order to preserve provenance.

## Finding 4 — Concept status choreography is inconsistent

**Status:** Accepted — resolved.

Earlier Concept cycles used `Under Review` at different stages, while Constraint remained `Proposed` in a Draft PR.

**Resolution:**

OCP-001 now defines one process:

```text
Draft PR / candidate registration → Proposed
Ready for review                 → Under Review
Architecture Board approval      → Accepted before merge
Separate canonicalization PR     → Canonical
```

PR-0005 passed through ready-for-review / `Under Review`, then `Constraint` was synchronously updated to `Accepted` in OCP-000, OCP-002 and OCP-006 after the explicit Architecture Board decision.

## Finding 5 — Executable validation is scheduled too late

**Status:** Accepted — sequence changed.

The first checker slice is moved before additional major Concept growth.

**Resolution:**

- `PR-0006 — Add Executable Ontology Checker` follows PR-0005;
- it will introduce YAML fixtures for Resource, Operation, Assignment and Constraint;
- accepted review counterexamples become regression fixtures;
- initial reference derivations and CI checks are included;
- later Concept PRs should carry fixtures where expressible.

PR-0006 is a reference validation layer, not production implementation.

## Architecture Board decision

> Accept OCP-006 Constraint Concept after resolution and external verification of the review findings. Preserve the clarified sequencing provenance, retain defense-in-depth for contradictory evaluation records, adopt the unified Concept status choreography, and make PR-0006 the next cycle. Constraint status is Accepted before merge.
