---
Decision-ID: AD-021
Title: Operation Authorization Source Contract
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-010, AD-011, AD-012, OCP-001, OCP-004, OCP-006, OCP-007, OCP-009, OCP-014, OCP-015, OCP-016, OCP-017, P-001
Applies-To: AB-017
Review-After: First production-facing authorization-source proposal or evidence that the selected Route C profile/decision contract, authorizer binding, level resolution, freshness, supersession or OCP-017 integration is incomplete
---

# AD-021 — Operation Authorization Source Contract

## 1. Mandate and decision form

AB-017 asks which governed sources may authorize an Operation without prematurely introducing `Authority`, `Approval` or `Policy` as Concepts. OCP-004 and OCP-017 already establish the consumer-side boundary: entry to `Authorized` requires exact accepted evidence, but neither artifact chooses or legitimizes its source.

This act deliberately combines the previously missing discovery and one executable Draft contract in one atomic tree. It:

1. rederives the present source/consumer gap;
2. declares comparison criteria before applying them;
3. compares the no-change result and four substantive alternatives without inherited preference;
4. selects one bounded result; and
5. prepares OCP-018 `0.1.0 / Draft`, a checker rule manifest, a validator, focused tests and synthetic positive/material-negative fixtures.

The Architecture Board fixes the selection only by separately authorizing and merging the exact reviewed head. Preparation, review or CI alone is not selection or merge authority.

## 2. Exact baseline and complete anchor chain

The act starts from `main@cdf5e1af329a363132aeca28257cf187a077d0f6`, tree `3a76b26b29fc7f73ec63938a281d2f1282a62240`.

For every row below, the Git blob was resolved from the path at that commit, the path was resolved back by `git ls-tree -r` from the blob, the state was read inside the blob, and SHA-256 was recomputed from the blob bytes. Every blob resolves back to exactly the listed path.

| Input | Reverse-resolved path | Stated exact state | Git blob | SHA-256 |
|---|---|---|---|---|
| OCP-004 | `docs/004-operation-concept/README.md` | `1.0.0 / Canonical`; Operation `Canonical` | `1ff548a1f213b574472a90a8b3cfe014f6c1ce11` | `9c9173d3a3dec044e2cae2eb8fd5b66d07a106318f497a973409fedf4677155b` |
| OCP-007 | `docs/007-organization-concept/README.md` | `1.1.1 / Canonical`; Organization `Canonical` | `9b89bbac9ae08e73e2b8fbe1e85a5aec86824e33` | `eee22fbfb9580960101e9ced677625a02aec6368ccdacd2283a1b7e9946fd810` |
| OCP-009 | `docs/009-capability-concept/README.md` | `1.0.0 / Canonical`; Capability `Canonical` | `31163eacb0ca2a78b17b9d2466d99ef0c8b2d272` | `29362c815cb14f07bfd06775d1398498a27ace5ee5a4acaafde0eb39e902152a` |
| OCP-014 | `docs/014-coordination-profile/README.md` | `0.2.0 / Accepted`; explicit non-authority boundary | `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` |
| OCP-015 | `docs/015-coordination-workflow/README.md` | `0.2.0 / Accepted`; evidence without authorization/selection | `ea60634e54faedabb8c5e08b036030c2f0e4e20b` | `6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d` |
| OCP-016 | `docs/016-core-boundary/README.md` | `1.0.0 / Canonical`; Routes F/C/E/D/I | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-017 | `docs/017-operation-lifecycle/README.md` | `0.2.0 / Accepted`; authorization-evidence acceptance only | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| AD-010 | `architecture/discovery/AD-010-cross-vertical-visibility-agreement.md` | `0.3.0 / Accepted`; V0/A0 no-new-authority | `f769d9292d9f5209c8ee35366257836b1222857f` | `8a4778ba679784634d166984dd3489b87f3680f5daa8970921c67f1a8314d488` |
| AD-011 | `architecture/discovery/AD-011-state-readiness-evidence.md` | `0.3.0 / Accepted`; S0/R0 no-new-authority | `cb398157d1941eb39d2585ed02993af924ff8bd7` | `bbf2916294de1c8bdc81b9e5cbdb77856126856b0c33ad11481f9395e0b85cf2` |
| AD-012 | `architecture/discovery/AD-012-evidence-freshness-replay-boundary.md` | `0.3.0 / Accepted`; contract-local F1/A1 only | `7c0de0dc8dfe8ff333e8e5120ca31f829cbeaaa5` | `65267c41568a8c7d333bc809d9e7096ca8e03fef297700385f78f5923c11dfb5` |
| P-001 | `patterns/P-001-identified-record-pattern.md` | `0.1.0 / Accepted`; Required Elements + optional A/C | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| architecture backlog | `backlog/architecture-backlog.md` | AB-002 and AB-017 both `Open` | `ad6940c4df39d2953ecc5960a09049f77ee05c39` | `92118ced370dff5a169b7cc00746247528203a286f4b6b84dfe244092aaca9eb` |
| lifecycle validator | `tools/ontology_checker/ocp_checker/operation_lifecycle.py` | accepts opaque exact source/owner/evidence envelope; does not resolve source decisions | `b3b44fab9602d46e59586d8767635263afd3c4ab` | `77b7cf4e818815a220a1284f37ba1925bb137483c7f96aa20a76426b652e28a0` |

