---
Decision-ID: AD-013
Title: Capability Claim Support Usability Activation Boundary
Version: 0.2.0
Status: Discovery
Owner: Architecture Board
Depends-On: AD-005, AD-007, AD-008, AD-012, OCP-001, OCP-009, OCP-010, OCP-011, OCP-012, OCP-013, P-001
Applies-To: AB-060, CapabilityClaimRecord support freshness, ambiguity and replay
Review-After: external adversarial review of the comparative revision before any Board selection
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
4. If they remain modes, is `support_mode` stable within one Module C lineage, or may an explicit reviewed transition rule govern a successor's mode change without reinterpreting its predecessor?
5. Which temporal fact is admissible for each existing evidence kind?
6. Which reference, lineage, temporal or semantic-classification ambiguity dimensions can OCP-012 decide mechanically?
7. How does a later explicit query derive current support usability without changing the historical claim or consulting current data?
8. Can OCP-013 safely consume an activated OCP-012 projection without inheriting its rule as an interchangeability or authorization rule?

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

This preserves one claim proposition form while preventing an evidence rule from reinterpreting a declaration. It does not yet prove a simpler history model than C: the selected contract must decide whether `support_mode` is stable within one Module C lineage or govern an explicit successor transition that leaves every predecessor's authority unchanged. Its main risk is conditional and transition complexity inside one claim kind.

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
| 14 | a successor flips `support_mode` and reinterprets a declaration as evidence-backed | reject; or apply an explicit reviewed transition rule that preserves the predecessor's authority | B rule contract; C cross-kind rule |
| 15 | claimant/source count selects authority | no count or majority authority | every outcome |
| 16 | matching positive claims imply Resource interchangeability | reject identity and AB-011 collapse | every outcome |
| 17 | Organization is used as direct holder | reject until AB-006/AB-052 decision | every outcome |
| 18 | withdrawal is converted to negative or stale | preserve distinct assertion semantics | every outcome |
| 19 | derived replay succeeds after old inputs disappear | fail closed | B/C/D |
| 20 | fixtures require a claim kind rejected by the selected outcome | outcome-conditional fixtures only | OCP-001 review |
| 21 | current implicit context replaces exact `condition_set_ref` | reject | every outcome |

No counterexample may pass by turning missing, stale, ambiguous, conflicting, unresolved or incomparable inputs into a more permissive result.

## 14. Outcome-fair executable evidence plan

### 14.1 Unconditional core

Every outcome must preserve existing OCP-012 exact Capability version, Resource-only holder, claimant/authority/condition/provenance bindings, immutable snapshots, Module A/C history, withdrawal semantics, fail-safe support projection, Resource identity and all non-equivalence boundaries.

### 14.2 Outcome-conditional blocks

| Outcome | Required executable evidence |
|---|---|
| A | fixtures prove current attributable support remains non-permissive where required and checker output never claims machine-derived freshness |
| B | exact `@1/@2` boundary, declaration/evidence modes, explicit evaluation time, complete rule bindings, support-mode lineage stability or explicit transition rule, inline replay, explicit current query and all applicable §13 pressures |
| C | distinct claim-kind authority, cross-kind/non-cross-kind lineage decision, exact replay and no hidden identity collapse |
| D | consumer-owned exact rule, time and snapshots; inline historical result when retained plus explicit-time derived query; OCP-012 remains unchanged; consumer cannot relabel attributable support as machine-proven |
| E | only after reopening: domain fixtures plus Core rejection of unknown or incompatible profiles |
| F | only after reopening: independent identity, endpoint, provenance, correction, branching and full P-001 evidence |

Derived-only current-query replay is the semantic equivalent for a later view. It is not an equivalent for a selected inline historical role unless the outcome explicitly preserves an attributable historical classification instead.

## 15. Comparison matrix

