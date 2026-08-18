from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
from typing import Any, Iterable

import yaml

from ._common import nonempty, result
from .checker import ValidationResult


ASSIGNMENT_NORM_MAP_INVALID = "ASSIGNMENT_NORM_MAP_INVALID"
ASSIGNMENT_NORM_SURVIVOR_DRIFT = "ASSIGNMENT_NORM_SURVIVOR_DRIFT"
ASSIGNMENT_NORM_SOURCE_DRIFT = "ASSIGNMENT_NORM_SOURCE_DRIFT"
ASSIGNMENT_NORM_PROBE_DRIFT = "ASSIGNMENT_NORM_PROBE_DRIFT"
ASSIGNMENT_NORM_GATE_DRIFT = "ASSIGNMENT_NORM_GATE_DRIFT"

ASSIGNMENT_NORM_FIXTURE_INVALID = "ASSIGNMENT_NORM_FIXTURE_INVALID"
ASSIGNMENT_NORM_RESOLUTION_INVALID = "ASSIGNMENT_NORM_RESOLUTION_INVALID"
ASSIGNMENT_NORM_CLAIM_INVALID = "ASSIGNMENT_NORM_CLAIM_INVALID"
ASSIGNMENT_NORM_RESULT_MISMATCH = "ASSIGNMENT_NORM_RESULT_MISMATCH"
ASSIGNMENT_NORM_FORBIDDEN_OUTCOME = "ASSIGNMENT_NORM_FORBIDDEN_OUTCOME"

ASSIGNMENT_NORM_ERROR_CODES = frozenset(
    {
        ASSIGNMENT_NORM_FIXTURE_INVALID,
        ASSIGNMENT_NORM_RESOLUTION_INVALID,
        ASSIGNMENT_NORM_CLAIM_INVALID,
        ASSIGNMENT_NORM_RESULT_MISMATCH,
        ASSIGNMENT_NORM_FORBIDDEN_OUTCOME,
    }
)

MAP_PATH = Path("architecture/assignment-norm-compatibility.yaml")
PRESSURE_MAP_PATH = Path("architecture/assignment-consumer-pressure.yaml")
SURFACE_PATH = Path("architecture/assignment-stable-surface.yaml")
GATE_PATH = Path("architecture/foundation-promotion-gate.yaml")
FIXTURE_ROOT = Path("tools/ontology_checker/fixtures/assignment_norm_compatibility")

BASELINE = "734dd019425b636f47187bf1c342612550028400"
CURRENT_DOCUMENT_STATUSES = frozenset({"Draft", "Accepted", "Canonical"})
COMPATIBLE = "compatible"
INCOMPATIBLE = "incompatible"
UNDERDETERMINED = "underdetermined"
ANALYTIC = "analytic"

BLOCKER_QUESTIONS = {
    "AMENDMENT_MODEL_ABSENT": ("Q2",),
    "TEMPORAL_MODEL_UNRESOLVED": ("Q3", "Q9"),
    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED": ("Q5",),
}

SURVIVOR_CLAIMS = {
    "SUPERSEDING_ASSIGNMENT_FOR_CHANGE": {
        "resource_cardinality": "one",
        "automatic_component_inheritance": "false",
        "post_establishment_change_model": "superseding-assignment",
    },
    "POST_ESTABLISHMENT_IMMUTABILITY": {
        "resource_cardinality": "one",
        "automatic_component_inheritance": "false",
        "post_establishment_change_model": "immutable-role-and-applicability",
    },
    "PROSPECTIVE_ONLY_SINGLE_INTERVAL": {
        "resource_cardinality": "one",
        "retroactivity_policy": "prospective-only",
        "interval_cardinality": "single",
    },
    "PROSPECTIVE_ONLY_MULTIPLE_INTERVALS": {
        "resource_cardinality": "one",
        "retroactivity_policy": "prospective-only",
        "interval_cardinality": "multiple",
    },
    "WHOLE_RESOURCE_ONLY": {
        "resource_cardinality": "one",
        "automatic_component_inheritance": "false",
    },
    "EXPLICIT_PART_SCOPE_ON_ASSIGNMENT": {
        "resource_cardinality": "one",
        "automatic_component_inheritance": "false",
        "part_scope_representation": "explicit-under-resource",
    },
}

