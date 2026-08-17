from __future__ import annotations

import copy
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

from .checker import load_fixture, validate_assignment


ASSIGNMENT_AMENDMENT_Q2_MAP_INVALID = "ASSIGNMENT_AMENDMENT_Q2_MAP_INVALID"
ASSIGNMENT_AMENDMENT_Q2_OWNER_TEXT_DRIFT = "ASSIGNMENT_AMENDMENT_Q2_OWNER_TEXT_DRIFT"
ASSIGNMENT_AMENDMENT_Q2_CONSUMER_DRIFT = "ASSIGNMENT_AMENDMENT_Q2_CONSUMER_DRIFT"
ASSIGNMENT_AMENDMENT_Q2_PROBE_DRIFT = "ASSIGNMENT_AMENDMENT_Q2_PROBE_DRIFT"
ASSIGNMENT_AMENDMENT_Q2_PROJECTION_DRIFT = "ASSIGNMENT_AMENDMENT_Q2_PROJECTION_DRIFT"
ASSIGNMENT_AMENDMENT_Q2_GATE_DRIFT = "ASSIGNMENT_AMENDMENT_Q2_GATE_DRIFT"

MAP_KEYS = frozenset(
    {
        "schema_version",
        "rule_owner",
        "baseline",
        "gate_first",
        "subject",
        "hypothesis_result",
        "owner_text_evidence",
        "missing_obligations",
        "accepted_consumer_review",
        "executable_gap_probes",
        "preserved_assignment_projection",
        "promotion_gate_guard",
        "forbidden_outcomes",
    }
)
OWNER_EVIDENCE_IDS = frozenset(
    {
        "SUPERSESSION_OPTIONAL_RESOURCE_REPLACEMENT_ONLY",
        "ONLY_ENDPOINT_REFERENCES_IMMUTABLE",
        "TRACEABILITY_MODEL_EXPLICITLY_OPEN",
        "LIFECYCLE_HAS_NO_AMENDMENT_TRANSITION",
    }
)
MISSING_OBLIGATION_IDS = frozenset(
    {
        "ROLE_VALUE_IMMUTABILITY_AFTER_ESTABLISHMENT",
        "APPLICABILITY_VALUE_IMMUTABILITY_AFTER_ESTABLISHMENT",
        "SUPERSESSION_REQUIRED_FOR_ROLE_OR_APPLICABILITY_CHANGE",
        "AMENDMENT_PROVENANCE_BINDING",
    }
)
ACCEPTED_CONSUMER_IDS = frozenset({"OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021", "OCP-023"})
PROBE_IDS = frozenset(
    {"ESTABLISHED_ROLE_VALUE_REPLACEMENT", "ESTABLISHED_APPLICABILITY_VALUE_REPLACEMENT"}
)
UNCHANGED_PROBE_FIELDS = frozenset({"transition_history", "provenance_ref", "supersedes_assignment_ref"})
FORBIDDEN_OUTCOMES = frozenset(
    {
        "Q2_CLOSURE",
        "AB026_RESOLUTION",
        "ASSIGNMENT_AMENDMENT_RULE",
        "ASSIGNMENT_SELECTION",
        "PROMOTION_CYCLE_START",
        "OCP005_PROMOTION",
        "ASSIGNMENT_CONCEPT_CANONICALIZATION",
        "T7_OPEN",
    }
)

