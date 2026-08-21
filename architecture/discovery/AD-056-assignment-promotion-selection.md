---
Decision-ID: AD-056
Title: Assignment Canonicalization Candidate Selection
Status: Accepted
Version: 0.1.0
Owner: Architecture Board
Date: 2026-08-21
---

# Assignment Canonicalization Candidate Selection

## 1. Gate-first and authority boundary

This act records the Architecture Board's explicit selection of OCP-005 and opens only the `CANDIDATE_BOARD_SELECTION` prefix of its canonicalization cycle. The operation is governance lifecycle state, not an operational rule, result, profile or activation. It is therefore not positive-capable under OCP-016 G4 and G4 does not apply to this act. OCP-005 remains Route F; that subject classification does not turn cycle selection into semantic activation.

The exact authorized effect is `ASSIGNMENT_T6`: `CANDIDATE_BOARD_SELECTION=completed` with evidence `AD-056`, while `DOCUMENT_PROMOTION=pending` and `CONCEPT_CANONICALIZATION=pending`. No review, CI result or authorization from this step transfers to either pending step.

## 2. Complete candidate inventory and actual choice

All three current gate candidates were rederived from their live primary metadata and the schema-5 gate before selection:

| Candidate | Live state | L2 | Prior cycle | Current eligibility and disposition |
|---|---|---|---|---|
| OCP-005 | `0.4.0 / Accepted`, Assignment `Accepted` | pass; OCP-000–004 are Canonical | none | eligible; AD-055 independently establishes the subject-controlled Canonical readiness prerequisites; selected by the Board |
| OCP-006 | `0.4.0 / Accepted`, Constraint `Accepted` | fail; direct OCP-005 is not Canonical | none | ineligible now; the Canonical direct-dependency floor fails |
| OCP-010 | `1.0.1 / Canonical`, Event `Canonical` | pass | completed `EVENT_T6` | ineligible for a new cycle; schema 5 requires candidate IDs to be unique across its cycle journal |

OCP-005 is the only eligible candidate, so no convenience tie-break is used. The choice is still a Board choice: eligibility does not self-select a candidate, and the Board mandate supplies the required authority.

## 3. Identifiers, position and exact state

`ASSIGNMENT_T6` is absent from the pre-act cycle-ID set and OCP-005 is absent from the pre-act cycle-candidate set, satisfying both explicit uniqueness rules. T6 is taken from OCP-005's current candidate row. AD-055's executable schema-5 probe already established that slot labels are not unique and that a valid OCP-005 selection prefix may reuse T6 after completed `EVENT_T6`; this act consumes that evidence without rerunning a new position decision.

The gate schema remains version 5 because no vocabulary, key set, ordering rule or validity rule changes. This is a state-instance update under the existing schema, not a schema revision.

## 4. Closability in both directions

Forward closure is defined by the existing ordered protocol: a separately mandated document-promotion act may complete `DOCUMENT_PROMOTION`, then another separately mandated Concept act may complete `CONCEPT_CANONICALIZATION`; only the all-completed state clears `active_cycle_id`.

Corrective rollback is also defined. OCP-001's atomic lifecycle table requires a new reviewed PR that restores the entire agreed unit and forbids partial edit or history rewrite. For this selection, that unit is the gate, AD-056 witness, all live cycle projections, their predecessor bindings, checker/tests and derived accounting. Its predecessor is executable and valid with only completed `EVENT_T6` and `active_cycle_id: null`. Rollback therefore removes the incomplete `ASSIGNMENT_T6` state atomically while retaining Git and decision history; it does not delete or rewrite this act. A one-file gate edit is not a valid rollback.

## 5. Live projections and historical predecessors

The gate-only mutation identified seventeen readers of fifteen current projection carriers. Every reader now derives the exact two-cycle prefix from the live gate. Each changed carrier has a byte-identical pre-selection copy under `architecture/baselines/`, and `assignment-promotion-selection.yaml` records the data-owned original-path → preserved-path → SHA-256 relation. Completed acts continue to resolve their historical assertions to those bytes; no prior `baseline_*`, discovery act or reviewed-contract snapshot is rewritten.

## 6. Atomicity, versioning and rollback accounting

The atomic package contains the active ID, cycle row, selection evidence, all live projections, all historical-successor bindings, checker/tests and repository accounting. Partial effect is invalid. OCP-005 stays `0.4.0 / Accepted`; Assignment stays `Accepted`; the gate remains schema 5; AD-056 is new `0.1.0 / Governance` evidence. No data, reference, schema or runtime migration occurs.

This act does not promote OCP-005 to Canonical, canonicalize Assignment, promote or canonicalize another artifact, close any question, activate a positive model, satisfy OCP-023's completeness need, change any document version/status or Concept status, or authorize either pending step or a later act.
