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

from ocp_checker import assignment_consumer_pressure  # noqa: E402
from ocp_checker.assignment_consumer_pressure import (  # noqa: E402
    ASSIGNMENT_PRESSURE_BLOCKER_DRIFT,
    ASSIGNMENT_PRESSURE_CONSUMER_NEED_DRIFT,
    ASSIGNMENT_PRESSURE_ERROR_CODES,
    ASSIGNMENT_PRESSURE_GATE_DRIFT,
    ASSIGNMENT_PRESSURE_PROBE_DRIFT,
    derive_assignment_consumer_pressure,
    validate_assignment_consumer_pressure,
)
from ocp_checker.checker import load_fixture  # noqa: E402
from ocp_checker import derive_resource_occupancy, validate_reference_fixture  # noqa: E402


class AssignmentConsumerPressureTests(unittest.TestCase):
    baseline = "6099a1ce042624b86fb4289f75d396a53fa9addb"
    map_path = Path("architecture/assignment-consumer-pressure.yaml")
    copied_paths = (
        map_path,
        Path("architecture/assignment-stable-surface.yaml"),
        Path("architecture/consumer-need-discovery.yaml"),
        Path("architecture/foundation-promotion-gate.yaml"),
        Path("tools/ontology_checker/fixtures/assignment_consumer_pressure"),
        Path("tools/ontology_checker/fixtures/resource_occupancy"),
    )
    baseline_anchors = {
        "docs/005-assignment-concept/README.md": (
            "6e6c00e723b15a348e7610d4ca5a1ae23526c52b",
            "a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065",
            ("Version: 0.2.8", "Status: Draft", "Concept-Status: Accepted"),
        ),
        "docs/016-core-boundary/README.md": (
            "94f5d997deea0168a3c553c2ac9f19d2ee03b4fb",
            "78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4",
            ("Version: 1.0.0", "Status: Canonical", "G4"),
        ),
        "docs/023-resource-occupancy/README.md": (
            "a846333fae80aff2b3697e811d2b155c91f04122",
            "5ec9aca56de4524b4ab78a9e98e2cf5d7561d6f13bac8cf7778d66a99f5490d9",
            ("Version: 0.2.0", "Status: Accepted", "assignment_set_complete_for_resource"),
        ),
        "docs/024-completeness-evaluator/README.md": (
            "2713c99ca6653d35fc52435eaeaeb8f9f5174b1d",
            "0c77e0527ec3adf9ed7cf5bbd32e0a63e55a1c3780f007d35a0ef2630cc18753",
            ("Version: 0.1.0", "Status: Draft", "Actual legitimacy cannot be established"),
        ),
        "architecture/assignment-stable-surface.yaml": (
            "eea05626eddfba594508c5e6d4c4d5bd851c0f5a",
            "b887717a064d479830b7aa0f360d2793a3cba4e54d2b1537d19374e553b3b593",
            ("AMENDMENT_MODEL_ABSENT", "TEMPORAL_MODEL_UNRESOLVED", "PARTIAL_SCOPE_IDENTITY_UNRESOLVED"),
        ),
        "architecture/consumer-need-discovery.yaml": (
            "b4882b4b91bf7dfd433fef9fdca08a297c8a6945",
            "a07d9826deaf4455ea5acbe065f5edd2be2cacb8d80bf3bed6e796ab111e5351",
            ("current_projection_owner: AD-043", "RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS"),
        ),
        "architecture/foundation-promotion-gate.yaml": (
            "78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1",
            "ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd",
            ("schema_version: 5", "active_cycle_id: null", "cycle_id: EVENT_T6"),
        ),
    }

    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = CHECKER_ROOT / "fixtures/assignment_consumer_pressure"
        cls.fixtures = {
            path.name: load_fixture(path) for path in sorted(fixture_root.glob("*.yaml"))
        }
        occupancy_root = CHECKER_ROOT / "fixtures/resource_occupancy"
        cls.occupancy_fixtures = {
            path.stem: load_fixture(path) for path in sorted(occupancy_root.glob("*.yaml"))
        }

    def copy_inputs(self, destination: Path) -> None:
        for relative in self.copied_paths:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copyfile(source, target)

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    def test_repository_assignment_consumer_pressure_is_valid(self) -> None:
        self.assertTrue(validate_assignment_consumer_pressure(ROOT).valid)

    def test_full_resolution_inventory_has_one_exact_synthetic_probe_each(self) -> None:
        expected = {
            (blocker, resolution)
            for blocker, resolutions in assignment_consumer_pressure.BLOCKER_SOLUTIONS.items()
            for resolution in resolutions
        }
        actual = {
            (fixture["probe"]["blocker_id"], fixture["probe"]["resolution_id"])
            for fixture in self.fixtures.values()
        }
        self.assertEqual(actual, expected)
        self.assertEqual(len(self.fixtures), 10)
        for name, fixture in self.fixtures.items():
            with self.subTest(fixture=name):
                validation = validate_reference_fixture(fixture)
                derived = derive_assignment_consumer_pressure(fixture["probe"])
                resolution = fixture["probe"]["resolution_id"]
                blocker = fixture["probe"]["blocker_id"]
                self.assertTrue(validation.valid)
                self.assertEqual(
                    derived.adequacy_effect,
                    assignment_consumer_pressure.RESOLUTION_ADEQUACY[resolution],
                )
                self.assertEqual(derived.live_satisfaction, "undecidable-from-inside")
                self.assertEqual(
                    derived.blocker_classification,
                    assignment_consumer_pressure.EXPECTED_BLOCKER_CLASSIFICATIONS[blocker],
                )

    def test_pressure_result_is_discriminating_and_replayed_on_live_derivation(self) -> None:
        payload = yaml.safe_load((ROOT / self.map_path).read_text(encoding="utf-8"))
        results = {item["blocker_id"]: item for item in payload["blocker_results"]}
        self.assertEqual(set(results), set(assignment_consumer_pressure.BLOCKER_SOLUTIONS))
        for blocker, resolutions in assignment_consumer_pressure.BLOCKER_SOLUTIONS.items():
            with self.subTest(blocker=blocker):
                self.assertEqual(
                    results[blocker]["classification"],
                    assignment_consumer_pressure.EXPECTED_BLOCKER_CLASSIFICATIONS[blocker],
                )
                self.assertEqual(results[blocker]["resolution_ids"], list(resolutions))
                probes = [
                    derive_assignment_consumer_pressure(item["probe"])
                    for item in self.fixtures.values()
                    if item["probe"]["blocker_id"] == blocker
                ]
                self.assertEqual(
                    {item.adequacy_effect for item in probes},
                    {assignment_consumer_pressure.RESOLUTION_ADEQUACY[item] for item in resolutions},
                )
                self.assertEqual(
                    {item.live_satisfaction for item in probes},
                    {"undecidable-from-inside"},
                )
                self.assertEqual(
                    {item.blocker_classification for item in probes},
                    {assignment_consumer_pressure.EXPECTED_BLOCKER_CLASSIFICATIONS[blocker]},
                )

        q2_effects = {
            assignment_consumer_pressure.RESOLUTION_ADEQUACY[item]
            for item in assignment_consumer_pressure.BLOCKER_SOLUTIONS["AMENDMENT_MODEL_ABSENT"]
        }
        temporal_effects = {
            assignment_consumer_pressure.RESOLUTION_ADEQUACY[item]
            for item in assignment_consumer_pressure.BLOCKER_SOLUTIONS["TEMPORAL_MODEL_UNRESOLVED"]
        }
        scope_effects = {
            assignment_consumer_pressure.RESOLUTION_ADEQUACY[item]
            for item in assignment_consumer_pressure.BLOCKER_SOLUTIONS["PARTIAL_SCOPE_IDENTITY_UNRESOLVED"]
        }
        self.assertEqual(
            q2_effects,
            {"current-three-bindings-adequate", "additional-observation-cut-binding-required"},
        )
        self.assertEqual(
            temporal_effects,
            {"current-three-bindings-adequate", "additional-observation-cut-binding-required"},
        )
        self.assertEqual(
            scope_effects,
            {"current-three-bindings-adequate", "additional-part-whole-closure-binding-required"},
        )
        observed_adequacy = {
            resolution: adequacy
            for resolution, adequacy in assignment_consumer_pressure.RESOLUTION_ADEQUACY.items()
            if assignment_consumer_pressure.RESOLUTION_EVIDENCE_MODES[resolution] == "observed"
        }
        self.assertEqual(
            assignment_consumer_pressure._derive_live_adequacy_evidence(ROOT),
            observed_adequacy,
        )
        self.assertNotIn(
            "POST_ESTABLISHMENT_IMMUTABILITY",
            assignment_consumer_pressure._derive_live_adequacy_evidence(ROOT),
        )
        transposed_q2 = dict(assignment_consumer_pressure.RESOLUTION_ADEQUACY)
        transposed_q2["IN_PLACE_TRACEABLE_AMENDMENT"] = "current-three-bindings-adequate"
        transposed_q2["SUPERSEDING_ASSIGNMENT_FOR_CHANGE"] = (
            "additional-observation-cut-binding-required"
        )
        transposed_observed_q2 = {
            resolution: adequacy
            for resolution, adequacy in transposed_q2.items()
            if assignment_consumer_pressure.RESOLUTION_EVIDENCE_MODES[resolution] == "observed"
        }
        self.assertNotEqual(
            assignment_consumer_pressure._derive_live_adequacy_evidence(ROOT),
            transposed_observed_q2,
        )
        with patch.object(
            assignment_consumer_pressure,
            "RESOLUTION_ADEQUACY",
            transposed_q2,
        ):
            self.assertIn(
                "ASSIGNMENT_PRESSURE_PROBE_DRIFT",
                validate_assignment_consumer_pressure(ROOT).errors,
            )

        control = copy.deepcopy(self.occupancy_fixtures["valid-one-effective"])
        self.assertEqual(derive_resource_occupancy(control["dataset"]).occupied, True)
        cross_bound_part = copy.deepcopy(control)
        cross_bound_part["dataset"]["assignment_snapshots"][0]["assignments"][0]["resource_ref"] = "R-001-PART-A"
        self.assertIsNone(derive_resource_occupancy(cross_bound_part["dataset"]).occupied)
        whole_bound_twin = copy.deepcopy(cross_bound_part)
        whole_bound_twin["dataset"]["assignment_snapshots"][0]["assignments"][0]["resource_ref"] = "R-001"
        self.assertTrue(validate_reference_fixture(whole_bound_twin).valid)
        self.assertEqual(derive_resource_occupancy(whole_bound_twin["dataset"]).occupied, True)
        self.assertEqual(
            assignment_consumer_pressure._scope_adequacy(
                cross_bound_part["dataset"], whole_bound_twin["dataset"]
            ),
            "additional-part-whole-closure-binding-required",
        )
        for defect in ("rule_ref", "duplicate_assignment_id", "snapshot_ref"):
            invalid_part = copy.deepcopy(cross_bound_part["dataset"])
            invalid_whole = copy.deepcopy(whole_bound_twin["dataset"])
            if defect == "rule_ref":
                invalid_part["occupancy_request"]["rule_ref"] = "OCP-023@9.9.9"
                invalid_whole["occupancy_request"]["rule_ref"] = "OCP-023@9.9.9"
            elif defect == "duplicate_assignment_id":
                invalid_part["assignment_snapshots"][0]["assignments"].append(
                    copy.deepcopy(invalid_part["assignment_snapshots"][0]["assignments"][0])
                )
                invalid_whole["assignment_snapshots"][0]["assignments"].append(
                    copy.deepcopy(invalid_whole["assignment_snapshots"][0]["assignments"][0])
                )
            else:
                invalid_part["occupancy_request"]["assignment_snapshot_ref"] = "MISSING-SNAPSHOT"
                invalid_whole["occupancy_request"]["assignment_snapshot_ref"] = "MISSING-SNAPSHOT"
            with self.subTest(unrelated_scope_rejection=defect):
                self.assertIsNone(
                    assignment_consumer_pressure._scope_adequacy(invalid_part, invalid_whole)
                )

        exact_bound_whole = copy.deepcopy(self.occupancy_fixtures["valid-zero-assignments"])
        exact_bound_whole["dataset"]["occupancy_request"]["evaluation_time"] = "2026-08-02T11:00:00Z"

        before_retroactive_record = copy.deepcopy(exact_bound_whole)
        before_retroactive_record["dataset"]["occupancy_request"]["assignment_snapshot_ref"] = "SYNTH-SNAPSHOT-RETRO"
        before_retroactive_record["dataset"]["assignment_snapshots"][0]["snapshot_ref"] = "SYNTH-SNAPSHOT-RETRO"
        after_retroactive_record = copy.deepcopy(before_retroactive_record)
        assignment = copy.deepcopy(
            control["dataset"]["assignment_snapshots"][0]["assignments"][0]
        )
        assignment["assignment_id"] = "A-RETRO"
        assignment["transition_history"][0]["transition_id"] = "AT-RETRO"
        assignment["transition_history"][0]["assignment_ref"] = "A-RETRO"
        after_retroactive_record["dataset"]["assignment_snapshots"][0]["assignments"] = [assignment]
        after_retroactive_record["dataset"]["occupancy_request"]["stored_occupied"] = True
        after_retroactive_record["dataset"]["occupancy_request"]["stored_witness_assignment_refs"] = ["A-RETRO"]
        self.assertTrue(validate_reference_fixture(before_retroactive_record).valid)
        self.assertTrue(validate_reference_fixture(after_retroactive_record).valid)
        self.assertEqual(derive_resource_occupancy(before_retroactive_record["dataset"]).occupied, False)
        self.assertEqual(derive_resource_occupancy(after_retroactive_record["dataset"]).occupied, True)

    def test_each_fixture_validation_boundary_is_executable(self) -> None:
        base = next(iter(self.fixtures.values()))
        attacks = {}
        candidate = copy.deepcopy(base)
        del candidate["probe"]["snapshot_ref"]
        attacks["ASSIGNMENT_PRESSURE_FIXTURE_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        candidate["probe"]["question_ids"] = ["Q999"]
        attacks["ASSIGNMENT_PRESSURE_BLOCKER_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        candidate["probe"]["resolution_id"] = "UNKNOWN_RESOLUTION"
        attacks["ASSIGNMENT_PRESSURE_RESOLUTION_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        candidate["probe"]["consumer_need_token"] = "different_need()"
        attacks["ASSIGNMENT_PRESSURE_NEED_BINDING_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        candidate["probe"]["completeness_authority_ref"] = "SYNTH-SELF-SUPPLIED"
        attacks["ASSIGNMENT_PRESSURE_SELF_SUPPLY_FORBIDDEN"] = candidate
        candidate = copy.deepcopy(base)
        candidate["probe"]["selected_resolution"] = True
        attacks["ASSIGNMENT_PRESSURE_FORBIDDEN_OUTCOME"] = candidate
        candidate = copy.deepcopy(base)
        candidate["probe"]["stored_blocker_classification"] = "neutral"
        attacks["ASSIGNMENT_PRESSURE_RESULT_MISMATCH"] = candidate
        self.assertEqual(set(attacks), set(ASSIGNMENT_PRESSURE_ERROR_CODES))
        for error, candidate in attacks.items():
            with self.subTest(error=error):
                self.assertIn(error, validate_reference_fixture(candidate).errors)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        base = next(iter(self.fixtures.values()))
        for value in sorted(assignment_consumer_pressure.PROBE_FIELDS):
            with self.subTest(attribute="PROBE_FIELDS", value=value), patch.object(
                assignment_consumer_pressure,
                "PROBE_FIELDS",
                assignment_consumer_pressure.PROBE_FIELDS - {value},
            ):
                self.assertFalse(validate_reference_fixture(base).valid)
        for value in sorted(assignment_consumer_pressure.FORBIDDEN_FIELDS):
            candidate = copy.deepcopy(base)
            candidate["probe"][value] = True
            self.assertIn("ASSIGNMENT_PRESSURE_FORBIDDEN_OUTCOME", validate_reference_fixture(candidate).errors)
            with self.subTest(attribute="FORBIDDEN_FIELDS", value=value), patch.object(
                assignment_consumer_pressure,
                "FORBIDDEN_FIELDS",
                assignment_consumer_pressure.FORBIDDEN_FIELDS - {value},
            ):
                self.assertNotIn("ASSIGNMENT_PRESSURE_FORBIDDEN_OUTCOME", validate_reference_fixture(candidate).errors)
        for value in sorted(assignment_consumer_pressure.FORBIDDEN_OUTCOMES):
            with self.subTest(attribute="FORBIDDEN_OUTCOMES", value=value), patch.object(
                assignment_consumer_pressure,
                "FORBIDDEN_OUTCOMES",
                assignment_consumer_pressure.FORBIDDEN_OUTCOMES - {value},
            ):
                self.assertFalse(validate_assignment_consumer_pressure(ROOT).valid)

        defensive_structures = (
            "BLOCKER_QUESTIONS", "BLOCKER_SOLUTIONS", "RESOLUTION_DETAILS",
            "RESOLUTION_ADEQUACY", "RESOLUTION_EVIDENCE_MODES", "EXPECTED_BLOCKER_CLASSIFICATIONS",
            "BLOCKER_ADEQUACY_SUMMARIES", "BLOCKER_REASONS",
            "EXPECTED_GATE_FIRST", "EXPECTED_CRITERION",
            "EXPECTED_MISSING_INPUTS", "EXPECTED_CONSUMER",
        )

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
                if isinstance(value, bool):
                    return not value
                if isinstance(value, int):
                    return value + 100
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

        for attribute in defensive_structures:
            original = getattr(assignment_consumer_pressure, attribute)
            for value_path in scalar_paths(original):
                mutated = mutate_scalar(original, value_path)
                with self.subTest(attribute=attribute, value_path=value_path), patch.object(
                    assignment_consumer_pressure, attribute, mutated
                ):
                    self.assertFalse(validate_assignment_consumer_pressure(ROOT).valid)

        scalar_mutations = {
            "BASELINE": "MUTATED-BASELINE",
            "CONSUMER_REF": "MUTATED-CONSUMER",
            "NEED_ID": "MUTATED-NEED",
            "NEED_TOKEN": "mutated_need()",
            "LIVE_SATISFACTION": "satisfied",
            "PRESSURED_CLASSIFICATION": "mutated-pressured",
            "CURRENT_BINDINGS_ADEQUATE": "mutated-adequacy",
            "OBSERVATION_CUT_REQUIRED": "mutated-observation-cut",
            "SCOPE_CLOSURE_REQUIRED": "mutated-scope-closure",
            "ABSENT_AUTHORITY": "present",
        }
        for attribute, mutation in scalar_mutations.items():
            with self.subTest(attribute=attribute), patch.object(
                assignment_consumer_pressure, attribute, mutation
            ):
                self.assertTrue(
                    not validate_assignment_consumer_pressure(ROOT).valid
                    or not validate_reference_fixture(base).valid
                )

    def test_live_blocker_need_probe_and_gate_mutations_fail_independently(self) -> None:
        cases = ("blocker", "need", "probe", "gate")
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                if case == "blocker":
                    relative = Path("architecture/assignment-stable-surface.yaml")
                    payload = yaml.safe_load((root / relative).read_text(encoding="utf-8"))
                    payload["blockers"] = payload["blockers"][1:]
                    expected = ASSIGNMENT_PRESSURE_BLOCKER_DRIFT
                elif case == "need":
                    relative = Path("architecture/consumer-need-discovery.yaml")
                    payload = yaml.safe_load((root / relative).read_text(encoding="utf-8"))
                    payload["current_result"]["unmet_positive_needs"] = []
                    expected = ASSIGNMENT_PRESSURE_CONSUMER_NEED_DRIFT
                elif case == "probe":
                    relative = self.map_path
                    payload = yaml.safe_load((root / relative).read_text(encoding="utf-8"))
                    payload["resolution_inventory"] = payload["resolution_inventory"][1:]
                    expected = ASSIGNMENT_PRESSURE_PROBE_DRIFT
                else:
                    relative = Path("architecture/foundation-promotion-gate.yaml")
                    payload = yaml.safe_load((root / relative).read_text(encoding="utf-8"))
                    payload["cycle_protocol"]["active_cycle_id"] = "ASSIGNMENT_T7"
                    expected = ASSIGNMENT_PRESSURE_GATE_DRIFT
                self.write_yaml(root, relative, payload)
                self.assertIn(expected, validate_assignment_consumer_pressure(root).errors)

    def test_baseline_anchors_reverse_resolve_and_hash_full_chain(self) -> None:
        tree = subprocess.check_output(
            ["git", "ls-tree", "-r", self.baseline], cwd=ROOT, text=True
        )
        for relative, (expected_blob, expected_sha, tokens) in self.baseline_anchors.items():
            with self.subTest(path=relative):
                blob = subprocess.check_output(
                    ["git", "rev-parse", f"{self.baseline}:{relative}"], cwd=ROOT, text=True
                ).strip()
                self.assertEqual(blob, expected_blob)
                reverse_paths = [
                    line.split("\t", 1)[1]
                    for line in tree.splitlines()
                    if line.split()[2] == blob
                ]
                self.assertIn(relative, reverse_paths)
                raw = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
                text = raw.decode("utf-8")
                for token in tokens:
                    self.assertIn(token, text)
                self.assertEqual(hashlib.sha256(raw).hexdigest(), expected_sha)

    def test_protected_existing_artifacts_and_fixtures_are_byte_identical(self) -> None:
        listing = subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", self.baseline], cwd=ROOT, text=True
        ).splitlines()
        protected = [
            relative for relative in listing
            if relative.startswith("docs/")
            or relative.startswith("patterns/")
            or relative.startswith("tools/ontology_checker/fixtures/")
            or "/reviewed-contract-" in relative
            or relative == "architecture/foundation-promotion-gate.yaml"
        ]
        for relative in protected:
            with self.subTest(path=relative):
                expected = subprocess.check_output(
                    ["git", "rev-parse", f"{self.baseline}:{relative}"], cwd=ROOT, text=True
                ).strip()
                actual = subprocess.check_output(
                    ["git", "hash-object", relative], cwd=ROOT, text=True
                ).strip()
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
