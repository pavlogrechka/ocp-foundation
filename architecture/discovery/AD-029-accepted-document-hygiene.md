---
Decision-ID: AD-029
Title: Accepted Document Snapshot Governance and Presentation Debt
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: OCP-001, OCP-011, OCP-012, OCP-013, OCP-014, OCP-015, OCP-016, OCP-017, OCP-018, OCP-020, AD-028
Applies-To: Accepted OCP lifecycle evidence, OCP-016 retained acceptance evidence
---

# AD-029 — Accepted Document Snapshot Governance and Presentation Debt

## 1. Decision and bounded result

This governance-hygiene act closes the reviewed-snapshot debt registered by OCP-020 §18. Every current primary OCP whose document `Status` is exactly `Accepted` must have one declared sibling snapshot of the reviewed pre-acceptance contract. The declaration binds the OCP identity, current primary path and status, reviewed version, exact filename, SHA-256 content and retention basis. Missing evidence, an unregistered Accepted primary, a wrong name, changed bytes, an absent primary link or a mismatched current status fails the repository check.

Canonical status alone does not trigger that rule. OCP-016 is the sole separately declared retained-acceptance-evidence case because its current Canonical primary expressly incorporates the immutable Draft that supported its earlier Accepted contract. The other current Canonical OCPs did not acquire their status through the same retained snapshot representation and gain no synthetic snapshot obligation here.

The second OCP-020 §18 debt is not repaired in place. A predeclared repository-wide inventory finds mixed current-primary Draft self-assertions in three Accepted and five Canonical OCPs. Editing the complete class would change Canonical artifacts and, for OCP-017/OCP-018/OCP-020, the incorporated reviewed bodies and section anchors. This mandate authorizes neither effect. The exact inventory and the shortest lawful next act are registered in §§7–8.

## 2. Exact baseline and anchor method

This act starts from exact `main@0f1f266a171bb0d0bc7d64503a3853f50d69cd3b`, tree `951b1fff8485f9d05f152f1f90864c783b98d069`. It does not reuse PR #147 or any merged feature branch as a semantic baseline.

Every baseline anchor below was resolved at that commit, reverse-resolved through `git ls-tree -r` to the stated path and independently SHA-256 hashed over raw blob bytes.

| Input | Reverse-resolved path | Git blob | SHA-256 |
|---|---|---|---|
| OCP-001 | `docs/001-ontology-governance/README.md` | `33524fa3d18f3253faa9a854500be7ddfb20815f` | `da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc` |
| OCP-011 primary | `docs/011-outcome-assessment-record/README.md` | `ff2608a372c6305db4c290f05c15e961ca96e6f6` | `1fb08e18fab560e671b468585d699a7d70bd55ed5be674315cb780a48bc70cc5` |
| OCP-012 primary | `docs/012-capability-claim-record/README.md` | `cd2df0f1961b6d03eea0db66c8fdfce1f97cb235` | `d4d5b4441cf2d1f7fea2dae572fcfa60f22b0ebce0e23ae6a86f71d9f4edd122` |
| OCP-013 primary | `docs/013-resource-interchangeability/README.md` | `658a291b4c3b9a0229aba09d485c1137723fe70b` | `a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74` |
| OCP-014 primary | `docs/014-coordination-profile/README.md` | `23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99` | `72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c` |
| OCP-015 primary | `docs/015-coordination-workflow/README.md` | `ea60634e54faedabb8c5e08b036030c2f0e4e20b` | `6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d` |
| OCP-016 primary | `docs/016-core-boundary/README.md` | `94f5d997deea0168a3c553c2ac9f19d2ee03b4fb` | `78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4` |
| OCP-017 primary | `docs/017-operation-lifecycle/README.md` | `0b2ea683df308babd1111ff47e9272c9b0742f78` | `061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030` |
| OCP-018 primary | `docs/018-operation-authorization-source/README.md` | `dc3148869f47af2bb27eb2fa74a188136d5fb568` | `e105e9c230277b6865721192ef4044ee77d9bfbff73505d164d7760c8ac31779` |
| OCP-020 primary | `docs/020-quantitative-constraint-input/README.md` | `0e1e7d0947ab3c7d1c0355258651179f618636a2` | `1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c` |
| artifact taxonomy | `architecture/artifact-taxonomy.yaml` | `fa0b6b5ade944f09f12f8597f33d1cf1522b8db3` | `247d15bb60afb5348d122fab07f43550e552ae615074830718b3f658e213c938` |
| checker entry point | `tools/ontology_checker/check.py` | `6ab4f5e6f4fad5ba600ab05efb0cf08c8de4e553` | `e9fb3af92a3051ad0ac8f9703a2fe2248cec5c5d8e5d8607fa87c8dcbf92ee28` |
| repository README | `README.md` | `950b3ecac451a986ec2f911e1989e6bd058a9484` | `810d40cd0321d0a4ef2402912b00ccd5ba4899acd18946ce4308fbe29ddc1343` |
| roadmap | `backlog/roadmap.md` | `35db355a7ff62cdf591e59988cb125c88d8458c5` | `842757e6ab2eaf5b686c992f7c909c97b9b3f9fdb55c1af9f230e271c50e74d3` |