SURVIVOR_BLOCKERS = {
    "SUPERSEDING_ASSIGNMENT_FOR_CHANGE": "AMENDMENT_MODEL_ABSENT",
    "POST_ESTABLISHMENT_IMMUTABILITY": "AMENDMENT_MODEL_ABSENT",
    "PROSPECTIVE_ONLY_SINGLE_INTERVAL": "TEMPORAL_MODEL_UNRESOLVED",
    "PROSPECTIVE_ONLY_MULTIPLE_INTERVALS": "TEMPORAL_MODEL_UNRESOLVED",
    "WHOLE_RESOURCE_ONLY": "PARTIAL_SCOPE_IDENTITY_UNRESOLVED",
    "EXPLICIT_PART_SCOPE_ON_ASSIGNMENT": "PARTIAL_SCOPE_IDENTITY_UNRESOLVED",
}

NORMATIVE_STATEMENTS = {
    "ASSIGNMENT_EXACT_ONE_RESOURCE_OPERATION": {
        "path": "docs/002-concept-taxonomy/README.md",
        "status": "Canonical",
        "section": "Assignment",
        "quote": "Assignment є ідентифікованим контекстним зв’язком рівно одного Resource з рівно однією Operation.",
        "axis": "resource_cardinality",
        "effect": "allow-only:one",
    },
    "COMPONENT_ASSIGNMENT_NON_INHERITANCE": {
        "path": "docs/003-resource-concept/README.md",
        "status": "Canonical",
        "section": "7. Component identity and non-inheritance",
        "quote": "Composite Assignment не створює Assignment або participation для component автоматично.",
        "axis": "automatic_component_inheritance",
        "effect": "forbid:true",
    },
    "COMPOSITION_REPRESENTATION_DEFERRED": {
        "path": "docs/003-resource-concept/README.md",
        "status": "Canonical",
        "section": "7. Component identity and non-inheritance",
        "quote": "Цей kernel не визначає record shape, directionality, effectivity, cycle rules або authority для `contains`, `part_of` чи іншої composition relation.",
        "axis": "part_scope_representation",
        "effect": "underdetermined",
    },
    "ASSIGNMENT_OWNS_IDENTITY_INTERVAL_LIFECYCLE": {
        "path": "docs/004-operation-concept/README.md",
        "status": "Canonical",
        "section": "10. Participation and Assignment",
        "quote": "Кожен Assignment пов’язує рівно один Resource з рівно однією Operation, має власну ідентичність, RoleSpecification, applicability interval та lifecycle record.",
        "axis": "resource_cardinality",
        "effect": "allow-only:one",
    },
    "ASSIGNMENT_CHANGE_REQUIRES_SEPARATE_OWNER": {
        "path": "docs/017-operation-lifecycle/README.md",
        "status": "Accepted",
        "section": "10. T1 terminal Assignment alignment",
        "quote": "Any such lifecycle coordination requires a separate owner and Board act.",
        "axis": "post_establishment_change_model",
        "effect": "underdetermined",
    },
    "ASSIGNMENT_AMENDMENT_MODEL_OPEN": {
        "path": "docs/005-assignment-concept/README.md",
        "status": "Draft",
        "section": "14. Business Rules",
        "quote": "6. Зміна ролі або applicability після Establishment повинна бути простежуваною. Остаточна amendment model залишається відкритою.",
        "axis": "post_establishment_change_model",
        "effect": "underdetermined",
    },
    "ASSIGNMENT_PROSPECTIVE_EFFECTIVITY_BOUNDARY": {
        "path": "docs/005-assignment-concept/README.md",
        "status": "Draft",
        "section": "8. Temporal Effectivity",
        "quote": "До окремого рішення про ретроактивне Establishment Assignment не може бути ефективним для часу раніше `established_at`.",
        "axis": "retroactivity_policy",
        "effect": "allow-only:prospective-only",
    },
    "CONSUMER_INTERVAL_CARDINALITY_NOT_DEFINED": {
        "path": "docs/023-resource-occupancy/README.md",
        "status": "Accepted",
        "section": "7. Time and multiplicity boundaries",
        "quote": "It neither defines retroactivity nor multiple applicability intervals.",
        "axis": "interval_cardinality",
        "effect": "underdetermined",
    },
}

