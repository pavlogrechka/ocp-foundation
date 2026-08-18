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
CHECKER_ROOT = ROOT / "tools/ontology_checker"
sys.path.insert(0, str(CHECKER_ROOT))

from ocp_checker import assignment_q2_sufficiency  # noqa: E402
from ocp_checker.assignment_q2_sufficiency import (  # noqa: E402
    ASSIGNMENT_Q2_SUFFICIENCY_GATE_DRIFT,
    ASSIGNMENT_Q2_SUFFICIENCY_PROJECTION_DRIFT,
    validate_assignment_q2_sufficiency,
)
from ocp_checker.checker import load_fixture, validate_assignment  # noqa: E402


class AssignmentQ2SufficiencyTests(unittest.TestCase):
    map_path = Path("architecture/assignment-q2-sufficiency.yaml")
    subject_path = Path("docs/005-assignment-concept/README.md")

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "architecture", destination / "architecture")
        shutil.copytree(ROOT / "docs", destination / "docs")
        fixture = assignment_q2_sufficiency.PROBE_FIXTURE
        target = destination / fixture
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / fixture, target)

    def test_repository_assignment_q2_sufficiency_is_valid(self) -> None:
        self.assertTrue(validate_assignment_q2_sufficiency(ROOT).valid)

    def test_gate_criterion_and_three_argument_types_are_separate(self) -> None:
        payload = self.payload()
        self.assertFalse(payload["gate_first"]["evidence_form"]["applies"])
        self.assertTrue(
            payload["gate_first"]["hypothetical_closures"]["SUPERSEDING_ASSIGNMENT_FOR_CHANGE"]["applies"]
        )
        self.assertFalse(
            payload["gate_first"]["hypothetical_closures"]["POST_ESTABLISHMENT_IMMUTABILITY"]["applies"]
        )
        self.assertTrue(payload["sufficiency_criterion"]["declared_before_application"])
        self.assertEqual(payload["sufficiency_criterion"]["result"], "insufficient-for-q2-closure")
        policy = payload["argument_type_policy"]
        self.assertEqual(
            set(policy), {"direct_normative_statement", "enumeration_inference", "silence_inference"}
        )
        self.assertTrue(all(item["current_sufficient_alone"] is False for item in policy.values()))

    def test_calibration_evidence_and_subject_preservation_are_exact(self) -> None:
        payload = self.payload()
        calibration = payload["calibration"]
        self.assertEqual(calibration["owner_selection"]["Q3"], "direct-boundary-present")
        self.assertEqual(calibration["owner_selection"]["Q2"], "traceability-only-model-open")
        self.assertEqual(calibration["owner_selection"]["Q9"], "closed-world-boundary-absent")
        self.assertEqual(len(payload["evidence_ledger"]), 10)
        self.assertEqual(
            {item["evidence_mode"] for item in payload["evidence_ledger"]}, {"analytic", "observed"}
        )
        self.assertTrue(all(item["proves"] and item["does_not_prove"] for item in payload["evidence_ledger"]))
        self.assertEqual(payload["subject_preservation"]["before"], payload["subject_preservation"]["after"])
        self.assertEqual(payload["subject_preservation"]["version_class"], "no-subject-change")
        self.assertEqual(payload["migration"]["assignment_data"], "none")

    def test_executable_role_and_applicability_changes_are_accepted_with_a_rejection_control(self) -> None:
        probe = self.payload()["executable_probe"]
        original = load_fixture(ROOT / assignment_q2_sufficiency.PROBE_FIXTURE)["entity"]
        role_changed = copy.deepcopy(original)
        role_changed["role_specification"]["role_code"] = probe["role_change"]["replacement_value"]
        applicability_changed = copy.deepcopy(original)
        applicability_changed["applicability_end"] = probe["applicability_change"]["replacement_value"]
        invalid = copy.deepcopy(original)
        invalid["role_specification"]["role_code"] = probe["rejection_control"]["replacement_value"]
        self.assertTrue(validate_assignment(original).valid)
        self.assertTrue(validate_assignment(role_changed).valid)
        self.assertTrue(validate_assignment(applicability_changed).valid)
        invalid_result = validate_assignment(invalid)
        self.assertFalse(invalid_result.valid)
        self.assertIn(probe["rejection_control"]["expected_error"], invalid_result.errors)

    def test_q2_and_every_other_open_question_must_remain_open(self) -> None:
        for question_id, token in assignment_q2_sufficiency.OPEN_QUESTION_TOKENS.items():
            with self.subTest(question_id=question_id), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                subject = root / self.subject_path
                text = subject.read_text(encoding="utf-8")
                self.assertIn(token, text)
                subject.write_text(text.replace(token, f"~~{token}~~", 1), encoding="utf-8")
                self.assertIn(
                    ASSIGNMENT_Q2_SUFFICIENCY_PROJECTION_DRIFT,
                    validate_assignment_q2_sufficiency(root).errors,
                )

    def test_blocker_status_readiness_candidates_and_cycle_changes_fail_independently(self) -> None:
        attacks = (
            (assignment_q2_sufficiency.SURFACE_PATH, ("blockers", 0, "question_ids"), []),
            (assignment_q2_sufficiency.SURFACE_PATH, ("subject", "expected_status"), "Accepted"),
            (assignment_q2_sufficiency.SURFACE_PATH, ("subject", "discovery_result"), "ready"),
            (assignment_q2_sufficiency.GATE_PATH, ("candidates", 0, "expected_document_status"), "Accepted"),
            (assignment_q2_sufficiency.GATE_PATH, ("candidates",), []),
            (assignment_q2_sufficiency.GATE_PATH, ("cycle_protocol", "active_cycle_id"), "ASSIGNMENT_T6"),
        )
        for relative, value_path, replacement in attacks:
            with self.subTest(relative=relative, value_path=value_path), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / relative
                data = yaml.safe_load(path.read_text(encoding="utf-8"))
                parent = data
                for part in value_path[:-1]:
                    parent = parent[part]
                parent[value_path[-1]] = replacement
                path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
                expected = (
                    ASSIGNMENT_Q2_SUFFICIENCY_GATE_DRIFT
                    if relative == assignment_q2_sufficiency.GATE_PATH
                    else ASSIGNMENT_Q2_SUFFICIENCY_PROJECTION_DRIFT
                )
                self.assertIn(expected, validate_assignment_q2_sufficiency(root).errors)

    def test_full_chain_anchors_and_protected_bytes_are_live(self) -> None:
        payload = self.payload()
        tree = subprocess.check_output(
            ["git", "ls-tree", "-r", payload["baseline"]], cwd=ROOT, text=True
        ).splitlines()
        by_blob: dict[str, list[str]] = {}
        for line in tree:
            metadata, path = line.split("\t", 1)
            by_blob.setdefault(metadata.split()[2], []).append(path)
        for item in payload["baseline_evidence_objects"]:
            with self.subTest(anchor=item["path"]):
                self.assertIn(item["path"], by_blob.get(item["blob"], []))
                raw = subprocess.check_output(["git", "cat-file", "blob", item["blob"]], cwd=ROOT)
                text = raw.decode("utf-8")
                self.assertTrue(all(token in text for token in item["state_tokens"]))
                self.assertEqual(hashlib.sha256(raw).hexdigest(), item["sha256"])
        for item in payload["protected_artifacts"]:
            self.assertEqual(hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest(), item["sha256"])
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            protected = root / payload["protected_artifacts"][0]["path"]
            protected.write_text(protected.read_text(encoding="utf-8") + "\nmutation\n", encoding="utf-8")
            self.assertFalse(validate_assignment_q2_sufficiency(root).valid)

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

        def mutate_scalar(value, value_path):
            if not value_path:
                if isinstance(value, bool):
                    return not value
                if isinstance(value, int):
                    return value + 1
                if value is None:
                    return "MUTATED"
                return f"MUTATED-{value}"
            part = value_path[0]
            child = mutate_scalar(value[part], value_path[1:])
            if isinstance(value, tuple):
                rebuilt = list(value)
                rebuilt[part] = child
                return tuple(rebuilt)
            mutated = copy.deepcopy(value)
            mutated[part] = child
            return mutated

        payload = self.payload()
        original_load = assignment_q2_sufficiency._load
        for value_path in scalar_paths(payload):
            mutated = mutate_scalar(payload, value_path)

            def load_with_mutated_map(path: Path, mutated=mutated):
                if path == ROOT / self.map_path:
                    return mutated
                return original_load(path)

            with self.subTest(attribute="map", value_path=value_path), patch.object(
                assignment_q2_sufficiency, "_load", side_effect=load_with_mutated_map
            ):
                self.assertFalse(validate_assignment_q2_sufficiency(ROOT).valid)

        for attribute in (
            "OPEN_QUESTION_TOKENS", "RESOLVED_QUESTION_TOKENS", "EXPECTED_Q2_CLASSES",
            "EXPECTED_PROTECTED_HASHES",
        ):
            original = getattr(assignment_q2_sufficiency, attribute)
            for key in sorted(original):
                mutated = copy.deepcopy(original)
                del mutated[key]
                with self.subTest(attribute=attribute, removed=key), patch.object(
                    assignment_q2_sufficiency, attribute, mutated
                ):
                    self.assertFalse(validate_assignment_q2_sufficiency(ROOT).valid)
            for value_path in scalar_paths(original):
                with self.subTest(attribute=attribute, value_path=value_path), patch.object(
                    assignment_q2_sufficiency, attribute, mutate_scalar(original, value_path)
                ):
                    self.assertFalse(validate_assignment_q2_sufficiency(ROOT).valid)

        for attribute in ("EXPECTED_MAP_KEYS", "EXPECTED_FORBIDDEN_OUTCOMES"):
            original = getattr(assignment_q2_sufficiency, attribute)
            for value in sorted(original):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    assignment_q2_sufficiency, attribute, original - {value}
                ):
                    self.assertFalse(validate_assignment_q2_sufficiency(ROOT).valid)

        for attribute, mutation in {
            "BASELINE": "MUTATED-BASELINE", "MAP_SHA256": "MUTATED-DIGEST",
            "SUBJECT_SHA256": "MUTATED-SHA", "Q2_TOKEN": "MUTATED-Q2",
        }.items():
            with self.subTest(attribute=attribute), patch.object(
                assignment_q2_sufficiency, attribute, mutation
            ):
                self.assertFalse(validate_assignment_q2_sufficiency(ROOT).valid)

        for attribute in (
            "MAP_PATH", "SUBJECT_PATH", "SURFACE_PATH", "PRESSURE_PATH", "NORM_PATH",
            "GATE_PATH", "PROBE_FIXTURE",
        ):
            with self.subTest(attribute=attribute), patch.object(
                assignment_q2_sufficiency, attribute,
                Path("missing") / getattr(assignment_q2_sufficiency, attribute).name,
            ):
                self.assertFalse(validate_assignment_q2_sufficiency(ROOT).valid)


if __name__ == "__main__":
    unittest.main()