| Outcome | Authority added | Main benefit | Main risk | Current admissibility |
|---|---|---|---|---|
| A — F0/A0 | none | safest current contract | leaves support usability attributable | admissible control |
| B — unified `@2` | OCP-012 local F1/A1 rule plus explicit support time | preserves one claim form | conditional mode and same-kind transition complexity | leading positive hypothesis, not selected |
| C — split kinds | separate declaration/evidence authority | clearest trust boundary | fragmented or cross-kind history | admissible alternative, not selected |
| D — downstream-only | consumer-local rule | maximally use-specific | duplicated or layer-violating interpretation | conditional alternative |
| E — domain profile | domain semantic owner | local specialization | opaque/incompatible profiles | inadmissible without reopening |
| F — separate record | independent usability identity | independent reference/history | overlaps OCP-012 and AD-012 decision | inadmissible without reopening |

## 16. Working hypothesis

B is the most promising positive direction because OCP-012 itself owns the attributable support projection and existing Module C lineage. A new exact claim-kind version can create a governed activation boundary without mutating `holder-capability@1` history.

Its central unresolved risk is the coexistence of declaration-only and evidence-backed authority in one kind, including whether a successor may change mode within one lineage. B has no lineage advantage over C until it proves either mode stability or an explicit transition rule that never changes a predecessor's authority. The model succeeds only if mixed forms and ungoverned mode changes are mechanically rejected and `declared` never acquires false evidence authority.

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
7. whether all twenty-one counterexamples have outcome-fair ownership; and
8. whether the comparison is understandable without checker code.

The discovery may advance to outcome comparison only when no evidence obligation assumes a layer rejected by the outcome it tests. It may advance to a Board selection only after external review closes all Blocking, Major and Moderate findings and every admissible outcome has a falsifiable implementation contract.

## 19. Discovery status and next act

Revision `0.1.0` opened `AD-013 / AB-060` in `Discovery`. It recorded no preferred Board outcome beyond the non-normative working hypothesis in §16. Its exact-head external review completed in PR #66; all findings were resolved before owner-authorized squash merge.

Revision `0.2.0` adds comparison only. Findings against that comparison must be resolved in AD-013 itself before a later selection act may choose A, B, C or D, or keep the question in Discovery. No OCP-012 version or status changes until a separate activation implementation is reviewed, approved, authorized and squash-merged.

## 20. Comparative revision scope and method

Revision `0.1.0` was exact-head reviewed through three iterations in PR #66. Fable's Moderate lineage-fairness finding and Minor counterexample-count finding were accepted and resolved before owner-authorized squash merge. Revision `0.2.0` now compares the admissible outcomes. It does not select one.

The comparison follows seven rules:

1. A is a complete no-new-authority control, not a failed implementation of B, C or D.
2. B, C and D must each name the protected use, historical evaluation-time owner, current-query owner and exact semantic boundary.
3. Declaration-only authority is tested independently from evidence-backed support.
4. B receives no lineage advantage merely because both modes share a claim kind; C receives no clarity advantage merely because it uses different kinds.
5. Every outcome is tested against the same human scenarios and all twenty-one §13 counterexamples using evidence expressible for that outcome.
6. E and F remain gated falsification controls. Comparison cannot silently reopen AD-012B or create independent usability identity.
7. Similar fields, one checker implementation or storage convenience are not decision-separating evidence.

The working verdicts below mean:

- **admissible control** — safe and complete while no positive activation is justified;
- **leading hypothesis** — the smallest currently plausible positive direction, still subject to a Board choice and exact implementation evidence;
- **conditional alternative** — viable only if its additional history or consumer boundary is explicitly selected and proven; and
- **gated control** — not an admissible final outcome in AD-013 without a separate reopening act.

These are comparison verdicts, not Architecture Board selections.

## 21. Protected-use and evaluation-time comparison

The outcomes differ first in the question they protect. An evaluation time owned by one layer cannot be borrowed by another.

| Outcome | Protected historical use | Historical evaluation-time owner | Current-query owner | Main authority risk | Working verdict |
|---|---|---|---|---|---|
| A — OCP-012 F0/A0 | attributable claim and fail-safe head projection | none added; no machine-derived claim-support evaluation | existing `as_of_time` selects applicable heads only | an implementation may present attributed `sufficient` as machine-proven | **Admissible control and current default.** |
| B — unified `holder-capability@2` | OCP-012's own evidence-backed attributable projection | explicit OCP-012 `support_evaluated_at` under exact local rules | OCP-012 explicit-time derived support view | conditional modes or a successor transition may change authority by implication | **Leading positive hypothesis.** |
| C — split claim kinds | OCP-012's evidence-backed kind under a uniform authority envelope | explicit OCP-012 support evaluation time for the evidence-backed kind | OCP-012 explicit-time derived support view | cross-kind history may fragment or silently weaken Module C identity | **Conditional clarity alternative.** |
| D — downstream-only | one exact consumer's use of the accepted OCP-012 projection | none in OCP-012; the downstream record owns only its own evaluation time | the same named consumer under an explicit query contract | consumer may reach through the projection and duplicate or relabel OCP-012 semantics | **Conditional use-specific alternative.** |

