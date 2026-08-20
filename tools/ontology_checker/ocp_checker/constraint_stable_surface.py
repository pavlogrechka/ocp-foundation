from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
from typing import Any, Iterable

import yaml

from .historical_evidence import historical_path


CONSTRAINT_STABLE_SURFACE_MAP_INVALID = "CONSTRAINT_STABLE_SURFACE_MAP_INVALID"
CONSTRAINT_STABLE_SURFACE_SUBJECT_DRIFT = "CONSTRAINT_STABLE_SURFACE_SUBJECT_DRIFT"
CONSTRAINT_STABLE_SURFACE_QUESTION_DRIFT = "CONSTRAINT_STABLE_SURFACE_QUESTION_DRIFT"
CONSTRAINT_STABLE_SURFACE_CLASSIFICATION_DRIFT = "CONSTRAINT_STABLE_SURFACE_CLASSIFICATION_DRIFT"
CONSTRAINT_STABLE_SURFACE_EVIDENCE_DRIFT = "CONSTRAINT_STABLE_SURFACE_EVIDENCE_DRIFT"
CONSTRAINT_STABLE_SURFACE_CLOSURE_DRIFT = "CONSTRAINT_STABLE_SURFACE_CLOSURE_DRIFT"
CONSTRAINT_STABLE_SURFACE_GATE_DRIFT = "CONSTRAINT_STABLE_SURFACE_GATE_DRIFT"

MAP_PATH = Path("architecture/constraint-stable-surface.yaml")
SUBJECT_PATH = Path("docs/006-constraint-concept/README.md")
HISTORICAL_SUBJECT_SHA256 = "0472d8ce4b15a8c64d58151ee7f706b450b930f708f6f0a7a40bdd87914b3b10"
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
MAP_KEYS = frozenset(
    {
        "schema_version", "rule_owner", "baseline", "gate_first",
        "promotion_gate_guard", "subject", "classification_criterion",
        "question_inventory", "stable_candidates", "moving_surfaces", "blockers",
        "forbidden_outcomes", "historical_closure_evidence",
        "baseline_evidence_objects",
    }
)
QUESTION_IDS = frozenset(f"Q{number}" for number in range(1, 13))
OPEN_QUESTION_IDS = frozenset({"Q1", "Q2", "Q6", "Q7", "Q8", "Q10", "Q11", "Q12"})
RESOLVED_QUESTION_IDS = frozenset({"Q3", "Q4", "Q5", "Q9"})
QUESTION_CLASSIFICATIONS = frozenset(
    {
        "blocks-whole-document-freeze", "local-after-bounded-freeze",
        "outside-bounded-surface", "outside-open-set",
    }
)
STABLE_SURFACE_IDS = frozenset(
    {
        "CONSTRAINT_IDENTITY_SUPERSESSION_KERNEL",
        "STRUCTURAL_LIFECYCLE_EFFECTIVITY_KERNEL",
        "BOUNDED_EVALUATION_KERNEL",
        "FAIL_SAFE_NON_AUTHORITY_BOUNDARY",
        "TARGET_SCOPE_NON_INHERITANCE_BOUNDARY",
    }
)
MOVING_SURFACE_IDS = frozenset(
    {
        "EXPRESSION_LANGUAGE", "DYNAMIC_INPUT_EVALUATION_CURRENTNESS",
        "STORAGE_OR_REPRODUCTION_POLICY", "OPTIONAL_KIND_TAXONOMY",
        "DOMAIN_RELATION_LANGUAGE", "FUTURE_CONFLICT_OWNER",
        "EXTERNAL_OPERATION_AUTHORIZATION_OWNER", "FUTURE_READINESS_AVAILABILITY_OWNER",
    }
)
BLOCKER_IDS = frozenset({"EVALUATION_CURRENTNESS_UNRESOLVED"})
FORBIDDEN_OUTCOMES = frozenset(
    {
        "OCP006_EDIT", "OCP006_STATUS_OR_VERSION_CHANGE", "OPEN_QUESTION_CLOSURE",
        "CONSTRAINT_SELECTION", "PROMOTION_CYCLE_START",
        "CONSTRAINT_CONCEPT_CANONICALIZATION", "OCP005_OR_ASSIGNMENT_BLOCKER_CHANGE",
        "GRAPH_OR_REGISTRY_CHANGE",
    }
)

