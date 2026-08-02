# PR-0005 External Review Findings

- Review target: `OCP-006 — Constraint Concept`
- Review source: external Fable 5 review provided to Architecture Board
- Decision date: 2026-08-02
- Resolution branch: `agent/pr-0005-constraint-concept`
- Resolution PR: `PR-0005 — Define Constraint Concept`

## Finding 1 — Applicable Constraint may retain `not_applicable`

**Status:** Accepted — blocking.

The draft allowed an authoritative `ConstraintEvaluationRecord.result = not_applicable` to coexist with `constraint_applicable_to(Constraint, Context) = true`.

Because the admissibility derivation ignored that contradiction, an evaluator error could produce a more permissive result than a missing evaluation. This violated the fail-safe rules for missing or uncertain evidence.

**Resolution:**

- `not_applicable` is authoritative only when temporal or target scope does not match the context;
- for an applicable Constraint, `effective_constraint_result` cannot be `not_applicable`;
- an applicable stored `not_applicable` is normalized to `indeterminate`;
- a dedicated invariant prohibits the contradictory authoritative record;
- the counterexample is retained as an example and will become a PR-0006 regression fixture.

## Finding 2 — Advisory violation and advisory uncertainty are asymmetric

**Status:** Accepted as clarification.

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

## Finding 3 — PR-0004A and PR-0005 are bundled in PR #8

**Status:** Rejected — factually incorrect.

PR-0004A was independently approved and squash-merged before PR-0005:

```text
PR-0004A merge commit:
faacaf7aacfa29de0d4bf642036b603a96097c9b
```

PR #8 uses that commit as its base and changes only the Constraint cycle files. OCP-001, OCP-003, OCP-004 and OCP-005 corrections from PR-0004A are already present in `main` and are not part of the PR #8 diff.

The governance precedent remains valid: corrective cycles and new Concept cycles are separate unless Architecture Board explicitly approves an exception.

## Finding 4 — Concept status choreography is inconsistent

**Status:** Accepted.

Earlier Concept cycles used `Under Review` at different stages, while Constraint remained `Proposed` in a Draft PR.

**Resolution:**

OCP-001 now defines one process:

```text
Draft PR / candidate registration → Proposed
Ready for review                 → Under Review
Architecture Board approval      → Accepted before merge
Separate canonicalization PR     → Canonical
```

External or adversarial review while the PR remains Draft does not automatically change Concept status.

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

> Accept the `not_applicable` finding and the advisory/indeterminate clarification. Reject the bundling finding because PR-0004A was merged separately before PR-0005. Adopt a single Concept status choreography. Move executable validation forward as PR-0006. Do not merge PR-0005 until the accepted semantic findings are resolved and reviewed.
