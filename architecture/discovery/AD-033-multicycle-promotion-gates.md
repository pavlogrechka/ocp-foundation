---
Decision-ID: AD-033
Title: Multicycle Foundation Promotion Gate Protocol
Version: 0.1.0
Status: Accepted
Owner: Architecture Board
Depends-On: AD-016, AD-031, AD-032, OCP-001, OCP-016
Applies-To: Foundation promotion gate infrastructure only
---

# AD-033 — Multicycle Foundation Promotion Gate Protocol

## 1. Mandate, G4 and exact boundary

The Architecture Board authorized one infrastructure act on `main@1723c3a26e3d7d99483be771ee69fcae9d55e7f0`: make the promotion gate capable of recording a completed candidate cycle followed by a later cycle without selecting or starting that later cycle now.

Gate-first is resolved before choosing the form. The result is a governance-state protocol, not a positive-capable operational rule, profile, result vocabulary or consumer activation. OCP-016 G4 does not apply and no Accepted activation consumer is required. The current tree after this act still records exactly one completed Event cycle and no active cycle. Capability is not authority: no Assignment/Constraint candidate, discovery scope, T7 step or next act is selected.

## 2. Exact base and full-chain anchors

The exact base tree is `3d1ba0c93530023854ea9c8bfc3d1c8ae2ecc425`. Every row was resolved by blob first, reverse-resolved through `git ls-tree -r`, checked against the state inside the object and SHA-256 hashed from raw bytes.

| Artifact | Reverse-resolved path | Base state | Git blob | SHA-256 |
|---|---|---|---|---|
| promotion gate | `architecture/foundation-promotion-gate.yaml` | schema 4; one hard-coded promoted OCP-010 scope | `d6925eb39473757045aa8266407607b35a6f6a77` | `64571c29fef93a7b7b9598a902ecf932248bc2deb83b0183002b9c8254eb8ef8` |
| gate validator | `tools/ontology_checker/ocp_checker/foundation_promotion_gate.py` | Event-specific completed/next-step constants | `06abe18ded9dfb5564ff9d240778e70298c43c0a` | `47b63a4a86adc5920897d7b28d7efe59dceae83806114912c5dbd1e76c979b06` |
| Event promotion validator | `tools/ontology_checker/ocp_checker/event_lifecycle_promotion.py` | live reader of schema-4 sequence fields | `cc8effe679d69cc1dca9270bc0b190cbd4000d96` | `a2e6b15c509d928b96d7fb2cd54d15a4997dc346c17e5eca0428b21e34fbfc8e` |
| gate tests | `tools/ontology_checker/tests/test_foundation_promotion_gate.py` | one-cycle reachability suite | `a3232f34287b149754c4611b76ef64086949239c` | `0fed9e79583aab5f41d6de8ade849d757d0250408547ff0efe75f40d5ea147ac` |
| Event promotion tests | `tools/ontology_checker/tests/test_event_lifecycle_promotion.py` | schema-4 unfinished-gate mutation | `d81e7f0a3d5eb8f92df79e8913f62fecccd6f97c` | `bf0e199b3ab98e97e903057e97babbc61816b0ab2db325e8d5ff5ab2e8b9e575` |
| checker guide | `tools/ontology_checker/README.md` | single-cycle gate description | `7721e76994ae8a9c8cabe64b651873296f60e3be` | `75e17f6734d09f4124517be8a3a74a0cd0a4851c47122f0525c92f8d87790189` |
| repository accounting | `README.md` | 291 tests / 274 fixtures | `b8ceb282f72c0f8fa882bddf5bb5827c980e8441` | `b546103a79a36ccef34a151bac571d643e288ce84d7afec1e35b361eb25ee31c` |
| roadmap | `backlog/roadmap.md` | completed Event cycle; no next cycle | `ebd85c95b9b18d5d1ee2cfa336e18c0a38539405` | `1d9d8fa9f99e5a2ef7e529c8bab08a3aaaed7ff7fa1cc1ff3570243f50b6e1ef` |
| AB-062 accounting | `backlog/architecture-backlog.md` | Planned; T7 closed | `03ba3bb9dd58dee5495f2b10fb0befa356e925a6` | `4337d3eb4cf0914a4c4aeda51608c6917e2cc58941ba930d10e8340e7161aa60` |

