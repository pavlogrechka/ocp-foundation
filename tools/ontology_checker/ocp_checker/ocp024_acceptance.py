from __future__ import annotations

import copy
from dataclasses import dataclass
import hashlib
from pathlib import Path
from typing import Any, Iterable

import yaml

from .historical_evidence import historical_path
from .foundation_promotion_gate import promotion_gate_guard_is_current

from .completeness_evaluator import (
    ACTIVATION_FIELDS,
    INDETERMINATE,
    REFERENCE_RESULT,
    derive_completeness_evidence_recognition,
    validate_completeness_evaluator_dataset,
)
from .resource_occupancy import derive_resource_occupancy


OCP024_ACCEPTANCE_MAP_INVALID = "OCP024_ACCEPTANCE_MAP_INVALID"
OCP024_ACCEPTANCE_SUBJECT_DRIFT = "OCP024_ACCEPTANCE_SUBJECT_DRIFT"
OCP024_ACCEPTANCE_SNAPSHOT_DRIFT = "OCP024_ACCEPTANCE_SNAPSHOT_DRIFT"
OCP024_ACCEPTANCE_STATUS_DRIFT = "OCP024_ACCEPTANCE_STATUS_DRIFT"
OCP024_ACCEPTANCE_CONSUMER_NEED_DRIFT = "OCP024_ACCEPTANCE_CONSUMER_NEED_DRIFT"
OCP024_ACCEPTANCE_RUNTIME_BOUNDARY_DRIFT = "OCP024_ACCEPTANCE_RUNTIME_BOUNDARY_DRIFT"
OCP024_ACCEPTANCE_PROTECTED_DRIFT = "OCP024_ACCEPTANCE_PROTECTED_DRIFT"
OCP024_ACCEPTANCE_GATE_DRIFT = "OCP024_ACCEPTANCE_GATE_DRIFT"

MAP_PATH = Path("architecture/ocp024-acceptance.yaml")
SUBJECT_PATH = Path("docs/024-completeness-evaluator/README.md")
SNAPSHOT_PATH = Path("docs/024-completeness-evaluator/reviewed-contract-v0.1.0.md")
SNAPSHOT_MAP_PATH = Path("architecture/accepted-document-snapshot-map.yaml")
NEED_MAP_PATH = Path("architecture/consumer-need-discovery.yaml")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
VALID_FIXTURE = Path("tools/ontology_checker/fixtures/completeness_evaluator/valid-synthetic-reference.yaml")
ZERO_OCCUPANCY_FIXTURE = Path("tools/ontology_checker/fixtures/resource_occupancy/valid-zero-assignments.yaml")

BASELINE = "954e2d76317a993d228d45a77ccfddec0c0f379a"
MAP_SHA256 = "21de9f37c251375b4eabcd3c97194c5bcf9c6f2f894277a8fc90afd00907a7f6"
SNAPSHOT_SHA256 = "0c77e0527ec3adf9ed7cf5bbd32e0a63e55a1c3780f007d35a0ef2630cc18753"
SNAPSHOT_BLOB = "2713c99ca6653d35fc52435eaeaeb8f9f5174b1d"
ACCEPTED_CONSUMERS = frozenset({"OCP-006", "OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021", "OCP-023"})
UNMET_NEEDS = ("RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS",)
FORBIDDEN_OUTCOMES = frozenset(
    {
        "REAL_EVALUATOR_OR_AUTHORITY_LEGITIMIZED", "ASSIGNMENT_SET_COMPLETENESS_ESTABLISHED",
        "G4_BINDING_SATISFIED", "POSITIVE_MODEL_ACTIVATED", "OCP023_NEGATIVE_RESULT_ENABLED",
        "OCP024_COMPLETENESS_PROVIDER", "OTHER_DOCUMENT_STATUS_CHANGE", "OCP005_OR_OCP023_CHANGE",
        "CONCEPT_OR_GRAPH_CHANGE", "ASSIGNMENT_BLOCKER_REMOVAL", "PROMOTION_CYCLE_START",
        "NEXT_ACT_AUTHORIZATION",
    }
)
EXPECTED_MAP_KEYS = frozenset(
    {
        "schema_version", "rule_owner", "current_projection_owner", "baseline", "gate_first", "readiness_criterion",
        "subject", "reviewed_snapshot", "consumer_need_projection", "runtime_boundary",
        "document_status_projection", "protected_artifacts", "promotion_gate_guard",
        "versioning", "migration", "forbidden_outcomes",
    }
)


@dataclass(frozen=True)
class Ocp024AcceptanceResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> Ocp024AcceptanceResult:
    return Ocp024AcceptanceResult(tuple(dict.fromkeys(errors)))


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
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return None
    end = text.find("\n---\n", 4)
    loaded = yaml.safe_load(text[4:end])
    return loaded if isinstance(loaded, dict) else None


