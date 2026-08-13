from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

from .assessment import validate_integrated_outcome_scenario
from .checker import load_fixture
from .operation_lifecycle import validate_operation_q3i_fixture


EVENT_LIFECYCLE_PROMOTION_MAP_INVALID = "EVENT_LIFECYCLE_PROMOTION_MAP_INVALID"
EVENT_LIFECYCLE_PROMOTION_SUBJECT_DRIFT = "EVENT_LIFECYCLE_PROMOTION_SUBJECT_DRIFT"
EVENT_LIFECYCLE_PROMOTION_PRECONDITION_UNPROVED = "EVENT_LIFECYCLE_PROMOTION_PRECONDITION_UNPROVED"
EVENT_LIFECYCLE_PROMOTION_CONSUMER_DRIFT = "EVENT_LIFECYCLE_PROMOTION_CONSUMER_DRIFT"
EVENT_LIFECYCLE_PROMOTION_GATE_DRIFT = "EVENT_LIFECYCLE_PROMOTION_GATE_DRIFT"
EVENT_LIFECYCLE_PROMOTION_EVIDENCE_DRIFT = "EVENT_LIFECYCLE_PROMOTION_EVIDENCE_DRIFT"

MAP_KEYS = frozenset({
    "schema_version", "rule_owner", "baseline", "gate_applicability", "subject",
    "promotion_preconditions", "compatibility", "migration", "rollback", "evidence",
})
GATE_KEYS = frozenset({"form", "route", "g4_required", "accepted_consumer_required"})
SUBJECT_KEYS = frozenset({
    "document_id", "primary", "expected_version", "expected_status",
    "expected_concept_status", "selected_by", "disposition",
})
PRECONDITION_KEYS = frozenset({"precondition_id", "proof", "status"})
COMPATIBILITY_KEYS = frozenset({
    "document_id", "primary", "expected_version", "expected_status",
    "preserved_refs", "executable_fixture",
})
MIGRATION_KEYS = frozenset({"data", "references", "schemas"})
ROLLBACK_KEYS = frozenset({"unit", "partial_rollback", "restores"})
EVIDENCE_KEYS = frozenset({"path", "tokens", "absent_tokens", "absent_current_edges"})
PRECONDITION_IDS = frozenset({
    "EVENT_OWNER_BOUNDARY_REMEDIATED",
    "LEGACY_ASSESSMENT_OVERLAP_REMEDIATED",
    "PRIMARY_CONSUMER_COMPATIBILITY_PROVED",
})
PROOF_IDS = frozenset({
    "STABLE_CORE_EXCLUSION", "OCP011_GOVERNED_ENVELOPE", "ACCEPTED_CONSUMERS_PRESERVED",
})
CONSUMER_IDS = frozenset({"OCP-011", "OCP-017"})
PRESERVED_REFS = frozenset({
    "event@1", "observation-record@1", "independent Event occurrence",
    "provenance", "does not create or prove that Event",
})
EXPECTED_PRECONDITIONS = {
    "EVENT_OWNER_BOUNDARY_REMEDIATED": "STABLE_CORE_EXCLUSION",
    "LEGACY_ASSESSMENT_OVERLAP_REMEDIATED": "OCP011_GOVERNED_ENVELOPE",
    "PRIMARY_CONSUMER_COMPATIBILITY_PROVED": "ACCEPTED_CONSUMERS_PRESERVED",
}
EXPECTED_CONSUMERS = {
    "OCP-011": (
        "docs/011-outcome-assessment-record/README.md", "0.3.0", "Accepted",
        ("event@1", "observation-record@1"),
        "tools/ontology_checker/fixtures/event/valid-integrated-scenario.yaml",
    ),
    "OCP-017": (
        "docs/017-operation-lifecycle/README.md", "0.2.0", "Accepted",
        ("independent Event occurrence", "provenance", "does not create or prove that Event"),
        "tools/ontology_checker/fixtures/operation_lifecycle/valid-q3i-completed.yaml",
    ),
}


@dataclass(frozen=True)
class EventLifecyclePromotionResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> EventLifecyclePromotionResult:
    return EventLifecyclePromotionResult(tuple(dict.fromkeys(errors)))