EXPECTED_GATE_FIRST = {
    "ocp016_gate": "G4",
    "applies": False,
    "reason": "discovery-evidence-is-not-a-positive-capable-rule-result-or-profile",
    "activation_performed": False,
}
EXPECTED_SUBJECT = {
    "document_id": "OCP-006",
    "primary": str(SUBJECT_PATH),
    "expected_version": "0.3.2",
    "expected_status": "Draft",
    "expected_concept_status": "Accepted",
    "discovery_result": "bounded-stable-candidate-with-one-whole-freeze-blocker-not-selected",
}
EXPECTED_CRITERION = {
    "vocabulary_source": "architecture/assignment-stable-surface.yaml",
    "classes": {
        "blocks-whole-document-freeze": "every-permitted-answer-can-change-a-declared-property-inside-the-bounded-kernel",
        "local-after-bounded-freeze": "a-named-kernel-remains-invariant-under-every-permitted-answer",
        "outside-bounded-surface": "current-owner-boundary-keeps-the-question-outside-the-named-kernel",
        "outside-open-set": "resolved-question-excluded-from-current-open-inventory",
    },
    "unclassified_policy": "report-vocabulary-gap-before-extension",
}

EXPECTED_QUESTIONS: dict[str, dict[str, Any]] = {
    "Q1": {"state": "open", "classification": "outside-bounded-surface", "surface": "CONFLICT_OBJECT_OR_AGGREGATION", "classification_basis_mode": "analytical", "evidence_token": "Чи потрібен окремий фундаментальний Concept `Conflict`, чи достатньо агрегованого evaluation model?", "basis": ((str(SUBJECT_PATH), ("## 13. Violation and Conflict Boundary", "не є автоматично фундаментальним Conflict")),), "invariant_surface": "VIOLATION_NON_CONFLICT_BOUNDARY", "moving_surface": "FUTURE_CONFLICT_OWNER"},
    "Q2": {"state": "open", "classification": "local-after-bounded-freeze", "surface": "PREDICATE_EXPRESSION_LANGUAGE", "classification_basis_mode": "analytical", "evidence_token": "Яка канонічна expression або rule language потрібна для PredicateSpecification?", "basis": ((str(SUBJECT_PATH), ("### 6.2 PredicateSpecification", "не визначає технологію його виконання")),), "invariant_surface": "VERSIONED_PREDICATE_INPUT_CONTRACT", "moving_surface": "EXPRESSION_LANGUAGE"},
    "Q3": {"state": "resolved", "classification": "outside-open-set", "surface": "PRECEDENCE_OVERRIDE_EXCEPTION", "classification_basis_mode": "observational", "evidence_token": "Як визначаються precedence, override та exception між Constraint?", "closure_act": "AD-027"},
    "Q4": {"state": "resolved", "classification": "outside-open-set", "surface": "CONTEXTUAL_WAIVER", "classification_basis_mode": "observational", "evidence_token": "Чи допускаються contextual waivers, і яким Concept вони представлені?", "closure_act": "AD-027"},
    "Q5": {"state": "resolved", "classification": "outside-open-set", "surface": "QUANTITY_UNIT_DEMAND_CAPACITY_INPUT", "classification_basis_mode": "observational", "evidence_token": "Яка модель quantity, unit, demand і capacity потрібна для кількісних Constraint?", "closure_act": "AD-025"},
    "Q6": {"state": "open", "classification": "blocks-whole-document-freeze", "surface": "DYNAMIC_INPUT_EVALUATION_CURRENTNESS", "classification_basis_mode": "analytical", "evidence_token": "Який строк актуальності має ConstraintEvaluationRecord для dynamic inputs?", "basis": ((str(SUBJECT_PATH), ("no current authoritative result exists", "Відсутність current evaluation ніколи не трактується як `satisfied`")),), "undefined_property": "when-a-dynamic-input-evaluation-ceases-to-be-current", "affected_declared_property": "EFFECTIVE_RESULT_AND_ADMISSIBILITY"},
    "Q7": {"state": "open", "classification": "local-after-bounded-freeze", "surface": "EVALUATION_PERSISTENCE_MODE", "classification_basis_mode": "analytical", "evidence_token": "Чи повинні всі blocking evaluations зберігатися, чи частина може бути відтворюваною derivation?", "basis": ((str(SUBJECT_PATH), ("authoritative stored or reproducible result", "exact Constraint version and input snapshot")),), "invariant_surface": "EXACT_BOUND_AUTHORITATIVE_RESULT", "moving_surface": "STORAGE_OR_REPRODUCTION_POLICY"},
    "Q8": {"state": "open", "classification": "outside-bounded-surface", "surface": "OPERATION_AUTHORIZATION", "classification_basis_mode": "analytical", "evidence_token": "Як Constraint взаємодіє з authorization Operation?", "basis": ((str(SUBJECT_PATH), ("не замінює authorization, approval або execution decision", "не є джерелом авторизації автоматично")),), "invariant_surface": "CONSTRAINT_NON_AUTHORIZATION_BOUNDARY", "moving_surface": "EXTERNAL_OPERATION_AUTHORIZATION_OWNER"},
    "Q9": {"state": "resolved", "classification": "outside-open-set", "surface": "RESERVATION_OBJECT_FORM", "classification_basis_mode": "observational", "evidence_token": "Чи є Reservation окремим Concept або результатом Assignment та blocking Constraint?", "closure_act": "AD-026"},
    "Q10": {"state": "open", "classification": "outside-bounded-surface", "surface": "READINESS_AVAILABILITY_HANDOFF", "classification_basis_mode": "analytical", "evidence_token": "Які Constraint повинні впливати на майбутню Readiness або availability model?", "basis": ((str(SUBJECT_PATH), ("Readiness і availability не виводяться з одного violation без окремого прийнятого правила",)),), "invariant_surface": "NON_READINESS_NON_AVAILABILITY_BOUNDARY", "moving_surface": "FUTURE_READINESS_AVAILABILITY_OWNER"},
    "Q11": {"state": "open", "classification": "local-after-bounded-freeze", "surface": "CONSTRAINT_KIND_TAXONOMY", "classification_basis_mode": "analytical", "evidence_token": "Чи потрібна окрема taxonomy constraint kinds у Core?", "basis": ((str(SUBJECT_PATH), ("## 14. Working Constraint Patterns", "робочими прикладами, а не канонічною taxonomy")),), "invariant_surface": "PREDICATE_AND_ENFORCEMENT_KERNEL", "moving_surface": "OPTIONAL_KIND_TAXONOMY"},
    "Q12": {"state": "open", "classification": "local-after-bounded-freeze", "surface": "DOMAIN_RELATION_EXPRESSION", "classification_basis_mode": "analytical", "evidence_token": "Як виражати Constraint над геометричними, часовими та спектральними relations без включення domain semantics до Core?", "basis": ((str(SUBJECT_PATH), ("relation_scope", "Конкретна selector language не визначається OCP-006", "Domain module може визначати власні predicate namespaces")),), "invariant_surface": "OPAQUE_TARGET_AND_VERSIONED_INPUT_CONTRACT", "moving_surface": "DOMAIN_RELATION_LANGUAGE"},
}

