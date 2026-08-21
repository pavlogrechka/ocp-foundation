from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
import subprocess
from typing import Any, Iterable

import yaml

from .foundation_promotion_gate import (
    assignment_document_promotion_prefix_is_current,
    validate_foundation_promotion_gate,
)


ASSIGNMENT_CANONICALIZATION_MAP_INVALID = "ASSIGNMENT_CANONICALIZATION_MAP_INVALID"
ASSIGNMENT_CANONICALIZATION_CRITERION_DRIFT = "ASSIGNMENT_CANONICALIZATION_CRITERION_DRIFT"
ASSIGNMENT_CANONICALIZATION_SUBJECT_DRIFT = "ASSIGNMENT_CANONICALIZATION_SUBJECT_DRIFT"
ASSIGNMENT_CANONICALIZATION_GATE_DRIFT = "ASSIGNMENT_CANONICALIZATION_GATE_DRIFT"
ASSIGNMENT_CANONICALIZATION_BOUNDARY_DRIFT = "ASSIGNMENT_CANONICALIZATION_BOUNDARY_DRIFT"
ASSIGNMENT_CANONICALIZATION_DEPENDENCY_DRIFT = "ASSIGNMENT_CANONICALIZATION_DEPENDENCY_DRIFT"
ASSIGNMENT_CANONICALIZATION_SNAPSHOT_DRIFT = "ASSIGNMENT_CANONICALIZATION_SNAPSHOT_DRIFT"
ASSIGNMENT_CANONICALIZATION_HISTORY_DRIFT = "ASSIGNMENT_CANONICALIZATION_HISTORY_DRIFT"
ASSIGNMENT_CANONICALIZATION_ANCHOR_DRIFT = "ASSIGNMENT_CANONICALIZATION_ANCHOR_DRIFT"

MAP_PATH = Path("architecture/assignment-document-canonicalization.yaml")
SUBJECT_PATH = Path("docs/005-assignment-concept/README.md")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
CRITERIA_PATH = Path("architecture/constraint-document-status-readiness.yaml")
SNAPSHOT_MAP_PATH = Path("architecture/accepted-document-snapshot-map.yaml")
NEED_PATH = Path("architecture/consumer-need-discovery.yaml")
BASELINE = "428e8170c051928b10383df4a4287df018f4be96"
MAP_SHA256 = "e2bcf03a548bfbc9f0be67d2b779bd8327c8d099563c7089ad7f599e24f15bcc"

CRITERION_IDS = (
    "BINDING_REVIEW_LANE", "EXACT_ROUTE_AND_AUTHORITY_LEDGER",
    "BOARD_ACCEPTS_CURRENT_SEMANTICS", "ATOMIC_DOCUMENT_PROMOTION_UNIT",
    "CANONICAL_STABILITY_CHECKS_AND_BOARD_ACT",
    "CANONICAL_DIRECT_DEPENDENCY_FLOOR_L2",
    "EXACT_HEAD_AUTHORIZATION_AND_ATOMIC_EFFECT",
)
DIRECT_DEPENDENCIES = {
    "OCP-000": ("1.6.0", "Canonical"),
    "OCP-001": ("1.0.0", "Canonical"),
    "OCP-002": ("1.6.0", "Canonical"),
    "OCP-003": ("1.0.0", "Canonical"),
    "OCP-004": ("1.0.1", "Canonical"),
}
OPEN_QUESTIONS = frozenset({"Q2", "Q4", "Q5", "Q7", "Q8", "Q9", "Q10", "Q11"})
CONSUMERS = frozenset({"OCP-006", "OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021", "OCP-023"})
NON_IMPLICATIONS = frozenset({
    "NO_CONCEPT_CANONICALIZATION", "NO_CYCLE_COMPLETION",
    "NO_THIRD_STEP_EXECUTION", "NO_THIRD_STEP_AUTHORIZATION",
    "NO_OTHER_DOCUMENT_PROMOTION_CANONICALIZATION_OR_SELECTION",
    "NO_QUESTION_CLOSURE", "NO_POSITIVE_MODEL_ACTIVATION",
    "NO_UNMET_NEED_SATISFACTION", "NO_NEXT_ACT_AUTHORIZATION",
})
MACHINE_VALIDATORS = (
    "assignment-stable-surface", "assignment-amendment-q2",
    "assignment-temporal-scope", "assignment-consumer-compatibility",
    "assignment-consumer-pressure", "assignment-norm-compatibility",
    "assignment-q3-lifecycle", "assignment-q2-sufficiency",
    "assignment-q9-sufficiency", "assignment-document-acceptance",
    "assignment-canonical-readiness", "foundation-promotion-gate",
)
EXPECTED_KEYS = frozenset({
    "schema_version", "rule_owner", "baseline", "gate_first", "authority",
    "subject", "criteria_source", "criteria", "route", "direct_dependencies",
    "machine_checks", "compatibility_surface", "consumer_effect",
    "dependent_consequence", "reviewed_body", "gate_transition",
    "current_projection", "historical_evidence_successions", "atomicity",
    "rollback", "non_implications", "versioning", "migration",
    "baseline_evidence_objects",
})


