from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
from typing import Any, Iterable

import yaml


CONSTRAINT_STATUS_READINESS_MAP_INVALID = "CONSTRAINT_STATUS_READINESS_MAP_INVALID"
CONSTRAINT_STATUS_READINESS_NORM_DRIFT = "CONSTRAINT_STATUS_READINESS_NORM_DRIFT"
CONSTRAINT_STATUS_READINESS_ASSESSMENT_DRIFT = "CONSTRAINT_STATUS_READINESS_ASSESSMENT_DRIFT"
CONSTRAINT_STATUS_READINESS_PRECEDENT_DRIFT = "CONSTRAINT_STATUS_READINESS_PRECEDENT_DRIFT"
CONSTRAINT_STATUS_READINESS_SUBJECT_DRIFT = "CONSTRAINT_STATUS_READINESS_SUBJECT_DRIFT"
CONSTRAINT_STATUS_READINESS_GATE_DRIFT = "CONSTRAINT_STATUS_READINESS_GATE_DRIFT"
CONSTRAINT_STATUS_READINESS_EVIDENCE_DRIFT = "CONSTRAINT_STATUS_READINESS_EVIDENCE_DRIFT"

MAP_PATH = Path("architecture/constraint-document-status-readiness.yaml")
SUBJECT_PATH = Path("docs/006-constraint-concept/README.md")
ASSIGNMENT_PATH = Path("docs/005-assignment-concept/README.md")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
BASELINE = "b0b7ccfa8a40ce4f7056fdd2fbf8c61088a7fbcd"
MAP_SHA256 = "07b3216249a888644ce46a2a818a7d4d70256cfbb90415b002d5d040c0d5212d"
SUBJECT_SHA256 = "0472d8ce4b15a8c64d58151ee7f706b450b930f708f6f0a7a40bdd87914b3b10"
EXPECTED_MAP_KEYS = frozenset({
    "schema_version", "rule_owner", "baseline", "gate_first", "subject",
    "norm_vs_practice", "governance_sweep", "promotion_criteria", "ocp006_live_inputs",
    "precedent_sweep", "result", "versioning", "migration",
    "forbidden_outcomes", "baseline_evidence_objects",
})
CRITERION_IDS = frozenset({
    "BINDING_REVIEW_LANE", "EXACT_ROUTE_AND_AUTHORITY_LEDGER",
    "BOARD_ACCEPTS_CURRENT_SEMANTICS", "ATOMIC_DOCUMENT_PROMOTION_UNIT",
    "CANONICAL_STABILITY_CHECKS_AND_BOARD_ACT",
    "CANONICAL_DIRECT_DEPENDENCY_FLOOR_L2",
    "EXACT_HEAD_AUTHORIZATION_AND_ATOMIC_EFFECT",
})
PRACTICE_AXES = frozenset({
    "open-question-count", "bounded-stable-surface", "whole-document-freeze",
    "moving-surface-classification",
})
GOVERNANCE_SOURCES = frozenset({
    "docs/000-operational-ontology/README.md",
    "docs/001-ontology-governance/README.md",
    "docs/002-concept-taxonomy/README.md",
    "docs/016-core-boundary/README.md",
    "architecture/artifact-taxonomy.yaml",
})
FORBIDDEN_OUTCOMES = frozenset({
    "OCP006_CHANGE", "OCP006_STATUS_OR_VERSION_CHANGE", "QUESTION_CLOSURE",
    "CONSTRAINT_SELECTION", "PROMOTION_AUTHORIZATION", "PROMOTION_CYCLE_START",
    "CONCEPT_OR_GRAPH_CHANGE", "OCP005_CHANGE", "NEXT_ACT_AUTHORIZATION",
})
PROMOTED_OPEN_CARRIERS = {
    "OCP-002": "Можливий mapping до Organizational Resource залишається відкритим",
    "OCP-003": "exact mapping `Organization ↔ Resource` лишаються відкритими",
    "OCP-004": "## 20. Open Questions",
    "OCP-008": "## 16. Open Questions",
    "OCP-010": "The first four questions remain open",
}
EXPECTED_DEPENDENCIES = (
    "OCP-000", "OCP-001", "OCP-002", "OCP-003", "OCP-004", "OCP-005",
)
EXPECTED_ASSESSMENTS = {
    "BINDING_REVIEW_LANE": "pending-separate-status-act",
    "EXACT_ROUTE_AND_AUTHORITY_LEDGER": "partially-present-but-pending-proposal-specific-package",
    "BOARD_ACCEPTS_CURRENT_SEMANTICS": "pending-separate-status-act",
    "ATOMIC_DOCUMENT_PROMOTION_UNIT": "partially-present-but-pending-atomic-status-unit",
    "CANONICAL_STABILITY_CHECKS_AND_BOARD_ACT": "not-satisfied",
    "CANONICAL_DIRECT_DEPENDENCY_FLOOR_L2": "not-satisfied",
    "EXACT_HEAD_AUTHORIZATION_AND_ATOMIC_EFFECT": "pending-separate-status-act",
}


