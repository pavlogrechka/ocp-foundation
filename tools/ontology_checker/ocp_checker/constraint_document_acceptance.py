from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
from typing import Any, Iterable

import yaml

from .historical_evidence import historical_path


CONSTRAINT_ACCEPTANCE_MAP_INVALID = "CONSTRAINT_ACCEPTANCE_MAP_INVALID"
CONSTRAINT_ACCEPTANCE_CRITERION_DRIFT = "CONSTRAINT_ACCEPTANCE_CRITERION_DRIFT"
CONSTRAINT_ACCEPTANCE_ROUTE_DRIFT = "CONSTRAINT_ACCEPTANCE_ROUTE_DRIFT"
CONSTRAINT_ACCEPTANCE_SUBJECT_DRIFT = "CONSTRAINT_ACCEPTANCE_SUBJECT_DRIFT"
CONSTRAINT_ACCEPTANCE_SNAPSHOT_DRIFT = "CONSTRAINT_ACCEPTANCE_SNAPSHOT_DRIFT"
CONSTRAINT_ACCEPTANCE_COMPATIBILITY_DRIFT = "CONSTRAINT_ACCEPTANCE_COMPATIBILITY_DRIFT"
CONSTRAINT_ACCEPTANCE_CONSUMER_DRIFT = "CONSTRAINT_ACCEPTANCE_CONSUMER_DRIFT"
CONSTRAINT_ACCEPTANCE_ATOMICITY_DRIFT = "CONSTRAINT_ACCEPTANCE_ATOMICITY_DRIFT"
CONSTRAINT_ACCEPTANCE_NON_IMPLICATION_DRIFT = "CONSTRAINT_ACCEPTANCE_NON_IMPLICATION_DRIFT"
CONSTRAINT_ACCEPTANCE_PROTECTED_DRIFT = "CONSTRAINT_ACCEPTANCE_PROTECTED_DRIFT"
CONSTRAINT_ACCEPTANCE_GATE_DRIFT = "CONSTRAINT_ACCEPTANCE_GATE_DRIFT"

MAP_PATH = Path("architecture/constraint-document-acceptance.yaml")
SUBJECT_PATH = Path("docs/006-constraint-concept/README.md")
SNAPSHOT_PATH = Path("docs/006-constraint-concept/reviewed-contract-v0.3.2.md")
SNAPSHOT_MAP_PATH = Path("architecture/accepted-document-snapshot-map.yaml")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")

