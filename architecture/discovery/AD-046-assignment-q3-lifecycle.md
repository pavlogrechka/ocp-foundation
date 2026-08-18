---
Decision-ID: AD-046
Title: Assignment Q3 Retroactivity Lifecycle Resolution
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-035, AD-039, AD-044, AD-045, OCP-001, OCP-005, OCP-016, OCP-023
Applies-To: OCP-005 §8, OCP-005 §19.3
Review-After: A separately mandated act proposes changing the authoritative established_at lower bound or resolving OCP-005 Q9
---

# AD-046 — Assignment Q3 Retroactivity Lifecycle Resolution

## 1. Mandate and exact result

This lifecycle act asks whether existing records are sufficient to turn the provisional OCP-005 §8 boundary into the final answer to Q3. They are sufficient for one narrow result:

> An Assignment cannot derive effectivity for an instant earlier than the authoritative `established_at` projected from its transition history.

Q3 is therefore resolved negatively and struck in OCP-005 §19.3. The result does **not** say when an Establishment transition was recorded or ingested, authenticate its `occurred_at`, define correction lineage, or choose the number of applicability intervals. Q9 remains open. `TEMPORAL_MODEL_UNRESOLVED` remains a `blocks-whole-document-freeze` blocker, now supported by Q9 alone.

OCP-005 moves from `0.2.8` to `0.3.0` and remains `Draft`; Assignment remains `Accepted`. No other question, blocker, survivor class, status, promotion cycle or activation changes.

## 2. Gate-first before result form

OCP-016 G4 does not apply to this result. The act finalizes an already executable negative effectivity boundary. It creates no positive-capable rule, positive result, profile, activation, owner or evaluator. A rule that permitted effectivity before the authoritative Establishment projection would be a different positive-capable proposal and would require its own G4 path.

The form is consequently one lifecycle AD, the bounded OCP-005 edit, a current stable-surface projection, and a machine-readable witness. It does not activate a Core or Route D model.

## 3. Sufficiency criterion declared before application

Q3 closes only if all four conditions hold:

1. current owner text and executable behavior already agree on the `established_at` lower bound;
2. accepted-consumer pressure excludes the retroactive-effectivity classes;
3. every surviving temporal class shares prospective-only effectivity; and
4. finalizing that common boundary requires no new recording-time, ingestion-time, correction-lineage, `occurred_at`-authentication or interval-cardinality rule.

Evidence is ordered as current owner boundary, executable behavior, accepted-consumer pressure, surviving current-norm classes, then authority/baseline separation. Historical evidence may establish what was observed at its baseline, but it cannot itself supply current lifecycle authority. The separately mandated Board act supplies that authority.

## 4. Evidence ledger: what each record proves and does not prove

| Record | What it proves | What it does not prove |
|---|---|---|
| Current OCP-005 §§7–8 | `established_at` is projected from the unique authoritative `Draft → Established` transition; effectivity requires `established_at <= t` | recording or ingestion time, correction lineage, authenticity of `occurred_at`, interval cardinality |
| Executable `valid-established.yaml` control | the current validator returns ineffective at `09:54Z` and effective at `09:55Z` for authoritative `established_at = 09:55Z`, even when applicability starts at `09:50Z` | trust in the transition producer or any backdating/correction policy |
| AD-039 baseline record | the lower-bound control holds while recording-time and Q9 gaps remain distinct | authority to close Q3 now |
| AD-044 baseline record | the accepted OCP-023 need retains both prospective classes and rejects both retroactive classes | a choice between single and multiple intervals, or lifecycle closure authority |
| AD-045 baseline record | the only surviving temporal classes are `PROSPECTIVE_ONLY_SINGLE_INTERVAL` and `PROSPECTIVE_ONLY_MULTIPLE_INTERVALS` | repository-wide semantic-axis completeness or authority to resolve Q9 |
| Current Accepted OCP-023 §7 | the accepted consumer reuses the rule that Establishment has occurred no later than evaluation and supplies no independent retroactivity rule | completeness authority, a production evaluator or multiple-interval policy |

The records agree on precisely one stable intersection: prospective-only effectivity relative to authoritative `established_at`. Their explicit gaps remain outside the decision. Closing Q3 does not elevate baseline-bound observations into current authority and does not turn analytic classifications into observed behavior.