EXPECTED_STABLE_EVIDENCE = {
    "CONSTRAINT_IDENTITY_SUPERSESSION_KERNEL": ((str(SUBJECT_PATH), ("## 5. Identity", "зміна predicate, target specification, parameters або enforcement semantics створює новий Constraint", "## 16. Supersession and Change")),),
    "STRUCTURAL_LIFECYCLE_EFFECTIVITY_KERNEL": ((str(SUBJECT_PATH), ("## 6. Minimum Structural Contract", "## 7. Working Lifecycle", "## 8. Temporal Effectivity")), ("tools/ontology_checker/ocp_checker/checker.py", ("def constraint_effective_at(", "def validate_constraint("))),
    "BOUNDED_EVALUATION_KERNEL": ((str(SUBJECT_PATH), ("## 9. Evaluation Context", "## 10. Applicability", "## 11. Evaluation Result", "## 12. Admissibility Derivation")), ("tools/ontology_checker/ocp_checker/checker.py", ("def constraint_applicable_to(", "def effective_constraint_result(", "def constraint_set_decision("))),
    "FAIL_SAFE_NON_AUTHORITY_BOUNDARY": ((str(SUBJECT_PATH), ("Відсутність current evaluation ніколи не трактується як `satisfied`", "не замінює authorization, approval або execution decision", "не є автоматично фундаментальним Conflict")),),
    "TARGET_SCOPE_NON_INHERITANCE_BOUNDARY": ((str(SUBJECT_PATH), ("### 6.1 TargetSpecification", "## 15. Composition and Non-Inheritance", "scope повинен бути перевірним і простежуваним")),),
}
EXPECTED_MOVING = {
    "EXPRESSION_LANGUAGE": ("moving", ("Q2",)),
    "DYNAMIC_INPUT_EVALUATION_CURRENTNESS": ("moving", ("Q6",)),
    "STORAGE_OR_REPRODUCTION_POLICY": ("moving", ("Q7",)),
    "OPTIONAL_KIND_TAXONOMY": ("moving", ("Q11",)),
    "DOMAIN_RELATION_LANGUAGE": ("moving", ("Q12",)),
    "FUTURE_CONFLICT_OWNER": ("moving-external-owner", ("Q1",)),
    "EXTERNAL_OPERATION_AUTHORIZATION_OWNER": ("moving-external-owner", ("Q8",)),
    "FUTURE_READINESS_AVAILABILITY_OWNER": ("moving-external-owner", ("Q10",)),
}
EXPECTED_BLOCKERS = {
    "EVALUATION_CURRENTNESS_UNRESOLVED": ("blocks-whole-document-freeze", ("Q6",)),
}
EXPECTED_CLOSURES = {
    "AD-025": ("architecture/discovery/AD-025-quantitative-constraint-input.md", "Accepted", ("Q5",), ("Quantity, Demand and Capacity Input Model", "positive capacity result remains gated future work")),
    "AD-026": ("architecture/discovery/AD-026-reservation-allocation-boundary.md", "Accepted", ("Q9",), ("Reservation and Allocation Establishment Boundary", "does not establish Reservation or Allocation authority")),
    "AD-027": ("architecture/discovery/AD-027-constraint-interaction-boundaries.md", "Accepted", ("Q3", "Q4"), ("Constraint Application Order, Override and Contextual Waiver Boundaries", "no normative Constraint application order is established")),
}
EXPECTED_BASELINE_OBJECTS = {
    str(SUBJECT_PATH): ("50f149cf5563083bb84d5d2197ec32c2ed15fa9b", "0472d8ce4b15a8c64d58151ee7f706b450b930f708f6f0a7a40bdd87914b3b10"),
    "architecture/discovery/AD-025-quantitative-constraint-input.md": ("cd4e320be2db6398d758c6fa3ae49e0a0f520df5", "dae3ee9ea8ffbe0fb62df127fa53920705d59f50ec793cb41cb6ca3c10642d46"),
    "architecture/discovery/AD-026-reservation-allocation-boundary.md": ("ad109d1003af32a019e6b525b4552db2c6e323b2", "e258d714d242a5065b23c296a413a6d0d8c52e72d967b42798153888f6d872bd"),
    "architecture/discovery/AD-027-constraint-interaction-boundaries.md": ("fa49556df4f06aa039df23d9cc244587411b2d5e", "8d62725e4f8b1513c85fd24d59017215da94ddef8cda5244f300a6f25a0ee442"),
}


