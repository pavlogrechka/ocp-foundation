from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


CONSUMER_NEED_MAP_INVALID = "CONSUMER_NEED_MAP_INVALID"
CONSUMER_NEED_SCOPE_DRIFT = "CONSUMER_NEED_SCOPE_DRIFT"
CONSUMER_NEED_CANDIDATE_DRIFT = "CONSUMER_NEED_CANDIDATE_DRIFT"
CONSUMER_NEED_POSITIVE_OUTPUT_DRIFT = "CONSUMER_NEED_POSITIVE_OUTPUT_DRIFT"
CONSUMER_NEED_GATE_HISTORY_DRIFT = "CONSUMER_NEED_GATE_HISTORY_DRIFT"
CONSUMER_NEED_EVIDENCE_DRIFT = "CONSUMER_NEED_EVIDENCE_DRIFT"
CONSUMER_NEED_PROMOTION_GATE_DRIFT = "CONSUMER_NEED_PROMOTION_GATE_DRIFT"

ELIGIBLE_LIFECYCLE_IDS = frozenset(
    {
        "OCP-000", "OCP-001", "OCP-002", "OCP-003", "OCP-004", "OCP-007",
        "OCP-008", "OCP-009", "OCP-010", "OCP-011", "OCP-012", "OCP-013",
        "OCP-014", "OCP-015", "OCP-016", "OCP-017", "OCP-018", "OCP-019",
        "OCP-020", "OCP-021", "OCP-022", "P-001",
    }
)
ELIGIBLE_GOVERNANCE_IDS = frozenset(
    {
        "AD-002", "AD-003", "AD-004", "AD-005", "AD-006", "AD-007", "AD-008",
        "AD-009", "AD-010", "AD-011", "AD-012", "AD-013", "AD-014", "AD-015",
        "AD-016", "AD-017", "AD-018", "AD-019", "AD-020", "AD-021", "AD-022",
        "AD-025", "AD-026", "AD-027", "AD-028", "AD-029", "AD-030", "AD-032",
        "AD-033", "AD-034", "AD-037",
    }
)
CANDIDATE_IDS = frozenset(
    {
        "QUANTITY_INPUT_PREREQUISITE", "OPERATION_REQUIREMENT_OWNER",
        "EVENT_OPERATION_RELATION", "INTERCHANGEABILITY_POSITIVE", "COORDINATION_ACTOR_AUTH",
        "COORDINATION_RESIDUAL", "G4_ACTIVATION_RULE", "LIFECYCLE_DOMAIN_RESPONSIBILITY",
        "PRODUCTION_SOURCE_PROFILE", "CAPACITY_RESULT", "CONFLICT_POSITIVE_REOPENING",
        "RESERVATION_POSITIVE_REOPENING", "ORDER_POSITIVE_REOPENING",
    }
)
ESTABLISHED_POSITIVE_IDS = frozenset(
    {"OCP-011", "OCP-012", "OCP-013", "OCP-015", "OCP-017", "OCP-018"}
)
NEGATIVE_GATE_SUBJECTS = frozenset(
    {"conflict", "capacity", "reservation-allocation", "precedence-override-waiver", "order"}
)
FORBIDDEN_OUTCOMES = frozenset(
    {
        "POSITIVE_MODEL_ACTIVATION", "CONSUMER_PROFILE_CREATION", "CONCEPT_OR_GRAPH_CHANGE",
        "STATUS_CHANGE", "AB018_OR_AB005_RESOLUTION", "PROMOTION_CYCLE_START",
        "ASSIGNMENT_REMEDIATION", "NEXT_ACT_AUTHORIZATION",
    }
)

