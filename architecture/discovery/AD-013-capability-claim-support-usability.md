---
Decision-ID: AD-013
Title: Capability Claim Support Usability Activation Boundary
Version: 0.1.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-005, AD-007, AD-008, AD-012, OCP-001, OCP-009, OCP-010, OCP-011, OCP-012, OCP-013, P-001
Applies-To: AB-060, CapabilityClaimRecord support freshness, ambiguity and replay
Review-After: external boundary review and outcome-fair evidence comparison
---

# AD-013 — Capability Claim Support Usability Activation Boundary

## 1. Trigger and purpose

OCP-011 `0.3.0` completed the first contract-local F1/A1 activation selected by AD-012B. OCP-012 remains deliberately unchanged: `stale`, `ambiguous`, `conflicting` and `sufficient` are attributable support statements, while only `declared`/`missing`, exact snapshots and finite structure are checked mechanically.

OCP-012 is the next useful comparison because it differs materially from OCP-011:

- it records one claimant's attributable proposition, not an independent assessment;
- `declared` may have no evidence set and remains usable only as “the claimant said this”;
- evidence-backed support and declaration-only authority coexist in one claim kind;
- the record has `recorded_at` and Module A effectivity, but no separate support-evaluation time;
- OCP-013 may consume the fail-safe claim projection, but matching claims still do not establish Resource interchangeability.

This discovery asks whether OCP-012 has enough legitimate authority for its own F1/A1 activation and, if so, which claim-kind and time boundary can express it without turning support into Capability truth, assessment, Readiness or authorization.

Revision `0.1.0` does not amend OCP-012, select an outcome, define a duration, introduce a rule identifier, add checker code or change AB-060 beyond `Discovery` accounting.

## 2. Inherited mandates

AD-005C, AD-007C and OCP-012 require:

- a holder-specific Capability claim remains a separate identified record;
- the initial direct holder is only exact `resource@1`;
- Capability binding remains exact to the OCP-009 namespace, identity and version;
- claim authority is attributable and does not independently verify possession;
- withdrawal is not a negative assertion;
- branching history remains visible;
- matching claims do not collapse Resource identities or decide AB-011 interchangeability.

AD-012B additionally requires:

- F1 contract-local ownership for any positive machine-derived freshness semantics;
- A1 only for dimensions the consuming contract can actually decide;
- F0/A0 wherever no separately reviewed activation exists;
- inline historical classification plus an explicit-time derived query as separate roles;
- no universal evidence lifetime, wall-clock fallback, newest-rule lookup or standing freshness property on evidence;
- a separate usability record only after a new Board reopening and independent-identity evidence.

AD-013 may specialize these mandates for OCP-012. It may not reopen them silently.

## 3. Current OCP-012 support contract

The current claim kind is exact `holder-capability@1`. One record binds claimant, Resource, exact Capability version, condition set, assertion, evidence snapshot, support state, authority, effectivity, recording time and provenance.

Current support states are:

```text
declared
sufficient
missing
stale
ambiguous
conflicting
```

`declared` means a direct attributable declaration without a separate evidence set. `sufficient` means the recorder attributes sufficient support; it does not mean independently verified Capability possession. Every non-permissive support state projects only `indeterminate`.

The present record has no field that means “the support rule was evaluated at this time.” These existing times have other owners:

| Existing time | Governed meaning | Why it cannot be silently reused |
|---|---|---|
| `effective_from` / `effective_until` | when the claimant proposition applies under P-001 Module A | claim effectivity is not evidence freshness |
| `recorded_at` | when the claim record was created | recording time is not evaluation time or evidence occurrence time |
| `as_of_time` in a projection query | which claim heads are applicable for that query | it may support a new derived view but cannot manufacture a historical inline evaluation time |
| Event `occurred_at` | occurrence time | it is evidence-kind data, not claim evaluation time |
| ObservationRecord `observed_at` | observation time | it is distinct from observation recording and claim recording |
| OutcomeAssessmentRecord `evaluated_at` | assessment evaluation time | its freshness for one assessment does not automatically transfer to claim support |

## 4. Decision questions

AD-013 must answer:

