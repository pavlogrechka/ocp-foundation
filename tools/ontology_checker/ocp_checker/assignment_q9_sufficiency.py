from __future__ import annotations

import copy
from dataclasses import dataclass
import hashlib
from pathlib import Path
from typing import Any, Iterable

import yaml

from .historical_evidence import historical_path

from .checker import assignment_effective_at, load_fixture, validate_assignment
from .foundation_promotion_gate import promotion_gate_guard_is_current


ASSIGNMENT_Q9_MAP_INVALID = "ASSIGNMENT_Q9_MAP_INVALID"
ASSIGNMENT_Q9_SUBJECT_DRIFT = "ASSIGNMENT_Q9_SUBJECT_DRIFT"
ASSIGNMENT_Q9_EVIDENCE_DRIFT = "ASSIGNMENT_Q9_EVIDENCE_DRIFT"
ASSIGNMENT_Q9_PROJECTION_DRIFT = "ASSIGNMENT_Q9_PROJECTION_DRIFT"
ASSIGNMENT_Q9_PROBE_DRIFT = "ASSIGNMENT_Q9_PROBE_DRIFT"
ASSIGNMENT_Q9_PROTECTED_ARTIFACT_DRIFT = "ASSIGNMENT_Q9_PROTECTED_ARTIFACT_DRIFT"
ASSIGNMENT_Q9_GATE_DRIFT = "ASSIGNMENT_Q9_GATE_DRIFT"

MAP_PATH = Path("architecture/assignment-q9-sufficiency.yaml")
SUBJECT_PATH = Path("docs/005-assignment-concept/README.md")
SURFACE_PATH = Path("architecture/assignment-stable-surface.yaml")
PRESSURE_PATH = Path("architecture/assignment-consumer-pressure.yaml")
NORM_PATH = Path("architecture/assignment-norm-compatibility.yaml")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
PROBE_FIXTURE = Path("tools/ontology_checker/fixtures/assignment/valid-established.yaml")

BASELINE = "7acced16b99790db04c8dccb9380a6191633af30"
MAP_SHA256 = "1318bf67a91c1c4f8355cfeb2a1a2a3ce648b4f5521a80380552576c4f6ed23e"
SUBJECT_SHA256 = "de84c9dafdb6126ff68a3a33218a344ddc250cf1a28e63c91407fd416e7e161b"
Q9_TOKEN = "Чи може один Assignment мати кілька неперервних applicability intervals, чи кожен інтервал потребує окремого Assignment?"

OPEN_QUESTION_TOKENS = {
    "Q2": "Яка amendment model потрібна для зміни role або applicability після Establishment?",
    "Q4": "Чи потрібна окрема Role Taxonomy у Core?",
    "Q5": "Чи повинен Assignment мати окремий scope для частини складеного Resource",
    "Q7": "Чи потрібен окремий тип Assignment для coordination, approval або observation roles?",
    "Q8": "Як Constraint визначає конфлікт одночасних Assignment?",
    "Q9": Q9_TOKEN,
    "Q10": "Які provenance types повинні бути канонічними",
    "Q11": "Яка replacement policy визначає допустимі overlap і gap",
}
RESOLVED_QUESTION_TOKENS = {
    "Q1": "Чи потрібен окремий фундаментальний Concept `Reservation`",
    "Q3": "Чи допускається ретроактивне Establishment Assignment?",
    "Q6": "Як представляти кількість Consumable Resource, зарезервовану або спожиту в Operation?",
}

EXPECTED_Q9_CLASSES = {
    "PROSPECTIVE_ONLY_SINGLE_INTERVAL": {
        "pressure_need_adequacy_effect": "current-three-bindings-adequate",
        "norm_classification": "underdetermined",
        "norm_underdetermined_axes": ("interval_cardinality",),
    },
    "PROSPECTIVE_ONLY_MULTIPLE_INTERVALS": {
        "pressure_need_adequacy_effect": "current-three-bindings-adequate",
        "norm_classification": "underdetermined",
        "norm_underdetermined_axes": ("interval_cardinality",),
    },
}