AXIS_POLICIES = {
    "resource_cardinality": {
        "kind": "allow-only",
        "values": ("one",),
        "statement_ids": (
            "ASSIGNMENT_EXACT_ONE_RESOURCE_OPERATION",
            "ASSIGNMENT_OWNS_IDENTITY_INTERVAL_LIFECYCLE",
        ),
    },
    "automatic_component_inheritance": {
        "kind": "forbid",
        "values": ("true",),
        "statement_ids": ("COMPONENT_ASSIGNMENT_NON_INHERITANCE",),
    },
    "post_establishment_change_model": {
        "kind": "underdetermined",
        "values": (),
        "statement_ids": (
            "ASSIGNMENT_AMENDMENT_MODEL_OPEN",
            "ASSIGNMENT_CHANGE_REQUIRES_SEPARATE_OWNER",
        ),
    },
    "retroactivity_policy": {
        "kind": "allow-only",
        "values": ("prospective-only",),
        "statement_ids": ("ASSIGNMENT_PROSPECTIVE_EFFECTIVITY_BOUNDARY",),
    },
    "interval_cardinality": {
        "kind": "underdetermined",
        "values": (),
        "statement_ids": ("CONSUMER_INTERVAL_CARDINALITY_NOT_DEFINED",),
    },
    "part_scope_representation": {
        "kind": "underdetermined",
        "values": (),
        "statement_ids": ("COMPOSITION_REPRESENTATION_DEFERRED",),
    },
}

SWEEP_DOCUMENT_STATUSES = ("Draft", "Accepted", "Canonical")
SWEEP_VOCABULARY = {
    "resource_cardinality": (
        ("assignment", "рівно одного resource", "рівно однією operation"),
        ("assignment", "рівно один resource", "рівно однією operation"),
        ("assignment", "one resource", "one operation"),
    ),
    "automatic_component_inheritance": (
        ("assignment", "успадков"),
        ("assignment", "inherit"),
        ("composite assignment", "component", "автоматично"),
    ),
    "post_establishment_change_model": (
        ("assignment", "amend"),
        ("supersedes_assignment_ref",),
        ("superseding assignment",),
        ("assignment", "immutab"),
        ("assignment", "traceab"),
        ("assignment", "простежув"),
        ("role_code", "immutab"),
        ("role_code", "change"),
        ("applicability", "immutab"),
        ("applicability", "amend"),
        ("applicability", "supersed"),
        ("зміна ролі", "applicability"),
        ("після встановлення assignment",),
        ("established assignment", "замін"),
        ("established assignment", "редагув"),
    ),
    "retroactivity_policy": (("retroactiv",), ("ретроактив",)),
    "interval_cardinality": (
        ("applicability interval",),
        ("кілька неперервних applicability interval",),
    ),
    "part_scope_representation": (
        ("part_scope",),
        ("part scope",),
        ("partial scope",),
        ("assignment", "component"),
        ("assignment", "composite"),
        ("assignment", "composition"),
        ("`contains`", "`part_of`"),
    ),
}
SOURCE_SWEEP_SHA256 = "a747871ba4a3e4e413c65eabc0b72ba632ab2256a322714a7b303e1850dcf6db"