@dataclass(frozen=True)
class ConstraintStableSurfaceResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> ConstraintStableSurfaceResult:
    return ConstraintStableSurfaceResult(tuple(dict.fromkeys(errors)))


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


def _evidence(entries: Any) -> tuple[tuple[str, tuple[str, ...]], ...] | None:
    if not isinstance(entries, list):
        return None
    result: list[tuple[str, tuple[str, ...]]] = []
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {"path", "tokens"} or not isinstance(entry.get("tokens"), list):
            return None
        result.append((str(entry["path"]), tuple(str(token) for token in entry["tokens"])))
    return tuple(result)


def _normalize_question(entry: Any) -> tuple[str, dict[str, Any]] | None:
    if not isinstance(entry, dict) or not isinstance(entry.get("question_id"), str):
        return None
    normalized = dict(entry)
    question_id = str(normalized.pop("question_id"))
    if "basis" in normalized:
        basis = _evidence(normalized["basis"])
        if basis is None:
            return None
        normalized["basis"] = basis
    return question_id, normalized


def _numbered_questions(text: str) -> dict[str, tuple[str, bool]]:
    start = text.find("## 22. Open Questions and Resolved Boundaries")
    end = text.find("## 23. Deferred Decisions", start + 1)
    if start < 0 or end < 0:
        return {}
    result: dict[str, tuple[str, bool]] = {}
    for line in text[start:end].splitlines():
        match = re.match(r"^(\d+)\.\s+(.*)$", line.strip())
        if match:
            result[f"Q{match.group(1)}"] = (match.group(2), match.group(2).startswith("~~"))
    return result