1. Is the protected use OCP-012's own `effective_capability_claim` support projection, a downstream consumer such as OCP-013, or both under separate exact rules?
2. Does an activated historical claim need an explicit `support_evaluated_at`, or is there another already-governed exact evaluation-time owner?
3. Should declaration-only and evidence-backed claims remain modes of one exact claim kind or use separate governed claim kinds?
4. Which temporal fact is admissible for each existing evidence kind?
5. Which reference, lineage, temporal or semantic-classification ambiguity dimensions can OCP-012 decide mechanically?
6. How does a later explicit query derive current support usability without changing the historical claim or consulting current data?
7. Can OCP-013 safely consume an activated OCP-012 projection without inheriting its rule as an interchangeability or authorization rule?

## 5. Terms that must remain distinct

| Term | Meaning here | Not implied |
|---|---|---|
| claim effectivity | whether the claimant proposition applies at query time | evidence freshness or truth |
| support usability | whether exact support can protect one exact attributable claim projection under one exact rule | Capability possession, certification or Readiness |
| declaration-only claim | attributable proposition with no external evidence set | missing evidence defect or independent verification |
| evidence-backed claim | proposition that exact-binds an evidence snapshot | objective truth or sufficient support automatically |
| support evaluation time | explicit time at which the claim-support rule was applied | claim `recorded_at`, `effective_from` or current wall clock |
| downstream evaluation time | explicit time owned by a consuming contract such as OCP-013 | permission to rewrite OCP-012 history |
| fresh support | support passes one exact temporal-usability rule | true assertion, reliable source, available Resource or positive eligibility |
| stale support | support is unusable for the exact temporal use | false or negative claim |

## 6. Authority gaps

Before a positive activation, all of the following must have legitimate owners:

| Binding or conclusion | Current owner or gap | Fail-safe obligation |
|---|---|---|
| protected projection | OCP-012 attributable projection exists; activation use is unselected | a caller cannot nominate itself as owner |
| declaration/evidence mode | OCP-012 support-state vocabulary | no evidence rule may invalidate `declared` by pretending it is evidence-backed |
| exact evidence | OCP-012 snapshot and evidence contracts | zero/multiple resolution is non-permissive |
| evidence temporal fact | unselected per evidence kind | no `recorded_at` or newest-time guess |
| historical evaluation time | absent in `holder-capability@1` | no inline machine-derived freshness until explicitly bound |
| current query time | OCP-012/OCP-013 call contracts can supply explicit time | it cannot rewrite stored history |
| freshness rule/version | unselected OCP-012 local rule | unknown/latest version fails closed |
| ambiguity dimensions/reasons | finite structure plus attributable recorder | semantic meaning cannot be inferred from labels or counts |
| claimant authority | exact `authority_ref` | authority to claim does not prove truth |
| downstream eligibility | OCP-013 exact consumer requirement | fresh support cannot become interchangeability, selection or authorization |

## 7. Candidate outcomes

### A — preserve OCP-012 F0/A0

`holder-capability@1` remains unchanged. `stale`, `ambiguous`, `conflicting` and `sufficient` remain attributable, with current fail-safe projection. This is the mandatory control if no complete time and rule owner is accepted.

### B — one activated `holder-capability@2` with explicit support mode

A new exact claim-kind version keeps one record family and one lineage form but distinguishes:

```text
support_mode: declaration-only | evidence-backed
```

`declaration-only` retains narrow attributable authority and forbids evidence-rule fields. `evidence-backed` requires exact rules, immutable rule inputs, explicit `support_evaluated_at` and inline freshness/ambiguity results. A current view reuses the exact rules and snapshots at an explicit query time.

This preserves one claim proposition form while preventing an evidence rule from reinterpreting a declaration. Its main risk is conditional complexity inside one claim kind.

### C — separate declaration and evidence-backed claim kinds

OCP-012 keeps one record family but introduces distinct exact kinds for declaration-only and evidence-backed propositions. Each kind has one uniform authority envelope.

This makes the trust boundary visible, but Module C currently requires a successor to preserve claim kind. Moving from a declaration to evidence-backed support would create a separate lineage or require an explicit reviewed cross-kind rule. The main risk is fragmented correction history for what users may understand as one proposition.

