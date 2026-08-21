from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile
from typing import Any, Iterable

import yaml

from .foundation_promotion_gate import (
    assignment_selection_prefix_is_current,
    promotion_gate_guard_is_current,
    validate_foundation_promotion_gate,
)


ASSIGNMENT_SELECTION_MAP_INVALID = "ASSIGNMENT_SELECTION_MAP_INVALID"
ASSIGNMENT_SELECTION_AUTHORITY_DRIFT = "ASSIGNMENT_SELECTION_AUTHORITY_DRIFT"
ASSIGNMENT_SELECTION_CANDIDATE_DRIFT = "ASSIGNMENT_SELECTION_CANDIDATE_DRIFT"
ASSIGNMENT_SELECTION_GATE_DRIFT = "ASSIGNMENT_SELECTION_GATE_DRIFT"
ASSIGNMENT_SELECTION_CLOSABILITY_DRIFT = "ASSIGNMENT_SELECTION_CLOSABILITY_DRIFT"
ASSIGNMENT_SELECTION_PROJECTION_DRIFT = "ASSIGNMENT_SELECTION_PROJECTION_DRIFT"
ASSIGNMENT_SELECTION_HISTORICAL_DRIFT = "ASSIGNMENT_SELECTION_HISTORICAL_DRIFT"
ASSIGNMENT_SELECTION_BOUNDARY_DRIFT = "ASSIGNMENT_SELECTION_BOUNDARY_DRIFT"
ASSIGNMENT_SELECTION_ANCHOR_DRIFT = "ASSIGNMENT_SELECTION_ANCHOR_DRIFT"

MAP_PATH = Path("architecture/assignment-promotion-selection.yaml")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
READINESS_PATH = Path("architecture/assignment-canonical-readiness.yaml")
NEED_PATH = Path("architecture/consumer-need-discovery.yaml")
BASELINE = "779aaf4c5d2799c8410a6934d28230c12b2ff31e"
MAP_SHA256 = "87f8a57c3a5916ee0a580e078e4d2dc32f515fc306096ed878a1cb9edd27dc29"

CANDIDATE_IDS = ("OCP-005", "OCP-006", "OCP-010")
LIVE_CARRIERS = (
    "architecture/assignment-amendment-q2-attempt.yaml",
    "architecture/assignment-canonical-readiness.yaml",
    "architecture/assignment-consumer-compatibility.yaml",
    "architecture/assignment-consumer-pressure.yaml",
    "architecture/assignment-document-acceptance.yaml",
    "architecture/assignment-norm-compatibility.yaml",
    "architecture/assignment-q2-sufficiency.yaml",
    "architecture/assignment-q9-sufficiency.yaml",
    "architecture/assignment-retroactivity-q3-resolution.yaml",
    "architecture/assignment-stable-surface.yaml",
    "architecture/assignment-temporal-scope-attempt.yaml",
    "architecture/constraint-document-acceptance.yaml",
    "architecture/constraint-stable-surface.yaml",
    "architecture/consumer-need-discovery.yaml",
    "architecture/ocp024-acceptance.yaml",
)
LIVE_READERS = (
    "assignment-stable-surface", "constraint-stable-surface",
    "constraint-q6-sufficiency", "constraint-document-status-readiness",
    "assignment-amendment-q2", "assignment-temporal-scope",
    "assignment-consumer-compatibility", "assignment-consumer-pressure",
    "assignment-norm-compatibility", "assignment-q3-lifecycle",
    "assignment-q2-sufficiency", "assignment-q9-sufficiency",
    "consumer-need-discovery", "ocp024-acceptance",
    "constraint-document-acceptance", "assignment-document-acceptance",
    "assignment-canonical-readiness",
)
NON_IMPLICATIONS = frozenset({
    "NO_DOCUMENT_PROMOTION", "NO_CONCEPT_CANONICALIZATION",
    "NO_OTHER_DOCUMENT_OR_CONCEPT_PROMOTION", "NO_QUESTION_CLOSURE",
    "NO_POSITIVE_MODEL_ACTIVATION", "NO_UNMET_NEED_SATISFACTION",
    "NO_NEXT_STEP_AUTHORIZATION", "NO_DOCUMENT_STATUS_OR_VERSION_CHANGE",
    "NO_CONCEPT_STATUS_CHANGE",
})
EXPECTED_KEYS = frozenset({
    "schema_version", "rule_owner", "baseline", "gate_first", "authority",
    "candidate_inventory", "selection", "closability", "live_projection_inventory",
    "historical_evidence_successions", "protected_current_state", "atomic_package",
    "non_implications", "versioning", "migration", "baseline_evidence_objects",
})


