---
Decision-ID: AD-043
Title: Assignment-Set Completeness Evaluator Recognition Contract
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-029, AD-036, AD-041, AD-042, OCP-001, OCP-016, OCP-023
Applies-To: OCP-024
Review-After: A separate act may accept the exact OCP-024 body; a different act grounded in external domain authority must name any real evaluator before activation
---

# AD-043 — Assignment-Set Completeness Evaluator Recognition Contract

## 1. Decision and exact outcome

Architecture Board authorizes OCP-024 `0.1.0 / Draft` as a Route D producer-independent recognition envelope. The act establishes executable necessary properties but reaches a deliberate negative limit: no real evaluator can be made legitimate from repository-internal references alone.

The only positive-looking test result is explicitly `synthetic-reference-recognized`. No completeness claim, occupancy result or Core model is activated.

## 2. Gate-first and route derivation

The classification criterion is ownership and effect, declared before choosing form:

- a Core contract would change reusable foundation meaning or a Core artifact;
- Route D owns a domain-local rule that consumes Core truth without changing Core;
- a G4 activation would make a positive-capable rule/result/profile effective for a named Accepted consumer.

The result is Route D because it recognizes domain-local evidence for OCP-023 and changes nothing in docs/000–022, the registry, taxonomy or graph. This act creates a Draft reference envelope, not an activation, so G4 does not apply to the act. Future activation remains G4-bound. OCP-023 supplies only the Accepted consumer; the activation baseline, rule version, production snapshot/context and legitimate real owner/evaluator remain absent.

## 3. Independence test before contract selection

The proposed properties were restated without a concrete producer, system, database, protocol, vendor or organization. Exact subject, exact coverage, temporal validity, provenance/authority binding, uniqueness and fail-safe behavior survive that removal, so a producer-independent envelope has an independent reason to exist: it makes admissibility and rejection mechanically distinguishable.

Actual authority does not survive. A string naming an authority basis cannot prove delegation or observational completeness. Consequently OCP-024 refuses production-shaped authority and proves only synthetic coherence. This avoids self-supplying the sixth G4 element.

## 4. Properties and their executable dispositions

| Property | Recognition condition | Invalid disposition |
|---|---|---|
| provenance/authority binding | one exact profile binds evaluator, domain, subject and authority basis | `indeterminate`; real authority unresolved |
| exact subject | Resource, evaluation time and Assignment snapshot match request | `indeterminate` |
| exact coverage | claim covers all Assignments for the Resource at the moment | `indeterminate` |
| temporal validity | profile covers evaluation time; evidence is not from the future | `indeterminate` |
| uniqueness/consistency | profile and evidence each resolve once and do not conflict | `indeterminate` |
| fail-safe | every invalid class is non-permissive | never `false`, never completeness |

The synthetic fixture shows the properties are jointly expressible. Stale, ungrounded and conflicting fixtures show that the failure boundary is operational. Activation and adjacent semantic fields are rejected.

## 5. Status and version derivation

OCP-024 is `0.1.0 / Draft`: it is the first semantic body, has not been externally reviewed as an exact accepted contract and names no real evaluator. Immediate Accepted status would require AD-029 snapshot duties and would misleadingly collapse authoring with acceptance. AD-043 itself is `0.1.0 / Accepted` because it is the first Board governance act recording the mandate and its bounded outcome; it is not the domain contract.

No existing OCP version changes. No dependency or lifecycle floor is asserted for a future acceptance or activation.

## 6. Exact baseline and anchor chain

The exact base is `main@46c822ce25ca31f99daf6168caffca67f75fe244`, tree `b7b473b5f1c84b63167ade6d0156ea9fa81e1ff9`. Each object below was resolved at that commit, reverse-resolved through `git ls-tree -r`, checked for the stated token and SHA-256 hashed over raw blob bytes.

| Artifact | Reverse-resolved path | Declared base state | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; Route D and G4 | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-023 | `docs/023-resource-occupancy/README.md` | `0.2.0 / Accepted`; direct unmet completeness token and no evaluator | `a846333fae80aff2b3697e811d2b155c91f04122` | `5ec9aca56de4524b4ab78a9e98e2cf5d7561d6f13bac8cf7778d66a99f5490d9` |
| AD-042 | `architecture/discovery/AD-042-resource-occupancy-acceptance.md` | `0.1.0 / Accepted`; consumer status without activation | `02d646d4e0c4e2abbce6bc782cfb011de04b0015` | `7c9ab64736a9c2547b77abb94069e62672c5a8cb09532b061eeb7e3aec06520c` |
| need projection | `architecture/consumer-need-discovery.yaml` | schema 2; exactly one live need | `bcde824ae979e2ebf46ffaaa39967b015b92d618` | `ed22ad35fac0f9c29663a789488b93d8fe20eb4762abf2428635b665dd7029a3` |
| occupancy module | `tools/ontology_checker/ocp_checker/resource_occupancy.py` | partial occupancy derivation; synthetic completeness reference only | `3d7ee96ac0d9f51cb04fd860cb5117806b422549` | `a44caaa19f1964e72b3c97f23175fa65695ce3b95e54f4b6f76fdf6bf96658c3` |
| occupancy manifest | `tools/ontology_checker/resource-occupancy-rules.yaml` | OCP-023 rule ownership | `32e7ac535b6a24fc30784deee59411597725998d` | `16cf4094dff5775e34731862dafc3b455b6b31eac0d17733d7fd3496ca06e496` |

## 7. Protection, accounting and safety

Core docs/000–022, patterns, graph, registry, taxonomy, promotion gates, P-001, OCP-023, existing fixtures, reviewed snapshots and historical baseline objects remain byte-identical to the base. Tests enforce the protected baseline and reverse-resolved anchor chain.

Current numeric accounting is derived from live files. The act adds one Draft OCP, one Accepted governance act, one isolated manifest/module and synthetic fixtures/tests; it changes no current Concept or P-001 count.

Fixtures use only `R-001`, synthetic references and the mandated synthetic time. They contain no real operation, location, unit, person, credential or producer identity.

## 8. Non-transfer and rollback

This act does not accept OCP-024, name or authorize a real evaluator, activate assignment-set completeness or resource occupancy, modify OCP-023/OCP-005, remove Assignment blockers, introduce a Concept, change status, select a candidate, start a promotion cycle, resolve AB-018/AB-005 or authorize a later act.

Rollback removes the new document, decision, module, manifest, tests, fixtures and current projections as one unit. Exact-head Fable review, Codex adjudication, green CI, explicit Pavlo authorization and squash merge remain required before this decision is effective.