BASELINE = "8bfeffb2e2e8928a36d0179a831fa3899ca7cd6a"
MAP_SHA256 = "a36a4459d6ba48e128ab1444be290b9544670bd35b07b1ca23af402859b5d0bb"
SNAPSHOT_SHA256 = "0472d8ce4b15a8c64d58151ee7f706b450b930f708f6f0a7a40bdd87914b3b10"
SNAPSHOT_BLOB = "50f149cf5563083bb84d5d2197ec32c2ed15fa9b"
DIRECT_DEPENDENCIES = (
    "OCP-000", "OCP-001", "OCP-002", "OCP-003", "OCP-004", "OCP-005",
)
CONSUMERS = frozenset({
    "OCP-011", "OCP-013", "OCP-014", "OCP-015", "OCP-017",
    "OCP-018", "OCP-019", "OCP-020", "OCP-021",
})
OPEN_QUESTIONS = frozenset({"Q1", "Q2", "Q6", "Q7", "Q8", "Q10", "Q11", "Q12"})
CRITERIA = {
    "BINDING_REVIEW_LANE": ("applicable-to-Accepted", "satisfied-by-exact-head-gates-and-authorized-squash", "analytical-external-gate"),
    "EXACT_ROUTE_AND_AUTHORITY_LEDGER": ("applicable-to-Accepted", "satisfied", "observational"),
    "BOARD_ACCEPTS_CURRENT_SEMANTICS": ("applicable-to-Accepted", "satisfied-by-mandate-and-exact-head-authorization", "analytical-board-act"),
    "ATOMIC_DOCUMENT_PROMOTION_UNIT": ("applicable-to-Accepted", "satisfied", "observational"),
    "CANONICAL_STABILITY_CHECKS_AND_BOARD_ACT": ("not-applicable-Canonical-only", "not-evaluated", "observational"),
    "CANONICAL_DIRECT_DEPENDENCY_FLOOR_L2": ("not-applicable-Canonical-only", "not-evaluated", "observational"),
    "EXACT_HEAD_AUTHORIZATION_AND_ATOMIC_EFFECT": ("applicable-to-Accepted", "satisfied-by-exact-head-gates-and-authorized-squash", "analytical-external-gate"),
}
GRANTED = frozenset({
    "CONSTRAINT_IDENTITY_SUPERSESSION_KERNEL", "STRUCTURAL_LIFECYCLE_EFFECTIVITY_KERNEL",
    "BOUNDED_APPLICABILITY_EVALUATION_ADMISSIBILITY_KERNEL",
    "FAIL_SAFE_NON_SATISFACTION_AND_NON_AUTHORITY_BOUNDARIES",
    "TARGET_SCOPE_NON_INHERITANCE_BOUNDARY",
})
WITHHELD = {
    "Q1": "CONFLICT_OBJECT_OR_AGGREGATION", "Q2": "PREDICATE_EXPRESSION_LANGUAGE",
    "Q6": "DYNAMIC_INPUT_EVALUATION_CURRENTNESS", "Q7": "EVALUATION_PERSISTENCE_MODE",
    "Q8": "OPERATION_AUTHORIZATION_INTERACTION", "Q10": "READINESS_AVAILABILITY_HANDOFF",
    "Q11": "CONSTRAINT_KIND_TAXONOMY", "Q12": "DOMAIN_RELATION_LANGUAGE",
}
NON_IMPLICATIONS = frozenset({
    "NOT_CANONICAL", "NO_QUESTION_CLOSURE", "NO_POSITIVE_ACTIVATION",
    "NO_CONCEPT_STATUS_CHANGE", "NO_CANDIDATE_SELECTION", "NO_PROMOTION_CYCLE_START",
    "NO_NEXT_ACT_AUTHORIZATION", "NO_OCP005_CHANGE", "NO_OCP016_CHANGE",
    "NO_AD052_CHANGE", "NO_OTHER_DOCUMENT_PROMOTION",
})
EXPECTED_KEYS = frozenset({
    "schema_version", "rule_owner", "baseline", "gate_first", "subject", "criteria",
    "route_decision", "authority_ledger", "compatibility_surface", "consumers",
    "consumer_effect", "reviewed_snapshot", "historical_evidence_successions",
    "document_status_projection", "atomic_package", "versioning", "migration",
    "promotion_gate_guard", "protected_artifacts", "non_implications",
    "baseline_evidence_objects",
})


@dataclass(frozen=True)
class ConstraintDocumentAcceptanceResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> ConstraintDocumentAcceptanceResult:
    return ConstraintDocumentAcceptanceResult(tuple(dict.fromkeys(errors)))