## 3. Predeclared snapshot criterion

The criterion was fixed before enumerating files.

1. The current carrier is every primary `docs/*/README.md`, identified by exact `Document-ID` and current document `Status`; `Concept-Status` is irrelevant.
2. Every current `Status: Accepted` OCP must resolve to exactly one map entry with basis `current-accepted` and one sibling `reviewed-contract-v<reviewed-version>.md`.
3. The filename is derived from the reviewed Draft version, not the current Accepted version. The primary must link that exact basename, and the snapshot bytes must equal the declared SHA-256.
4. `Canonical` does not imply this obligation. A Canonical entry is admissible only as an explicit `retained-acceptance-evidence` exception whose current primary incorporates the same snapshot; it does not create a rule for other Canonical OCPs.
5. Draft OCPs, Patterns, ADs, ADRs, review records, fixtures and operational input snapshots are outside this governance class.
6. The map is evidence binding, not lifecycle authority: it cannot make a document Accepted, Canonical or approved.

## 4. Complete snapshot inventory and OCP-016 interpretation

The scan finds twenty-two primary OCP documents: eight Accepted, nine Canonical and five Draft. Exactly nine sibling reviewed-contract files exist.

| OCP | Current status | Reviewed version | Snapshot SHA-256 | Basis |
|---|---|---:|---|---|
| OCP-011 | Accepted | 0.1.1 | `1c293a9b58ddd3a14a73bc3e614e24fce9dfa0f458a968c44d2ac350d708ff3f` | current Accepted requirement |
| OCP-012 | Accepted | 0.1.0 | `a397323ee69863790e55f1b548bce3946100797abe03b464d642e0261c76db55` | current Accepted requirement |
| OCP-013 | Accepted | 0.1.0 | `64df2a408a70edbf40c27b1d9d294d04426e063506792f6dc1d95af658e6371b` | current Accepted requirement |
| OCP-014 | Accepted | 0.1.0 | `022580c6731414a533736171c5cfc111ff311fd75adc0462cb7095697a7fd0ac` | current Accepted requirement |
| OCP-015 | Accepted | 0.1.0 | `08f0d972c327a8572551821f66beb7675fad407cccda94f057eeb4780fc3826e` | current Accepted requirement |
| OCP-016 | Canonical | 0.1.0 | `111e676ac750a2bfbe17d34fb1e8d2984af860fd38c856b824b4aff8c261c155` | retained acceptance evidence |
| OCP-017 | Accepted | 0.1.0 | `e3fc44295a8182eb97c3e39cd407daadc3434b49000b74fd4926cfa4e420cb28` | current Accepted requirement |
| OCP-018 | Accepted | 0.1.0 | `7b60d478ac15ced656eaee2d6a7062ca1c0291e6dadc6dccae85787f700df077` | current Accepted requirement |
| OCP-020 | Accepted | 0.1.0 | `05992f1006dee9c2dca137e6145f3c5c70ce57746bb0febb79a3ca9598146bb8` | current Accepted requirement |

OCP-016 §§1 and 10 say that the externally reviewed Draft is preserved verbatim and incorporated into the Accepted specification. Its later §§11–15 then move the same primary to Canonical while retaining that incorporated evidence. The snapshot therefore survives canonicalization as historical acceptance evidence; Canonical status does not newly require it. OCP-000 through OCP-009, other than OCP-016, have no snapshot and remain valid because their Canonical acts used a different evidence representation.