The anchors establish inputs. They do not select a result.

## 3. Current evidence and count correction

### 3.1 OCP-004

The case-insensitive exact token `authorization` appears on **35 lines** in OCP-004 and occurs 37 times. Those lines are not 35 independent rules. They separate into four classes:

1. negative boundaries: intent validation, provenance, spatial bindings, IO2 and hierarchy do not grant authorization;
2. delegation: OCP-017 owns lifecycle acceptance of authorization evidence;
3. unresolved questions: the source/mechanism and possible multiple sources remain open; and
4. process language about Board or merge authorization.

The normative gap is explicit in OCP-004 §§11.3, 15, 20 and the incorporated ownership ledger: an Operation may require authorization, but the external source/mechanism is separately governed and Order is only a candidate.

### 3.2 OCP-017

The technical brief's claim of 24 exact-token occurrences does **not** reproduce on the mandated base. The exact token `authorization` occurs **23 times on 21 lines**. The wider `authorize | authorized | authorization` family occurs 37 times on 32 lines.

The discrepancy does not change the decision boundary. OCP-017 §9 exact-resolves `source_contract_ref`, `source_owner_ref`, `evidence_ref`, subject, input and provenance and requires `effective / accepted`, while expressly refusing to authenticate the owner, issue an Order, grant permission or select a source by newest/order/count.

### 3.3 Accepted negative boundaries

- OCP-014 can state an exact consumer need without authorization, selection or Assignment action.
- OCP-015 proposal/response evidence never becomes authorization, approval, selection or Assignment mutation.
- AD-010 V0/A0 adds no shared visibility/agreement authority.
- AD-011 S0/R0 adds no shared State or Readiness authority.

These are accepted results, not candidates in this act. Any outcome that relies on those artifacts to issue permission is inadmissible.

## 4. Required expression surface

Every positive outcome must express all four questions without a new Concept:

1. **Who:** exact authorizer Organization and exact Capability version required by the source, without claiming an OCP-012 Organization holder.
2. **Level:** one exact source-contract-local decision level resolved by an exact rule/input when several levels exist, without inferring a universal hierarchy.
3. **Record:** one attributable decision with replayable identity or a justified existing record whose identity already owns the same semantics.
4. **Staleness:** an exact consumer-local freshness/effectivity rule in which missing, stale, ambiguous or conflicting input cannot become accepted.

OCP-017 integration is also mandatory: the result must exact-bind the existing source/owner/evidence/subject/input/provenance envelope and cannot mutate a transition itself.

## 5. Predeclared comparison criteria

Criteria are declared before outcomes are applied:

