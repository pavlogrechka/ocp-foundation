---
Decision-ID: AD-028
Title: Resolved Backlog and Open-Question Synchronization
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-001, OCP-002, OCP-005, OCP-006, OCP-010, OCP-011, AD-010, AD-022, AD-025, AD-026, AD-027
Applies-To: AB-025, AB-036, AB-037, AB-056, AB-059
---

# AD-028 — Resolved Backlog and Open-Question Synchronization

## 1. Decision and scope

This is a governance-hygiene act. It synchronizes twelve exact current-question mirrors with five already Resolved Architecture Backlog items, while preserving each original prompt as struck historical evidence and appending the exact current disposition. It changes no Architecture Backlog status and makes no semantic selection.

The act also introduces a bounded machine-readable resolution map and checker rule. That rule proves only the declared finite inventory: a mapped question must remain struck in its named current document, its named AB must remain `Resolved`, and its exact resolution reference must remain on the same line. It does not infer semantic similarity or prove that a future author found every possible mirror.

## 2. Exact baseline and anchor chain

This act starts from exact `main@3d6c7bf2329e81476786fb98a14a6dcb7999fcd5`, tree `ddeae6291aec28d8aa8000e3b7f06fde4d0bf0aa`. It does not reuse the merged PR #146 branch as a semantic baseline.

Every baseline anchor below was resolved to its Git blob, reverse-resolved to the declared path and SHA-256 checked over raw blob bytes.

| Input | Reverse-resolved path | Declared baseline state | Git blob | SHA-256 |
|---|---|---|---|---|
| architecture backlog | `backlog/architecture-backlog.md` | 34 rows are `Resolved`; no status changes are authorized | `5ce3e43b3752ce40794f3c19933227739df38a37` | `4824d87d9256982052b5700269c6ca96be02c0fb1d931acd2b9b7d971e3fba71` |
| global questions | `backlog/open-questions.md` | 12 prompts; none struck | `aa8969b7cc581c69ae58f88af5c5a4f1d8c800b7` | `28c2441fd35fcb683b5f1574696c3e74c524b35048b511cf622cad8b63ce32d5` |
| OCP-002 | `docs/002-concept-taxonomy/README.md` | `1.5.0 / Canonical`; six future-review prompts | `aaa4ac27a7d77c52b74833a1c088c037538f1f06` | `335f3e8c2f51110f192ceb608188437b6d2fe5b908bbf12894c31e45a651e7c6` |
| OCP-005 | `docs/005-assignment-concept/README.md` | `0.2.6 / Draft`; eleven §19 prompts | `6e78d6d54d53260fb42f4ef67776e3cf8b11daa7` | `fd77fbdc47d1d436a95c95c6a211521d65dd5261633ccd2eee17f9a761fef3ba` |
| OCP-006 | `docs/006-constraint-concept/README.md` | `0.3.0 / Draft`; twelve §22 prompts, two already struck | `579eec572a65e983828e9d988a92dec2700e41e3` | `02f6a6f88277eabe0badd6eabd4179aa796751f9466dcadb88db16f3a878d71d` |
| OCP-010 | `docs/010-event-concept/README.md` | `0.2.0 / Draft`; five §22 prompts | `d73bab07acac3c316a9a2a4f4d25cb1f9b1bdc06` | `f66a2deb2bd8748aa464adefe3f4ff5ac35baf6af017fb9c782f9a427d7ac95f` |
| OCP-011 | `docs/011-outcome-assessment-record/README.md` | `0.3.0 / Accepted`; AB-056 current owner | `ff2608a372c6305db4c290f05c15e961ca96e6f6` | `1fb08e18fab560e671b468585d699a7d70bd55ed5be674315cb780a48bc70cc5` |
| AD-010 | `architecture/discovery/AD-010-cross-vertical-visibility-agreement.md` | `0.3.0 / Accepted`; V0 and A0 selected | `f769d9292d9f5209c8ee35366257836b1222857f` | `8a4778ba679784634d166984dd3489b87f3680f5daa8970921c67f1a8314d488` |
| AD-022 | `architecture/discovery/AD-022-conflict-derivation-boundary.md` | `0.1.0 / Accepted`; H0-B only, AB-018 open | `daba3472caaa650c41231437bddba1a70d895230` | `a52f0fb9cab2bdd32f23e5f2c529c4c76db1ffd8efe1ae6046fc3dda23747d54` |
| AD-025 | `architecture/discovery/AD-025-quantitative-constraint-input.md` | `0.1.0 / Accepted`; QC selected for AB-037 | `cd4e320be2db6398d758c6fa3ae49e0a0f520df5` | `dae3ee9ea8ffbe0fb62df127fa53920705d59f50ec793cb41cb6ca3c10642d46` |
| AD-026 | `architecture/discovery/AD-026-reservation-allocation-boundary.md` | `0.1.0 / Accepted`; EN/QN selected for AB-025 | `ad109d1003af32a019e6b525b4552db2c6e323b2` | `e258d714d242a5065b23c296a413a6d0d8c52e72d967b42798153888f6d872bd` |
| AD-027 | `architecture/discovery/AD-027-constraint-interaction-boundaries.md` | `0.1.0 / Accepted`; AN/ON/WN selected for AB-036 | `fa49556df4f06aa039df23d9cc244587411b2d5e` | `8d62725e4f8b1513c85fd24d59017215da94ddef8cda5244f300a6f25a0ee442` |
| P-001 | `patterns/P-001-identified-record-pattern.md` | `0.1.0 / Accepted`; outside this hygiene act | `c679f3e35eb015aecf6cb9a839aacd75a432e844` | `2c9dd172a19c2d340b58a159fe5e71b64215a3968ee05fa330790b7e6359c797` |
| checker entry point | `tools/ontology_checker/check.py` | no open-question validation | `ca136fb192f8ae6acc05e3e6eb8239a42f40795d` | `3b78a95adb8ce2f7b37c4b45340f0ed72ec09f7cc28db873327267dbee2505d0` |
| artifact governance | `tools/ontology_checker/ocp_checker/artifact_governance.py` | AB statuses validated; no AB↔question map | `021b0c2da482d1d6b09cfd8f76d9da2feeecb031` | `3bd03d57e574bffd28eb0630b45afdd424c0eb06d3a37600aa62acfaac6feb13` |
| repository README | `README.md` | 231 tests and 239 fixtures | `fb4d83de45bd64d00f88f600a7ebc49459d7909d` | `53d64b20a5cf6fa595c8a85e48f928bc567965749ce09ad1a4d7c6ade1d487ce` |
| roadmap | `backlog/roadmap.md` | 33% operational, 77% enforcement, ≈72% overall | `a18161083c7c271c73e36a66f88466cb9a395649` | `8fd2c66f347408ee2a52e730db99bedce473cd07de47ee403e7621a448c2088a` |