EXPECTED_GATE_FIRST = {
    "evidence_form": {
        "ocp016_gate": "G4",
        "applies": False,
        "reason": "negative-discovery-evidence-is-not-a-positive-capable-rule-result-or-profile",
    },
    "hypothetical_closure": {
        "ocp016_gate": "G4",
        "applies": True,
        "reason": "closure-would-add-positive-post-establishment-mutation-and-supersession-rules",
    },
}
EXPECTED_SUBJECT = {
    "document_id": "OCP-005",
    "primary": "docs/005-assignment-concept/README.md",
    "expected_version": "0.2.8",
    "expected_status": "Draft",
    "expected_concept_status": "Accepted",
    "question_id": "Q2",
    "question_state": "open",
    "question_classification": "blocks-whole-document-freeze",
    "blocker_id": "AMENDMENT_MODEL_ABSENT",
}
EXPECTED_HYPOTHESIS_RESULT = {
    "hypothesis_id": "Q2_SUPERSESSION_ONLY",
    "proposed_boundary": "no-separate-amendment-model-required",
    "result": "not-established",
    "q2_disposition": "remains-open",
    "blocker_disposition": "remains-blocking-whole-document-freeze",
    "reason": "current-owner-contract-does-not-make-role-or-applicability-immutable-or-require-supersession",
}
EXPECTED_OWNER_EVIDENCE = {
    "SUPERSESSION_OPTIONAL_RESOURCE_REPLACEMENT_ONLY": (
        "docs/005-assignment-concept/README.md",
        (
            "supersedes_assignment_ref [optional]",
            "Заміна Resource в Operation не змінює `resource_ref` існуючого Established Assignment.",
            "Новий Assignment може містити",
            "Supersession означає намір замінити попередній Assignment",
        ),
        "does-not-require-role-or-applicability-supersession",
    ),
    "ONLY_ENDPOINT_REFERENCES_IMMUTABLE": (
        "docs/005-assignment-concept/README.md",
        (
            "Після transition `Draft → Established` значення `resource_ref` та `operation_ref` є незмінними.",
            "Кожен Assignment у stage `Established`, `Closed` або `Revoked` має RoleSpecification",
            "Кожен Assignment у stage `Established`, `Closed` або `Revoked` має `applicability_start`.",
        ),
        "role-and-applicability-values-are-not-declared-immutable",
    ),
    "TRACEABILITY_MODEL_EXPLICITLY_OPEN": (
        "docs/005-assignment-concept/README.md",
        (
            "Зміна ролі або applicability після Establishment повинна бути простежуваною. Остаточна amendment model залишається відкритою.",
            "Яка amendment model потрібна для зміни role або applicability після Establishment?",
        ),
        "traceability-obligation-exists-without-a-selected-mechanism",
    ),
    "LIFECYCLE_HAS_NO_AMENDMENT_TRANSITION": (
        "docs/005-assignment-concept/README.md",
        (
            "Draft → Established",
            "Draft → Cancelled",
            "Established → Closed",
            "Established → Revoked",
            "AssignmentTransitionRecord",
        ),
        "current-history-can-trace-lifecycle-but-not-field-value-change",
    ),
}
EXPECTED_CONSUMERS = {
    "OCP-013": (
        "docs/013-resource-interchangeability/README.md",
        "Assignment mutation",
        "preserves-non-mutation-boundary",
    ),
    "OCP-015": (
        "docs/015-coordination-workflow/README.md",
        "alter Resource or Assignment identity",
        "preserves-assignment-identity",
    ),
    "OCP-017": (
        "docs/017-operation-lifecycle/README.md",
        "never edits an Assignment transition history",
        "consumes-current-truth-without-mutation-authority",
    ),
    "OCP-020": (
        "docs/020-quantitative-constraint-input/README.md",
        "create, amend, activate, suspend or terminate an Assignment",
        "explicitly-excludes-amendment-authority",
    ),
    "OCP-021": (
        "docs/021-reservation-allocation-boundary/README.md",
        "creates, blocks, cancels, supersedes or mutates an Assignment",
        "treats-assignment-truth-as-upstream-and-opaque",
    ),
    "OCP-023": (
        "docs/023-resource-occupancy/README.md",
        "Every Assignment must independently satisfy the current OCP-005 reference validator",
        "consumes-current-assignment-truth-without-amendment-authority",
    ),
}
EXPECTED_PROBES = {
    "ESTABLISHED_ROLE_VALUE_REPLACEMENT": (
        "role_specification.role_code",
        "executor",
        "support",
        True,
        True,
    ),
    "ESTABLISHED_APPLICABILITY_VALUE_REPLACEMENT": (
        "applicability_end",
        "2026-08-02T12:00:00Z",
        "2026-08-02T13:00:00Z",
        True,
        True,
    ),
}
EXPECTED_PROJECTION = {
    "witness": "architecture/assignment-stable-surface.yaml",
    "q2_state": "open",
    "q2_classification": "blocks-whole-document-freeze",
    "moving_surface": "AMENDMENT_AFTER_ESTABLISHMENT",
    "blocker_id": "AMENDMENT_MODEL_ABSENT",
}
EXPECTED_GATE_GUARD = {
    "schema_version": 5,
    "completed_cycle_ids": ["EVENT_T6"],
    "active_cycle_id": None,
}


