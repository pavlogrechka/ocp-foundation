---
Review-ID: REVIEW-PR-0003-EXTERNAL
Subject: PR-0003 — Define Operation Concept
Status: Resolved in PR-0003A
Reviewer: External review / Claude Opus 5
Owner: Architecture Board
Review-Date: 2026-08-02
---

# PR-0003 External Review Findings

## Finding 1 — Participation invariant was tautological

**Status:** Accepted.

OCP-003 and OCP-004 quantified an undefined “participation relationship” while the model represented participation only through Assignment. The rule therefore either repeated its own derivation or depended on an undefined direct edge.

**Resolution:**

- removed the mirrored participation statements from Invariants;
- defined participation through Assignment as a Semantic Rule and provisional derivation rule;
- explicitly stated that Core does not define an authoritative direct Resource-to-Operation participation edge;
- deferred Assignment cardinality, validity and temporal semantics to OCP-005.

## Finding 2 — Intent invariant allowed structurally non-empty placeholders

**Status:** Accepted.

A raw non-empty string could satisfy the former invariant without expressing a meaningful intent.

**Resolution:**

- replaced the raw string alternative with a local ExplicitIntentRecord;
- required normalized text with at least one letter or digit;
- required a passed validation result, validation rule reference and validation time outside Draft;
- separated Core structural validation from domain semantic validation.

## Finding 3 — Lifecycle transition source lacked a contract

**Status:** Accepted.

The former invariant required a source field without defining its structure or how a linter could validate it.

**Resolution:**

- defined a local LifecycleTransitionRecord;
- replaced the ambiguous source with a non-empty provenance_ref;
- clarified that provenance may reference an Event, Order, rule, decision, system action or other evidence without introducing a new fundamental Concept;
- added a corresponding structural invariant.

## Finding 4 — Operation status was not synchronized after approval

**Status:** Accepted.

Operation remained Under Review in OCP-000 and OCP-002 after Architecture Board approval and merge of PR-0003.

**Resolution:**

- changed Operation status to Accepted in OCP-000 and OCP-002;
- added Concept-Status: Accepted to OCP-004;
- added Concept-Status metadata to OCP-003 for consistency;
- strengthened OCP-001 with mandatory registry and defining-document synchronization rules.

## Governance outcome

The review demonstrated that invariant validation and Concept status synchronization must be applied during every Concept cycle, not only documented as future governance goals. PR-0003A applies these rules to the first cycle after their introduction.
