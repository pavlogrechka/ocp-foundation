from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
import subprocess
from typing import Any, Iterable

import yaml


ASSIGNMENT_ACCEPTANCE_MAP_INVALID = "ASSIGNMENT_ACCEPTANCE_MAP_INVALID"
ASSIGNMENT_ACCEPTANCE_CRITERION_DRIFT = "ASSIGNMENT_ACCEPTANCE_CRITERION_DRIFT"
ASSIGNMENT_ACCEPTANCE_ROUTE_DRIFT = "ASSIGNMENT_ACCEPTANCE_ROUTE_DRIFT"
ASSIGNMENT_ACCEPTANCE_SUBJECT_DRIFT = "ASSIGNMENT_ACCEPTANCE_SUBJECT_DRIFT"
ASSIGNMENT_ACCEPTANCE_SNAPSHOT_DRIFT = "ASSIGNMENT_ACCEPTANCE_SNAPSHOT_DRIFT"
ASSIGNMENT_ACCEPTANCE_CONSUMER_DRIFT = "ASSIGNMENT_ACCEPTANCE_CONSUMER_DRIFT"
ASSIGNMENT_ACCEPTANCE_NEED_DRIFT = "ASSIGNMENT_ACCEPTANCE_NEED_DRIFT"
ASSIGNMENT_ACCEPTANCE_ATOMICITY_DRIFT = "ASSIGNMENT_ACCEPTANCE_ATOMICITY_DRIFT"
ASSIGNMENT_ACCEPTANCE_NON_IMPLICATION_DRIFT = "ASSIGNMENT_ACCEPTANCE_NON_IMPLICATION_DRIFT"
ASSIGNMENT_ACCEPTANCE_PROTECTED_DRIFT = "ASSIGNMENT_ACCEPTANCE_PROTECTED_DRIFT"
ASSIGNMENT_ACCEPTANCE_GATE_DRIFT = "ASSIGNMENT_ACCEPTANCE_GATE_DRIFT"
ASSIGNMENT_ACCEPTANCE_ANCHOR_DRIFT = "ASSIGNMENT_ACCEPTANCE_ANCHOR_DRIFT"

MAP_PATH = Path("architecture/assignment-document-acceptance.yaml")
SUBJECT_PATH = Path("docs/005-assignment-concept/README.md")
SNAPSHOT_PATH = Path("docs/005-assignment-concept/reviewed-contract-v0.3.0.md")
SNAPSHOT_MAP_PATH = Path("architecture/accepted-document-snapshot-map.yaml")
NEED_PATH = Path("architecture/consumer-need-discovery.yaml")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
BASELINE = "1325de6a4fff84b8350fe1bfecf51e4fd0f4c176"
MAP_SHA256 = "1fe41710d74251edde06c2465871c9c0162866e6a56a25d6217c7fa69607e596"
SNAPSHOT_SHA256 = "de84c9dafdb6126ff68a3a33218a344ddc250cf1a28e63c91407fd416e7e161b"
SNAPSHOT_BLOB = "1dd975a17ec65df751357fdd049c8ca928739bd1"
DIRECT_DEPENDENCIES = ("OCP-000", "OCP-001", "OCP-002", "OCP-003", "OCP-004")
CONSUMERS = frozenset({"OCP-006", "OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021", "OCP-023"})
OPEN_QUESTIONS = frozenset({"Q2", "Q4", "Q5", "Q7", "Q8", "Q9", "Q10", "Q11"})
WITHHELD = {
    "Q2": "AMENDMENT_AFTER_ESTABLISHMENT", "Q4": "ROLE_TAXONOMY",
    "Q5": "COMPOSITE_RESOURCE_SCOPE", "Q7": "ROLE_SPECIALIZATIONS",
    "Q8": "CONSTRAINT_CONFLICT_HANDOFF", "Q9": "MULTIPLE_APPLICABILITY_INTERVALS",
    "Q10": "PROVENANCE_TAXONOMY", "Q11": "REPLACEMENT_POLICY",
}
GRANTED = frozenset({
    "ASSIGNMENT_IDENTITY_REFERENCE_KERNEL", "TRANSITION_HISTORY_LIFECYCLE_KERNEL",
    "STRUCTURAL_ROLE_PROVENANCE_KERNEL", "SINGLE_INTERVAL_EFFECTIVITY_AND_PARTICIPATION_KERNEL",
    "NON_INHERITANCE_NON_AUTHORITY_BOUNDARY", "SUPERSESSION_IDENTITY_BOUNDARY",
    "EXECUTABLE_ASSIGNMENT_BOUNDARY",
})
NON_IMPLICATIONS = frozenset({
    "NOT_CANONICAL", "NO_OTHER_DOCUMENT_PROMOTION_OR_CANONICALIZATION",
    "NO_QUESTION_CLOSURE", "NO_POSITIVE_ACTIVATION", "NO_CONCEPT_STATUS_CHANGE",
    "NO_UNMET_NEED_SATISFACTION", "NO_CANDIDATE_SELECTION", "NO_PROMOTION_CYCLE_START",
    "NO_NEXT_ACT_AUTHORIZATION", "NO_OCP006_LIFECYCLE_EFFECT", "NO_OCP016_CHANGE",
    "NO_AD052_CRITERIA_CHANGE",
})
CRITERIA = {
    "BINDING_REVIEW_LANE": ("applicable-to-Accepted", "satisfied-by-exact-head-gates-and-authorized-squash", "analytical-external-gate"),
    "EXACT_ROUTE_AND_AUTHORITY_LEDGER": ("applicable-to-Accepted", "satisfied", "observational"),
    "BOARD_ACCEPTS_CURRENT_SEMANTICS": ("applicable-to-Accepted", "satisfied-by-mandate-and-exact-head-authorization", "analytical-board-act"),
    "ATOMIC_DOCUMENT_PROMOTION_UNIT": ("applicable-to-Accepted", "satisfied", "observational"),
    "CANONICAL_STABILITY_CHECKS_AND_BOARD_ACT": ("not-applicable-Canonical-only", "not-evaluated", "observational"),
    "CANONICAL_DIRECT_DEPENDENCY_FLOOR_L2": ("not-applicable-Canonical-only", "not-evaluated", "observational"),
    "EXACT_HEAD_AUTHORIZATION_AND_ATOMIC_EFFECT": ("applicable-to-Accepted", "satisfied-by-exact-head-gates-and-authorized-squash", "analytical-external-gate"),
}
EXPECTED_KEYS = frozenset({
    "schema_version", "rule_owner", "baseline", "gate_first", "subject", "criteria",
    "route_decision", "authority_ledger", "compatibility_surface", "consumers",
    "consumer_effect", "unmet_positive_need", "differences_from_previously_accepted_subject",
    "reviewed_snapshot", "historical_evidence_successions", "current_projection_sync",
    "document_status_projection", "atomic_package", "versioning", "migration",
    "promotion_gate_guard", "baseline_evidence_objects", "protected_artifacts",
    "non_implications",
})


