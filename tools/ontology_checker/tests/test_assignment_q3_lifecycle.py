from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[3]
CHECKER_ROOT = ROOT / "tools/ontology_checker"
sys.path.insert(0, str(CHECKER_ROOT))

from ocp_checker import assignment_norm_compatibility, assignment_q3_lifecycle  # noqa: E402
from ocp_checker import assignment_temporal_scope  # noqa: E402
from ocp_checker.assignment_q3_lifecycle import (  # noqa: E402
    ASSIGNMENT_Q3_HISTORICAL_DRIFT,
    ASSIGNMENT_Q3_PROJECTION_DRIFT,
    ASSIGNMENT_Q3_SUBJECT_DRIFT,
    validate_assignment_q3_lifecycle,
)
from ocp_checker.checker import assignment_effective_at, load_fixture, validate_assignment  # noqa: E402


class AssignmentQ3LifecycleTests(unittest.TestCase):
    map_path = Path("architecture/assignment-retroactivity-q3-resolution.yaml")
    subject_path = Path("docs/005-assignment-concept/README.md")

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "architecture", destination / "architecture")
        shutil.copytree(ROOT / "docs", destination / "docs")
        fixture = assignment_q3_lifecycle.PROBE_FIXTURE
        target = destination / fixture
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / fixture, target)

    def test_repository_assignment_q3_lifecycle_is_valid(self) -> None:
        self.assertTrue(validate_assignment_q3_lifecycle(ROOT).valid)

    def test_gate_first_and_sufficiency_are_narrow_and_explicit(self) -> None:
        payload = self.payload()
        self.assertEqual(
            payload["gate_first"],
            {
                "ocp016_gate": "G4",
                "applies": False,
                "positive_capable": False,
                "activation_created": False,
                "reason": "finalizing-an-existing-negative-effectivity-boundary-creates-no-positive-capable-rule-result-profile-or-activation",
            },
        )
        criterion = payload["sufficiency_criterion"]
        self.assertEqual(criterion["result"], "sufficient-for-q3-effectivity-boundary-only")
        self.assertFalse(criterion["baseline_only_records_are_current_authority"])
        self.assertEqual(payload["decision"]["disposition"], "resolved-negative")
        self.assertTrue(payload["decision"]["q9_unchanged"])

    def test_each_evidence_record_states_what_it_proves_and_does_not_prove(self) -> None:
        evidence = self.payload()["evidence_ledger"]
        self.assertEqual(len(evidence), 6)
        self.assertEqual(
            {item["evidence_id"] for item in evidence},
            {
                "CURRENT_OWNER_EFFECTIVITY_BOUNDARY",
                "EXECUTABLE_PRE_ESTABLISHMENT_CONTROL",
                "AD039_BASELINE_GAP_SEPARATION",
                "AD044_CONSUMER_PRESSURE",
                "AD045_SURVIVING_NORM_CLASSES",
                "ACCEPTED_CONSUMER_TIME_BOUNDARY",
            },
        )
        self.assertEqual({item["evidence_mode"] for item in evidence}, {"analytic", "observed"})
        self.assertTrue(all(item["proves"] and item["does_not_prove"] for item in evidence))
        historical = [item for item in evidence if item["source_class"] == "historical-baseline-evidence"]
        self.assertEqual(len(historical), 3)
        self.assertTrue(all(item.get("baseline") for item in historical))

    def test_reopening_q3_fails_independently(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            path = root / self.subject_path
            text = path.read_text(encoding="utf-8")
            text = text.replace(
                f"~~{assignment_q3_lifecycle.Q3_TOKEN}~~",
                assignment_q3_lifecycle.Q3_TOKEN,
                1,
            )
            path.write_text(text, encoding="utf-8")
            errors = validate_assignment_q3_lifecycle(root).errors
            self.assertIn(ASSIGNMENT_Q3_SUBJECT_DRIFT, errors)

    def test_closing_any_question_other_than_q3_fails_independently(self) -> None:
        for question_id, token in assignment_q3_lifecycle.OTHER_OPEN_QUESTION_TOKENS.items():
            with self.subTest(question_id=question_id), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / self.subject_path
                text = path.read_text(encoding="utf-8")
                self.assertIn(token, text)
                path.write_text(text.replace(token, f"~~{token}~~", 1), encoding="utf-8")
                self.assertIn(
                    ASSIGNMENT_Q3_PROJECTION_DRIFT,
                    validate_assignment_q3_lifecycle(root).errors,
                )

    def test_executable_boundary_and_current_q9_blocker_are_preserved(self) -> None:
        fixture = load_fixture(ROOT / assignment_q3_lifecycle.PROBE_FIXTURE)
        assignment = copy.deepcopy(fixture["entity"])
        assignment["applicability_start"] = "2026-08-02T09:50:00Z"
        self.assertTrue(validate_assignment(assignment).valid)
        self.assertFalse(assignment_effective_at(assignment, "2026-08-02T09:54:00Z"))
        self.assertTrue(assignment_effective_at(assignment, "2026-08-02T09:55:00Z"))
        projection = self.payload()["current_projection"]
        self.assertEqual(projection["temporal_blocker_question_ids"], ["Q9"])
        self.assertEqual(projection["temporal_blocker_disposition"], "blocks-whole-document-freeze")
        self.assertEqual(projection["open_question_count_after"], 8)

    def test_historical_evidence_version_migration_and_rollback_boundaries_hold(self) -> None:
        payload = self.payload()
        transition = payload["subject_transition"]
        self.assertEqual(transition["before"], {"version": "0.2.8", "status": "Draft", "concept_status": "Accepted"})
        self.assertEqual(transition["after"], {"version": "0.3.0", "status": "Draft", "concept_status": "Accepted"})
        self.assertEqual(transition["version_class"], "pre-canonical-content-change")
        self.assertEqual(payload["migration"]["assignment_data"], "none")
        self.assertIn("OCP-005-version-section-8-and-q3-line", payload["migration"]["rollback_unit"])
        for item in payload["protected_historical_artifacts"]:
            resolved = assignment_q3_lifecycle.historical_path(
                ROOT, Path(item["path"]), item["sha256"]
            )
            self.assertEqual(hashlib.sha256((ROOT / resolved).read_bytes()).hexdigest(), item["sha256"])
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            item = payload["protected_historical_artifacts"][0]
            protected = root / assignment_q3_lifecycle.historical_path(root, Path(item["path"]), item["sha256"])
            protected.write_text(protected.read_text(encoding="utf-8") + "\nmutation\n", encoding="utf-8")
            self.assertIn(
                ASSIGNMENT_Q3_HISTORICAL_DRIFT,
                validate_assignment_q3_lifecycle(root).errors,
            )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            map_path = root / self.map_path
            mutated = self.payload(root)
            mutated["superseded_source_quotes"][0]["current_successor_quote"] += " MUTATED"
            map_path.write_text(
                yaml.safe_dump(mutated, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            self.assertFalse(validate_assignment_q3_lifecycle(root).valid)
            self.assertIn(
                assignment_temporal_scope.ASSIGNMENT_TEMPORAL_SCOPE_OWNER_TEXT_DRIFT,
                assignment_temporal_scope.validate_assignment_temporal_scope(root).errors,
            )

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
        original_load = assignment_q3_lifecycle._load
        for value_path in scalar_paths(payload):
            with self.subTest(attribute="map", value_path=value_path):
                mutated = mutate_scalar(payload, value_path)

                def load_with_mutated_map(path: Path):
                    if path == ROOT / self.map_path:
                        return mutated
                    return original_load(path)

                with patch.object(
                    assignment_q3_lifecycle,
                    "_load",
                    side_effect=load_with_mutated_map,
                ):
                    self.assertFalse(validate_assignment_q3_lifecycle(ROOT).valid)

        structures = (
            "OTHER_OPEN_QUESTION_TOKENS",
            "HISTORICALLY_RESOLVED_QUESTION_TOKENS",
            "EXPECTED_HISTORICAL_HASHES",
        )
        for attribute in structures:
            original = getattr(assignment_q3_lifecycle, attribute)
            for key in sorted(original):
                mutated = copy.deepcopy(original)
                del mutated[key]
                with self.subTest(attribute=attribute, removed=key), patch.object(
                    assignment_q3_lifecycle,
                    attribute,
                    mutated,
                ):
                    self.assertFalse(validate_assignment_q3_lifecycle(ROOT).valid)
            for value_path in scalar_paths(original):
                with self.subTest(attribute=attribute, value_path=value_path), patch.object(
                    assignment_q3_lifecycle,
                    attribute,
                    mutate_scalar(original, value_path),
                ):
                    self.assertFalse(validate_assignment_q3_lifecycle(ROOT).valid)

        sets = (
            "EXPECTED_PRESSURE_RESOLUTIONS",
            "EXPECTED_NORM_SURVIVORS",
            "EXPECTED_MAP_KEYS",
            "EXPECTED_FORBIDDEN_OUTCOMES",
            "EXPECTED_SUCCESSION_ROW_KEYS",
            "EXPECTED_SUCCESSION_STATEMENT_IDS",
        )
        for attribute in sets:
            original = getattr(assignment_q3_lifecycle, attribute)
            for value in sorted(original):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    assignment_q3_lifecycle,
                    attribute,
                    original - {value},
                ):
                    self.assertFalse(validate_assignment_q3_lifecycle(ROOT).valid)

        scalar_constants = {
            "BASELINE": "MUTATED-BASELINE",
            "MAP_SHA256": "MUTATED-DIGEST",
            "Q3_TOKEN": "MUTATED-Q3",
            "Q9_TOKEN": "MUTATED-Q9",
            "FINAL_BOUNDARY": "MUTATED-BOUNDARY",
            "NON_IMPLICATION": "MUTATED-NON-IMPLICATION",
        }
        for attribute, mutation in scalar_constants.items():
            with self.subTest(attribute=attribute), patch.object(
                assignment_q3_lifecycle,
                attribute,
                mutation,
            ):
                self.assertFalse(validate_assignment_q3_lifecycle(ROOT).valid)

        path_constants = (
            "MAP_PATH",
            "SUBJECT_PATH",
            "SURFACE_PATH",
            "PRESSURE_PATH",
            "NORM_PATH",
            "GATE_PATH",
            "PROBE_FIXTURE",
        )
        for attribute in path_constants:
            with self.subTest(attribute=attribute), patch.object(
                assignment_q3_lifecycle,
                attribute,
                Path("missing") / getattr(assignment_q3_lifecycle, attribute).name,
            ):
                self.assertFalse(validate_assignment_q3_lifecycle(ROOT).valid)


if __name__ == "__main__":
    unittest.main()