## 3. Predeclared mirror criterion

The criterion was fixed before scanning.

1. A current question is a mirror only when its subject and full requested scope match a `Resolved` AB disposition.
2. The backlog-to-AD/OCP chain must directly show that the act gave the current final answer to that prompt. Topic overlap, a shared noun or `Resolved` alone is insufficient.
3. Strikeout is permitted only for a fully dispositive current answer. A bounded negative answer is dispositive when the same AB is explicitly `Resolved` by a selected no-establishment/no-new-authority outcome over every alternative named by the question and records a future reopening gate; it is not dispositive when the act is partial, consumer-local, transfers the requested positive subject to a separate Open owner or the question explicitly asks for future reopening evidence.
4. Historical reviewed-contract snapshots are evidence and remain byte-unchanged. The scan covers only current question carriers: `backlog/open-questions.md` and current primary OCP README sections explicitly named as questions/future-review prompts.
5. A mixed prompt is struck only if every clause has a current disposition. Otherwise it stays open and the partial resolution is registered here.

## 4. Complete carrier inventory

The rule finds 58 current question items in seven carriers:

| Carrier | Current items at baseline | Adjudication |
|---|---:|---|
| `backlog/open-questions.md` | 12 | five exact mirrors; seven remain open |
| OCP-002 future-review section | 6 | zero exact full-scope mirrors; unchanged by mandate |
| OCP-004 §20 | 7 | zero exact full-scope mirrors |
| OCP-005 §19 | 11 | two exact mirrors; nine remain open |
| OCP-006 §22 | 12 | two prior exact mirrors plus two newly synchronized; eight remain open |
| OCP-008 §16 | 5 | zero exact full-scope mirrors |
| OCP-010 §22 | 5 | one exact mirror; four remain open |