OCP-013 already owns `evaluation_time` for one directional eligibility evaluation. That makes a D-style consumer rule expressible, but the time remains OCP-013's. It cannot become a historical OCP-012 `support_evaluated_at`, and it cannot convert attributable `sufficient` into machine-proven support.

B and C protect OCP-012's own projection. Therefore both need a new exact claim-kind contract that owns support evaluation time, per-evidence temporal facts, rule versions, snapshots and inline results. `recorded_at`, effectivity and a downstream evaluation time remain inadmissible substitutes.

## 22. Human scenario comparison

The following scenarios expose what a user would see before checker details.

| Scenario | A — F0/A0 | B — unified `@2` | C — split kinds | D — downstream-only |
|---|---|---|---|---|
| claimant makes a direct declaration with no evidence | attributable `declared`; freshness not applicable | explicit `declaration-only`; evidence-rule fields forbidden | declaration kind with no evidence authority | unchanged OCP-012 declaration; consumer may preserve attribution or require review |
| first claim is evidence-backed | attributable support state; no machine-derived freshness | `evidence-backed` mode exact-binds rule, time and snapshots | evidence-backed kind exact-binds rule, time and snapshots | OCP-012 remains attributable; named consumer evaluates only its exact use |
| the same claimant later adds evidence to a declaration | new record without machine-derived mode transition | explicit mode-stable lineage treatment or reviewed same-kind transition; predecessor never changes meaning | separate lineage or reviewed cross-kind transition; predecessor never changes meaning | source claim history remains unchanged; consumer creates a new evaluation |
| claimant corrects evidence-backed support | ordinary successor with attributable support | same-mode successor preserves binding identity and exact replay | evidence-backed-kind successor preserves binding identity and exact replay | new consumer evaluation; no source mutation |
| claimant withdraws a proposition | explicit successor withdrawal, never negative | withdrawal remains assertion semantics, not support failure | withdrawal remains assertion semantics within the applicable kind/lineage contract | downstream result cannot manufacture source withdrawal |
| two correction branches remain live | visible branches; projection fails safe | branches remain visible within the selected mode/transition contract | branches remain visible within each governed kind and any reviewed cross-kind rule | consumer binds exact heads or returns non-permissive result |
| a later user asks whether support is usable now | no machine-derived freshness; attributable history remains | new explicit-time OCP-012 view replays exact historical rule and snapshot | new explicit-time evidence-backed-kind view replays its exact historical rule and snapshot | named consumer evaluates at its own explicit time and context |
| two consumers use the same evidence differently | distinct attributable consumer uses | one OCP-012 source-use classification may feed both, but neither consumer may reuse it as its own freshness conclusion | one evidence-backed-kind source classification may feed both, but neither consumer may reuse it as its own freshness conclusion | each consumer owns a separate rule; results are not portable by label |

No row turns evidence-backed support into verified Capability possession. No row turns a direct declaration into missing evidence.

## 23. Outcome-by-outcome comparison verdicts