| Criterion | Required test |
|---|---|
| C1 — accepted-consumer fit | can OCP-017 resolve one exact source decision without changing its acceptance-only authority? |
| C2 — four-question expressivity | can the outcome express who, level, record and staleness without hidden defaults? |
| C3 — accepted-boundary preservation | does it preserve OCP-014/OCP-015/AD-010/AD-011 and leave AB-002 open? |
| C4 — identity and replay | can audit distinguish two decisions and reproduce historical use without newest/order/count selection? |
| C5 — fail-safe behavior | do missing, stale, ineligible, wrong-level, conflicting and denied evidence remain non-accepted? |
| C6 — OCP-016 route fit | is semantic ownership explicit, acyclic and neither over-concentrated nor empty fragmentation? |
| C7 — executable falsifiability | can every finite material obligation have checker rules and positive/material-negative fixtures? |
| C8 — migration restraint | can existing sources remain historical without invented data or automatic rebinding? |

No criterion rewards age, file centrality, prior recommendation, line count or the desire to close AB-017.

## 6. Outcome space

### A0 — no new source contract

Retain the OCP-017 acceptance envelope and leave every source entirely external. This is a complete fail-safe result: no semantics are invented. It preserves all boundaries and migration cost is zero.

Its stop is equally explicit. It cannot answer the four expression questions in Foundation, cannot exact-resolve source evidence beyond an opaque identifier and cannot add the mandated executable evidence. A0 remains legitimate if evidence cannot distinguish a positive route; current accepted consumer evidence does distinguish it.

### AO — Order-only authorization source

Define Order as mandatory or sufficient for every Operation authorization. This offers a familiar named source and may later be valid for a concrete domain.

It is inadmissible here. No accepted Order contract supplies identity, level, freshness or legitimacy. Selecting it would resolve AB-002 by implication and would treat one candidate source as universal without evidence.

### AE — evidence field on any existing governed record

Permit an existing record—Order if later available, coordination evidence, provenance, assessment or another source artifact—to carry evidence consumed directly by OCP-017. This avoids a new record family and may preserve domain-native identity.

The common outcome is under-specified. Existing records own different subjects, authorities, history and effectivity; OCP-014/OCP-015 explicitly reject permission inference, while provenance alone is non-authoritative. Without one shared decision contract the same evidence label cannot answer who/level/staleness consistently. A future exact source may still map an existing record into the selected envelope, but “any existing record” is not itself a contract.

### AD — domain-only source profiles

Keep source meaning and every decision record entirely in Route D contracts; OCP-017 consumes only their existing generic envelope. This respects legitimate domain ownership and can support Order or other sources independently.

AD is admissible but incomplete for the accepted shared consumer. Every domain would need to repeat exact subject, authorizer, level, effectivity, supersession and fail-safe OCP-017 equality rules. The repeated minimum is Foundation-owned meaning rather than private vocabulary. Leaving it ungoverned creates drift precisely at the shared lifecycle boundary.

### AC — Route C decision envelope with exact source profiles

Create one Route C non-Concept OCP-018 contract. Core owns the shared `OperationAuthorizationDecisionRecord`, exact profile/owner/subject/Organization/Capability/level bindings, effectivity, supersession and OCP-017 acceptance derivation. Each exact source profile retains its legitimate owner and domain-specific decision meaning.

The decision record invokes P-001 Modules A and C. Source profiles are versioned defining profiles, not a second record family. Order remains one possible future source; no source kind is mandatory. Finite rules receive checker coverage and synthetic negative fixtures.

## 7. Outcome-fair application

| Outcome | C1 consumer fit | C2 expression | C3 boundaries | C4 replay | C5 fail-safe | C6 route | C7 executable | C8 migration | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| A0 | opaque only | no | strong | no shared decision | opaque only | valid stop | cannot meet mandate | strongest | reject on demonstrated consumer gap |
| AO | hypothetical | incomplete | fails AB-002 | no accepted identity | undefined | unproved F/C/D | not grounded | high invention | inadmissible |
| AE | source-dependent | inconsistent | risks accepted negatives | source-dependent | inconsistent | owner conflict | no common rules | variable | reject as common contract |
| AD | generic OCP-017 fit | domain-local yes | strong | domain-local | domain-local | valid D but repeated minimum | possible only per domain | restrained | admissible alternative, not selected |
| AC | exact | yes | strong | exact A/C record | explicit | Route C + domain profiles | complete in this act | no automatic rebinding | **selected** |

