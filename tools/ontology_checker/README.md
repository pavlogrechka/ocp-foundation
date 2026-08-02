# Executable Ontology Checker

This directory contains the first executable reference slice for OCP Foundation.

The checker is **not** a production validator, persistence schema, policy engine, or independent normative source. OCP documents remain authoritative. Code in this directory implements a deliberately limited subset of rules from OCP-003 through OCP-006 so that accepted counterexamples can become repeatable tests.

## Current scope

Implemented validators:

- Resource: identity and classification presence;
- Operation: identity and the accepted non-Draft intent gate subset;
- Assignment: authoritative linear transition history, materialized lifecycle projections, required Established-lineage fields, applicability interval, and supersession self-reference;
- Constraint: authoritative linear transition history, materialized lifecycle projections, target/predicate/enforcement completeness, validity interval, evaluation uniqueness, and contradictory `not_applicable` detection.

Implemented reference derivations:

- `assignment_effective_at`;
- `derived_participates_in`;
- `constraint_effective_at`;
- `constraint_applicable_to`;
- `effective_constraint_result`;
- `constraint_blocks`;
- `constraint_set_decision`.

## Regression fixtures

The initial suite includes:

- an Established Assignment with a materialized `terminal_at` but no terminal transition;
- an applicable Constraint with a stored `not_applicable` result;
- advisory uncertainty producing `review_required`, not `inadmissible`.

The `not_applicable` case intentionally tests two independent layers:

1. validation reports `CONSTRAINT_NOT_APPLICABLE_CONTRADICTION`;
2. derivation still normalizes the stored result to `indeterminate`.

This defense-in-depth is intentional.

## Fixture contract

Each YAML fixture contains:

```yaml
case_id: stable-test-id
concept: Resource | Operation | Assignment | Constraint
expected:
  valid: true | false
  error_codes: []
entity: {}
contexts: [] # optional; used by Constraint fixtures
```

The fixture format is a reference test contract, not an implementation-facing API schema.

## Run locally

```bash
python -m pip install -r tools/ontology_checker/requirements.txt
python -m unittest discover -s tools/ontology_checker/tests -v
python tools/ontology_checker/check.py tools/ontology_checker/fixtures
```

## Explicitly deferred

This slice does not yet provide:

- a complete machine-readable Concept registry;
- cross-file uniqueness and graph-wide acyclicity checks;
- full Operation lifecycle validation;
- a Constraint expression language or production evaluator interface;
- quantity, capacity, geometry, spectrum, authorization, Conflict, Risk, Readiness, or State semantics;
- database, API, or UI contracts.

Every additional rule must cite its defining OCP document and arrive with positive and negative fixtures where expressible.
