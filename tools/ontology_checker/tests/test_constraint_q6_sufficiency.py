from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import constraint_q6_sufficiency  # noqa: E402
from ocp_checker.constraint_q6_sufficiency import (  # noqa: E402
    CONSTRAINT_Q6_CRITERION_DRIFT,
    CONSTRAINT_Q6_PROJECTION_DRIFT,
    validate_constraint_q6_sufficiency,
)


class ConstraintQ6SufficiencyTests(unittest.TestCase):
    map_path = Path("architecture/constraint-q6-sufficiency.yaml")

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        paths = set(constraint_q6_sufficiency.DOC_PATHS.values()) | {
            self.map_path,
            constraint_q6_sufficiency.SURFACE_PATH,
            constraint_q6_sufficiency.GATE_PATH,
            constraint_q6_sufficiency.PROBE_FIXTURE,
        }
        for relative in paths:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def write_payload(self, root: Path, payload: dict) -> None:
        (root / self.map_path).write_text(
            yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8"
        )

    def test_repository_constraint_q6_sufficiency_is_valid(self) -> None:
        self.assertTrue(validate_constraint_q6_sufficiency(ROOT).valid)

    def test_gate_first_and_three_answer_forms_are_explicit(self) -> None:
        payload = self.payload()
        self.assertFalse(payload["gate_first"]["evidence_form"]["applies"])
        self.assertEqual(
            {key: value["applies"] for key, value in payload["gate_first"]["hypothetical_answers"].items()},
            {"magnitude-established": True, "magnitude-unnecessary-with-replacement": True, "not-established-until-separate-decision": False},
        )
        self.assertEqual(
            {key: value["supported"] for key, value in payload["answer_disposition"].items()},
            {"magnitude-established": False, "magnitude-unnecessary-with-replacement": False, "not-established-until-separate-decision": False},
        )

    def test_full_structural_neighborhood_and_basis_types_are_derived(self) -> None:
        payload = self.payload()
        self.assertEqual(len(payload["normative_inventory"]), 16)
        self.assertEqual(
            {row["document_id"] for row in payload["normative_inventory"]},
            set(constraint_q6_sufficiency.DOC_PATHS),
        )
        self.assertEqual(
            {row["basis_type"] for row in payload["normative_inventory"]},
            {"direct-normative-statement", "inference-from-silence"},
        )
        self.assertEqual(payload["record_shape_basis"]["basis_type"], "inference-from-list")
        self.assertFalse(payload["record_shape_basis"]["explicitly_exhaustive"])

    def test_executable_probe_is_age_blind_but_exact_binding_control_discriminates(self) -> None:
        self.assertTrue(validate_constraint_q6_sufficiency(ROOT).valid)
        payload = self.payload()["executable_probe"]
        self.assertEqual(
            {row["evaluated_at"]: row["expected_effective_result"] for row in payload["observed_mutations"]},
            {"1900-01-01T00:00:00Z": "satisfied", "2099-01-01T00:00:00Z": "satisfied"},
        )
        self.assertEqual(payload["discriminating_control"]["expected_effective_result"], "indeterminate")

    def test_q6_status_change_without_basis_change_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            payload = self.payload(root)
            payload["decision"]["disposition"] = "closed"
            payload["decision"]["criterion_satisfied"] = True
            self.write_payload(root, payload)
            self.assertIn(CONSTRAINT_Q6_CRITERION_DRIFT, validate_constraint_q6_sufficiency(root).errors)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            surface_path = root / constraint_q6_sufficiency.SURFACE_PATH
            surface = yaml.safe_load(surface_path.read_text(encoding="utf-8"))
            q6 = next(row for row in surface["question_inventory"] if row["question_id"] == "Q6")
            q6["state"] = "resolved"
            surface_path.write_text(yaml.safe_dump(surface, sort_keys=False, allow_unicode=True), encoding="utf-8")
            self.assertIn(CONSTRAINT_Q6_PROJECTION_DRIFT, validate_constraint_q6_sufficiency(root).errors)

    def test_declared_sufficiency_criterion_cannot_diverge_from_applied_criterion(self) -> None:
        attacks = (
            (("sufficiency_criterion", "basis_types", "inference-from-silence"), "may-be-sufficient"),
            (("sufficiency_criterion", "declared_before_application"), False),
            (("sufficiency_criterion", "result"), "sufficient-for-q6-closure"),
        )
        for value_path, replacement in attacks:
            with self.subTest(value_path=value_path), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload(root)
                parent = payload
                for part in value_path[:-1]:
                    parent = parent[part]
                parent[value_path[-1]] = replacement
                self.write_payload(root, payload)
                self.assertIn(CONSTRAINT_Q6_CRITERION_DRIFT, validate_constraint_q6_sufficiency(root).errors)

    def test_baseline_anchors_are_full_chain_and_protected_bytes_are_live(self) -> None:
        payload = self.payload()
        tree = subprocess.check_output(["git", "ls-tree", "-r", payload["baseline"]], cwd=ROOT, text=True).splitlines()
        reverse: dict[str, list[str]] = {}
        for line in tree:
            metadata, path = line.split("\t", 1)
            reverse.setdefault(metadata.split()[2], []).append(path)
        for item in payload["baseline_evidence_objects"]:
            with self.subTest(path=item["path"]):
                self.assertIn(item["path"], reverse.get(item["blob"], []))
                raw = subprocess.check_output(["git", "cat-file", "blob", item["blob"]], cwd=ROOT)
                self.assertEqual(hashlib.sha256(raw).hexdigest(), item["sha256"])
                self.assertTrue(all(token in raw.decode("utf-8") for token in item["state_tokens"]))
        for item in payload["protected_artifacts"]:
            self.assertEqual(hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest(), item["sha256"])

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        def scalar_paths(value, prefix=()):
            if isinstance(value, dict):
                for key, child in value.items():
                    yield from scalar_paths(child, prefix + (key,))
            elif isinstance(value, (list, tuple)):
                for index, child in enumerate(value):
                    yield from scalar_paths(child, prefix + (index,))
            else:
                yield prefix

        def mutate(value, path):
            if not path:
                if isinstance(value, bool):
                    return not value
                if isinstance(value, int):
                    return value + 1
                return f"MUTATED-{value}"
            part = path[0]
            rebuilt = copy.deepcopy(value)
            rebuilt[part] = mutate(value[part], path[1:])
            return rebuilt

        payload = self.payload()
        original_load = constraint_q6_sufficiency._load
        for value_path in scalar_paths(payload):
            changed = mutate(payload, value_path)

            def changed_load(path: Path):
                return changed if path == ROOT / self.map_path else original_load(path)

            with self.subTest(value_path=value_path), patch.object(
                constraint_q6_sufficiency, "_load", side_effect=changed_load
            ):
                self.assertFalse(validate_constraint_q6_sufficiency(ROOT).valid)

        collections = ("DIRECT_DEPENDENCIES", "DIRECT_CONSUMERS", "BASIS_TYPES", "EXPECTED_FORBIDDEN", "EXPECTED_MAP_KEYS")
        for name in collections:
            original = getattr(constraint_q6_sufficiency, name)
            for value in sorted(original):
                with self.subTest(attribute=name, value=value), patch.object(
                    constraint_q6_sufficiency, name, original - {value}
                ):
                    self.assertFalse(validate_constraint_q6_sufficiency(ROOT).valid)
        for name in ("DOC_PATHS",):
            original = getattr(constraint_q6_sufficiency, name)
            for key in sorted(original):
                changed = dict(original)
                del changed[key]
                with self.subTest(attribute=name, key=key), patch.object(constraint_q6_sufficiency, name, changed):
                    self.assertFalse(validate_constraint_q6_sufficiency(ROOT).valid)
        for name, value in {
            "BASELINE": "MUTATED", "SUBJECT_SHA256": "MUTATED", "MAP_SHA256": "MUTATED"
        }.items():
            with self.subTest(attribute=name), patch.object(constraint_q6_sufficiency, name, value):
                self.assertFalse(validate_constraint_q6_sufficiency(ROOT).valid)


if __name__ == "__main__":
    unittest.main()