def _body(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return ""
    end = text.find("\n---\n", 4)
    return text[end + 5:] if text.startswith("---\n") and end >= 0 else ""


def _status_projection(root: Path) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for path in sorted((root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(path)
        if metadata and isinstance(metadata.get("Document-ID"), str):
            result[metadata["Document-ID"]] = [str(metadata.get("Version")), str(metadata.get("Status"))]
    return result


def _depends_on(metadata: dict[str, Any], target: str) -> bool:
    value = metadata.get("Depends-On", "")
    tokens = value if isinstance(value, list) else str(value).split(",")
    return any(str(item).strip().split("@", 1)[0] == target for item in tokens)


def _accepted_consumers(root: Path, target: str) -> frozenset[str]:
    values = set()
    for path in (root / "docs").glob("[0-9][0-9][0-9]-*/README.md"):
        metadata = _frontmatter(path)
        if metadata and metadata.get("Status") == "Accepted" and _depends_on(metadata, target):
            values.add(str(metadata.get("Document-ID")))
    return frozenset(values)


def _ocp024_dependents(root: Path) -> list[str]:
    values = []
    for path in (root / "docs").glob("[0-9][0-9][0-9]-*/README.md"):
        metadata = _frontmatter(path)
        if metadata and _depends_on(metadata, "OCP-024"):
            values.append(str(metadata.get("Document-ID")))
    return sorted(values)


def validate_ocp024_acceptance(repo_root: Path) -> Ocp024AcceptanceResult:
    errors: list[str] = []
    payload = _load(repo_root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_MAP_KEYS:
        return _result((OCP024_ACCEPTANCE_MAP_INVALID,))
    digest = hashlib.sha256(
        yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode("utf-8")
    ).hexdigest()
    if (
        digest != MAP_SHA256
        or
        payload.get("schema_version") != 2
        or payload.get("rule_owner") != "AD-049"
        or payload.get("current_projection_owner") != "AD-054"
        or payload.get("baseline") != BASELINE
        or set(payload.get("forbidden_outcomes") or ()) != FORBIDDEN_OUTCOMES
        or len(payload.get("forbidden_outcomes") or ()) != len(FORBIDDEN_OUTCOMES)
        or ACTIVATION_FIELDS != frozenset({"activation_state", "activation_baseline_ref", "production_context_ref"})
    ):
        errors.append(OCP024_ACCEPTANCE_MAP_INVALID)

    gate = payload.get("gate_first", {})
    criterion = payload.get("readiness_criterion", {})
    if (
        gate != {
            "route": "Route-D", "positive_capable": False, "ocp016_g4_applies": False,
            "reason": "lifecycle-admission-of-non-activated-synthetic-recognition-contract",
            "changes_other_document_g4_answer": False,
        }
        or criterion.get("declared_before_application") is not True
        or criterion.get("result") != "satisfied"
        or len(criterion.get("conditions") or ()) != 7
        or criterion.get("useful_subject") != "synthetic-reference-conformance-and-fail-safe-rejection"
    ):
        errors.append(OCP024_ACCEPTANCE_MAP_INVALID)

    subject = _frontmatter(repo_root / SUBJECT_PATH)
    subject_claim = payload.get("subject", {})
    if (
        subject is None
        or subject.get("Document-ID") != "OCP-024"
        or str(subject.get("Version")) != "0.2.0"
        or subject.get("Status") != "Accepted"
        or subject_claim.get("after") != {"version": "0.2.0", "status": "Accepted"}
        or subject_claim.get("before") != {"version": "0.1.0", "status": "Draft"}
        or subject_claim.get("semantic_delta") != "none"
    ):
        errors.append(OCP024_ACCEPTANCE_SUBJECT_DRIFT)

    snapshot = payload.get("reviewed_snapshot", {})
    snapshot_map = _load(repo_root / SNAPSHOT_MAP_PATH)
    entries = {
        item.get("document_id"): item for item in (snapshot_map or {}).get("entries", [])
        if isinstance(item, dict)
    }
    expected_entry = {
        "document_id": "OCP-024", "primary": SUBJECT_PATH.as_posix(), "current_status": "Accepted",
        "reviewed_version": "0.1.0", "snapshot": SNAPSHOT_PATH.as_posix(),
        "sha256": SNAPSHOT_SHA256, "basis": "current-accepted",
    }
    if (
        snapshot != {
            "path": SNAPSHOT_PATH.as_posix(), "reviewed_version": "0.1.0",
            "sha256": SNAPSHOT_SHA256, "baseline_blob": SNAPSHOT_BLOB,
            "basis": "current-accepted",
        }
        or _hash(repo_root / SNAPSHOT_PATH) != SNAPSHOT_SHA256
        or not _body(repo_root / SUBJECT_PATH).startswith(_body(repo_root / SNAPSHOT_PATH))
        or entries.get("OCP-024") != expected_entry
    ):
        errors.append(OCP024_ACCEPTANCE_SNAPSHOT_DRIFT)

    if payload.get("document_status_projection") != _status_projection(repo_root):
        errors.append(OCP024_ACCEPTANCE_STATUS_DRIFT)

    need = _load(repo_root / NEED_MAP_PATH)
    projection = payload.get("consumer_need_projection", {})
    current_needs = tuple((need or {}).get("current_result", {}).get("unmet_positive_needs", []))
    if (
        projection.get("documents_depending_on_ocp024") != _ocp024_dependents(repo_root)
        or set(projection.get("accepted_ocp005_consumers") or ()) != ACCEPTED_CONSUMERS
        or _accepted_consumers(repo_root, "OCP-005") != ACCEPTED_CONSUMERS
        or tuple(projection.get("unmet_positive_needs") or ()) != UNMET_NEEDS
        or current_needs != UNMET_NEEDS
        or projection.get("ocp024_real_evaluator_disposition") != "deferred-outside-synthetic-obligation"
    ):
        errors.append(OCP024_ACCEPTANCE_CONSUMER_NEED_DRIFT)

    boundary = payload.get("runtime_boundary", {})
    fixture_record = _load(repo_root / VALID_FIXTURE)
    fixture = fixture_record.get("dataset", {}) if isinstance(fixture_record, dict) else {}
    derived = derive_completeness_evidence_recognition(fixture)
    if (
        derived.result != REFERENCE_RESULT
        or boundary.get("accepted_result") != REFERENCE_RESULT
        or boundary.get("invalid_result") != INDETERMINATE
        or any(boundary.get(key) is not False for key in (
            "production_shaped_values_are_recognized", "activation_fields_are_recognized",
            "establishes_completeness", "permits_ocp023_occupied_false",
            "is_completeness_provider", "is_g4_binding",
        ))
    ):
        errors.append(OCP024_ACCEPTANCE_RUNTIME_BOUNDARY_DRIFT)
    try:
        fixture["evaluator_profiles"][0]
        fixture["recognition_request"]
    except (KeyError, IndexError, TypeError):
        errors.append(OCP024_ACCEPTANCE_RUNTIME_BOUNDARY_DRIFT)
    else:
        for field, replacement in (("evaluator_ref", "PRODUCTION-EVALUATOR-001"), ("authority_basis_ref", "PRODUCTION-AUTHORITY-001")):
            mutated = copy.deepcopy(fixture)
            mutated["evaluator_profiles"][0][field] = replacement
            if (
                derive_completeness_evidence_recognition(mutated).result != INDETERMINATE
                or validate_completeness_evaluator_dataset(mutated).valid
            ):
                errors.append(OCP024_ACCEPTANCE_RUNTIME_BOUNDARY_DRIFT)
        for field in ACTIVATION_FIELDS:
            mutated = copy.deepcopy(fixture)
            mutated["recognition_request"][field] = "synthetic-disabled"
            if (
                derive_completeness_evidence_recognition(mutated).result != INDETERMINATE
                or validate_completeness_evaluator_dataset(mutated).valid
            ):
                errors.append(OCP024_ACCEPTANCE_RUNTIME_BOUNDARY_DRIFT)
    zero_record = _load(repo_root / ZERO_OCCUPANCY_FIXTURE)
    zero = zero_record.get("dataset", {}) if isinstance(zero_record, dict) else {}
    without_completeness = copy.deepcopy(zero)
    try:
        without_completeness["assignment_snapshots"][0]["completeness_evidence_ref"] = None
    except (KeyError, IndexError, TypeError):
        errors.append(OCP024_ACCEPTANCE_RUNTIME_BOUNDARY_DRIFT)
    else:
        if derive_resource_occupancy(without_completeness).occupied is not None:
            errors.append(OCP024_ACCEPTANCE_RUNTIME_BOUNDARY_DRIFT)

    protected = payload.get("protected_artifacts", [])
    if not isinstance(protected, list) or len(protected) != 11:
        errors.append(OCP024_ACCEPTANCE_PROTECTED_DRIFT)
    else:
        for item in protected:
            original = Path(str(item.get("path"))) if isinstance(item, dict) else Path("")
            resolved = historical_path(repo_root, original, str(item.get("sha256", ""))) if isinstance(item, dict) else original
            if not isinstance(item, dict) or set(item) != {"path", "sha256"} or _hash(repo_root / resolved) != item.get("sha256"):
                errors.append(OCP024_ACCEPTANCE_PROTECTED_DRIFT)
                break

    live_gate = _load(repo_root / GATE_PATH)
    guard = payload.get("promotion_gate_guard", {})
    cycle = (live_gate or {}).get("cycle_protocol", {})
    completed = [
        item.get("cycle_id") for item in (live_gate or {}).get("cycles", [])
        if isinstance(item, dict)
        and all(state == "completed" for state in (item.get("steps") or {}).values())
    ]
    if (
        set(guard or {}) != {"schema_version", "completed_cycle_ids", "active_cycle_id"}
        or not promotion_gate_guard_is_current(live_gate, guard)
    ):
        errors.append(OCP024_ACCEPTANCE_GATE_DRIFT)
    return _result(errors)