### D — downstream-only activation

OCP-012 stays under F0/A0. A concrete consumer such as OCP-013 owns a rule for the usability of exact claim projections at its own evaluation time and exact context.

This fits use-relative freshness, but the consumer may not relabel OCP-012's attributable `sufficient` as machine-proven or reach through the projection to invent missing claim-support semantics. The main risk is duplicated evidence interpretation across consumers.

If the downstream consumer retains a historical decision, its own accepted contract must store the exact rule, snapshots, evaluation time and inline classification. A derived current view may complement that history; it cannot replace a historical role that the consumer claims to provide.

### E — domain profile with Core envelope

A named domain owns claim-support rules while Core validates exact profile bindings. AD-012B did not select F3/A3, and no concrete domain profile or interoperability consumer is present. E is therefore a falsification control, not an admissible final outcome without an explicit AD-012 reopening gate.

### F — separate identified support-usability record

A separate record would carry independent reference, attribution and correction history. AD-012B explicitly rejected this representation under current evidence. F is not admissible without new independent-identity evidence, a Board reopening and a full P-001 invocation or reviewed reason not to invoke it.

## 8. Declaration versus evidence-backed support

Any admissible positive outcome must preserve these cases:

| Case | Required behavior |
|---|---|
| direct `declared` assertion with no evidence | remains attributable; freshness is semantically not applicable, not `missing` or `fresh`—Outcome A stores no freshness classification |
| evidence expected but empty | `missing`; never silently converted to declaration-only |
| evidence snapshot present | exact-resolves and exact-matches normalized bindings |
| late evidence | creates a new snapshot and record/successor; does not mutate history |
| positive assertion with stale support | effective claim projection is `indeterminate`, not negative |
| withdrawn successor | remains withdrawal, not evidence failure or negative polarity |

An implementation cannot infer `support_mode` from whichever fields happen to be present unless the selected normative contract makes that derivation exact and rejects mixed forms.

## 9. Candidate temporal-fact envelope

The following are candidate bindings to test, not selected rules:

| Evidence kind | Candidate temporal fact | Required caution |
|---|---|---|
| `event@1` | Event `occurred_at` | occurrence may prove history while being stale for a current-support use |
| `observation-record@1` | ObservationRecord `observed_at` | `recorded_at` cannot replace observation time; late arrival remains visible |
| `outcome-assessment-record@1` | OutcomeAssessmentRecord `evaluated_at` | assessment freshness, criterion and conclusion do not transfer automatically to claim support |

Every selected rule must state comparison precision, inclusive/exclusive cutoff behavior and non-permissive handling of missing, future-dated, timezone-less or otherwise incomparable values. AD-013 does not select numeric cutoffs.

## 10. Candidate ambiguity envelope

OCP-012 can plausibly machine-detect only bounded dimensions whose inputs it owns:

- `reference` — zero/multiple exact resolution, kind/version mismatch or missing rule/snapshot;
- `lineage` — invalid, unresolved or branching claim heads where the projection requires one meaning;
- `temporal` — missing, future-dated or incomparable exact selected times;
- finite `conflict` — incompatible exact claim heads or explicitly governed finite evidence disagreement.

Semantic questions remain attributable unless a later exact rule owns them:

- whether an observation actually supports the Capability proposition;
- whether two evidence statements mean the same thing;
- whether a claimant is reliable;
- whether a condition set is substantively equivalent to another;
- whether assessment evidence is relevant to the claim.

A1 cannot choose a winner by newest timestamp, record order, claimant count, source count or majority.

## 11. Historical and current-query roles

If B or C is selected, an evidence-backed historical record must preserve:

```text
exact claim kind and support mode
exact evidence snapshot
exact freshness and ambiguity rules
immutable rule-input snapshot
explicit support evaluation time
inline freshness/ambiguity classification and findings
attributable recorder/rule provenance
```

A current query supplies a new explicit time and returns a derived view. It does not mutate `support_state`, change assertion polarity, expire the claim record or select a newer rule. If an old rule, snapshot or evidence item cannot resolve, the query fails closed.

