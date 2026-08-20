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
    derive_completeness_evidence_recognition,
    load_fixture,
    validate_reference_fixture,
)
from ocp_checker import completeness_evaluator  # noqa: E402


class CompletenessEvaluatorTests(unittest.TestCase):
    baseline = "46c822ce25ca31f99daf6168caffca67f75fe244"
    baseline_anchors = {
        "docs/016-core-boundary/README.md": (
            "94f5d997deea0168a3c553c2ac9f19d2ee03b4fb",
            "78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4",
            ("Version: 1.0.0", "Status: Canonical", "Route D", "G4"),
        ),
        "docs/023-resource-occupancy/README.md": (
            "a846333fae80aff2b3697e811d2b155c91f04122",
            "5ec9aca56de4524b4ab78a9e98e2cf5d7561d6f13bac8cf7778d66a99f5490d9",
            ("Version: 0.2.0", "Status: Accepted", "assignment_set_complete_for_resource"),
        ),
        "architecture/discovery/AD-042-resource-occupancy-acceptance.md": (
            "02d646d4e0c4e2abbce6bc782cfb011de04b0015",
            "7c9ab64736a9c2547b77abb94069e62672c5a8cb09532b061eeb7e3aec06520c",
            ("Decision-ID: AD-042", "Status: Accepted", "legitimate owner/evaluator"),
        ),
        "architecture/consumer-need-discovery.yaml": (
            "bcde824ae979e2ebf46ffaaa39967b015b92d618",
            "ed22ad35fac0f9c29663a789488b93d8fe20eb4762abf2428635b665dd7029a3",
            ("schema_version: 2", "RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS"),
        ),
        "tools/ontology_checker/ocp_checker/resource_occupancy.py": (
            "3d7ee96ac0d9f51cb04fd860cb5117806b422549",
            "a44caaa19f1964e72b3c97f23175fa65695ce3b95e54f4b6f76fdf6bf96658c3",
            ("def derive_resource_occupancy(", "SYNTHETIC_COMPLETENESS_PREFIX"),
        ),
        "tools/ontology_checker/resource-occupancy-rules.yaml": (
            "32e7ac535b6a24fc30784deee59411597725998d",
            "16cf4094dff5775e34731862dafc3b455b6b31eac0d17733d7fd3496ca06e496",
            ("RESOURCE_OCCUPANCY_COMPLETENESS_EVIDENCE_REQUIRED", "derive_resource_occupancy"),
        ),
    }

    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = ROOT / "fixtures/completeness_evaluator"
        cls.fixtures = {
            path.stem: load_fixture(path) for path in sorted(fixture_root.glob("*.yaml"))
        }

    def test_required_synthetic_fixture_matrix(self) -> None:
        expected = {
            "valid-synthetic-reference": "synthetic-reference-recognized",
            "invalid-stale-evidence": "indeterminate",
            "invalid-unresolved-authority": "indeterminate",
            "invalid-conflicting-evidence": "indeterminate",
            "invalid-activation": "indeterminate",
            "invalid-forbidden-coupling": "indeterminate",
        }
        self.assertEqual(set(self.fixtures), set(expected))
        for name, expected_result in expected.items():
            with self.subTest(fixture=name):
                derived = derive_completeness_evidence_recognition(
                    self.fixtures[name]["dataset"]
                )
                self.assertEqual(derived.result, expected_result)

    def test_fixture_expected_results_are_exact(self) -> None:
        for name, fixture in self.fixtures.items():
            with self.subTest(fixture=name):
                validation = validate_reference_fixture(fixture)
                self.assertEqual(validation.valid, fixture["expected"]["valid"])
                self.assertEqual(set(validation.errors), set(fixture["expected"]["error_codes"]))

    def test_invalid_stale_conflicting_or_ungrounded_never_derives_false(self) -> None:
        for name in (
            "invalid-stale-evidence",
            "invalid-unresolved-authority",
            "invalid-conflicting-evidence",
        ):
            with self.subTest(fixture=name):
                derived = derive_completeness_evidence_recognition(
                    self.fixtures[name]["dataset"]
                )
                self.assertEqual(derived.result, completeness_evaluator.INDETERMINATE)
                self.assertNotEqual(derived.result, "false")

    def test_each_validation_boundary_is_executable(self) -> None:
        base = self.fixtures["valid-synthetic-reference"]
        attacks = {}

        candidate = copy.deepcopy(base)
        del candidate["dataset"]["evaluator_profiles"]
        attacks["COMPLETENESS_EVALUATOR_FIXTURE_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        candidate["dataset"]["recognition_request"]["rule_ref"] = "wrong@0"
        attacks["COMPLETENESS_EVALUATOR_REQUEST_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        del candidate["dataset"]["evaluator_profiles"][0]["domain_ref"]
        attacks["COMPLETENESS_EVALUATOR_PROFILE_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        del candidate["dataset"]["completeness_evidence"][0]["claim"]
        attacks["COMPLETENESS_EVALUATOR_EVIDENCE_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        candidate["dataset"]["recognition_request"]["evaluator_profile_ref"] = "MISSING"
        attacks["COMPLETENESS_EVALUATOR_REFERENCE_UNRESOLVED"] = candidate
        candidate = copy.deepcopy(base)
        candidate["dataset"]["evaluator_profiles"].append(
            copy.deepcopy(candidate["dataset"]["evaluator_profiles"][0])
        )
        attacks["COMPLETENESS_EVALUATOR_REFERENCE_AMBIGUOUS"] = candidate
        candidate = copy.deepcopy(base)
        candidate["dataset"]["completeness_evidence"][0]["resource_ref"] = "R-002"
        attacks["COMPLETENESS_EVALUATOR_SUBJECT_MISMATCH"] = candidate
        candidate = copy.deepcopy(base)
        candidate["dataset"]["completeness_evidence"][0]["coverage_kind"] = "subset"
        attacks["COMPLETENESS_EVALUATOR_SCOPE_MISMATCH"] = candidate
        attacks["COMPLETENESS_EVALUATOR_TIME_INVALID"] = self.fixtures["invalid-stale-evidence"]
        attacks["COMPLETENESS_EVALUATOR_AUTHORITY_UNRESOLVED"] = self.fixtures[
            "invalid-unresolved-authority"
        ]
        attacks["COMPLETENESS_EVALUATOR_EVIDENCE_CONFLICT"] = self.fixtures[
            "invalid-conflicting-evidence"
        ]
        attacks["COMPLETENESS_EVALUATOR_ACTIVATION_FORBIDDEN"] = self.fixtures[
            "invalid-activation"
        ]
        attacks["COMPLETENESS_EVALUATOR_FORBIDDEN_COUPLING"] = self.fixtures[
            "invalid-forbidden-coupling"
        ]
        candidate = copy.deepcopy(base)
        candidate["dataset"]["recognition_request"]["stored_result"] = "indeterminate"
        attacks["COMPLETENESS_EVALUATOR_RESULT_MISMATCH"] = candidate

        self.assertEqual(set(attacks), set(completeness_evaluator.COMPLETENESS_EVALUATOR_ERROR_CODES))
        for error, candidate in attacks.items():
            with self.subTest(error=error):
                self.assertIn(error, validate_reference_fixture(candidate).errors)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        base = self.fixtures["valid-synthetic-reference"]
        for attribute in ("DATASET_FIELDS", "REQUEST_FIELDS", "PROFILE_FIELDS", "EVIDENCE_FIELDS"):
            values = getattr(completeness_evaluator, attribute)
            for value in sorted(values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    completeness_evaluator, attribute, values - {value}
                ):
                    self.assertFalse(validate_reference_fixture(base).valid)

        for attribute, expected_error in (
            ("ACTIVATION_FIELDS", "COMPLETENESS_EVALUATOR_ACTIVATION_FORBIDDEN"),
            ("FORBIDDEN_FIELDS", "COMPLETENESS_EVALUATOR_FORBIDDEN_COUPLING"),
        ):
            values = getattr(completeness_evaluator, attribute)
            for value in sorted(values):
                candidate = copy.deepcopy(base)
                candidate["dataset"]["completeness_evidence"][0][value] = True
                self.assertIn(expected_error, validate_reference_fixture(candidate).errors)
                with self.subTest(attribute=attribute, value=value), patch.object(
                    completeness_evaluator, attribute, values - {value}
                ):
                    self.assertNotIn(expected_error, validate_reference_fixture(candidate).errors)

        scalar_mutations = {
            "RULE_REF": "mutated@0",
            "DOMAIN_REF": "mutated-domain",
            "SUBJECT_KIND": "mutated-subject",
            "COVERAGE_KIND": "mutated-coverage",
            "POSITIVE_CLAIM": "mutated-claim",
            "REFERENCE_RESULT": "mutated-result",
            "SYNTHETIC_EVALUATOR_PREFIX": "MUTATED-EVALUATOR-",
            "SYNTHETIC_AUTHORITY_PREFIX": "MUTATED-AUTHORITY-",
        }
        for attribute, value in scalar_mutations.items():
            with self.subTest(attribute=attribute), patch.object(
                completeness_evaluator, attribute, value
            ):
                self.assertFalse(validate_reference_fixture(base).valid)

        manifest = yaml.safe_load(
            (ROOT / "completeness-evaluator-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"] for item in manifest if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {item["id"] for item in manifest if item.get("kind") == "derivation"}
        for value in sorted(completeness_evaluator.COMPLETENESS_EVALUATOR_ERROR_CODES):
            with self.subTest(attribute="error-code", value=value), patch.object(
                completeness_evaluator,
                "COMPLETENESS_EVALUATOR_ERROR_CODES",
                completeness_evaluator.COMPLETENESS_EVALUATOR_ERROR_CODES - {value},
            ):
                self.assertNotEqual(
                    validation_ids, set(completeness_evaluator.COMPLETENESS_EVALUATOR_ERROR_CODES)
                )
        for value in sorted(completeness_evaluator.COMPLETENESS_EVALUATOR_DERIVATION_RULES):
            with self.subTest(attribute="derivation", value=value), patch.object(
                completeness_evaluator,
                "COMPLETENESS_EVALUATOR_DERIVATION_RULES",
                completeness_evaluator.COMPLETENESS_EVALUATOR_DERIVATION_RULES - {value},
            ):
                self.assertNotEqual(
                    derivation_ids,
                    set(completeness_evaluator.COMPLETENESS_EVALUATOR_DERIVATION_RULES),
                )

    def test_manifest_matches_exported_rules(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "completeness-evaluator-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        self.assertEqual(
            {item["id"] for item in rules if item.get("kind", "validation") == "validation"},
            set(completeness_evaluator.COMPLETENESS_EVALUATOR_ERROR_CODES),
        )
        self.assertEqual(
            {item["id"] for item in rules if item.get("kind") == "derivation"},
            set(completeness_evaluator.COMPLETENESS_EVALUATOR_DERIVATION_RULES),
        )

    def test_baseline_anchors_reverse_resolve_and_hash_full_chain(self) -> None:
        tree = subprocess.check_output(
            ["git", "ls-tree", "-r", self.baseline], cwd=REPO_ROOT, text=True
        )
        for relative, (expected_blob, expected_sha, tokens) in self.baseline_anchors.items():
            with self.subTest(path=relative):
                blob = subprocess.check_output(
                    ["git", "rev-parse", f"{self.baseline}:{relative}"],
                    cwd=REPO_ROOT,
                    text=True,
                ).strip()
                self.assertEqual(blob, expected_blob)
                reverse_paths = [
                    line.split("\t", 1)[1]
                    for line in tree.splitlines()
                    if line.split()[2] == blob
                ]
                self.assertIn(relative, reverse_paths)
                raw = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=REPO_ROOT)
                text = raw.decode("utf-8")
                for token in tokens:
                    self.assertIn(token, text)
                self.assertEqual(hashlib.sha256(raw).hexdigest(), expected_sha)

    def test_protected_existing_artifacts_and_fixtures_are_byte_identical(self) -> None:
        listing = subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", self.baseline],
            cwd=REPO_ROOT,
            text=True,
        ).splitlines()
        protected = [
            path for path in listing
            if path.startswith("patterns/")
            or path.startswith("tools/ontology_checker/fixtures/")
            or "/reviewed-contract-" in path
            or any(
                path.startswith(f"docs/{number:03d}-")
                for number in range(24)
                if number != 5
            )
        ]
        self.assertTrue(protected)
        for relative in protected:
            with self.subTest(path=relative):
                expected = subprocess.check_output(
                    ["git", "rev-parse", f"{self.baseline}:{relative}"],
                    cwd=REPO_ROOT,
                    text=True,
                ).strip()
                actual = subprocess.check_output(
                    ["git", "hash-object", relative], cwd=REPO_ROOT, text=True
                ).strip()
                self.assertEqual(actual, expected)

    def test_route_d_contract_does_not_activate_completeness(self) -> None:
        source = (REPO_ROOT / "docs/024-completeness-evaluator/README.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Route D", source)
        self.assertIn("Actual legitimacy cannot be established", source)
        self.assertIn("does not assert that any real Assignment set is complete", source)
        self.assertIn("Status: Accepted", source)

        observed_results = {
            derive_completeness_evidence_recognition(fixture["dataset"]).result
            for fixture in self.fixtures.values()
        }
        self.assertEqual(
            observed_results,
            {"synthetic-reference-recognized", "indeterminate"},
        )
        self.assertNotIn(False, observed_results)
        self.assertNotIn("complete", observed_results)
        self.assertNotIn("occupied=false", observed_results)

        valid = self.fixtures["valid-synthetic-reference"]["dataset"]
        for field, replacement in (
            ("evaluator_ref", "PRODUCTION-EVALUATOR-001"),
            ("authority_basis_ref", "PRODUCTION-AUTHORITY-001"),
        ):
            with self.subTest(field=field):
                mutated = copy.deepcopy(valid)
                mutated["evaluator_profiles"][0][field] = replacement
                self.assertEqual(
                    derive_completeness_evidence_recognition(mutated).result,
                    "indeterminate",
                )
                self.assertFalse(
                    completeness_evaluator.validate_completeness_evaluator_dataset(mutated).valid
                )


if __name__ == "__main__":
    unittest.main()