EXPECTED_PROTECTED_HASHES = {
    "docs/005-assignment-concept/README.md": SUBJECT_SHA256,
    "architecture/assignment-stable-surface.yaml": "cd093bd36ab29a203ad56ccded32baee671989be768b7ad415f65850e2b6d3d9",
    "architecture/assignment-temporal-scope-attempt.yaml": "4a8899d58ddf9edcf613760d330ff0003a3f982c1d6c188c4283c52fc364f7fb",
    "architecture/assignment-consumer-pressure.yaml": "d20f8b8330b4efdb6a23c09aa6f02b2182182ddd022486c370b11afb1d8f61b2",
    "architecture/assignment-norm-compatibility.yaml": "6e32c5ed98df564c4cf23b1791bff86a80772ecd6be2135ab786d924ac4066dd",
    "architecture/assignment-retroactivity-q3-resolution.yaml": "aa6b8fc70d320ad5a5c920dcd46379fb3119cfbfab938ba58600747cd0482d7a",
    "architecture/discovery/AD-039-assignment-temporal-scope-attempt.md": "310d2c3bb36b1c788e2573d42593f113066f344be1e9ee279901b1b8f6ce68dc",
    "architecture/discovery/AD-044-assignment-consumer-pressure.md": "078a615572c864478929f9abfef7ae1ee287ebe1cca4919a010fb375d8676a6e",
    "architecture/discovery/AD-045-assignment-norm-compatibility.md": "7a1c25d22bdf3179ff552dc1635ded320a6220ec6a205da091c26188bd590020",
    "architecture/discovery/AD-046-assignment-q3-lifecycle.md": "1732397cc866a68d93b80530b17975f9eb58e26acd0aa0cf0817a7b99c0021ac",
    "architecture/foundation-promotion-gate.yaml": "ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd",
}

EXPECTED_MAP_KEYS = frozenset(
    {
        "schema_version",
        "rule_owner",
        "baseline",
        "baseline_evidence_objects",
        "gate_first",
        "sufficiency_criterion",
        "evidence_ledger",
        "executable_probe",
        "surviving_q9_classes",
        "decision",
        "subject_preservation",
        "current_projection",
        "versioning",
        "migration",
        "protected_artifacts",
        "promotion_gate_guard",
        "forbidden_outcomes",
    }
)
EXPECTED_FORBIDDEN_OUTCOMES = frozenset(
    {
        "Q9_CLOSURE",
        "ANY_OTHER_QUESTION_CLOSURE",
        "TEMPORAL_BLOCKER_REMOVAL",
        "OCP005_CHANGE",
        "OCP005_STATUS_CHANGE",
        "ASSIGNMENT_CONCEPT_STATUS_CHANGE",
        "ASSIGNMENT_READINESS_CHANGE",
        "PROMOTION_CANDIDATE_SET_CHANGE",
        "POSITIVE_MODEL_ACTIVATION",
        "ASSIGNMENT_SELECTION",
        "PROMOTION_CYCLE_START",
        "T7_OPEN",
        "NEXT_ACT_AUTHORIZATION",
    }
)


@dataclass(frozen=True)
class AssignmentQ9SufficiencyResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentQ9SufficiencyResult:
    return AssignmentQ9SufficiencyResult(tuple(dict.fromkeys(errors)))


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


def _section_lines(text: str, start: str, end: str) -> list[str]:
    lines = text.splitlines()
    try:
        first = lines.index(start) + 1
        last = lines.index(end, first)
    except ValueError:
        return []
    return lines[first:last]


def _question_line(lines: list[str], token: str) -> str:
    matches = [line for line in lines if token in line]
    return matches[0] if len(matches) == 1 else ""


