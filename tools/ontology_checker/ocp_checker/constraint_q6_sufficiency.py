from __future__ import annotations

import copy
from dataclasses import dataclass
import hashlib
from pathlib import Path
from typing import Any, Iterable

import yaml

from .checker import effective_constraint_result, load_fixture, validate_constraint
from .historical_evidence import historical_path
from .foundation_promotion_gate import validate_foundation_promotion_gate


CONSTRAINT_Q6_MAP_INVALID = "CONSTRAINT_Q6_MAP_INVALID"
CONSTRAINT_Q6_CRITERION_DRIFT = "CONSTRAINT_Q6_CRITERION_DRIFT"
CONSTRAINT_Q6_INVENTORY_DRIFT = "CONSTRAINT_Q6_INVENTORY_DRIFT"
CONSTRAINT_Q6_EVIDENCE_DRIFT = "CONSTRAINT_Q6_EVIDENCE_DRIFT"
CONSTRAINT_Q6_PROBE_DRIFT = "CONSTRAINT_Q6_PROBE_DRIFT"
CONSTRAINT_Q6_SUBJECT_DRIFT = "CONSTRAINT_Q6_SUBJECT_DRIFT"
CONSTRAINT_Q6_PROJECTION_DRIFT = "CONSTRAINT_Q6_PROJECTION_DRIFT"
CONSTRAINT_Q6_GATE_DRIFT = "CONSTRAINT_Q6_GATE_DRIFT"

MAP_PATH = Path("architecture/constraint-q6-sufficiency.yaml")
SUBJECT_PATH = Path("docs/006-constraint-concept/README.md")
SURFACE_PATH = Path("architecture/constraint-stable-surface.yaml")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
PROBE_FIXTURE = Path("tools/ontology_checker/fixtures/constraint/valid-blocking.yaml")
BASELINE = "50cfb512f17880218060619363774a9fa38a874a"
SUBJECT_SHA256 = "0472d8ce4b15a8c64d58151ee7f706b450b930f708f6f0a7a40bdd87914b3b10"
MAP_SHA256 = "31f082ba7ed6c5b676122cb23238750b3906a02a32d27f85596744cf73cd7247"

DIRECT_DEPENDENCIES = frozenset({"OCP-000", "OCP-001", "OCP-002", "OCP-003", "OCP-004", "OCP-005"})
DIRECT_CONSUMERS = frozenset({"OCP-011", "OCP-013", "OCP-014", "OCP-015", "OCP-017", "OCP-018", "OCP-019", "OCP-020", "OCP-021"})
BASIS_TYPES = frozenset({"direct-normative-statement", "inference-from-list", "inference-from-silence"})
EXPECTED_FORBIDDEN = frozenset({
    "Q6_CLOSURE", "ANY_OTHER_QUESTION_CLOSURE", "OCP006_CHANGE", "OCP006_STATUS_CHANGE",
    "EVALUATION_CURRENTNESS_BLOCKER_REMOVAL", "CONSTRAINT_READINESS_CHANGE",
    "POSITIVE_MODEL_ACTIVATION", "CONSTRAINT_SELECTION", "PROMOTION_CYCLE_START",
    "GRAPH_OR_REGISTRY_CHANGE", "NEXT_ACT_AUTHORIZATION",
})
EXPECTED_MAP_KEYS = frozenset({
    "schema_version", "rule_owner", "baseline", "baseline_evidence_objects", "gate_first",
    "sufficiency_criterion", "normative_scope", "normative_inventory", "record_shape_basis",
    "explicit_obstacle", "executable_probe", "answer_disposition", "decision",
    "subject_preservation", "current_projection", "versioning", "migration",
    "forbidden_outcomes", "protected_artifacts",
})
DOC_PATHS = {
    f"OCP-{number:03d}": Path(path) for number, path in (
        (0, "docs/000-operational-ontology/README.md"),
        (1, "docs/001-ontology-governance/README.md"),
        (2, "docs/002-concept-taxonomy/README.md"),
        (3, "docs/003-resource-concept/README.md"),
        (4, "docs/004-operation-concept/README.md"),
        (5, "docs/005-assignment-concept/README.md"),
        (6, "docs/006-constraint-concept/README.md"),
        (11, "docs/011-outcome-assessment-record/README.md"),
        (13, "docs/013-resource-interchangeability/README.md"),
        (14, "docs/014-coordination-profile/README.md"),
        (15, "docs/015-coordination-workflow/README.md"),
        (17, "docs/017-operation-lifecycle/README.md"),
        (18, "docs/018-operation-authorization-source/README.md"),
        (19, "docs/019-conflict-derivation-boundary/README.md"),
        (20, "docs/020-quantitative-constraint-input/README.md"),
        (21, "docs/021-reservation-allocation-boundary/README.md"),
    )
}


