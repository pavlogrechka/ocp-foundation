from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


ASSIGNMENT_STABLE_SURFACE_MAP_INVALID = "ASSIGNMENT_STABLE_SURFACE_MAP_INVALID"
ASSIGNMENT_STABLE_SURFACE_SUBJECT_DRIFT = "ASSIGNMENT_STABLE_SURFACE_SUBJECT_DRIFT"
ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT = "ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT"
ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT = "ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT"
ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT = "ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT"
ASSIGNMENT_STABLE_SURFACE_EVIDENCE_DRIFT = "ASSIGNMENT_STABLE_SURFACE_EVIDENCE_DRIFT"
ASSIGNMENT_STABLE_SURFACE_GATE_DRIFT = "ASSIGNMENT_STABLE_SURFACE_GATE_DRIFT"

CONCEPT_DEPENDENCY_IDS = frozenset({"Resource", "Operation"})
DIRECT_CONSUMER_IDS = frozenset(
    {"OCP-006", "OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021"}
)
ACCEPTED_CONSUMER_IDS = frozenset({"OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021"})
DRAFT_CONSUMER_IDS = frozenset({"OCP-006"})
QUESTION_IDS = frozenset({f"Q{number}" for number in range(1, 12)})
QUESTION_CLASSIFICATIONS = frozenset(
    {
        "outside-open-set",
        "blocks-whole-document-freeze",
        "local-after-bounded-freeze",
        "outside-bounded-surface",
    }
)
STABLE_SURFACE_IDS = frozenset(
    {
        "ASSIGNMENT_IDENTITY_REFERENCE_KERNEL",
        "TRANSITION_HISTORY_LIFECYCLE_KERNEL",
        "STRUCTURAL_ROLE_PROVENANCE_KERNEL",
        "NON_INHERITANCE_NON_AUTHORITY_BOUNDARY",
        "SUPERSESSION_IDENTITY_BOUNDARY",
        "EXECUTABLE_ASSIGNMENT_BOUNDARY",
    }
)
MOVING_SURFACE_IDS = frozenset(
    {
        "AMENDMENT_AFTER_ESTABLISHMENT",
        "TEMPORAL_EFFECTIVITY_EXTENSION",
        "ROLE_GOVERNANCE",
        "COMPOSITE_RESOURCE_SCOPE",
        "CONSTRAINT_CONFLICT_HANDOFF",
        "PROVENANCE_TAXONOMY",
        "REPLACEMENT_POLICY",
    }
)
BLOCKER_IDS = frozenset(
    {
        "AMENDMENT_MODEL_ABSENT",
        "TEMPORAL_MODEL_UNRESOLVED",
        "PARTIAL_SCOPE_IDENTITY_UNRESOLVED",
    }
)
FORBIDDEN_OUTCOMES = frozenset(
    {
        "ASSIGNMENT_SELECTION",
        "PROMOTION_CYCLE_START",
        "OCP005_PROMOTION",
        "ASSIGNMENT_CONCEPT_CANONICALIZATION",
        "OPEN_QUESTION_CLOSURE",
        "T7_OPEN",
    }
)