## 5. Outcome-fair placement comparison

| Outcome | Authority fit | Mechanical fit | Cost and boundary | Result |
|---|---|---|---|---|
| G1 — amend OCP-001 | Natural long-term owner of OCP lifecycle and atomic promotion evidence | checker can implement it directly | adds a new compatible obligation to `1.0.0 / Canonical`, requiring a separately authorized Canonical MINOR act | lawful future route, not authorized now |
| G2 — extend `artifact-taxonomy.yaml` | central machine-readable artifact policy | concise global declaration | changes the protected global taxonomy/governance surface and still needs readable normative authority | not authorized now |
| G3 — create a new OCP contract | could own a reusable document-governance contract | machine map could bind it | invents a new primary lifecycle artifact and routing problem for a finite hygiene invariant already within Board governance | disproportionate |
| G4 — Board act + bounded map + advisory checker | AD is binding under the unchanged taxonomy and can close the registered finite debt | exact current Accepted coverage, retained exception, name, link and digest are directly executable | does not mutate Canonical OCP-001 or taxonomy; future OCP-001 incorporation remains explicit debt | selected |

G4 is selected for this act. It is not a claim that AD-029 permanently displaces OCP-001. The shortest durable route is a separate OCP-001 `1.x` MINOR governance act that incorporates the compatible obligation and either adopts or replaces this map without weakening its current checks.

## 6. Machine contract and individual mutation evidence

`architecture/accepted-document-snapshot-map.yaml` declares the exact nine entries. `validate_accepted_snapshots` checks:

1. closed map shape, safe paths, unique OCP identities, exact status/basis vocabulary and the declared OCP-016 retained set;
2. equality between all discovered current Accepted OCP IDs and all `current-accepted` map IDs;
3. exact current primary identity/status and same-directory `reviewed-contract-v<reviewed-version>.md` naming;
4. exactly one sibling reviewed-contract snapshot for each declared carrier;
5. exact SHA-256 bytes and an exact primary Markdown link to the mapped basename; and
6. OCP-016 as Canonical retained evidence, not as a generalized Canonical requirement.

Six new unit-test methods provide individual rather than sampled evidence. For every one of the nine entries, deleting the snapshot fails, renaming the same bytes to `reviewed-contract-v9.9.9.md` fails, changing its bytes fails, removing its primary link fails and changing its current status fails. Removing any mapping separately fails coverage, including retained OCP-016; a direct Draft-to-Accepted mutation of OCP-019 without a map entry also fails. The exact nine identity/primary-path/status/version/snapshot-path/digest/basis tuples and the exact retained set are asserted, so removing or silently rewriting a declared element cannot leave the suite green.

The mutation controls produce `ACCEPTED_SNAPSHOT_MISSING`, `ACCEPTED_SNAPSHOT_NAME_MISMATCH`, `ACCEPTED_SNAPSHOT_CONTENT_MISMATCH`, `ACCEPTED_SNAPSHOT_DECLARATION_MISSING`, `ACCEPTED_SNAPSHOT_PRIMARY_INVALID` or `ACCEPTED_SNAPSHOT_COVERAGE_MISMATCH` as applicable. This is the required proof that an acceptance without its snapshot, with a mismatched name or with mismatched content fails the build.

## 7. Predeclared Draft-self-assertion criterion and complete inventory

The second criterion was also fixed before applying it to all twenty-two current primary OCP documents.

1. A carrier is current primary prose that identifies the same document, exact OCP revision or the current primary as `Draft` in present-tense or present-effect language while frontmatter is Accepted or Canonical.
2. The carrier remains in scope when a later bridge correctly labels it historical: that bridge prevents lifecycle ambiguity but does not normalize the mixed primary presentation that OCP-020 §18 registered.
3. Frontmatter, immutable reviewed-contract snapshots, lifecycle values of domain records, exact baseline tables, hypothetical future rollback destinations such as “may return to Draft”, other-document references and generic process language such as “Draft PR” are excluded. A preserved active instruction that still says rollback removes “the Draft contract” remains a self-assertion and is included.
4. The detected forms are: `This <version> artifact is Draft`; `<document> remains Draft`; `<version> is a Draft revision`; `this Draft` as the current contract/change; and an expired `until merge` statement that says the reviewed Draft remains current.