The evidence distinguishes AC from AD only for the shared minimum. It does **not** distinguish legitimate real source owners, whether Order is one source, or domain-specific eligibility content. Those remain profile-owned and separately gated.

## 8. Board selection

The selected outcome is **AC — Route C decision envelope with exact source profiles**.

Selection establishes only the scope of OCP-018 `0.1.0 / Draft` in this atomic act. It does not make any source profile legitimate, authorize an Operation, change a lifecycle stage or approve production use. The Board chooses the contract form; an exact source owner remains responsible for the profile and evidence it later proposes.

If any of the following is found before merge, the result returns to A0 rather than weakening rules:

- no acyclic Route C placement;
- Organization-Capability binding requires an OCP-012 Organization holder;
- decision level requires a universal hierarchy;
- P-001 identity/effectivity/supersession cannot be mapped fully;
- stale or conflicting evidence can become accepted;
- a fixture needs real operational data; or
- the checker cannot bind every material finite rule to OCP-018.

## 9. OCP-016 authority ledger and placement

| Ledger question | AC answer |
|---|---|
| Candidate | source profile plus independently identified `OperationAuthorizationDecisionRecord`; non-Concept contract |
| Responsibility | produce one exact attributable, effective and replayable decision for one Operation that OCP-017 may accept |
| Primary route | C: shared rule/result/record meaning; not F, E, D-only or I |
| Semantic owner | OCP-018 owns the minimum envelope/derivation; exact profile owner owns legitimacy and domain meaning |
| Consumer | Accepted OCP-017 authorization-evidence acceptance at `→ Authorized` |
| Defining source | OCP-018 `0.1.0 / Draft` plus exact source profiles |
| Dependencies | Operation, Organization, Capability, OCP-017 envelope, AD-012 freshness and P-001 form |
| Evidence | human comparison plus source-bound rules, validator, focused tests and synthetic fixtures |
| Non-implications | no new Concept/edge, Order requirement, authentication, lifecycle/Assignment mutation or Readiness |
| Lifecycle | exact contract/profile versions; decision Module A/C history; no automatic migration |

Route F fails because neither source profile nor decision form is a fundamental subject and no new Concept identity is needed. Route E fails because AC owns decision meaning/result, not only interoperability. Route D-only fails because the accepted Core lifecycle consumer requires the same minimum guarantees independent of source vocabulary. Route I fails because the responsibility exists independently of storage or API shape.

Separate OCP-018 placement is preferred over inline OCP-004 because OCP-004 is already a stable Canonical Operation kernel and explicitly delegates source/mechanism. OCP-018 also depends downstream on OCP-017's envelope; inserting that responsibility into OCP-004 would reverse the existing acyclic direction. A separate bounded contract is therefore readable and semantically owned rather than empty fragmentation.

## 10. P-001 record-form decision

AE asked whether evidence on an existing record was enough. It is not enough for the shared contract because no existing accepted record owns all of these properties simultaneously:

- one independently addressable Operation decision;
- exact source owner, authorizer Organization, Capability and decision level;
- effectivity at a requested time;
- history-preserving replacement; and
- exact use as OCP-017 `evidence_ref`.

`OperationAuthorizationDecisionRecord` therefore exact-invokes unchanged `P-001@0.1.0` with Modules A and C. OCP-018 maps every Required Element and supplies invalid counterexamples. The Pattern contributes form only; source legitimacy, `authorize | deny`, level semantics and acceptance remain OCP-018/profile-owned.

The profile itself is not a P-001 record. It is an exact versioned defining contract with no instance history. This avoids inventing a second identity merely because the checker resolves a profile.

## 11. Freshness and Constraint boundary

AC activates one contract-local AD-012 F1/A1 rule: a decision is usable only inside its explicit half-open interval and with exact, unambiguous source/level/eligibility/input bindings. Missing, expired, ineligible, wrong-level, conflicting or invalid data derives `indeterminate`; stored `accepted` cannot override it.