| Outcome | Positive evidence already present | Decision-separating gap | Main benefit | Main risk | Separate working verdict |
|---|---|---|---|---|---|
| A — preserve F0/A0 | accepted OCP-012 already preserves attribution, exact bindings, history and fail-safe projection | no machine-derived support usability | least authority and no migration | attributable thresholds remain non-portable | **Admissible control.** Mandatory wherever a positive contract is incomplete. |
| B — unified `@2` | OCP-012 owns the proposition, support vocabulary, evidence snapshots and Module C history | select the support-mode lineage rule and complete per-evidence temporal/ambiguity rules | one exact claim-kind contract can expose the declaration/evidence boundary without a second record family | conditional schema and same-kind transitions may hide authority changes | **Leading positive hypothesis.** Smallest Core-local activation if its transition contract is explicit. |
| C — split kinds | each kind can have a uniform authority envelope | prove how declaration and evidence-backed histories relate without silent cross-kind supersession | most visible trust boundary for humans and validators | duplicated kind handling, fragmented heads or a weakened Module C identity rule | **Conditional alternative.** Prefer only if uniform-kind clarity materially outweighs history cost. |
| D — downstream-only | OCP-013 demonstrates exact consumer, context, evaluation time, snapshots and fail-safe combination | name a concrete consumer rule that does not reinterpret source support | maximally use-relative; OCP-012 remains stable | evidence interpretation may be duplicated across consumers or moved to the wrong layer | **Conditional alternative.** No generic downstream rule is justified. |
| E — domain profile | no concrete domain profile or Core interoperability need exists | explicit AD-012 reopening plus profile owner and compatibility evidence | local specialization | opaque or falsely comparable meanings | **Gated control.** Not selectable by AD-013. |
| F — separate record | no independent-reference, correction-history or shared-consumer need exists | Board reopening, independent identity and full P-001 evidence | independent reference/history if ever justified | overlaps OCP-012 and turns use-relative usability into a standing object | **Gated control.** Not selectable by AD-013. |

B remains the leading hypothesis because OCP-012 already owns the exact proposition and support projection that would be protected. This is not a Board decision. If B cannot state a safe mode-transition rule or complete temporal owner, A remains correct; C or D may become preferable only through their own decision-separating evidence.

A B/C activation would answer only whether support is usable for OCP-012's own attributable projection under its exact rule. It would not answer whether the same source input is usable for every downstream consumer. Any additional consumer-specific conclusion remains a separate D-style rule and cannot be imported from OCP-012 by label.

## 24. B–C lineage and mode comparison

B and C share the same underlying history question: what happens when one claimant first declares a proposition and later supports it with evidence? The kind spelling does not answer that question.

| Sub-option to be decided | Binding treatment | Late-evidence behavior | Projection obligation | Main falsifier |
|---|---|---|---|---|
| B with mode-stable lineages | `support_mode` is part of the binding preserved by Module C | a declaration and later evidence-backed record occupy distinct mode-specific lineages | OCP-012 must preserve or explicitly reconcile both applicable heads without treating either as a correction of the other | identical-kind storage still produces fragmented proposition history |
| B with reviewed same-kind transition | `support_mode` may change only through an explicit allowed transition under `holder-capability@2` | successor may become evidence-backed while predecessor remains declaration-only historically | transition provenance and replay must prove that old authority never changes and field presence cannot trigger the transition | transition silently upgrades the predecessor or permits an ungoverned downgrade |
| C with separate lineages | claim kind remains Module C binding identity | later evidence starts a separate evidence-backed lineage | OCP-012 must expose both exact histories without pretending one superseded the other | consumers cannot determine which history expresses the current attributable proposition |
| C with reviewed cross-kind transition | OCP-012 explicitly narrows an exception to the existing same-kind successor rule | successor changes kind under a separately reviewed transition contract | resolver and replay preserve old kind, new kind, transition basis and branches | exception weakens exact kind identity or becomes a generic cross-kind rewrite |

These are sub-options within B and C, not additional AD-013 outcomes. A later Board act that selects B or C must select one explicit lineage treatment. It may not defer the choice to storage code.

B's potential advantage is one governed kind and resolver family, not automatically one lineage. C's potential advantage is a visible trust boundary, not automatically safer history. A valid selection must show the same late-evidence, correction, withdrawal and branching examples in both human prose and executable fixtures.

## 25. Temporal and ambiguity contract comparison

### 25.1 Temporal owner