EXPECTED_GATE_FIRST = {
    "ocp016_gate": "G4",
    "applies": False,
    "reason": "norm-compatibility-discovery-creates-no-positive-capable-rule-result-profile-or-activation",
    "hypothetical_lifecycle_resolution_still_requires_its_own_gate": True,
}
EXPECTED_CRITERION = {
    "order": ["incompatible", "underdetermined", "compatible"],
    "incompatible": "a-current-accepted-or-canonical-statement-is-violated",
    "underdetermined": "a-defining-axis-is-explicitly-unowned-or-deferred-by-current-norm",
    "compatible": "every-defining-axis-is-addressed-and-no-current-statement-is-violated",
    "source_floor": ["current-primary-body"],
    "historical_and_baseline_sources_forbidden": True,
}
FORBIDDEN_FIELDS = frozenset(
    {
        "selected_resolution",
        "blocker_removed",
        "question_resolved",
        "ocp005_change",
        "positive_activation",
        "promotion_cycle_id",
        "concept_status",
    }
)
FORBIDDEN_OUTCOMES = frozenset(
    {
        "ASSIGNMENT_RULE_SELECTION",
        "BLOCKER_REMOVAL",
        "CONCEPT_OR_GRAPH_CHANGE",
        "NEXT_ACT_AUTHORIZATION",
        "OCP005_CHANGE",
        "OPEN_QUESTION_RESOLUTION",
        "POSITIVE_MODEL_ACTIVATION",
        "PROMOTION_CYCLE_START",
    }
)
PROBE_FIELDS = frozenset(
    {
        "probe_id",
        "blocker_id",
        "question_ids",
        "resolution_id",
        "claims",
        "source_statement_ids",
        "evidence_mode",
        "stored_classification",
        "stored_violation_statement_ids",
        "stored_underdetermined_axes",
    }
)


@dataclass(frozen=True)
class AssignmentNormCompatibilityResult:
    classification: str | None
    violation_statement_ids: tuple[str, ...]
    underdetermined_axes: tuple[str, ...]


@dataclass(frozen=True)
class AssignmentNormCompatibilityMapResult:
    errors: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.errors


def _map_result(errors: Iterable[str]) -> AssignmentNormCompatibilityMapResult:
    return AssignmentNormCompatibilityMapResult(tuple(dict.fromkeys(errors)))


def _contains_named(value: Any, names: frozenset[str]) -> bool:
    if isinstance(value, dict):
        return any(key in names or _contains_named(item, names) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_named(item, names) for item in value)
    return False


def _source_ids_for_claims(claims: dict[str, Any]) -> tuple[str, ...]:
    ids = {
        statement_id
        for axis in claims
        for statement_id in AXIS_POLICIES.get(axis, {}).get("statement_ids", ())
    }
    return tuple(sorted(ids))


def derive_assignment_norm_compatibility(
    probe: Any,
) -> AssignmentNormCompatibilityResult:
    empty = AssignmentNormCompatibilityResult(None, (), ())
    if not isinstance(probe, dict) or _contains_named(probe, FORBIDDEN_FIELDS):
        return empty
    claims = probe.get("claims")
    if not isinstance(claims, dict) or not claims or any(
        axis not in AXIS_POLICIES or not nonempty(value) for axis, value in claims.items()
    ):
        return empty

    violations: set[str] = set()
    underdetermined: set[str] = set()
    for axis, value in claims.items():
        policy = AXIS_POLICIES[axis]
        if policy["kind"] == "allow-only" and value not in policy["values"]:
            violations.update(policy["statement_ids"])
        elif policy["kind"] == "forbid" and value in policy["values"]:
            violations.update(policy["statement_ids"])
        elif policy["kind"] == "underdetermined":
            underdetermined.add(axis)

    classification = (
        INCOMPATIBLE if violations else UNDERDETERMINED if underdetermined else COMPATIBLE
    )
    return AssignmentNormCompatibilityResult(
        classification,
        tuple(sorted(violations)),
        tuple(sorted(underdetermined)),
    )


def _probe_shape_valid(probe: Any) -> bool:
    return bool(
        isinstance(probe, dict)
        and set(probe) == PROBE_FIELDS
        and all(nonempty(probe.get(field)) for field in PROBE_FIELDS - {
            "claims", "question_ids", "source_statement_ids",
            "stored_violation_statement_ids", "stored_underdetermined_axes",
        })
        and isinstance(probe.get("claims"), dict)
        and isinstance(probe.get("question_ids"), list)
        and isinstance(probe.get("source_statement_ids"), list)
        and isinstance(probe.get("stored_violation_statement_ids"), list)
        and isinstance(probe.get("stored_underdetermined_axes"), list)
    )


