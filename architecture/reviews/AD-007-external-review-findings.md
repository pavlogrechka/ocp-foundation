# AD-007 External Review Findings

- Review target: `PR #39 — PR-0014 — Open Capability Claim Boundary Discovery`
- Reviewed head: `4c9d4f9` (AD-007 revision `0.1.0`, Status `Discovery`)
- Review source: external adversarial boundary review provided to Architecture Board
- Review comment: PR #39 `#issuecomment-5175036101`
- Decision date: 2026-08-04
- Merge commit: `6e8bd40` — Architecture Board opened the Capability Claim discovery cycle by merging revision `0.1.0` without amendments
- External review verdict: boundary survives adversarial review; findings bind the next AD-007 revision
- Findings resolution state: **Open** — to be resolved in the next AD-007 revision before the Architecture Board outcome-selection act

The Architecture Board merged the discovery revision to open the cycle, following the AD-005/AD-006 precedent of iterative discovery revisions. No outcome was selected by this merge. Findings below are not resolved by the merge and must be addressed before or together with the outcome-selection decision.

## Finding 1 — §18 counterexample list is unconditional: third recurrence of the outcome-fairness defect

**Severity:** Moderate.

**Status:** Open — must be resolved before the Board outcome selection.

The §18 list is presented unconditionally ("a downstream normative cycle must prove"), but several items are inexpressible under part of the admissible outcomes:

- "withdrawal or expiry does not create a negative claim" — under **E (derived-only)** no stored claims exist, hence no withdrawal; under **A (Resource-local attribute)** history-preserving withdrawal is itself an open question of the outcome;
- "supersession … does not rewrite historical claims" — under E there is no supersession lineage; the equivalent is reproducibility of historical conclusions from snapshots (the R5-form from AD-006);
- "selected P-001 manifests exactly cover …" — under A/E/F P-001 may not be invoked at all;
- "one Resource may have a claim for v1 but not v2" — under F this is a domain demonstration, not a Core fixture.

This is the same structural defect resolved in AD-005 v0.2.0 (F1) and AD-006 v0.2.0 (F1). Neither §20 nor §21 of AD-007 carries the falsification target and exit criterion that AD-006 v0.2.0 institutionalized.

**Required resolution:** apply the AD-006 §16.1–16.3 structure to §18 (unconditional core + outcome-conditional blocks + explicit equivalents for non-record outcomes: detect-and-reject for F, snapshot replayability for E); add the falsification target "evidence obligations assume a layer rejected by the selected outcome" and the outcome-fairness exit criterion.

**Systemic recommendation:** since the defect recurred three times, the outcome-fair evidence structure should enter the discovery-document template itself (candidate: a sentence in OCP-001 «Виконувана валідація» or artifact-taxonomy notes), so future ADs are born with it by default.

## Finding 2 — Outcome matrix omits the "extend OCP-011 target contract" option

**Severity:** Moderate.

**Status:** Open — must be resolved before the Board outcome selection, because it distorts the fairness of outcome comparison.

Outcome C honestly flags the risk of "duplicating OCP-011 without sharing its Objective-only target contract", but the matrix lacks the cheapest assessment-path alternative: **extending accepted OCP-011** with a new target kind (e.g. `capability-holder@1` alongside `objective@1`) instead of a new record family. OCP-011 §4 is designed as an extensible governed vocabulary; this option differs materially from C in the number of contracts, manifests and the shape of the authoritative projection for AB-011. The Board cannot fairly compare C and D without seeing the reuse variant.

**Required resolution:** either a separate Outcome C′ ("claim assessment as an extension of the OCP-011 target/evidence contract") or an explicit sub-question inside C with the obligation to compare both forms externally and a selection criterion: a separate record family is justified only if claim-assessment semantics demonstrably do not fit the OCP-011 evidence matrix without diluting it.

## Verified positives

- Seventeen semantic layers (§3) — the most complete boundary map to date, consistently carried through §§4–13.
- Polarity discipline (§6): `no claim ≠ negative ≠ withdrawn ≠ expired`, `conflicting ≠ latest wins` — exact and explicit.
- Authority boundary (§7) with `claimant/evaluator/authority` separation and "provenance alone must not silently prove authority".
- Temporal semantics (§9) name the `reference_time` trap; §10 keeps withdrawal ≠ negative claim and branching without a winner.
- No-inheritance defaults (§12) and the AB-011 boundary (§16, `Resource A ≠ Resource B`) are explicit.
- Falsification targets 16–18 (simultaneous contradictory claims, overlap-manufactured positive, unresolved refs fail-closed) are strong additions.
- Frontmatter, AB-057 accounting and the full checker run passed; CI was green on the reviewed head and after merge.

## External reviewer verdict

> The claim-layer boundary is the most carefully drawn discovery so far. Both findings are structural, not semantic: F1 closes with the established AD-006 pattern, F2 with adding the reuse option to the matrix. With those amendments, AD-007 is ready for external outcome comparison and the Architecture Board decision.

## Resolution candidate tracking

AD-007 revision `0.2.0` proposes the following resolution for repeated external verification:

- F1: §18 is split into an unconditional claim-contract core and explicit representation-conditional evidence, including snapshot replayability for derived materialization, domain/Core fixture ownership for Outcome F and P-001 obligations only when invoked;
- F2: Outcome C-prime compares extension of the accepted OCP-011 target/evidence contract against a dedicated CapabilityAssessmentRecord and names target, conclusion-profile, evidence-kind and projection fit criteria;
- the systemic recommendation is implemented in OCP-001 revision `0.7.0` as a general outcome-fair discovery-evidence rule.

F1 and F2 remain **Open** until external review verifies the exact AD-007 revision `0.2.0` head. This tracking section records a proposed resolution; it does not close either finding or select an outcome.
