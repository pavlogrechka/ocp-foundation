from __future__ import annotations

import copy
from dataclasses import dataclass
import hashlib
from pathlib import Path
from typing import Any, Iterable

import yaml

from .historical_evidence import historical_path

from .checker import load_fixture, validate_assignment


ASSIGNMENT_Q2_SUFFICIENCY_MAP_INVALID = "ASSIGNMENT_Q2_SUFFICIENCY_MAP_INVALID"
ASSIGNMENT_Q2_SUFFICIENCY_SUBJECT_DRIFT = "ASSIGNMENT_Q2_SUFFICIENCY_SUBJECT_DRIFT"
ASSIGNMENT_Q2_SUFFICIENCY_EVIDENCE_DRIFT = "ASSIGNMENT_Q2_SUFFICIENCY_EVIDENCE_DRIFT"
ASSIGNMENT_Q2_SUFFICIENCY_PROJECTION_DRIFT = "ASSIGNMENT_Q2_SUFFICIENCY_PROJECTION_DRIFT"
ASSIGNMENT_Q2_SUFFICIENCY_PROBE_DRIFT = "ASSIGNMENT_Q2_SUFFICIENCY_PROBE_DRIFT"
ASSIGNMENT_Q2_SUFFICIENCY_PROTECTED_DRIFT = "ASSIGNMENT_Q2_SUFFICIENCY_PROTECTED_DRIFT"
ASSIGNMENT_Q2_SUFFICIENCY_GATE_DRIFT = "ASSIGNMENT_Q2_SUFFICIENCY_GATE_DRIFT"

MAP_PATH = Path("architecture/assignment-q2-sufficiency.yaml")
SUBJECT_PATH = Path("docs/005-assignment-concept/README.md")
SURFACE_PATH = Path("architecture/assignment-stable-surface.yaml")
PRESSURE_PATH = Path("architecture/assignment-consumer-pressure.yaml")
NORM_PATH = Path("architecture/assignment-norm-compatibility.yaml")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
PROBE_FIXTURE = Path("tools/ontology_checker/fixtures/assignment/valid-established.yaml")

BASELINE = "4586bccbdc943c6a92daf052ce3df915d41fb976"
MAP_SHA256 = "f519447c04752af0b1ef2e72b59e68374ddd845706cdc01acbb4cb6b45ac3a04"
SUBJECT_SHA256 = "de84c9dafdb6126ff68a3a33218a344ddc250cf1a28e63c91407fd416e7e161b"
Q2_TOKEN = "Яка amendment model потрібна для зміни role або applicability після Establishment?"

