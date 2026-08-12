from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any, Iterable

import yaml


EVENT_STABLE_SURFACE_MAP_INVALID = "EVENT_STABLE_SURFACE_MAP_INVALID"
EVENT_STABLE_SURFACE_SUBJECT_DRIFT = "EVENT_STABLE_SURFACE_SUBJECT_DRIFT"
EVENT_STABLE_SURFACE_DEPENDENCY_DRIFT = "EVENT_STABLE_SURFACE_DEPENDENCY_DRIFT"
EVENT_STABLE_SURFACE_CONSUMER_DRIFT = "EVENT_STABLE_SURFACE_CONSUMER_DRIFT"
EVENT_STABLE_SURFACE_EVIDENCE_DRIFT = "EVENT_STABLE_SURFACE_EVIDENCE_DRIFT"
EVENT_STABLE_SURFACE_NEXT_GATE_REQUIRED = "EVENT_STABLE_SURFACE_NEXT_GATE_REQUIRED"

DIRECT_DEPENDENCY_IDS = frozenset(
    {"OCP-000", "OCP-001", "OCP-002", "OCP-004", "OCP-008", "AD-006", "P-001"}
)
DIRECT_DEPENDENCY_ORDER = (
    "OCP-000", "OCP-001", "OCP-002", "OCP-004", "OCP-008", "AD-006", "P-001"
)
DIRECT_CONSUMER_IDS = frozenset({"OCP-011", "OCP-017"})
DIRECT_CONSUMER_ORDER = ("OCP-011", "OCP-017")
BINDING_KINDS = frozenset(
    {"unversioned-document", "unversioned-decision", "unversioned-pattern-plus-exact-use"}
)
STABLE_SURFACE_IDS = frozenset(
    {
        "EVENT_IDENTITY_KERNEL",
        "OBSERVATION_RECORD_KERNEL",
        "P001_OBSERVATION_BINDING",
        "CROSS_DOMAIN_NON_IMPLICATIONS",
        "EXECUTABLE_REFERENCE_BOUNDARY",
    }
)
MOVING_SURFACE_IDS = frozenset(
    {
        "TEMPORAL_EXTENSION",
        "OPERATION_EVENT_RELATION",
        "EVENT_CORRELATION",
        "EVENT_KIND_GOVERNANCE",
        "LEGACY_ASSESSMENT_ENVELOPE",
    }
)
BLOCKER_IDS = frozenset(
    {
        "UNRESOLVED_OPERATION_EVENT_OWNER",
        "LEGACY_ASSESSMENT_ENVELOPE_OVERLAP",
        "UNVERSIONED_PRIMARY_CONSUMER_BINDINGS",
        "CANDIDATE_BOARD_SELECTION_ABSENT",
    }
)
REMAINING_GATE_IDS = frozenset({"CANDIDATE_BOARD_SELECTION"})
REMAINING_GATE_ORDER = ("CANDIDATE_BOARD_SELECTION",)
FORBIDDEN_OUTCOMES = frozenset(
    {
        "OCP010_ACCEPTANCE",
        "CANONICAL_PROMOTION",
        "T6_OPEN",
        "DISCOVERY_SELF_SUPPLIED_REASSESSMENT",
        "CANDIDATE_BOARD_SELECTION",
    }
)

