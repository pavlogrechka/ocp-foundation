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

from ocp_checker import assignment_canonical_readiness as readiness  # noqa: E402
from ocp_checker.assignment_canonical_readiness import (  # noqa: E402
    ASSIGNMENT_CANONICAL_READINESS_CRITERION_DRIFT,
    ASSIGNMENT_CANONICAL_READINESS_NEED_DRIFT,
    ASSIGNMENT_CANONICAL_READINESS_OPEN_QUESTION_DRIFT,
    ASSIGNMENT_CANONICAL_READINESS_SLOT_DRIFT,
    ASSIGNMENT_CANONICAL_READINESS_SUBJECT_DRIFT,
    validate_assignment_canonical_readiness,
)


class AssignmentCanonicalReadinessTests(unittest.TestCase):
    map_path = readiness.MAP_PATH

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        for source in (ROOT / "docs").glob("[0-9][0-9][0-9]-*/README.md"):
            relative = source.relative_to(ROOT)
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        for relative in (self.map_path, readiness.CRITERIA_PATH, readiness.GATE_PATH, readiness.NEED_PATH):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def validate_isolated(self, root: Path):
        with patch.object(readiness, "_machine_results", return_value={name: True for name in readiness.MACHINE_VALIDATORS}), patch.object(readiness, "slot_reuse_probe", return_value=True):
            return validate_assignment_canonical_readiness(root)

    def test_repository_assignment_canonical_readiness_is_valid(self) -> None:
        result = validate_assignment_canonical_readiness(ROOT)
        self.assertTrue(result.valid, result.errors)

    def test_fixed_criteria_are_applied_separately_and_accepted_only_is_not_rechecked(self) -> None:
        payload = self.payload()
        observed = {
            row["criterion_id"]: (row["applicability"], row["result"], row["readiness_effect"])
            for row in payload["criteria_assessment"]
        }
        self.assertEqual(observed, readiness.EXPECTED_ASSESSMENTS)
        self.assertEqual(
            observed["BOARD_ACCEPTS_CURRENT_SEMANTICS"],
            ("Accepted-only-previously-passed", "not-re-evaluated", "excluded-from-Canonical-assessment"),
        )
        criteria = yaml.safe_load((ROOT / readiness.CRITERIA_PATH).read_text(encoding="utf-8"))
        changed = copy.deepcopy(criteria)
        changed["promotion_criteria"] = changed["promotion_criteria"][:-1]
        original_load = readiness._load

        def changed_load(path: Path):
            return changed if path == ROOT / readiness.CRITERIA_PATH else original_load(path)

        with patch.object(readiness, "_load", side_effect=changed_load), patch.object(readiness, "_machine_results", return_value={name: True for name in readiness.MACHINE_VALIDATORS}):
            self.assertIn(ASSIGNMENT_CANONICAL_READINESS_CRITERION_DRIFT, validate_assignment_canonical_readiness(ROOT).errors)

    def test_each_subject_lifecycle_value_and_cycle_state_is_live(self) -> None:
        cases = (
            (readiness.SUBJECT_PATH, "Version: 0.4.0", "Version: 1.0.0", ASSIGNMENT_CANONICAL_READINESS_SUBJECT_DRIFT),
            (readiness.SUBJECT_PATH, "Status: Accepted", "Status: Canonical", ASSIGNMENT_CANONICAL_READINESS_SUBJECT_DRIFT),
            (readiness.SUBJECT_PATH, "Concept-Status: Accepted", "Concept-Status: Canonical", ASSIGNMENT_CANONICAL_READINESS_SUBJECT_DRIFT),
            (readiness.GATE_PATH, "active_cycle_id: null", "active_cycle_id: ASSIGNMENT_T6", ASSIGNMENT_CANONICAL_READINESS_SLOT_DRIFT),
        )
        for relative, old, new, expected in cases:
            with self.subTest(relative=relative, old=old), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / relative
                path.write_text(path.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8")
                self.assertIn(expected, self.validate_isolated(root).errors)

    def test_open_question_and_unmet_need_conclusions_are_observational(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            path = root / readiness.SUBJECT_PATH
            path.write_text(path.read_text(encoding="utf-8").replace("2. Яка amendment model", "2. ~~Яка amendment model", 1), encoding="utf-8")
            self.assertIn(ASSIGNMENT_CANONICAL_READINESS_OPEN_QUESTION_DRIFT, self.validate_isolated(root).errors)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            path = root / readiness.NEED_PATH
            path.write_text(path.read_text(encoding="utf-8").replace("disposition: current-unmet-positive-consumer-need", "disposition: satisfied", 1), encoding="utf-8")
            self.assertIn(ASSIGNMENT_CANONICAL_READINESS_NEED_DRIFT, self.validate_isolated(root).errors)

    def test_every_machine_check_is_current_and_t6_reuse_is_executable(self) -> None:
        self.assertEqual(tuple(readiness._machine_results(ROOT)), readiness.MACHINE_VALIDATORS)
        for name, valid in readiness._machine_results(ROOT).items():
            with self.subTest(validator=name):
                self.assertTrue(valid)
        self.assertTrue(readiness.slot_reuse_probe(ROOT))
        changed = self.payload()
        changed["slot_occupancy"]["conclusion"] = "slot-reuse-forbidden"
        changed_digest = hashlib.sha256(
            yaml.safe_dump(changed, sort_keys=True, allow_unicode=True).encode()
        ).hexdigest()
        original_load = readiness._load

        def changed_load(path: Path):
            return changed if path == ROOT / self.map_path else original_load(path)

        with patch.object(readiness, "_load", side_effect=changed_load), patch.object(
            readiness, "MAP_SHA256", changed_digest
        ):
            self.assertIn(
                ASSIGNMENT_CANONICAL_READINESS_SLOT_DRIFT,
                validate_assignment_canonical_readiness(ROOT).errors,
            )

    def test_baseline_anchors_are_full_chain(self) -> None:
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
        original_load = readiness._load
        for value_path in scalar_paths(payload):
            changed = mutate(payload, value_path)

            def changed_load(path: Path):
                return changed if path == ROOT / self.map_path else original_load(path)

            with self.subTest(value_path=value_path), patch.object(readiness, "_load", side_effect=changed_load):
                self.assertFalse(validate_assignment_canonical_readiness(ROOT).valid)


if __name__ == "__main__":
    unittest.main()