OPEN_QUESTION_TOKENS = {
    "Q2": Q2_TOKEN,
    "Q4": "Чи потрібна окрема Role Taxonomy у Core?",
    "Q5": "Чи повинен Assignment мати окремий scope для частини складеного Resource",
    "Q7": "Чи потрібен окремий тип Assignment для coordination, approval або observation roles?",
    "Q8": "Як Constraint визначає конфлікт одночасних Assignment?",
    "Q9": "Чи може один Assignment мати кілька неперервних applicability intervals",
    "Q10": "Які provenance types повинні бути канонічними",
    "Q11": "Яка replacement policy визначає допустимі overlap і gap",
}
RESOLVED_QUESTION_TOKENS = {
    "Q1": "Чи потрібен окремий фундаментальний Concept `Reservation`",
    "Q3": "Чи допускається ретроактивне Establishment Assignment?",
    "Q6": "Як представляти кількість Consumable Resource, зарезервовану або спожиту в Operation?",
}
EXPECTED_Q2_CLASSES = {
    "SUPERSEDING_ASSIGNMENT_FOR_CHANGE": {
        "pressure_effect": "current-three-bindings-adequate",
        "norm_classification": "underdetermined",
        "norm_underdetermined_axes": ("post_establishment_change_model",),
    },
    "POST_ESTABLISHMENT_IMMUTABILITY": {
        "pressure_effect": "current-three-bindings-adequate",
        "norm_classification": "underdetermined",
        "norm_underdetermined_axes": ("post_establishment_change_model",),
    },
}
EXPECTED_PROTECTED_HASHES = {
    "docs/005-assignment-concept/README.md": SUBJECT_SHA256,
    "architecture/assignment-amendment-q2-attempt.yaml": "05792d9211c7520604101f8d3e7655377805bb89e8bb6b6e9600da388c608299",
    "architecture/assignment-consumer-pressure.yaml": "d20f8b8330b4efdb6a23c09aa6f02b2182182ddd022486c370b11afb1d8f61b2",
    "architecture/assignment-norm-compatibility.yaml": "6e32c5ed98df564c4cf23b1791bff86a80772ecd6be2135ab786d924ac4066dd",
    "architecture/assignment-stable-surface.yaml": "cd093bd36ab29a203ad56ccded32baee671989be768b7ad415f65850e2b6d3d9",
    "architecture/assignment-retroactivity-q3-resolution.yaml": "aa6b8fc70d320ad5a5c920dcd46379fb3119cfbfab938ba58600747cd0482d7a",
    "architecture/assignment-q9-sufficiency.yaml": "773ebb1d147850d4eec317f9ef544662b1dcf2688f53c590742eeece1d7889ef",
    "architecture/discovery/AD-038-assignment-amendment-q2-attempt.md": "3e9311901a261bb297c13c93616f3c65421757e6a8468ef013875106a22df1c9",
    "architecture/discovery/AD-044-assignment-consumer-pressure.md": "078a615572c864478929f9abfef7ae1ee287ebe1cca4919a010fb375d8676a6e",
    "architecture/discovery/AD-045-assignment-norm-compatibility.md": "7a1c25d22bdf3179ff552dc1635ded320a6220ec6a205da091c26188bd590020",
    "architecture/discovery/AD-046-assignment-q3-lifecycle.md": "1732397cc866a68d93b80530b17975f9eb58e26acd0aa0cf0817a7b99c0021ac",
    "architecture/discovery/AD-047-assignment-q9-sufficiency.md": "55c7cd4b8846710a8f86364d99cd29a9197b734a2432b8e9f50ea5180bed9ef7",
    "architecture/foundation-promotion-gate.yaml": "ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd",
}
EXPECTED_MAP_KEYS = frozenset(
    {
        "schema_version", "rule_owner", "baseline", "baseline_evidence_objects",
        "gate_first", "sufficiency_criterion", "argument_type_policy", "calibration",
        "evidence_ledger", "executable_probe", "surviving_q2_classes",
        "accepted_consumer_ids", "decision", "subject_preservation", "current_projection",
        "versioning", "migration", "protected_artifacts", "promotion_gate_guard",
        "forbidden_outcomes",
    }
)
EXPECTED_FORBIDDEN_OUTCOMES = frozenset(
    {
        "Q2_CLOSURE", "ANY_OTHER_QUESTION_CLOSURE", "AMENDMENT_BLOCKER_REMOVAL",
        "OCP005_CHANGE", "OCP005_STATUS_CHANGE", "ASSIGNMENT_CONCEPT_STATUS_CHANGE",
        "ASSIGNMENT_READINESS_CHANGE", "PROMOTION_CANDIDATE_SET_CHANGE",
        "POSITIVE_MODEL_ACTIVATION", "ASSIGNMENT_SELECTION", "PROMOTION_CYCLE_START",
        "T7_OPEN", "NEXT_ACT_AUTHORIZATION",
    }
)


@dataclass(frozen=True)
class AssignmentQ2SufficiencyResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentQ2SufficiencyResult:
    return AssignmentQ2SufficiencyResult(tuple(dict.fromkeys(errors)))


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


def _frontmatter(text: str) -> dict[str, Any] | None:
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


def _question_lines(text: str) -> list[str]:
    lines = text.splitlines()
    try:
        start = lines.index("## 19. Open Questions and Resolved Boundaries") + 1
        end = lines.index("## 20. Deferred Decisions", start)
    except ValueError:
        return []
    return lines[start:end]


def _one_line(lines: list[str], token: str) -> str:
    found = [line for line in lines if token in line]
    return found[0] if len(found) == 1 else ""