@dataclass(frozen=True)
class AssignmentAmendmentQ2Result:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentAmendmentQ2Result:
    return AssignmentAmendmentQ2Result(tuple(dict.fromkeys(errors)))


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


def _references(value: Any) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(str(item).strip() for item in value if str(item).strip())
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    return ()


def _normalize_owner_evidence(value: Any) -> dict[str, tuple[str, tuple[str, ...], str]] | None:
    if not isinstance(value, list):
        return None
    result: dict[str, tuple[str, tuple[str, ...], str]] = {}
    for item in value:
        if not isinstance(item, dict) or set(item) != {"evidence_id", "path", "tokens", "consequence"}:
            return None
        evidence_id = item.get("evidence_id")
        tokens = item.get("tokens")
        if (
            not isinstance(evidence_id, str)
            or evidence_id in result
            or not isinstance(item.get("path"), str)
            or not isinstance(tokens, list)
            or not tokens
            or len(tokens) != len(set(tokens))
            or any(not isinstance(token, str) or not token for token in tokens)
        ):
            return None
        result[evidence_id] = (str(item["path"]), tuple(tokens), str(item.get("consequence")))
    return result


def _normalize_consumers(value: Any) -> dict[str, tuple[str, str, str]] | None:
    if not isinstance(value, list):
        return None
    result: dict[str, tuple[str, str, str]] = {}
    for item in value:
        if not isinstance(item, dict) or set(item) != {
            "document_id",
            "primary",
            "expected_status",
            "evidence_token",
            "requires_in_place_amendment",
            "consequence",
        }:
            return None
        document_id = item.get("document_id")
        if (
            not isinstance(document_id, str)
            or document_id in result
            or item.get("expected_status") != "Accepted"
            or item.get("requires_in_place_amendment") is not False
        ):
            return None
        result[document_id] = (
            str(item.get("primary")),
            str(item.get("evidence_token")),
            str(item.get("consequence")),
        )
    return result


def _normalize_probes(value: Any) -> dict[str, tuple[str, Any, Any, bool, bool]] | None:
    if not isinstance(value, dict) or set(value) != {"fixture", "unchanged_fields", "probes"}:
        return None
    if value.get("fixture") != "tools/ontology_checker/fixtures/assignment/valid-established.yaml":
        return None
    unchanged = value.get("unchanged_fields")
    if not isinstance(unchanged, list) or set(unchanged) != UNCHANGED_PROBE_FIELDS or len(unchanged) != len(UNCHANGED_PROBE_FIELDS):
        return None
    probes = value.get("probes")
    if not isinstance(probes, list):
        return None
    result: dict[str, tuple[str, Any, Any, bool, bool]] = {}
    for item in probes:
        if not isinstance(item, dict) or set(item) != {
            "probe_id",
            "field_path",
            "original_value",
            "replacement_value",
            "expected_original_valid",
            "expected_mutated_valid",
        }:
            return None
        probe_id = item.get("probe_id")
        if not isinstance(probe_id, str) or probe_id in result:
            return None
        result[probe_id] = (
            str(item.get("field_path")),
            item.get("original_value"),
            item.get("replacement_value"),
            item.get("expected_original_valid") is True,
            item.get("expected_mutated_valid") is True,
        )
    return result


def _nested_get(value: dict[str, Any], field_path: str) -> Any:
    current: Any = value
    for part in field_path.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(part)
    return current


def _nested_set(value: dict[str, Any], field_path: str, replacement: Any) -> None:
    current: dict[str, Any] = value
    parts = field_path.split(".")
    for part in parts[:-1]:
        child = current.get(part)
        if not isinstance(child, dict):
            return
        current = child
    current[parts[-1]] = replacement