def _load(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None


def _hash(path: Path) -> str | None:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def _git_blob(path: Path) -> str | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


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


def _body(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return ""
    end = text.find("\n---\n", 4)
    return text[end + 5:] if end >= 0 else ""


def _refs(value: Any) -> tuple[str, ...]:
    values = value if isinstance(value, list) else str(value or "").split(",")
    return tuple(str(item).strip().split("@", 1)[0] for item in values if str(item).strip())


def _status_projection(root: Path) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for path in sorted((root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(path)
        if metadata and isinstance(metadata.get("Document-ID"), str):
            result[str(metadata["Document-ID"])] = [str(metadata.get("Version")), str(metadata.get("Status"))]
    return result


def _accepted_consumers(root: Path) -> frozenset[str]:
    result: set[str] = set()
    for path in (root / "docs").glob("[0-9][0-9][0-9]-*/README.md"):
        metadata = _frontmatter(path)
        if metadata and metadata.get("Status") == "Accepted" and "OCP-006" in _refs(metadata.get("Depends-On")):
            result.add(str(metadata.get("Document-ID")))
    return frozenset(result)


def _open_questions(text: str) -> frozenset[str]:
    start = text.find("## 22. Open Questions and Resolved Boundaries")
    end = text.find("## 23. Deferred Decisions", start + 1)
    if start < 0 or end < 0:
        return frozenset()
    result = set()
    for line in text[start:end].splitlines():
        match = re.match(r"^(\d+)\.\s+(.*)$", line.strip())
        if match and not match.group(2).startswith("~~"):
            result.add(f"Q{match.group(1)}")
    return frozenset(result)


def validate_constraint_document_acceptance(repo_root: Path) -> ConstraintDocumentAcceptanceResult:
    errors: list[str] = []
    payload = _load(repo_root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_KEYS:
        return _result((CONSTRAINT_ACCEPTANCE_MAP_INVALID,))
    digest = hashlib.sha256(yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode()).hexdigest()
    if (
        digest != MAP_SHA256 or payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-053" or payload.get("baseline") != BASELINE
    ):
        errors.append(CONSTRAINT_ACCEPTANCE_MAP_INVALID)

    gate_first = payload.get("gate_first") or {}
    if gate_first != {
        "route": "Route-F", "positive_capable": False, "ocp016_g4_applies": False,
        "activation_performed": False,
        "reason": "document-lifecycle-authority-changes-without-adding-or-activating-a-rule-result-profile",
        "absent_activation_bindings": ["consumer-baseline", "rule-version", "input-snapshot", "evaluation-context", "legitimate-owner-evaluator"],
    }:
        errors.append(CONSTRAINT_ACCEPTANCE_ROUTE_DRIFT)

    criteria = payload.get("criteria") or []
    observed_criteria = {
        str(row.get("criterion_id")): (
            row.get("applicability"), row.get("result"), row.get("basis_mode")
        ) for row in criteria if isinstance(row, dict)
    }
    if observed_criteria != CRITERIA or len(criteria) != len(CRITERIA):
        errors.append(CONSTRAINT_ACCEPTANCE_CRITERION_DRIFT)
    for row in criteria:
        if not isinstance(row, dict):
            continue
        try:
            source_text = (repo_root / str(row["source"])).read_text(encoding="utf-8")
        except (OSError, KeyError):
            source_text = ""
        if not row.get("tokens") or any(str(token) not in source_text for token in row.get("tokens") or ()):
            errors.append(CONSTRAINT_ACCEPTANCE_CRITERION_DRIFT)

    route = payload.get("route_decision") or {}
    if (
        route.get("selected") != "Route-F"
        or route.get("precedent_guide_is_not_route_proof") is not True
        or set((route.get("rejected_routes") or {}).keys()) != {"Route-C", "Route-E", "Route-D", "Route-I"}
    ):
        errors.append(CONSTRAINT_ACCEPTANCE_ROUTE_DRIFT)
    for evidence in route.get("evidence") or ():
        try:
            text = (repo_root / str(evidence["path"])).read_text(encoding="utf-8")
        except (OSError, KeyError):
            text = ""
        if not evidence.get("tokens") or any(str(token) not in text for token in evidence.get("tokens") or ()):
            errors.append(CONSTRAINT_ACCEPTANCE_ROUTE_DRIFT)

    metadata = _frontmatter(repo_root / SUBJECT_PATH) or {}
    subject = payload.get("subject") or {}
    if (
        metadata.get("Document-ID") != "OCP-006" or str(metadata.get("Version")) != "0.4.0"
        or metadata.get("Status") != "Accepted" or metadata.get("Concept-Status") != "Accepted"
        or _refs(metadata.get("Depends-On")) != DIRECT_DEPENDENCIES
        or subject.get("before") != {"version": "0.3.2", "status": "Draft", "concept_status": "Accepted"}
        or subject.get("after") != {"version": "0.4.0", "status": "Accepted", "concept_status": "Accepted"}
        or subject.get("semantic_delta") != "none"
        or tuple(subject.get("exact_direct_dependencies") or ()) != DIRECT_DEPENDENCIES
    ):
        errors.append(CONSTRAINT_ACCEPTANCE_SUBJECT_DRIFT)

    snapshot = payload.get("reviewed_snapshot") or {}
    snapshot_map = _load(repo_root / SNAPSHOT_MAP_PATH) or {}
    entries = {
        row.get("document_id"): row for row in snapshot_map.get("entries", []) if isinstance(row, dict)
    }
    expected_entry = {
        "document_id": "OCP-006", "primary": SUBJECT_PATH.as_posix(), "current_status": "Accepted",
        "reviewed_version": "0.3.2", "snapshot": SNAPSHOT_PATH.as_posix(),
        "sha256": SNAPSHOT_SHA256, "basis": "current-accepted",
    }
    if (
        snapshot != {"path": SNAPSHOT_PATH.as_posix(), "reviewed_version": "0.3.2", "sha256": SNAPSHOT_SHA256, "baseline_blob": SNAPSHOT_BLOB, "basis": "current-accepted"}
        or _hash(repo_root / SNAPSHOT_PATH) != SNAPSHOT_SHA256
        or _git_blob(repo_root / SNAPSHOT_PATH) != SNAPSHOT_BLOB
        or not _body(repo_root / SUBJECT_PATH).startswith(_body(repo_root / SNAPSHOT_PATH))
        or entries.get("OCP-006") != expected_entry
    ):
        errors.append(CONSTRAINT_ACCEPTANCE_SNAPSHOT_DRIFT)

    surface = payload.get("compatibility_surface") or {}
    current_text = (repo_root / SUBJECT_PATH).read_text(encoding="utf-8")
    q6 = surface.get("q6_boundary") or {}
    if (
        frozenset(surface.get("granted") or ()) != GRANTED
        or surface.get("withheld_open_surfaces") != WITHHELD
        or _open_questions(current_text) != OPEN_QUESTIONS
        or set(surface.get("withheld_open_surfaces") or {}) != OPEN_QUESTIONS
        or any(q6.get(key) is not False for key in (
            "currentness_magnitude_defined", "currentness_evaluator_defined",
            "fail_safe_rule_defines_currentness", "dependent_inference_permitted",
        ))
        or "neither this acceptance nor that fail-safe language defines a freshness magnitude" not in current_text
    ):
        errors.append(CONSTRAINT_ACCEPTANCE_COMPATIBILITY_DRIFT)

    consumers = payload.get("consumers") or []
    claimed_consumers = {row.get("document_id") for row in consumers if isinstance(row, dict)}
    if (
        claimed_consumers != CONSUMERS or len(consumers) != len(CONSUMERS)
        or _accepted_consumers(repo_root) != CONSUMERS
        or payload.get("consumer_effect") != {
            "accepted_direct_consumer_count": 9, "data_migration": "none",
            "ocp005_accepted_consumer_added": "OCP-006",
            "ocp006_declares_new_unmet_positive_need": False,
            "consumer_need_projection_change": "eligible-inventory-only-no-new-need",
            "reference_migration": "none", "schema_migration": "none",
            "runtime_behavior": "unchanged", "newly_legitimized_positive_behavior": "none",
        }
    ):
        errors.append(CONSTRAINT_ACCEPTANCE_CONSUMER_DRIFT)
    for row in consumers:
        try:
            consumer_text = (repo_root / str(row["path"])).read_text(encoding="utf-8")
            consumer_meta = _frontmatter(repo_root / str(row["path"])) or {}
        except (OSError, KeyError):
            consumer_text, consumer_meta = "", {}
        if (
            row.get("token") not in consumer_text or consumer_meta.get("Status") != "Accepted"
            or "OCP-006" not in _refs(consumer_meta.get("Depends-On"))
            or row.get("acceptance_change") != "lifecycle-assurance-only"
            or not row.get("consumed_surface")
        ):
            errors.append(CONSTRAINT_ACCEPTANCE_CONSUMER_DRIFT)

    atomic = payload.get("atomic_package") or {}
    expected_elements = {
        "version", "status", "compatibility-surface", "exact-direct-dependencies",
        "criteria-evidence", "reviewed-snapshot", "promotion-gate-projection", "repository-accounting",
    }
    if (
        set(atomic.get("required_elements") or ()) != expected_elements
        or atomic.get("complete") is not True or atomic.get("partial_effect_permitted") is not False
        or payload.get("document_status_projection") != _status_projection(repo_root)
        or payload.get("versioning", {}).get("OCP-006") != "0.3.2-to-0.4.0-precanonical-minor-lifecycle-acceptance-no-semantic-delta"
        or payload.get("migration", {}).get("data") != "none"
        or payload.get("migration", {}).get("references") != "none"
        or payload.get("migration", {}).get("schemas") != "none"
        or payload.get("migration", {}).get("runtime_behavior") != "unchanged"
    ):
        errors.append(CONSTRAINT_ACCEPTANCE_ATOMICITY_DRIFT)

    successions = payload.get("historical_evidence_successions") or []
    if len(successions) != 3:
        errors.append(CONSTRAINT_ACCEPTANCE_PROTECTED_DRIFT)
    for row in successions:
        preserved = Path(str(row.get("preserved_path", "")))
        if preserved.is_absolute() or ".." in preserved.parts or _hash(repo_root / preserved) != row.get("sha256"):
            errors.append(CONSTRAINT_ACCEPTANCE_PROTECTED_DRIFT)

    for item in payload.get("protected_artifacts") or ():
        if _hash(repo_root / Path(str(item.get("path", "")))) != item.get("sha256"):
            errors.append(CONSTRAINT_ACCEPTANCE_PROTECTED_DRIFT)

    baseline_objects = payload.get("baseline_evidence_objects") or []
    if len(baseline_objects) != 14:
        errors.append(CONSTRAINT_ACCEPTANCE_PROTECTED_DRIFT)
    for item in baseline_objects:
        original = Path(str(item.get("path", "")))
        resolved = historical_path(repo_root, original, str(item.get("sha256", "")))
        try:
            data = (repo_root / resolved).read_bytes()
            text = data.decode("utf-8")
        except (OSError, UnicodeDecodeError):
            errors.append(CONSTRAINT_ACCEPTANCE_PROTECTED_DRIFT)
            continue
        if (
            _git_blob(repo_root / resolved) != item.get("blob")
            or hashlib.sha256(data).hexdigest() != item.get("sha256")
            or any(str(token) not in text for token in item.get("state_tokens") or ())
        ):
            errors.append(CONSTRAINT_ACCEPTANCE_PROTECTED_DRIFT)

    gate_payload = _load(repo_root / GATE_PATH)
    guard = payload.get("promotion_gate_guard") or {}
    candidates = {
        row.get("document_id"): row for row in (gate_payload or {}).get("candidates", []) if isinstance(row, dict)
    }
    completed = [
        row.get("cycle_id") for row in (gate_payload or {}).get("cycles", []) if isinstance(row, dict)
        and set((row.get("steps") or {}).values()) == {"completed"}
    ]
    if (
        guard != {"schema_version": 5, "completed_cycle_ids": ["EVENT_T6"], "active_cycle_id": None, "ocp006_status_projection": "Accepted", "candidate_selected": False, "cycle_opened": False}
        or not isinstance(gate_payload, dict) or gate_payload.get("schema_version") != 5
        or gate_payload.get("cycle_protocol", {}).get("active_cycle_id") is not None
        or completed != ["EVENT_T6"]
        or candidates.get("OCP-006", {}).get("expected_document_status") != "Accepted"
        or len((gate_payload or {}).get("cycles", [])) != 1
    ):
        errors.append(CONSTRAINT_ACCEPTANCE_GATE_DRIFT)

    non_implications = frozenset(payload.get("non_implications") or ())
    other_statuses = payload.get("document_status_projection") or {}
    if (
        non_implications != NON_IMPLICATIONS or len(payload.get("non_implications") or ()) != len(NON_IMPLICATIONS)
        or metadata.get("Status") == "Canonical" or metadata.get("Concept-Status") != "Accepted"
        or _open_questions(current_text) != OPEN_QUESTIONS
        or gate_first.get("activation_performed") is not False
        or guard.get("candidate_selected") is not False or guard.get("cycle_opened") is not False
        or any(value != _status_projection(repo_root).get(doc_id) for doc_id, value in other_statuses.items() if doc_id != "OCP-006")
    ):
        errors.append(CONSTRAINT_ACCEPTANCE_NON_IMPLICATION_DRIFT)
    return _result(errors)