def validate_assignment_q9_sufficiency(repo_root: Path) -> AssignmentQ9SufficiencyResult:
    errors: list[str] = []
    payload = _load(repo_root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_MAP_KEYS:
        return _result((ASSIGNMENT_Q9_MAP_INVALID,))

    digest = hashlib.sha256(
        yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode("utf-8")
    ).hexdigest()
    if (
        digest != MAP_SHA256
        or payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-047"
        or payload.get("baseline") != BASELINE
        or set(payload.get("forbidden_outcomes") or ()) != EXPECTED_FORBIDDEN_OUTCOMES
        or len(payload.get("forbidden_outcomes") or ()) != len(EXPECTED_FORBIDDEN_OUTCOMES)
    ):
        errors.append(ASSIGNMENT_Q9_MAP_INVALID)

    criterion = payload.get("sufficiency_criterion")
    decision = payload.get("decision")
    gate = payload.get("gate_first")
    if (
        not isinstance(criterion, dict)
        or criterion.get("declared_before_application") is not True
        or criterion.get("form_only_basis_is_sufficient") is not False
        or criterion.get("result") != "insufficient-for-q9-closure"
        or not isinstance(decision, dict)
        or decision.get("question_id") != "Q9"
        or decision.get("disposition") != "remains-open-insufficient-evidence"
        or decision.get("criterion_satisfied") is not False
        or decision.get("closure_authorized_by_this_outcome") is not False
        or decision.get("subject_changed") is not False
        or decision.get("temporal_blocker_removed") is not False
        or not isinstance(gate, dict)
        or gate.get("evidence_form", {}).get("applies") is not False
        or gate.get("evidence_form", {}).get("positive_capable") is not False
        or gate.get("hypothetical_closures", {}).get("single_interval_only", {}).get("applies") is not True
        or gate.get("hypothetical_closures", {}).get("multiple_intervals", {}).get("applies") is not True
        or gate.get("consumer_selects_cardinality") is not False
    ):
        errors.append(ASSIGNMENT_Q9_EVIDENCE_DRIFT)

    historical_subject = historical_path(repo_root, SUBJECT_PATH, SUBJECT_SHA256)
    try:
        subject_text = (repo_root / historical_subject).read_text(encoding="utf-8")
        current_text = (repo_root / SUBJECT_PATH).read_text(encoding="utf-8")
    except OSError:
        subject_text = ""
        current_text = ""
    metadata = _frontmatter(subject_text)
    current_metadata = _frontmatter(current_text)
    question_lines = _section_lines(
        current_text,
        "## 19. Open Questions and Resolved Boundaries",
        "## 20. Deferred Decisions",
    )
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
        errors.append(ASSIGNMENT_Q9_SUBJECT_DRIFT)

    if set(OPEN_QUESTION_TOKENS) != {"Q2", "Q4", "Q5", "Q7", "Q8", "Q9", "Q10", "Q11"}:
        errors.append(ASSIGNMENT_Q9_PROJECTION_DRIFT)
    for token in OPEN_QUESTION_TOKENS.values():
        line = _question_line(question_lines, token)
        if not line or "~~" in line:
            errors.append(ASSIGNMENT_Q9_PROJECTION_DRIFT)
            break
    if OPEN_QUESTION_TOKENS.get("Q9") != Q9_TOKEN:
        errors.append(ASSIGNMENT_Q9_PROJECTION_DRIFT)
    if set(RESOLVED_QUESTION_TOKENS) != {"Q1", "Q3", "Q6"}:
        errors.append(ASSIGNMENT_Q9_PROJECTION_DRIFT)
    for token in RESOLVED_QUESTION_TOKENS.values():
        line = _question_line(question_lines, token)
        if not line or "~~" not in line:
            errors.append(ASSIGNMENT_Q9_PROJECTION_DRIFT)
            break
    if len([line for line in question_lines if line.strip()]) != 11:
        errors.append(ASSIGNMENT_Q9_PROJECTION_DRIFT)

    surface = _load(repo_root / SURFACE_PATH)
    if not isinstance(surface, dict):
        errors.append(ASSIGNMENT_Q9_PROJECTION_DRIFT)
    else:
        questions = {
            item.get("question_id"): (item.get("state"), item.get("classification"))
            for item in surface.get("open_question_inventory", [])
            if isinstance(item, dict)
        }
        moving = {
            item.get("surface_id"): item.get("question_ids")
            for item in surface.get("moving_surfaces", [])
            if isinstance(item, dict)
        }
        blockers = {
            item.get("blocker_id"): item.get("question_ids")
            for item in surface.get("blockers", [])
            if isinstance(item, dict)
        }
        subject = surface.get("subject")
        if (
            questions.get("Q9") != ("open", "blocks-whole-document-freeze")
            or questions.get("Q2") != ("open", "blocks-whole-document-freeze")
            or questions.get("Q5") != ("open", "blocks-whole-document-freeze")
            or moving.get("TEMPORAL_EFFECTIVITY_EXTENSION") != ["Q9"]
            or blockers != {
                "AMENDMENT_MODEL_ABSENT": ["Q2"],
                "TEMPORAL_MODEL_UNRESOLVED": ["Q9"],
                "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": ["Q5"],
            }
            or not isinstance(subject, dict)
            or subject.get("discovery_result") != "bounded_stable_candidate_not_selected"
            or str(subject.get("expected_version")) != "0.4.0"
            or subject.get("expected_status") != "Accepted"
            or subject.get("expected_concept_status") != "Accepted"
            or payload.get("current_projection") != {
                "q2_state": "open",
                "q5_state": "open",
                "q9_state": "open",
                "temporal_moving_surface_question_ids": ["Q9"],
                "blockers": {
                    "AMENDMENT_MODEL_ABSENT": ["Q2"],
                    "TEMPORAL_MODEL_UNRESOLVED": ["Q9"],
                    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": ["Q5"],
                },
                "assignment_discovery_result": "bounded_stable_candidate_not_selected",
                "whole_document_freeze_reachable": False,
                "promotion_candidate_ids": ["OCP-005", "OCP-006", "OCP-010"],
            }
        ):
            errors.append(ASSIGNMENT_Q9_PROJECTION_DRIFT)

    declared_classes = {
        item.get("resolution_id"): {
            "pressure_need_adequacy_effect": item.get("pressure_need_adequacy_effect"),
            "norm_classification": item.get("norm_classification"),
            "norm_underdetermined_axes": tuple(item.get("norm_underdetermined_axes") or ()),
        }
        for item in payload.get("surviving_q9_classes", [])
        if isinstance(item, dict)
    }
    pressure = _load(repo_root / PRESSURE_PATH)
    pressure_rows = {
        item.get("resolution_id"): item
        for item in pressure.get("resolution_inventory", [])
        if isinstance(item, dict)
    } if isinstance(pressure, dict) else {}
    norm = _load(repo_root / NORM_PATH)
    norm_rows = {
        item.get("resolution_id"): item
        for item in norm.get("survivor_results", [])
        if isinstance(item, dict)
    } if isinstance(norm, dict) else {}
    if declared_classes != EXPECTED_Q9_CLASSES:
        errors.append(ASSIGNMENT_Q9_EVIDENCE_DRIFT)
    for resolution_id, expected in EXPECTED_Q9_CLASSES.items():
        pressure_row = pressure_rows.get(resolution_id, {})
        norm_row = norm_rows.get(resolution_id, {})
        if (
            pressure_row.get("need_adequacy_effect") != expected["pressure_need_adequacy_effect"]
            or norm_row.get("classification") != expected["norm_classification"]
            or tuple(norm_row.get("underdetermined_axes") or ()) != expected["norm_underdetermined_axes"]
            or norm_row.get("violation_statement_ids") != []
        ):
            errors.append(ASSIGNMENT_Q9_EVIDENCE_DRIFT)
            break

    evidence = payload.get("evidence_ledger")
    anchors = payload.get("baseline_evidence_objects")
    if (
        not isinstance(anchors, list)
        or len(anchors) != 15
        or len({item.get("path") for item in anchors if isinstance(item, dict)}) != 15
        or any(
            set(item) != {"path", "blob", "sha256", "state_tokens"}
            or not item.get("path")
            or not item.get("blob")
            or not item.get("sha256")
            or not item.get("state_tokens")
            for item in anchors
            if isinstance(item, dict)
        )
        or len([item for item in anchors if isinstance(item, dict)]) != 15
        or
        not isinstance(evidence, list)
        or len(evidence) != 7
        or {item.get("evidence_mode") for item in evidence if isinstance(item, dict)} != {"analytic", "observed"}
        or any(not item.get("proves") or not item.get("does_not_prove") for item in evidence if isinstance(item, dict))
    ):
        errors.append(ASSIGNMENT_Q9_EVIDENCE_DRIFT)

    probe = payload.get("executable_probe")
    try:
        fixture = load_fixture(repo_root / PROBE_FIXTURE)
        original = fixture.get("entity")
    except (OSError, ValueError, yaml.YAMLError):
        original = None
    if not isinstance(probe, dict) or not isinstance(original, dict):
        errors.append(ASSIGNMENT_Q9_PROBE_DRIFT)
    else:
        extension = copy.deepcopy(original)
        extension[probe.get("subject_field")] = copy.deepcopy(
            probe.get("two_interval_extension", {}).get("value")
        )
        invalid = copy.deepcopy(original)
        invalid["applicability_end"] = probe.get("validator_rejection_control", {}).get("applicability_end")
        original_result = validate_assignment(original)
        extension_result = validate_assignment(extension)
        invalid_result = validate_assignment(invalid)
        at = probe.get("single_interval_control", {}).get("expected_effective_at")
        extension_at = probe.get("two_interval_extension", {}).get("expected_effective_at")
        if (
            probe.get("fixture") != str(PROBE_FIXTURE)
            or probe.get("subject_field") != "applicability_intervals"
            or probe.get("result") != "validator-does-not-discriminate-q9-cardinality"
            or original_result.valid is not True
            or extension_result.valid is not True
            or probe.get("single_interval_control", {}).get("expected_valid") is not True
            or probe.get("two_interval_extension", {}).get("expected_valid") is not True
            or assignment_effective_at(original, at) is not True
            or assignment_effective_at(extension, extension_at) is not True
            or invalid_result.valid is not False
            or probe.get("validator_rejection_control", {}).get("expected_valid") is not False
            or probe.get("validator_rejection_control", {}).get("expected_error") not in invalid_result.errors
        ):
            errors.append(ASSIGNMENT_Q9_PROBE_DRIFT)

    declared_hashes = {
        item.get("path"): item.get("sha256")
        for item in payload.get("protected_artifacts", [])
        if isinstance(item, dict)
    }
    if declared_hashes != EXPECTED_PROTECTED_HASHES or any(
        _hash(repo_root / historical_path(repo_root, Path(path), sha256)) != sha256
        for path, sha256 in EXPECTED_PROTECTED_HASHES.items()
    ):
        errors.append(ASSIGNMENT_Q9_PROTECTED_ARTIFACT_DRIFT)

    promotion = _load(repo_root / GATE_PATH)
    protocol = promotion.get("cycle_protocol") if isinstance(promotion, dict) else None
    cycles = promotion.get("cycles") if isinstance(promotion, dict) else None
    candidates = promotion.get("candidates") if isinstance(promotion, dict) else None
    completed = [
        item.get("cycle_id")
        for item in cycles
        if isinstance(item, dict)
        and isinstance(item.get("steps"), dict)
        and set(item["steps"].values()) == {"completed"}
    ] if isinstance(cycles, list) else []
    candidate_ids = [item.get("document_id") for item in candidates if isinstance(item, dict)] if isinstance(candidates, list) else []
    assignment_candidate = next(
        (item for item in candidates if isinstance(item, dict) and item.get("document_id") == "OCP-005"),
        {},
    ) if isinstance(candidates, list) else {}
    if (
        not isinstance(promotion, dict)
        or not isinstance(protocol, dict)
        or candidate_ids != ["OCP-005", "OCP-006", "OCP-010"]
        or assignment_candidate.get("expected_document_status") != "Accepted"
        or assignment_candidate.get("expected_concept_status") != "Accepted"
        or set(payload.get("promotion_gate_guard") or {}) != {"schema_version", "completed_cycle_ids", "active_cycle_id"}
        or not promotion_gate_guard_is_current(promotion, payload.get("promotion_gate_guard"))
    ):
        errors.append(ASSIGNMENT_Q9_GATE_DRIFT)

    return _result(errors)