@dataclass(frozen=True)
class AssignmentDocumentCanonicalizationResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentDocumentCanonicalizationResult:
    return AssignmentDocumentCanonicalizationResult(tuple(dict.fromkeys(errors)))


def _load(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None


def _frontmatter_text(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    try:
        value = yaml.safe_load(text[4:end]) if end >= 0 else None
    except yaml.YAMLError:
        value = None
    return value if isinstance(value, dict) else {}


def _frontmatter(path: Path) -> dict[str, Any]:
    try:
        return _frontmatter_text(path.read_text(encoding="utf-8"))
    except OSError:
        return {}


def _refs(value: Any) -> tuple[str, ...]:
    values = value if isinstance(value, list) else str(value or "").split(",")
    return tuple(str(item).strip().split("@", 1)[0] for item in values if str(item).strip())


def _documents(root: Path) -> dict[str, tuple[Path, dict[str, Any], str]]:
    result: dict[str, tuple[Path, dict[str, Any], str]] = {}
    for path in sorted((root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        text = path.read_text(encoding="utf-8")
        metadata = _frontmatter_text(text)
        if isinstance(metadata.get("Document-ID"), str):
            result[str(metadata["Document-ID"])] = (path, metadata, text)
    return result


def _open_questions(text: str) -> frozenset[str]:
    start = text.find("## 19. Open Questions and Resolved Boundaries")
    end = text.find("## 20. Deferred Decisions", start + 1)
    if start < 0 or end < 0:
        return frozenset()
    return frozenset(
        f"Q{match.group(1)}" for line in text[start:end].splitlines()
        if (match := re.match(r"^(\d+)\.\s+(.*)$", line.strip()))
        and not match.group(2).startswith("~~")
    )


def _accepted_consumers(root: Path) -> frozenset[str]:
    result: set[str] = set()
    for doc_id, (_, metadata, _) in _documents(root).items():
        if metadata.get("Status") == "Accepted" and "OCP-005" in _refs(metadata.get("Depends-On")):
            result.add(doc_id)
    return frozenset(result)


def _baseline_blob(root: Path, relative: str) -> tuple[str, bytes] | None:
    try:
        line = subprocess.check_output(
            ["git", "ls-tree", "-r", BASELINE, "--", relative], cwd=root,
            text=True, stderr=subprocess.DEVNULL,
        ).strip()
        metadata, resolved = line.split("\t", 1)
        if resolved != relative:
            return None
        blob = metadata.split()[2]
        raw = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=root, stderr=subprocess.DEVNULL)
        return blob, raw
    except (OSError, subprocess.CalledProcessError, ValueError, IndexError):
        return None


def _current_counts(root: Path) -> dict[str, int]:
    docs = _documents(root)
    return {
        "Canonical": sum(meta.get("Status") == "Canonical" for _, meta, _ in docs.values()),
        "Accepted": sum(meta.get("Status") == "Accepted" for _, meta, _ in docs.values()),
        "Draft": sum(meta.get("Status") == "Draft" for _, meta, _ in docs.values()),
        "concept_Canonical": sum(meta.get("Concept-Status") == "Canonical" for _, meta, _ in docs.values()),
        "concept_Accepted": sum(meta.get("Concept-Status") == "Accepted" for _, meta, _ in docs.values()),
    }


def _machine_results(root: Path) -> dict[str, bool]:
    from .assignment_amendment_q2 import validate_assignment_amendment_q2
    from .assignment_canonical_readiness import validate_assignment_canonical_readiness
    from .assignment_consumer_compatibility import validate_assignment_consumer_compatibility
    from .assignment_consumer_pressure import validate_assignment_consumer_pressure
    from .assignment_document_acceptance import validate_assignment_document_acceptance
    from .assignment_norm_compatibility import validate_assignment_norm_compatibility
    from .assignment_q2_sufficiency import validate_assignment_q2_sufficiency
    from .assignment_q3_lifecycle import validate_assignment_q3_lifecycle
    from .assignment_q9_sufficiency import validate_assignment_q9_sufficiency
    from .assignment_stable_surface import validate_assignment_stable_surface
    from .assignment_temporal_scope import validate_assignment_temporal_scope

    validators = (
        validate_assignment_stable_surface, validate_assignment_amendment_q2,
        validate_assignment_temporal_scope, validate_assignment_consumer_compatibility,
        validate_assignment_consumer_pressure, validate_assignment_norm_compatibility,
        validate_assignment_q3_lifecycle, validate_assignment_q2_sufficiency,
        validate_assignment_q9_sufficiency, validate_assignment_document_acceptance,
        validate_assignment_canonical_readiness, validate_foundation_promotion_gate,
    )
    return {name: validator(root).valid for name, validator in zip(MACHINE_VALIDATORS, validators)}


def validate_assignment_document_canonicalization(root: Path) -> AssignmentDocumentCanonicalizationResult:
    errors: list[str] = []
    payload = _load(root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_KEYS:
        return _result((ASSIGNMENT_CANONICALIZATION_MAP_INVALID,))
    digest = hashlib.sha256(yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode()).hexdigest()
    if payload.get("schema_version") != 1 or payload.get("rule_owner") != "AD-057" or payload.get("baseline") != BASELINE or digest != MAP_SHA256:
        return _result((ASSIGNMENT_CANONICALIZATION_MAP_INVALID,))

    gate_first = payload.get("gate_first") or {}
    authority = payload.get("authority") or {}
    if gate_first != {
        "route": "Route-F", "operation": "governance-document-lifecycle-promotion",
        "positive_capable": False, "ocp016_g4_applies": False,
        "activation_performed": False,
        "reason": "document-status-promotion-adds-no-operational-rule-result-profile-or-activation",
    } or authority.get("authorized_step") != "DOCUMENT_PROMOTION" or authority.get("unauthorized_step") != "CONCEPT_CANONICALIZATION":
        errors.append(ASSIGNMENT_CANONICALIZATION_BOUNDARY_DRIFT)

    criteria_map = _load(root / CRITERIA_PATH) or {}
    source_ids = tuple(row.get("criterion_id") for row in criteria_map.get("promotion_criteria", []) if isinstance(row, dict))
    declared_ids = tuple((payload.get("criteria_source") or {}).get("criterion_ids") or ())
    rows = payload.get("criteria") or []
    observed_ids = tuple(row.get("criterion_id") for row in rows if isinstance(row, dict))
    if source_ids != CRITERION_IDS or declared_ids != CRITERION_IDS or observed_ids != CRITERION_IDS or len(rows) != 7:
        errors.append(ASSIGNMENT_CANONICALIZATION_CRITERION_DRIFT)
    for row in rows:
        if not isinstance(row, dict) or not row.get("result") or not row.get("basis") or row.get("evidence_mode") not in {"observational", "derived", "analytical-external-gate", "observational-and-analytical-board-act"}:
            errors.append(ASSIGNMENT_CANONICALIZATION_CRITERION_DRIFT)

    documents = _documents(root)
    subject = documents.get("OCP-005", (Path(), {}, ""))
    metadata, text = subject[1], subject[2]
    subject_claim = payload.get("subject") or {}
    if (
        metadata.get("Version") != "1.0.0" or metadata.get("Status") != "Canonical"
        or metadata.get("Concept-Status") != "Accepted"
        or _refs(metadata.get("Depends-On")) != tuple(DIRECT_DEPENDENCIES)
        or subject_claim.get("before") != {"version": "0.4.0", "status": "Accepted", "concept_status": "Accepted"}
        or subject_claim.get("after") != {"version": "1.0.0", "status": "Canonical", "concept_status": "Accepted"}
        or subject_claim.get("semantic_delta") != "none" or subject_claim.get("rights_delta_beyond_accepted") != "none"
    ):
        errors.append(ASSIGNMENT_CANONICALIZATION_SUBJECT_DRIFT)

    declared_dependencies = {
        row.get("document_id"): (str(row.get("version")), row.get("status"))
        for row in payload.get("direct_dependencies") or [] if isinstance(row, dict)
    }
    actual_dependencies = {
        doc_id: (str(documents[doc_id][1].get("Version")), documents[doc_id][1].get("Status"))
        for doc_id in DIRECT_DEPENDENCIES if doc_id in documents
    }
    if declared_dependencies != DIRECT_DEPENDENCIES or actual_dependencies != DIRECT_DEPENDENCIES:
        errors.append(ASSIGNMENT_CANONICALIZATION_DEPENDENCY_DRIFT)

    machine = payload.get("machine_checks") or {}
    if tuple(machine.get("validators") or ()) != MACHINE_VALIDATORS or machine.get("result") != "satisfied" or not all(_machine_results(root).values()):
        errors.append(ASSIGNMENT_CANONICALIZATION_CRITERION_DRIFT)

    surface = payload.get("compatibility_surface") or {}
    need = payload.get("consumer_effect", {}).get("unmet_need", {})
    live_need = _load(root / NEED_PATH) or {}
    live_need_ids = set((live_need.get("current_result") or {}).get("unmet_positive_needs") or ())
    if (
        _open_questions(text) != OPEN_QUESTIONS
        or set(surface.get("withheld") or {}) != OPEN_QUESTIONS
        or surface.get("stable_not_complete") is not True
        or surface.get("dependent_inference_from_silence_permitted") is not False
        or "`Canonical` означає стабільну versioned governance-поверхню" not in str(surface.get("canonical_meaning_exact_quote"))
        or _accepted_consumers(root) != CONSUMERS
        or frozenset(payload.get("consumer_effect", {}).get("accepted_direct_consumers") or ()) != CONSUMERS
        or need.get("state") != "unmet" or need.get("supplied_by_promotion") is not False
        or live_need_ids != {"RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS"}
        or "occupied=false" not in text or "remains unmet" not in text
    ):
        errors.append(ASSIGNMENT_CANONICALIZATION_BOUNDARY_DRIFT)

    gate = _load(root / GATE_PATH)
    transition = payload.get("gate_transition") or {}
    if (
        not validate_foundation_promotion_gate(root).valid
        or not assignment_document_promotion_prefix_is_current(gate)
        or transition.get("active_cycle_id_before") != "ASSIGNMENT_T6"
        or transition.get("active_cycle_id_after") != "ASSIGNMENT_T6"
        or transition.get("before") != {"CANDIDATE_BOARD_SELECTION": "completed", "DOCUMENT_PROMOTION": "pending", "CONCEPT_CANONICALIZATION": "pending"}
        or transition.get("after") != {"CANDIDATE_BOARD_SELECTION": "completed", "DOCUMENT_PROMOTION": "completed", "CONCEPT_CANONICALIZATION": "pending"}
        or transition.get("cycle_completed") is not False
    ):
        errors.append(ASSIGNMENT_CANONICALIZATION_GATE_DRIFT)

    consequence = payload.get("dependent_consequence") or {}
    constraint = documents.get("OCP-006", (Path(), {}, ""))[1]
    if (
        consequence.get("before_l2") != {"result": "fail", "blockers": ["OCP-005"]}
        or consequence.get("after_l2") != {"result": "pass", "blockers": []}
        or consequence.get("lifecycle_effect") != "none"
        or constraint.get("Version") != "0.4.0" or constraint.get("Status") != "Accepted"
        or constraint.get("Concept-Status") != "Accepted"
    ):
        errors.append(ASSIGNMENT_CANONICALIZATION_DEPENDENCY_DRIFT)

    snapshot_map = _load(root / SNAPSHOT_MAP_PATH) or {}
    entry = next((row for row in snapshot_map.get("entries", []) if isinstance(row, dict) and row.get("document_id") == "OCP-005"), {})
    reviewed = payload.get("reviewed_body") or {}
    if (
        entry.get("current_status") != "Canonical" or entry.get("basis") != "retained-acceptance-evidence"
        or entry.get("snapshot") != reviewed.get("path") or entry.get("sha256") != reviewed.get("sha256")
        or reviewed.get("canonical_snapshot_required_by_norm") is not False
        or hashlib.sha256((root / str(reviewed.get("path", ""))).read_bytes()).hexdigest() != reviewed.get("sha256")
        or set(snapshot_map.get("required_retained_evidence") or ()) != {"OCP-005", "OCP-016"}
    ):
        errors.append(ASSIGNMENT_CANONICALIZATION_SNAPSHOT_DRIFT)

    projection = payload.get("current_projection") or {}
    counts = _current_counts(root)
    if (
        projection.get("OCP-005") != {"version": "1.0.0", "status": "Canonical", "concept_status": "Accepted"}
        or projection.get("OCP-006") != {"version": "0.4.0", "status": "Accepted", "concept_status": "Accepted", "canonical_l2": "pass"}
        or projection.get("primary_document_status_counts") != {key: counts[key] for key in ("Canonical", "Accepted", "Draft")}
        or projection.get("concept_status_counts") != {"Canonical": counts["concept_Canonical"], "Accepted": counts["concept_Accepted"]}
        or projection.get("active_cycle_id") != "ASSIGNMENT_T6"
        or projection.get("accepted_snapshot_count") != 14 or projection.get("retained_snapshot_count") != 2
    ):
        errors.append(ASSIGNMENT_CANONICALIZATION_BOUNDARY_DRIFT)

    successions = payload.get("historical_evidence_successions") or []
    if len(successions) != 19:
        errors.append(ASSIGNMENT_CANONICALIZATION_HISTORY_DRIFT)
    for row in successions:
        original = str(row.get("original_path", ""))
        preserved = Path(str(row.get("preserved_path", "")))
        baseline = _baseline_blob(root, original)
        try:
            raw = (root / preserved).read_bytes()
        except OSError:
            raw = b""
        if (
            preserved.is_absolute() or ".." in preserved.parts or baseline is None
            or raw != baseline[1] or hashlib.sha256(raw).hexdigest() != row.get("sha256")
        ):
            errors.append(ASSIGNMENT_CANONICALIZATION_HISTORY_DRIFT)

    atomic = payload.get("atomicity") or {}
    rollback = payload.get("rollback") or {}
    if (
        atomic.get("complete") is not True or atomic.get("partial_effect_permitted") is not False
        or len(atomic.get("required_elements") or ()) != 11
        or rollback.get("restores") != {"OCP-005": "0.4.0-Accepted", "DOCUMENT_PROMOTION": "pending", "active_cycle_id": "ASSIGNMENT_T6"}
        or rollback.get("partial_rollback_permitted") is not False
        or rollback.get("history_rewrite_permitted") is not False
        or frozenset(payload.get("non_implications") or ()) != NON_IMPLICATIONS
    ):
        errors.append(ASSIGNMENT_CANONICALIZATION_BOUNDARY_DRIFT)

    try:
        tree = subprocess.check_output(["git", "ls-tree", "-r", BASELINE], cwd=root, text=True, stderr=subprocess.DEVNULL).splitlines()
        reverse: dict[str, list[str]] = {}
        for line in tree:
            meta, relative = line.split("\t", 1)
            reverse.setdefault(meta.split()[2], []).append(relative)
        for row in payload.get("baseline_evidence_objects") or []:
            raw = subprocess.check_output(["git", "cat-file", "blob", row["blob"]], cwd=root, stderr=subprocess.DEVNULL)
            if row["path"] not in reverse.get(row["blob"], []) or hashlib.sha256(raw).hexdigest() != row["sha256"] or not all(token in raw.decode("utf-8") for token in row["state_tokens"]):
                errors.append(ASSIGNMENT_CANONICALIZATION_ANCHOR_DRIFT)
    except (OSError, subprocess.CalledProcessError, KeyError, ValueError, UnicodeDecodeError):
        errors.append(ASSIGNMENT_CANONICALIZATION_ANCHOR_DRIFT)
    return _result(errors)