This reuses the accepted fail-safe shape but does not change OCP-006. Constraint retains its own applicability, result vocabulary and explicit `indeterminate_disposition`. An authorization decision does not evaluate a Constraint, and a Constraint decision does not authorize an Operation.

## 12. Executable evidence delivered by the act

The atomic Draft includes:

1. `operation-authorization-rules.yaml`, with every validation/derivation ID exact-bound to OCP-018 sections;
2. a dedicated checker module and central fixture dispatch;
3. focused unit tests for exact fixture results, manifest equality and order independence;
4. a positive authorize fixture with a superseded historical denial; and
5. separate material negatives for stale evidence, ineligible authorizer, unresolved or malformed Organization/Capability evidence, malformed history, denial, wrong level, conflicting heads and prohibited mandatory-Order/concept coupling.

The fixtures mechanically prove only finite structural and derivation obligations. They do not authenticate a real owner or prove real operational permission. Those responsibilities stay outside this repository slice.

## 13. Safety boundary

All fixture and prose examples are generated specifically for this act. They use abstract synthetic identifiers, synthetic future timestamps and synthetic Capability/profile names.

The act includes no real operations, frequencies, coordinates, unit designators, people, credentials, operational windows or restricted material. Nothing is copied from another repository or project on this machine. Any future evidence that cannot remain synthetic must be reviewed outside this act and cannot be committed here.

## 14. Status, version and accounting

AD-021 is `0.1.0 / Accepted` because the merged act would be the Board's first outcome comparison and selection for AB-017. OCP-018 is `0.1.0 / Draft` because it is a new compatible Route C contract with no production-facing source or migration evidence.

No Canonical document is edited. OCP-000, OCP-002, OCP-004, OCP-007, OCP-009, OCP-016, P-001, the taxonomy, Concept graph and foundation map remain byte-identical. No `Concept-Status`, `Review-After` or existing dependency is changed.

On merge only:

- AB-017 becomes `Resolved` by AD-021 + OCP-018 Draft;
- `Operational rules and workflows` moves from 23% to 25% because a governed executable source contract now exists, while overall readiness remains `≈72%` and no T6 scope opens;
- P-001 gains one current structured invoker without editing its time-anchored T3 ledger; and
- the executable suite grows from 125 to 136 fixtures and from 191 to 201 unit tests as required.

AB-002 remains `Open`. AB-015, AB-016, AB-018, AB-020, AB-023 and AB-028 retain their statuses. No status changes by implication.

## 15. Negative boundary and non-transfer

Acceptance of this act does not:

- make Order mandatory, optional or sufficient in any exact source profile;
- create Authority, Approval, Policy, Authorization or DecisionLevel as Concepts;
- add a registry row, taxonomy class, graph edge or foundation-map node;
- make Organization an OCP-012 Capability holder;
- authenticate a source owner, authorize an actor or grant permission;
- change OCP-004, OCP-017, lifecycle history, Assignment, Constraint, Event, assessment or coordination evidence;
- repair or change any `Review-After` field;
- authorize Y10D Event discovery, a normative `Review-After` act, YR, T6 or another architecture act; or
- transfer merge authority beyond the exact reviewed head.

Every later source profile, production adoption, lifecycle integration change or status promotion requires its own explicit owner, evidence and four fresh gates.

## 16. External review questions

1. Are the OCP-004 and OCP-017 counts/classifications reproducible, including the correction from 24 to 23 exact OCP-017 occurrences?
2. Were C1–C8 declared before application, and is A0 treated as a real result?
3. Does any outcome receive hidden weight from Order familiarity, closure pressure or prior work?
4. Is Route C justified over inline OCP-004, Route D-only and Route E without creating a Concept?
5. Does Organization + Capability binding avoid an OCP-012 Organization-holder or universal hierarchy claim?
6. Is P-001 invocation required by actual identity/effectivity/supersession rather than repeated shape alone?
7. Do the checker and separate material-negative fixtures fully implement the four-question acceptance surface?
8. Can stale, denied, ineligible, wrong-level, ambiguous or conflicting evidence ever reach OCP-017 as accepted?
9. Are every anchor and reverse path exact on the mandated base?
10. Does any change resolve AB-002 or transfer authority to another act by implication?
