from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
from typing import Any, Iterable

import yaml

from .checker import assignment_effective_at, load_fixture, validate_assignment
from .historical_evidence import historical_path


ASSIGNMENT_Q3_MAP_INVALID = "ASSIGNMENT_Q3_MAP_INVALID"
ASSIGNMENT_Q3_SUBJECT_DRIFT = "ASSIGNMENT_Q3_SUBJECT_DRIFT"
ASSIGNMENT_Q3_EVIDENCE_DRIFT = "ASSIGNMENT_Q3_EVIDENCE_DRIFT"
ASSIGNMENT_Q3_PROJECTION_DRIFT = "ASSIGNMENT_Q3_PROJECTION_DRIFT"
ASSIGNMENT_Q3_PROBE_DRIFT = "ASSIGNMENT_Q3_PROBE_DRIFT"
ASSIGNMENT_Q3_HISTORICAL_DRIFT = "ASSIGNMENT_Q3_HISTORICAL_DRIFT"
ASSIGNMENT_Q3_GATE_DRIFT = "ASSIGNMENT_Q3_GATE_DRIFT"

MAP_PATH = Path("architecture/assignment-retroactivity-q3-resolution.yaml")
SUBJECT_PATH = Path("docs/005-assignment-concept/README.md")
SURFACE_PATH = Path("architecture/assignment-stable-surface.yaml")
PRESSURE_PATH = Path("architecture/assignment-consumer-pressure.yaml")
NORM_PATH = Path("architecture/assignment-norm-compatibility.yaml")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
PROBE_FIXTURE = Path("tools/ontology_checker/fixtures/assignment/valid-established.yaml")