MAP_KEYS = {
    "schema_version",
    "rule_owner",
    "subject",
    "discovery_result",
    "direct_dependencies",
    "direct_consumers",
    "stable_candidates",
    "moving_surfaces",
    "blockers",
    "remaining_gates",
    "forbidden_outcomes",
}
SUBJECT_KEYS = {
    "document_id",
    "primary",
    "expected_version",
    "expected_status",
    "expected_concept_status",
    "expected_pattern_binding",
}
DEPENDENCY_KEYS = {
    "artifact_id",
    "declared_reference",
    "binding",
    "additional_exact_binding",
}
CONSUMER_KEYS = {
    "document_id",
    "primary",
    "expected_version",
    "expected_status",
    "document_binding",
    "exact_record_refs",
}
SURFACE_KEYS = {"surface_id", "disposition", "evidence"}
BLOCKER_KEYS = {"blocker_id", "disposition", "evidence"}
EVIDENCE_KEYS = {"path", "tokens"}
EXPECTED_DEPENDENCY_BINDINGS = {
    "OCP-000": ("unversioned-document", None),
    "OCP-001": ("unversioned-document", None),
    "OCP-002": ("unversioned-document", None),
    "OCP-004": ("unversioned-document", None),
    "OCP-008": ("unversioned-document", None),
    "AD-006": ("unversioned-decision", None),
    "P-001": ("unversioned-pattern-plus-exact-use", "P-001@0.1.0"),
}
EXPECTED_CONSUMERS = {
    "OCP-011": (
        "docs/011-outcome-assessment-record/README.md",
        "0.3.0",
        "Accepted",
        ("event@1", "observation-record@1"),
    ),
    "OCP-017": (
        "docs/017-operation-lifecycle/README.md",
        "0.2.0",
        "Accepted",
        (),
    ),
}
EXPECTED_DISPOSITIONS = {
    "EVENT_IDENTITY_KERNEL": "candidate",
    "OBSERVATION_RECORD_KERNEL": "candidate",
    "P001_OBSERVATION_BINDING": "candidate",
    "CROSS_DOMAIN_NON_IMPLICATIONS": "candidate",
    "EXECUTABLE_REFERENCE_BOUNDARY": "candidate",
    "TEMPORAL_EXTENSION": "moving",
    "OPERATION_EVENT_RELATION": "moving",
    "EVENT_CORRELATION": "moving",
    "EVENT_KIND_GOVERNANCE": "moving",
    "LEGACY_ASSESSMENT_ENVELOPE": "moving",
    "UNRESOLVED_OPERATION_EVENT_OWNER": "blocks_whole_document_freeze",
    "LEGACY_ASSESSMENT_ENVELOPE_OVERLAP": "blocks_whole_document_freeze",
    "UNVERSIONED_PRIMARY_CONSUMER_BINDINGS": "requires_consumer_compatibility_evidence",
    "CANDIDATE_BOARD_SELECTION_ABSENT": "blocks_promotion",
}
EXPECTED_EVIDENCE = {
    "EVENT_IDENTITY_KERNEL": (
        ("docs/010-event-concept/README.md", ("## 4. Event identity", "`event_id` є єдиною Core identity Event", "## 8. Exact Event resolution")),
    ),
    "OBSERVATION_RECORD_KERNEL": (
        ("docs/010-event-concept/README.md", ("## 6. ObservationRecord", "має власну identity", "## 9. Observation collection derivation")),
    ),
    "P001_OBSERVATION_BINDING": (
        ("docs/010-event-concept/README.md", ("invokes `P-001@0.1.0` для ObservationRecord", "## 20. P-001 conformance for ObservationRecord")),
    ),
    "CROSS_DOMAIN_NON_IMPLICATIONS": (
        ("docs/010-event-concept/README.md", ("## 10. Operation boundary", "## 11. Objective and assessment boundary", "## 12. Constraint, Conflict and Risk boundary", "## 13. Capability, Readiness and State boundary")),
    ),
    "EXECUTABLE_REFERENCE_BOUNDARY": (
        ("tools/ontology_checker/rules.yaml", ("source: OCP-010 §8 exact Event reference contract", "source: OCP-010 §9")),
        ("tools/ontology_checker/ocp_checker/event.py", ("EVENT_DERIVATION_RULES", "def resolve_event(", "def observations_for_event(")),
    ),
    "TEMPORAL_EXTENSION": (
        ("docs/010-event-concept/README.md", ("не визначає interval, uncertainty range, timezone policy", "окремого temporal interval module")),
    ),
    "OPERATION_EVENT_RELATION": (
        ("docs/010-event-concept/README.md", ("не вводить current Concept edge `Event → Operation` або `Operation → Event`", "Operation-to-Event relationship record")),
    ),
    "EVENT_CORRELATION": (
        ("docs/010-event-concept/README.md", ("не визначає автоматичну occurrence deduplication", "domain correlation rules")),
    ),
    "EVENT_KIND_GOVERNANCE": (
        ("docs/010-event-concept/README.md", ("canonical Event taxonomy", "governed Event-kind registry")),
    ),
    "LEGACY_ASSESSMENT_ENVELOPE": (
        ("docs/010-event-concept/README.md", ("checker-local assessment envelope", "не є normative OutcomeAssessmentRecord contract")),
        ("docs/011-outcome-assessment-record/README.md", ("Status: Accepted", "event@1", "observation-record@1")),
    ),
    "UNRESOLVED_OPERATION_EVENT_OWNER": (
        ("docs/010-event-concept/README.md", ("Який normative owner визначить Operation-to-Event relationship record",)),
    ),
    "LEGACY_ASSESSMENT_ENVELOPE_OVERLAP": (
        ("docs/010-event-concept/README.md", ("checker-local assessment envelope", "General OutcomeAssessmentRecord contract належить AB-056")),
        ("docs/011-outcome-assessment-record/README.md", ("Status: Accepted", "OutcomeAssessmentRecord")),
    ),
    "UNVERSIONED_PRIMARY_CONSUMER_BINDINGS": (
        ("docs/011-outcome-assessment-record/README.md", ("Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, OCP-006, OCP-008, OCP-010",)),
        ("docs/017-operation-lifecycle/README.md", ("Depends-On: AD-020, OCP-001, OCP-004, OCP-005, OCP-006, OCP-010",)),
    ),
    "CANDIDATE_BOARD_SELECTION_ABSENT": (
        ("architecture/foundation-promotion-gate.yaml", ("CANDIDATE_BOARD_SELECTION", "promotion_selections: []")),
    ),
}
RECORD_REF_PATTERN = re.compile(r"\b(?:event|observation-record)@[0-9]+(?:\.[0-9]+){0,2}\b", re.I)