EXPECTED_CANDIDATES = {
    "QUANTITY_INPUT_PREREQUISITE": (
        "OCP-003", "docs/003-resource-concept/README.md",
        "окремий accepted consumable/measurement contract", "quantitative-input-contract", True,
        "satisfied-by-existing-OCP-020-input-not-positive-result",
    ),
    "OPERATION_REQUIREMENT_OWNER": (
        "OCP-009", "docs/009-capability-concept/README.md",
        "Operation requirement representation, holder claims та Resource interchangeability мають окремих normative owners.",
        "operation-requirement-contract", True, "deferred-separate-owner",
    ),
    "EVENT_OPERATION_RELATION": (
        "OCP-010", "docs/010-event-concept/README.md",
        "A future positive relation requires a separately mandated owner act",
        "positive-operation-event-relation", True, "deferred-future-relation",
    ),
    "INTERCHANGEABILITY_POSITIVE": (
        "OCP-013", "docs/013-resource-interchangeability/README.md",
        "A `positive` result remains eligibility evidence only",
        "contextual-interchangeability-positive", True, "already-defined-and-executable",
    ),
    "COORDINATION_ACTOR_AUTH": (
        "OCP-014", "docs/014-coordination-profile/README.md",
        "Actor authentication and authorization require a separate future contract",
        "actor-authentication-or-authorization", True, "explicitly-outside-current-profile",
    ),
    "COORDINATION_RESIDUAL": (
        "OCP-015", "docs/015-coordination-workflow/README.md",
        "AB-059 is the next normative cycle named by this acceptance act.",
        "visibility-policy-or-agreement-semantics", True, "deferred-next-cycle",
    ),
    "G4_ACTIVATION_RULE": (
        "OCP-016", "docs/016-core-boundary/README.md",
        "G4 consumer activation remains binding for positive-capable rules, results and profiles",
        "none-governance-admission-rule", True, "gate-not-consumer-need",
    ),
    "LIFECYCLE_DOMAIN_RESPONSIBILITY": (
        "OCP-017", "docs/017-operation-lifecycle/README.md",
        "A concrete domain must govern those responsibilities separately.",
        "production-domain-source-legitimacy", True, "deferred-production-responsibility",
    ),
    "PRODUCTION_SOURCE_PROFILE": (
        "OCP-018", "docs/018-operation-authorization-source/README.md",
        "Any future production profile must name its own legitimate owner",
        "production-source-profile", True, "deferred-future-production-profile",
    ),
    "CAPACITY_RESULT": (
        "OCP-020", "docs/020-quantitative-constraint-input/README.md",
        "The exact baseline has no Accepted consumer that owns such a result need",
        "capacity-sufficiency-or-reservation-result", True, "explicit-negative-boundary",
    ),
    "CONFLICT_POSITIVE_REOPENING": (
        "OCP-019", "docs/019-conflict-derivation-boundary/README.md",
        "A later positive-capable model must be a separate Board act.",
        "positive-conflict-model", True, "deferred-separate-positive-act",
    ),
    "RESERVATION_POSITIVE_REOPENING": (
        "OCP-021", "docs/021-reservation-allocation-boundary/README.md",
        "Each branch can be reopened only by a separate Board act",
        "positive-reservation-or-allocation-model", True, "deferred-separate-positive-act",
    ),
    "ORDER_POSITIVE_REOPENING": (
        "OCP-022", "docs/022-order-authorization-boundary/README.md",
        "A future positive proposal requires a separate Board act.",
        "positive-order-authorization-model", True, "deferred-separate-positive-act",
    ),
}

EXPECTED_POSITIVE_OUTPUTS = {
    "OCP-011": (
        "docs/011-outcome-assessment-record/README.md",
        "`sufficient` | `achieved`, `not_achieved`, `partially_achieved` or `indeterminate`",
        "outcome-assessment-conclusion",
    ),
    "OCP-012": (
        "docs/012-capability-claim-record/README.md",
        "`effective_capability_claim` may project an activated evidence-backed assertion",
        "effective-capability-claim",
    ),
    "OCP-013": (
        "docs/013-resource-interchangeability/README.md",
        "`positive` — complete exact inputs show that the candidate satisfies the requirement",
        "contextual-interchangeability-positive",
    ),
    "OCP-015": (
        "docs/015-coordination-workflow/README.md",
        "A `positive` projection means only that the required attributable confirmations exist",
        "coordination-confirmation-positive",
    ),
    "OCP-017": (
        "docs/017-operation-lifecycle/README.md",
        "Only `input_state: effective` with `result: passed` satisfies the binding",
        "lifecycle-evidence-binding",
    ),
    "OCP-018": (
        "docs/018-operation-authorization-source/README.md",
        "A unique effective `authorize` head derives `accepted`",
        "authorization-source-accepted",
    ),
}

