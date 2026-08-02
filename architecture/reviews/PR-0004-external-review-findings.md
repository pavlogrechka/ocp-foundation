# PR-0004 External Review Findings

- Review target: `OCP-005 — Assignment Concept`
- Review source: external Opus 5 review provided to Architecture Board
- Decision date: 2026-08-02
- Resolution PR: `PR-0004A — Enforce Assignment Lifecycle Consistency`

## Finding 1 — One-way `terminal_at` invariant

**Status:** Accepted — critical.

OCP-005 required `terminal_at` for Closed or Revoked Assignment but did not prohibit the field for Established Assignment. Because `assignment_effective_at` trusted this field, a structurally valid Established record could silently stop producing participation without a lifecycle transition.

**Resolution:**

- transition history is the authoritative lifecycle source;
- `terminal_at` exists if and only if history ends with `Established → Closed` or `Established → Revoked`;
- a materialized value must equal the terminal transition timestamp;
- derivation reads the transition-derived projection, not an independent field.

## Finding 2 — One-way `established_at` invariant

**Status:** Accepted.

Draft Assignment could contain `established_at` even though Establishment had not occurred.

**Resolution:**

- `established_at` exists if and only if history contains the unique `Draft → Established` transition;
- the value equals that transition timestamp;
- Assignment cannot be effective before `established_at`.

## Finding 3 — Transition history and materialized fields were not consistent

**Status:** Accepted.

Nothing required `lifecycle_stage`, `established_at`, `terminal_at` and establishment provenance to agree with AssignmentTransitionRecord. Conflicting transitions such as both `Draft → Established` and `Draft → Cancelled` were not prohibited.

**Resolution:**

- Assignment transition history is a single linear path;
- mutually exclusive and branching transitions are prohibited;
- lifecycle stage and timestamps are deterministic projections;
- timestamps are ordered and tied to their source transition records;
- pattern registered as AB-031 for later application to Operation lifecycle.

## Finding 4 — Unclassified normative supersession statement

**Status:** Accepted.

The statement that a superseded Assignment must be Closed or Revoked was normative prose outside Business Rules and did not address deliberate overlap or gap during replacement.

**Resolution:**

- supersession itself has no lifecycle or temporal effect;
- an explicit Business Rule requires a terminal transition under replacement policy;
- timing, overlap and gap are deferred to Constraint or amendment rules.

## Finding 5 — Participation derivation duplicated in three documents

**Status:** Accepted.

OCP-003, OCP-004 and OCP-005 contained independent copies of the same normative formula.

**Resolution:**

- OCP-005 §§8–9 are the sole defining location;
- OCP-003 and OCP-004 contain references only;
- OCP-001 requires one defining location for every normative rule;
- linter coverage registered as AB-032.

## Finding 6 — Direct commits to `main`

**Status:** Accepted as a process control failure.

The accidental placeholder and its immediate revert left two direct commits in `main`, despite the governance rule requiring branch and PR review.

**Resolution:**

- OCP-001 now requires mechanical enforcement through GitHub Ruleset or branch protection;
- required controls are tracked in AB-033;
- the available GitHub connector does not expose ruleset configuration, so repository settings remain an explicit administrative action.

## Architecture sequence decision

**Status:** Accepted.

The next fundamental Concept cycle is `Constraint`, not the review of ADR-DRAFT-007.

Reasons:

1. State and Readiness review conditions are not yet fully satisfied by Canonical Operation and Assignment descriptions.
2. Assignment conflict, exclusivity, capacity, multiple roles and replacement timing depend on Constraint.
3. Constraint provides evidence for deciding whether availability and readiness require independent fundamental State semantics.

Tracked as AB-034.

## Architecture Board decision

> Findings accepted. OCP-005 must prevent lifecycle fields from independently changing participation derivation, make transition history authoritative, classify supersession obligations, retain one normative home for derivation rules, and require mechanical protection of `main`. Constraint is the next Concept cycle before ADR-DRAFT-007 review.