EXPECTED_CONCEPT_DEPENDENCIES = {
    "Resource": ("OCP-003", "Canonical", "Canonical"),
    "Operation": ("OCP-004", "Canonical", "Canonical"),
}
EXPECTED_CONSUMERS = {
    "OCP-006": (
        "docs/006-constraint-concept/README.md",
        "Draft",
        "draft",
        (
            "кілька ефективних Assignment одного Resource",
            "Сам `supersedes_assignment_ref` не визначає допустимі часові межі",
        ),
    ),
    "OCP-013": (
        "docs/013-resource-interchangeability/README.md",
        "Accepted",
        "accepted",
        (
            "retain every exclusion of availability, authorization, ranking, selection, replacement and Assignment mutation",
        ),
    ),
    "OCP-015": (
        "docs/015-coordination-workflow/README.md",
        "Accepted",
        "accepted",
        ("preserves Resource and Assignment identity", "alter Resource or Assignment identity"),
    ),
    "OCP-017": (
        "docs/017-operation-lifecycle/README.md",
        "Accepted",
        "accepted",
        (
            "if OCP-005 `assignment_effective_at` is true at that instant",
            "whose `operation_ref` names the Operation",
            "never edits an Assignment transition history",
        ),
    ),
    "OCP-020": (
        "docs/020-quantitative-constraint-input/README.md",
        "Accepted",
        "accepted",
        (
            "create, amend, activate, suspend or terminate an Assignment",
            "Existing Resource, Operation, Assignment and Constraint artifacts remain valid",
        ),
    ),
    "OCP-021": (
        "docs/021-reservation-allocation-boundary/README.md",
        "Accepted",
        "accepted",
        (
            "Their truth remains owned by OCP-005/OCP-006",
            "creates, blocks, cancels, supersedes or mutates an Assignment",
        ),
    ),
}
EXPECTED_QUESTIONS = {
    "Q1": ("resolved-historical", "outside-open-set", "RESERVATION_OBJECT_FORM", "Чи потрібен окремий фундаментальний Concept `Reservation`"),
    "Q2": ("open", "blocks-whole-document-freeze", "AMENDMENT_AFTER_ESTABLISHMENT", "Яка amendment model потрібна для зміни role або applicability після Establishment?"),
    "Q3": ("open", "blocks-whole-document-freeze", "RETROACTIVE_ESTABLISHMENT", "Чи допускається ретроактивне Establishment Assignment?"),
    "Q4": ("open", "local-after-bounded-freeze", "ROLE_TAXONOMY", "Чи потрібна окрема Role Taxonomy у Core?"),
    "Q5": ("open", "blocks-whole-document-freeze", "COMPOSITE_RESOURCE_SCOPE", "Чи повинен Assignment мати окремий scope для частини складеного Resource"),
    "Q6": ("resolved-historical", "outside-open-set", "QUANTITATIVE_INPUT", "Як представляти кількість Consumable Resource, зарезервовану або спожиту в Operation?"),
    "Q7": ("open", "local-after-bounded-freeze", "ROLE_SPECIALIZATIONS", "Чи потрібен окремий тип Assignment для coordination, approval або observation roles?"),
    "Q8": ("open", "outside-bounded-surface", "CONSTRAINT_CONFLICT_HANDOFF", "Як Constraint визначає конфлікт одночасних Assignment?"),
    "Q9": ("open", "blocks-whole-document-freeze", "MULTIPLE_APPLICABILITY_INTERVALS", "Чи може один Assignment мати кілька неперервних applicability intervals"),
    "Q10": ("open", "local-after-bounded-freeze", "PROVENANCE_TAXONOMY", "Які provenance types повинні бути канонічними"),
    "Q11": ("open", "local-after-bounded-freeze", "REPLACEMENT_POLICY", "Яка replacement policy визначає допустимі overlap і gap"),
}
EXPECTED_EVIDENCE = {
    "ASSIGNMENT_IDENTITY_REFERENCE_KERNEL": (("docs/005-assignment-concept/README.md", ("## 5. Identity", "його `resource_ref` і `operation_ref` не змінюються")),),
    "TRANSITION_HISTORY_LIFECYCLE_KERNEL": (("docs/005-assignment-concept/README.md", ("## 7. Working Lifecycle", "### 7.6 Authoritative transition history", "рівно один із допустимих лінійних шляхів")),),
    "STRUCTURAL_ROLE_PROVENANCE_KERNEL": (("docs/005-assignment-concept/README.md", ("## 6. Minimum Structural Contract", "### 6.2 RoleSpecification", "### 6.4 Provenance")),),
    "NON_INHERITANCE_NON_AUTHORITY_BOUNDARY": (("docs/005-assignment-concept/README.md", ("## 11. Composition and Non-Inheritance", "Assignment не означає автоматично", "Встановлення Assignment не підтверджує Readiness")),),
    "SUPERSESSION_IDENTITY_BOUNDARY": (("docs/005-assignment-concept/README.md", ("## 12. Replacement and Supersession", "саме по собі не завершує, не відкликає")),),
    "EXECUTABLE_ASSIGNMENT_BOUNDARY": (
        ("tools/ontology_checker/ocp_checker/checker.py", ("def validate_assignment(", "def assignment_effective_at(", "def derived_participates_in(")),
        ("tools/ontology_checker/rules.yaml", ("source: OCP-005 §8", "source: OCP-005 §9")),
    ),
}
EXPECTED_MOVING = {
    "AMENDMENT_AFTER_ESTABLISHMENT": ("moving", ("Q2",)),
    "TEMPORAL_EFFECTIVITY_EXTENSION": ("moving", ("Q3", "Q9")),
    "ROLE_GOVERNANCE": ("moving", ("Q4", "Q7")),
    "COMPOSITE_RESOURCE_SCOPE": ("moving", ("Q5",)),
    "CONSTRAINT_CONFLICT_HANDOFF": ("moving-external-owner", ("Q8",)),
    "PROVENANCE_TAXONOMY": ("moving", ("Q10",)),
    "REPLACEMENT_POLICY": ("moving", ("Q11",)),
}
EXPECTED_BLOCKERS = {
    "AMENDMENT_MODEL_ABSENT": ("blocks-whole-document-freeze", ("Q2",), ()),
    "TEMPORAL_MODEL_UNRESOLVED": ("blocks-whole-document-freeze", ("Q3", "Q9"), ()),
    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": ("blocks-whole-document-freeze", ("Q5",), ()),
}
EXPECTED_BASELINE_EVIDENCE_OBJECTS = {
    "docs/005-assignment-concept/README.md": ("6e6c00e723b15a348e7610d4ca5a1ae23526c52b", "a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065"),
    "docs/006-constraint-concept/README.md": ("50f149cf5563083bb84d5d2197ec32c2ed15fa9b", "0472d8ce4b15a8c64d58151ee7f706b450b930f708f6f0a7a40bdd87914b3b10"),
    "docs/013-resource-interchangeability/README.md": ("658a291b4c3b9a0229aba09d485c1137723fe70b", "a20659422f847f49a9231b8c1d1dabc0d8b911d9667c44013280b1826f621a74"),
    "docs/015-coordination-workflow/README.md": ("ea60634e54faedabb8c5e08b036030c2f0e4e20b", "6077136b2460cfc56d0e06af9137338cb494ac9a8e14df036e662d9240415b1d"),
    "docs/017-operation-lifecycle/README.md": ("0b2ea683df308babd1111ff47e9272c9b0742f78", "061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030"),
    "docs/020-quantitative-constraint-input/README.md": ("0e1e7d0947ab3c7d1c0355258651179f618636a2", "1783c32094aee9f09ca50ececb12bf9ec8f3c6599590331dba3894ad727d9b5c"),
    "docs/021-reservation-allocation-boundary/README.md": ("af96e2a9a67977cf5de8c4c566b1e9293e23687f", "85cdc7e3bb5281a6b2fe0af4d11b31bc47040b762de5786a0a8a10c2e000f683"),
    "tools/ontology_checker/ocp_checker/checker.py": ("120ada9dd00b1df0b46cf3060aef2b0c290948b1", "3a093f0d76113bb5dd2799c7d0aaf73b51b752569dc13de145bb3d158a7b4a47"),
    "tools/ontology_checker/rules.yaml": ("8d00050e32cea2ceb27d13c3d7788b5e8554cc84", "e861e860f576cf824aff755d99f0da3118256f20d742f25eb4b0434503c6042d"),
}

