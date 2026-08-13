from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

from .assessment import validate_integrated_outcome_scenario
from .checker import load_fixture
from .event_promotion_selection import validate_event_promotion_selection
from .event_lifecycle_promotion import validate_event_lifecycle_promotion
from .event_stable_surface import validate_event_stable_surface
from .foundation_promotion_reassessment import validate_foundation_promotion_reassessment


EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID = "EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID"
EVENT_CONCEPT_CANONICALIZATION_DEPENDENCY_UNSTABLE = "EVENT_CONCEPT_CANONICALIZATION_DEPENDENCY_UNSTABLE"
EVENT_CONCEPT_CANONICALIZATION_EVIDENCE_INSUFFICIENT = "EVENT_CONCEPT_CANONICALIZATION_EVIDENCE_INSUFFICIENT"
EVENT_CONCEPT_CANONICALIZATION_STATUS_DRIFT = "EVENT_CONCEPT_CANONICALIZATION_STATUS_DRIFT"
EVENT_CONCEPT_CANONICALIZATION_HISTORY_REWRITTEN = "EVENT_CONCEPT_CANONICALIZATION_HISTORY_REWRITTEN"

MAP_KEYS = frozenset({
    "schema_version", "rule_owner", "baseline", "gate_applicability", "board_decision",
    "requirements", "current_status_carriers", "historical_witnesses",
    "executable_evidence", "freeze_boundary", "forbidden_implications",
})
GATE_KEYS = frozenset({"form", "route", "g4_required", "accepted_consumer_required"})
BOARD_KEYS = frozenset({"concept", "transition", "authority"})
REQUIREMENT_KEYS = frozenset({"stable_dependencies", "machine_readable_checks"})
DEPENDENCY_KEYS = frozenset({
    "concept_dependencies", "direct_ocp_dependencies", "required_direct_ocp_status",
    "pattern_binding", "required_pattern_status", "result",
})
MACHINE_KEYS = frozenset({"semantic_surfaces", "result"})
CARRIER_KEYS = frozenset({"path", "carrier", "expected_status"})
HISTORICAL_KEYS = frozenset({"path", "baseline", "expected_historical_status"})
EVIDENCE_KEYS = frozenset({"path", "tokens"})

