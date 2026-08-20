from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from typing import Any, Iterable

import yaml


ASSIGNMENT_CANONICAL_READINESS_MAP_INVALID = "ASSIGNMENT_CANONICAL_READINESS_MAP_INVALID"
ASSIGNMENT_CANONICAL_READINESS_CRITERION_DRIFT = "ASSIGNMENT_CANONICAL_READINESS_CRITERION_DRIFT"
ASSIGNMENT_CANONICAL_READINESS_SUBJECT_DRIFT = "ASSIGNMENT_CANONICAL_READINESS_SUBJECT_DRIFT"
ASSIGNMENT_CANONICAL_READINESS_DEPENDENCY_DRIFT = "ASSIGNMENT_CANONICAL_READINESS_DEPENDENCY_DRIFT"
ASSIGNMENT_CANONICAL_READINESS_CHECK_DRIFT = "ASSIGNMENT_CANONICAL_READINESS_CHECK_DRIFT"
ASSIGNMENT_CANONICAL_READINESS_OPEN_QUESTION_DRIFT = "ASSIGNMENT_CANONICAL_READINESS_OPEN_QUESTION_DRIFT"
ASSIGNMENT_CANONICAL_READINESS_NEED_DRIFT = "ASSIGNMENT_CANONICAL_READINESS_NEED_DRIFT"
ASSIGNMENT_CANONICAL_READINESS_SLOT_DRIFT = "ASSIGNMENT_CANONICAL_READINESS_SLOT_DRIFT"
ASSIGNMENT_CANONICAL_READINESS_BOUNDARY_DRIFT = "ASSIGNMENT_CANONICAL_READINESS_BOUNDARY_DRIFT"
ASSIGNMENT_CANONICAL_READINESS_ANCHOR_DRIFT = "ASSIGNMENT_CANONICAL_READINESS_ANCHOR_DRIFT"

MAP_PATH = Path("architecture/assignment-canonical-readiness.yaml")
CRITERIA_PATH = Path("architecture/constraint-document-status-readiness.yaml")
SUBJECT_PATH = Path("docs/005-assignment-concept/README.md")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
NEED_PATH = Path("architecture/consumer-need-discovery.yaml")
BASELINE = "5fab92bfa9d7392a325c5577e5aba69c0049ba24"
MAP_SHA256 = "779db359496b2ec3b1f0ff12f55c2b8235224fcd1f7330e40fabe5fdd286fe7f"

