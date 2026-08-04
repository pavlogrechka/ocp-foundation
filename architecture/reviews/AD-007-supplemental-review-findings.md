# AD-007 Supplemental Review Findings

- Review target: `AD-007 — Capability Claim Boundary`, revision `0.1.0`
- Basis: accepted AD-005C holder-record mandate, OCP-009 definition/claim separation and P-001 identified-record boundary
- Discovery merge: `6e8bd40`
- Initial review-record merge: `ef4ac9f`
- Supplemental review date: 2026-08-04
- Repeated verification comments: PR #41 `#issuecomment-5175339679`, `#issuecomment-5175367766`
- Review-resolution head: `1cf2a6e` — AD-007 revision `0.2.0`
- Findings resolution state: **Resolved and externally verified**

This supplemental record captures a governance defect identified after the original PR #39 external review and the pure Review-record merge in PR #40. It does not rewrite `#issuecomment-5175036101` or imply that the original reviewer recorded this finding. It supplies distinct provenance for the additional review result.

## Finding 3 — AD-007 silently reopens the accepted AD-005C holder-record mandate

**Severity:** Major — governance.

**Status:** Resolved and externally verified in AD-007 v0.2.0.

AD-005C selected Outcome D and established that a holder-specific Capability claim remains a separate identified record binding one subject to one exact Capability definition under governed conditions, provenance, evidence and temporal applicability. P-001 invocation remained optional and separately governed, but separate claim-record identity did not.

AD-007 revision `0.1.0` repeats that mandate in §1, then reopens it without an explicit superseding act:

- §2 asks whether a stored holder claim is needed at all;
- Outcome A avoids a separate record in favor of a Resource-local attribute or reference;
- Outcome E stores no standing holder claim record and permits a derived-only view;
- Outcome F does not explicitly require domain-owned claims to retain separate identified-record identity.

Storage location and materialization are implementation choices, so a Resource-local or derived representation can conform only when it implements the same separate identified-record semantic contract: stable claim identity, exact Resource and Capability endpoints, provenance, authority, history or replay and fail-safe validation. A direct attribute, unidentified current view or evidence set that replaces claim identity contradicts AD-005C.

**Required resolution:** constrain every admissible AD-007 outcome to the accepted separate identified-record mandate; reformulate A and E as storage/materialization variants with independent stable claim identity; require F to use domain-owned identified claim records behind the Core envelope; and treat pure attribute/no-record forms only as rejected falsification controls. If the Architecture Board wishes to select a model without separate claim identity, it must first reopen and supersede AD-005C explicitly with new evidence and external review.

## Review-resolution verification

AD-007 revision `0.2.0` provides the required correction by:

- stating the controlling AD-005C mandate in §§1–2 and §14;
- reframing A and E as identified-record materialization variants;
- constraining F to domain-owned identified claim records;
- adding mandate-reopening falsification and exit criteria;
- preserving P-001 as optional until a downstream normative owner invokes it completely.

Repeated external review of exact head `1cf2a6e93a77a9d978dbfe93b9cc533aa90aa149` confirmed Finding 3 as a Major governance finding, verified its resolution and returned **Approved for Architecture Board outcome comparison**. No Capability Claim outcome is selected by this verification.