| Evidence kind | B/C historical temporal fact | D consumer use | Forbidden substitution |
|---|---|---|---|
| `event@1` | exact `occurred_at` only when the OCP-012 rule names occurrence as the measured fact | consumer may measure occurrence only under its own exact rule | Event recording or claim recording time |
| `observation-record@1` | exact `observed_at` under the selected OCP-012 rule | consumer may measure observation time under its own exact rule | observation `recorded_at` or arrival order |
| `outcome-assessment-record@1` | exact assessment `evaluated_at` as an input fact, followed by a separate claim-support evaluation | consumer may measure the exact assessment evaluation for its use | inherited OCP-011 freshness or claim `recorded_at` |

B and C require explicit `support_evaluated_at` for a stored historical classification. D uses the consuming contract's own evaluation time and stores no machine-derived OCP-012 historical classification. Every positive rule must bind precision, cutoff equality and non-permissive handling of missing, future-dated, timezone-less or incomparable time. No numeric duration is selected here.

### 25.2 Ambiguity owner

| Dimension | A | B/C | D |
|---|---|---|---|
| exact reference and snapshot | accepted structural rejection | accepted structural baseline plus exact selected rule/snapshot bindings | consumer rejects its unresolved exact input |
| claim lineage | accepted branching visibility and fail-safe projection | selected mode/kind transition contract additionally owns its named lineage cases | consumer binds exact heads; it cannot choose a source winner |
| temporal comparability | attributable unless structurally invalid | exact OCP-012 local temporal rule may derive named ambiguity | exact consumer rule may derive ambiguity only for its use |
| semantic relevance or source reliability | attributable | remains attributable unless a later separately governed rule owns one finite dimension | remains outside the consumer's mechanical rule unless explicitly accepted |
| conflict | finite accepted claim-head conflict remains non-permissive | exact local rules may add only named decidable cases | consumer preserves source conflict and may add its own input conflict |

No ambiguity rule chooses authority by newest timestamp, record order, claimant count, source count, issuer count or majority.

## 26. Normative authority accounting

“Unselected” means the implementation must fail closed; it is not permission for a caller or checker to choose.

| Binding or conclusion | A | B | C | D | Fail-safe obligation |
|---|---|---|---|---|---|
| protected projection | accepted attributable OCP-012 projection | OCP-012 evidence-backed `@2` mode | OCP-012 evidence-backed exact kind | named downstream consumer only | another layer's result is not portable by label |
| declaration/evidence boundary | accepted support-state contract | exact `support_mode` contract | exact claim-kind contract | source boundary remains OCP-012 | direct declaration never becomes missing or verified |
| lineage identity/transition | accepted same-kind binding | selected B mode-stability or transition rule | selected C separate-lineage or cross-kind rule | source OCP-012 history unchanged | no implicit transition by field presence, time or order |
| evidence kind/reference | accepted OCP-012 bindings | OCP-012 local rule and snapshot | OCP-012 evidence-backed kind and snapshot | exact consumer input contract | zero, multiple, wrong-kind or mismatched input is non-permissive |
| evidence temporal fact | none selected | exact OCP-012 rule per kind | exact OCP-012 rule per kind | exact named consumer rule | no recording/effectivity fallback |
| historical evaluation time | none | explicit OCP-012 `support_evaluated_at` | explicit evidence-backed-kind support time | none in OCP-012; consumer owns only its own time | downstream time cannot rewrite source history |
| current query time | existing claim-head `as_of_time` only | explicit OCP-012 derived query | explicit OCP-012 derived query | explicit consumer query | current wall clock is never implicit |
| freshness/ambiguity rule version | none selected | exact OCP-012 local binding | exact OCP-012 evidence-backed-kind binding | exact consumer-local binding | unknown or latest-only rule fails closed |
| immutable inputs | accepted evidence snapshot | evidence plus rule-input snapshots | evidence plus rule-input snapshots | consumer input snapshot | current data cannot replace historical inputs |
| claimant authority | accepted `claimant_ref` + `authority_ref` | unchanged | unchanged | unchanged source attribution | support usability does not prove truth |
| downstream eligibility | OCP-013 | OCP-013 after consuming exact source projection | OCP-013 after consuming exact source projection | named consumer, if selected | no availability, authorization, ranking, selection or Assignment mutation |

Exact OCP-009 Capability version and `condition_set_ref` remain binding in every column.

## 27. Mandatory counterexample mapping

Every row maps the complete §13 pressure to A–D. E and F remain gated; any future reopening must additionally satisfy every applicable row without borrowing another outcome's fixtures.