EXPECTED_GATE_HISTORY = {
    "AD-022": (
        "architecture/discovery/AD-022-conflict-derivation-boundary.md",
        "every positive option lacks a concrete Accepted consumer", "conflict",
    ),
    "AD-025": (
        "architecture/discovery/AD-025-quantitative-constraint-input.md",
        "no positive-capable form may bypass its missing Accepted consumer", "capacity",
    ),
    "AD-026": (
        "architecture/discovery/AD-026-reservation-allocation-boundary.md",
        "no Accepted artifact owns a protected quantitative reservation/allocation result",
        "reservation-allocation",
    ),
    "AD-027": (
        "architecture/discovery/AD-027-constraint-interaction-boundaries.md",
        "no Accepted consumer need, exact positive rule", "precedence-override-waiver",
    ),
    "AD-030": (
        "architecture/discovery/AD-030-order-authorization-boundary.md",
        "lacks Order-specific need, rule, owner/evaluator and form", "order",
    ),
}

EXPECTED_BASELINE_OBJECTS = {
    "docs/003-resource-concept/README.md": ("71485bb337cfd59def2e0f1b18b474a7959bd30c", "f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315"),
    "docs/009-capability-concept/README.md": ("31163eacb0ca2a78b17b9d2466d99ef0c8b2d272", "29362c815cb14f07bfd06775d1398498a27ace5ee5a4acaafde0eb39e902152a"),
    "docs/010-event-concept/README.md": ("a9de19a0873a6616d4c77614acf48d17e1b06bad", "51023373a39056ac70f80d97cea3c529938f82a01c9a1ee1f83410d34ae4f3ed"),
    "docs/011-outcome-assessment-record/README.md": ("ff2608a372c6305db4c290f05c15e961ca96e6f6", "1fb08e18fab560e671b468585d699a7d70bd55ed5be674315cb780a48bc70cc5"),
    "docs/012-capability-claim-record/README.md": ("cd2df0f1961b6d03eea0db66c8fdfce1f97cb235", "d4d5b4441cf2d1f7fea2dae572fcfa60f22b0ebce0e23ae6a86f71d9f4edd122"),
    "docs/013-resource-interchangeability/README.md": ("658a291b4c3b9a0229aba09d485c1137723fe70b", "a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74"),
    "docs/014-coordination-profile/README.md": ("23bd05b4bb14fd7a85101bd5a8b3dd733b53dd99", "72c789c7b15ab2fd8997f60ba8cfd9d89f0e7730407763d18fb222bac5f06a8c"),
    "docs/015-coordination-workflow/README.md": ("ea60634e54faedabb8c5e08b036030c2f0e4e20b", "6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d"),
    "docs/016-core-boundary/README.md": ("94f5d997deea0168a3c553c2ac9f19d2ee03b4fb", "78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4"),
    "docs/017-operation-lifecycle/README.md": ("0b2ea683df308babd1111ff47e9272c9b0742f78", "061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030"),
    "docs/018-operation-authorization-source/README.md": ("dc3148869f47af2bb27eb2fa74a188136d5fb568", "e105e9c230277b6865721192ef4044ee77d9bfbff73505d164d7760c8ac31779"),
    "docs/020-quantitative-constraint-input/README.md": ("0e1e7d0947ab3c7d1c0355258651179f618636a2", "1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c"),
    "architecture/discovery/AD-022-conflict-derivation-boundary.md": ("daba3472caaa650c41231437bddba1a70d895230", "a52f0fb9cab2bdd32f23e5f2c529c4c76db1ffd8efe1ae6046fc3dda23747d54"),
    "architecture/discovery/AD-025-quantitative-constraint-input.md": ("cd4e320be2db6398d758c6fa3ae49e0a0f520df5", "dae3ee9ea8ffbe0fb62df127fa53920705d59f50ec793cb41cb6ca3c10642d46"),
    "architecture/discovery/AD-026-reservation-allocation-boundary.md": ("ad109d1003af32a019e6b525b4552db2c6e323b2", "e258d714d242a5065b23c296a413a6d0d8c52e72d967b42798153888f6d872bd"),
    "architecture/discovery/AD-027-constraint-interaction-boundaries.md": ("fa49556df4f06aa039df23d9cc244587411b2d5e", "8d62725e4f8b1513c85fd24d59017215da94ddef8cda5244f300a6f25a0ee442"),
    "architecture/discovery/AD-030-order-authorization-boundary.md": ("01b7a6f01065b57130f8c0572242d683bcd22108", "6ab90174bc1db423f403ac28a87d9eb0e1f84a7685cce881d94596a2fb9989bf"),
}

MAP_KEYS = {
    "schema_version", "rule_owner", "baseline", "gate_first", "criterion", "result",
    "promotion_gate_guard", "eligible_lifecycle_documents", "eligible_governance_acts",
    "candidate_mentions", "established_positive_outputs", "negative_gate_history",
    "baseline_evidence_objects", "forbidden_outcomes",
}