@dataclass(frozen=True)
class EventStableSurfaceResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> EventStableSurfaceResult:
    return EventStableSurfaceResult(tuple(dict.fromkeys(errors)))


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
        loaded = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return loaded if isinstance(loaded, dict) else None


def _references(value: Any) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(str(item).strip() for item in value if str(item).strip())
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    return ()


def _ocp_index(repo_root: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    result: dict[str, tuple[Path, dict[str, Any]]] = {}
    for primary in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(primary)
        if metadata is not None and isinstance(metadata.get("Document-ID"), str):
            result[str(metadata["Document-ID"])] = (primary, metadata)
    return result


def _safe_relative_path(value: Any) -> Path | None:
    if not isinstance(value, str):
        return None
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        return None
    return candidate


def _validate_evidence(repo_root: Path, entries: Any, id_key: str, expected_ids: frozenset[str]) -> list[str]:
    errors: list[str] = []
    if not isinstance(entries, list):
        return [EVENT_STABLE_SURFACE_MAP_INVALID]
    ids = [entry.get(id_key) for entry in entries if isinstance(entry, dict)]
    if len(ids) != len(entries) or set(ids) != expected_ids or len(ids) != len(set(ids)):
        errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
    expected_keys = SURFACE_KEYS if id_key == "surface_id" else BLOCKER_KEYS
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != expected_keys:
            errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
            continue
        entry_id = entry.get(id_key)
        evidence = entry.get("evidence")
        if (
            entry.get("disposition") != EXPECTED_DISPOSITIONS.get(str(entry_id))
            or not isinstance(evidence, list)
            or not evidence
        ):
            errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
            continue
        normalized_evidence: list[tuple[str, tuple[str, ...]]] = []
        for item in evidence:
            if not isinstance(item, dict) or set(item) != EVIDENCE_KEYS:
                errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
                continue
            relative = _safe_relative_path(item.get("path"))
            tokens = item.get("tokens")
            if (
                relative is None
                or not isinstance(tokens, list)
                or not tokens
                or len(tokens) != len(set(tokens))
                or any(not isinstance(token, str) or not token for token in tokens)
            ):
                errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
                continue
            normalized_evidence.append((str(item.get("path")), tuple(tokens)))
            try:
                text = (repo_root / relative).read_text(encoding="utf-8")
            except OSError:
                errors.append(EVENT_STABLE_SURFACE_EVIDENCE_DRIFT)
                continue
            if any(token not in text for token in tokens):
                errors.append(EVENT_STABLE_SURFACE_EVIDENCE_DRIFT)
        if tuple(normalized_evidence) != EXPECTED_EVIDENCE.get(str(entry_id)):
            errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
    return errors


def validate_event_stable_surface(repo_root: Path) -> EventStableSurfaceResult:
    errors: list[str] = []
    map_path = repo_root / "architecture/event-stable-surface.yaml"
    try:
        payload = yaml.safe_load(map_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return _result((EVENT_STABLE_SURFACE_MAP_INVALID,))
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((EVENT_STABLE_SURFACE_MAP_INVALID,))

    subject = payload.get("subject")
    if (
        payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-031"
        or payload.get("discovery_result") != "stable_candidate_not_selected"
        or not isinstance(subject, dict)
        or set(subject) != SUBJECT_KEYS
    ):
        errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)

    ocps = _ocp_index(repo_root)
    resolved_subject = ocps.get("OCP-010")
    expected_primary = repo_root / "docs/010-event-concept/README.md"
    if resolved_subject is None:
        errors.append(EVENT_STABLE_SURFACE_SUBJECT_DRIFT)
    else:
        primary, metadata = resolved_subject
        if (
            subject.get("document_id") != "OCP-010"
            or subject.get("primary") != "docs/010-event-concept/README.md"
            or primary != expected_primary
            or str(metadata.get("Version")) != "0.2.1"
            or metadata.get("Status") != "Draft"
            or metadata.get("Concept-Status") != "Accepted"
            or tuple(_references(metadata.get("Uses-Patterns"))) != ("P-001@0.1.0",)
            or subject.get("expected_version") != "0.2.1"
            or subject.get("expected_status") != "Draft"
            or subject.get("expected_concept_status") != "Accepted"
            or subject.get("expected_pattern_binding") != "P-001@0.1.0"
        ):
            errors.append(EVENT_STABLE_SURFACE_SUBJECT_DRIFT)

    dependencies = payload.get("direct_dependencies")
    if not isinstance(dependencies, list):
        errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
        dependencies = []
    dependency_ids = [item.get("artifact_id") for item in dependencies if isinstance(item, dict)]
    if (
        set(dependency_ids) != DIRECT_DEPENDENCY_IDS
        or tuple(dependency_ids) != DIRECT_DEPENDENCY_ORDER
        or len(dependency_ids) != len(set(dependency_ids))
    ):
        errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
    for entry in dependencies:
        if not isinstance(entry, dict) or set(entry) != DEPENDENCY_KEYS:
            errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
            continue
        artifact_id = entry.get("artifact_id")
        expected_binding = EXPECTED_DEPENDENCY_BINDINGS.get(str(artifact_id))
        if (
            expected_binding is None
            or entry.get("declared_reference") != artifact_id
            or entry.get("binding") not in BINDING_KINDS
            or (entry.get("binding"), entry.get("additional_exact_binding")) != expected_binding
        ):
            errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
    if resolved_subject is not None:
        actual_dependencies = _references(resolved_subject[1].get("Depends-On"))
        if actual_dependencies != DIRECT_DEPENDENCY_ORDER:
            errors.append(EVENT_STABLE_SURFACE_DEPENDENCY_DRIFT)

    consumers = payload.get("direct_consumers")
    if not isinstance(consumers, list):
        errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
        consumers = []
    consumer_ids = [item.get("document_id") for item in consumers if isinstance(item, dict)]
    if (
        set(consumer_ids) != DIRECT_CONSUMER_IDS
        or tuple(consumer_ids) != DIRECT_CONSUMER_ORDER
        or len(consumer_ids) != len(set(consumer_ids))
    ):
        errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
    actual_consumer_ids = tuple(
        document_id
        for document_id, (_, metadata) in sorted(ocps.items())
        if "OCP-010" in _references(metadata.get("Depends-On"))
    )
    if actual_consumer_ids != DIRECT_CONSUMER_ORDER:
        errors.append(EVENT_STABLE_SURFACE_CONSUMER_DRIFT)
    for entry in consumers:
        if not isinstance(entry, dict) or set(entry) != CONSUMER_KEYS:
            errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)
            continue
        document_id = str(entry.get("document_id"))
        expected = EXPECTED_CONSUMERS.get(document_id)
        resolved = ocps.get(document_id)
        exact_refs = entry.get("exact_record_refs")
        if expected is None or resolved is None or not isinstance(exact_refs, list):
            errors.append(EVENT_STABLE_SURFACE_CONSUMER_DRIFT)
            continue
        primary, metadata = resolved
        expected_path, version, status, record_refs = expected
        try:
            text = primary.read_text(encoding="utf-8")
        except OSError:
            text = ""
        actual_record_refs = tuple(sorted(set(match.lower() for match in RECORD_REF_PATTERN.findall(text))))
        if (
            entry.get("primary") != expected_path
            or primary != repo_root / expected_path
            or str(metadata.get("Version")) != version
            or metadata.get("Status") != status
            or entry.get("expected_version") != version
            or entry.get("expected_status") != status
            or entry.get("document_binding") != "unversioned-document"
            or tuple(exact_refs) != record_refs
            or actual_record_refs != tuple(sorted(record_refs))
        ):
            errors.append(EVENT_STABLE_SURFACE_CONSUMER_DRIFT)

    errors.extend(_validate_evidence(repo_root, payload.get("stable_candidates"), "surface_id", STABLE_SURFACE_IDS))
    errors.extend(_validate_evidence(repo_root, payload.get("moving_surfaces"), "surface_id", MOVING_SURFACE_IDS))
    errors.extend(_validate_evidence(repo_root, payload.get("blockers"), "blocker_id", BLOCKER_IDS))

    remaining_gates = payload.get("remaining_gates")
    forbidden = payload.get("forbidden_outcomes")
    if (
        not isinstance(remaining_gates, list)
        or set(remaining_gates) != REMAINING_GATE_IDS
        or tuple(remaining_gates) != REMAINING_GATE_ORDER
        or not isinstance(forbidden, list)
        or set(forbidden) != FORBIDDEN_OUTCOMES
        or len(forbidden) != len(FORBIDDEN_OUTCOMES)
    ):
        errors.append(EVENT_STABLE_SURFACE_MAP_INVALID)

    try:
        gate = yaml.safe_load(
            (repo_root / "architecture/foundation-promotion-gate.yaml").read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        gate = None
    sequence = gate.get("sequence") if isinstance(gate, dict) else None
    if (
        not isinstance(sequence, dict)
        or sequence.get("selected_next_scope") != "Y10D"
        or sequence.get("selected_next_scope_state") != "complete"
        or "Y10D" not in (sequence.get("completed_steps") or [])
        or "POST_DISCOVERY_REASSESSMENT" not in (sequence.get("completed_steps") or [])
        or tuple(sequence.get("required_before_promotion") or ()) != REMAINING_GATE_ORDER
        or gate.get("promotion_selections") != []
    ):
        errors.append(EVENT_STABLE_SURFACE_NEXT_GATE_REQUIRED)
    return _result(errors)
