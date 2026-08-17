from __future__ import annotations

from pathlib import Path
from unittest.mock import patch
import copy
import shutil
import sys
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import assignment_stable_surface  # noqa: E402
from ocp_checker.assignment_stable_surface import (  # noqa: E402
    ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT,
    ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT,
    ASSIGNMENT_STABLE_SURFACE_EVIDENCE_DRIFT,
    ASSIGNMENT_STABLE_SURFACE_GATE_DRIFT,
    ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT,
    ASSIGNMENT_STABLE_SURFACE_SUBJECT_DRIFT,
    validate_assignment_stable_surface,
)


EXPECTED_CONCEPT_DEPENDENCIES = {"Resource", "Operation"}
EXPECTED_DIRECT_CONSUMERS = {"OCP-006", "OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021", "OCP-023"}
EXPECTED_ACCEPTED_CONSUMERS = {"OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021", "OCP-023"}
EXPECTED_DRAFT_CONSUMERS = {"OCP-006"}
EXPECTED_QUESTION_IDS = {f"Q{number}" for number in range(1, 12)}
EXPECTED_QUESTION_CLASSIFICATIONS = {
    "outside-open-set", "blocks-whole-document-freeze", "local-after-bounded-freeze",
    "outside-bounded-surface",
}
EXPECTED_STABLE_SURFACES = {
    "ASSIGNMENT_IDENTITY_REFERENCE_KERNEL", "TRANSITION_HISTORY_LIFECYCLE_KERNEL",
    "STRUCTURAL_ROLE_PROVENANCE_KERNEL", "NON_INHERITANCE_NON_AUTHORITY_BOUNDARY",
    "SUPERSESSION_IDENTITY_BOUNDARY", "EXECUTABLE_ASSIGNMENT_BOUNDARY",
}
EXPECTED_MOVING_SURFACES = {
    "AMENDMENT_AFTER_ESTABLISHMENT", "TEMPORAL_EFFECTIVITY_EXTENSION", "ROLE_GOVERNANCE",
    "COMPOSITE_RESOURCE_SCOPE", "CONSTRAINT_CONFLICT_HANDOFF", "PROVENANCE_TAXONOMY",
    "REPLACEMENT_POLICY",
}
EXPECTED_BLOCKERS = {
    "AMENDMENT_MODEL_ABSENT", "TEMPORAL_MODEL_UNRESOLVED",
    "PARTIAL_SCOPE_IDENTITY_UNRESOLVED",
}
EXPECTED_FORBIDDEN_OUTCOMES = {
    "ASSIGNMENT_SELECTION", "PROMOTION_CYCLE_START", "OCP005_PROMOTION",
    "ASSIGNMENT_CONCEPT_CANONICALIZATION", "OPEN_QUESTION_CLOSURE", "T7_OPEN",
}