DIRECT_OCP_DEPENDENCIES = (
    "OCP-000", "OCP-001", "OCP-002", "OCP-004", "OCP-008",
)
SEMANTIC_SURFACES = frozenset({
    "EVENT_IDENTITY_AND_REFERENCE",
    "OBSERVATION_COLLECTION_AND_SUPERSESSION",
    "INTEGRATED_EVENT_ASSESSMENT_SCENARIO",
    "PRIMARY_CONSUMER_COMPATIBILITY",
})
FREEZE_BOUNDARY = frozenset({
    "EVENT_IDENTITY", "OBSERVATION_RECORD_AUTHORITY",
    "HISTORY_PRESERVING_SUPERSESSION", "OCCURRENCE_OBSERVATION_BOUNDARY",
})
FORBIDDEN_IMPLICATIONS = frozenset({
    "OPERATION_EVENT_EDGE", "POSITIVE_RELATION_OWNER", "TEMPORAL_INTERVAL_MODEL",
    "CORRELATION_RULE", "EVENT_KIND_REGISTRY", "TRUTH_OR_ASSESSMENT_AUTHORITY",
    "CONFLICT_RISK_READINESS", "AUTHORIZATION_OR_PRODUCTION_SCHEMA",
})
EXPECTED_CARRIERS = {
    "docs/000-operational-ontology/README.md": "REGISTRY_ROW",
    "docs/002-concept-taxonomy/README.md": "TAXONOMY_METADATA_AND_CURRENT_VIEWS",
    "docs/010-event-concept/README.md": "DEFINING_METADATA_AND_CURRENT_SECTION",
    "docs/004-operation-concept/README.md": "CURRENT_PEER_AND_DECOMPOSITION_VIEWS",
    "docs/005-assignment-concept/README.md": "CURRENT_PEER_VIEW",
    "docs/006-constraint-concept/README.md": "CURRENT_PEER_VIEW",
    "architecture/baselines/foundation-map.md": "GENERATED_CURRENT_PROJECTION",
    "architecture/baselines/foundation-future-edges.yaml": "CURRENT_FUTURE_INTENT_BASIS",
    "architecture/event-lifecycle-promotion.yaml": "CURRENT_COMPLETED_PROMOTION_SUBJECT",
    "architecture/foundation-promotion-gate.yaml": "CURRENT_PROMOTED_CANDIDATE",
    "README.md": "CURRENT_REPOSITORY_SUMMARY",
    "backlog/roadmap.md": "CURRENT_ROADMAP_SUMMARY",
    "backlog/architecture-backlog.md": "CURRENT_AB062_SUMMARY",
}
CURRENT_TOKENS = {
    "docs/000-operational-ontology/README.md": ("| Event | Canonical |", "Version: 1.6.0"),
    "docs/002-concept-taxonomy/README.md": (
        "Event: Canonical", "Event [Canonical]", "Concept `Event` має статус `Canonical`",
    ),
    "docs/010-event-concept/README.md": (
        "Concept-Status: Canonical", "## 27. Event Concept canonicalization — v1.0.1",
    ),
    "docs/004-operation-concept/README.md": (
        "Version: 1.0.1", "| Event | Canonical |", "Event [Canonical]",
    ),
    "docs/005-assignment-concept/README.md": ("| Event | Canonical |",),
    "docs/006-constraint-concept/README.md": ("| Event | Canonical |",),
    "architecture/baselines/foundation-map.md": ("| Event | Canonical |",),
    "architecture/baselines/foundation-future-edges.yaml": ("OCP-010 Event Canonical",),
    "architecture/event-lifecycle-promotion.yaml": ("expected_concept_status: Canonical",),
    "architecture/foundation-promotion-gate.yaml": ("expected_concept_status: Canonical",),
    "README.md": ("Assignment та Constraint лишаються `Accepted`, а Event є `Canonical`",),
    "backlog/roadmap.md": ("Assignment і Constraint лишаються Accepted, Event є Canonical",),
    "backlog/architecture-backlog.md": ("Event Concept Canonical", "active_cycle_id: null"),
}
EXPECTED_HISTORICAL = {
    "architecture/event-stable-surface.yaml": "ed1e338f52d87de42d56c66c20c7cf89891a589f",
    "architecture/foundation-promotion-reassessment.yaml": "53d254405e6f75c7198e3e989d14a5a5678628ce",
    "architecture/event-promotion-selection.yaml": "ffc698ecc7fabab9d0f8ade9c85913f7cc95eadc",
}
EXPECTED_EVIDENCE = {
    "tools/ontology_checker/rules.yaml": (
        "OCP-010 §8 exact Event reference contract", "OCP-010 §9",
    ),
    "tools/ontology_checker/ocp_checker/event.py": (
        "EVENT_DERIVATION_RULES", "def resolve_event(", "def observations_for_event(",
    ),
    "tools/ontology_checker/fixtures/event/valid-integrated-scenario.yaml": (
        "event_id", "observation-record@1", "event_ref",
    ),
    "architecture/event-lifecycle-promotion.yaml": (
        "PRIMARY_CONSUMER_COMPATIBILITY_PROVED", "OCP-011", "OCP-017",
        "ACCEPTED_CONSUMERS_PRESERVED",
    ),
}


@dataclass(frozen=True)
class EventConceptCanonicalizationResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> EventConceptCanonicalizationResult:
    return EventConceptCanonicalizationResult(tuple(dict.fromkeys(errors)))