MAP_KEYS = {
    "schema_version", "rule_owner", "baseline", "gate_first", "promotion_gate_guard",
    "baseline_evidence_objects", "subject", "concept_dependencies", "direct_consumers",
    "open_question_inventory", "stable_candidates", "moving_surfaces", "blockers",
    "forbidden_outcomes",
}


@dataclass(frozen=True)
class AssignmentStableSurfaceResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _result(errors: Iterable[str]) -> AssignmentStableSurfaceResult:
    return AssignmentStableSurfaceResult(tuple(dict.fromkeys(errors)))


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


def _numbered_section(text: str, start_heading: str, end_heading: str) -> tuple[str, ...]:
    start = text.find(start_heading)
    if start < 0:
        return ()
    end = text.find(end_heading, start + len(start_heading))
    if end < 0:
        return ()
    return tuple(
        line.strip() for line in text[start:end].splitlines()
        if line.strip() and line.lstrip().split(".", 1)[0].isdigit()
    )


def _ocp_index(repo_root: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    result: dict[str, tuple[Path, dict[str, Any]]] = {}
    for path in sorted((repo_root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
        metadata = _frontmatter(path)
        if metadata is not None and isinstance(metadata.get("Document-ID"), str):
            result[str(metadata["Document-ID"])] = (path, metadata)
    return result


def _normalize_evidence(entries: Any) -> tuple[dict[str, tuple[tuple[str, tuple[str, ...]], ...]], bool]:
    result: dict[str, tuple[tuple[str, tuple[str, ...]], ...]] = {}
    if not isinstance(entries, list):
        return result, False
    valid = True
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {"surface_id", "disposition", "evidence"}:
            valid = False
            continue
        entry_id = entry.get("surface_id")
        evidence = entry.get("evidence")
        if not isinstance(entry_id, str) or not isinstance(evidence, list) or not evidence:
            valid = False
            continue
        normalized: list[tuple[str, tuple[str, ...]]] = []
        for item in evidence:
            if not isinstance(item, dict) or set(item) != {"path", "tokens"}:
                valid = False
                continue
            path, tokens = item.get("path"), item.get("tokens")
            if not isinstance(path, str) or Path(path).is_absolute() or ".." in Path(path).parts:
                valid = False
                continue
            if (
                not isinstance(tokens, list)
                or not tokens
                or len(tokens) != len(set(tokens))
                or any(not isinstance(token, str) or not token for token in tokens)
            ):
                valid = False
                continue
            normalized.append((path, tuple(tokens)))
        if entry_id in result:
            valid = False
        result[entry_id] = tuple(normalized)
    return result, valid


def _source_tokens_present(repo_root: Path, evidence: dict[str, tuple[tuple[str, tuple[str, ...]], ...]]) -> bool:
    for items in evidence.values():
        for relative, tokens in items:
            try:
                text = (repo_root / relative).read_text(encoding="utf-8")
            except OSError:
                return False
            if any(token not in text for token in tokens):
                return False
    return True


def validate_assignment_stable_surface(repo_root: Path) -> AssignmentStableSurfaceResult:
    errors: list[str] = []
    try:
        payload = yaml.safe_load(
            (repo_root / "architecture/assignment-stable-surface.yaml").read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        return _result((ASSIGNMENT_STABLE_SURFACE_MAP_INVALID,))
    if not isinstance(payload, dict) or set(payload) != MAP_KEYS:
        return _result((ASSIGNMENT_STABLE_SURFACE_MAP_INVALID,))

    if (
        payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-035"
        or payload.get("baseline") != "6e83f34292fa818f62b1170e4b77aae98515a9a8"
        or payload.get("gate_first") != {
            "ocp016_gate": "G4",
            "applies": False,
            "reason": "discovery-evidence-is-not-a-positive-capable-rule-result-or-profile",
            "accepted_consumer_activation_required": False,
        }
        or payload.get("promotion_gate_guard") != {
            "schema_version": 5,
            "completed_cycle_ids": ["EVENT_T6"],
            "active_cycle_id": None,
        }
    ):
        errors.append(ASSIGNMENT_STABLE_SURFACE_MAP_INVALID)

    baseline_objects = payload.get("baseline_evidence_objects")
    normalized_objects: dict[str, tuple[str, str]] = {}
    if isinstance(baseline_objects, list):
        for item in baseline_objects:
            if not isinstance(item, dict) or set(item) != {"path", "blob", "sha256"}:
                errors.append(ASSIGNMENT_STABLE_SURFACE_EVIDENCE_DRIFT)
                continue
            path = item.get("path")
            if not isinstance(path, str) or path in normalized_objects:
                errors.append(ASSIGNMENT_STABLE_SURFACE_EVIDENCE_DRIFT)
                continue
            normalized_objects[path] = (str(item.get("blob")), str(item.get("sha256")))
    else:
        errors.append(ASSIGNMENT_STABLE_SURFACE_EVIDENCE_DRIFT)
    if normalized_objects != EXPECTED_BASELINE_EVIDENCE_OBJECTS:
        errors.append(ASSIGNMENT_STABLE_SURFACE_EVIDENCE_DRIFT)

    ocps = _ocp_index(repo_root)
    subject = payload.get("subject")
    resolved_subject = ocps.get("OCP-005")
    if not isinstance(subject, dict) or resolved_subject is None:
        errors.append(ASSIGNMENT_STABLE_SURFACE_SUBJECT_DRIFT)
    else:
        primary, metadata = resolved_subject
        if (
            subject != {
                "document_id": "OCP-005",
                "primary": "docs/005-assignment-concept/README.md",
                "expected_version": "0.2.8",
                "expected_status": "Draft",
                "expected_concept_status": "Accepted",
                "discovery_result": "bounded_stable_candidate_not_selected",
            }
            or primary != repo_root / "docs/005-assignment-concept/README.md"
            or str(metadata.get("Version")) != "0.2.8"
            or metadata.get("Status") != "Draft"
            or metadata.get("Concept-Status") != "Accepted"
        ):
            errors.append(ASSIGNMENT_STABLE_SURFACE_SUBJECT_DRIFT)

    dependencies = payload.get("concept_dependencies")
    dependency_ids: list[str] = []
    if not isinstance(dependencies, list):
        errors.append(ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT)
        dependencies = []
    for entry in dependencies:
        if not isinstance(entry, dict) or set(entry) != {
            "concept", "defining_document", "expected_document_status",
            "expected_concept_status", "consequence",
        }:
            errors.append(ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT)
            continue
        concept = str(entry.get("concept"))
        dependency_ids.append(concept)
        expected = EXPECTED_CONCEPT_DEPENDENCIES.get(concept)
        if expected is None:
            errors.append(ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT)
            continue
        document_id, document_status, concept_status = expected
        resolved = ocps.get(document_id)
        if (
            entry.get("defining_document") != document_id
            or entry.get("expected_document_status") != document_status
            or entry.get("expected_concept_status") != concept_status
            or entry.get("consequence") != "dependency-floor-passes-without-freezing-assignment"
            or resolved is None
            or resolved[1].get("Status") != document_status
            or resolved[1].get("Concept-Status") != concept_status
        ):
            errors.append(ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT)
    if set(dependency_ids) != CONCEPT_DEPENDENCY_IDS or len(dependency_ids) != len(set(dependency_ids)):
        errors.append(ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT)
    if resolved_subject is not None and set(_references(resolved_subject[1].get("Concept-Depends-On"))) != CONCEPT_DEPENDENCY_IDS:
        errors.append(ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT)

    consumers = payload.get("direct_consumers")
    consumer_ids: list[str] = []
    if not isinstance(consumers, list):
        errors.append(ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT)
        consumers = []
    for entry in consumers:
        if not isinstance(entry, dict) or set(entry) != {
            "document_id", "primary", "expected_status", "lifecycle_class", "consumed_elements"
        }:
            errors.append(ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT)
            continue
        document_id = str(entry.get("document_id"))
        consumer_ids.append(document_id)
        expected = EXPECTED_CONSUMERS.get(document_id)
        resolved = ocps.get(document_id)
        if expected is None or resolved is None:
            errors.append(ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT)
            continue
        expected_path, status, lifecycle_class, elements = expected
        try:
            text = resolved[0].read_text(encoding="utf-8")
        except OSError:
            text = ""
        if (
            entry.get("primary") != expected_path
            or resolved[0] != repo_root / expected_path
            or entry.get("expected_status") != status
            or resolved[1].get("Status") != status
            or entry.get("lifecycle_class") != lifecycle_class
            or tuple(entry.get("consumed_elements") or ()) != elements
            or any(token not in text for token in elements)
        ):
            errors.append(ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT)
    actual_consumers = {
        document_id
        for document_id, (_, metadata) in ocps.items()
        if "OCP-005" in _references(metadata.get("Depends-On"))
    }
    if (
        set(consumer_ids) != DIRECT_CONSUMER_IDS
        or len(consumer_ids) != len(set(consumer_ids))
        or actual_consumers != DIRECT_CONSUMER_IDS
    ):
        errors.append(ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT)
    if {
        item["document_id"] for item in consumers if isinstance(item, dict) and item.get("lifecycle_class") == "accepted"
    } != ACCEPTED_CONSUMER_IDS:
        errors.append(ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT)
    if {
        item["document_id"] for item in consumers if isinstance(item, dict) and item.get("lifecycle_class") == "draft"
    } != DRAFT_CONSUMER_IDS:
        errors.append(ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT)

    questions = payload.get("open_question_inventory")
    question_ids: list[str] = []
    try:
        subject_text = (repo_root / "docs/005-assignment-concept/README.md").read_text(encoding="utf-8")
    except OSError:
        subject_text = ""
    current_question_lines = _numbered_section(
        subject_text,
        "## 19. Open Questions and Resolved Boundaries",
        "## 20. Deferred Decisions",
    )
    if not isinstance(questions, list):
        errors.append(ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT)
        questions = []
    for entry in questions:
        if not isinstance(entry, dict) or set(entry) != {
            "question_id", "state", "classification", "surface", "evidence_token"
        }:
            errors.append(ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT)
            continue
        question_id = str(entry.get("question_id"))
        question_ids.append(question_id)
        expected = EXPECTED_QUESTIONS.get(question_id)
        actual = (
            entry.get("state"), entry.get("classification"), entry.get("surface"), entry.get("evidence_token")
        )
        matching_lines = [line for line in current_question_lines if str(entry.get("evidence_token")) in line]
        expected_resolved = entry.get("state") == "resolved-historical"
        if (
            expected is None
            or actual != expected
            or entry.get("classification") not in QUESTION_CLASSIFICATIONS
            or len(matching_lines) != 1
            or (("~~" in matching_lines[0]) if matching_lines else False) != expected_resolved
        ):
            errors.append(ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT)
    if set(question_ids) != QUESTION_IDS or len(question_ids) != len(set(question_ids)):
        errors.append(ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT)
    if (
        len(current_question_lines) != 11
        or sum(1 for item in questions if isinstance(item, dict) and item.get("state") == "open") != 9
    ):
        errors.append(ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT)

    evidence, evidence_shape_valid = _normalize_evidence(payload.get("stable_candidates"))
    if (
        not evidence_shape_valid
        or set(evidence) != STABLE_SURFACE_IDS
        or len(payload.get("stable_candidates", [])) != len(STABLE_SURFACE_IDS)
        or evidence != EXPECTED_EVIDENCE
        or not _source_tokens_present(repo_root, evidence)
        or any(item.get("disposition") != "candidate" for item in payload.get("stable_candidates", []) if isinstance(item, dict))
    ):
        errors.append(ASSIGNMENT_STABLE_SURFACE_EVIDENCE_DRIFT)

    moving = payload.get("moving_surfaces")
    normalized_moving: dict[str, tuple[str, tuple[str, ...]]] = {}
    if isinstance(moving, list):
        for entry in moving:
            if not isinstance(entry, dict) or set(entry) != {"surface_id", "disposition", "question_ids"}:
                errors.append(ASSIGNMENT_STABLE_SURFACE_MAP_INVALID)
                continue
            normalized_moving[str(entry.get("surface_id"))] = (
                str(entry.get("disposition")), tuple(entry.get("question_ids") or ())
            )
    else:
        errors.append(ASSIGNMENT_STABLE_SURFACE_MAP_INVALID)
    if (
        set(normalized_moving) != MOVING_SURFACE_IDS
        or (len(moving) if isinstance(moving, list) else -1) != len(MOVING_SURFACE_IDS)
        or normalized_moving != EXPECTED_MOVING
    ):
        errors.append(ASSIGNMENT_STABLE_SURFACE_MAP_INVALID)

    blockers = payload.get("blockers")
    normalized_blockers: dict[str, tuple[str, tuple[str, ...], tuple[str, ...]]] = {}
    if isinstance(blockers, list):
        for entry in blockers:
            if not isinstance(entry, dict):
                errors.append(ASSIGNMENT_STABLE_SURFACE_MAP_INVALID)
                continue
            keys = set(entry)
            if keys not in (
                {"blocker_id", "disposition", "question_ids"},
                {"blocker_id", "disposition", "consumer_ids"},
            ):
                errors.append(ASSIGNMENT_STABLE_SURFACE_MAP_INVALID)
                continue
            normalized_blockers[str(entry.get("blocker_id"))] = (
                str(entry.get("disposition")),
                tuple(entry.get("question_ids") or ()),
                tuple(entry.get("consumer_ids") or ()),
            )
    else:
        errors.append(ASSIGNMENT_STABLE_SURFACE_MAP_INVALID)
    if (
        set(normalized_blockers) != BLOCKER_IDS
        or (len(blockers) if isinstance(blockers, list) else -1) != len(BLOCKER_IDS)
        or normalized_blockers != EXPECTED_BLOCKERS
    ):
        errors.append(ASSIGNMENT_STABLE_SURFACE_MAP_INVALID)

    forbidden = payload.get("forbidden_outcomes")
    if not isinstance(forbidden, list) or set(forbidden) != FORBIDDEN_OUTCOMES or len(forbidden) != len(FORBIDDEN_OUTCOMES):
        errors.append(ASSIGNMENT_STABLE_SURFACE_MAP_INVALID)

    try:
        gate = yaml.safe_load(
            (repo_root / "architecture/foundation-promotion-gate.yaml").read_text(encoding="utf-8")
        )
    except (OSError, yaml.YAMLError):
        gate = None
    if not isinstance(gate, dict):
        errors.append(ASSIGNMENT_STABLE_SURFACE_GATE_DRIFT)
    else:
        cycles = gate.get("cycles")
        completed = [
            item.get("cycle_id")
            for item in cycles if isinstance(item, dict)
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
            errors.append(ASSIGNMENT_STABLE_SURFACE_GATE_DRIFT)

    return _result(errors)
