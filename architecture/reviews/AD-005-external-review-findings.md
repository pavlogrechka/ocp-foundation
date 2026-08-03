# AD-005 External Review Findings

- Review target: `PR #28 — AD-005 — Capability Boundary`
- Reviewed head: `cfdcdbf` (AD-005 revision `0.1.0`, Status `Under Review`)
- Review source: external adversarial boundary review provided to Architecture Board
- Review comment: PR #28 `#issuecomment-5172670262`
- Decision date: 2026-08-04
- Merge commit: `41289f4` — Architecture Board opened the Capability discovery cycle by merging revision `0.1.0` without amendments
- External review verdict: boundary survives adversarial review; findings bind the next AD-005 revision
- Findings resolution state: **Open** — to be resolved in the next AD-005 revision before the Architecture Board outcome-selection act

The Architecture Board merged the discovery revision to open the cycle, following the AD-004 precedent of iterative discovery revisions (`0.1.0 → … → acceptance act`). No outcome was selected by this merge. Findings below are not resolved by the merge and must be addressed before or together with the outcome-selection decision.

## Finding 1 — Base counterexample list is inexpressible under Outcome A

**Severity:** Moderate.

**Status:** Open — must be resolved before the Board outcome selection, because it distorts the fairness of outcome comparison.

Two items of the unconditional required-counterexample list in §12 presuppose governed identity and versioning:

- "a domain Capability reference resolves through the selected namespace and version contract";
- "changing a Capability definition does not silently reinterpret historical exact-version claims".

Outcome A by definition has neither governed identity nor a version contract ("minimal naming or reference convention", "no universal registry"). As written, either Outcome A structurally cannot satisfy the mandatory list — unfairly forcing the selection toward Outcomes B/D — or the items would be silently dropped. Both contradict the document's own principle that "an unspecified blend of outcomes is not a decision".

**Required resolution:** mark the identity/version-dependent counterexamples as conditional on outcomes with governed identity (B, C, D), and give Outcome A its own equivalent — for example, prove that cross-domain reference ambiguity is detectable and rejectable without central identity rather than remaining invisible.

## Finding 2 — Qualification ambiguity between §4 and §8

**Severity:** Minor.

**Status:** Open.

§4 states Capability is not qualification or certification; §8 lists "confidence, level or qualification where a domain requires it" among candidate claim dimensions. The positions are compatible but the boundary is implicit.

**Required resolution:** one sentence — qualification/certification may be an *evidence input* to a holder claim, but is never part of Capability identity and never creates a positive claim automatically.

## Finding 3 — Missing namespace-collision counterexample

**Severity:** Minor.

**Status:** Open.

§9 introduces namespaces, but §12 does not test the collision case: the same human-readable name in two namespaces with different semantics must remain two identities; a label match must never substitute for identity resolution.

**Required resolution:** add the counterexample to §12, conditional on governed-identity outcomes.

## Finding 4 — Holder typing inherits the open Organization ↔ Organizational Resource boundary

**Severity:** Minor (observation).

**Status:** Open.

§6 names Resource and Organization as candidate claim subjects. A Unit as Organizational Resource sits on both sides of the unresolved AB-006/AB-052 boundary: a claim issued to a "unit" would have an ambiguous subject type. The discovery must not resolve this silently.

**Required resolution:** an explicit sentence that claim-subject typing inherits the open AB-006/AB-052 boundary and will be fixed by a downstream decision, not by this discovery.

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