@dataclass(frozen=True)
class ConstraintQ6SufficiencyResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> ConstraintQ6SufficiencyResult:
    return ConstraintQ6SufficiencyResult(tuple(dict.fromkeys(errors)))


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


def _refs(value: Any) -> frozenset[str]:
    if isinstance(value, str):
        return frozenset(part.strip() for part in value.split(",") if part.strip())
    if isinstance(value, list):
        return frozenset(str(part).strip() for part in value if str(part).strip())
    return frozenset()


def validate_constraint_q6_sufficiency(repo_root: Path) -> ConstraintQ6SufficiencyResult:
    errors: list[str] = []
    payload = _load(repo_root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_MAP_KEYS:
        return _result((CONSTRAINT_Q6_MAP_INVALID,))
    digest = hashlib.sha256(yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode()).hexdigest()
    if (
        digest != MAP_SHA256 or payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-051" or payload.get("baseline") != BASELINE
        or frozenset(payload.get("forbidden_outcomes") or ()) != EXPECTED_FORBIDDEN
    ):
        errors.append(CONSTRAINT_Q6_MAP_INVALID)

    gate = payload.get("gate_first") or {}
    criterion = payload.get("sufficiency_criterion") or {}
    decision = payload.get("decision") or {}
    if (
        gate.get("evidence_form", {}).get("applies") is not False
        or gate.get("evidence_form", {}).get("positive_capable") is not False
        or gate.get("hypothetical_answers", {}).get("magnitude-established", {}).get("applies") is not True
        or gate.get("hypothetical_answers", {}).get("magnitude-unnecessary-with-replacement", {}).get("applies") is not True
        or gate.get("hypothetical_answers", {}).get("not-established-until-separate-decision", {}).get("applies") is not False
        or criterion.get("declared_before_application") is not True
        or set((criterion.get("basis_types") or {}).keys()) != BASIS_TYPES
        or criterion.get("basis_types", {}).get("inference-from-silence") != "never-sufficient"
        or criterion.get("result") != "insufficient-for-q6-closure"
        or decision != {
            "question_id": "Q6", "disposition": "remains-open-insufficient-evidence",
            "criterion_satisfied": False, "closure_authorized_by_this_outcome": False,
            "subject_changed": False, "blocker_removed": False,
        }
    ):
        errors.append(CONSTRAINT_Q6_CRITERION_DRIFT)

    metadata = {doc_id: _frontmatter(repo_root / path) for doc_id, path in DOC_PATHS.items()}
    subject_meta = metadata.get("OCP-006") or {}
    dependencies = _refs(subject_meta.get("Depends-On")) & frozenset(DOC_PATHS)
    consumers = frozenset(
        doc_id for doc_id, item in metadata.items()
        if doc_id != "OCP-006" and item is not None and "OCP-006" in _refs(item.get("Depends-On"))
    )
    scope = payload.get("normative_scope") or {}
    inventory = payload.get("normative_inventory") or []
    inventory_ids = [item.get("document_id") for item in inventory if isinstance(item, dict)]
    if (
        dependencies != DIRECT_DEPENDENCIES or consumers != DIRECT_CONSUMERS
        or set(scope.get("direct_dependencies") or ()) != DIRECT_DEPENDENCIES
        or set(scope.get("direct_consumers") or ()) != DIRECT_CONSUMERS
        or scope.get("subject") != "OCP-006"
        or len(inventory_ids) != 16 or set(inventory_ids) != set(DOC_PATHS)
    ):
        errors.append(CONSTRAINT_Q6_INVENTORY_DRIFT)

    for row in inventory:
        if not isinstance(row, dict) or row.get("basis_type") not in BASIS_TYPES or row.get("sufficient") is not False:
            errors.append(CONSTRAINT_Q6_EVIDENCE_DRIFT)
            break
        path = DOC_PATHS.get(str(row.get("document_id")))
        try:
            text = (repo_root / path).read_text(encoding="utf-8") if path else ""
        except OSError:
            text = ""
        if any(str(token) not in text for token in row.get("tokens") or ()):
            errors.append(CONSTRAINT_Q6_EVIDENCE_DRIFT)
            break
        if row.get("basis_type") == "inference-from-silence" and row.get("tokens") != []:
            errors.append(CONSTRAINT_Q6_EVIDENCE_DRIFT)
            break

    historical_subject = historical_path(repo_root, SUBJECT_PATH, SUBJECT_SHA256)
    subject_text = ""
    try:
        subject_text = (repo_root / historical_subject).read_text(encoding="utf-8")
    except OSError:
        pass
    obstacle = payload.get("explicit_obstacle") or {}
    if (
        _hash(repo_root / historical_subject) != SUBJECT_SHA256
        or (_frontmatter(repo_root / historical_subject) or {}).get("Version") != "0.3.2"
        or (_frontmatter(repo_root / historical_subject) or {}).get("Status") != "Draft"
        or subject_meta.get("Concept-Status") != "Accepted"
        or obstacle.get("same_subject_as_q6") is not True or obstacle.get("quote") not in subject_text
        or payload.get("subject_preservation", {}).get("sha256") != SUBJECT_SHA256
    ):
        errors.append(CONSTRAINT_Q6_SUBJECT_DRIFT)

    surface = _load(repo_root / SURFACE_PATH)
    blockers = surface.get("blockers") if isinstance(surface, dict) else None
    q6 = next((item for item in surface.get("question_inventory", []) if item.get("question_id") == "Q6"), None) if isinstance(surface, dict) else None
    blocker = next((item for item in blockers or [] if item.get("blocker_id") == "EVALUATION_CURRENTNESS_UNRESOLVED"), None)
    projection = payload.get("current_projection") or {}
    if (
        not q6 or q6.get("state") != "open" or q6.get("classification") != "blocks-whole-document-freeze"
        or not blocker or blocker.get("question_ids") != ["Q6"]
        or projection.get("q6_state") != "open"
        or projection.get("blocker", {}).get("question_ids") != ["Q6"]
        or projection.get("whole_document_freeze_reachable") is not False
    ):
        errors.append(CONSTRAINT_Q6_PROJECTION_DRIFT)

    fixture = _load(repo_root / PROBE_FIXTURE)
    try:
        entity = fixture["entity"]
        context = fixture["contexts"][0]
        version = fixture["reference"]["constraint_version_ref"]
        observations = payload["executable_probe"]["observed_mutations"]
        for observation in observations:
            mutated = copy.deepcopy(entity)
            mutated["evaluation_records"][0]["evaluated_at"] = observation["evaluated_at"]
            if validate_constraint(mutated, {context["context_id"]: context}, version).valid is not observation["expected_valid"]:
                errors.append(CONSTRAINT_Q6_PROBE_DRIFT)
            if effective_constraint_result(mutated, context, version) != observation["expected_effective_result"]:
                errors.append(CONSTRAINT_Q6_PROBE_DRIFT)
        mismatch = copy.deepcopy(context)
        mismatch["input_snapshot_ref"] = "SNAP-MISMATCH"
        if effective_constraint_result(entity, mismatch, version) != payload["executable_probe"]["discriminating_control"]["expected_effective_result"]:
            errors.append(CONSTRAINT_Q6_PROBE_DRIFT)
    except (KeyError, TypeError, IndexError):
        errors.append(CONSTRAINT_Q6_PROBE_DRIFT)

    for item in payload.get("protected_artifacts") or ():
        original = Path(item.get("path", ""))
        resolved = historical_path(repo_root, original, str(item.get("sha256", "")))
        if _hash(repo_root / resolved) != item.get("sha256"):
            errors.append(CONSTRAINT_Q6_EVIDENCE_DRIFT)
            break
    if not validate_foundation_promotion_gate(repo_root).valid:
        errors.append(CONSTRAINT_Q6_GATE_DRIFT)
    return _result(errors)