@dataclass(frozen=True)
class AssignmentDocumentAcceptanceResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentDocumentAcceptanceResult:
    return AssignmentDocumentAcceptanceResult(tuple(dict.fromkeys(errors)))


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
        if metadata and metadata.get("Status") == "Accepted" and "OCP-005" in _refs(metadata.get("Depends-On")):
            result.add(str(metadata.get("Document-ID")))
    return frozenset(result)


def _open_questions(text: str) -> frozenset[str]:
    start = text.find("## 19. Open Questions and Resolved Boundaries")
    end = text.find("## 20. Deferred Decisions", start + 1)
    if start < 0 or end < 0:
        return frozenset()
    questions = set()
    for line in text[start:end].splitlines():
        match = re.match(r"^(\d+)\.\s+(.*)$", line.strip())
        if match and not match.group(2).startswith("~~"):
            questions.add(f"Q{match.group(1)}")
    return frozenset(questions)


def _baseline_blob(root: Path, baseline: str, path: str) -> tuple[str, bytes] | None:
    try:
        line = subprocess.check_output(
            ["git", "ls-tree", "-r", baseline, "--", path], cwd=root, text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        if not line:
            return None
        metadata, resolved = line.split("\t", 1)
        if resolved != path:
            return None
        blob = metadata.split()[2]
        raw = subprocess.check_output(
            ["git", "cat-file", "blob", blob], cwd=root, stderr=subprocess.DEVNULL
        )
        return blob, raw
    except (OSError, subprocess.CalledProcessError, ValueError, IndexError):
        return None


def validate_assignment_document_acceptance(repo_root: Path) -> AssignmentDocumentAcceptanceResult:
    errors: list[str] = []
    payload = _load(repo_root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_KEYS:
        return _result((ASSIGNMENT_ACCEPTANCE_MAP_INVALID,))
    digest = hashlib.sha256(yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode()).hexdigest()
    if digest != MAP_SHA256 or payload.get("schema_version") != 1 or payload.get("rule_owner") != "AD-054" or payload.get("baseline") != BASELINE:
        errors.append(ASSIGNMENT_ACCEPTANCE_MAP_INVALID)

    if payload.get("gate_first") != {
        "route": "Route-F", "positive_capable": False, "ocp016_g4_applies": False,
        "activation_performed": False,
        "reason": "document-lifecycle-authority-changes-without-adding-or-activating-a-rule-result-profile",
        "unmet_consumer_need_effect": "remains-unmet-and-unactivated",
    }:
        errors.append(ASSIGNMENT_ACCEPTANCE_ROUTE_DRIFT)

    observed_criteria = {
        str(row.get("criterion_id")): (row.get("applicability"), row.get("result"), row.get("basis_mode"))
        for row in payload.get("criteria") or () if isinstance(row, dict)
    }
    if observed_criteria != CRITERIA or len(payload.get("criteria") or ()) != len(CRITERIA):
        errors.append(ASSIGNMENT_ACCEPTANCE_CRITERION_DRIFT)
    for row in payload.get("criteria") or ():
        if not isinstance(row, dict):
            continue
        try:
            text = (repo_root / str(row["source"])).read_text(encoding="utf-8")
        except (OSError, KeyError):
            text = ""
        if not row.get("tokens") or any(str(token) not in text for token in row.get("tokens") or ()):
            errors.append(ASSIGNMENT_ACCEPTANCE_CRITERION_DRIFT)

    route = payload.get("route_decision") or {}
    if route.get("selected") != "Route-F" or route.get("precedent_guide_is_not_route_proof") is not True or set((route.get("rejected_routes") or {}).keys()) != {"Route-C", "Route-E", "Route-D", "Route-I"}:
        errors.append(ASSIGNMENT_ACCEPTANCE_ROUTE_DRIFT)
    for evidence in route.get("evidence") or ():
        try:
            text = (repo_root / str(evidence["path"])).read_text(encoding="utf-8")
        except (OSError, KeyError):
            text = ""
        if not evidence.get("tokens") or any(str(token) not in text for token in evidence.get("tokens") or ()):
            errors.append(ASSIGNMENT_ACCEPTANCE_ROUTE_DRIFT)

    metadata = _frontmatter(repo_root / SUBJECT_PATH) or {}
    subject = payload.get("subject") or {}
    if (
        metadata.get("Document-ID") != "OCP-005" or str(metadata.get("Version")) != "0.4.0"
        or metadata.get("Status") != "Accepted" or metadata.get("Concept-Status") != "Accepted"
        or _refs(metadata.get("Depends-On")) != DIRECT_DEPENDENCIES
        or subject.get("before") != {"version": "0.3.0", "status": "Draft", "concept_status": "Accepted"}
        or subject.get("after") != {"version": "0.4.0", "status": "Accepted", "concept_status": "Accepted"}
        or subject.get("semantic_delta") != "none"
        or tuple(subject.get("exact_direct_dependencies") or ()) != DIRECT_DEPENDENCIES
    ):
        errors.append(ASSIGNMENT_ACCEPTANCE_SUBJECT_DRIFT)

    snapshot = payload.get("reviewed_snapshot") or {}
    snapshot_map = _load(repo_root / SNAPSHOT_MAP_PATH) or {}
    entries = {row.get("document_id"): row for row in snapshot_map.get("entries", []) if isinstance(row, dict)}
    expected_entry = {
        "document_id": "OCP-005", "primary": SUBJECT_PATH.as_posix(), "current_status": "Accepted",
        "reviewed_version": "0.3.0", "snapshot": SNAPSHOT_PATH.as_posix(),
        "sha256": SNAPSHOT_SHA256, "basis": "current-accepted",
    }
    if (
        snapshot != {"path": SNAPSHOT_PATH.as_posix(), "reviewed_version": "0.3.0", "sha256": SNAPSHOT_SHA256, "baseline_blob": SNAPSHOT_BLOB, "basis": "current-accepted"}
        or _hash(repo_root / SNAPSHOT_PATH) != SNAPSHOT_SHA256
        or _git_blob(repo_root / SNAPSHOT_PATH) != SNAPSHOT_BLOB
        or not _body(repo_root / SUBJECT_PATH).startswith(_body(repo_root / SNAPSHOT_PATH))
        or entries.get("OCP-005") != expected_entry
    ):
        errors.append(ASSIGNMENT_ACCEPTANCE_SNAPSHOT_DRIFT)

    consumer_rows = payload.get("consumers") or []
    if {row.get("document_id") for row in consumer_rows if isinstance(row, dict)} != CONSUMERS or len(consumer_rows) != 7 or _accepted_consumers(repo_root) != CONSUMERS:
        errors.append(ASSIGNMENT_ACCEPTANCE_CONSUMER_DRIFT)
    for row in consumer_rows:
        try:
            text = (repo_root / str(row["path"])).read_text(encoding="utf-8")
        except (OSError, KeyError):
            text = ""
        if row.get("acceptance_change") != "lifecycle-assurance-only" or str(row.get("token", "")) not in text:
            errors.append(ASSIGNMENT_ACCEPTANCE_CONSUMER_DRIFT)

    need_map = _load(repo_root / NEED_PATH) or {}
    current_need_ids = set((need_map.get("current_result") or {}).get("unmet_positive_needs") or ())
    need = payload.get("unmet_positive_need") or {}
    if (
        current_need_ids != {"RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS"}
        or need.get("before") != "unmet" or need.get("after") != "unmet"
        or any(need.get(key) is not False for key in ("acceptance_supplies_completeness", "acceptance_names_legitimate_evaluator", "acceptance_activates_positive_model"))
    ):
        errors.append(ASSIGNMENT_ACCEPTANCE_NEED_DRIFT)

    differences = (payload.get("differences_from_previously_accepted_subject") or {}).get("differences") or []
    if (
        {row.get("axis") for row in differences if isinstance(row, dict)}
        != {"direct-dependencies", "accepted-consumers", "whole-freeze-surfaces", "unmet-positive-consumer-need", "direct-dependent-previous-subject"}
        or len(differences) != 5
        or any(row.get("evidence_mode") != "analytic" or not row.get("criterion_effect") for row in differences if isinstance(row, dict))
    ):
        errors.append(ASSIGNMENT_ACCEPTANCE_CRITERION_DRIFT)

    body = (repo_root / SUBJECT_PATH).read_text(encoding="utf-8") if (repo_root / SUBJECT_PATH).exists() else ""
    surface = payload.get("compatibility_surface") or {}
    if frozenset(surface.get("granted") or ()) != GRANTED or surface.get("withheld_open_surfaces") != WITHHELD or _open_questions(body) != OPEN_QUESTIONS or surface.get("dependent_inference_permitted") is not False:
        errors.append(ASSIGNMENT_ACCEPTANCE_ATOMICITY_DRIFT)

    if payload.get("document_status_projection") != _status_projection(repo_root):
        errors.append(ASSIGNMENT_ACCEPTANCE_ATOMICITY_DRIFT)
    projection = payload.get("current_projection_sync") or {}
    statuses = [value[1] for value in _status_projection(repo_root).values()]
    expected_counts = {name: statuses.count(name) for name in ("Canonical", "Accepted", "Draft")}
    if (projection.get("expected") or {}).get("primary_document_status_counts") != expected_counts:
        errors.append(ASSIGNMENT_ACCEPTANCE_ATOMICITY_DRIFT)

    gate = _load(repo_root / GATE_PATH) or {}
    guard = payload.get("promotion_gate_guard") or {}
    cycles = gate.get("cycles") or []
    completed = [row.get("cycle_id") for row in cycles if isinstance(row, dict) and all(value == "completed" for value in (row.get("steps") or {}).values())]
    candidates = {row.get("document_id"): row for row in gate.get("candidates") or [] if isinstance(row, dict)}
    if (
        gate.get("schema_version") != 5 or (gate.get("cycle_protocol") or {}).get("active_cycle_id") is not None
        or completed != ["EVENT_T6"] or guard.get("candidate_selected") is not False or guard.get("cycle_opened") is not False
        or (candidates.get("OCP-005") or {}).get("expected_document_status") != "Accepted"
        or (candidates.get("OCP-006") or {}).get("expected_document_status") != "Accepted"
        or (candidates.get("OCP-006") or {}).get("l2_blockers") != ["OCP-005"]
    ):
        errors.append(ASSIGNMENT_ACCEPTANCE_GATE_DRIFT)

    if frozenset(payload.get("non_implications") or ()) != NON_IMPLICATIONS:
        errors.append(ASSIGNMENT_ACCEPTANCE_NON_IMPLICATION_DRIFT)
    for item in payload.get("protected_artifacts") or ():
        if _hash(repo_root / str(item.get("path", ""))) != item.get("sha256"):
            errors.append(ASSIGNMENT_ACCEPTANCE_PROTECTED_DRIFT)

    for item in payload.get("baseline_evidence_objects") or ():
        path = str(item.get("path", ""))
        resolved = _baseline_blob(repo_root, BASELINE, path)
        if resolved is None:
            errors.append(ASSIGNMENT_ACCEPTANCE_ANCHOR_DRIFT)
            continue
        blob, raw = resolved
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = ""
        if blob != item.get("blob") or hashlib.sha256(raw).hexdigest() != item.get("sha256") or any(str(token) not in text for token in item.get("state_tokens") or ()):
            errors.append(ASSIGNMENT_ACCEPTANCE_ANCHOR_DRIFT)
    for row in payload.get("historical_evidence_successions") or ():
        if _hash(repo_root / str(row.get("preserved_path", ""))) != row.get("sha256"):
            errors.append(ASSIGNMENT_ACCEPTANCE_ANCHOR_DRIFT)

    atomic = payload.get("atomic_package") or {}
    migration = payload.get("migration") or {}
    if atomic.get("complete") is not True or atomic.get("partial_effect_permitted") is not False or migration.get("runtime_behavior") != "unchanged" or not migration.get("rollback_unit"):
        errors.append(ASSIGNMENT_ACCEPTANCE_ATOMICITY_DRIFT)

    return _result(errors)
