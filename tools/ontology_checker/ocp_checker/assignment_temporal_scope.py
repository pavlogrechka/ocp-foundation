from __future__ import annotations

import copy
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

from .assignment_q3_lifecycle import load_q3_source_quote_successions
from .checker import assignment_effective_at, load_fixture, validate_assignment
from .foundation_promotion_gate import promotion_gate_guard_is_current


ASSIGNMENT_TEMPORAL_SCOPE_MAP_INVALID = "ASSIGNMENT_TEMPORAL_SCOPE_MAP_INVALID"
ASSIGNMENT_TEMPORAL_SCOPE_OWNER_TEXT_DRIFT = "ASSIGNMENT_TEMPORAL_SCOPE_OWNER_TEXT_DRIFT"
ASSIGNMENT_TEMPORAL_SCOPE_PROBE_DRIFT = "ASSIGNMENT_TEMPORAL_SCOPE_PROBE_DRIFT"
ASSIGNMENT_TEMPORAL_SCOPE_PROJECTION_DRIFT = "ASSIGNMENT_TEMPORAL_SCOPE_PROJECTION_DRIFT"
ASSIGNMENT_TEMPORAL_SCOPE_GATE_DRIFT = "ASSIGNMENT_TEMPORAL_SCOPE_GATE_DRIFT"

MAP_KEYS = frozenset(
    {
        "schema_version",
        "rule_owner",
        "baseline",
        "gate_first",
        "subject",
        "zone_results",
        "owner_text_evidence",
        "missing_obligations",
        "executable_gap_probes",
        "preserved_assignment_projection",
        "promotion_gate_guard",
        "forbidden_outcomes",
    }
)
OWNER_EVIDENCE_IDS = frozenset(
    {
        "PRE_ESTABLISHMENT_EFFECTIVITY_ALREADY_FALSE",
        "NO_ESTABLISHMENT_RECORDING_TIME_AXIS",
        "SINGLE_INTERVAL_MINIMUM_IS_NOT_CLOSED_WORLD",
        "DIRECT_REFERENCE_NON_INHERITANCE_ONLY",
        "ONE_RESOURCE_REFERENCE_IS_NOT_PART_IDENTITY",
        "PARTIAL_SCOPE_QUESTION_EXPLICITLY_OPEN",
    }
)
TEMPORAL_OBLIGATION_IDS = frozenset(
    {
        "ESTABLISHMENT_RECORDING_TIME_AXIS",
        "RETROACTIVE_ESTABLISHMENT_PROHIBITION_OR_RULE",
        "CLOSED_WORLD_APPLICABILITY_INTERVAL_CARDINALITY",
        "MULTI_INTERVAL_REPRESENTATION_OR_SEPARATE_ASSIGNMENT_RULE",
    }
)
PARTIAL_SCOPE_OBLIGATION_IDS = frozenset(
    {
        "PARTIAL_SCOPE_FIELD_PROHIBITION_OR_SCHEMA",
        "COMPOSITE_PART_SUBJECT_IDENTITY_RULE",
        "PARTIAL_SCOPE_DERIVATION_AND_PROVENANCE",
    }
)
PROBE_IDS = frozenset(
    {
        "RETROACTIVE_ESTABLISHMENT_BACKDATE",
        "MULTIPLE_APPLICABILITY_INTERVAL_EXTENSION",
        "PARTIAL_COMPOSITE_RESOURCE_SCOPE_EXTENSION",
    }
)
QUESTION_IDS = frozenset({"Q3", "Q9", "Q5"})
FORBIDDEN_OUTCOMES = frozenset(
    {
        "Q3_CLOSURE",
        "Q9_CLOSURE",
        "Q5_CLOSURE",
        "ASSIGNMENT_TEMPORAL_RULE",
        "ASSIGNMENT_PARTIAL_SCOPE_RULE",
        "ASSIGNMENT_SELECTION",
        "PROMOTION_CYCLE_START",
        "OCP005_PROMOTION",
        "ASSIGNMENT_CONCEPT_CANONICALIZATION",
        "T7_OPEN",
    }
)