The complete result is twenty-four carriers in eight current primaries:

| Current primary | Current status | Carrier group | Later current-authority bridge |
|---|---|---|---|
| OCP-003 | Canonical | §18, one present-status assertion | §21 explicitly time-bounds §18 |
| OCP-004 | Canonical | §§22–25, six assertions | §§22–24 are versioned PATCH records; §26 time-bounds §25 and establishes current Canonical authority |
| OCP-007 | Canonical | §§24 and 31, three assertions | §33 time-bounds §§1–32 and specifically §31 |
| OCP-008 | Canonical | §18, one assertion | §19 explicitly time-bounds §§17–18 |
| OCP-016 | Canonical | §10, one expired pre-merge current-Draft assertion | §§11–15 establish current Canonical authority |
| OCP-017 | Accepted | §§1, 16 and 17, three assertions | §18 and §22 establish current Accepted authority |
| OCP-018 | Accepted | §§1, 4 and 15, four assertions | §17 and §§27–28 establish current Accepted authority |
| OCP-020 | Accepted | §§1, 4, 10, 13 and 14, five assertions | §§15 and 21–23 establish current Accepted authority |

OCP-020 §18 named only OCP-017, OCP-018 and OCP-020. That registration was directionally correct but incomplete for the repository-wide class. The five Canonical carriers above are not lifecycle errors because their later bridges are explicit, but they prove that normalization cannot honestly be scoped only to three Accepted documents.

## 8. Presentation normalization disposition

No carrier in §7 is edited here. A complete normalization would require one of two separately reviewed strategies:

1. **wrapper replacement** — move historical bodies out of current primaries and preserve exact snapshots/section addressability through a governed compatibility map; or
2. **in-place qualification** — edit each assertion to carry an explicit historical baseline while proving that every manifest `source:` section anchor and incorporated-body guarantee still resolves to unchanged semantics.

The first strategy changes current primary structure and source resolution. The second changes Canonical OCP-003/OCP-004/OCP-007/OCP-008/OCP-016 and breaks the exact byte-stability claims for the incorporated bodies of OCP-017/OCP-018/OCP-020 unless those claims and snapshots are simultaneously re-governed. Either is a broader act. The shortest lawful next step is a separate outcome-fair presentation-normalization act over all eight primaries, with exact anchor replay before any bytes change. Partial cleanup of only OCP-017/OCP-018/OCP-020 is rejected because it would falsely claim closure of the wider class.

## 9. Accounting and unchanged surfaces

The reference suite grows from 234 to 240 unit tests. Fixture count remains 239 because this is repository governance, not operational behavior; no imitative fixture is introduced. Readiness percentages remain unchanged because the act closes evidence-governance drift without adding a domain capability.

No primary OCP, reviewed-contract snapshot, OCP-000 row, Concept taxonomy/graph, foundation map, P-001 byte, normative semantic rule manifest, operational checker module, fixture, AB status or `Review-After` value changes. OCP-001 and `artifact-taxonomy.yaml` remain byte-identical. This act changes no lifecycle status and grants no Canonical status, production authority or T6 permission.

## 10. Migration, rollback and future incorporation

No domain data, record or consumer migration exists. The nine current snapshots already satisfy the new map; the only migration is from an unenforced repository convention to an explicit finite governance check.

Rollback removes AD-029, the map, validator, six tests and accounting text atomically and returns to the registered OCP-020 §18 debt. It does not remove or rewrite any snapshot and cannot alter an OCP lifecycle by implication.

A future Accepted OCP must add its exact snapshot and map entry in the same lifecycle act. A future canonicalization of an Accepted OCP must explicitly retain or migrate that evidence; deleting it silently is invalid. Incorporating this rule into OCP-001 requires its own Canonical act and must preserve every current fail-safe result.

## 11. Exact-head gates

Merge requires all four gates on one unchanged head: exact-head Fable external review, Codex adjudication, green required CI and fresh explicit Pavlo/Architecture Board authorization. Any head change resets all four. Only squash merge is admissible, and authorization for this act cannot transfer to another PR, head or act.