def _canonical_probe_value(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    return value


def validate_assignment_amendment_q2(repo_root: Path) -> AssignmentAmendmentQ2Result:
    errors: list[str] = []
    try:
        payload = yaml.safe_load(
            (repo_root / "architecture/assignment-amendment-q2-attempt.yaml").read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        return _result((ASSIGNMENT_AMENDMENT_Q2_MAP_INVALID,))
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((ASSIGNMENT_AMENDMENT_Q2_MAP_INVALID,))

    if (
        payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-038"
        or payload.get("baseline") != "448d7d10fe3a3213da8479ce991995e01102cf3b"
        or payload.get("gate_first") != EXPECTED_GATE_FIRST
        or payload.get("subject") != EXPECTED_SUBJECT
        or payload.get("hypothesis_result") != EXPECTED_HYPOTHESIS_RESULT
        or set(payload.get("missing_obligations") or ()) != MISSING_OBLIGATION_IDS
        or len(payload.get("missing_obligations") or ()) != len(MISSING_OBLIGATION_IDS)
        or payload.get("preserved_assignment_projection") != EXPECTED_PROJECTION
        or payload.get("promotion_gate_guard") != EXPECTED_GATE_GUARD
        or set(payload.get("forbidden_outcomes") or ()) != FORBIDDEN_OUTCOMES
        or len(payload.get("forbidden_outcomes") or ()) != len(FORBIDDEN_OUTCOMES)
    ):
        errors.append(ASSIGNMENT_AMENDMENT_Q2_MAP_INVALID)

    subject_path = repo_root / EXPECTED_SUBJECT["primary"]
    subject_metadata = _frontmatter(subject_path)
    try:
        subject_text = subject_path.read_text(encoding="utf-8")
    except OSError:
        subject_text = ""
    q2_line = next(
        (line for line in subject_text.splitlines() if EXPECTED_SUBJECT["question_id"] == "Q2" and "Яка amendment model потрібна" in line),
        "",
    )
    if (
        subject_metadata is None
        or subject_metadata.get("Document-ID") != "OCP-005"
        or str(subject_metadata.get("Version")) != "0.2.8"
        or subject_metadata.get("Status") != "Draft"
        or subject_metadata.get("Concept-Status") != "Accepted"
        or not q2_line
        or "~~" in q2_line
    ):
        errors.append(ASSIGNMENT_AMENDMENT_Q2_PROJECTION_DRIFT)

    evidence = _normalize_owner_evidence(payload.get("owner_text_evidence"))
    if evidence != EXPECTED_OWNER_EVIDENCE or set(evidence or {}) != OWNER_EVIDENCE_IDS:
        errors.append(ASSIGNMENT_AMENDMENT_Q2_OWNER_TEXT_DRIFT)
    else:
        for relative, tokens, _ in evidence.values():
            try:
                text = (repo_root / relative).read_text(encoding="utf-8")
            except OSError:
                text = ""
            if any(token not in text for token in tokens):
                errors.append(ASSIGNMENT_AMENDMENT_Q2_OWNER_TEXT_DRIFT)
                break

    consumers = _normalize_consumers(payload.get("accepted_consumer_review"))
    if consumers != EXPECTED_CONSUMERS or set(consumers or {}) != ACCEPTED_CONSUMER_IDS:
        errors.append(ASSIGNMENT_AMENDMENT_Q2_CONSUMER_DRIFT)
    actual_accepted: set[str] = set()
    for primary in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(primary)
        if metadata is None:
            continue
        if "OCP-005" in _references(metadata.get("Depends-On")) and metadata.get("Status") in {"Accepted", "Canonical"}:
            actual_accepted.add(str(metadata.get("Document-ID")))
    if actual_accepted != ACCEPTED_CONSUMER_IDS:
        errors.append(ASSIGNMENT_AMENDMENT_Q2_CONSUMER_DRIFT)
    if consumers is not None:
        for document_id, (relative, token, _) in consumers.items():
            metadata = _frontmatter(repo_root / relative)
            try:
                text = (repo_root / relative).read_text(encoding="utf-8")
            except OSError:
                text = ""
            if (
                metadata is None
                or metadata.get("Document-ID") != document_id
                or metadata.get("Status") != "Accepted"
                or "OCP-005" not in _references(metadata.get("Depends-On"))
                or token not in text
            ):
                errors.append(ASSIGNMENT_AMENDMENT_Q2_CONSUMER_DRIFT)

    probes = _normalize_probes(payload.get("executable_gap_probes"))
    if probes != EXPECTED_PROBES or set(probes or {}) != PROBE_IDS:
        errors.append(ASSIGNMENT_AMENDMENT_Q2_PROBE_DRIFT)
    else:
        try:
            fixture = load_fixture(
                repo_root / "tools/ontology_checker/fixtures/assignment/valid-established.yaml"
            )
            original = fixture.get("entity")
        except (OSError, ValueError, yaml.YAMLError):
            original = None
        if not isinstance(original, dict):
            errors.append(ASSIGNMENT_AMENDMENT_Q2_PROBE_DRIFT)
        else:
            original_unchanged = {key: copy.deepcopy(original.get(key)) for key in UNCHANGED_PROBE_FIELDS}
            for field_path, old, new, expected_original, expected_mutated in probes.values():
                mutated = copy.deepcopy(original)
                if _canonical_probe_value(_nested_get(mutated, field_path)) != old:
                    errors.append(ASSIGNMENT_AMENDMENT_Q2_PROBE_DRIFT)
                    continue
                _nested_set(mutated, field_path, new)
                if (
                    validate_assignment(original).valid is not expected_original
                    or validate_assignment(mutated).valid is not expected_mutated
                    or any(mutated.get(key) != value for key, value in original_unchanged.items())
                ):
                    errors.append(ASSIGNMENT_AMENDMENT_Q2_PROBE_DRIFT)

    try:
        surface = yaml.safe_load(
            (repo_root / EXPECTED_PROJECTION["witness"]).read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        surface = None
    if not isinstance(surface, dict):
        errors.append(ASSIGNMENT_AMENDMENT_Q2_PROJECTION_DRIFT)
    else:
        questions = surface.get("open_question_inventory")
        q2 = next(
            (item for item in questions if isinstance(item, dict) and item.get("question_id") == "Q2"),
            None,
        ) if isinstance(questions, list) else None
        moving = surface.get("moving_surfaces")
        q2_surface = next(
            (item for item in moving if isinstance(item, dict) and item.get("surface_id") == "AMENDMENT_AFTER_ESTABLISHMENT"),
            None,
        ) if isinstance(moving, list) else None
        blockers = surface.get("blockers")
        q2_blocker = next(
            (item for item in blockers if isinstance(item, dict) and item.get("blocker_id") == "AMENDMENT_MODEL_ABSENT"),
            None,
        ) if isinstance(blockers, list) else None
        if (
            q2 is None
            or q2.get("state") != "open"
            or q2.get("classification") != "blocks-whole-document-freeze"
            or q2_surface is None
            or q2_surface.get("disposition") != "moving"
            or q2_surface.get("question_ids") != ["Q2"]
            or q2_blocker is None
            or q2_blocker.get("disposition") != "blocks-whole-document-freeze"
            or q2_blocker.get("question_ids") != ["Q2"]
        ):
            errors.append(ASSIGNMENT_AMENDMENT_Q2_PROJECTION_DRIFT)

    try:
        gate = yaml.safe_load(
            (repo_root / "architecture/foundation-promotion-gate.yaml").read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        gate = None
    if not isinstance(gate, dict):
        errors.append(ASSIGNMENT_AMENDMENT_Q2_GATE_DRIFT)
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
        if (
            gate.get("schema_version") != 5
            or completed != ["EVENT_T6"]
            or not isinstance(protocol, dict)
            or protocol.get("active_cycle_id") is not None
        ):
            errors.append(ASSIGNMENT_AMENDMENT_Q2_GATE_DRIFT)

    return _result(errors)
