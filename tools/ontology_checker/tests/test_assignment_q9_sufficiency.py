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

from ocp_checker import assignment_q9_sufficiency  # noqa: E402
from ocp_checker.assignment_q9_sufficiency import (  # noqa: E402
    ASSIGNMENT_Q9_GATE_DRIFT,
    ASSIGNMENT_Q9_PROJECTION_DRIFT,
    validate_assignment_q9_sufficiency,
)
from ocp_checker.checker import assignment_effective_at, load_fixture, validate_assignment  # noqa: E402


class AssignmentQ9SufficiencyTests(unittest.TestCase):
    map_path = Path("architecture/assignment-q9-sufficiency.yaml")
    subject_path = Path("docs/005-assignment-concept/README.md")

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "architecture", destination / "architecture")
        shutil.copytree(ROOT / "docs", destination / "docs")
        fixture = assignment_q9_sufficiency.PROBE_FIXTURE
        target = destination / fixture
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / fixture, target)

    def test_repository_assignment_q9_sufficiency_is_valid(self) -> None:
        self.assertTrue(validate_assignment_q9_sufficiency(ROOT).valid)

    def test_gate_first_criterion_and_q3_comparison_are_explicit(self) -> None:
        payload = self.payload()
        self.assertFalse(payload["gate_first"]["evidence_form"]["applies"])
        self.assertFalse(payload["gate_first"]["evidence_form"]["positive_capable"])
        self.assertTrue(
            payload["gate_first"]["hypothetical_closures"]["single_interval_only"]["applies"]
        )
        self.assertTrue(
            payload["gate_first"]["hypothetical_closures"]["multiple_intervals"]["applies"]
        )
        criterion = payload["sufficiency_criterion"]
        self.assertTrue(criterion["declared_before_application"])
        self.assertFalse(criterion["form_only_basis_is_sufficient"])
        self.assertEqual(criterion["result"], "insufficient-for-q9-closure")
        comparison = criterion["comparison_to_q3"]
        self.assertEqual(comparison["current_owner_normative_boundary"], {"q3": "present", "q9": "absent"})
        self.assertEqual(comparison["survivor_intersection"]["q9"], "two-cardinality-classes-remain")

    def test_every_evidence_row_is_scoped_and_the_subject_has_no_version_transition(self) -> None:
        payload = self.payload()
        evidence = payload["evidence_ledger"]
        self.assertEqual(len(evidence), 7)
        self.assertEqual({item["evidence_mode"] for item in evidence}, {"analytic", "observed"})
        self.assertTrue(all(item["proves"] and item["does_not_prove"] for item in evidence))
        self.assertEqual(payload["decision"]["disposition"], "remains-open-insufficient-evidence")
        self.assertFalse(payload["decision"]["criterion_satisfied"])
        self.assertEqual(payload["subject_preservation"]["before"], payload["subject_preservation"]["after"])
        self.assertEqual(payload["subject_preservation"]["version_class"], "no-subject-change")
        self.assertEqual(payload["migration"]["assignment_data"], "none")

    def test_executable_probe_accepts_extra_intervals_but_rejects_a_real_scalar_violation(self) -> None:
        payload = self.payload()["executable_probe"]
        fixture = load_fixture(ROOT / assignment_q9_sufficiency.PROBE_FIXTURE)
        original = fixture["entity"]
        extension = copy.deepcopy(original)
        extension[payload["subject_field"]] = copy.deepcopy(payload["two_interval_extension"]["value"])
        invalid = copy.deepcopy(original)
        invalid["applicability_end"] = payload["validator_rejection_control"]["applicability_end"]
        self.assertTrue(validate_assignment(original).valid)
        self.assertTrue(validate_assignment(extension).valid)
        self.assertTrue(
            assignment_effective_at(extension, payload["two_interval_extension"]["expected_effective_at"])
        )
        invalid_result = validate_assignment(invalid)
        self.assertFalse(invalid_result.valid)
        self.assertIn(payload["validator_rejection_control"]["expected_error"], invalid_result.errors)

    def test_q9_and_every_other_open_question_must_remain_open(self) -> None:
        for question_id, token in assignment_q9_sufficiency.OPEN_QUESTION_TOKENS.items():
            with self.subTest(question_id=question_id), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                subject = root / self.subject_path
                text = subject.read_text(encoding="utf-8")
                self.assertIn(token, text)
                subject.write_text(text.replace(token, f"~~{token}~~", 1), encoding="utf-8")
                self.assertIn(
                    ASSIGNMENT_Q9_PROJECTION_DRIFT,
                    validate_assignment_q9_sufficiency(root).errors,
                )

    def test_blocker_status_readiness_and_candidate_changes_fail_independently(self) -> None:
        attacks = (
            (assignment_q9_sufficiency.SURFACE_PATH, ("blockers", 1, "question_ids"), []),
            (assignment_q9_sufficiency.SURFACE_PATH, ("subject", "expected_status"), "Accepted"),
            (assignment_q9_sufficiency.SURFACE_PATH, ("subject", "discovery_result"), "ready"),
            (assignment_q9_sufficiency.GATE_PATH, ("candidates", 0, "expected_document_status"), "Accepted"),
            (assignment_q9_sufficiency.GATE_PATH, ("candidates",), []),
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
                errors = validate_assignment_q9_sufficiency(root).errors
                expected = ASSIGNMENT_Q9_GATE_DRIFT if relative == assignment_q9_sufficiency.GATE_PATH else ASSIGNMENT_Q9_PROJECTION_DRIFT
                self.assertIn(expected, errors)

    def test_protected_anchors_are_full_chain_and_byte_live(self) -> None:
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
            resolved = assignment_q9_sufficiency.historical_path(ROOT, Path(item["path"]), item["sha256"])
            path = ROOT / resolved
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), item["sha256"])
            declared = next(
                row for row in payload["evidence_ledger"] if row.get("path") == item["path"]
            ) if any(row.get("path") == item["path"] for row in payload["evidence_ledger"]) else None
            if declared is not None:
                self.assertTrue(declared["proves"])
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            protected = root / payload["protected_artifacts"][0]["path"]
            protected.write_text(protected.read_text(encoding="utf-8") + "\nmutation\n", encoding="utf-8")
            self.assertFalse(validate_assignment_q9_sufficiency(root).valid)

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
        original_load = assignment_q9_sufficiency._load
        for value_path in scalar_paths(payload):
            with self.subTest(attribute="map", value_path=value_path):
                mutated = mutate_scalar(payload, value_path)

                def load_with_mutated_map(path: Path):
                    if path == ROOT / self.map_path:
                        return mutated
                    return original_load(path)

                with patch.object(assignment_q9_sufficiency, "_load", side_effect=load_with_mutated_map):
                    self.assertFalse(validate_assignment_q9_sufficiency(ROOT).valid)

        structures = (
            "OPEN_QUESTION_TOKENS",
            "RESOLVED_QUESTION_TOKENS",
            "EXPECTED_Q9_CLASSES",
            "EXPECTED_PROTECTED_HASHES",
        )
        for attribute in structures:
            original = getattr(assignment_q9_sufficiency, attribute)
            for key in sorted(original):
                mutated = copy.deepcopy(original)
                del mutated[key]
                with self.subTest(attribute=attribute, removed=key), patch.object(
                    assignment_q9_sufficiency, attribute, mutated
                ):
                    self.assertFalse(validate_assignment_q9_sufficiency(ROOT).valid)
            for value_path in scalar_paths(original):
                with self.subTest(attribute=attribute, value_path=value_path), patch.object(
                    assignment_q9_sufficiency,
                    attribute,
                    mutate_scalar(original, value_path),
                ):
                    self.assertFalse(validate_assignment_q9_sufficiency(ROOT).valid)

        for attribute in ("EXPECTED_MAP_KEYS", "EXPECTED_FORBIDDEN_OUTCOMES"):
            original = getattr(assignment_q9_sufficiency, attribute)
            for value in sorted(original):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    assignment_q9_sufficiency, attribute, original - {value}
                ):
                    self.assertFalse(validate_assignment_q9_sufficiency(ROOT).valid)

        scalar_constants = {
            "BASELINE": "MUTATED-BASELINE",
            "MAP_SHA256": "MUTATED-DIGEST",
            "SUBJECT_SHA256": "MUTATED-SHA",
            "Q9_TOKEN": "MUTATED-Q9",
        }
        for attribute, mutation in scalar_constants.items():
            with self.subTest(attribute=attribute), patch.object(
                assignment_q9_sufficiency, attribute, mutation
            ):
                self.assertFalse(validate_assignment_q9_sufficiency(ROOT).valid)

        for attribute in (
            "MAP_PATH",
            "SUBJECT_PATH",
            "SURFACE_PATH",
            "PRESSURE_PATH",
            "NORM_PATH",
            "GATE_PATH",
            "PROBE_FIXTURE",
        ):
            with self.subTest(attribute=attribute), patch.object(
                assignment_q9_sufficiency,
                attribute,
                Path("missing") / getattr(assignment_q9_sufficiency, attribute).name,
            ):
                self.assertFalse(validate_assignment_q9_sufficiency(ROOT).valid)


if __name__ == "__main__":
    unittest.main()
