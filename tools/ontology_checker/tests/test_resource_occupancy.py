from __future__ import annotations

import copy
import hashlib
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    derive_resource_occupancy,
    load_fixture,
    validate_reference_fixture,
)
from ocp_checker import resource_occupancy  # noqa: E402


class ResourceOccupancyTests(unittest.TestCase):
    baseline = "5d60bfc4ba96f49382383d487d26ef971c4a0cde"
    baseline_anchors = {
        "docs/003-resource-concept/README.md": (
            "71485bb337cfd59def2e0f1b18b474a7959bd30c",
            "f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315",
            ("Version: 1.0.0", "Status: Canonical", "Concept-Status: Canonical"),
        ),
        "docs/005-assignment-concept/README.md": (
            "6e6c00e723b15a348e7610d4ca5a1ae23526c52b",
            "a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065",
            ("Version: 0.2.8", "Status: Draft", "Concept-Status: Accepted"),
        ),
        "docs/016-core-boundary/README.md": (
            "94f5d997deea0168a3c553c2ac9f19d2ee03b4fb",
            "78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4",
            ("Version: 1.0.0", "Status: Canonical", "Route D", "G4"),
        ),
        "architecture/discovery/AD-036-consumer-need-discovery.md": (
            "3f8642777c16015226065f29f745b2e31bb6cd3a",
            "564bc5c5b7d12c2be95278af6b3518a3af773ade701e3fee1dc4a9a4daac5603",
            ("Version: 0.1.0", "No current Accepted or Canonical document states an unmet positive consumer need"),
        ),
        "tools/ontology_checker/ocp_checker/checker.py": (
            "120ada9dd00b1df0b46cf3060aef2b0c290948b1",
            "3a093f0d76113bb5dd2799c7d0aaf73b51b752569dc13de145bb3d158a7b4a47",
            ("def assignment_effective_at(", "def derived_participates_in("),
        ),
        "tools/ontology_checker/ocp_checker/__init__.py": (
            "cf7aec93f299a072075adce93ffe4bcb6a3c5c99",
            "bd4b4a9be22e4d6e8f9c50bb4b11a6b68406d18fac7445b9aa1714da7c16763d",
            ("def validate_reference_fixture(fixture):",),
        ),
    }
    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = ROOT / "fixtures/resource_occupancy"
        cls.fixtures = {
            path.stem: load_fixture(path) for path in sorted(fixture_root.glob("*.yaml"))
        }

    def test_required_synthetic_fixture_matrix(self) -> None:
        expected = {
            "valid-zero-assignments": (False, ()),
            "valid-one-effective": (True, ("A-001",)),
            "valid-two-overlapping": (True, ("A-001", "A-002")),
            "valid-two-nonoverlapping": (False, ()),
            "valid-start-boundary": (True, ("A-001",)),
            "valid-end-boundary": (False, ()),
        }
        self.assertEqual(set(self.fixtures), set(expected))
        for name, (occupied, witnesses) in expected.items():
            with self.subTest(fixture=name):
                fixture = self.fixtures[name]
                validation = validate_reference_fixture(fixture)
                derived = derive_resource_occupancy(fixture["dataset"])
                self.assertTrue(validation.valid)
                self.assertEqual(derived.occupied, occupied)
                self.assertEqual(derived.witness_assignment_refs, witnesses)

    def test_fixture_expected_results_are_exact(self) -> None:
        for name, fixture in self.fixtures.items():
            with self.subTest(fixture=name):
                validation = validate_reference_fixture(fixture)
                self.assertEqual(validation.valid, fixture["expected"]["valid"])
                self.assertEqual(set(validation.errors), set(fixture["expected"]["error_codes"]))

    def test_overlap_reports_all_witnesses_without_selection_order(self) -> None:
        fixture = copy.deepcopy(self.fixtures["valid-two-overlapping"])
        assignments = fixture["dataset"]["assignment_snapshots"][0]["assignments"]
        assignments.reverse()
        derived = derive_resource_occupancy(fixture["dataset"])
        self.assertEqual(derived.occupied, True)
        self.assertEqual(derived.witness_assignment_refs, ("A-001", "A-002"))
        self.assertTrue(validate_reference_fixture(fixture).valid)

    def test_false_result_requires_completeness_evidence(self) -> None:
        fixture = copy.deepcopy(self.fixtures["valid-zero-assignments"])
        fixture["dataset"]["assignment_snapshots"][0]["completeness_evidence_ref"] = None
        validation = validate_reference_fixture(fixture)
        derived = derive_resource_occupancy(fixture["dataset"])
        self.assertIn("RESOURCE_OCCUPANCY_COMPLETENESS_EVIDENCE_REQUIRED", validation.errors)
        self.assertIsNone(derived.occupied)
        self.assertEqual(derived.witness_assignment_refs, ())

    def test_each_validation_boundary_is_executable(self) -> None:
        base = self.fixtures["valid-one-effective"]
        attacks = {}

        candidate = copy.deepcopy(base)
        del candidate["dataset"]["assignment_snapshots"]
        attacks["RESOURCE_OCCUPANCY_FIXTURE_INVALID"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["occupancy_request"]["evaluation_time"] = "not-a-time"
        attacks["RESOURCE_OCCUPANCY_REQUEST_INVALID"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["assignment_snapshots"][0]["assignments"] = "not-a-list"
        attacks["RESOURCE_OCCUPANCY_SNAPSHOT_INVALID"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["occupancy_request"]["assignment_snapshot_ref"] = "MISSING"
        attacks["RESOURCE_OCCUPANCY_SNAPSHOT_UNRESOLVED"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["assignment_snapshots"].append(
            copy.deepcopy(candidate["dataset"]["assignment_snapshots"][0])
        )
        attacks["RESOURCE_OCCUPANCY_SNAPSHOT_AMBIGUOUS"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["assignment_snapshots"][0]["resource_ref"] = "R-002"
        attacks["RESOURCE_OCCUPANCY_BINDING_MISMATCH"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["assignment_snapshots"][0]["completeness_evidence_ref"] = None
        attacks["RESOURCE_OCCUPANCY_COMPLETENESS_EVIDENCE_REQUIRED"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["assignment_snapshots"][0]["assignments"][0]["operation_ref"] = None
        attacks["RESOURCE_OCCUPANCY_ASSIGNMENT_INVALID"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["assignment_snapshots"][0]["assignments"].append(
            copy.deepcopy(candidate["dataset"]["assignment_snapshots"][0]["assignments"][0])
        )
        attacks["RESOURCE_OCCUPANCY_ASSIGNMENT_DUPLICATE"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["assignment_snapshots"][0]["assignments"][0]["activation_state"] = "active"
        attacks["RESOURCE_OCCUPANCY_ACTIVATION_FORBIDDEN"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["assignment_snapshots"][0]["assignments"][0]["conflict"] = True
        attacks["RESOURCE_OCCUPANCY_FORBIDDEN_COUPLING"] = candidate

        candidate = copy.deepcopy(base)
        candidate["dataset"]["occupancy_request"]["stored_occupied"] = False
        attacks["RESOURCE_OCCUPANCY_RESULT_MISMATCH"] = candidate

        self.assertEqual(set(attacks), set(resource_occupancy.RESOURCE_OCCUPANCY_ERROR_CODES))
        for error, candidate in attacks.items():
            with self.subTest(error=error):
                self.assertIn(error, validate_reference_fixture(candidate).errors)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        base = self.fixtures["valid-one-effective"]

        for attribute in ("DATASET_FIELDS", "REQUEST_FIELDS", "SNAPSHOT_FIELDS"):
            values = getattr(resource_occupancy, attribute)
            for value in sorted(values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    resource_occupancy, attribute, values - {value}
                ):
                    self.assertFalse(validate_reference_fixture(base).valid)

        for attribute, expected_error in (
            ("ACTIVATION_FIELDS", "RESOURCE_OCCUPANCY_ACTIVATION_FORBIDDEN"),
            ("FORBIDDEN_FIELDS", "RESOURCE_OCCUPANCY_FORBIDDEN_COUPLING"),
        ):
            values = getattr(resource_occupancy, attribute)
            for value in sorted(values):
                candidate = copy.deepcopy(base)
                candidate["dataset"]["assignment_snapshots"][0]["assignments"][0][value] = True
                self.assertIn(expected_error, validate_reference_fixture(candidate).errors)
                with self.subTest(attribute=attribute, value=value), patch.object(
                    resource_occupancy, attribute, values - {value}
                ):
                    self.assertNotIn(expected_error, validate_reference_fixture(candidate).errors)

        with patch.object(resource_occupancy, "RULE_REF", "resource-occupancy-at@SYNTH"):
            self.assertFalse(validate_reference_fixture(base).valid)
        with patch.object(resource_occupancy, "SYNTHETIC_COMPLETENESS_PREFIX", "MUTATED-"):
            self.assertFalse(validate_reference_fixture(base).valid)

        manifest = yaml.safe_load(
            (ROOT / "resource-occupancy-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"] for item in manifest if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {item["id"] for item in manifest if item.get("kind") == "derivation"}
        for value in sorted(resource_occupancy.RESOURCE_OCCUPANCY_ERROR_CODES):
            with self.subTest(attribute="RESOURCE_OCCUPANCY_ERROR_CODES", value=value), patch.object(
                resource_occupancy,
                "RESOURCE_OCCUPANCY_ERROR_CODES",
                resource_occupancy.RESOURCE_OCCUPANCY_ERROR_CODES - {value},
            ):
                self.assertNotEqual(validation_ids, set(resource_occupancy.RESOURCE_OCCUPANCY_ERROR_CODES))
        for value in sorted(resource_occupancy.RESOURCE_OCCUPANCY_DERIVATION_RULES):
            with self.subTest(attribute="RESOURCE_OCCUPANCY_DERIVATION_RULES", value=value), patch.object(
                resource_occupancy,
                "RESOURCE_OCCUPANCY_DERIVATION_RULES",
                resource_occupancy.RESOURCE_OCCUPANCY_DERIVATION_RULES - {value},
            ):
                self.assertNotEqual(derivation_ids, set(resource_occupancy.RESOURCE_OCCUPANCY_DERIVATION_RULES))

    def test_manifest_matches_exported_rules(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "resource-occupancy-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"] for item in rules if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {item["id"] for item in rules if item.get("kind") == "derivation"}
        self.assertEqual(validation_ids, set(resource_occupancy.RESOURCE_OCCUPANCY_ERROR_CODES))
        self.assertEqual(derivation_ids, set(resource_occupancy.RESOURCE_OCCUPANCY_DERIVATION_RULES))

    def test_existing_single_assignment_truth_is_reused_without_mutation(self) -> None:
        fixture = self.fixtures["valid-two-overlapping"]
        assignments = fixture["dataset"]["assignment_snapshots"][0]["assignments"]
        before = copy.deepcopy(assignments)
        derive_resource_occupancy(fixture["dataset"])
        self.assertEqual(assignments, before)

    def test_baseline_anchors_reverse_resolve_and_hash_full_chain(self) -> None:
        for relative, (expected_blob, expected_sha, state_tokens) in self.baseline_anchors.items():
            with self.subTest(path=relative):
                blob = subprocess.check_output(
                    ["git", "rev-parse", f"{self.baseline}:{relative}"],
                    cwd=REPO_ROOT,
                    text=True,
                ).strip()
                self.assertEqual(blob, expected_blob)
                tree = subprocess.check_output(
                    ["git", "ls-tree", "-r", self.baseline],
                    cwd=REPO_ROOT,
                    text=True,
                )
                reverse_paths = [
                    line.split("\t", 1)[1]
                    for line in tree.splitlines()
                    if line.split()[2] == blob
                ]
                self.assertEqual(reverse_paths, [relative])
                raw = subprocess.check_output(
                    ["git", "cat-file", "blob", blob], cwd=REPO_ROOT
                )
                self.assertEqual(hashlib.sha256(raw).hexdigest(), expected_sha)
                text = raw.decode("utf-8")
                for token in state_tokens:
                    self.assertIn(token, text)
                if relative.endswith("ocp_checker/__init__.py"):
                    self.assertNotIn("ResourceOccupancyDataset", text)

    def test_protected_existing_artifacts_and_fixtures_are_byte_identical(self) -> None:
        baseline_fixture_paths = subprocess.check_output(
            [
                "git",
                "ls-tree",
                "-r",
                "--name-only",
                self.baseline,
                "--",
                "tools/ontology_checker/fixtures",
            ],
            cwd=REPO_ROOT,
            text=True,
        ).splitlines()
        self.assertTrue(baseline_fixture_paths)
        self.assertFalse(
            any(
                path.startswith("tools/ontology_checker/fixtures/resource_occupancy/")
                for path in baseline_fixture_paths
            )
        )
        protected = [
            *(
                str(next(REPO_ROOT.glob(f"docs/{number:03d}-*"))).replace(
                    str(REPO_ROOT) + "/", ""
                )
                for number in range(23)
                if number not in {5, 6}
            ),
            "patterns",
            "architecture/baselines/foundation-map.md",
            *baseline_fixture_paths,
        ]
        completed = subprocess.run(
            ["git", "diff", "--quiet", self.baseline, "--", *protected],
            cwd=REPO_ROOT,
            check=False,
        )
        self.assertEqual(completed.returncode, 0)
        self.assertEqual(
            (REPO_ROOT / "docs/006-constraint-concept/reviewed-contract-v0.3.2.md").read_bytes(),
            subprocess.check_output(["git", "show", f"{self.baseline}:docs/006-constraint-concept/README.md"], cwd=REPO_ROOT),
        )
        self.assertEqual(
            (REPO_ROOT / "architecture/baselines/foundation-promotion-gate-pre-ocp006-acceptance.yaml").read_bytes(),
            subprocess.check_output(["git", "show", f"{self.baseline}:architecture/foundation-promotion-gate.yaml"], cwd=REPO_ROOT),
        )


if __name__ == "__main__":
    unittest.main()