CRITERION_IDS = (
    "BINDING_REVIEW_LANE",
    "EXACT_ROUTE_AND_AUTHORITY_LEDGER",
    "BOARD_ACCEPTS_CURRENT_SEMANTICS",
    "ATOMIC_DOCUMENT_PROMOTION_UNIT",
    "CANONICAL_STABILITY_CHECKS_AND_BOARD_ACT",
    "CANONICAL_DIRECT_DEPENDENCY_FLOOR_L2",
    "EXACT_HEAD_AUTHORIZATION_AND_ATOMIC_EFFECT",
)
EXPECTED_ASSESSMENTS = {
    "BINDING_REVIEW_LANE": ("Canonical-transition-carried", "pending-separate-canonicalization-act", "no-subject-readiness-failure"),
    "EXACT_ROUTE_AND_AUTHORITY_LEDGER": ("Canonical", "satisfied-for-readiness", "pass"),
    "BOARD_ACCEPTS_CURRENT_SEMANTICS": ("Accepted-only-previously-passed", "not-re-evaluated", "excluded-from-Canonical-assessment"),
    "ATOMIC_DOCUMENT_PROMOTION_UNIT": ("Canonical-transition-carried", "future-unit-is-exactly-enumerable-but-not-executed", "no-subject-readiness-failure"),
    "CANONICAL_STABILITY_CHECKS_AND_BOARD_ACT": ("Canonical", "readiness-prerequisites-satisfied-board-act-pending", "pass-subject-evidence-pending-transition-authority"),
    "CANONICAL_DIRECT_DEPENDENCY_FLOOR_L2": ("Canonical", "satisfied", "pass"),
    "EXACT_HEAD_AUTHORIZATION_AND_ATOMIC_EFFECT": ("Canonical-transition-carried", "pending-separate-canonicalization-act", "no-subject-readiness-failure"),
}
DIRECT_DEPENDENCIES = {
    "OCP-000": ("1.6.0", "Canonical"),
    "OCP-001": ("1.0.0", "Canonical"),
    "OCP-002": ("1.6.0", "Canonical"),
    "OCP-003": ("1.0.0", "Canonical"),
    "OCP-004": ("1.0.1", "Canonical"),
}
CONCEPT_DEPENDENCIES = {
    "Resource": ("OCP-003", "Canonical"),
    "Operation": ("OCP-004", "Canonical"),
}
OPEN_QUESTIONS = frozenset({"Q2", "Q4", "Q5", "Q7", "Q8", "Q9", "Q10", "Q11"})
CANONICAL_OPEN_CARRIERS = frozenset({"OCP-002", "OCP-003", "OCP-004", "OCP-007", "OCP-008", "OCP-010"})
MACHINE_VALIDATORS = (
    "assignment-stable-surface",
    "assignment-amendment-q2",
    "assignment-temporal-scope",
    "assignment-consumer-compatibility",
    "assignment-consumer-pressure",
    "assignment-norm-compatibility",
    "assignment-q3-lifecycle",
    "assignment-q2-sufficiency",
    "assignment-q9-sufficiency",
    "assignment-document-acceptance",
)
NON_IMPLICATIONS = frozenset({
    "NO_CANONICALIZATION", "NO_CANDIDATE_SELECTION", "NO_PROMOTION_CYCLE_START",
    "NO_ACTIVE_CYCLE_CHANGE", "NO_DOCUMENT_STATUS_OR_VERSION_CHANGE",
    "NO_CONCEPT_STATUS_CHANGE", "NO_QUESTION_CLOSURE",
    "NO_POSITIVE_NEED_SATISFACTION", "NO_POSITIVE_ACTIVATION",
    "NO_NEXT_ACT_AUTHORIZATION",
})
EXPECTED_KEYS = frozenset({
    "schema_version", "rule_owner", "baseline", "gate_first", "subject",
    "criteria_source", "criteria_assessment", "stable_dependencies",
    "machine_readable_checks", "open_questions", "unmet_positive_need",
    "slot_occupancy", "result", "protected_current_state", "non_implications",
    "versioning", "migration", "baseline_evidence_objects",
})


@dataclass(frozen=True)
class AssignmentCanonicalReadinessResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentCanonicalReadinessResult:
    return AssignmentCanonicalReadinessResult(tuple(dict.fromkeys(errors)))