BASELINE = "ca87815b0198c165cfeec759965656da2ef7b5b2"
MAP_SHA256 = "a6f01849e0b23db0fdbf5ab94d397834cf11363bd46d07dd5086056bf8c5f2e7"
Q3_TOKEN = "Чи допускається ретроактивне Establishment Assignment?"
Q9_TOKEN = "Чи може один Assignment мати кілька неперервних applicability intervals"
FINAL_BOUNDARY = (
    "Assignment не може бути ефективним для часу раніше авторитетного `established_at`. "
    "Це остаточна негативна межа Q3: ретроактивне Establishment не створює effectivity "
    "до авторитетного `established_at`."
)
NON_IMPLICATION = (
    "Ця межа не визначає recording time, ingestion time, correction lineage або автентичність "
    "`occurred_at`; вона лише фіксує часову межу derivation над авторитетною transition history. "
    "Кардинальність applicability intervals лишається окремим відкритим Q9."
)
OTHER_OPEN_QUESTION_TOKENS = {
    "Q2": "Яка amendment model потрібна для зміни role або applicability після Establishment?",
    "Q4": "Чи потрібна окрема Role Taxonomy у Core?",
    "Q5": "Чи повинен Assignment мати окремий scope для частини складеного Resource",
    "Q7": "Чи потрібен окремий тип Assignment для coordination, approval або observation roles?",
    "Q8": "Як Constraint визначає конфлікт одночасних Assignment?",
    "Q9": Q9_TOKEN,
    "Q10": "Які provenance types повинні бути канонічними",
    "Q11": "Яка replacement policy визначає допустимі overlap і gap",
}
HISTORICALLY_RESOLVED_QUESTION_TOKENS = {
    "Q1": "Чи потрібен окремий фундаментальний Concept `Reservation`",
    "Q6": "Як представляти кількість Consumable Resource, зарезервовану або спожиту в Operation?",
}
EXPECTED_PRESSURE_RESOLUTIONS = frozenset(
    {
        "IN_PLACE_TRACEABLE_AMENDMENT",
        "SUPERSEDING_ASSIGNMENT_FOR_CHANGE",
        "POST_ESTABLISHMENT_IMMUTABILITY",
        "PROSPECTIVE_ONLY_SINGLE_INTERVAL",
        "PROSPECTIVE_ONLY_MULTIPLE_INTERVALS",
        "RETROACTIVE_ALLOWED_SINGLE_INTERVAL",
        "RETROACTIVE_ALLOWED_MULTIPLE_INTERVALS",
        "WHOLE_RESOURCE_ONLY",
        "EXPLICIT_PART_SCOPE_ON_ASSIGNMENT",
        "PART_AS_RESOURCE_IDENTITY",
    }
)
EXPECTED_NORM_SURVIVORS = frozenset(
    {
        "SUPERSEDING_ASSIGNMENT_FOR_CHANGE",
        "POST_ESTABLISHMENT_IMMUTABILITY",
        "PROSPECTIVE_ONLY_SINGLE_INTERVAL",
        "PROSPECTIVE_ONLY_MULTIPLE_INTERVALS",
        "WHOLE_RESOURCE_ONLY",
        "EXPLICIT_PART_SCOPE_ON_ASSIGNMENT",
    }
)
EXPECTED_HISTORICAL_HASHES = {
    "architecture/discovery/AD-035-assignment-stable-surface.md": "85a10e965faaa7ba65484efe08e985b7a04bf06712553c914673d65faf1df805",
    "architecture/discovery/AD-038-assignment-amendment-q2-attempt.md": "3e9311901a261bb297c13c93616f3c65421757e6a8468ef013875106a22df1c9",
    "architecture/assignment-amendment-q2-attempt.yaml": "05792d9211c7520604101f8d3e7655377805bb89e8bb6b6e9600da388c608299",
    "architecture/discovery/AD-039-assignment-temporal-scope-attempt.md": "310d2c3bb36b1c788e2573d42593f113066f344be1e9ee279901b1b8f6ce68dc",
    "architecture/assignment-temporal-scope-attempt.yaml": "4a8899d58ddf9edcf613760d330ff0003a3f982c1d6c188c4283c52fc364f7fb",
    "architecture/discovery/AD-040-assignment-consumer-compatibility.md": "3c6a551779f5592a56999c8b135f1e94bd0a9bd72a953b8b3094d953fd55eb99",
    "architecture/assignment-consumer-compatibility.yaml": "755f7b8520c85676669834bba2ef84f0de8c908d517f9278b8b7fde3f2dcfc1b",
    "architecture/discovery/AD-044-assignment-consumer-pressure.md": "078a615572c864478929f9abfef7ae1ee287ebe1cca4919a010fb375d8676a6e",
    "architecture/assignment-consumer-pressure.yaml": "d20f8b8330b4efdb6a23c09aa6f02b2182182ddd022486c370b11afb1d8f61b2",
    "architecture/discovery/AD-045-assignment-norm-compatibility.md": "7a1c25d22bdf3179ff552dc1635ded320a6220ec6a205da091c26188bd590020",
    "architecture/assignment-norm-compatibility.yaml": "6e32c5ed98df564c4cf23b1791bff86a80772ecd6be2135ab786d924ac4066dd",
}
EXPECTED_MAP_KEYS = frozenset(
    {
        "schema_version",
        "rule_owner",
        "baseline",
        "gate_first",
        "sufficiency_criterion",
        "evidence_ledger",
        "decision",
        "subject_transition",
        "current_projection",
        "superseded_source_quotes",
        "migration",
        "protected_historical_artifacts",
        "promotion_gate_guard",
        "forbidden_outcomes",
    }
)
EXPECTED_SUCCESSION_ROW_KEYS = frozenset(
    {
        "witness_path",
        "statement_id",
        "source_path",
        "section",
        "historical_quote",
        "current_successor_quote",
        "reason",
    }
)
EXPECTED_SUCCESSION_STATEMENT_IDS = frozenset(
    {
        "ASSIGNMENT_PROSPECTIVE_EFFECTIVITY_BOUNDARY",
        "AD045_SOURCE_SWEEP_Q3_OPEN_QUESTION",
    }
)
EXPECTED_FORBIDDEN_OUTCOMES = frozenset(
    {
        "Q2_CLOSURE",
        "Q5_CLOSURE",
        "Q9_CLOSURE",
        "TEMPORAL_BLOCKER_REMOVAL",
        "POSITIVE_MODEL_ACTIVATION",
        "ASSIGNMENT_SELECTION",
        "PROMOTION_CYCLE_START",
        "OCP005_PROMOTION",
        "ASSIGNMENT_CONCEPT_CANONICALIZATION",
        "T7_OPEN",
        "NEXT_ACT_AUTHORIZATION",
    }
)


@dataclass(frozen=True)
class AssignmentQ3LifecycleResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentQ3LifecycleResult:
    return AssignmentQ3LifecycleResult(tuple(dict.fromkeys(errors)))