@dataclass(frozen=True)
class ConsumerNeedDiscoveryResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> ConsumerNeedDiscoveryResult:
    return ConsumerNeedDiscoveryResult(tuple(dict.fromkeys(errors)))


def _frontmatter(path: Path) -> dict[str, Any] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        value = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return value if isinstance(value, dict) else None


def _live_inventory(paths: Iterable[Path], id_fields: tuple[str, ...]) -> dict[str, tuple[str, str, str]]:
    result: dict[str, tuple[str, str, str]] = {}
    for path in paths:
        metadata = _frontmatter(path)
        if metadata is None or metadata.get("Status") not in {"Accepted", "Canonical"}:
            continue
        artifact_id = next(
            (str(metadata[field]) for field in id_fields if isinstance(metadata.get(field), str)), ""
        )
        if artifact_id:
            result[artifact_id] = (
                path.as_posix(), str(metadata.get("Version")), str(metadata.get("Status"))
            )
    return result


def _normalize_inventory(entries: Any) -> dict[str, tuple[str, str, str]] | None:
    if not isinstance(entries, list):
        return None
    result: dict[str, tuple[str, str, str]] = {}
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {"artifact_id", "path", "version", "status"}:
            return None
        artifact_id = entry.get("artifact_id")
        path = entry.get("path")
        if (
            not isinstance(artifact_id, str) or not isinstance(path, str)
            or Path(path).is_absolute() or ".." in Path(path).parts or artifact_id in result
        ):
            return None
        result[artifact_id] = (path, str(entry.get("version")), str(entry.get("status")))
    return result


def _normalize_candidates(entries: Any) -> dict[str, tuple[Any, ...]] | None:
    if not isinstance(entries, list):
        return None
    result: dict[str, tuple[Any, ...]] = {}
    keys = {
        "candidate_id", "artifact_id", "path", "token", "positive_result",
        "can_complete_without_new_result", "disposition",
    }
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != keys:
            return None
        candidate_id = entry.get("candidate_id")
        if not isinstance(candidate_id, str) or candidate_id in result:
            return None
        result[candidate_id] = (
            entry.get("artifact_id"), entry.get("path"), entry.get("token"),
            entry.get("positive_result"), entry.get("can_complete_without_new_result"),
            entry.get("disposition"),
        )
    return result


def _normalize_named(entries: Any, id_key: str, fields: tuple[str, ...]) -> dict[str, tuple[Any, ...]] | None:
    if not isinstance(entries, list):
        return None
    result: dict[str, tuple[Any, ...]] = {}
    expected_keys = {id_key, *fields}
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != expected_keys:
            return None
        entry_id = entry.get(id_key)
        if not isinstance(entry_id, str) or entry_id in result:
            return None
        result[entry_id] = tuple(entry.get(field) for field in fields)
    return result


def _tokens_present(repo_root: Path, records: Iterable[tuple[str, str]]) -> bool:
    for relative, token in records:
        try:
            text = (repo_root / relative).read_text(encoding="utf-8")
        except OSError:
            return False
        if token not in text:
            return False
    return True