## 5. Why the negative boundary is sufficient and narrow

OCP-005 already defines `established_at(Assignment)` as the `occurred_at` of the unique `Draft → Established` record and derives effectivity only when `established_at <= t`. The executable control discriminates the boundary: changing only the query instant across `09:55Z` changes the result. It is not a constant verdict on unrelated inputs.

AD-044 independently tested all four temporal resolution classes against the accepted consumer need. Both retrospective classes failed the need; both prospective classes survived. AD-045 then tested the two survivors against current primary norm. Neither was excluded, and their only remaining difference is Q9 interval cardinality. Thus closing Q3 does not select between the survivors or change their inventory.

The result is not “backdating is impossible.” A transition record may still present an `occurred_at` whose production, recording, ingestion or correction provenance is not defined here. The final rule is only that the authoritative value, once present in valid transition history, is the lower bound for derived effectivity. That is the full extent of the existing rule and therefore the full extent of this resolution.

## 6. Current projections and historical separation

The complete current-projection and historical-succession sweep found four carriers that must change with OCP-005:

1. `docs/005-assignment-concept/README.md`: version, §8 final boundary and §19 Q3 strikeout;
2. `architecture/assignment-stable-surface.yaml`: current expected version, Q3 state/classification, and Q9-only membership of `TEMPORAL_EFFECTIVITY_EXTENSION` and `TEMPORAL_MODEL_UNRESOLVED`.
3. `architecture/consumer-need-discovery.yaml`: the current Accepted-governance inventory and latest current-projection owner, while its AD-036 historical result and current unmet OCP-023 need remain unchanged; and
4. `architecture/assignment-retroactivity-q3-resolution.yaml`: exact `superseded_source_quotes` bindings from the byte-stable AD-045 witness rows to their current OCP-005 successors, including the witness path, statement identifier, historical quote, successor quote and reason.

The fourth carrier makes succession durable without mutating history: both checker readers resolve the same exact data-side binding instead of carrying independent code literals. Checker modules that read current carriers advance to `0.3.0` and distinguish current projections from historical baseline assertions. Repository accounting and navigation gain AD-046 descriptions; their status distributions do not change.

AD-035, AD-038, AD-039, AD-040, AD-044 and AD-045 documents and witnesses remain byte-identical. Their `baseline`, `baseline_evidence_objects`, pressure inventory and survivor inventory describe completed observations at their own commits. In particular, AD-039 truthfully records that Q3 was open then, while AD-044 and AD-045 truthfully preserve the classes they enumerated. Rewriting any of them would falsify evidence rather than synchronize current state.

## 7. Executable enforcement

`architecture/assignment-retroactivity-q3-resolution.yaml` binds the exact baseline, gate result, ordered sufficiency criterion, six-row evidence ledger, narrow decision, version transition, current projections, exact historical-to-current quote successions, migration/rollback unit, historical hashes and unchanged promotion gate.

The checker requires:

- OCP-005 `0.3.0 / Draft`, Assignment `Accepted`, one exact final §8 boundary and one exact Q3 resolution reference;
- Q3 struck while Q2, Q4, Q5, Q7, Q8, Q9, Q10 and Q11 remain open, with historical Q1 and Q6 still struck;
- Q3 `resolved-current`, Q9 open, and the temporal moving surface and blocker both bound exactly to `[Q9]`;
- all ten AD-044 pressure classes and all six AD-045 survivors unchanged;
- the `09:54Z → false`, `09:55Z → true` causal probe;
- all protected historical bytes unchanged; and
- promotion-gate schema 5 with only `EVENT_T6` complete and no active cycle.

Two explicit regression tests fail if Q3 re-enters the open set or if any other currently open question is struck. The named `test_every_defensive_value_is_individually_fixture_and_mutation_live` mutates every scalar in the witness and each protective map, set, token, digest and path individually. Inputs outside the Q3 subject cannot earn the decision.

## 8. Version classification, migration and rollback

OCP-001 §Versioning says pre-canonical `Y` increases for a substantive change, while `Z` is editorial only. Replacing a provisional “until a separate decision” boundary with a final lifecycle decision changes contract meaning. OCP-005 therefore moves `0.2.8 → 0.3.0`; a PATCH would understate the change. The document remains pre-canonical `Draft`, so Canonical SemVer categories do not apply.