def _load(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None


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


def _refs(value: Any) -> tuple[str, ...]:
    values = value if isinstance(value, list) else str(value or "").split(",")
    return tuple(str(item).strip().split("@", 1)[0] for item in values if str(item).strip())


def _documents(root: Path) -> dict[str, tuple[Path, dict[str, Any], str]]:
    result: dict[str, tuple[Path, dict[str, Any], str]] = {}
    for path in sorted((root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(path)
        if not metadata or not isinstance(metadata.get("Document-ID"), str):
            continue
        result[str(metadata["Document-ID"])] = (path, metadata, path.read_text(encoding="utf-8"))
    return result


def _open_questions(text: str) -> frozenset[str]:
    start = text.find("## 19. Open Questions and Resolved Boundaries")
    end = text.find("## 20. Deferred Decisions", start + 1)
    if start < 0 or end < 0:
        return frozenset()
    return frozenset(
        f"Q{match.group(1)}"
        for line in text[start:end].splitlines()
        if (match := re.match(r"^(\d+)\.\s+(.*)$", line.strip())) and not match.group(2).startswith("~~")
    )


def slot_reuse_probe(root: Path) -> bool:
    from .foundation_promotion_gate import validate_foundation_promotion_gate

    with tempfile.TemporaryDirectory() as tmp:
        probe_root = Path(tmp)
        for source in (root / "docs").glob("[0-9][0-9][0-9]-*/README.md"):
            relative = source.relative_to(root)
            target = probe_root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        target = probe_root / GATE_PATH
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / GATE_PATH, target)
        payload = yaml.safe_load(target.read_text(encoding="utf-8"))
        payload["cycles"].append({
            "cycle_id": "ASSIGNMENT_T6",
            "candidate_id": "OCP-005",
            "slot": "T6",
            "steps": {
                "CANDIDATE_BOARD_SELECTION": "completed",
                "DOCUMENT_PROMOTION": "pending",
                "CONCEPT_CANONICALIZATION": "pending",
            },
            "evidence": {"CANDIDATE_BOARD_SELECTION": "SYNTHETIC_BOARD_ACT"},
        })
        payload["cycle_protocol"]["active_cycle_id"] = "ASSIGNMENT_T6"
        target.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        return validate_foundation_promotion_gate(probe_root).valid


def _machine_results(root: Path) -> dict[str, bool]:
    from .assignment_amendment_q2 import validate_assignment_amendment_q2
    from .assignment_consumer_compatibility import validate_assignment_consumer_compatibility
    from .assignment_consumer_pressure import validate_assignment_consumer_pressure
    from .assignment_document_acceptance import validate_assignment_document_acceptance
    from .assignment_norm_compatibility import validate_assignment_norm_compatibility
    from .assignment_q2_sufficiency import validate_assignment_q2_sufficiency
    from .assignment_q3_lifecycle import validate_assignment_q3_lifecycle
    from .assignment_q9_sufficiency import validate_assignment_q9_sufficiency
    from .assignment_stable_surface import validate_assignment_stable_surface
    from .assignment_temporal_scope import validate_assignment_temporal_scope

    validators = {
        "assignment-stable-surface": validate_assignment_stable_surface,
        "assignment-amendment-q2": validate_assignment_amendment_q2,
        "assignment-temporal-scope": validate_assignment_temporal_scope,
        "assignment-consumer-compatibility": validate_assignment_consumer_compatibility,
        "assignment-consumer-pressure": validate_assignment_consumer_pressure,
        "assignment-norm-compatibility": validate_assignment_norm_compatibility,
        "assignment-q3-lifecycle": validate_assignment_q3_lifecycle,
        "assignment-q2-sufficiency": validate_assignment_q2_sufficiency,
        "assignment-q9-sufficiency": validate_assignment_q9_sufficiency,
        "assignment-document-acceptance": validate_assignment_document_acceptance,
    }
    return {name: validators[name](root).valid for name in MACHINE_VALIDATORS}


def validate_assignment_canonical_readiness(root: Path) -> AssignmentCanonicalReadinessResult:
    errors: list[str] = []
    payload = _load(root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_KEYS:
        return _result((ASSIGNMENT_CANONICAL_READINESS_MAP_INVALID,))
    digest = hashlib.sha256(yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode()).hexdigest()
    if payload.get("schema_version") != 1 or payload.get("rule_owner") != "AD-055" or payload.get("baseline") != BASELINE or digest != MAP_SHA256:
        return _result((ASSIGNMENT_CANONICAL_READINESS_MAP_INVALID,))

    gate_first = payload.get("gate_first") or {}
    result = payload.get("result") or {}
    if gate_first != {
        "ocp016_gate": "G4", "applies": False, "positive_capable": False,
        "activation_performed": False,
        "reason": "discovery-classifies-existing-canonical-readiness-evidence-without-adding-or-activating-a-rule-result-profile",
    } or result != {
        "subject_readiness_prerequisites": "satisfied",
        "transition_carried_requirements": "pending-separate-canonicalization-act",
        "ready_for_separate_cycle-and-canonicalization-proposal": True,
        "canonicalization_authorized": False, "candidate_selected": False,
        "cycle_opened": False, "lifecycle_effect": "none",
    }:
        errors.append(ASSIGNMENT_CANONICAL_READINESS_BOUNDARY_DRIFT)

    criteria = _load(root / CRITERIA_PATH)
    source_rows = criteria.get("promotion_criteria") if isinstance(criteria, dict) else None
    source_ids = tuple(row.get("criterion_id") for row in source_rows or () if isinstance(row, dict))
    declared_ids = tuple((payload.get("criteria_source") or {}).get("criterion_ids") or ())
    assessments = {
        row.get("criterion_id"): (row.get("applicability"), row.get("result"), row.get("readiness_effect"))
        for row in payload.get("criteria_assessment") or () if isinstance(row, dict)
    }
    if source_ids != CRITERION_IDS or declared_ids != CRITERION_IDS or assessments != EXPECTED_ASSESSMENTS:
        errors.append(ASSIGNMENT_CANONICAL_READINESS_CRITERION_DRIFT)

    documents = _documents(root)
    subject = documents.get("OCP-005")
    metadata = subject[1] if subject else {}
    subject_text = subject[2] if subject else ""
    protected = payload.get("protected_current_state") or {}
    if (
        metadata.get("Version") != "0.4.0" or metadata.get("Status") != "Accepted"
        or metadata.get("Concept-Status") != "Accepted"
        or _refs(metadata.get("Depends-On")) != tuple(DIRECT_DEPENDENCIES)
        or protected.get("document_version") != metadata.get("Version")
        or protected.get("document_status") != metadata.get("Status")
        or protected.get("concept_status") != metadata.get("Concept-Status")
    ):
        errors.append(ASSIGNMENT_CANONICAL_READINESS_SUBJECT_DRIFT)

    declared_direct = {
        row.get("document_id"): (str(row.get("version")), row.get("status"))
        for row in (payload.get("stable_dependencies") or {}).get("direct_ocp") or () if isinstance(row, dict)
    }
    actual_direct = {
        doc_id: (str(documents.get(doc_id, ({}, {}, ""))[1].get("Version")), documents.get(doc_id, ({}, {}, ""))[1].get("Status"))
        for doc_id in DIRECT_DEPENDENCIES
    }
    declared_concepts = {
        row.get("concept_id"): (row.get("defining_document"), row.get("status"))
        for row in (payload.get("stable_dependencies") or {}).get("concept") or () if isinstance(row, dict)
    }
    registry = documents.get("OCP-000", ({}, {}, ""))[2]
    taxonomy = documents.get("OCP-002", ({}, {}, ""))[2]
    if (
        declared_direct != DIRECT_DEPENDENCIES or actual_direct != DIRECT_DEPENDENCIES
        or declared_concepts != CONCEPT_DEPENDENCIES
        or "| Resource | Canonical |" not in registry or "| Operation | Canonical |" not in registry
        or "Resource: Canonical" not in taxonomy or "Operation: Canonical" not in taxonomy
        or (payload.get("stable_dependencies") or {}).get("result") != "satisfied"
    ):
        errors.append(ASSIGNMENT_CANONICAL_READINESS_DEPENDENCY_DRIFT)

    checks = payload.get("machine_readable_checks") or {}
    if tuple(checks.get("validators") or ()) != MACHINE_VALIDATORS or checks.get("result") != "satisfied" or not all(_machine_results(root).values()):
        errors.append(ASSIGNMENT_CANONICAL_READINESS_CHECK_DRIFT)

    open_data = payload.get("open_questions") or {}
    canonical_carriers = {
        doc_id for doc_id, (_, doc_meta, text) in documents.items()
        if doc_meta.get("Status") == "Canonical" and re.search(r"(?:Open Questions|unresolved|залиша(?:ється|ються) відкрит|лиша(?:ється|ються) відкрит)", text, re.IGNORECASE)
    }
    if (
        _open_questions(subject_text) != OPEN_QUESTIONS
        or frozenset(open_data.get("current_ids") or ()) != OPEN_QUESTIONS
        or frozenset(open_data.get("canonical_precedent_carriers") or ()) != CANONICAL_OPEN_CARRIERS
        or not CANONICAL_OPEN_CARRIERS.issubset(canonical_carriers)
        or open_data.get("Canonical_criterion_found") is not False
        or "all open questions" in documents.get("OCP-001", ({}, {}, ""))[2].lower()
    ):
        errors.append(ASSIGNMENT_CANONICAL_READINESS_OPEN_QUESTION_DRIFT)

    need_map = _load(root / NEED_PATH)
    need_rows = need_map.get("candidate_mentions") if isinstance(need_map, dict) else []
    observed_need = next((row for row in need_rows or () if isinstance(row, dict) and row.get("candidate_id") == "RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS"), None)
    need = payload.get("unmet_positive_need") or {}
    if (
        not observed_need or observed_need.get("artifact_id") != "OCP-023"
        or observed_need.get("disposition") != "current-unmet-positive-consumer-need"
        or need.get("current_state") != "unmet" or need.get("Canonical_criterion_found") is not False
        or need.get("exact_result") != "assignment_set_complete_for_resource(resource_ref, evaluation_time, snapshot_ref)"
        or frozenset(need.get("remains_unavailable_after_hypothetical_canonicalization") or ()) != frozenset({"assignment-set-completeness", "legitimate-real-evaluator", "occupied-false-without-completeness"})
    ):
        errors.append(ASSIGNMENT_CANONICAL_READINESS_NEED_DRIFT)

    promotion_gate = _load(root / GATE_PATH)
    slot = payload.get("slot_occupancy") or {}
    candidate = next((row for row in (promotion_gate or {}).get("candidates", []) if row.get("document_id") == "OCP-005"), None)
    cycles = (promotion_gate or {}).get("cycles", [])
    if (
        not candidate or candidate.get("slot") != "T6"
        or [row.get("cycle_id") for row in cycles] != ["EVENT_T6"]
        or cycles[0].get("slot") != "T6"
        or (promotion_gate.get("cycle_protocol") or {}).get("active_cycle_id") is not None
        or slot.get("current_protocol_requires_unique") != ["cycle_id", "candidate_id"]
        or slot.get("current_protocol_does_not_require_unique") != ["slot"]
        or not slot_reuse_probe(root)
    ):
        errors.append(ASSIGNMENT_CANONICAL_READINESS_SLOT_DRIFT)

    counts = {"Canonical": 0, "Accepted": 0, "Draft": 0}
    for _, doc_meta, _ in documents.values():
        status = doc_meta.get("Status")
        if status in counts:
            counts[status] += 1
    if (
        protected.get("active_cycle_id") is not None
        or protected.get("primary_document_status_counts") != counts
        or protected.get("registry_status") != "Accepted" or "| Assignment | Accepted |" not in registry
        or protected.get("taxonomy_status") != "Accepted" or "Assignment: Accepted" not in taxonomy
        or frozenset(payload.get("non_implications") or ()) != NON_IMPLICATIONS
    ):
        errors.append(ASSIGNMENT_CANONICAL_READINESS_BOUNDARY_DRIFT)

    try:
        tree = subprocess.check_output(
            ["git", "ls-tree", "-r", payload["baseline"]], cwd=root, text=True,
            stderr=subprocess.DEVNULL,
        ).splitlines()
        reverse: dict[str, list[str]] = {}
        for line in tree:
            metadata_text, path = line.split("\t", 1)
            reverse.setdefault(metadata_text.split()[2], []).append(path)
        for item in payload.get("baseline_evidence_objects") or ():
            raw = subprocess.check_output(
                ["git", "cat-file", "blob", item["blob"]], cwd=root,
                stderr=subprocess.DEVNULL,
            )
            if item["path"] not in reverse.get(item["blob"], []) or hashlib.sha256(raw).hexdigest() != item["sha256"] or not all(token in raw.decode("utf-8") for token in item["state_tokens"]):
                errors.append(ASSIGNMENT_CANONICAL_READINESS_ANCHOR_DRIFT)
    except (OSError, subprocess.CalledProcessError, KeyError, ValueError):
        errors.append(ASSIGNMENT_CANONICAL_READINESS_ANCHOR_DRIFT)
    return _result(errors)