| # | A — F0/A0 | B — unified `@2` | C — split kinds | D — downstream-only |
|---|---|---|---|---|
| 1 | no support evaluation is derived from `recorded_at` | explicit `support_evaluated_at`; reject substitution | explicit evidence-backed-kind support evaluation time; reject substitution | consumer uses its own time; source remains unchanged |
| 2 | effectivity only selects applicable claims | support rule keeps effectivity and freshness separate | evidence-backed-kind rule keeps effectivity and freshness separate | consumer keeps source effectivity distinct from input usability |
| 3 | attributable history never recomputes | current view is a new explicit-time derivation | evidence-backed-kind current view is a new explicit-time derivation | new consumer evaluation only |
| 4 | preserve distinct attributable consumer uses | exact-bind the OCP-012 source use; divergent consumer uses require separate downstream rules | exact-bind the evidence-backed source use; divergent consumer uses require separate downstream rules | each consumer owns a separate exact rule |
| 5 | `declared` remains attributable and freshness-not-applicable | declaration-only mode forbids evidence rule | declaration kind forbids evidence rule | consumer cannot mark absence of evidence stale |
| 6 | support label never verifies Capability | derived support remains non-verifying | evidence-backed-kind support remains non-verifying | consumer result remains use-specific and attributable to inputs |
| 7 | OCP-011 state is merely exact evidence input | claim rule separately evaluates the selected assessment fact | evidence-backed-kind rule separately evaluates the selected assessment fact | consumer separately evaluates its exact use |
| 8 | exact historical OCP-009 version remains | `@2` cannot redirect Capability version | no split claim kind may redirect Capability version | consumer exact-binds source version |
| 9 | replay preserves attributable record | exact historical rule and snapshots only | exact evidence-backed-kind rule and snapshots only | exact consumer rule and snapshot only |
| 10 | no positive machine conclusion is claimed | missing rule/time/snapshot/evidence is non-permissive | missing evidence-backed-kind binding is non-permissive | missing consumer binding is non-permissive |
| 11 | no machine-derived fresh result | temporal rule rejects or returns ambiguity | evidence-backed-kind temporal rule rejects or returns ambiguity | consumer rule fails closed |
| 12 | no implicit cutoff exists | exact rule states equality and precision | exact evidence-backed-kind rule states equality and precision | exact consumer rule states them |
| 13 | accepted branches remain visible | selected mode/transition rule preserves branches | selected kind/transition rule preserves branches | consumer binds exact heads or returns non-permissive result |
| 14 | no mode exists to flip | ungoverned mode flip rejects; reviewed transition preserves predecessor | ungoverned cross-kind rewrite rejects; reviewed rule preserves predecessor | source mode/kind never changes through consumer evaluation |
| 15 | no count-based authority | claimant/source/issuer count remains irrelevant | claimant/source/issuer count remains irrelevant | claimant/source/issuer count remains irrelevant |
| 16 | existing OCP-013 boundary remains | activated support is only one exact input | evidence-backed-kind support is only one exact input | consumer result remains directional eligibility, never Resource equality |
| 17 | Organization holder rejects | `@2` remains Resource-only | all claim kinds remain Resource-only | consumer cannot legalize an invalid source holder |
| 18 | withdrawal remains assertion semantics | rule cannot turn it into negative or stale | evidence-backed-kind rule cannot turn it into negative or stale | consumer preserves withdrawn input as non-permissive |
| 19 | no derived historical replay is claimed | missing old rule/input fails closed | evidence-backed-kind replay fails closed on missing old rule/input | consumer replay fails closed |
| 20 | only A-compatible fixtures apply | B fixtures require the selected B sub-option | C fixtures require the selected C sub-option | D fixtures belong to the named consumer; OCP-012 stays unchanged |
| 21 | exact bound conditions remain | query exact-binds historical `condition_set_ref` | evidence-backed-kind query exact-binds historical `condition_set_ref` | consumer context cannot replace the source condition binding |

No row may pass by turning missing, stale, ambiguous, conflicting, unresolved, incomparable or structurally invalid inputs into a more permissive result.

## 28. Outcome-conditional implementation contracts

