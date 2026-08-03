# AD-005 External Review Findings

- Review target: `PR #28 — AD-005 — Capability Boundary`
- Reviewed head: `cfdcdbf` (AD-005 revision `0.1.0`, Status `Under Review`)
- Review source: external adversarial boundary review provided to Architecture Board
- Review comment: PR #28 `#issuecomment-5172670262`
- Decision date: 2026-08-04
- Merge commit: `41289f4` — Architecture Board opened the Capability discovery cycle by merging revision `0.1.0` without amendments
- External review verdict: boundary survives adversarial review; findings bind the next AD-005 revision
- Findings resolution state: **Addressed in AD-005 v0.2.0 — pending repeated external verification before the Architecture Board outcome-selection act**

The Architecture Board merged the discovery revision to open the cycle, following the AD-004 precedent of iterative discovery revisions (`0.1.0 → … → acceptance act`). No outcome was selected by this merge. AD-005 v0.2.0 addresses all findings in one review-resolution revision; closure remains subject to repeated external verification.

## Finding 1 — Base counterexample list is inexpressible under Outcome A

**Severity:** Moderate.

**Status:** Addressed in AD-005 v0.2.0 — pending repeated external verification.

Two items of the unconditional required-counterexample list in §12 presuppose governed identity and versioning:

- "a domain Capability reference resolves through the selected namespace and version contract";
- "changing a Capability definition does not silently reinterpret historical exact-version claims".

Outcome A by definition has neither governed identity nor a version contract ("minimal naming or reference convention", "no universal registry"). As written, either Outcome A structurally cannot satisfy the mandatory list — unfairly forcing the selection toward Outcomes B/D — or the items would be silently dropped. Both contradict the document's own principle that "an unspecified blend of outcomes is not a decision".

**Resolution in v0.2.0:** the unconditional list now contains only claim semantics common to outcomes that support holder claims. Namespace and exact-version counterexamples are conditional on Outcomes B, C and D. Outcome A must independently prove that cross-domain ambiguity is detected and rejected without central governed identity.

## Finding 2 — Qualification ambiguity between §4 and §8

**Severity:** Minor.

**Status:** Addressed in AD-005 v0.2.0 — pending repeated external verification.

§4 states Capability is not qualification or certification; §8 lists "confidence, level or qualification where a domain requires it" among candidate claim dimensions. The positions are compatible but the boundary is implicit.

**Resolution in v0.2.0:** §8 now states that qualification, certification or accreditation may be evidence input under a domain rule, but are never part of Capability identity and never create an authoritative positive claim automatically.

## Finding 3 — Missing namespace-collision counterexample

**Severity:** Minor.

**Status:** Addressed in AD-005 v0.2.0 — pending repeated external verification.

§9 introduces namespaces, but §12 does not test the collision case: the same human-readable name in two namespaces with different semantics must remain two identities; a label match must never substitute for identity resolution.

**Resolution in v0.2.0:** §12 adds a governed-identity counterexample requiring equal labels in different namespaces to remain distinct identities; label equality cannot substitute for identity resolution.

## Finding 4 — Holder typing inherits the open Organization ↔ Organizational Resource boundary

**Severity:** Minor (observation).

**Status:** Addressed in AD-005 v0.2.0 — pending repeated external verification.

§6 names Resource and Organization as candidate claim subjects. A Unit as Organizational Resource sits on both sides of the unresolved AB-006/AB-052 boundary: a claim issued to a "unit" would have an ambiguous subject type. The discovery must not resolve this silently.

**Resolution in v0.2.0:** §6 explicitly inherits AB-006/AB-052 and requires the downstream Capability decision to bind Organization, Organizational Resource or an explicit mapping without identity collapse.

## Review-resolution revision

- AD-005 revision: `0.2.0`
- Resolution scope: F1–F4 only
- Outcome selected: none
- Concept graph impact: none
- P-001 invocation: none
- Required next gate: repeated external adversarial review of the exact v0.2.0 head

## Verified positives

- The three-layer boundary definition / claim / current-usability is consistent throughout the document and aligned with the OCP-004/OCP-006 fail-safe precedents.
- The default "no inheritance, aggregation or transitive possession" is explicit.
- The AD-002 guardrail `Capability ≠ Readiness` is preserved.
- The registry boundary (§9) correctly blocks Core from becoming a catalog of domain labels.
- The outcome space covers all five options of §2; the sequenced-outcome contract mirrors AD-004 §5.
- Falsification targets §14 items 1–7 and 11–13 are covered by §12 counterexamples.
- Frontmatter, artifact identifiers and the AB-004 `Open → Discovery` transition passed the artifact-governance checker; CI was green on the reviewed head.

## External reviewer verdict

> The definition / claim / current-usability boundary survives adversarial review. Finding 1 must be corrected before the Board outcome selection; Findings 2–4 are editorial and suitable for the same revision. With those amendments, AD-005 is ready for the Architecture Board outcome decision from the external reviewer position.
