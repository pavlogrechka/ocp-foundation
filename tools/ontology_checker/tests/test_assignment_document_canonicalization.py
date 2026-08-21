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

from ocp_checker import assignment_document_canonicalization as canonicalization  # noqa: E402
from ocp_checker.assignment_document_canonicalization import (  # noqa: E402
    ASSIGNMENT_CANONICALIZATION_BOUNDARY_DRIFT,
    ASSIGNMENT_CANONICALIZATION_CRITERION_DRIFT,
    ASSIGNMENT_CANONICALIZATION_GATE_DRIFT,
    ASSIGNMENT_CANONICALIZATION_HISTORY_DRIFT,
    ASSIGNMENT_CANONICALIZATION_SUBJECT_DRIFT,
    validate_assignment_document_canonicalization,
)


class AssignmentDocumentCanonicalizationTests(unittest.TestCase):
    map_path = canonicalization.MAP_PATH

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "docs", destination / "docs")
        shutil.copytree(ROOT / "architecture", destination / "architecture")

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")

    def validate_isolated(self, root: Path):
        with patch.object(
            canonicalization, "_machine_results",
            return_value={name: True for name in canonicalization.MACHINE_VALIDATORS},
        ):
            return validate_assignment_document_canonicalization(root)

    def test_repository_transition_is_valid_and_every_criterion_is_separate(self) -> None:
        result = validate_assignment_document_canonicalization(ROOT)
        self.assertTrue(result.valid, result.errors)
        rows = self.payload()["criteria"]
        self.assertEqual(tuple(row["criterion_id"] for row in rows), canonicalization.CRITERION_IDS)
        self.assertTrue(all(row["basis"] and row["evidence_mode"] for row in rows))

    def test_document_step_is_completed_while_concept_step_and_concept_status_remain_pending(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            gate = yaml.safe_load((root / canonicalization.GATE_PATH).read_text())
            gate["cycles"][1]["steps"]["CONCEPT_CANONICALIZATION"] = "completed"
            self.write_yaml(root, canonicalization.GATE_PATH, gate)
            self.assertIn(ASSIGNMENT_CANONICALIZATION_GATE_DRIFT, self.validate_isolated(root).errors)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            subject = root / canonicalization.SUBJECT_PATH
            subject.write_text(subject.read_text().replace("Concept-Status: Accepted", "Concept-Status: Canonical", 1))
            self.assertIn(ASSIGNMENT_CANONICALIZATION_SUBJECT_DRIFT, self.validate_isolated(root).errors)

    def test_atomicity_fails_in_both_partial_rollback_directions(self) -> None:
        cases = ("subject-only", "gate-only")
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                if case == "subject-only":
                    subject = root / canonicalization.SUBJECT_PATH
                    text = subject.read_text().replace("Version: 1.0.0", "Version: 0.4.0", 1).replace("Status: Canonical", "Status: Accepted", 1)
                    subject.write_text(text)
                    expected = ASSIGNMENT_CANONICALIZATION_SUBJECT_DRIFT
                else:
                    gate = yaml.safe_load((root / canonicalization.GATE_PATH).read_text())
                    gate["cycles"][1]["steps"]["DOCUMENT_PROMOTION"] = "pending"
                    gate["cycles"][1]["evidence"].pop("DOCUMENT_PROMOTION")
                    self.write_yaml(root, canonicalization.GATE_PATH, gate)
                    expected = ASSIGNMENT_CANONICALIZATION_GATE_DRIFT
                self.assertIn(expected, self.validate_isolated(root).errors)

    def test_open_questions_and_unmet_need_remain_live(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            subject = root / canonicalization.SUBJECT_PATH
            subject.write_text(subject.read_text().replace("2. Яка amendment model", "2. ~~Яка amendment model", 1))
            self.assertIn(ASSIGNMENT_CANONICALIZATION_BOUNDARY_DRIFT, self.validate_isolated(root).errors)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            need = yaml.safe_load((root / canonicalization.NEED_PATH).read_text())
            need["current_result"]["unmet_positive_needs"] = []
            self.write_yaml(root, canonicalization.NEED_PATH, need)
            self.assertIn(ASSIGNMENT_CANONICALIZATION_BOUNDARY_DRIFT, self.validate_isolated(root).errors)

    def test_every_historical_predecessor_is_byte_exact_and_individually_live(self) -> None:
        for row in self.payload()["historical_evidence_successions"]:
            with self.subTest(original=row["original_path"]):
                baseline = canonicalization._baseline_blob(ROOT, row["original_path"])
                self.assertIsNotNone(baseline)
                raw = (ROOT / row["preserved_path"]).read_bytes()
                self.assertEqual(raw, baseline[1])
                self.assertEqual(hashlib.sha256(raw).hexdigest(), row["sha256"])
                with tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    path = root / row["preserved_path"]
                    path.write_bytes(path.read_bytes() + b"\nmutation")
                    self.assertIn(ASSIGNMENT_CANONICALIZATION_HISTORY_DRIFT, self.validate_isolated(root).errors)

    def test_baseline_anchors_are_full_chain(self) -> None:
        payload = self.payload()
        tree = subprocess.check_output(["git", "ls-tree", "-r", payload["baseline"]], cwd=ROOT, text=True).splitlines()
        reverse: dict[str, list[str]] = {}
        for line in tree:
            metadata, path = line.split("\t", 1)
            reverse.setdefault(metadata.split()[2], []).append(path)
        for row in payload["baseline_evidence_objects"]:
            with self.subTest(path=row["path"]):
                self.assertIn(row["path"], reverse.get(row["blob"], []))
                raw = subprocess.check_output(["git", "cat-file", "blob", row["blob"]], cwd=ROOT)
                self.assertEqual(hashlib.sha256(raw).hexdigest(), row["sha256"])
                self.assertTrue(all(token in raw.decode("utf-8") for token in row["state_tokens"]))

    def test_each_machine_check_and_non_implication_is_individually_live(self) -> None:
        for name, valid in canonicalization._machine_results(ROOT).items():
            with self.subTest(validator=name):
                self.assertTrue(valid)
        for value in canonicalization.NON_IMPLICATIONS:
            changed = self.payload()
            changed["non_implications"].remove(value)
            digest = hashlib.sha256(yaml.safe_dump(changed, sort_keys=True, allow_unicode=True).encode()).hexdigest()
            original_load = canonicalization._load

            def changed_load(path: Path):
                return changed if path == ROOT / self.map_path else original_load(path)

            with self.subTest(non_implication=value), patch.object(canonicalization, "_load", side_effect=changed_load), patch.object(canonicalization, "MAP_SHA256", digest):
                self.assertIn(ASSIGNMENT_CANONICALIZATION_BOUNDARY_DRIFT, validate_assignment_document_canonicalization(ROOT).errors)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        def scalar_paths(value, prefix=()):
            if isinstance(value, dict):
                for key, child in value.items():
                    yield from scalar_paths(child, prefix + (key,))
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    yield from scalar_paths(child, prefix + (index,))
            else:
                yield prefix

        def mutate(value, value_path):
            if not value_path:
                if isinstance(value, bool):
                    return not value
                if isinstance(value, int):
                    return value + 1
                if value is None:
                    return "MUTATED-null"
                return f"MUTATED-{value}"
            rebuilt = copy.deepcopy(value)
            part = value_path[0]
            rebuilt[part] = mutate(value[part], value_path[1:])
            return rebuilt

        payload = self.payload()
        original_load = canonicalization._load
        for value_path in scalar_paths(payload):
            changed = mutate(payload, value_path)

            def changed_load(path: Path):
                return changed if path == ROOT / self.map_path else original_load(path)

            with self.subTest(value_path=value_path), patch.object(canonicalization, "_load", side_effect=changed_load):
                self.assertFalse(validate_assignment_document_canonicalization(ROOT).valid)


if __name__ == "__main__":
    unittest.main()