def validate_consumer_need_discovery(repo_root: Path) -> ConsumerNeedDiscoveryResult:
    errors: list[str] = []
    try:
        payload = yaml.safe_load(
            (repo_root / "architecture/consumer-need-discovery.yaml").read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        return _result((CONSUMER_NEED_MAP_INVALID,))
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((CONSUMER_NEED_MAP_INVALID,))

    if (
        payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-036"
        or payload.get("baseline") != "f64b3a23419092649cfb4059d4853eabd93fbbc2"
        or payload.get("gate_first") != {
            "ocp016_gate": "G4",
            "applies": False,
            "reason": "discovery-witness-is-not-a-positive-capable-rule-result-or-profile",
            "accepted_consumer_activation_required": False,
        }
        or payload.get("criterion") != {
            "eligible_statuses": ["Accepted", "Canonical"],
            "positive_unmet_need_requires": [
                "current-normative-statement", "exact-positive-result-token",
                "own-obligation-cannot-complete-without-result",
            ],
            "non_qualifying_classes": [
                "negative-boundary-is-sufficient", "deferred-or-future-mention",
                "already-satisfied-positive-output", "governance-act-is-not-consumer-contract",
                "historical-baseline-or-review-snapshot",
            ],
        }
        or payload.get("result") != {
            "disposition": "no_unmet_positive_consumer_need_declared",
            "unmet_positive_needs": [],
        }
    ):
        errors.append(CONSUMER_NEED_MAP_INVALID)

    lifecycle = _normalize_inventory(payload.get("eligible_lifecycle_documents"))
    lifecycle_paths = sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md"))
    lifecycle_paths.extend(sorted((repo_root / "patterns").glob("*.md")))
    live_lifecycle = _live_inventory(lifecycle_paths, ("Document-ID", "Pattern-ID"))
    live_lifecycle = {
        key: (Path(value[0]).relative_to(repo_root).as_posix(), value[1], value[2])
        for key, value in live_lifecycle.items()
    }
    if (
        lifecycle is None or lifecycle != live_lifecycle
        or set(lifecycle or {}) != ELIGIBLE_LIFECYCLE_IDS
    ):
        errors.append(CONSUMER_NEED_SCOPE_DRIFT)

    governance = _normalize_inventory(payload.get("eligible_governance_acts"))
    governance_paths = sorted((repo_root / "architecture/discovery").glob("AD-*.md"))
    live_governance = _live_inventory(governance_paths, ("Decision-ID",))
    live_governance = {
        key: (Path(value[0]).relative_to(repo_root).as_posix(), value[1], value[2])
        for key, value in live_governance.items()
    }
    if (
        governance is None or governance != live_governance
        or set(governance or {}) != ELIGIBLE_GOVERNANCE_IDS
    ):
        errors.append(CONSUMER_NEED_SCOPE_DRIFT)

    candidates = _normalize_candidates(payload.get("candidate_mentions"))
    if candidates != EXPECTED_CANDIDATES or set(candidates or {}) != CANDIDATE_IDS:
        errors.append(CONSUMER_NEED_CANDIDATE_DRIFT)
    elif not _tokens_present(repo_root, ((value[1], value[2]) for value in candidates.values())):
        errors.append(CONSUMER_NEED_CANDIDATE_DRIFT)

    positives = _normalize_named(
        payload.get("established_positive_outputs"), "artifact_id", ("path", "token", "result")
    )
    if positives != EXPECTED_POSITIVE_OUTPUTS or set(positives or {}) != ESTABLISHED_POSITIVE_IDS:
        errors.append(CONSUMER_NEED_POSITIVE_OUTPUT_DRIFT)
    elif not _tokens_present(repo_root, ((value[0], value[1]) for value in positives.values())):
        errors.append(CONSUMER_NEED_POSITIVE_OUTPUT_DRIFT)

    gate_history = _normalize_named(
        payload.get("negative_gate_history"), "artifact_id", ("path", "token", "subject")
    )
    if (
        gate_history != EXPECTED_GATE_HISTORY
        or {value[2] for value in (gate_history or {}).values()} != NEGATIVE_GATE_SUBJECTS
    ):
        errors.append(CONSUMER_NEED_GATE_HISTORY_DRIFT)
    elif not _tokens_present(repo_root, ((value[0], value[1]) for value in gate_history.values())):
        errors.append(CONSUMER_NEED_GATE_HISTORY_DRIFT)

    anchors = _normalize_named(
        payload.get("baseline_evidence_objects"), "path", ("blob", "sha256")
    )
    if anchors != EXPECTED_BASELINE_OBJECTS:
        errors.append(CONSUMER_NEED_EVIDENCE_DRIFT)

    if set(payload.get("forbidden_outcomes", ())) != FORBIDDEN_OUTCOMES:
        errors.append(CONSUMER_NEED_MAP_INVALID)

    try:
        promotion_gate = yaml.safe_load(
            (repo_root / "architecture/foundation-promotion-gate.yaml").read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        promotion_gate = None
    expected_guard = {"schema_version": 5, "completed_cycle_ids": ["EVENT_T6"], "active_cycle_id": None}
    if payload.get("promotion_gate_guard") != expected_guard or not isinstance(promotion_gate, dict):
        errors.append(CONSUMER_NEED_PROMOTION_GATE_DRIFT)
    else:
        cycle_ids = [item.get("cycle_id") for item in promotion_gate.get("cycles", []) if isinstance(item, dict)]
        if (
            promotion_gate.get("schema_version") != 5
            or promotion_gate.get("cycle_protocol", {}).get("active_cycle_id") is not None
            or cycle_ids != ["EVENT_T6"]
        ):
            errors.append(CONSUMER_NEED_PROMOTION_GATE_DRIFT)

    return _result(errors)