No Assignment data, reference or schema migration is required: current derivation already enforces the final boundary and consumer behavior is unchanged. Rollback is one separately reviewed unit restoring OCP-005 `0.2.8` provisional prose/Q3 line, the prior current stable-surface projection, the prior current consumer-need governance scope, and removing AD-046 witness/checker/tests/accounting. Partial rollback is invalid. It reopens Q3 without touching Q9.

## 9. Exact baseline and full-chain anchors

Baseline is `main@ca87815b0198c165cfeec759965656da2ef7b5b2`, tree `19f22c6e7ab274ee7d789238991a20e7d1513e8c`. Each object below was resolved from that tree, reverse-resolved through `git ls-tree -r`, checked for the stated internal token/state, and SHA-256 hashed over the same raw blob bytes.

| Evidence | Reverse-resolved path and stated baseline condition | Git blob | SHA-256 |
|---|---|---|---|
| OCP-001 version rule | `docs/001-ontology-governance/README.md`; `1.0.0 / Canonical`, pre-canonical `Y`/`Z` rule | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-005 before-state | `docs/005-assignment-concept/README.md`; `0.2.8 / Draft`, Q3 open and provisional §8 boundary | `6e6c00e723b15a348e7610d4ca5a1ae23526c52b` | `a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065` |
| OCP-016 G4 | `docs/016-core-boundary/README.md`; `1.0.0 / Canonical`, exact G4 route boundary | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| Accepted consumer | `docs/023-resource-occupancy/README.md`; `0.2.0 / Accepted`, §7 reuses Establishment-at-evaluation boundary | `a846333fae80aff2b3697e811d2b155c91f04122` | `5ec9aca56de4524b4ab78a9e98e2cf5d7561d6f13bac8cf7778d66a99f5490d9` |
| current blocker projection before-state | `architecture/assignment-stable-surface.yaml`; Q3+Q9 temporal blocker | `eea05626eddfba594508c5e6d4c4d5bd851c0f5a` | `b887717a064d479830b7aa0f360d2793a3cba4e54d2b1537d19374e553b3b593` |
| AD-039 witness | `architecture/assignment-temporal-scope-attempt.yaml`; baseline gap separation and pre-Establishment control | `9fa12f7c527c7d66ebbba24cf063fc353973d8ae` | `4a8899d58ddf9edcf613760d330ff0003a3f982c1d6c188c4283c52fc364f7fb` |
| AD-044 witness | `architecture/assignment-consumer-pressure.yaml`; ten resolution classes and six survivors | `2a96810984b79374c04bff20663cbc6953744c3d` | `d20f8b8330b4efdb6a23c09aa6f02b2182182ddd022486c370b11afb1d8f61b2` |
| AD-045 witness | `architecture/assignment-norm-compatibility.yaml`; two prospective temporal survivors | `7abda1ed215fb15a520e56682c442db9c9e042b4` | `6e32c5ed98df564c4cf23b1791bff86a80772ecd6be2135ab786d924ac4066dd` |
| causal fixture | `tools/ontology_checker/fixtures/assignment/valid-established.yaml`; valid Established Assignment | `354de6880fe59429c40179eedd4037e52ff5208a` | `3f2ea38f35292b821a7297ed4604a1764efd12c5399ee61a64ea7a2aa5b91117` |
| promotion gate | `architecture/foundation-promotion-gate.yaml`; schema 5, `EVENT_T6` complete, `active_cycle_id: null` | `78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1` | `ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd` |

## 10. Accounting, safety and non-implications

AD-046 begins `0.1.0 / Accepted` as the separately authorized Board lifecycle record. It adds no fixtures and eight test methods; machine-derived accounting moves from `302 / 378` to `302 / 386`.

No test or document adds operational data. The reused synthetic fixture contains only abstract identifiers and the already governed synthetic `2026-08-02` timestamps; no coordinate, route, organization/unit, person, credential, key or token is introduced.

AD-046 does not close Q2, Q5 or Q9; remove `TEMPORAL_MODEL_UNRESOLVED`; change the six AD-045 survivors; define recording/ingestion/correction/authentication semantics; activate a positive model; select or promote Assignment; canonicalize its Concept; start a promotion cycle; open T7; or authorize another act. Q9 remains the exact reason the temporal whole-document-freeze blocker survives.