def validate_assignment_norm_compatibility_probe(probe: Any) -> ValidationResult:
    errors: list[str] = []
    if _contains_named(probe, FORBIDDEN_FIELDS):
        errors.append(ASSIGNMENT_NORM_FORBIDDEN_OUTCOME)
    if not _probe_shape_valid(probe):
        errors.append(ASSIGNMENT_NORM_FIXTURE_INVALID)
        return result(errors)
    resolution = str(probe.get("resolution_id"))
    blocker = SURVIVOR_BLOCKERS.get(resolution)
    if blocker is None or probe.get("blocker_id") != blocker or tuple(
        probe.get("question_ids") or ()
    ) != BLOCKER_QUESTIONS.get(blocker):
        errors.append(ASSIGNMENT_NORM_RESOLUTION_INVALID)
    expected_claims = SURVIVOR_CLAIMS.get(resolution)
    if (
        probe.get("claims") != expected_claims
        or tuple(probe.get("source_statement_ids") or ()) != _source_ids_for_claims(expected_claims or {})
        or probe.get("evidence_mode") != ANALYTIC
    ):
        errors.append(ASSIGNMENT_NORM_CLAIM_INVALID)
    derived = derive_assignment_norm_compatibility(probe)
    if (
        probe.get("stored_classification") != derived.classification
        or tuple(probe.get("stored_violation_statement_ids") or ()) != derived.violation_statement_ids
        or tuple(probe.get("stored_underdetermined_axes") or ()) != derived.underdetermined_axes
    ):
        errors.append(ASSIGNMENT_NORM_RESULT_MISMATCH)
    return result(errors)


def validate_assignment_norm_compatibility_fixture(fixture: Any) -> ValidationResult:
    if not isinstance(fixture, dict) or fixture.get("concept") != "AssignmentNormCompatibilityProbe":
        return result((ASSIGNMENT_NORM_FIXTURE_INVALID,))
    return validate_assignment_norm_compatibility_probe(fixture.get("probe"))


def _frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    loaded = yaml.safe_load(text[4:end])
    return loaded if isinstance(loaded, dict) else {}


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


def _live_sources_valid(repo_root: Path) -> bool:
    for statement in NORMATIVE_STATEMENTS.values():
        try:
            text = (repo_root / statement["path"]).read_text(encoding="utf-8")
        except OSError:
            return False
        metadata = _frontmatter(text)
        section = _section(text, statement["section"])
        if (
            metadata.get("Status") != statement["status"]
            or metadata.get("Status") not in CURRENT_DOCUMENT_STATUSES
            or section is None
            or section.count(statement["quote"]) != 1
        ):
            return False
    return True


def _source_sweep_hits(repo_root: Path) -> list[dict[str, str]] | None:
    hits: list[dict[str, str]] = []
    paths = sorted(repo_root.glob("docs/[0-9][0-9][0-9]-*/README.md"))
    if len(paths) != 25:
        return None
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            return None
        status = _frontmatter(text).get("Status")
        if status not in SWEEP_DOCUMENT_STATUSES:
            return None
        section = "frontmatter"
        for raw_line in text.splitlines():
            if raw_line.startswith("## "):
                section = raw_line[3:]
                continue
            quote = raw_line.strip()
            if not quote:
                continue
            folded = quote.casefold()
            for axis, term_groups in SWEEP_VOCABULARY.items():
                if any(all(term.casefold() in folded for term in group) for group in term_groups):
                    hits.append(
                        {
                            "axis": axis,
                            "path": str(path.relative_to(repo_root)),
                            "status": str(status),
                            "section": section,
                            "quote": quote,
                        }
                    )
    return hits


