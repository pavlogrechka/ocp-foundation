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

from ocp_checker import assignment_norm_compatibility  # noqa: E402
from ocp_checker.assignment_norm_compatibility import (  # noqa: E402
    ASSIGNMENT_NORM_ERROR_CODES,
    ASSIGNMENT_NORM_GATE_DRIFT,
    ASSIGNMENT_NORM_PROBE_DRIFT,
    ASSIGNMENT_NORM_SOURCE_DRIFT,
    ASSIGNMENT_NORM_SURVIVOR_DRIFT,
    derive_assignment_norm_compatibility,
    validate_assignment_norm_compatibility,
)
from ocp_checker import validate_reference_fixture  # noqa: E402
from ocp_checker.checker import load_fixture  # noqa: E402


class AssignmentNormCompatibilityTests(unittest.TestCase):
    baseline = "734dd019425b636f47187bf1c342612550028400"
    map_path = Path("architecture/assignment-norm-compatibility.yaml")
    copied_paths = (
        map_path,
        Path("architecture/assignment-consumer-pressure.yaml"),
        Path("architecture/assignment-stable-surface.yaml"),
        Path("architecture/foundation-promotion-gate.yaml"),
        Path("tools/ontology_checker/fixtures/assignment_norm_compatibility"),
        Path("docs"),
    )
    baseline_anchors = {
        "docs/002-concept-taxonomy/README.md": (
            "295512bdfaffd679ae021d0876072cdbcb2be75e",
            "d49e9f896508d246994fd954174f04c69e0b4d32dfacc1dd612659263118df77",
            ("Version: 1.6.0", "Status: Canonical", "рівно одного Resource"),
        ),
        "docs/003-resource-concept/README.md": (
            "71485bb337cfd59def2e0f1b18b474a7959bd30c",
            "f8656769dd046f221843f627c746d0d6040c2e83c736b900370d60244fce8315",
            ("Version: 1.0.0", "Status: Canonical", "Composite Assignment не створює"),
        ),
        "docs/004-operation-concept/README.md": (
            "37fab136c578d2b8fafd6e900261ef64144943d9",
            "ff0480913044b4dff8abcf69808b2d1cafe80a7d9f58c7ec06d2adeb33745538",
            ("Version: 1.0.1", "Status: Canonical", "має власну ідентичність"),
        ),
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
        "docs/017-operation-lifecycle/README.md": (
            "0b2ea683df308babd1111ff47e9272c9b0742f78",
            "061e2c8a4c9d3d02bb5a7492e9c8723cace11a462548970727552e18c645a030",
            ("Version: 0.2.0", "Status: Accepted", "requires a separate owner and Board act"),
        ),
        "docs/023-resource-occupancy/README.md": (
            "a846333fae80aff2b3697e811d2b155c91f04122",
            "5ec9aca56de4524b4ab78a9e98e2cf5d7561d6f13bac8cf7778d66a99f5490d9",
            ("Version: 0.2.0", "Status: Accepted", "neither defines retroactivity"),
        ),
        "architecture/assignment-consumer-pressure.yaml": (
            "2a96810984b79374c04bff20663cbc6953744c3d",
            "d20f8b8330b4efdb6a23c09aa6f02b2182182ddd022486c370b11afb1d8f61b2",
            ("rule_owner: AD-044", "SUPERSEDING_ASSIGNMENT_FOR_CHANGE", "WHOLE_RESOURCE_ONLY"),
        ),
        "architecture/assignment-stable-surface.yaml": (
            "eea05626eddfba594508c5e6d4c4d5bd851c0f5a",
            "b887717a064d479830b7aa0f360d2793a3cba4e54d2b1537d19374e553b3b593",
            ("AMENDMENT_MODEL_ABSENT", "TEMPORAL_MODEL_UNRESOLVED", "PARTIAL_SCOPE_IDENTITY_UNRESOLVED"),
        ),
        "architecture/foundation-promotion-gate.yaml": (
            "78f5f75d84fe9b0bdbf43ad3922404fa34f6c2d1",
            "ca11036e10397d24b308957e059d0d5def1a9d90177c0d82987191c919a56dfd",
            ("schema_version: 5", "active_cycle_id: null", "cycle_id: EVENT_T6"),
        ),
    }

    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = CHECKER_ROOT / "fixtures/assignment_norm_compatibility"
        cls.fixtures = {
            path.name: load_fixture(path) for path in sorted(fixture_root.glob("*.yaml"))
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

    def test_repository_assignment_norm_compatibility_is_valid(self) -> None:
        self.assertTrue(validate_assignment_norm_compatibility(ROOT).valid)

    def test_all_six_survivors_have_one_exact_analytic_probe(self) -> None:
        self.assertEqual(len(self.fixtures), 6)
        self.assertEqual(
            {item["probe"]["resolution_id"] for item in self.fixtures.values()},
            set(assignment_norm_compatibility.SURVIVOR_CLAIMS),
        )
        classifications = {}
        for name, fixture in self.fixtures.items():
            with self.subTest(fixture=name):
                self.assertTrue(validate_reference_fixture(fixture).valid)
                derived = derive_assignment_norm_compatibility(fixture["probe"])
                self.assertEqual(derived.classification, fixture["probe"]["stored_classification"])
                self.assertEqual(fixture["probe"]["evidence_mode"], "analytic")
                classifications[fixture["probe"]["resolution_id"]] = derived.classification
        self.assertEqual(
            [resolution for resolution, value in classifications.items() if value == "compatible"],
            ["WHOLE_RESOURCE_ONLY"],
        )
        self.assertNotIn("incompatible", classifications.values())

    def test_current_authoritative_source_floor_and_exact_tokens_are_live(self) -> None:
        self.assertTrue(assignment_norm_compatibility._live_sources_valid(ROOT))
        payload = yaml.safe_load((ROOT / self.map_path).read_text(encoding="utf-8"))
        self.assertEqual(
            payload["source_policy"]["current_document_statuses"],
            ["Draft", "Accepted", "Canonical"],
        )
        self.assertTrue(
            payload["source_policy"]["subject_inventory_and_source_eligibility_are_separate"]
        )
        self.assertFalse(payload["source_policy"]["historical_snapshots_and_baseline_objects_are_sources"])
        self.assertEqual(payload["source_policy"]["classification_evidence_mode"], "analytic")
        self.assertEqual(
            {item["status"] for item in payload["normative_sources"]},
            {"Draft", "Accepted", "Canonical"},
        )
        self.assertEqual(payload["source_sweep"]["document_scope"]["document_count"], 25)
        self.assertEqual(
            payload["source_sweep"]["claim_boundary"]["proof_scope"],
            "declared-vocabulary-hit-completeness-only",
        )
        self.assertFalse(
            payload["source_sweep"]["claim_boundary"]["semantic_axis_completeness_claimed"]
        )
        self.assertEqual(len(payload["source_sweep"]["hits"]), 64)
        self.assertEqual(
            {item["disposition"] for item in payload["source_sweep"]["hits"]},
            {"classification-source", "considered-no-exclusion"},
        )
        self.assertEqual(
            sum(
                item["disposition"] == "classification-source"
                for item in payload["source_sweep"]["hits"]
            ),
            7,
        )
        self.assertEqual(
            sum(
                item["disposition"] == "considered-no-exclusion"
                for item in payload["source_sweep"]["hits"]
            ),
            57,
        )
        self.assertTrue(
            all(item["evidence_mode"] == "analytic" for item in payload["source_sweep"]["hits"])
        )
        self.assertEqual(len(payload["source_sweep"]["known_out_of_vocabulary"]), 3)
        self.assertTrue(
            all(
                item["evidence_mode"] == "analytic"
                for item in payload["source_sweep"]["known_out_of_vocabulary"]
            )
        )
        self.assertIn(
            "ASSIGNMENT_AMENDMENT_MODEL_OPEN",
            {item["statement_id"] for item in payload["normative_sources"]},
        )

    def test_rule_discriminates_real_norm_violations_and_invalid_inputs(self) -> None:
        whole = copy.deepcopy(self.fixtures["norm-q5-whole-resource.yaml"]["probe"])
        many_resources = copy.deepcopy(whole)
        many_resources["claims"]["resource_cardinality"] = "many"
        derived = derive_assignment_norm_compatibility(many_resources)
        self.assertEqual(derived.classification, "incompatible")
        self.assertEqual(
            set(derived.violation_statement_ids),
            {"ASSIGNMENT_EXACT_ONE_RESOURCE_OPERATION", "ASSIGNMENT_OWNS_IDENTITY_INTERVAL_LIFECYCLE"},
        )
        inherited = copy.deepcopy(whole)
        inherited["claims"]["automatic_component_inheritance"] = "true"
        derived = derive_assignment_norm_compatibility(inherited)
        self.assertEqual(derived.classification, "incompatible")
        self.assertEqual(derived.violation_statement_ids, ("COMPONENT_ASSIGNMENT_NON_INHERITANCE",))
        malformed = copy.deepcopy(whole)
        malformed["claims"]["unknown_axis"] = "value"
        self.assertIsNone(derive_assignment_norm_compatibility(malformed).classification)

    def test_each_fixture_validation_boundary_is_executable(self) -> None:
        base = copy.deepcopy(self.fixtures["norm-q5-whole-resource.yaml"])
        attacks = {}
        candidate = copy.deepcopy(base)
        del candidate["probe"]["probe_id"]
        attacks["ASSIGNMENT_NORM_FIXTURE_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        candidate["probe"]["resolution_id"] = "UNKNOWN_RESOLUTION"
        attacks["ASSIGNMENT_NORM_RESOLUTION_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        candidate["probe"]["claims"]["resource_cardinality"] = "many"
        attacks["ASSIGNMENT_NORM_CLAIM_INVALID"] = candidate
        candidate = copy.deepcopy(base)
        candidate["probe"]["stored_classification"] = "incompatible"
        attacks["ASSIGNMENT_NORM_RESULT_MISMATCH"] = candidate
        candidate = copy.deepcopy(base)
        candidate["probe"]["selected_resolution"] = True
        attacks["ASSIGNMENT_NORM_FORBIDDEN_OUTCOME"] = candidate
        self.assertEqual(set(attacks), set(ASSIGNMENT_NORM_ERROR_CODES))
        for error, candidate in attacks.items():
            with self.subTest(error=error):
                self.assertIn(error, validate_reference_fixture(candidate).errors)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        base = self.fixtures["norm-q5-whole-resource.yaml"]
        for value in sorted(assignment_norm_compatibility.PROBE_FIELDS):
            with self.subTest(attribute="PROBE_FIELDS", value=value), patch.object(
                assignment_norm_compatibility,
                "PROBE_FIELDS",
                assignment_norm_compatibility.PROBE_FIELDS - {value},
            ):
                self.assertFalse(validate_reference_fixture(base).valid)
        for value in sorted(assignment_norm_compatibility.FORBIDDEN_FIELDS):
            candidate = copy.deepcopy(base)
            candidate["probe"][value] = True
            self.assertIn("ASSIGNMENT_NORM_FORBIDDEN_OUTCOME", validate_reference_fixture(candidate).errors)
            with self.subTest(attribute="FORBIDDEN_FIELDS", value=value), patch.object(
                assignment_norm_compatibility,
                "FORBIDDEN_FIELDS",
                assignment_norm_compatibility.FORBIDDEN_FIELDS - {value},
            ):
                self.assertNotIn("ASSIGNMENT_NORM_FORBIDDEN_OUTCOME", validate_reference_fixture(candidate).errors)
        for value in sorted(assignment_norm_compatibility.FORBIDDEN_OUTCOMES):
            with self.subTest(attribute="FORBIDDEN_OUTCOMES", value=value), patch.object(
                assignment_norm_compatibility,
                "FORBIDDEN_OUTCOMES",
                assignment_norm_compatibility.FORBIDDEN_OUTCOMES - {value},
            ):
                self.assertFalse(validate_assignment_norm_compatibility(ROOT).valid)
        for value in sorted(assignment_norm_compatibility.CURRENT_DOCUMENT_STATUSES):
            with self.subTest(attribute="CURRENT_DOCUMENT_STATUSES", value=value), patch.object(
                assignment_norm_compatibility,
                "CURRENT_DOCUMENT_STATUSES",
                assignment_norm_compatibility.CURRENT_DOCUMENT_STATUSES - {value},
            ):
                self.assertFalse(validate_assignment_norm_compatibility(ROOT).valid)

        defensive_structures = (
            "BLOCKER_QUESTIONS", "SURVIVOR_CLAIMS", "SURVIVOR_BLOCKERS",
            "NORMATIVE_STATEMENTS", "AXIS_POLICIES", "SWEEP_DOCUMENT_STATUSES",
            "SWEEP_VOCABULARY", "EXPECTED_GATE_FIRST", "EXPECTED_CRITERION",
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
            original = getattr(assignment_norm_compatibility, attribute)
            for value_path in scalar_paths(original):
                with self.subTest(attribute=attribute, value_path=value_path), patch.object(
                    assignment_norm_compatibility,
                    attribute,
                    mutate_scalar(original, value_path),
                ):
                    self.assertFalse(validate_assignment_norm_compatibility(ROOT).valid)

        source_sweep = yaml.safe_load((ROOT / self.map_path).read_text(encoding="utf-8"))["source_sweep"]
        for value_path in scalar_paths(source_sweep):
            with self.subTest(attribute="source_sweep", value_path=value_path):
                self.assertFalse(
                    assignment_norm_compatibility._source_sweep_payload_valid(
                        mutate_scalar(source_sweep, value_path), ROOT
                    )
                )

        scalar_mutations = {
            "BASELINE": "MUTATED-BASELINE",
            "COMPATIBLE": "mutated-compatible",
            "INCOMPATIBLE": "mutated-incompatible",
            "UNDERDETERMINED": "mutated-underdetermined",
            "ANALYTIC": "observed",
            "SOURCE_SWEEP_SHA256": "mutated-source-sweep-digest",
        }
        for attribute, mutation in scalar_mutations.items():
            with self.subTest(attribute=attribute), patch.object(
                assignment_norm_compatibility, attribute, mutation
            ):
                self.assertFalse(validate_assignment_norm_compatibility(ROOT).valid)

    def test_live_source_survivor_probe_and_gate_mutations_fail_independently(self) -> None:
        cases = ("source", "source-sweep", "out-of-vocabulary", "survivor", "probe", "gate")
        expected_errors = {
            "source": ASSIGNMENT_NORM_SOURCE_DRIFT,
            "source-sweep": ASSIGNMENT_NORM_SOURCE_DRIFT,
            "out-of-vocabulary": ASSIGNMENT_NORM_SOURCE_DRIFT,
            "survivor": ASSIGNMENT_NORM_SURVIVOR_DRIFT,
            "probe": ASSIGNMENT_NORM_PROBE_DRIFT,
            "gate": ASSIGNMENT_NORM_GATE_DRIFT,
        }
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                if case == "source":
                    relative = Path("docs/023-resource-occupancy/README.md")
                    text = (root / relative).read_text(encoding="utf-8")
                    (root / relative).write_text(text.replace("Status: Accepted", "Status: Draft", 1), encoding="utf-8")
                elif case == "source-sweep":
                    relative = Path("docs/004-operation-concept/README.md")
                    text = (root / relative).read_text(encoding="utf-8")
                    (root / relative).write_text(
                        text + "\nAssignment may have multiple applicability intervals.\n",
                        encoding="utf-8",
                    )
                elif case == "out-of-vocabulary":
                    relative = Path("docs/004-operation-concept/README.md")
                    text = (root / relative).read_text(encoding="utf-8")
                    (root / relative).write_text(
                        text.replace(
                            "Остаточна модель часу буде визначена окремо.",
                            "Остаточну модель часу буде визначено окремо.",
                            1,
                        ),
                        encoding="utf-8",
                    )
                elif case == "survivor":
                    relative = Path("architecture/assignment-consumer-pressure.yaml")
                    payload = yaml.safe_load((root / relative).read_text(encoding="utf-8"))
                    payload["resolution_inventory"] = [
                        item for item in payload["resolution_inventory"]
                        if item["resolution_id"] != "SUPERSEDING_ASSIGNMENT_FOR_CHANGE"
                    ]
                    self.write_yaml(root, relative, payload)
                elif case == "probe":
                    relative = self.map_path
                    payload = yaml.safe_load((root / relative).read_text(encoding="utf-8"))
                    payload["survivor_results"][0]["classification"] = "compatible"
                    self.write_yaml(root, relative, payload)
                else:
                    relative = Path("architecture/foundation-promotion-gate.yaml")
                    payload = yaml.safe_load((root / relative).read_text(encoding="utf-8"))
                    payload["cycle_protocol"]["active_cycle_id"] = "SYNTH-CYCLE"
                    self.write_yaml(root, relative, payload)
                self.assertIn(expected_errors[case], validate_assignment_norm_compatibility(root).errors)

    def test_baseline_anchors_protected_bytes_safety_and_accounting(self) -> None:
        tree = subprocess.run(
            ["git", "rev-parse", f"{self.baseline}^{{tree}}"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout.strip()
        self.assertEqual(tree, "5bfc5e0d09f6c52f7576e2a5ea60630875eed224")
        for path, (blob, sha256, tokens) in self.baseline_anchors.items():
            with self.subTest(path=path):
                row = subprocess.run(
                    ["git", "ls-tree", "-r", self.baseline, "--", path],
                    cwd=ROOT, check=True, capture_output=True, text=True,
                ).stdout.strip()
                self.assertEqual(row.split()[2], blob)
                self.assertEqual(row.split(maxsplit=3)[3], path)
                baseline_bytes = subprocess.run(
                    ["git", "cat-file", "blob", blob], cwd=ROOT, check=True, capture_output=True,
                ).stdout
                self.assertEqual(hashlib.sha256(baseline_bytes).hexdigest(), sha256)
                self.assertEqual((ROOT / path).read_bytes(), baseline_bytes)
                text = baseline_bytes.decode("utf-8")
                self.assertTrue(all(token in text for token in tokens))
        fixture_text = "\n".join(
            (CHECKER_ROOT / "fixtures/assignment_norm_compatibility" / name).read_text(encoding="utf-8")
            for name in self.fixtures
        )
        for forbidden in ("latitude", "longitude", "unit_name", "person_name", "password", "secret", "token:"):
            self.assertNotIn(forbidden, fixture_text.lower())