Thus ten previously unstruck items are synchronized and the two AD-027 items already struck by PR #146 are admitted to the same enforced map. The resulting current inventory has twelve resolved mirrors and forty-six still-open items. A heading/template mention without a question item, prose review target and immutable reviewed snapshot are not carriers.

## 5. Exact resolved mirrors

Each finite item below is represented one-for-one by `QSYNC-001`…`QSYNC-012` in `architecture/open-question-resolution-map.yaml`.

| IDs | Carrier and item | Current disposition |
|---|---|---|
| QSYNC-001 / AB-059 | global 4, cross-vertical visibility | AD-010 §§25–26 selects V0 publisher envelope only |
| QSYNC-002 / AB-059 | global 7, agreement/confirmation/withdrawal | AD-010 §§25–26 separately selects A0 OCP-015 evidence only |
| QSYNC-003 / AB-036 | global 10, precedence/override/exception/waiver | AD-027/OCP-006 §27 selects AN/ON/WN |
| QSYNC-004 / AB-037 | global 11, quantity/demand/capacity/units | AD-025/OCP-020 accepts bounded exact-unit input and aggregation; positive capacity remains gated |
| QSYNC-005 / AB-025 | global 12, Reservation form | AD-026/OCP-021 selects EN/QN negative establishment boundaries |
| QSYNC-006 / AB-025 | OCP-005 §19.1 | same current EN/QN answer |
| QSYNC-007 / AB-025 + AB-037 | OCP-005 §19.6, reserved/consumed quantity | accepted consumed input plus no established reservation covers both clauses |
| QSYNC-008 / AB-036 | OCP-006 §22.3 | prior AD-027 application-order/override answer, preserved |
| QSYNC-009 / AB-036 | OCP-006 §22.4 | prior AD-027 waiver answer, preserved |
| QSYNC-010 / AB-037 | OCP-006 §22.5 | same bounded OCP-020 quantity/capacity disposition |
| QSYNC-011 / AB-025 | OCP-006 §22.9 | same EN/QN Reservation disposition |
| QSYNC-012 / AB-056 | OCP-010 §22 item 5 | OCP-011 §§2–8 now owns accepted targets, conclusions, supersession and authority boundary |

Negative answers are not treated uniformly. AB-025, AB-036 and AB-059 are fully dispositive for the exact current-control questions above, just as PR #146 preserved the prompt while recording AN/ON/WN. AB-038 is not: its H0-B lower boundary explicitly leaves AB-018's requested positive Conflict model open.

## 6. Resolved ABs with lawful still-open topical questions

Fourteen Resolved rows overlap current question text without satisfying the full mirror criterion:

| Resolved AB | Current question surface | Why it remains open |
|---|---|---|
| AB-003, AB-058 | global 3 and the coordination domain | accepted proposal/response workflow does not define simultaneous organizational/operational/coordination affiliation; global 7 is instead answered by later AB-059 |
| AB-004, AB-060, AB-061 | global 5 | Capability registry/support and Core routing do not settle the broader Core-versus-domain Capability vocabulary boundary |
| AB-007 | global 1 | it explicitly asks for new decision-separating reopening evidence after S0/R0 |
| AB-008 | global 6 | local spatial/environment binding does not decide Spectrum identity/category |
| AB-011 | OCP-005 §19.11 | interchangeability deliberately grants no replacement policy or selection authority |
| AB-017 | OCP-004 §20.1 and §20.5 | OCP-018 accepts one source profile, while source legitimacy and multiple independent sources remain separately gated |
| AB-038 | global 8, OCP-005 §19.8, OCP-006 §22.1 | H0-B proves `violation ≠ Conflict`; AB-018 and every positive Conflict form remain open |
| AB-039 | OCP-006 §22.6, OCP-008 §16.4, OCP-002 future-review freshness item | F1/A1 is activated only for exact `objective-achievement@2`, not every dynamic input, target or evidence kind |
| AB-054, AB-055 | OCP-002 Operation-to-Event item and OCP-010 §22 first four items | accepted Event/Result boundary and occurrence contract leave time model, relation owner, correlation rules and kind registry separate |
| AB-063 | OCP-008 §16.2 | the prompt asks for future evidence that could reopen the already selected strict-immutability answer |