Outcome D retains OCP-012's historical attributable record and stores no machine-derived OCP-012 classification. Its downstream view still exact-binds its own rule, input snapshot and evaluation time. If that downstream contract claims a historical classification, it stores the classification inline under its own identity/history rules; otherwise it may expose only an explicitly timed current derivation and makes no historical-classification claim.

## 12. OCP-013 boundary

OCP-013 consumes exact claim projections for one candidate, requirement, context and evaluation time. It does not own OCP-012 claim truth.

An activated OCP-012 projection may become one exact input to OCP-013, but:

- `fresh` support is not a positive interchangeability result;
- an attributable `declared` claim remains attributable, not verified;
- OCP-013 still owns its requirement, constraint and eligibility rule;
- claim freshness cannot supply availability, authorization, ranking, selection or Assignment execution;
- matching activated claims do not make two Resources equal or interchangeable.

If D is selected, OCP-013 must name the exact downstream use and prove that its rule does not silently mutate OCP-012 semantics.

## 13. Mandatory counterexamples

| # | Pressure | Required result | Evidence owner by outcome |
|---|---|---|---|
| 1 | `recorded_at` is used as support evaluation time | reject or remain F0; never machine-derived positive | B/C rule contract; D consumer |
| 2 | claim effectivity is treated as evidence freshness | keep the two classifications separate | every outcome |
| 3 | a later query rewrites historical support state | history unchanged; new derived view only | B/C/D |
| 4 | same support is usable for one consumer and stale for another | separate exact rules and uses | B/C/D |
| 5 | declaration-only claim is marked stale because it has no evidence | declaration remains attributable with freshness not applicable | A/B/C/D |
| 6 | evidence-backed claim is displayed as verified Capability possession | forbidden | every outcome |
| 7 | a fresh OCP-011 assessment automatically makes claim support fresh | reject inherited freshness; evaluate exact claim use | B/C/D |
| 8 | newest OCP-009 Capability version replaces the bound version | exact historical version remains | every outcome |
| 9 | latest rule or current evidence replaces historical bindings | fail closed | B/C/D |
| 10 | missing rule, snapshot, evaluation time or evidence yields permissive output | `indeterminate` or no machine conclusion | B/C/D |
| 11 | future-dated, timezone-less or incomparable evidence is fresh | non-permissive temporal ambiguity | B/C/D |
| 12 | cutoff equality differs by implementation | exact inclusive/exclusive behavior | B/C/D |
| 13 | branching claim lineage selects newest head | preserve branches; `indeterminate` where unresolved | every outcome |
| 14 | claimant/source count selects authority | no count or majority authority | every outcome |
| 15 | matching positive claims imply Resource interchangeability | reject identity and AB-011 collapse | every outcome |
| 16 | Organization is used as direct holder | reject until AB-006/AB-052 decision | every outcome |
| 17 | withdrawal is converted to negative or stale | preserve distinct assertion semantics | every outcome |
| 18 | derived replay succeeds after old inputs disappear | fail closed | B/C/D |
| 19 | fixtures require a claim kind rejected by the selected outcome | outcome-conditional fixtures only | OCP-001 review |
| 20 | current implicit context replaces exact `condition_set_ref` | reject | every outcome |

No counterexample may pass by turning missing, stale, ambiguous, conflicting, unresolved or incomparable inputs into a more permissive result.

## 14. Outcome-fair executable evidence plan

### 14.1 Unconditional core

Every outcome must preserve existing OCP-012 exact Capability version, Resource-only holder, claimant/authority/condition/provenance bindings, immutable snapshots, Module A/C history, withdrawal semantics, fail-safe support projection, Resource identity and all non-equivalence boundaries.

### 14.2 Outcome-conditional blocks

| Outcome | Required executable evidence |
|---|---|
| A | fixtures prove current attributable support remains non-permissive where required and checker output never claims machine-derived freshness |
| B | exact `@1/@2` boundary, declaration/evidence modes, explicit evaluation time, complete rule bindings, inline replay, explicit current query and all applicable §13 pressures |
| C | distinct claim-kind authority, cross-kind/non-cross-kind lineage decision, exact replay and no hidden identity collapse |
| D | consumer-owned exact rule, time and snapshots; inline historical result when retained plus explicit-time derived query; OCP-012 remains unchanged; consumer cannot relabel attributable support as machine-proven |
| E | only after reopening: domain fixtures plus Core rejection of unknown or incompatible profiles |
| F | only after reopening: independent identity, endpoint, provenance, correction, branching and full P-001 evidence |