@dataclass(frozen=True)
class AssignmentPromotionSelectionResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentPromotionSelectionResult:
    return AssignmentPromotionSelectionResult(tuple(dict.fromkeys(errors)))


def _load(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None


def _frontmatter_text(text: str) -> dict[str, Any] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    try:
        loaded = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return loaded if isinstance(loaded, dict) else None


def _frontmatter(path: Path) -> dict[str, Any] | None:
    try:
        return _frontmatter_text(path.read_text(encoding="utf-8"))
    except OSError:
        return None


def _baseline_object(root: Path, path: str) -> tuple[str, bytes] | None:
    try:
        line = subprocess.check_output(
            ["git", "ls-tree", "-r", BASELINE, "--", path], cwd=root,
            text=True, stderr=subprocess.DEVNULL,
        ).strip()
        metadata, resolved = line.split("\t", 1)
        if resolved != path:
            return None
        blob = metadata.split()[2]
        raw = subprocess.check_output(
            ["git", "cat-file", "blob", blob], cwd=root, stderr=subprocess.DEVNULL,
        )
        return blob, raw
    except (OSError, subprocess.CalledProcessError, ValueError, IndexError):
        return None


def _active_cycle_values(value: Any) -> tuple[Any, ...]:
    found: list[Any] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "active_cycle_id":
                found.append(child)
            else:
                found.extend(_active_cycle_values(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(_active_cycle_values(child))
    return tuple(found)


def _gate_guards(value: Any) -> tuple[dict[str, Any], ...]:
    found: list[dict[str, Any]] = []
    if isinstance(value, dict):
        if {"schema_version", "completed_cycle_ids", "active_cycle_id"}.issubset(value):
            found.append(value)
        for child in value.values():
            found.extend(_gate_guards(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(_gate_guards(child))
    return tuple(found)


def rollback_gate_probe(root: Path) -> bool:
    predecessor = root / "architecture/baselines/foundation-promotion-gate-pre-assignment-cycle-selection.yaml"
    try:
        with tempfile.TemporaryDirectory() as tmp:
            probe = Path(tmp)
            for source in (root / "docs").glob("[0-9][0-9][0-9]-*/README.md"):
                target = probe / source.relative_to(root)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
            target = probe / GATE_PATH
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(predecessor, target)
            return validate_foundation_promotion_gate(probe).valid
    except OSError:
        return False


def _current_documents(root: Path) -> dict[str, tuple[str, str, str | None]]:
    values: dict[str, tuple[str, str, str | None]] = {}
    for path in sorted((root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(path)
        if not metadata or not isinstance(metadata.get("Document-ID"), str):
            continue
        values[str(metadata["Document-ID"])] = (
            str(metadata.get("Version")), str(metadata.get("Status")),
            str(metadata.get("Concept-Status")) if metadata.get("Concept-Status") is not None else None,
        )
    return values


def _baseline_documents(root: Path, current: dict[str, tuple[str, str, str | None]]) -> dict[str, tuple[str, str, str | None]]:
    values: dict[str, tuple[str, str, str | None]] = {}
    tree_paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", BASELINE], cwd=root,
        text=True, stderr=subprocess.DEVNULL,
    ).splitlines()
    for document_id in current:
        number = document_id.split("-", 1)[1]
        paths = [
            path for path in tree_paths
            if path.startswith(f"docs/{number}-") and path.endswith("/README.md")
        ]
        if len(paths) != 1:
            continue
        resolved = _baseline_object(root, paths[0])
        if resolved is None:
            continue
        metadata = _frontmatter_text(resolved[1].decode("utf-8")) or {}
        values[document_id] = (
            str(metadata.get("Version")), str(metadata.get("Status")),
            str(metadata.get("Concept-Status")) if metadata.get("Concept-Status") is not None else None,
        )
    return values


def validate_assignment_promotion_selection(root: Path) -> AssignmentPromotionSelectionResult:
    errors: list[str] = []
    payload = _load(root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_KEYS:
        return _result((ASSIGNMENT_SELECTION_MAP_INVALID,))
    digest = hashlib.sha256(yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode()).hexdigest()
    if payload.get("schema_version") != 1 or payload.get("rule_owner") != "AD-056" or payload.get("baseline") != BASELINE or digest != MAP_SHA256:
        return _result((ASSIGNMENT_SELECTION_MAP_INVALID,))

    if payload.get("gate_first") != {
        "subject_route": "Route-F", "operation": "governance-lifecycle-selection",
        "positive_capable": False, "ocp016_g4_applies": False,
        "activation_performed": False,
        "reason": "selection-opens-a-governance-cycle-without-adding-or-activating-an-operational-rule-result-or-profile",
    } or payload.get("authority") != {
        "owner": "Architecture Board", "decision": "select-OCP-005-for-canonicalization",
        "authorized_step": "CANDIDATE_BOARD_SELECTION",
        "unauthorized_steps": ["DOCUMENT_PROMOTION", "CONCEPT_CANONICALIZATION"],
    }:
        errors.append(ASSIGNMENT_SELECTION_AUTHORITY_DRIFT)

    gate = _load(root / GATE_PATH)
    candidates = {row.get("document_id"): row for row in (gate or {}).get("candidates", []) if isinstance(row, dict)}
    cycles = {row.get("candidate_id"): row for row in (gate or {}).get("cycles", []) if isinstance(row, dict)}
    baseline_gate_object = _baseline_object(root, GATE_PATH.as_posix())
    try:
        baseline_gate = yaml.safe_load(baseline_gate_object[1].decode("utf-8")) if baseline_gate_object else {}
    except (UnicodeDecodeError, yaml.YAMLError):
        baseline_gate = {}
    prior_cycles = {
        row.get("candidate_id"): row for row in (baseline_gate or {}).get("cycles", [])
        if isinstance(row, dict)
    }
    readiness = _load(root / READINESS_PATH) or {}
    expected_inventory = {
        "OCP-005": ("T6", "Accepted", "Accepted", "pass", "none", "eligible", "selected-by-explicit-Board-decision"),
        "OCP-006": ("T7", "Accepted", "Accepted", "fail", "none", "ineligible", "rejected-currently-direct-dependency-floor-L2-fails"),
        "OCP-010": ("T6", "Canonical", "Canonical", "pass", "EVENT_T6", "ineligible", "rejected-currently-candidate-already-consumed-by-completed-cycle-and-candidate-ids-are-unique"),
    }
    observed_inventory: dict[str, tuple[Any, ...]] = {}
    for row in payload.get("candidate_inventory") or ():
        if not isinstance(row, dict):
            continue
        observed_inventory[str(row.get("document_id"))] = (
            row.get("slot"), row.get("document_status"), row.get("concept_status"),
            row.get("l2_result"), row.get("prior_cycle"), row.get("eligibility"),
            row.get("disposition"),
        )
        candidate = candidates.get(row.get("document_id"), {})
        primary = root / str(candidate.get("primary", ""))
        metadata = _frontmatter(primary) or {}
        prior = prior_cycles.get(row.get("document_id"))
        actual_prior = prior.get("cycle_id") if prior else "none"
        if (
            row.get("evidence_mode") != "derived"
            or row.get("slot") != candidate.get("slot")
            or row.get("document_status") != metadata.get("Status")
            or row.get("concept_status") != metadata.get("Concept-Status")
            or row.get("l2_result") != candidate.get("expected_l2")
            or row.get("l2_blockers", []) != candidate.get("l2_blockers", [])
            or row.get("prior_cycle") != actual_prior
            or (row.get("document_id") == "OCP-005" and row.get("subject_readiness") != "satisfied-by-AD-055")
        ):
            errors.append(ASSIGNMENT_SELECTION_CANDIDATE_DRIFT)
    if observed_inventory != expected_inventory or tuple(candidates) != CANDIDATE_IDS or (readiness.get("result") or {}).get("ready_for_separate_cycle-and-canonicalization-proposal") is not True:
        errors.append(ASSIGNMENT_SELECTION_CANDIDATE_DRIFT)

    selection = payload.get("selection") or {}
    assignment_cycle = cycles.get("OCP-005", {})
    if (
        selection != {
            "eligible_candidates": ["OCP-005"], "tie_break_required": False,
            "selected_candidate": "OCP-005", "cycle_id": "ASSIGNMENT_T6", "slot": "T6",
            "slot_reuse_basis": "AD-055-executable-reuse-probe", "cycle_id_unique": True,
            "candidate_id_unique": True,
            "step_state": {"CANDIDATE_BOARD_SELECTION": "completed", "DOCUMENT_PROMOTION": "pending", "CONCEPT_CANONICALIZATION": "pending"},
            "step_evidence": {"CANDIDATE_BOARD_SELECTION": "AD-056"},
        }
        or assignment_cycle.get("cycle_id") != "ASSIGNMENT_T6"
        or not isinstance(gate, dict) or not assignment_selection_prefix_is_current(gate)
        or not validate_foundation_promotion_gate(root).valid
    ):
        errors.append(ASSIGNMENT_SELECTION_GATE_DRIFT)

    closability = payload.get("closability") or {}
    forward = closability.get("forward") or {}
    rollback = closability.get("rollback") or {}
    if (
        forward != {
            "defined": True, "ordered_remaining_steps": ["DOCUMENT_PROMOTION", "CONCEPT_CANONICALIZATION"],
            "each_requires_separate_mandate": True,
            "completion_state": "all-three-steps-completed-and-active_cycle_id-null",
            "basis": "foundation-promotion-gate-schema-5-ordered-prefix",
        }
        or rollback.get("defined") is not True
        or rollback.get("mechanism") != "new-reviewed-corrective-rollback-PR"
        or rollback.get("restores_active_cycle_id") is not None
        or rollback.get("restores_cycle_count") != 1
        or rollback.get("history_rewrite") is not False
        or rollback.get("partial_edit_permitted") is not False
        or rollback.get("basis") != "OCP-001-corrective-rollback-row"
        or set(rollback.get("atomic_unit") or ()) != {"foundation-promotion-gate", "assignment-selection-witness", "all-live-cycle-projections", "historical-successor-bindings", "checker-and-tests", "repository-accounting"}
        or closability.get("conclusion") != "cycle-is-closable-forward-or-by-reviewed-atomic-rollback"
        or not rollback_gate_probe(root)
    ):
        errors.append(ASSIGNMENT_SELECTION_CLOSABILITY_DRIFT)

    projection = payload.get("live_projection_inventory") or {}
    if tuple(projection.get("carriers") or ()) != LIVE_CARRIERS or tuple(projection.get("readers") or ()) != LIVE_READERS or projection.get("active_cycle_id") != "ASSIGNMENT_T6" or projection.get("completed_cycle_ids") != ["EVENT_T6"]:
        errors.append(ASSIGNMENT_SELECTION_PROJECTION_DRIFT)
    for relative in LIVE_CARRIERS:
        live = _load(root / relative)
        values = _active_cycle_values(live)
        guards = _gate_guards(live)
        if (
            not values or set(values) != {"ASSIGNMENT_T6"}
            or any(not promotion_gate_guard_is_current(gate, guard) for guard in guards)
        ):
            errors.append(ASSIGNMENT_SELECTION_PROJECTION_DRIFT)

    successions = payload.get("historical_evidence_successions") or []
    if len(successions) != len(LIVE_CARRIERS) + 1:
        errors.append(ASSIGNMENT_SELECTION_HISTORICAL_DRIFT)
    for row in successions:
        original = str(row.get("original_path", ""))
        preserved = Path(str(row.get("preserved_path", "")))
        baseline_object = _baseline_object(root, original)
        try:
            raw = (root / preserved).read_bytes()
        except OSError:
            raw = b""
        if (
            preserved.is_absolute() or ".." in preserved.parts
            or baseline_object is None or raw != baseline_object[1]
            or hashlib.sha256(raw).hexdigest() != row.get("sha256")
            or row.get("reason") != "live-cycle-projection-advances-without-rewriting-the-pre-selection-evidence"
        ):
            errors.append(ASSIGNMENT_SELECTION_HISTORICAL_DRIFT)

    current_documents = _current_documents(root)
    try:
        baseline_documents = _baseline_documents(root, current_documents)
    except (OSError, subprocess.CalledProcessError):
        baseline_documents = {}
    protected = payload.get("protected_current_state") or {}
    registry = (root / "docs/000-operational-ontology/README.md").read_text(encoding="utf-8")
    taxonomy = (root / "docs/002-concept-taxonomy/README.md").read_text(encoding="utf-8")
    need = _load(root / NEED_PATH) or {}
    current_need_ids = set((need.get("current_result") or {}).get("unmet_positive_needs") or ())
    atomic = payload.get("atomic_package") or {}
    migration = payload.get("migration") or {}
    if (
        current_documents != baseline_documents
        or protected.get("OCP-005") != {"version": "0.4.0", "status": "Accepted", "concept_status": "Accepted"}
        or protected.get("OCP-006") != {"version": "0.4.0", "status": "Accepted", "concept_status": "Accepted"}
        or protected.get("OCP-010") != {"version": "1.0.1", "status": "Canonical", "concept_status": "Canonical"}
        or "| Assignment | Accepted |" not in registry or "Assignment: Accepted" not in taxonomy
        or protected.get("assignment_registry_status") != "Accepted"
        or protected.get("assignment_taxonomy_status") != "Accepted"
        or current_need_ids != {"RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS"}
        or protected.get("unmet_positive_need_state") != "unmet"
        or frozenset(payload.get("non_implications") or ()) != NON_IMPLICATIONS
        or atomic.get("complete") is not True or atomic.get("partial_effect_permitted") is not False
        or set(atomic.get("required_elements") or ()) != {"active-cycle-id", "cycle-record", "selection-evidence", "live-projections", "historical-successions", "checker-and-tests", "repository-accounting"}
        or migration.get("data") != "none" or migration.get("references") != "none"
        or migration.get("schemas") != "none" or migration.get("runtime_behavior") != "unchanged"
    ):
        errors.append(ASSIGNMENT_SELECTION_BOUNDARY_DRIFT)

    try:
        tree = subprocess.check_output(["git", "ls-tree", "-r", BASELINE], cwd=root, text=True, stderr=subprocess.DEVNULL).splitlines()
        reverse: dict[str, list[str]] = {}
        for line in tree:
            metadata, path = line.split("\t", 1)
            reverse.setdefault(metadata.split()[2], []).append(path)
        for item in payload.get("baseline_evidence_objects") or ():
            raw = subprocess.check_output(["git", "cat-file", "blob", item["blob"]], cwd=root, stderr=subprocess.DEVNULL)
            if item["path"] not in reverse.get(item["blob"], []) or hashlib.sha256(raw).hexdigest() != item["sha256"] or not all(str(token) in raw.decode("utf-8") for token in item["state_tokens"]):
                errors.append(ASSIGNMENT_SELECTION_ANCHOR_DRIFT)
    except (OSError, subprocess.CalledProcessError, KeyError, ValueError, UnicodeDecodeError):
        errors.append(ASSIGNMENT_SELECTION_ANCHOR_DRIFT)
    return _result(errors)
