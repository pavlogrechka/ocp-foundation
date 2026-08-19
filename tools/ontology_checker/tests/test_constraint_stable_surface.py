from __future__ import annotations

import copy
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import constraint_stable_surface  # noqa: E402
from ocp_checker.constraint_stable_surface import (  # noqa: E402
    CONSTRAINT_STABLE_SURFACE_CLASSIFICATION_DRIFT,
    CONSTRAINT_STABLE_SURFACE_CLOSURE_DRIFT,
    CONSTRAINT_STABLE_SURFACE_EVIDENCE_DRIFT,
    CONSTRAINT_STABLE_SURFACE_GATE_DRIFT,
    CONSTRAINT_STABLE_SURFACE_QUESTION_DRIFT,
    CONSTRAINT_STABLE_SURFACE_SUBJECT_DRIFT,
    validate_constraint_stable_surface,
)


class ConstraintStableSurfaceTests(unittest.TestCase):
    map_path = Path("architecture/constraint-stable-surface.yaml")
    copied_paths = (
        map_path,
        Path("architecture/foundation-promotion-gate.yaml"),
        Path("architecture/discovery/AD-025-quantitative-constraint-input.md"),
        Path("architecture/discovery/AD-026-reservation-allocation-boundary.md"),
        Path("architecture/discovery/AD-027-constraint-interaction-boundaries.md"),
        Path("docs/006-constraint-concept/README.md"),
        Path("tools/ontology_checker/ocp_checker/checker.py"),
    )

    def copy_inputs(self, destination: Path) -> None:
        for relative in self.copied_paths:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def write_payload(self, root: Path, payload: dict) -> None:
        (root / self.map_path).write_text(
            yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8"
        )

    def test_repository_constraint_stable_surface_is_valid(self) -> None:
        self.assertTrue(validate_constraint_stable_surface(ROOT).valid)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        set_names = (
            "MAP_KEYS", "QUESTION_IDS", "OPEN_QUESTION_IDS", "RESOLVED_QUESTION_IDS",
            "QUESTION_CLASSIFICATIONS", "STABLE_SURFACE_IDS", "MOVING_SURFACE_IDS",
            "BLOCKER_IDS", "FORBIDDEN_OUTCOMES",
        )
        for name in set_names:
            values = getattr(constraint_stable_surface, name)
            for value in sorted(values):
                with self.subTest(attribute=name, value=value), patch.object(
                    constraint_stable_surface, name, values - {value}
                ):
                    self.assertFalse(validate_constraint_stable_surface(ROOT).valid)

        dictionary_names = (
            "EXPECTED_GATE_FIRST", "EXPECTED_SUBJECT", "EXPECTED_CRITERION",
            "EXPECTED_QUESTIONS", "EXPECTED_STABLE_EVIDENCE", "EXPECTED_MOVING",
            "EXPECTED_BLOCKERS", "EXPECTED_CLOSURES", "EXPECTED_BASELINE_OBJECTS",
        )
        for name in dictionary_names:
            values = getattr(constraint_stable_surface, name)
            for key in sorted(values):
                mutated = copy.deepcopy(values)
                del mutated[key]
                with self.subTest(attribute=name, removed=key), patch.object(
                    constraint_stable_surface, name, mutated
                ):
                    self.assertFalse(validate_constraint_stable_surface(ROOT).valid)

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
                if not value_path:
                    return "MUTATED-DEFENSIVE-VALUE"
                part = value_path[0]
                child = mutate_scalar(value[part], value_path[1:])
                if isinstance(value, tuple):
                    rebuilt = list(value)
                    rebuilt[part] = child
                    return tuple(rebuilt)
                if isinstance(value, list):
                    rebuilt = list(value)
                    rebuilt[part] = child
                    return rebuilt
                rebuilt = copy.deepcopy(value)
                rebuilt[part] = child
                return rebuilt

            for value_path in scalar_paths(values):
                mutated = mutate_scalar(values, value_path)
                with self.subTest(attribute=name, value_path=value_path), patch.object(
                    constraint_stable_surface, name, mutated
                ):
                    self.assertFalse(validate_constraint_stable_surface(ROOT).valid)

    def test_open_question_inventory_cannot_diverge_from_document_body(self) -> None:
        for question_id in sorted(constraint_stable_surface.QUESTION_IDS):
            with self.subTest(question=question_id), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / "docs/006-constraint-concept/README.md"
                text = path.read_text(encoding="utf-8")
                token = constraint_stable_surface.EXPECTED_QUESTIONS[question_id]["evidence_token"]
                path.write_text(text.replace(token, "MUTATED-QUESTION", 1), encoding="utf-8")
                self.assertIn(
                    CONSTRAINT_STABLE_SURFACE_QUESTION_DRIFT,
                    validate_constraint_stable_surface(root).errors,
                )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            path = root / "docs/006-constraint-concept/README.md"
            text = path.read_text(encoding="utf-8")
            marker = "## 23. Deferred Decisions"
            path.write_text(text.replace(marker, "13. Нова незареєстрована межа?\n\n" + marker, 1), encoding="utf-8")
            self.assertIn(
                CONSTRAINT_STABLE_SURFACE_QUESTION_DRIFT,
                validate_constraint_stable_surface(root).errors,
            )

    def test_classification_cannot_change_without_basis_change(self) -> None:
        alternatives = {
            "blocks-whole-document-freeze": "local-after-bounded-freeze",
            "local-after-bounded-freeze": "outside-bounded-surface",
            "outside-bounded-surface": "blocks-whole-document-freeze",
            "outside-open-set": "local-after-bounded-freeze",
        }
        for question_id in sorted(constraint_stable_surface.QUESTION_IDS):
            with self.subTest(question=question_id), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload(root)
                question = next(item for item in payload["question_inventory"] if item["question_id"] == question_id)
                question["classification"] = alternatives[question["classification"]]
                self.write_payload(root, payload)
                self.assertIn(
                    CONSTRAINT_STABLE_SURFACE_CLASSIFICATION_DRIFT,
                    validate_constraint_stable_surface(root).errors,
                )

    def test_each_classification_basis_and_stable_surface_token_is_live(self) -> None:
        payload = self.payload()
        evidence_groups = []
        for question in payload["question_inventory"]:
            evidence_groups.extend(question.get("basis", []))
        for surface in payload["stable_candidates"]:
            evidence_groups.extend(surface["evidence"])
        for evidence in evidence_groups:
            for token in evidence["tokens"]:
                with self.subTest(path=evidence["path"], token=token), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    path = root / evidence["path"]
                    text = path.read_text(encoding="utf-8")
                    path.write_text(text.replace(token, "MUTATED-EVIDENCE", 1), encoding="utf-8")
                    self.assertIn(
                        CONSTRAINT_STABLE_SURFACE_EVIDENCE_DRIFT,
                        validate_constraint_stable_surface(root).errors,
                    )

    def test_each_resolved_question_is_bound_to_its_closure_act(self) -> None:
        payload = self.payload()
        for act_id, closure in payload["historical_closure_evidence"].items():
            for token in closure["tokens"]:
                with self.subTest(act=act_id, token=token), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    path = root / closure["path"]
                    text = path.read_text(encoding="utf-8")
                    path.write_text(text.replace(token, "MUTATED-CLOSURE"), encoding="utf-8")
                    self.assertIn(
                        CONSTRAINT_STABLE_SURFACE_CLOSURE_DRIFT,
                        validate_constraint_stable_surface(root).errors,
                    )

    def test_subject_and_promotion_gate_are_guarded_without_lifecycle_authority(self) -> None:
        subject_mutations = (
            ("Version: 0.3.2", "Version: 0.3.3"),
            ("Status: Draft", "Status: Accepted"),
            ("Concept-Status: Accepted", "Concept-Status: Canonical"),
        )
        for old, new in subject_mutations:
            with self.subTest(subject=old), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / "docs/006-constraint-concept/README.md"
                text = path.read_text(encoding="utf-8")
                path.write_text(text.replace(old, new, 1), encoding="utf-8")
                self.assertIn(
                    CONSTRAINT_STABLE_SURFACE_SUBJECT_DRIFT,
                    validate_constraint_stable_surface(root).errors,
                )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            path = root / "architecture/foundation-promotion-gate.yaml"
            payload = yaml.safe_load(path.read_text(encoding="utf-8"))
            payload["cycle_protocol"]["active_cycle_id"] = "CONSTRAINT_T7"
            path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
            self.assertIn(
                CONSTRAINT_STABLE_SURFACE_GATE_DRIFT,
                validate_constraint_stable_surface(root).errors,
            )

    def test_baseline_objects_are_path_and_byte_bound(self) -> None:
        for evidence in self.payload()["baseline_evidence_objects"]:
            with self.subTest(path=evidence["path"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / evidence["path"]
                path.write_bytes(path.read_bytes() + b"\n")
                self.assertIn(
                    CONSTRAINT_STABLE_SURFACE_EVIDENCE_DRIFT,
                    validate_constraint_stable_surface(root).errors,
                )


if __name__ == "__main__":
    unittest.main()
