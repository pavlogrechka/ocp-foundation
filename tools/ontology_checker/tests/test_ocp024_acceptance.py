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

from ocp_checker import ocp024_acceptance  # noqa: E402
from ocp_checker.completeness_evaluator import (  # noqa: E402
    ACTIVATION_FIELDS,
    INDETERMINATE,
    derive_completeness_evidence_recognition,
    validate_completeness_evaluator_dataset,
)
from ocp_checker.ocp024_acceptance import (  # noqa: E402
    OCP024_ACCEPTANCE_CONSUMER_NEED_DRIFT,
    OCP024_ACCEPTANCE_RUNTIME_BOUNDARY_DRIFT,
    OCP024_ACCEPTANCE_SNAPSHOT_DRIFT,
    OCP024_ACCEPTANCE_STATUS_DRIFT,
    validate_ocp024_acceptance,
)
from ocp_checker.resource_occupancy import derive_resource_occupancy  # noqa: E402
from ocp_checker.checker import load_fixture  # noqa: E402


class Ocp024AcceptanceTests(unittest.TestCase):
    copied_paths = (
        Path("architecture"), Path("docs"),
        Path("tools/ontology_checker/fixtures/completeness_evaluator"),
        Path("tools/ontology_checker/fixtures/resource_occupancy/valid-zero-assignments.yaml"),
        Path("tools/ontology_checker/ocp_checker/completeness_evaluator.py"),
        Path("tools/ontology_checker/completeness-evaluator-rules.yaml"),
        Path("tools/ontology_checker/tests/test_completeness_evaluator.py"),
    )

    def copy_inputs(self, destination: Path) -> None:
        for relative in self.copied_paths:
            source, target = ROOT / relative, destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copyfile(source, target)

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / ocp024_acceptance.MAP_PATH).read_text(encoding="utf-8"))

    def test_repository_ocp024_acceptance_is_valid(self) -> None:
        self.assertTrue(validate_ocp024_acceptance(ROOT).valid)

    def test_gate_readiness_versioning_and_nonimplications_are_exact(self) -> None:
        payload = self.payload()
        self.assertFalse(payload["gate_first"]["ocp016_g4_applies"])
        self.assertFalse(payload["gate_first"]["changes_other_document_g4_answer"])
        self.assertTrue(payload["readiness_criterion"]["declared_before_application"])
        self.assertEqual(payload["readiness_criterion"]["result"], "satisfied")
        self.assertEqual(len(payload["readiness_criterion"]["conditions"]), 7)
        self.assertIn("0.1.0-to-0.2.0", payload["versioning"]["OCP-024"])
        self.assertEqual(payload["migration"]["runtime_behavior"], "unchanged")

    def test_reviewed_body_full_chain_and_standard_snapshot_binding_are_exact(self) -> None:
        payload = self.payload()
        snapshot = payload["reviewed_snapshot"]
        tree = subprocess.check_output(
            ["git", "ls-tree", "-r", payload["baseline"]], cwd=ROOT, text=True
        ).splitlines()
        matches = [line for line in tree if line.split()[2] == snapshot["baseline_blob"]]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].split("\t", 1)[1], "docs/024-completeness-evaluator/README.md")
        baseline_bytes = subprocess.check_output(
            ["git", "show", f"{payload['baseline']}:docs/024-completeness-evaluator/README.md"], cwd=ROOT
        )
        current_bytes = (ROOT / snapshot["path"]).read_bytes()
        self.assertEqual(current_bytes, baseline_bytes)
        self.assertEqual(hashlib.sha256(current_bytes).hexdigest(), snapshot["sha256"])

    def test_production_shaped_evaluator_and_authority_never_gain_recognition(self) -> None:
        dataset = load_fixture(ROOT / ocp024_acceptance.VALID_FIXTURE)["dataset"]
        for field, value in (("evaluator_ref", "PRODUCTION-EVALUATOR-001"), ("authority_basis_ref", "PRODUCTION-AUTHORITY-001")):
            with self.subTest(field=field):
                mutated = copy.deepcopy(dataset)
                mutated["evaluator_profiles"][0][field] = value
                self.assertEqual(derive_completeness_evidence_recognition(mutated).result, INDETERMINATE)
                self.assertFalse(validate_completeness_evaluator_dataset(mutated).valid)

    def test_every_activation_field_is_rejected_and_indeterminate(self) -> None:
        dataset = load_fixture(ROOT / ocp024_acceptance.VALID_FIXTURE)["dataset"]
        for field in ACTIVATION_FIELDS:
            with self.subTest(field=field):
                mutated = copy.deepcopy(dataset)
                mutated["recognition_request"][field] = "synthetic-disabled"
                self.assertEqual(derive_completeness_evidence_recognition(mutated).result, INDETERMINATE)
                self.assertFalse(validate_completeness_evaluator_dataset(mutated).valid)

    def test_ocp023_negative_result_remains_unavailable_without_completeness(self) -> None:
        dataset = load_fixture(ROOT / ocp024_acceptance.ZERO_OCCUPANCY_FIXTURE)["dataset"]
        self.assertFalse(derive_resource_occupancy(dataset).occupied)
        dataset["assignment_snapshots"][0]["completeness_evidence_ref"] = None
        self.assertIsNone(derive_resource_occupancy(dataset).occupied)

    def test_each_other_document_status_change_and_consumer_need_change_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            for path in sorted((root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
                metadata = ocp024_acceptance._frontmatter(path)
                if metadata and metadata.get("Document-ID") != "OCP-024":
                    with self.subTest(document=metadata.get("Document-ID")):
                        target = (
                            root / "docs/006-constraint-concept/reviewed-contract-v0.3.2.md"
                            if metadata.get("Document-ID") == "OCP-006" else path
                        )
                        target_metadata = ocp024_acceptance._frontmatter(target)
                        original = target.read_text(encoding="utf-8")
                        old = f"Status: {target_metadata['Status']}"
                        new = "Status: Draft" if target_metadata["Status"] != "Draft" else "Status: Accepted"
                        target.write_text(original.replace(old, new, 1), encoding="utf-8")
                        self.assertIn(OCP024_ACCEPTANCE_STATUS_DRIFT, validate_ocp024_acceptance(root).errors)
                        target.write_text(original, encoding="utf-8")
            need_path = root / ocp024_acceptance.NEED_MAP_PATH
            need = yaml.safe_load(need_path.read_text(encoding="utf-8"))
            need["current_result"]["unmet_positive_needs"] = []
            need_path.write_text(yaml.safe_dump(need, sort_keys=False), encoding="utf-8")
            self.assertIn(OCP024_ACCEPTANCE_CONSUMER_NEED_DRIFT, validate_ocp024_acceptance(root).errors)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        for attribute in ("EXPECTED_MAP_KEYS", "FORBIDDEN_OUTCOMES", "ACCEPTED_CONSUMERS"):
            values = getattr(ocp024_acceptance, attribute)
            for value in sorted(values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    ocp024_acceptance, attribute, values - {value}
                ):
                    self.assertFalse(validate_ocp024_acceptance(ROOT).valid)
        for attribute in ("BASELINE", "MAP_SHA256", "SNAPSHOT_SHA256", "SNAPSHOT_BLOB"):
            with self.subTest(attribute=attribute), patch.object(ocp024_acceptance, attribute, "mutated"):
                self.assertFalse(validate_ocp024_acceptance(ROOT).valid)
        for field in sorted(ACTIVATION_FIELDS):
            with self.subTest(activation_field=field), patch.object(
                ocp024_acceptance, "ACTIVATION_FIELDS", ACTIVATION_FIELDS - {field}
            ):
                self.assertFalse(validate_ocp024_acceptance(ROOT).valid)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            snapshot = root / ocp024_acceptance.SNAPSHOT_PATH
            snapshot.write_text(snapshot.read_text(encoding="utf-8") + "\nmutation\n", encoding="utf-8")
            self.assertIn(OCP024_ACCEPTANCE_SNAPSHOT_DRIFT, validate_ocp024_acceptance(root).errors)
        for item in self.payload()["protected_artifacts"]:
            with self.subTest(protected=item["path"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                original = Path(item["path"])
                resolved = ocp024_acceptance.historical_path(root, original, item["sha256"])
                path = root / resolved
                path.write_bytes(path.read_bytes() + b"\nmutation\n")
                self.assertFalse(validate_ocp024_acceptance(root).valid)

        payload = self.payload()

        def scalar_paths(value, prefix=()):
            if isinstance(value, dict):
                for key, child in value.items():
                    yield from scalar_paths(child, prefix + (key,))
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    yield from scalar_paths(child, prefix + (index,))
            else:
                yield prefix

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            for value_path in scalar_paths(payload):
                with self.subTest(witness_scalar=value_path):
                    mutated = copy.deepcopy(payload)
                    parent = mutated
                    for part in value_path[:-1]:
                        parent = parent[part]
                    old = parent[value_path[-1]]
                    parent[value_path[-1]] = not old if isinstance(old, bool) else f"{old}-mutated"
                    (root / ocp024_acceptance.MAP_PATH).write_text(
                        yaml.safe_dump(mutated, sort_keys=False, allow_unicode=True), encoding="utf-8"
                    )
                    self.assertFalse(validate_ocp024_acceptance(root).valid)


if __name__ == "__main__":
    unittest.main()