@dataclass(frozen=True)
class ConstraintDocumentStatusReadinessResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> ConstraintDocumentStatusReadinessResult:
    return ConstraintDocumentStatusReadinessResult(tuple(dict.fromkeys(errors)))


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


def _hash(path: Path) -> str | None:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def _refs(value: Any) -> tuple[str, ...]:
    if isinstance(value, str):
        return tuple(part.strip() for part in value.split(",") if part.strip())
    if isinstance(value, list):
        return tuple(str(part).strip() for part in value if str(part).strip())
    return ()


def _primary_documents(repo_root: Path) -> dict[str, tuple[Path, dict[str, Any], str]]:
    documents: dict[str, tuple[Path, dict[str, Any], str]] = {}
    for path in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(path)
        if not metadata or not isinstance(metadata.get("Document-ID"), str):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        documents[str(metadata["Document-ID"])] = (path, metadata, text)
    return documents


def validate_constraint_document_status_readiness(
    repo_root: Path,
) -> ConstraintDocumentStatusReadinessResult:
    errors: list[str] = []
    payload = _load(repo_root / MAP_PATH)
    if not isinstance(payload, dict) or set(payload) != EXPECTED_MAP_KEYS:
        return _result((CONSTRAINT_STATUS_READINESS_MAP_INVALID,))
    digest = hashlib.sha256(
        yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode()
    ).hexdigest()
    if (
        digest != MAP_SHA256
        or payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-052"
        or payload.get("baseline") != BASELINE
        or frozenset(payload.get("forbidden_outcomes") or ()) != FORBIDDEN_OUTCOMES
    ):
        errors.append(CONSTRAINT_STATUS_READINESS_MAP_INVALID)

    gate = payload.get("gate_first") or {}
    result = payload.get("result") or {}
    if (
        gate != {
            "ocp016_gate": "G4", "applies": False, "positive_capable": False,
            "activation_performed": False,
            "reason": "discovery-classifies-existing-governance-and-status-evidence-without-adding-a-rule-result-profile-or-activation",
        }
        or result.get("promotion_authorized") is not False
        or result.get("candidate_selected") is not False
        or result.get("cycle_opened") is not False
    ):
        errors.append(CONSTRAINT_STATUS_READINESS_GATE_DRIFT)

    norm = payload.get("norm_vs_practice") or {}
    axes = norm.get("axes") or []
    if (
        {row.get("axis") for row in axes if isinstance(row, dict)} != PRACTICE_AXES
        or any(row.get("kind") != "discovery-practice-not-promotion-criterion" for row in axes if isinstance(row, dict))
    ):
        errors.append(CONSTRAINT_STATUS_READINESS_NORM_DRIFT)
    for source in norm.get("normative_sources") or ():
        try:
            text = (repo_root / source).read_text(encoding="utf-8")
        except OSError:
            text = ""
        if any(term in text for term in ("blocks-whole-document-freeze", "whole-document freeze", "bounded-stable-surface")):
            errors.append(CONSTRAINT_STATUS_READINESS_NORM_DRIFT)
    practice_path = repo_root / str(norm.get("practice_source", ""))
    try:
        practice_text = practice_path.read_text(encoding="utf-8")
    except OSError:
        practice_text = ""
    if any(str(row.get("token")) not in practice_text for row in axes if isinstance(row, dict)):
        errors.append(CONSTRAINT_STATUS_READINESS_NORM_DRIFT)

    governance = payload.get("governance_sweep") or {}
    governance_rows = governance.get("sources") or []
    if (
        governance.get("scope") != "all-current-foundation-governance-owners-and-machine-classification"
        or {row.get("source") for row in governance_rows if isinstance(row, dict)} != GOVERNANCE_SOURCES
    ):
        errors.append(CONSTRAINT_STATUS_READINESS_NORM_DRIFT)
    for row in governance_rows:
        try:
            source_text = (repo_root / str(row["source"])).read_text(encoding="utf-8")
        except (OSError, KeyError):
            source_text = ""
        if not row.get("role") or not row.get("tokens") or any(
            str(token) not in source_text for token in row.get("tokens") or ()
        ):
            errors.append(CONSTRAINT_STATUS_READINESS_NORM_DRIFT)

    criteria = payload.get("promotion_criteria") or []
    ids = [row.get("criterion_id") for row in criteria if isinstance(row, dict)]
    if len(ids) != len(CRITERION_IDS) or set(ids) != CRITERION_IDS:
        errors.append(CONSTRAINT_STATUS_READINESS_NORM_DRIFT)
    for row in criteria:
        if not isinstance(row, dict) or row.get("ocp006_assessment") != EXPECTED_ASSESSMENTS.get(row.get("criterion_id")):
            errors.append(CONSTRAINT_STATUS_READINESS_ASSESSMENT_DRIFT)
            continue
        try:
            source_text = (repo_root / str(row["source"])).read_text(encoding="utf-8")
        except (OSError, KeyError):
            source_text = ""
        if not row.get("tokens") or any(str(token) not in source_text for token in row.get("tokens") or ()):
            errors.append(CONSTRAINT_STATUS_READINESS_NORM_DRIFT)

    subject = _frontmatter(repo_root / SUBJECT_PATH) or {}
    assignment = _frontmatter(repo_root / ASSIGNMENT_PATH) or {}
    live = payload.get("ocp006_live_inputs") or {}
    subject_claim = payload.get("subject") or {}
    if (
        _hash(repo_root / SUBJECT_PATH) != SUBJECT_SHA256
        or subject.get("Document-ID") != "OCP-006"
        or subject.get("Version") != "0.3.2"
        or subject.get("Status") != "Draft"
        or subject.get("Concept-Status") != "Accepted"
        or _refs(subject.get("Depends-On")) != EXPECTED_DEPENDENCIES
        or assignment.get("Status") != "Draft"
        or live.get("direct_dependencies") != list(EXPECTED_DEPENDENCIES)
        or live.get("draft_direct_dependencies") != ["OCP-005"]
        or subject_claim != {
            "document_id": "OCP-006", "primary": str(SUBJECT_PATH), "version": "0.3.2",
            "status": "Draft", "concept_status": "Accepted", "changed": False,
        }
    ):
        errors.append(CONSTRAINT_STATUS_READINESS_SUBJECT_DRIFT)
    route = live.get("route_evidence") or {}
    try:
        route_text = (repo_root / str(route.get("source", ""))).read_text(encoding="utf-8")
    except OSError:
        route_text = ""
    if (
        route.get("token") not in route_text
        or "precedent guide, а не автоматична reclassification" not in route_text
        or route.get("force") != "precedent-guide-not-automatic-reclassification"
    ):
        errors.append(CONSTRAINT_STATUS_READINESS_ASSESSMENT_DRIFT)

    documents = _primary_documents(repo_root)
    promoted = {
        doc_id: item for doc_id, item in documents.items()
        if item[1].get("Status") in {"Accepted", "Canonical"}
    }
    sweep = payload.get("precedent_sweep") or {}
    carriers = sweep.get("carriers") or []
    claimed = {row.get("document_id"): row for row in carriers if isinstance(row, dict)}
    if len(promoted) != 23 or sweep.get("promoted_document_count") != len(promoted) or set(claimed) != set(PROMOTED_OPEN_CARRIERS):
        errors.append(CONSTRAINT_STATUS_READINESS_PRECEDENT_DRIFT)
    for doc_id, token in PROMOTED_OPEN_CARRIERS.items():
        item = promoted.get(doc_id)
        row = claimed.get(doc_id) or {}
        if not item or token not in item[2] or row.get("token") != token or row.get("status") != item[1].get("Status"):
            errors.append(CONSTRAINT_STATUS_READINESS_PRECEDENT_DRIFT)
    # Formal current Open Questions headings are a second, repository-wide control.
    formal = {
        doc_id for doc_id, (_, _, text) in promoted.items()
        if re.search(r"^##(?:\s+\d+\.)?\s+Open questions", text, flags=re.IGNORECASE | re.MULTILINE)
    }
    if formal != {"OCP-004", "OCP-008", "OCP-010"}:
        errors.append(CONSTRAINT_STATUS_READINESS_PRECEDENT_DRIFT)

    gate_payload = _load(repo_root / GATE_PATH)
    if not isinstance(gate_payload, dict) or gate_payload.get("cycle_protocol", {}).get("active_cycle_id") is not None:
        errors.append(CONSTRAINT_STATUS_READINESS_GATE_DRIFT)

    for item in payload.get("baseline_evidence_objects") or ():
        path = Path(str(item.get("path", "")))
        try:
            data = (repo_root / path).read_bytes()
            text = data.decode("utf-8")
        except (OSError, UnicodeDecodeError):
            errors.append(CONSTRAINT_STATUS_READINESS_EVIDENCE_DRIFT)
            continue
        if hashlib.sha256(data).hexdigest() != item.get("sha256") or any(
            str(token) not in text for token in item.get("state_tokens") or ()
        ):
            errors.append(CONSTRAINT_STATUS_READINESS_EVIDENCE_DRIFT)
    return _result(errors)