class AssignmentStableSurfaceTests(unittest.TestCase):
    map_path = Path("architecture/assignment-stable-surface.yaml")
    gate_path = Path("architecture/foundation-promotion-gate.yaml")

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "docs", destination / "docs")
        for relative in (
            self.map_path,
            self.gate_path,
            Path("tools/ontology_checker/rules.yaml"),
            Path("tools/ontology_checker/ocp_checker/checker.py"),
        ):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    def test_repository_assignment_stable_surface_is_valid(self) -> None:
        self.assertTrue(validate_assignment_stable_surface(ROOT).valid)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            ("CONCEPT_DEPENDENCY_IDS", EXPECTED_CONCEPT_DEPENDENCIES),
            ("DIRECT_CONSUMER_IDS", EXPECTED_DIRECT_CONSUMERS),
            ("ACCEPTED_CONSUMER_IDS", EXPECTED_ACCEPTED_CONSUMERS),
            ("DRAFT_CONSUMER_IDS", EXPECTED_DRAFT_CONSUMERS),
            ("QUESTION_IDS", EXPECTED_QUESTION_IDS),
            ("QUESTION_CLASSIFICATIONS", EXPECTED_QUESTION_CLASSIFICATIONS),
            ("STABLE_SURFACE_IDS", EXPECTED_STABLE_SURFACES),
            ("MOVING_SURFACE_IDS", EXPECTED_MOVING_SURFACES),
            ("BLOCKER_IDS", EXPECTED_BLOCKERS),
            ("FORBIDDEN_OUTCOMES", EXPECTED_FORBIDDEN_OUTCOMES),
        )
        for attribute, expected_values in categories:
            production_values = getattr(assignment_stable_surface, attribute)
            self.assertEqual(production_values, frozenset(expected_values))
            for value in sorted(expected_values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    assignment_stable_surface, attribute, production_values - {value}
                ):
                    self.assertFalse(validate_assignment_stable_surface(ROOT).valid)

        dictionaries = (
            "EXPECTED_CONCEPT_DEPENDENCIES", "EXPECTED_CONSUMERS", "EXPECTED_QUESTIONS",
            "EXPECTED_EVIDENCE", "EXPECTED_MOVING", "EXPECTED_BLOCKERS",
        )
        for attribute in dictionaries:
            production_values = getattr(assignment_stable_surface, attribute)
            for key in sorted(production_values):
                mutated = dict(production_values)
                del mutated[key]
                with self.subTest(attribute=attribute, value=key), patch.object(
                    assignment_stable_surface, attribute, mutated
                ):
                    self.assertFalse(validate_assignment_stable_surface(ROOT).valid)

            def scalar_paths(value, prefix=()):
                if isinstance(value, dict):
                    for child_key, child_value in value.items():
                        yield from scalar_paths(child_value, prefix + (child_key,))
                elif isinstance(value, (tuple, list)):
                    for index, child_value in enumerate(value):
                        yield from scalar_paths(child_value, prefix + (index,))
                else:
                    yield prefix

            def mutate_scalar(value, value_path):
                replacement = "MUTATED-DEFENSIVE-VALUE"
                if len(value_path) == 1:
                    part = value_path[0]
                    if isinstance(value, tuple):
                        rebuilt = list(value)
                        rebuilt[part] = replacement
                        return tuple(rebuilt)
                    mutated = copy.deepcopy(value)
                    mutated[part] = replacement
                    return mutated
                part = value_path[0]
                child = mutate_scalar(value[part], value_path[1:])
                if isinstance(value, tuple):
                    rebuilt = list(value)
                    rebuilt[part] = child
                    return tuple(rebuilt)
                mutated = copy.deepcopy(value)
                mutated[part] = child
                return mutated

            for value_path in scalar_paths(production_values):
                top_key = value_path[0]
                nested_path = value_path[1:]
                mutated = copy.deepcopy(production_values)
                mutated[top_key] = mutate_scalar(mutated[top_key], nested_path)
                with self.subTest(attribute=attribute, value_path=value_path), patch.object(
                    assignment_stable_surface, attribute, mutated
                ):
                    self.assertFalse(validate_assignment_stable_surface(ROOT).valid)

    def test_subject_and_concept_dependency_state_are_live(self) -> None:
        subject_mutations = (
            ("Version: 0.2.8", "Version: 0.2.9"),
            ("Status: Draft", "Status: Accepted"),
            ("Concept-Status: Accepted", "Concept-Status: Canonical"),
            ("Concept-Depends-On: [Resource, Operation]", "Concept-Depends-On: [Resource]"),
        )
        for old, new in subject_mutations:
            with self.subTest(old=old), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / "docs/005-assignment-concept/README.md"
                path.write_text(path.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8")
                errors = validate_assignment_stable_surface(root).errors
                self.assertTrue(
                    ASSIGNMENT_STABLE_SURFACE_SUBJECT_DRIFT in errors
                    or ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT in errors
                )

        for document_id in ("OCP-003", "OCP-004"):
            with self.subTest(document=document_id), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                entry = next(
                    value for value in self.payload(root)["concept_dependencies"]
                    if value["defining_document"] == document_id
                )
                path = next(
                    value for value in (root / "docs").glob("*/README.md")
                    if f"Document-ID: {document_id}" in value.read_text(encoding="utf-8")
                )
                text = path.read_text(encoding="utf-8")
                path.write_text(text.replace("Concept-Status: Canonical", "Concept-Status: Accepted", 1), encoding="utf-8")
                self.assertIn(
                    ASSIGNMENT_STABLE_SURFACE_DEPENDENCY_DRIFT,
                    validate_assignment_stable_surface(root).errors,
                    entry,
                )

    def test_each_consumer_binding_status_and_consumed_element_is_live(self) -> None:
        for consumer in self.payload()["direct_consumers"]:
            mutations = ["OCP-005", *consumer["consumed_elements"]]
            for token in mutations:
                with self.subTest(consumer=consumer["document_id"], token=token), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    path = root / consumer["primary"]
                    text = path.read_text(encoding="utf-8")
                    path.write_text(text.replace(token, "MUTATED-CONSUMER-TOKEN"), encoding="utf-8")
                    self.assertIn(
                        ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT,
                        validate_assignment_stable_surface(root).errors,
                    )

            with self.subTest(consumer=consumer["document_id"], token="Status"), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / consumer["primary"]
                text = path.read_text(encoding="utf-8")
                old = f"Status: {consumer['expected_status']}"
                path.write_text(text.replace(old, "Status: Canonical", 1), encoding="utf-8")
                self.assertIn(
                    ASSIGNMENT_STABLE_SURFACE_CONSUMER_DRIFT,
                    validate_assignment_stable_surface(root).errors,
                )

    def test_each_question_token_state_and_classification_is_live(self) -> None:
        for question in self.payload()["open_question_inventory"]:
            with self.subTest(question=question["question_id"], mutation="source"), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / "docs/005-assignment-concept/README.md"
                text = path.read_text(encoding="utf-8")
                token = question["evidence_token"]
                path.write_text(text.replace(token, "MUTATED-QUESTION-TOKEN"), encoding="utf-8")
                self.assertIn(
                    ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT,
                    validate_assignment_stable_surface(root).errors,
                )
            with self.subTest(question=question["question_id"], mutation="strikeout"), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / "docs/005-assignment-concept/README.md"
                text = path.read_text(encoding="utf-8")
                line = next(value for value in text.splitlines() if question["evidence_token"] in value)
                if question["state"] == "resolved-historical":
                    replacement = line.replace("~~", "")
                else:
                    replacement = line.replace(
                        question["evidence_token"], f"~~{question['evidence_token']}~~", 1
                    )
                path.write_text(text.replace(line, replacement, 1), encoding="utf-8")
                self.assertIn(
                    ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT,
                    validate_assignment_stable_surface(root).errors,
                )
            for field in ("state", "classification", "surface"):
                with self.subTest(question=question["question_id"], field=field), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    payload = self.payload(root)
                    target = next(item for item in payload["open_question_inventory"] if item["question_id"] == question["question_id"])
                    target[field] = str(target[field]) + "-mutated"
                    self.write_yaml(root, self.map_path, payload)
                    self.assertIn(
                        ASSIGNMENT_STABLE_SURFACE_QUESTION_DRIFT,
                        validate_assignment_stable_surface(root).errors,
                    )

    def test_each_stable_surface_source_token_is_live(self) -> None:
        for surface in self.payload()["stable_candidates"]:
            for evidence in surface["evidence"]:
                for token in evidence["tokens"]:
                    with self.subTest(surface=surface["surface_id"], token=token), tempfile.TemporaryDirectory() as tmp:
                        root = Path(tmp)
                        self.copy_inputs(root)
                        path = root / evidence["path"]
                        text = path.read_text(encoding="utf-8")
                        path.write_text(text.replace(token, "MUTATED-EVIDENCE-TOKEN"), encoding="utf-8")
                        self.assertIn(
                            ASSIGNMENT_STABLE_SURFACE_EVIDENCE_DRIFT,
                            validate_assignment_stable_surface(root).errors,
                        )

    def test_every_baseline_anchor_value_is_individually_live(self) -> None:
        for item_index, item in enumerate(self.payload()["baseline_evidence_objects"]):
            for key in ("path", "blob", "sha256"):
                with self.subTest(item=item_index, key=key), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    payload = self.payload(root)
                    payload["baseline_evidence_objects"][item_index][key] = str(item[key]) + "-mutated"
                    self.write_yaml(root, self.map_path, payload)
                    self.assertIn(
                        ASSIGNMENT_STABLE_SURFACE_EVIDENCE_DRIFT,
                        validate_assignment_stable_surface(root).errors,
                    )

    def test_discovery_neither_starts_nor_rewrites_a_promotion_cycle(self) -> None:
        mutations = ("activate", "remove-event", "downgrade-schema")
        for mutation in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                gate = yaml.safe_load((root / self.gate_path).read_text(encoding="utf-8"))
                if mutation == "activate":
                    gate["cycle_protocol"]["active_cycle_id"] = "ASSIGNMENT_T6"
                elif mutation == "remove-event":
                    gate["cycles"] = []
                else:
                    gate["schema_version"] = 4
                self.write_yaml(root, self.gate_path, gate)
                self.assertIn(
                    ASSIGNMENT_STABLE_SURFACE_GATE_DRIFT,
                    validate_assignment_stable_surface(root).errors,
                )


if __name__ == "__main__":
    unittest.main()