OCP-002's mixed `Reservation, Allocation, Role Taxonomy or Conflict` prompt also remains open: AB-025 disposes only Reservation/Allocation at the current negative boundary, while AB-027 and AB-018 remain Open. The Canonical OCP-002 byte surface is therefore unchanged.

## 7. Resolved ABs with no current mirrored question

The remaining fifteen Resolved rows have no current question satisfying subject plus full-scope matching: **AB-012, AB-014, AB-021, AB-022, AB-024, AB-031, AB-032, AB-033, AB-034, AB-040, AB-041, AB-042, AB-043, AB-053 and AB-057**.

Their absence from the resolution map is explicit. The act does not manufacture a question merely to make every Resolved row symmetrical.

## 8. Mechanical enforcement and mutation proof

`architecture/open-question-resolution-map.yaml` declares exactly twelve IDs, AB bindings, current documents, exact question text and exact resolution references. `validate_open_question_sync` checks:

1. map shape, unique `QSYNC-NNN` IDs and safe current Markdown paths;
2. every named AB is exactly `Resolved` in the authoritative backlog;
3. each exact question occurs once as `~~question~~`; and
4. its exact resolution reference occurs on the same line.

The test suite validates the live repository, changes AB-025 from `Resolved` to `Open` as a negative control, and removes strikeout from each QSYNC item one at a time. All twelve individual mutations must fail with `OPEN_QUESTION_RESOLUTION_MISSING`. This is individual evidence for every declared finite item, not categorical sampling.

The checker cannot infer whether an unlisted future question is semantically equivalent to an AB. That completeness judgment remains an exact external-review obligation until a future act defines stable question identities and a normative semantic ownership model. The claim here is deliberately limited to the declared map.

## 9. PATCH documents and unchanged semantics

- OCP-005 advances `0.2.6 → 0.2.7 / Draft` and synchronizes §19 items 1 and 6.
- OCP-006 advances `0.3.0 → 0.3.1 / Draft` and synchronizes §22 items 5 and 9 while preserving items 3 and 4.
- OCP-010 advances `0.2.0 → 0.2.1 / Draft` and synchronizes §22 item 5.
- `backlog/open-questions.md` gains five struck current dispositions without changing any AB row.
- The AB-036 backlog explanation updates only the current OCP-006 PATCH version; all 34 `Resolved` values and every other row disposition remain unchanged.

These are PATCH changes because they only reconcile current governance prose with acts already in force. They add no field, record, lifecycle, derivation, authority, Concept, status, dependency, graph edge, Pattern invocation, normative semantic rule or fixture.

## 10. Optional debt disposition

This act does not normalize the mixed Accepted-document representation of OCP-017/OCP-018/OCP-020 and does not normatively define or enforce the reviewed-contract snapshot convention. Both debts remain registered by OCP-020 §18.

Combining them here would dilute exact review: representation normalization would touch three Accepted current documents, while snapshot enforcement needs a separate normative definition and migration audit across every Accepted contract. Neither is required to make the twelve question mirrors mechanically coherent.

## 11. Accounting, migration and rollback

The reference suite grows from 231 to 234 unit tests because the new governance invariant is executable. Fixture count remains 239: no operational behavior or semantic fixture class changes. Readiness percentages remain 33% operational, 77% machine enforcement and ≈72% overall because this repairs governance drift rather than adding a domain capability.

There is no data or record migration. Rollback removes AD-028, the map, validator and three tests; restores the ten question lines and three PATCH versions; and reverses README/roadmap/checker accounting atomically. Rollback must not change any AB status or reopen/resolve a semantic question by implication.

## 12. Explicit non-effects and safety

This act does not modify OCP-000, OCP-002, any Concept status, Concept graph, foundation map, P-001 bytes, reviewed-contract snapshot, normative rule manifest, operational checker module or fixture. It does not make an artifact Canonical, accept OCP-019/OCP-021, authorize a production profile, open T6 or change `Review-After`.

All added evidence is repository-governance text and synthetic mutation data. It contains no real frequency, coordinate, unit designation, operational time window or material from another project.

## 13. Exact-head gates

Merge requires all four gates on one unchanged head: exact-head Fable external review, Codex adjudication, green required CI and fresh explicit Pavlo/Architecture Board authorization. Any head change resets all four. Only squash merge is admissible, and authorization for this act cannot transfer to another PR, head or act.