Anchors prove reviewed inputs, not selection or permission.

## 3. Reader criterion and complete inventory

The criterion was fixed before inspection. A location depends on the one-cycle construction if it reads, compares or mutation-tests `selected_next_scope`, `selected_next_scope_state`, `promotion_selections`, `completed_steps` or `required_before_promotion`, or hard-codes their exact single Event terminal state. A baseline-bound location that records those tokens against its own immutable base is historical, not a current reader.

Current readers are exactly: the promotion-gate YAML; `foundation_promotion_gate.py`; its tests; `event_lifecycle_promotion.py`; and the Event lifecycle promotion test that mutates the live gate. README, roadmap, AB-062 and checker guide are current accounting readers without executable parsing.

Historical carriers are `event-stable-surface.yaml`, `foundation-promotion-reassessment.yaml`, `event-promotion-selection.yaml`, their validators/tests and exact-base narratives in AD-016/AD-031. They keep the vocabulary and states of the completed Event chain and remain byte-identical. Their continued validation after schema 5 is an explicit regression proof, not an invitation to migrate them.

## 4. Schema 5 multicycle form

Schema 5 replaces one mutable selection/sequence tuple with:

1. one generic ordered protocol: `CANDIDATE_BOARD_SELECTION → DOCUMENT_PROMOTION → CONCEPT_CANONICALIZATION`;
2. an append-only ordered `cycles` journal, one unique cycle and candidate per entry;
3. per-step `pending|completed` state and non-empty evidence for every completed step;
4. at most one incomplete cycle, always last, named exactly by `active_cycle_id`;
5. candidate status, Concept status and live L2 checked against the cycle state.

The schema version changes `4 → 5` because the serialized shape and reader contract are incompatible: old consumers cannot interpret the journal. The new generic validator is a compatible infrastructure capability, but no OCP document changes and no OCP SemVer is implicated. AD-033 `0.1.0` is the first Accepted infrastructure decision carrying this form.

The repository instance contains only `EVENT_T6`, completed with evidence AD-016AC / AD-016AD / AD-032, and `active_cycle_id: null`. It does not append an Assignment or Constraint entry.

## 5. Executable reachability and retained strictness

Isolated copied-tree tests run the same schema-5 validator code without patching or replacing it:

- the repository state—cycle N complete, N+1 absent—is valid;
- appending an Assignment cycle with selection completed and document/Concept still Draft/Accepted is valid;
- advancing that same copy to Canonical document / Accepted Concept is valid;
- advancing it to Canonical document / Canonical Concept is valid;
- placing document promotion before selection, Concept canonicalization before document promotion or both before selection fails;
- making a candidate Canonical without a matching completed selection/promotion cycle fails;
- selecting live-L2-failing Constraint fails;
- two incomplete cycles, a non-last incomplete cycle or an incorrect `active_cycle_id` fails.

These are capability probes only. Synthetic evidence labels inside temporary test copies never enter repository data and grant no authority.

Every defensive collection and each value remains individually mutation-live under the required test name `test_every_defensive_value_is_individually_fixture_and_mutation_live`. The claim is bounded to declared structural constants and candidate/live-state fields; it does not claim that arbitrary prose is executable.

## 6. Versioning, accounting and boundary

Changed artifacts with a version are AD-033 `0.1.0 / Accepted` and the promotion gate schema `5`. Python modules/tests, README, roadmap, backlog and checker guide have no independent SemVer. No OCP is edited, so OCP-005 remains `0.2.8 / Draft`, OCP-006 `0.3.2 / Draft` and OCP-010 `1.0.1 / Canonical`; Assignment/Constraint remain Accepted and Event Canonical.

No Concept registry/taxonomy, graph edge, P-001 byte, fixture, reviewed-contract snapshot, historical `baseline_*`, AB status or document/Concept lifecycle changes. The `6 Canonical / 2 Accepted` Concept distribution is unchanged. This act opens neither T7 nor an Assignment discovery; it accepts no OCP-019/021/022, opens no AB-018/AB-005 and authorizes no next cycle or act.

The exact base reproduces 291 unit tests and 274 synthetic fixtures. The schema-5 suite replaces one-cycle examples with distinct selected/Draft, document-promoted and fully completed next-cycle reachability checks plus retained skipped-step/history regressions, producing 293 tests and the same 274 fixtures in both checker contexts.