This comparison adds no checker code or fixtures. A later selection must prove only the block that matches the selected outcome.

### 28.1 A — no-new-authority control

- preserve `holder-capability@1`, accepted support vocabulary and current projection;
- prove that checker outputs do not claim machine-derived support freshness or semantic ambiguity;
- retain non-permissive behavior for `missing`, `stale`, `ambiguous`, `conflicting`, invalid or unresolved inputs;
- add no placeholder rule, time field, kind, record or migration.

### 28.2 B — unified `holder-capability@2`

- exact `@1/@2` boundary and no rewrite of `@1` history;
- exact protected OCP-012 source use; no claim of downstream-use portability;
- mechanically disjoint `declaration-only` and `evidence-backed` shapes;
- explicit selection of mode-stable lineage or reviewed same-kind transition;
- explicit `support_evaluated_at`, exact per-evidence temporal facts, rule versions, evidence and rule-input snapshots;
- inline historical states plus explicit-time derived query replay;
- rejection of mixed forms, implicit mode inference and ungoverned mode changes;
- all applicable §13 cases, including withdrawal, branching, late evidence and two-consumer divergence.

### 28.3 C — split claim kinds

- exact declaration and evidence-backed kind contracts within the existing record family;
- exact protected OCP-012 source use; no claim of downstream-use portability;
- explicit selection of separate lineages or a narrowly reviewed cross-kind transition;
- uniform authority envelope per kind and no inference from whichever fields are present;
- complete support-time, rule, snapshot, inline history and current-query obligations for the evidence-backed kind;
- deterministic head projection that does not hide a declaration or evidence-backed branch;
- all applicable §13 cases and proof that the trust-boundary clarity outweighs duplicated kind/history handling.

### 28.4 D — named downstream consumer

- name the concrete accepted consumer and exact protected decision;
- leave OCP-012 `holder-capability@1`, support states and historical authority unchanged under F0/A0;
- exact-bind consumer rule, context, evaluation time, claim heads and immutable input snapshot;
- store an inline result only if the consumer claims historical authority for it; otherwise expose only an explicit-time derived result;
- forbid reaching through an attributable projection to relabel source `sufficient` as machine-proven support;
- prove that duplicated evidence interpretation is required and cannot be expressed by consuming a future OCP-012 activation.

E requires a separate AD-012 reopening with a concrete domain profile. F requires a Board reopening, independent identity evidence and a full P-001 invocation or reviewed reason not to invoke it. Neither receives implementation fixtures from AD-013A.

## 29. Comparison status and next decision gate

Revision `0.2.0` supplies protected-use comparison, human scenarios, B/C lineage sub-options, temporal and ambiguity ownership, authority accounting, a complete mapping of all twenty-one counterexamples and outcome-conditional implementation contracts. AD-013 remains `Discovery`; AB-060 remains `Discovery`; no outcome is selected.

External adversarial review must now determine:

1. whether B is fairly identified as the smallest positive Core-local direction while A remains the complete current control;
2. whether B's mode-stable and reviewed-transition sub-options expose every lineage cost that C also carries;
3. whether C's visible trust boundary provides decision-separating value beyond schema spelling;
4. whether OCP-013 or another concrete consumer supplies enough evidence for D without reaching through OCP-012;
5. whether historical and current-query roles have legitimate, separate evaluation-time owners;
6. whether declared authority survives unchanged in every admissible outcome;
7. whether §§26–28 map all authority and every counterexample without assuming a rejected layer; and
8. whether the comparison remains understandable without checker code.

A later `AD-013B` Board act may select A, B, C or D, or retain the question in Discovery. If it selects B or C, it must also choose the explicit lineage sub-option and protected OCP-012 use. If it selects D, it must name the concrete downstream consumer and exact decision. The selection act may not itself amend OCP-012, create a claim kind, schema, rule, fixture, Pattern, record family, Concept or graph edge.

Any selected activation requires a later separately reviewed OCP-012 or named-consumer implementation PR with its own version, normative contract, executable evidence and owner authorization. Exact-head Fable approval, Codex adjudication, green CI and explicit Pavlo or Architecture Board authorization remain mandatory before squash merge of this comparison and every later act.