EXPECTED_IDENTITY = {
    "schema_version": 1,
    "rule_owner": "AD-039",
    "baseline": "94820489c7e6de17bc7eb1439a1c3dd78bfbc14f",
}
EXPECTED_GATE_FIRST = {
    "evidence_form": {
        "ocp016_gate": "G4",
        "applies": False,
        "reason": "negative-discovery-evidence-is-not-a-positive-capable-rule-result-or-profile",
    },
    "hypothetical_closures": {
        "temporal": {
            "ocp016_gate": "G4",
            "applies": True,
            "reason": "closure-would-add-retroactivity-and-interval-cardinality-rules",
        },
        "partial_scope": {
            "ocp016_gate": "G4",
            "applies": True,
            "reason": "closure-would-add-composite-part-identity-and-scope-rules",
        },
    },
}
EXPECTED_SUBJECT = {
    "document_id": "OCP-005",
    "primary": "docs/005-assignment-concept/README.md",
    "expected_version": "1.0.0",
    "expected_status": "Canonical",
    "expected_concept_status": "Accepted",
}
EXPECTED_ZONE_RESULTS = {
    "temporal": {
        "question_ids": ["Q3", "Q9"],
        "result": "not-established",
        "question_disposition": "remain-open",
        "blocker_id": "TEMPORAL_MODEL_UNRESOLVED",
        "blocker_disposition": "remains-blocking-whole-document-freeze",
        "existing_boundary": "effectivity-before-established-at-is-false",
        "missing_boundaries": [
            "retroactive-establishment-recording",
            "multiple-applicability-interval-cardinality",
        ],
    },
    "partial_scope": {
        "question_ids": ["Q5"],
        "result": "not-established",
        "question_disposition": "remain-open",
        "blocker_id": "PARTIAL_SCOPE_IDENTITY_UNRESOLVED",
        "blocker_disposition": "remains-blocking-whole-document-freeze",
        "existing_boundary": "composition-does-not-auto-create-component-assignments",
        "missing_boundaries": ["partial-composite-resource-scope-identity"],
    },
}
EXPECTED_OWNER_EVIDENCE = {
    "PRE_ESTABLISHMENT_EFFECTIVITY_ALREADY_FALSE": (
        "temporal",
        "docs/005-assignment-concept/README.md",
        (
            "established_at(Assignment) <= t",
            "До окремого рішення про ретроактивне Establishment Assignment не може бути ефективним для часу раніше `established_at`.",
        ),
        "controls-effectivity-before-the-recorded-establishment-instant-only",
    ),
    "NO_ESTABLISHMENT_RECORDING_TIME_AXIS": (
        "temporal",
        "docs/005-assignment-concept/README.md",
        (
            "occurred_at of the unique Draft → Established record",
            "AssignmentTransitionRecord",
            "provenance_ref",
            "Чи допускається ретроактивне Establishment Assignment?",
        ),
        "cannot-distinguish-original-from-later-backdated-establishment-record",
    ),
    "SINGLE_INTERVAL_MINIMUM_IS_NOT_CLOSED_WORLD": (
        "temporal",
        "docs/005-assignment-concept/README.md",
        (
            "applicability_start",
            "applicability_end [optional]",
            "Цей перелік визначає мінімальні перевірні поля Concept, але не є схемою бази даних чи API.",
            "Чи може один Assignment мати кілька неперервних applicability intervals",
        ),
        "singular-minimum-does-not-prohibit-an-additional-interval-representation",
    ),
    "DIRECT_REFERENCE_NON_INHERITANCE_ONLY": (
        "partial_scope",
        "docs/005-assignment-concept/README.md",
        (
            "Assignment застосовується лише до Resource та Operation, указаних безпосередньо в його references.",
            "Assignment складеного Resource не створює Assignment для його складових Resource",
            "Механізми явного успадкування або масового створення Assignment можуть бути визначені окремими правилами",
        ),
        "rejects-automatic-component-assignment-inference-not-explicit-partial-scope",
    ),
    "ONE_RESOURCE_REFERENCE_IS_NOT_PART_IDENTITY": (
        "partial_scope",
        "docs/005-assignment-concept/README.md",
        (
            "один Assignment не може групувати кілька Resource або кілька Operation.",
            "один Resource, який сам представляє визначену групу",
            "окремий Assignment для кожного Resource.",
        ),
        "grouping-boundary-does-not-decide-subject-identity-for-a-part",
    ),
    "PARTIAL_SCOPE_QUESTION_EXPLICITLY_OPEN": (
        "partial_scope",
        "docs/005-assignment-concept/README.md",
        (
            "Чи повинен Assignment мати окремий scope для частини складеного Resource без створення нового Resource?",
        ),
        "owner-contract-does-not-select-prohibition-or-positive-scope-form",
    ),
}
EXPECTED_CONTROL = {
    "probe_id": "PRE_ESTABLISHMENT_EFFECTIVITY_FALSE",
    "applicability_start": "2026-08-02T09:50:00Z",
    "query_time": "2026-08-02T09:54:00Z",
    "expected_assignment_valid": True,
    "expected_effective": False,
}
EXPECTED_PROBE_FIXTURE = "tools/ontology_checker/fixtures/assignment/valid-established.yaml"
EXPECTED_PROBES = {
    "RETROACTIVE_ESTABLISHMENT_BACKDATE": {
        "zone": "temporal",
        "mutation": "backdate-establishment",
        "original_value": "2026-08-02T09:55:00Z",
        "replacement_value": "2026-08-02T09:52:00Z",
        "expected_original_valid": True,
        "expected_mutated_valid": True,
    },
    "MULTIPLE_APPLICABILITY_INTERVAL_EXTENSION": {
        "zone": "temporal",
        "mutation": "add-multiple-intervals",
        "replacement_value": [
            {"start": "2026-08-02T10:00:00Z", "end": "2026-08-02T10:30:00Z"},
            {"start": "2026-08-02T11:00:00Z", "end": "2026-08-02T12:00:00Z"},
        ],
        "expected_original_valid": True,
        "expected_mutated_valid": True,
    },
    "PARTIAL_COMPOSITE_RESOURCE_SCOPE_EXTENSION": {
        "zone": "partial_scope",
        "mutation": "add-partial-scope",
        "replacement_value": {"kind": "component", "component_ref": "R-COMPONENT-001"},
        "expected_original_valid": True,
        "expected_mutated_valid": True,
    },
}
EXPECTED_PROJECTION = {
    "witness": "architecture/assignment-stable-surface.yaml",
    "questions": {
        "Q3": "blocks-whole-document-freeze",
        "Q9": "blocks-whole-document-freeze",
        "Q5": "blocks-whole-document-freeze",
    },
    "moving_surfaces": {
        "TEMPORAL_EFFECTIVITY_EXTENSION": ["Q3", "Q9"],
        "COMPOSITE_RESOURCE_SCOPE": ["Q5"],
    },
    "blockers": {
        "TEMPORAL_MODEL_UNRESOLVED": ["Q3", "Q9"],
        "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": ["Q5"],
    },
}
CURRENT_PROJECTION = {
    "witness": "architecture/assignment-stable-surface.yaml",
    "questions": {
        "Q9": "blocks-whole-document-freeze",
        "Q5": "blocks-whole-document-freeze",
    },
    "moving_surfaces": {
        "TEMPORAL_EFFECTIVITY_EXTENSION": ["Q9"],
        "COMPOSITE_RESOURCE_SCOPE": ["Q5"],
    },
    "blockers": {
        "TEMPORAL_MODEL_UNRESOLVED": ["Q9"],
        "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": ["Q5"],
    },
}
@dataclass(frozen=True)
class AssignmentTemporalScopeResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentTemporalScopeResult:
    return AssignmentTemporalScopeResult(tuple(dict.fromkeys(errors)))


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