def validate_assignment_q2_sufficiency(repo_root: Path) -> AssignmentQ2SufficiencyResult:
    errors: list[str] = []
    payload = _load(repo_root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_MAP_KEYS:
        return _result((ASSIGNMENT_Q2_SUFFICIENCY_MAP_INVALID,))

    digest = hashlib.sha256(
        yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode("utf-8")
    ).hexdigest()
    if (
        digest != MAP_SHA256
        or payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-048"
        or payload.get("baseline") != BASELINE
        or set(payload.get("forbidden_outcomes") or ()) != EXPECTED_FORBIDDEN_OUTCOMES
        or len(payload.get("forbidden_outcomes") or ()) != len(EXPECTED_FORBIDDEN_OUTCOMES)
    ):
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_MAP_INVALID)

    criterion = payload.get("sufficiency_criterion", {})
    policy = payload.get("argument_type_policy", {})
    decision = payload.get("decision", {})
    gate = payload.get("gate_first", {})
    if (
        criterion.get("declared_before_application") is not True
        or criterion.get("result") != "insufficient-for-q2-closure"
        or set(policy) != {"direct_normative_statement", "enumeration_inference", "silence_inference"}
        or any(item.get("current_sufficient_alone") is not False for item in policy.values())
        or decision.get("question_id") != "Q2"
        or decision.get("disposition") != "remains-open-insufficient-evidence"
        or decision.get("criterion_satisfied") is not False
        or decision.get("closure_authorized_by_this_outcome") is not False
        or decision.get("subject_changed") is not False
        or decision.get("amendment_blocker_removed") is not False
        or gate.get("evidence_form", {}).get("applies") is not False
        or gate.get("evidence_form", {}).get("positive_capable") is not False
        or gate.get("hypothetical_closures", {}).get("SUPERSEDING_ASSIGNMENT_FOR_CHANGE", {}).get("applies") is not True
        or gate.get("hypothetical_closures", {}).get("POST_ESTABLISHMENT_IMMUTABILITY", {}).get("applies") is not False
    ):
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_EVIDENCE_DRIFT)

    historical_subject = historical_path(repo_root, SUBJECT_PATH, SUBJECT_SHA256)
    try:
        subject_text = (repo_root / historical_subject).read_text(encoding="utf-8")
        current_text = (repo_root / SUBJECT_PATH).read_text(encoding="utf-8")
    except OSError:
        subject_text = ""
        current_text = ""
    metadata = _frontmatter(subject_text)
    current_metadata = _frontmatter(current_text)
    lines = _question_lines(current_text)
    if (
        _hash(repo_root / historical_subject) != SUBJECT_SHA256
        or metadata is None
        or metadata.get("Document-ID") != "OCP-005"
        or str(metadata.get("Version")) != "0.3.0"
        or metadata.get("Status") != "Draft"
        or metadata.get("Concept-Status") != "Accepted"
        or payload.get("subject_preservation", {}).get("sha256") != SUBJECT_SHA256
        or payload.get("subject_preservation", {}).get("version_class") != "no-subject-change"
        or current_metadata is None
        or str(current_metadata.get("Version")) != "0.4.0"
        or current_metadata.get("Status") != "Accepted"
    ):
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_SUBJECT_DRIFT)
    if set(OPEN_QUESTION_TOKENS) != {"Q2", "Q4", "Q5", "Q7", "Q8", "Q9", "Q10", "Q11"}:
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_PROJECTION_DRIFT)
    for token in OPEN_QUESTION_TOKENS.values():
        line = _one_line(lines, token)
        if not line or "~~" in line:
            errors.append(ASSIGNMENT_Q2_SUFFICIENCY_PROJECTION_DRIFT)
            break
    if OPEN_QUESTION_TOKENS.get("Q2") != Q2_TOKEN or set(RESOLVED_QUESTION_TOKENS) != {"Q1", "Q3", "Q6"}:
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_PROJECTION_DRIFT)
    for token in RESOLVED_QUESTION_TOKENS.values():
        line = _one_line(lines, token)
        if not line or "~~" not in line:
            errors.append(ASSIGNMENT_Q2_SUFFICIENCY_PROJECTION_DRIFT)
            break

    surface = _load(repo_root / SURFACE_PATH)
    questions = {
        item.get("question_id"): (item.get("state"), item.get("classification"))
        for item in surface.get("open_question_inventory", [])
        if isinstance(item, dict)
    } if isinstance(surface, dict) else {}
    moving = {
        item.get("surface_id"): item.get("question_ids")
        for item in surface.get("moving_surfaces", [])
        if isinstance(item, dict)
    } if isinstance(surface, dict) else {}
    blockers = {
        item.get("blocker_id"): item.get("question_ids")
        for item in surface.get("blockers", [])
        if isinstance(item, dict)
    } if isinstance(surface, dict) else {}
    subject = surface.get("subject", {}) if isinstance(surface, dict) else {}
    expected_projection = {
        "q2_state": "open", "q5_state": "open", "q9_state": "open",
        "amendment_moving_surface_question_ids": ["Q2"],
        "blockers": {
            "AMENDMENT_MODEL_ABSENT": ["Q2"],
            "TEMPORAL_MODEL_UNRESOLVED": ["Q9"],
            "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": ["Q5"],
        },
        "assignment_discovery_result": "bounded_stable_candidate_not_selected",
        "whole_document_freeze_reachable": False,
        "promotion_candidate_ids": ["OCP-005", "OCP-006", "OCP-010"],
    }
    if (
        questions.get("Q2") != ("open", "blocks-whole-document-freeze")
        or questions.get("Q5") != ("open", "blocks-whole-document-freeze")
        or questions.get("Q9") != ("open", "blocks-whole-document-freeze")
        or moving.get("AMENDMENT_AFTER_ESTABLISHMENT") != ["Q2"]
        or blockers != expected_projection["blockers"]
        or subject.get("discovery_result") != "bounded_stable_candidate_not_selected"
        or str(subject.get("expected_version")) != "0.4.0"
        or subject.get("expected_status") != "Accepted"
        or subject.get("expected_concept_status") != "Accepted"
        or payload.get("current_projection") != expected_projection
    ):
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_PROJECTION_DRIFT)

    declared_classes = {
        item.get("resolution_id"): {
            "pressure_effect": item.get("pressure_effect"),
            "norm_classification": item.get("norm_classification"),
            "norm_underdetermined_axes": tuple(item.get("norm_underdetermined_axes") or ()),
        }
        for item in payload.get("surviving_q2_classes", []) if isinstance(item, dict)
    }
    pressure = _load(repo_root / PRESSURE_PATH)
    pressure_rows = {
        item.get("resolution_id"): item for item in pressure.get("resolution_inventory", [])
        if isinstance(item, dict)
    } if isinstance(pressure, dict) else {}
    norm = _load(repo_root / NORM_PATH)
    norm_rows = {
        item.get("resolution_id"): item for item in norm.get("survivor_results", [])
        if isinstance(item, dict)
    } if isinstance(norm, dict) else {}
    if declared_classes != EXPECTED_Q2_CLASSES:
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_EVIDENCE_DRIFT)
    for resolution_id, expected in EXPECTED_Q2_CLASSES.items():
        if (
            pressure_rows.get(resolution_id, {}).get("need_adequacy_effect") != expected["pressure_effect"]
            or norm_rows.get(resolution_id, {}).get("classification") != expected["norm_classification"]
            or tuple(norm_rows.get(resolution_id, {}).get("underdetermined_axes") or ()) != expected["norm_underdetermined_axes"]
            or norm_rows.get(resolution_id, {}).get("violation_statement_ids") != []
        ):
            errors.append(ASSIGNMENT_Q2_SUFFICIENCY_EVIDENCE_DRIFT)
            break

    evidence = payload.get("evidence_ledger")
    anchors = payload.get("baseline_evidence_objects")
    if (
        not isinstance(anchors, list) or len(anchors) != 19
        or len({item.get("path") for item in anchors if isinstance(item, dict)}) != 19
        or any(set(item) != {"path", "blob", "sha256", "state_tokens"} or not all(item.values()) for item in anchors if isinstance(item, dict))
        or len([item for item in anchors if isinstance(item, dict)]) != 19
        or not isinstance(evidence, list) or len(evidence) != 10
        or {item.get("evidence_mode") for item in evidence if isinstance(item, dict)} != {"analytic", "observed"}
        or any(not item.get("proves") or not item.get("does_not_prove") for item in evidence if isinstance(item, dict))
        or payload.get("accepted_consumer_ids") != ["OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021", "OCP-023"]
    ):
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_EVIDENCE_DRIFT)

    probe = payload.get("executable_probe", {})
    try:
        original = load_fixture(repo_root / PROBE_FIXTURE)["entity"]
    except (OSError, ValueError, KeyError, yaml.YAMLError):
        original = None
    if not isinstance(original, dict):
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_PROBE_DRIFT)
    else:
        role_changed = copy.deepcopy(original)
        role_changed["role_specification"]["role_code"] = probe.get("role_change", {}).get("replacement_value")
        applicability_changed = copy.deepcopy(original)
        applicability_changed["applicability_end"] = probe.get("applicability_change", {}).get("replacement_value")
        invalid = copy.deepcopy(original)
        invalid["role_specification"]["role_code"] = probe.get("rejection_control", {}).get("replacement_value")
        invalid_result = validate_assignment(invalid)
        if (
            probe.get("fixture") != str(PROBE_FIXTURE)
            or probe.get("unchanged_fields") != ["assignment_id", "transition_history", "provenance_ref", "supersedes_assignment_ref"]
            or probe.get("result") != "validator-does-not-discriminate-q2-survivors"
            or validate_assignment(original).valid is not True
            or validate_assignment(role_changed).valid is not True
            or validate_assignment(applicability_changed).valid is not True
            or invalid_result.valid is not False
            or probe.get("rejection_control", {}).get("expected_error") not in invalid_result.errors
        ):
            errors.append(ASSIGNMENT_Q2_SUFFICIENCY_PROBE_DRIFT)

    declared_hashes = {
        item.get("path"): item.get("sha256") for item in payload.get("protected_artifacts", [])
        if isinstance(item, dict)
    }
    if declared_hashes != EXPECTED_PROTECTED_HASHES or any(
        _hash(repo_root / historical_path(repo_root, Path(path), digest)) != digest
        for path, digest in EXPECTED_PROTECTED_HASHES.items()
    ):
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_PROTECTED_DRIFT)

    promotion = _load(repo_root / GATE_PATH)
    protocol = promotion.get("cycle_protocol") if isinstance(promotion, dict) else None
    cycles = promotion.get("cycles") if isinstance(promotion, dict) else None
    candidates = promotion.get("candidates") if isinstance(promotion, dict) else None
    completed = [
        item.get("cycle_id") for item in cycles if isinstance(item, dict)
        and isinstance(item.get("steps"), dict) and set(item["steps"].values()) == {"completed"}
    ] if isinstance(cycles, list) else []
    candidate_ids = [item.get("document_id") for item in candidates if isinstance(item, dict)] if isinstance(candidates, list) else []
    assignment = next((item for item in candidates if item.get("document_id") == "OCP-005"), {}) if isinstance(candidates, list) else {}
    if (
        not isinstance(promotion, dict) or promotion.get("schema_version") != 5
        or not isinstance(protocol, dict) or protocol.get("active_cycle_id") is not None
        or completed != ["EVENT_T6"] or candidate_ids != ["OCP-005", "OCP-006", "OCP-010"]
        or assignment.get("expected_document_status") != "Accepted"
        or assignment.get("expected_concept_status") != "Accepted"
        or payload.get("promotion_gate_guard") != {
            "schema_version": 5, "completed_cycle_ids": ["EVENT_T6"], "active_cycle_id": None
        }
    ):
        errors.append(ASSIGNMENT_Q2_SUFFICIENCY_GATE_DRIFT)

    return _result(errors)