def _source_sweep_payload_valid(payload: Any, repo_root: Path) -> bool:
    if not isinstance(payload, dict) or set(payload) != {
        "document_scope", "claim_boundary", "vocabulary", "hits",
        "known_out_of_vocabulary",
    }:
        return False
    vocabulary = {
        axis: [list(group) for group in groups]
        for axis, groups in SWEEP_VOCABULARY.items()
    }
    if payload.get("document_scope") != {
        "primary_glob": "docs/[0-9][0-9][0-9]-*/README.md",
        "statuses": list(SWEEP_DOCUMENT_STATUSES),
        "document_count": 25,
        "subject_inventory_and_source_eligibility_are_separate": True,
    } or payload.get("claim_boundary") != {
        "proof_scope": "declared-vocabulary-hit-completeness-only",
        "vocabulary_origin": "derived-from-preidentified-statements-not-from-the-axes-themselves",
        "semantic_axis_completeness_claimed": False,
        "out_of_vocabulary_axis_statements_can_exist": True,
    } or payload.get("vocabulary") != vocabulary:
        return False
    rows = payload.get("hits")
    if not isinstance(rows, list):
        return False
    digest = hashlib.sha256(
        yaml.safe_dump(payload, sort_keys=True, allow_unicode=True).encode("utf-8")
    ).hexdigest()
    if digest != SOURCE_SWEEP_SHA256:
        return False
    row_keys = {
        "axis", "path", "status", "section", "quote", "disposition",
        "statement_ids", "reason", "evidence_mode",
    }
    for row in rows:
        if (
            not isinstance(row, dict)
            or set(row) != row_keys
            or row.get("disposition") not in {
                "classification-source", "considered-no-exclusion",
            }
            or row.get("evidence_mode") != ANALYTIC
            or not isinstance(row.get("statement_ids"), list)
            or not nonempty(row.get("reason"))
        ):
            return False
        try:
            text = (repo_root / row["path"]).read_text(encoding="utf-8")
        except OSError:
            return False
        section = _section(text, row["section"])
        if (
            _frontmatter(text).get("Status") != row["status"]
            or section is None
            or section.count(row["quote"]) != 1
        ):
            return False
        matching_sources = sorted(
            statement_id
            for statement_id, statement in NORMATIVE_STATEMENTS.items()
            if statement["path"] == row["path"]
            and statement["status"] == row["status"]
            and statement["axis"] == row["axis"]
            and statement["quote"] in row["quote"]
        )
        if row["statement_ids"] != matching_sources or (
            row["disposition"] == "classification-source"
        ) != bool(matching_sources):
            return False
    out_of_vocabulary = payload.get("known_out_of_vocabulary")
    if not isinstance(out_of_vocabulary, list) or len(out_of_vocabulary) != 3:
        return False
    out_keys = {
        "axes", "path", "status", "section", "quote", "disposition", "reason",
        "evidence_mode",
    }
    observed_identity = {
        (row["path"], row["section"], row["quote"])
        for row in rows
    }
    for row in out_of_vocabulary:
        if (
            not isinstance(row, dict)
            or set(row) != out_keys
            or not isinstance(row.get("axes"), list)
            or not row["axes"]
            or any(axis not in SWEEP_VOCABULARY for axis in row["axes"])
            or row.get("status") not in SWEEP_DOCUMENT_STATUSES
            or row.get("disposition") != "known-out-of-vocabulary-deferral"
            or row.get("evidence_mode") != ANALYTIC
            or not nonempty(row.get("reason"))
            or (row["path"], row["section"], row["quote"]) in observed_identity
        ):
            return False
        try:
            text = (repo_root / row["path"]).read_text(encoding="utf-8")
        except OSError:
            return False
        section = _section(text, row["section"])
        if (
            _frontmatter(text).get("Status") != row["status"]
            or section is None
            or section.count(row["quote"]) != 1
        ):
            return False
    observed = _source_sweep_hits(repo_root)
    if observed is None:
        return False
    projected = [
        {key: row.get(key) for key in ("axis", "path", "status", "section", "quote")}
        for row in rows if isinstance(row, dict)
    ]
    if len(projected) != len(rows) or projected != observed:
        return False
    return len({tuple(item.values()) for item in projected}) == len(projected)