def _load(fpath: Path) -> Any:
    try:
        return yaml.safe_load(fpath.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None


def _frontmatter(fpath: Path) -> dict[str, Any] | None:
    try:
        text = fpath.read_text(encoding="utf-8")
    except OSError:
        return None
    end = text.find("\n---\n", 4) if text.startswith("---\n") else -1
    if end < 0:
        return None
    try:
        value = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None
    return value if isinstance(value, dict) else None


def _refs(value: Any) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(str(item).strip() for item in value if str(item).strip())
    if isinstance(value, str):
        return tuple(item.strip() for item in value.split(",") if item.strip())
    return ()


def validate_event_concept_canonicalization(repo_root: Path) -> EventConceptCanonicalizationResult:
    errors: list[str] = []
    payload = _load(repo_root / "architecture/event-concept-canonicalization.yaml")
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID,))
    if (
        payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-032"
        or payload.get("baseline") != "060b801e78b0ce88c0eb858be127cecce3e6569f"
        or payload.get("gate_applicability") != {
            "form": "existing-concept-status-canonicalization", "route": "OCP-016-F",
            "g4_required": False, "accepted_consumer_required": False,
        }
        or set(payload.get("gate_applicability") or {}) != GATE_KEYS
        or payload.get("board_decision") != {
            "concept": "Event", "transition": "ACCEPTED_TO_CANONICAL",
            "authority": "EXPLICIT_ARCHITECTURE_BOARD_INPUT",
        }
        or set(payload.get("board_decision") or {}) != BOARD_KEYS
    ):
        errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)

    requirements = payload.get("requirements")
    if not isinstance(requirements, dict) or set(requirements) != REQUIREMENT_KEYS:
        errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
        requirements = {}
    dependencies = requirements.get("stable_dependencies")
    machine = requirements.get("machine_readable_checks")
    if (
        not isinstance(dependencies, dict) or set(dependencies) != DEPENDENCY_KEYS
        or dependencies != {
            "concept_dependencies": [],
            "direct_ocp_dependencies": list(DIRECT_OCP_DEPENDENCIES),
            "required_direct_ocp_status": "Canonical", "pattern_binding": "P-001@0.1.0",
            "required_pattern_status": "Accepted", "result": "proved",
        }
    ):
        errors.append(EVENT_CONCEPT_CANONICALIZATION_DEPENDENCY_UNSTABLE)
    if (
        not isinstance(machine, dict) or set(machine) != MACHINE_KEYS
        or set(machine.get("semantic_surfaces") or ()) != SEMANTIC_SURFACES
        or machine.get("result") != "proved"
    ):
        errors.append(EVENT_CONCEPT_CANONICALIZATION_EVIDENCE_INSUFFICIENT)

    subject = _frontmatter(repo_root / "docs/010-event-concept/README.md")
    if subject is None:
        errors.append(EVENT_CONCEPT_CANONICALIZATION_STATUS_DRIFT)
    else:
        direct_ocps = tuple(item for item in _refs(subject.get("Depends-On")) if item.startswith("OCP-"))
        concept_dependencies = _refs(subject.get("Concept-Depends-On"))
        if direct_ocps != DIRECT_OCP_DEPENDENCIES or concept_dependencies:
            errors.append(EVENT_CONCEPT_CANONICALIZATION_DEPENDENCY_UNSTABLE)
        if (
            subject.get("Document-ID") != "OCP-010" or str(subject.get("Version")) != "1.0.1"
            or subject.get("Status") != "Canonical" or subject.get("Concept-Status") != "Canonical"
            or _refs(subject.get("Uses-Patterns")) != ("P-001@0.1.0",)
        ):
            errors.append(EVENT_CONCEPT_CANONICALIZATION_STATUS_DRIFT)
        for document_id in direct_ocps:
            resolved = next(
                (p for p in (repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")
                 if (_frontmatter(p) or {}).get("Document-ID") == document_id), None,
            )
            if resolved is None or (_frontmatter(resolved) or {}).get("Status") != "Canonical":
                errors.append(EVENT_CONCEPT_CANONICALIZATION_DEPENDENCY_UNSTABLE)
        pattern = _frontmatter(repo_root / "patterns/P-001-identified-record-pattern.md")
        if pattern is None or str(pattern.get("Version")) != "0.1.0" or pattern.get("Status") != "Accepted":
            errors.append(EVENT_CONCEPT_CANONICALIZATION_DEPENDENCY_UNSTABLE)

    carriers = payload.get("current_status_carriers")
    normalized_carriers: dict[str, str] = {}
    if not isinstance(carriers, list):
        errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
    else:
        for item in carriers:
            if not isinstance(item, dict) or set(item) != CARRIER_KEYS:
                errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
                continue
            fpath = str(item.get("path"))
            normalized_carriers[fpath] = str(item.get("carrier"))
            if item.get("expected_status") != "Canonical":
                errors.append(EVENT_CONCEPT_CANONICALIZATION_STATUS_DRIFT)
        if normalized_carriers != EXPECTED_CARRIERS:
            errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
    if set(CURRENT_TOKENS) != set(EXPECTED_CARRIERS) or any(not tokens for tokens in CURRENT_TOKENS.values()):
        errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
    for fpath, tokens in CURRENT_TOKENS.items():
        try:
            text = (repo_root / fpath).read_text(encoding="utf-8")
        except OSError:
            text = ""
        if any(token not in text for token in tokens):
            errors.append(EVENT_CONCEPT_CANONICALIZATION_STATUS_DRIFT)

    historical = payload.get("historical_witnesses")
    normalized_historical: dict[str, str] = {}
    if not isinstance(historical, list):
        errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
    else:
        for item in historical:
            if not isinstance(item, dict) or set(item) != HISTORICAL_KEYS:
                errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
                continue
            fpath = str(item.get("path"))
            normalized_historical[fpath] = str(item.get("baseline"))
            if item.get("expected_historical_status") != "Accepted":
                errors.append(EVENT_CONCEPT_CANONICALIZATION_HISTORY_REWRITTEN)
        if normalized_historical != EXPECTED_HISTORICAL:
            errors.append(EVENT_CONCEPT_CANONICALIZATION_HISTORY_REWRITTEN)
    if not all((
        validate_event_stable_surface(repo_root).valid,
        validate_foundation_promotion_reassessment(repo_root).valid,
        validate_event_promotion_selection(repo_root).valid,
    )):
        errors.append(EVENT_CONCEPT_CANONICALIZATION_HISTORY_REWRITTEN)

    evidence = payload.get("executable_evidence")
    normalized_evidence: dict[str, tuple[str, ...]] = {}
    if not isinstance(evidence, list):
        errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
    else:
        for item in evidence:
            if not isinstance(item, dict) or set(item) != EVIDENCE_KEYS:
                errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
                continue
            fpath = str(item.get("path"))
            tokens = tuple(item.get("tokens") or ())
            normalized_evidence[fpath] = tokens
            try:
                text = (repo_root / fpath).read_text(encoding="utf-8")
            except OSError:
                text = ""
            if any(not isinstance(token, str) or token not in text for token in tokens):
                errors.append(EVENT_CONCEPT_CANONICALIZATION_EVIDENCE_INSUFFICIENT)
        if normalized_evidence != EXPECTED_EVIDENCE:
            errors.append(EVENT_CONCEPT_CANONICALIZATION_EVIDENCE_INSUFFICIENT)
    try:
        integrated = load_fixture(repo_root / "tools/ontology_checker/fixtures/event/valid-integrated-scenario.yaml")
        if not validate_integrated_outcome_scenario(integrated).valid or not validate_event_lifecycle_promotion(repo_root).valid:
            errors.append(EVENT_CONCEPT_CANONICALIZATION_EVIDENCE_INSUFFICIENT)
    except (OSError, ValueError, yaml.YAMLError):
        errors.append(EVENT_CONCEPT_CANONICALIZATION_EVIDENCE_INSUFFICIENT)

    if set(payload.get("freeze_boundary") or ()) != FREEZE_BOUNDARY:
        errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
    if set(payload.get("forbidden_implications") or ()) != FORBIDDEN_IMPLICATIONS:
        errors.append(EVENT_CONCEPT_CANONICALIZATION_MAP_INVALID)
    return _result(errors)