def _section(text: str, heading: str) -> str | None:
    marker = f"## {heading}"
    lines = text.splitlines()
    starts = [index for index, line in enumerate(lines) if line == marker]
    if len(starts) != 1:
        return None
    start = starts[0]
    end = next(
        (index for index in range(start + 1, len(lines)) if lines[index].startswith("## ")),
        len(lines),
    )
    return "\n".join(lines[start:end])


def _canonical_time(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    return value


def _normalize_evidence(value: Any) -> dict[str, tuple[str, str, tuple[str, ...], str]] | None:
    if not isinstance(value, list):
        return None
    result: dict[str, tuple[str, str, tuple[str, ...], str]] = {}
    expected_keys = {"evidence_id", "zone", "path", "tokens", "consequence"}
    for item in value:
        if not isinstance(item, dict) or set(item) != expected_keys:
            return None
        evidence_id = item.get("evidence_id")
        tokens = item.get("tokens")
        if (
            not isinstance(evidence_id, str)
            or evidence_id in result
            or item.get("zone") not in {"temporal", "partial_scope"}
            or not isinstance(item.get("path"), str)
            or not isinstance(tokens, list)
            or not tokens
            or len(tokens) != len(set(tokens))
            or any(not isinstance(token, str) or not token for token in tokens)
        ):
            return None
        result[evidence_id] = (
            str(item["zone"]),
            str(item["path"]),
            tuple(tokens),
            str(item.get("consequence")),
        )
    return result


def _normalize_probes(value: Any) -> tuple[dict[str, Any], dict[str, dict[str, Any]]] | None:
    if not isinstance(value, dict) or set(value) != {"fixture", "control", "probes"}:
        return None
    if value.get("fixture") != EXPECTED_PROBE_FIXTURE:
        return None
    control = value.get("control")
    probes = value.get("probes")
    if not isinstance(control, dict) or not isinstance(probes, list):
        return None
    result: dict[str, dict[str, Any]] = {}
    for item in probes:
        if not isinstance(item, dict):
            return None
        probe_id = item.get("probe_id")
        if not isinstance(probe_id, str) or probe_id in result:
            return None
        result[probe_id] = {key: copy.deepcopy(child) for key, child in item.items() if key != "probe_id"}
    return copy.deepcopy(control), result


def _mutated_probe(original: dict[str, Any], probe_id: str, probe: dict[str, Any]) -> dict[str, Any]:
    mutated = copy.deepcopy(original)
    if probe_id == "RETROACTIVE_ESTABLISHMENT_BACKDATE":
        mutated["transition_history"][0]["occurred_at"] = probe["replacement_value"]
        mutated["established_at"] = probe["replacement_value"]
    elif probe_id == "MULTIPLE_APPLICABILITY_INTERVAL_EXTENSION":
        mutated["applicability_intervals"] = copy.deepcopy(probe["replacement_value"])
    elif probe_id == "PARTIAL_COMPOSITE_RESOURCE_SCOPE_EXTENSION":
        mutated["resource_scope"] = copy.deepcopy(probe["replacement_value"])
    return mutated


def validate_assignment_temporal_scope(repo_root: Path) -> AssignmentTemporalScopeResult:
    errors: list[str] = []
    try:
        payload = yaml.safe_load(
            (repo_root / "architecture/assignment-temporal-scope-attempt.yaml").read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        return _result((ASSIGNMENT_TEMPORAL_SCOPE_MAP_INVALID,))
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((ASSIGNMENT_TEMPORAL_SCOPE_MAP_INVALID,))

    obligations = payload.get("missing_obligations")
    if (
        any(payload.get(key) != value for key, value in EXPECTED_IDENTITY.items())
        or payload.get("gate_first") != EXPECTED_GATE_FIRST
        or payload.get("subject") != EXPECTED_SUBJECT
        or payload.get("zone_results") != EXPECTED_ZONE_RESULTS
        or not isinstance(obligations, dict)
        or set(obligations) != {"temporal", "partial_scope"}
        or set(obligations.get("temporal") or ()) != TEMPORAL_OBLIGATION_IDS
        or len(obligations.get("temporal") or ()) != len(TEMPORAL_OBLIGATION_IDS)
        or set(obligations.get("partial_scope") or ()) != PARTIAL_SCOPE_OBLIGATION_IDS
        or len(obligations.get("partial_scope") or ()) != len(PARTIAL_SCOPE_OBLIGATION_IDS)
        or payload.get("preserved_assignment_projection") != EXPECTED_PROJECTION
        or set(payload.get("promotion_gate_guard") or {}) != {"schema_version", "completed_cycle_ids", "active_cycle_id"}
        or set(payload.get("forbidden_outcomes") or ()) != FORBIDDEN_OUTCOMES
        or len(payload.get("forbidden_outcomes") or ()) != len(FORBIDDEN_OUTCOMES)
    ):
        errors.append(ASSIGNMENT_TEMPORAL_SCOPE_MAP_INVALID)

    subject_path = repo_root / EXPECTED_SUBJECT["primary"]
    subject_metadata = _frontmatter(subject_path)
    try:
        subject_text = subject_path.read_text(encoding="utf-8")
    except OSError:
        subject_text = ""
    question_tokens = {
        "Q3": "Чи допускається ретроактивне Establishment Assignment?",
        "Q9": "Чи може один Assignment мати кілька неперервних applicability intervals",
        "Q5": "Чи повинен Assignment мати окремий scope для частини складеного Resource",
    }
    question_lines = {
        question_id: next((line for line in subject_text.splitlines() if token in line), "")
        for question_id, token in question_tokens.items()
    }
    if (
        subject_metadata is None
        or subject_metadata.get("Document-ID") != "OCP-005"
        or str(subject_metadata.get("Version")) != "1.0.0"
        or subject_metadata.get("Status") != "Canonical"
        or subject_metadata.get("Concept-Status") != "Accepted"
        or set(question_lines) != QUESTION_IDS
        or not question_lines.get("Q3")
        or "~~" not in question_lines["Q3"]
        or any(
            not question_lines.get(question_id) or "~~" in question_lines[question_id]
            for question_id in ("Q9", "Q5")
        )
    ):
        errors.append(ASSIGNMENT_TEMPORAL_SCOPE_PROJECTION_DRIFT)

    evidence = _normalize_evidence(payload.get("owner_text_evidence"))
    succession_rows = load_q3_source_quote_successions(repo_root)
    succession_by_source = {
        (row["source_path"], row["historical_quote"]): (
            row["section"],
            row["current_successor_quote"],
        )
        for row in succession_rows.values()
    } if succession_rows is not None else {}
    if evidence != EXPECTED_OWNER_EVIDENCE or set(evidence or {}) != OWNER_EVIDENCE_IDS:
        errors.append(ASSIGNMENT_TEMPORAL_SCOPE_OWNER_TEXT_DRIFT)
    else:
        for _, relative, tokens, _ in evidence.values():
            try:
                text = (repo_root / relative).read_text(encoding="utf-8")
            except OSError:
                text = ""
            unresolved = False
            for token in tokens:
                if token in text:
                    continue
                successor = succession_by_source.get((relative, token))
                if successor is None:
                    unresolved = True
                    break
                section_name, current_quote = successor
                section = _section(text, section_name)
                if section is None or section.count(current_quote) != 1:
                    unresolved = True
                    break
            if unresolved:
                errors.append(ASSIGNMENT_TEMPORAL_SCOPE_OWNER_TEXT_DRIFT)
                break

    normalized = _normalize_probes(payload.get("executable_gap_probes"))
    if normalized is None:
        errors.append(ASSIGNMENT_TEMPORAL_SCOPE_PROBE_DRIFT)
    else:
        control, probes = normalized
        if control != EXPECTED_CONTROL or probes != EXPECTED_PROBES or set(probes) != PROBE_IDS:
            errors.append(ASSIGNMENT_TEMPORAL_SCOPE_PROBE_DRIFT)
        try:
            fixture = load_fixture(
                repo_root / EXPECTED_PROBE_FIXTURE
            )
            original = fixture.get("entity")
        except (OSError, ValueError, yaml.YAMLError):
            original = None
        if not isinstance(original, dict):
            errors.append(ASSIGNMENT_TEMPORAL_SCOPE_PROBE_DRIFT)
        elif control == EXPECTED_CONTROL and probes == EXPECTED_PROBES:
            controlled = copy.deepcopy(original)
            controlled["applicability_start"] = control["applicability_start"]
            if (
                validate_assignment(controlled).valid is not control["expected_assignment_valid"]
                or assignment_effective_at(controlled, control["query_time"]) is not control["expected_effective"]
            ):
                errors.append(ASSIGNMENT_TEMPORAL_SCOPE_PROBE_DRIFT)
            for probe_id, probe in probes.items():
                if probe_id == "RETROACTIVE_ESTABLISHMENT_BACKDATE" and (
                    _canonical_time(original["transition_history"][0].get("occurred_at"))
                    != probe.get("original_value")
                    or _canonical_time(original.get("established_at")) != probe.get("original_value")
                ):
                    errors.append(ASSIGNMENT_TEMPORAL_SCOPE_PROBE_DRIFT)
                    continue
                mutated = _mutated_probe(original, probe_id, probe)
                if (
                    validate_assignment(original).valid is not probe["expected_original_valid"]
                    or validate_assignment(mutated).valid is not probe["expected_mutated_valid"]
                ):
                    errors.append(ASSIGNMENT_TEMPORAL_SCOPE_PROBE_DRIFT)

    try:
        surface = yaml.safe_load(
            (repo_root / CURRENT_PROJECTION["witness"]).read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        surface = None
    if not isinstance(surface, dict):
        errors.append(ASSIGNMENT_TEMPORAL_SCOPE_PROJECTION_DRIFT)
    else:
        questions = surface.get("open_question_inventory")
        moving = surface.get("moving_surfaces")
        blockers = surface.get("blockers")
        actual_questions = {
            item.get("question_id"): item.get("classification")
            for item in questions or []
            if isinstance(item, dict) and item.get("question_id") in QUESTION_IDS and item.get("state") == "open"
        }
        actual_moving = {
            item.get("surface_id"): item.get("question_ids")
            for item in moving or []
            if isinstance(item, dict) and item.get("surface_id") in CURRENT_PROJECTION["moving_surfaces"]
        }
        actual_blockers = {
            item.get("blocker_id"): item.get("question_ids")
            for item in blockers or []
            if isinstance(item, dict)
            and item.get("blocker_id") in CURRENT_PROJECTION["blockers"]
            and item.get("disposition") == "blocks-whole-document-freeze"
        }
        if (
            actual_questions != CURRENT_PROJECTION["questions"]
            or actual_moving != CURRENT_PROJECTION["moving_surfaces"]
            or actual_blockers != CURRENT_PROJECTION["blockers"]
        ):
            errors.append(ASSIGNMENT_TEMPORAL_SCOPE_PROJECTION_DRIFT)

    try:
        gate = yaml.safe_load(
            (repo_root / "architecture/foundation-promotion-gate.yaml").read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        gate = None
    if not isinstance(gate, dict):
        errors.append(ASSIGNMENT_TEMPORAL_SCOPE_GATE_DRIFT)
    else:
        cycles = gate.get("cycles")
        completed = [
            item.get("cycle_id")
            for item in cycles
            if isinstance(item, dict)
            and isinstance(item.get("steps"), dict)
            and set(item["steps"].values()) == {"completed"}
        ] if isinstance(cycles, list) else []
        protocol = gate.get("cycle_protocol")
        if not isinstance(protocol, dict) or not promotion_gate_guard_is_current(gate, payload.get("promotion_gate_guard")):
            errors.append(ASSIGNMENT_TEMPORAL_SCOPE_GATE_DRIFT)

    return _result(errors)