def _git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def _check_tokens(repo_root: Path, evidence: tuple[tuple[str, tuple[str, ...]], ...]) -> bool:
    for path, tokens in evidence:
        try:
            relative = Path(path)
            resolved = historical_path(
                repo_root, relative, HISTORICAL_SUBJECT_SHA256
            ) if relative == SUBJECT_PATH else relative
            text = (repo_root / resolved).read_text(encoding="utf-8")
        except OSError:
            return False
        if any(token not in text for token in tokens):
            return False
    return True


def validate_constraint_stable_surface(repo_root: Path) -> ConstraintStableSurfaceResult:
    errors: list[str] = []
    try:
        payload = yaml.safe_load((repo_root / MAP_PATH).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return _result((CONSTRAINT_STABLE_SURFACE_MAP_INVALID,))
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((CONSTRAINT_STABLE_SURFACE_MAP_INVALID,))

    if (
        payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-050"
        or payload.get("baseline") != "f76f2d0828088e8d98b7a8d64f8c71cc843a13e6"
        or payload.get("gate_first") != EXPECTED_GATE_FIRST
        or payload.get("subject") != EXPECTED_SUBJECT
        or payload.get("classification_criterion") != EXPECTED_CRITERION
        or frozenset(payload.get("forbidden_outcomes") or ()) != FORBIDDEN_OUTCOMES
        or MAP_KEYS != frozenset(MAP_KEYS)
        or QUESTION_IDS != OPEN_QUESTION_IDS | RESOLVED_QUESTION_IDS
        or set(EXPECTED_QUESTIONS) != QUESTION_IDS
        or QUESTION_CLASSIFICATIONS != frozenset(EXPECTED_CRITERION["classes"])
    ):
        errors.append(CONSTRAINT_STABLE_SURFACE_MAP_INVALID)

    historical_subject = historical_path(repo_root, SUBJECT_PATH, HISTORICAL_SUBJECT_SHA256)
    metadata = _frontmatter(repo_root / historical_subject)
    if not metadata or any(
        metadata.get(field) != expected
        for field, expected in (
            ("Document-ID", "OCP-006"), ("Version", "0.3.2"),
            ("Status", "Draft"), ("Concept-Status", "Accepted"),
        )
    ):
        errors.append(CONSTRAINT_STABLE_SURFACE_SUBJECT_DRIFT)

    try:
        subject_text = (repo_root / SUBJECT_PATH).read_text(encoding="utf-8")
    except OSError:
        subject_text = ""
    live_questions = _numbered_questions(subject_text)
    normalized_questions: dict[str, dict[str, Any]] = {}
    raw_questions = payload.get("question_inventory")
    if isinstance(raw_questions, list):
        for item in raw_questions:
            normalized = _normalize_question(item)
            if normalized is None or normalized[0] in normalized_questions:
                errors.append(CONSTRAINT_STABLE_SURFACE_MAP_INVALID)
                continue
            normalized_questions[normalized[0]] = normalized[1]
    else:
        errors.append(CONSTRAINT_STABLE_SURFACE_MAP_INVALID)

    if set(live_questions) != QUESTION_IDS or set(normalized_questions) != QUESTION_IDS:
        errors.append(CONSTRAINT_STABLE_SURFACE_QUESTION_DRIFT)
    for question_id, expected in EXPECTED_QUESTIONS.items():
        actual = normalized_questions.get(question_id)
        if actual != expected:
            errors.append(CONSTRAINT_STABLE_SURFACE_CLASSIFICATION_DRIFT)
            continue
        line, resolved = live_questions.get(question_id, ("", False))
        if expected["evidence_token"] not in line or resolved != (expected["state"] == "resolved"):
            errors.append(CONSTRAINT_STABLE_SURFACE_QUESTION_DRIFT)
        basis = expected.get("basis")
        if basis and not _check_tokens(repo_root, basis):
            errors.append(CONSTRAINT_STABLE_SURFACE_EVIDENCE_DRIFT)

    stable: dict[str, tuple[tuple[str, tuple[str, ...]], ...]] = {}
    for item in payload.get("stable_candidates") or ():
        if isinstance(item, dict) and set(item) == {"surface_id", "evidence"}:
            evidence = _evidence(item["evidence"])
            if evidence is not None:
                stable[str(item["surface_id"])] = evidence
    if set(stable) != STABLE_SURFACE_IDS or stable != EXPECTED_STABLE_EVIDENCE:
        errors.append(CONSTRAINT_STABLE_SURFACE_CLASSIFICATION_DRIFT)
    for evidence in stable.values():
        if not _check_tokens(repo_root, evidence):
            errors.append(CONSTRAINT_STABLE_SURFACE_EVIDENCE_DRIFT)

    moving = {
        str(item.get("surface_id")): (str(item.get("disposition")), tuple(item.get("question_ids") or ()))
        for item in payload.get("moving_surfaces") or () if isinstance(item, dict)
    }
    blockers = {
        str(item.get("blocker_id")): (str(item.get("disposition")), tuple(item.get("question_ids") or ()))
        for item in payload.get("blockers") or () if isinstance(item, dict)
    }
    if set(moving) != MOVING_SURFACE_IDS or moving != EXPECTED_MOVING:
        errors.append(CONSTRAINT_STABLE_SURFACE_CLASSIFICATION_DRIFT)
    if set(blockers) != BLOCKER_IDS or blockers != EXPECTED_BLOCKERS:
        errors.append(CONSTRAINT_STABLE_SURFACE_CLASSIFICATION_DRIFT)

    closures = payload.get("historical_closure_evidence")
    normalized_closures: dict[str, tuple[str, str, tuple[str, ...], tuple[str, ...]]] = {}
    if isinstance(closures, dict):
        for act_id, item in closures.items():
            if isinstance(item, dict):
                normalized_closures[str(act_id)] = (
                    str(item.get("path")), str(item.get("expected_status")),
                    tuple(item.get("question_ids") or ()), tuple(item.get("tokens") or ()),
                )
    if normalized_closures != EXPECTED_CLOSURES:
        errors.append(CONSTRAINT_STABLE_SURFACE_CLOSURE_DRIFT)
    for path, status, _, tokens in normalized_closures.values():
        metadata = _frontmatter(repo_root / path)
        try:
            text = (repo_root / path).read_text(encoding="utf-8")
        except OSError:
            text = ""
        if not metadata or metadata.get("Status") != status or any(token not in text for token in tokens):
            errors.append(CONSTRAINT_STABLE_SURFACE_CLOSURE_DRIFT)

    baseline_objects = {
        str(item.get("path")): (str(item.get("blob")), str(item.get("sha256")))
        for item in payload.get("baseline_evidence_objects") or () if isinstance(item, dict)
    }
    if baseline_objects != EXPECTED_BASELINE_OBJECTS:
        errors.append(CONSTRAINT_STABLE_SURFACE_EVIDENCE_DRIFT)
    for path, (blob, sha256) in baseline_objects.items():
        try:
            resolved = historical_path(repo_root, Path(path), sha256)
            data = (repo_root / resolved).read_bytes()
        except OSError:
            errors.append(CONSTRAINT_STABLE_SURFACE_EVIDENCE_DRIFT)
            continue
        if _git_blob(data) != blob or hashlib.sha256(data).hexdigest() != sha256:
            errors.append(CONSTRAINT_STABLE_SURFACE_EVIDENCE_DRIFT)

    try:
        gate = yaml.safe_load((repo_root / GATE_PATH).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        gate = None
    guard = payload.get("promotion_gate_guard")
    cycles = gate.get("cycles") if isinstance(gate, dict) else None
    completed = [
        item.get("cycle_id") for item in cycles or ()
        if isinstance(item, dict)
        and set((item.get("steps") or {}).values()) == {"completed"}
    ]
    protocol = gate.get("cycle_protocol") if isinstance(gate, dict) else None
    if (
        guard != {"schema_version": 5, "completed_cycle_ids": ["EVENT_T6"], "active_cycle_id": None}
        or not isinstance(gate, dict) or gate.get("schema_version") != 5
        or completed != ["EVENT_T6"]
        or not isinstance(protocol, dict) or protocol.get("active_cycle_id") is not None
    ):
        errors.append(CONSTRAINT_STABLE_SURFACE_GATE_DRIFT)
    return _result(errors)