def _expected_results() -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for resolution, claims in SURVIVOR_CLAIMS.items():
        blocker = SURVIVOR_BLOCKERS[resolution]
        probe = {"claims": claims}
        derived = derive_assignment_norm_compatibility(probe)
        results.append(
            {
                "blocker_id": blocker,
                "question_ids": list(BLOCKER_QUESTIONS[blocker]),
                "resolution_id": resolution,
                "claims": claims,
                "source_statement_ids": list(_source_ids_for_claims(claims)),
                "classification": derived.classification,
                "violation_statement_ids": list(derived.violation_statement_ids),
                "underdetermined_axes": list(derived.underdetermined_axes),
                "evidence_mode": ANALYTIC,
            }
        )
    return results


def validate_assignment_norm_compatibility(
    repo_root: Path,
) -> AssignmentNormCompatibilityMapResult:
    errors: list[str] = []
    try:
        payload = yaml.safe_load((repo_root / MAP_PATH).read_text(encoding="utf-8"))
        pressure = yaml.safe_load((repo_root / PRESSURE_MAP_PATH).read_text(encoding="utf-8"))
        surface = yaml.safe_load((repo_root / SURFACE_PATH).read_text(encoding="utf-8"))
        gate = yaml.safe_load((repo_root / GATE_PATH).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return _map_result((ASSIGNMENT_NORM_MAP_INVALID,))

    expected_keys = {
        "schema_version", "rule_owner", "baseline", "gate_first", "criterion",
        "source_policy", "normative_sources", "source_sweep", "survivor_results",
        "blocker_disposition", "promotion_gate_guard", "forbidden_outcomes",
    }
    source_rows = [
        {"statement_id": statement_id, **statement}
        for statement_id, statement in NORMATIVE_STATEMENTS.items()
    ]
    canonical_axis_policies = {
        "resource_cardinality": {
            "kind": "allow-only",
            "values": ("one",),
            "statement_ids": (
                "ASSIGNMENT_EXACT_ONE_RESOURCE_OPERATION",
                "ASSIGNMENT_OWNS_IDENTITY_INTERVAL_LIFECYCLE",
            ),
        },
        "automatic_component_inheritance": {
            "kind": "forbid",
            "values": ("true",),
            "statement_ids": ("COMPONENT_ASSIGNMENT_NON_INHERITANCE",),
        },
        "post_establishment_change_model": {
            "kind": "underdetermined",
            "values": (),
            "statement_ids": (
                "ASSIGNMENT_AMENDMENT_MODEL_OPEN",
                "ASSIGNMENT_CHANGE_REQUIRES_SEPARATE_OWNER",
            ),
        },
        "retroactivity_policy": {
            "kind": "allow-only",
            "values": ("prospective-only",),
            "statement_ids": ("ASSIGNMENT_PROSPECTIVE_EFFECTIVITY_BOUNDARY",),
        },
        "interval_cardinality": {
            "kind": "underdetermined",
            "values": (),
            "statement_ids": ("CONSUMER_INTERVAL_CARDINALITY_NOT_DEFINED",),
        },
        "part_scope_representation": {
            "kind": "underdetermined",
            "values": (),
            "statement_ids": ("COMPOSITION_REPRESENTATION_DEFERRED",),
        },
    }
    if (
        not isinstance(payload, dict)
        or set(payload) != expected_keys
        or payload.get("schema_version") != 1
        or payload.get("rule_owner") != "AD-045"
        or payload.get("baseline") != BASELINE
        or payload.get("gate_first") != EXPECTED_GATE_FIRST
        or payload.get("criterion") != EXPECTED_CRITERION
        or payload.get("source_policy") != {
            "current_document_statuses": ["Draft", "Accepted", "Canonical"],
            "subject_inventory_and_source_eligibility_are_separate": True,
            "historical_snapshots_and_baseline_objects_are_sources": False,
            "classification_evidence_mode": "analytic",
            "reason": "natural-language-compatibility-cannot-be-derived-by-the-reference-checker",
        }
        or payload.get("normative_sources") != source_rows
        or payload.get("forbidden_outcomes") != sorted(FORBIDDEN_OUTCOMES)
        or AXIS_POLICIES != canonical_axis_policies
        or (COMPATIBLE, INCOMPATIBLE, UNDERDETERMINED, ANALYTIC)
        != ("compatible", "incompatible", "underdetermined", "analytic")
    ):
        errors.append(ASSIGNMENT_NORM_MAP_INVALID)

    if not _live_sources_valid(repo_root):
        errors.append(ASSIGNMENT_NORM_SOURCE_DRIFT)
    if not _source_sweep_payload_valid(
        payload.get("source_sweep") if isinstance(payload, dict) else None,
        repo_root,
    ):
        errors.append(ASSIGNMENT_NORM_SOURCE_DRIFT)

    pressure_survivors = {
        item.get("resolution_id")
        for item in pressure.get("resolution_inventory", [])
        if item.get("need_adequacy_effect") == "current-three-bindings-adequate"
    } if isinstance(pressure, dict) else set()
    live_blockers = {
        item.get("blocker_id"): tuple(item.get("question_ids") or ())
        for item in surface.get("blockers", [])
        if item.get("disposition") == "blocks-whole-document-freeze"
    } if isinstance(surface, dict) else {}
    if pressure_survivors != set(SURVIVOR_CLAIMS) or live_blockers != BLOCKER_QUESTIONS:
        errors.append(ASSIGNMENT_NORM_SURVIVOR_DRIFT)

    try:
        expected_results = _expected_results()
    except (KeyError, TypeError, ValueError):
        expected_results = []
        errors.append(ASSIGNMENT_NORM_PROBE_DRIFT)
    if (
        payload.get("survivor_results") != expected_results
        or payload.get("blocker_disposition") != {
            "excluded_resolution_ids": [],
            "unique_compatible_resolution_by_blocker": False,
            "questions_and_blockers_unchanged": True,
        }
        or {item["classification"] for item in expected_results}
        != {COMPATIBLE, UNDERDETERMINED}
        or [
            item["resolution_id"] for item in expected_results
            if item["classification"] == COMPATIBLE
        ] != ["WHOLE_RESOURCE_ONLY"]
    ):
        errors.append(ASSIGNMENT_NORM_PROBE_DRIFT)

    fixture_pairs: set[tuple[str, str]] = set()
    try:
        for fpath in sorted((repo_root / FIXTURE_ROOT).glob("*.yaml")):
            fixture = yaml.safe_load(fpath.read_text(encoding="utf-8"))
            validation = validate_assignment_norm_compatibility_fixture(fixture)
            if not validation.valid:
                errors.append(ASSIGNMENT_NORM_PROBE_DRIFT)
            probe = fixture.get("probe") if isinstance(fixture, dict) else {}
            fixture_pairs.add((probe.get("blocker_id"), probe.get("resolution_id")))
    except (OSError, yaml.YAMLError):
        errors.append(ASSIGNMENT_NORM_PROBE_DRIFT)
    if fixture_pairs != {
        (SURVIVOR_BLOCKERS[resolution], resolution) for resolution in SURVIVOR_CLAIMS
    }:
        errors.append(ASSIGNMENT_NORM_PROBE_DRIFT)

    guard = payload.get("promotion_gate_guard") if isinstance(payload, dict) else None
    cycle_protocol = gate.get("cycle_protocol") if isinstance(gate, dict) else None
    if (
        guard != {"schema_version": 5, "completed_cycle_ids": ["EVENT_T6"], "active_cycle_id": None}
        or gate.get("schema_version") != 5
        or not isinstance(cycle_protocol, dict)
        or cycle_protocol.get("active_cycle_id") is not None
    ):
        errors.append(ASSIGNMENT_NORM_GATE_DRIFT)
    return _map_result(errors)
