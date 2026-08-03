# AD-005 External Review Findings

- Review target: `PR #28 — AD-005 — Capability Boundary`
- Reviewed head: `cfdcdbf` (AD-005 revision `0.1.0`, Status `Under Review`)
- Review source: external adversarial boundary review provided to Architecture Board
- Initial review comment: PR #28 `#issuecomment-5172670262`
- Repeated verification comment: PR #30 `#issuecomment-5172884216`
- Decision date: 2026-08-04
- Merge commit: `41289f4` — Architecture Board opened the Capability discovery cycle by merging revision `0.1.0` without amendments
- Review-resolution merge: `890c1ee` — AD-005 revision `0.2.0`
- External review verdict: boundary survives adversarial review; findings F1–F4 are resolved and externally verified
- Findings resolution state: **Resolved and externally verified**

The Architecture Board merged the discovery revision to open the cycle, following the AD-004 precedent of iterative discovery revisions (`0.1.0 → … → acceptance act`). AD-005 v0.2.0 addressed all findings in one review-resolution revision. Repeated external verification on the exact reviewed head approved closure of F1–F4 and declared the boundary ready for the Architecture Board outcome-selection act.

## Finding 1 — Base counterexample list is inexpressible under Outcome A

**Severity:** Moderate.

**Status:** Resolved and externally verified in AD-005 v0.2.0.

Two items of the unconditional required-counterexample list in §12 presupposed governed identity and versioning:

- "a domain Capability reference resolves through the selected namespace and version contract";
- "changing a Capability definition does not silently reinterpret historical exact-version claims".

Outcome A by definition has neither governed identity nor a version contract ("minimal naming or reference convention", "no universal registry"). As originally written, either Outcome A structurally could not satisfy the mandatory list — unfairly forcing selection toward Outcomes B/D — or the items would have been silently dropped. Both contradicted the document's own principle that "an unspecified blend of outcomes is not a decision".

**Resolution in v0.2.0:** the unconditional list now contains only claim semantics common to outcomes that support holder claims. Namespace and exact-version counterexamples are conditional on Outcomes B, C and D. Outcome A must independently prove that cross-domain ambiguity is detected and rejected without central governed identity.

**Repeated verification:** approved in PR #30 `#issuecomment-5172884216`; outcome fairness is restored without dropping either governed-identity obligation.

## Finding 2 — Qualification ambiguity between §4 and §8

**Severity:** Minor.

**Status:** Resolved and externally verified in AD-005 v0.2.0.

§4 states Capability is not qualification or certification; §8 listed "confidence, level or qualification where a domain requires it" among candidate claim dimensions. The positions were compatible but the boundary was implicit.

**Resolution in v0.2.0:** §8 now states that qualification, certification or accreditation may be evidence input under a domain rule, but are never part of Capability identity and never create an authoritative positive claim automatically.

**Repeated verification:** approved in PR #30 `#issuecomment-5172884216`.

## Finding 3 — Missing namespace-collision counterexample

**Severity:** Minor.

**Status:** Resolved and externally verified in AD-005 v0.2.0.

§9 introduced namespaces, but §12 did not test the collision case: the same human-readable name in two namespaces with different semantics must remain two identities; a label match must never substitute for identity resolution.

**Resolution in v0.2.0:** §12 adds a governed-identity counterexample requiring equal labels in different namespaces to remain distinct identities; label equality cannot substitute for identity resolution.

**Repeated verification:** approved in PR #30 `#issuecomment-5172884216`.

## Finding 4 — Holder typing inherits the open Organization ↔ Organizational Resource boundary

**Severity:** Minor (observation).

**Status:** Resolved and externally verified in AD-005 v0.2.0.

§6 names Resource and Organization as candidate claim subjects. A Unit as Organizational Resource sits on both sides of the unresolved AB-006/AB-052 boundary: a claim issued to a "unit" would have an ambiguous subject type. The discovery must not resolve this silently.

**Resolution in v0.2.0:** §6 explicitly inherits AB-006/AB-052 and requires the downstream Capability decision to bind Organization, Organizational Resource or an explicit mapping without identity collapse.

**Repeated verification:** approved in PR #30 `#issuecomment-5172884216`.

## Review-resolution revision

- AD-005 revision: `0.2.0`
- Resolution scope: F1–F4
- Outcome selected by the review-resolution revision: none
- Concept graph impact: none
- P-001 invocation: none
- Repeated external verification: complete and approved
- Required next gate: Architecture Board outcome-selection act

## Verified positives

- The three-layer boundary definition / claim / current-usability is consistent throughout the document and aligned with the OCP-004/OCP-006 fail-safe precedents.
- The default "no inheritance, aggregation or transitive possession" is explicit.
- The AD-002 guardrail `Capability ≠ Readiness` is preserved.
- The registry boundary (§9) correctly blocks Core from becoming a catalog of domain labels.
- The outcome space covers all five options of §2; the sequenced-outcome contract mirrors AD-004 §5.
- Falsification targets §14 items 1–7 and 11–13 are covered by §12 counterexamples.
- Frontmatter, artifact identifiers and the AB-004 `Open → Discovery` transition passed the artifact-governance checker; CI was green on the reviewed head and after merge to `main`.

## External reviewer verdict

> Findings F1–F4 are closed at the boundary-text and evidence-contract level. AD-005 v0.2.0 is ready for the Architecture Board outcome-selection act. From the external reviewer position, head `7ba79d3` is approved.