def _load(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None


def _frontmatter(path: Path) -> dict[str, Any] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return None
    end = text.find("\n---\n", 4)
    try:
        value = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return value if isinstance(value, dict) else None


def validate_event_lifecycle_promotion(repo_root: Path) -> EventLifecyclePromotionResult:
    errors: list[str] = []
    payload = _load(repo_root / "architecture/event-lifecycle-promotion.yaml")
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((EVENT_LIFECYCLE_PROMOTION_MAP_INVALID,))
    gate_applicability = payload.get("gate_applicability")
    subject = payload.get("subject")
    if (
        payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-016AD"
        or payload.get("baseline") != "3b956d68255ef7b9a8fcf589737b5fe3b182f24a"
        or not isinstance(gate_applicability, dict)
        or set(gate_applicability) != GATE_KEYS
        or gate_applicability != {
            "form": "existing-concept-document-lifecycle-remediation",
            "route": "OCP-016-F", "g4_required": False,
            "accepted_consumer_required": False,
        }
        or not isinstance(subject, dict)
        or set(subject) != SUBJECT_KEYS
        or subject != {
            "document_id": "OCP-010", "primary": "docs/010-event-concept/README.md",
            "expected_version": "1.0.1", "expected_status": "Canonical",
            "expected_concept_status": "Canonical", "selected_by": "AD-016AC",
            "disposition": "PROMOTED_AFTER_PROVED_REMEDIATION",
        }
    ):
        errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)

    metadata = _frontmatter(repo_root / "docs/010-event-concept/README.md")
    if metadata is None or any((
        metadata.get("Document-ID") != "OCP-010",
        str(metadata.get("Version")) != "1.0.1",
        metadata.get("Status") != "Canonical",
        metadata.get("Concept-Status") != "Canonical",
    )):
        errors.append(EVENT_LIFECYCLE_PROMOTION_SUBJECT_DRIFT)

    preconditions = payload.get("promotion_preconditions")
    if not isinstance(preconditions, list):
        errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)
        preconditions = []
    seen_preconditions: set[str] = set()
    for item in preconditions:
        if not isinstance(item, dict) or set(item) != PRECONDITION_KEYS:
            errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)
            continue
        precondition_id = str(item.get("precondition_id"))
        seen_preconditions.add(precondition_id)
        if item.get("proof") != EXPECTED_PRECONDITIONS.get(precondition_id) or item.get("status") != "proved":
            errors.append(EVENT_LIFECYCLE_PROMOTION_PRECONDITION_UNPROVED)
    if seen_preconditions != PRECONDITION_IDS or {item.get("proof") for item in preconditions if isinstance(item, dict)} != PROOF_IDS:
        errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)

    consumers = payload.get("compatibility")
    if not isinstance(consumers, list):
        errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)
        consumers = []
    seen_consumers: set[str] = set()
    for item in consumers:
        if not isinstance(item, dict) or set(item) != COMPATIBILITY_KEYS:
            errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)
            continue
        document_id = str(item.get("document_id"))
        expected = EXPECTED_CONSUMERS.get(document_id)
        seen_consumers.add(document_id)
        if expected is None or item != {
            "document_id": document_id, "primary": expected[0],
            "expected_version": expected[1], "expected_status": expected[2],
            "preserved_refs": list(expected[3]), "executable_fixture": expected[4],
        }:
            errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)
            continue
        consumer_meta = _frontmatter(repo_root / expected[0])
        try:
            text = (repo_root / expected[0]).read_text(encoding="utf-8")
            fixture = load_fixture(repo_root / expected[4])
            fixture_valid = (
                validate_integrated_outcome_scenario(fixture).valid
                if document_id == "OCP-011"
                else validate_operation_q3i_fixture(fixture).valid
            )
        except (OSError, ValueError, yaml.YAMLError):
            text = ""
            fixture_valid = False
        if (
            consumer_meta is None
            or str(consumer_meta.get("Version")) != expected[1]
            or consumer_meta.get("Status") != expected[2]
            or "OCP-010" not in str(consumer_meta.get("Depends-On"))
            or any(token not in text for token in expected[3])
            or not fixture_valid
        ):
            errors.append(EVENT_LIFECYCLE_PROMOTION_CONSUMER_DRIFT)
    if seen_consumers != CONSUMER_IDS or set(PRESERVED_REFS) != {
        ref for expected in EXPECTED_CONSUMERS.values() for ref in expected[3]
    }:
        errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)

    if payload.get("migration") != {
        "data": "NONE", "references": "PRESERVED_UNVERSIONED_DOCUMENT_BINDINGS", "schemas": "NONE",
    } or payload.get("rollback") != {
        "unit": "EVENT_BODY_PROMOTION_PROOFS_GATE_WITNESSES_AND_ACCOUNTING",
        "partial_rollback": "FORBIDDEN", "restores": "OCP010_0_2_1_DRAFT_SELECTED",
    }:
        errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)
    if not isinstance(payload.get("migration"), dict) or set(payload["migration"]) != MIGRATION_KEYS:
        errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)
    if not isinstance(payload.get("rollback"), dict) or set(payload["rollback"]) != ROLLBACK_KEYS:
        errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)

    evidence = payload.get("evidence")
    if not isinstance(evidence, dict) or set(evidence) != PRECONDITION_IDS:
        errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)
        evidence = {}
    for precondition_id, items in evidence.items():
        if not isinstance(items, list) or not items:
            errors.append(EVENT_LIFECYCLE_PROMOTION_PRECONDITION_UNPROVED)
            continue
        for item in items:
            if not isinstance(item, dict) or not set(item) <= EVIDENCE_KEYS or "path" not in item:
                errors.append(EVENT_LIFECYCLE_PROMOTION_MAP_INVALID)
                continue
            path = repo_root / str(item.get("path"))
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                text = ""
            tokens = item.get("tokens") or []
            absent_tokens = item.get("absent_tokens") or []
            absent_edges = item.get("absent_current_edges") or []
            current_section = text.split("## Current normative dependencies", 1)[-1].split("## Current isolated", 1)[0]
            if (
                any(not isinstance(token, str) or token not in text for token in tokens)
                or any(not isinstance(token, str) or token in text for token in absent_tokens)
                or any(not isinstance(token, str) or token in current_section for token in absent_edges)
            ):
                errors.append(EVENT_LIFECYCLE_PROMOTION_EVIDENCE_DRIFT)

    gate = _load(repo_root / "architecture/foundation-promotion-gate.yaml")
    sequence = gate.get("sequence") if isinstance(gate, dict) else None
    if (
        not isinstance(sequence, dict)
        or "EVENT_LIFECYCLE_PROMOTION_ACT" not in (sequence.get("completed_steps") or ())
        or sequence.get("required_before_promotion") != []
        or sequence.get("selected_next_scope") != "OCP-010"
        or sequence.get("selected_next_scope_state") != "promoted"
        or gate.get("promotion_selections") != ["OCP-010"]
    ):
        errors.append(EVENT_LIFECYCLE_PROMOTION_GATE_DRIFT)
    return _result(errors)