Derived-only current-query replay is the semantic equivalent for a later view. It is not an equivalent for a selected inline historical role unless the outcome explicitly preserves an attributable historical classification instead.

## 15. Comparison matrix

| Outcome | Authority added | Main benefit | Main risk | Current admissibility |
|---|---|---|---|---|
| A — F0/A0 | none | safest current contract | leaves support usability attributable | admissible control |
| B — unified `@2` | OCP-012 local F1/A1 rule plus explicit support time | preserves one claim form and lineage | conditional mode complexity | leading positive hypothesis, not selected |
| C — split kinds | separate declaration/evidence authority | clearest trust boundary | fragmented or cross-kind history | admissible alternative, not selected |
| D — downstream-only | consumer-local rule | maximally use-specific | duplicated or layer-violating interpretation | conditional alternative |
| E — domain profile | domain semantic owner | local specialization | opaque/incompatible profiles | inadmissible without reopening |
| F — separate record | independent usability identity | independent reference/history | overlaps OCP-012 and AD-012 decision | inadmissible without reopening |

## 16. Working hypothesis

B is the most promising positive direction because OCP-012 itself owns the attributable support projection and existing Module C lineage. A new exact claim-kind version can create a governed activation boundary without mutating `holder-capability@1` history.

Its central unresolved risk is the coexistence of declaration-only and evidence-backed authority in one kind. The model succeeds only if mixed forms are mechanically rejected and `declared` never acquires false evidence authority.

C is the strongest clarity alternative but must prove a coherent history model when the same claimant later adds evidence. D remains plausible only for a concrete downstream use that does not need OCP-012 to claim machine-derived support.

If no outcome supplies an explicit historical evaluation-time owner and complete rule contract, A remains mandatory. Implementation convenience is not decision-separating evidence.

## 17. Explicit exclusions

AD-013 does not:

- create a Concept, Pattern, record family, schema, checker rule, fixture or graph edge;
- amend OCP-009, OCP-011, OCP-012 or OCP-013;
- introduce Organization claims or resolve AB-006/AB-052;
- define a Capability assessment, verification, certification or trust score;
- define Readiness, availability, authorization, admissibility, selection or Assignment execution;
- decide Resource interchangeability or AB-011 again;
- make identical claims or support states establish Resource equality;
- define universal durations, source reliability or a semantic-equivalence engine;
- use newest timestamp, record order, claimant count, source count or issuer count as authority.

`Capability ≠ Readiness` remains binding. Exact OCP-009 Capability version binding and fail-safe evidence semantics remain unchanged.

## 18. External review target and exit criteria

External review must test:

1. whether AD-013 is a permitted specialization of AD-012B rather than a silent reopening;
2. whether A–D are genuinely distinct and E/F are correctly gated controls;
3. whether `recorded_at`, effectivity and query time are kept separate from historical support evaluation time;
4. whether declaration-only authority survives without being treated as missing evidence or independent verification;
5. whether B and C preserve coherent Module C history;
6. whether D avoids reaching through OCP-012 and duplicating claim semantics;
7. whether all twenty counterexamples have outcome-fair ownership; and
8. whether the comparison is understandable without checker code.

The discovery may advance to outcome comparison only when no evidence obligation assumes a layer rejected by the outcome it tests. It may advance to a Board selection only after external review closes all Blocking, Major and Moderate findings and every admissible outcome has a falsifiable implementation contract.

## 19. Discovery status and next act

Revision `0.1.0` opens `AD-013 / AB-060` in `Discovery`. It records no preferred Board outcome beyond the non-normative working hypothesis in §16.

The next PR after external review should resolve findings in AD-013 itself. A later comparison/selection act may select A, B, C or D, or keep the question in Discovery. No OCP-012 version or status changes until a separate activation implementation is reviewed, approved, authorized and squash-merged.