def _load(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None


def load_q3_source_quote_successions(repo_root: Path) -> dict[str, dict[str, str]] | None:
    payload = _load(repo_root / MAP_PATH)
    rows = payload.get("superseded_source_quotes") if isinstance(payload, dict) else None
    if not isinstance(rows, list):
        return None
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        if (
            not isinstance(row, dict)
            or set(row) != EXPECTED_SUCCESSION_ROW_KEYS
            or any(not isinstance(value, str) or not value for value in row.values())
        ):
            return None
        statement_id = row["statement_id"]
        if statement_id in result:
            return None
        result[statement_id] = dict(row)
    return result


def _frontmatter(text: str) -> dict[str, Any] | None:
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


def _hash(path: Path) -> str | None:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def validate_assignment_q3_lifecycle(repo_root: Path) -> AssignmentQ3LifecycleResult:
    errors: list[str] = []
    payload = _load(repo_root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_MAP_KEYS:
        return _result((ASSIGNMENT_Q3_MAP_INVALID,))

    digest = hashlib.sha256(
        yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode("utf-8")
    ).hexdigest()
    if (
        digest != MAP_SHA256
        or payload.get("schema_version") != 2
        or payload.get("rule_owner") != "AD-046"
        or payload.get("baseline") != BASELINE
        or set(payload.get("forbidden_outcomes") or ()) != EXPECTED_FORBIDDEN_OUTCOMES
        or len(payload.get("forbidden_outcomes") or ()) != len(EXPECTED_FORBIDDEN_OUTCOMES)
    ):
        errors.append(ASSIGNMENT_Q3_MAP_INVALID)

    successions = load_q3_source_quote_successions(repo_root)
    if (
        successions is None
        or set(successions) != EXPECTED_SUCCESSION_STATEMENT_IDS
        or any(
            row.get("witness_path") != str(NORM_PATH)
            or row.get("source_path") != str(SUBJECT_PATH)
            for row in successions.values()
        )
    ):
        errors.append(ASSIGNMENT_Q3_MAP_INVALID)

    try:
        subject_text = (repo_root / SUBJECT_PATH).read_text(encoding="utf-8")
    except OSError:
        subject_text = ""
    metadata = _frontmatter(subject_text)
    questions = _section_lines(
        subject_text,
        "## 19. Open Questions and Resolved Boundaries",
        "## 20. Deferred Decisions",
    )
    q3_line = _question_line(questions, Q3_TOKEN)
    if (
        metadata is None
        or metadata.get("Document-ID") != "OCP-005"
        or str(metadata.get("Version")) != "0.3.0"
        or metadata.get("Status") != "Draft"
        or metadata.get("Concept-Status") != "Accepted"
        or subject_text.count(FINAL_BOUNDARY) != 1
        or subject_text.count(NON_IMPLICATION) != 1
        or not q3_line
        or f"~~{Q3_TOKEN}~~" not in q3_line
        or "AD-046/OCP-005 §8" not in q3_line
    ):
        errors.append(ASSIGNMENT_Q3_SUBJECT_DRIFT)

    if set(OTHER_OPEN_QUESTION_TOKENS) != {"Q2", "Q4", "Q5", "Q7", "Q8", "Q9", "Q10", "Q11"}:
        errors.append(ASSIGNMENT_Q3_PROJECTION_DRIFT)
    for token in OTHER_OPEN_QUESTION_TOKENS.values():
        line = _question_line(questions, token)
        if not line or "~~" in line:
            errors.append(ASSIGNMENT_Q3_PROJECTION_DRIFT)
            break
    if OTHER_OPEN_QUESTION_TOKENS.get("Q9") != Q9_TOKEN:
        errors.append(ASSIGNMENT_Q3_PROJECTION_DRIFT)
    if set(HISTORICALLY_RESOLVED_QUESTION_TOKENS) != {"Q1", "Q6"}:
        errors.append(ASSIGNMENT_Q3_PROJECTION_DRIFT)
    for token in HISTORICALLY_RESOLVED_QUESTION_TOKENS.values():
        line = _question_line(questions, token)
        if not line or "~~" not in line:
            errors.append(ASSIGNMENT_Q3_PROJECTION_DRIFT)
            break
    if len([line for line in questions if line.strip()]) != 11:
        errors.append(ASSIGNMENT_Q3_PROJECTION_DRIFT)

    surface = _load(repo_root / SURFACE_PATH)
    if not isinstance(surface, dict):
        errors.append(ASSIGNMENT_Q3_PROJECTION_DRIFT)
    else:
        surface_questions = {
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
        surface_subject = surface.get("subject")
        if (
            not isinstance(surface_subject, dict)
            or str(surface_subject.get("expected_version")) != "0.3.0"
            or surface_questions.get("Q3") != ("resolved-current", "outside-open-set")
            or surface_questions.get("Q9") != ("open", "blocks-whole-document-freeze")
            or moving.get("TEMPORAL_EFFECTIVITY_EXTENSION") != ["Q9"]
            or blockers.get("TEMPORAL_MODEL_UNRESOLVED") != ["Q9"]
            or blockers.get("AMENDMENT_MODEL_ABSENT") != ["Q2"]
            or blockers.get("PARTIAL_SCOPE_IDENTITY_UNRESOLVED") != ["Q5"]
        ):
            errors.append(ASSIGNMENT_Q3_PROJECTION_DRIFT)

    evidence = payload.get("evidence_ledger")
    if (
        not isinstance(evidence, list)
        or len(evidence) != 6
        or {item.get("evidence_mode") for item in evidence if isinstance(item, dict)}
        != {"analytic", "observed"}
        or {item.get("evidence_id") for item in evidence if isinstance(item, dict)}
        != {
            "CURRENT_OWNER_EFFECTIVITY_BOUNDARY",
            "EXECUTABLE_PRE_ESTABLISHMENT_CONTROL",
            "AD039_BASELINE_GAP_SEPARATION",
            "AD044_CONSUMER_PRESSURE",
            "AD045_SURVIVING_NORM_CLASSES",
            "ACCEPTED_CONSUMER_TIME_BOUNDARY",
        }
    ):
        errors.append(ASSIGNMENT_Q3_EVIDENCE_DRIFT)

    pressure = _load(repo_root / PRESSURE_PATH)
    pressure_ids = {
        item.get("resolution_id")
        for item in pressure.get("resolution_inventory", [])
        if isinstance(item, dict)
    } if isinstance(pressure, dict) else set()
    norm = _load(repo_root / NORM_PATH)
    norm_ids = {
        item.get("resolution_id")
        for item in norm.get("survivor_results", [])
        if isinstance(item, dict)
    } if isinstance(norm, dict) else set()
    if pressure_ids != EXPECTED_PRESSURE_RESOLUTIONS or norm_ids != EXPECTED_NORM_SURVIVORS:
        errors.append(ASSIGNMENT_Q3_EVIDENCE_DRIFT)

    try:
        fixture = load_fixture(repo_root / PROBE_FIXTURE)
        assignment = fixture.get("entity")
    except (OSError, ValueError, yaml.YAMLError):
        assignment = None
    if not isinstance(assignment, dict):
        errors.append(ASSIGNMENT_Q3_PROBE_DRIFT)
    else:
        controlled = dict(assignment)
        controlled["applicability_start"] = "2026-08-02T09:50:00Z"
        if (
            not validate_assignment(controlled).valid
            or assignment_effective_at(controlled, "2026-08-02T09:54:00Z") is not False
            or assignment_effective_at(controlled, "2026-08-02T09:55:00Z") is not True
        ):
            errors.append(ASSIGNMENT_Q3_PROBE_DRIFT)

    declared_historical = {
        item.get("path"): item.get("sha256")
        for item in payload.get("protected_historical_artifacts", [])
        if isinstance(item, dict)
    }
    if declared_historical != EXPECTED_HISTORICAL_HASHES or any(
        _hash(repo_root / historical_path(repo_root, Path(path), sha256)) != sha256
        for path, sha256 in EXPECTED_HISTORICAL_HASHES.items()
    ):
        errors.append(ASSIGNMENT_Q3_HISTORICAL_DRIFT)

    gate = _load(repo_root / GATE_PATH)
    cycles = gate.get("cycles") if isinstance(gate, dict) else None
    completed = [
        item.get("cycle_id")
        for item in cycles
        if isinstance(item, dict)
        and isinstance(item.get("steps"), dict)
        and set(item["steps"].values()) == {"completed"}
    ] if isinstance(cycles, list) else []
    protocol = gate.get("cycle_protocol") if isinstance(gate, dict) else None
    if (
        not isinstance(gate, dict)
        or gate.get("schema_version") != 5
        or completed != ["EVENT_T6"]
        or not isinstance(protocol, dict)
        or protocol.get("active_cycle_id") is not None
    ):
        errors.append(ASSIGNMENT_Q3_GATE_DRIFT)

    return _result(errors)
