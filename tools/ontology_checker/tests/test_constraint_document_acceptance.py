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

from ocp_checker import constraint_document_acceptance as acceptance  # noqa: E402
from ocp_checker.constraint_document_acceptance import (  # noqa: E402
    CONSTRAINT_ACCEPTANCE_ATOMICITY_DRIFT,
    CONSTRAINT_ACCEPTANCE_CRITERION_DRIFT,
    CONSTRAINT_ACCEPTANCE_NON_IMPLICATION_DRIFT,
    CONSTRAINT_ACCEPTANCE_SUBJECT_DRIFT,
    validate_constraint_document_acceptance,
)


class ConstraintDocumentAcceptanceTests(unittest.TestCase):
    map_path = acceptance.MAP_PATH

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        paths = {
            self.map_path, acceptance.SNAPSHOT_MAP_PATH, acceptance.GATE_PATH,
            acceptance.SNAPSHOT_PATH,
            Path("architecture/baselines/foundation-promotion-gate-pre-ocp006-acceptance.yaml"),
            Path("architecture/baselines/foundation-map.md"),
            Path("architecture/baselines/assignment-stable-surface-pre-ocp006-acceptance.yaml"),
            Path("architecture/baselines/assignment-consumer-compatibility-pre-ocp006-acceptance.yaml"),
            Path("architecture/baselines/assignment-amendment-q2-attempt-pre-ocp006-acceptance.yaml"),
            Path("architecture/baselines/constraint-document-status-readiness-pre-ocp006-acceptance.yaml"),
            Path("architecture/assignment-stable-surface.yaml"),
            Path("architecture/assignment-consumer-compatibility.yaml"),
            Path("architecture/assignment-amendment-q2-attempt.yaml"),
            Path("architecture/ocp024-acceptance.yaml"),
            Path("architecture/discovery/AD-052-constraint-document-status-readiness.md"),
            Path("architecture/constraint-document-status-readiness.yaml"),
        }
        for source in (ROOT / "docs").glob("[0-9][0-9][0-9]-*/README.md"):
            paths.add(source.relative_to(ROOT))
        for relative in paths:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def write_payload(self, root: Path, payload: dict) -> None:
        (root / self.map_path).write_text(
            yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8"
        )

    def test_repository_constraint_document_acceptance_is_valid(self) -> None:
        result = validate_constraint_document_acceptance(ROOT)
        self.assertTrue(result.valid, result.errors)

    def test_each_ad052_criterion_has_its_own_live_basis_and_applicability(self) -> None:
        payload = self.payload()
        observed = {
            row["criterion_id"]: (row["applicability"], row["result"], row["basis_mode"])
            for row in payload["criteria"]
        }
        self.assertEqual(observed, acceptance.CRITERIA)
        self.assertEqual(
            {key for key, value in observed.items() if value[0] == "not-applicable-Canonical-only"},
            {"CANONICAL_STABILITY_CHECKS_AND_BOARD_ACT", "CANONICAL_DIRECT_DEPENDENCY_FLOOR_L2"},
        )
        for row in payload["criteria"]:
            for token in row["tokens"]:
                with self.subTest(criterion=row["criterion_id"], token=token), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    path = root / row["source"]
                    path.write_text(path.read_text(encoding="utf-8").replace(token, "MUTATED-BASIS", 1), encoding="utf-8")
                    self.assertIn(
                        CONSTRAINT_ACCEPTANCE_CRITERION_DRIFT,
                        validate_constraint_document_acceptance(root).errors,
                    )

    def test_route_f_and_gate_first_are_derived_without_precedent_reclassification(self) -> None:
        payload = self.payload()
        self.assertEqual(payload["route_decision"]["selected"], "Route-F")
        self.assertTrue(payload["route_decision"]["precedent_guide_is_not_route_proof"])
        self.assertEqual(set(payload["route_decision"]["rejected_routes"]), {"Route-C", "Route-E", "Route-D", "Route-I"})
        self.assertFalse(payload["gate_first"]["positive_capable"])
        self.assertFalse(payload["gate_first"]["ocp016_g4_applies"])
        self.assertFalse(payload["gate_first"]["activation_performed"])

    def test_baseline_anchors_are_full_chain_and_preserved_paths_are_exact(self) -> None:
        payload = self.payload()
        tree = subprocess.check_output(["git", "ls-tree", "-r", payload["baseline"]], cwd=ROOT, text=True).splitlines()
        reverse: dict[str, list[str]] = {}
        for line in tree:
            metadata, path = line.split("\t", 1)
            reverse.setdefault(metadata.split()[2], []).append(path)
        snapshot = payload["reviewed_snapshot"]
        self.assertIn(acceptance.SUBJECT_PATH.as_posix(), reverse.get(snapshot["baseline_blob"], []))
        raw = subprocess.check_output(["git", "cat-file", "blob", snapshot["baseline_blob"]], cwd=ROOT)
        self.assertEqual(hashlib.sha256(raw).hexdigest(), snapshot["sha256"])
        self.assertEqual(hashlib.sha256((ROOT / snapshot["path"]).read_bytes()).hexdigest(), snapshot["sha256"])
        for item in payload["baseline_evidence_objects"]:
            with self.subTest(path=item["path"]):
                self.assertIn(item["path"], reverse.get(item["blob"], []))
                baseline_raw = subprocess.check_output(["git", "cat-file", "blob", item["blob"]], cwd=ROOT)
                self.assertEqual(hashlib.sha256(baseline_raw).hexdigest(), item["sha256"])
                baseline_text = baseline_raw.decode("utf-8")
                self.assertTrue(all(token in baseline_text for token in item["state_tokens"]))
        for row in payload["historical_evidence_successions"]:
            with self.subTest(path=row["preserved_path"]):
                self.assertEqual(hashlib.sha256((ROOT / row["preserved_path"]).read_bytes()).hexdigest(), row["sha256"])

    def test_nine_accepted_consumers_are_individually_bound_and_unchanged(self) -> None:
        payload = self.payload()
        self.assertEqual({row["document_id"] for row in payload["consumers"]}, acceptance.CONSUMERS)
        self.assertEqual(len(payload["consumers"]), 9)
        for row in payload["consumers"]:
            with self.subTest(document_id=row["document_id"]):
                text = (ROOT / row["path"]).read_text(encoding="utf-8")
                self.assertIn(row["token"], text)
                self.assertEqual(row["acceptance_change"], "lifecycle-assurance-only")

    def test_status_or_version_change_without_the_atomic_package_fails(self) -> None:
        for old, new in (("Version: 0.4.0", "Version: 0.4.1"), ("Status: Accepted", "Status: Draft")):
            with self.subTest(field=old), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / acceptance.SUBJECT_PATH
                path.write_text(path.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8")
                errors = validate_constraint_document_acceptance(root).errors
                self.assertTrue(
                    CONSTRAINT_ACCEPTANCE_SUBJECT_DRIFT in errors
                    or CONSTRAINT_ACCEPTANCE_ATOMICITY_DRIFT in errors
                )

    def test_each_non_implication_is_individually_mutation_live(self) -> None:
        payload = self.payload()
        self.assertEqual(frozenset(payload["non_implications"]), acceptance.NON_IMPLICATIONS)
        original_load = acceptance._load
        for index, value in enumerate(payload["non_implications"]):
            changed = copy.deepcopy(payload)
            changed["non_implications"][index] = f"MUTATED-{value}"

            def changed_load(path: Path):
                return changed if path == ROOT / self.map_path else original_load(path)

            with self.subTest(non_implication=value), patch.object(acceptance, "_load", side_effect=changed_load), patch.object(acceptance, "MAP_SHA256", acceptance.MAP_SHA256):
                self.assertIn(
                    CONSTRAINT_ACCEPTANCE_NON_IMPLICATION_DRIFT,
                    validate_constraint_document_acceptance(ROOT).errors,
                )

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

        def mutate(value, path):
            if not path:
                if isinstance(value, bool):
                    return not value
                if isinstance(value, int):
                    return value + 1
                if value is None:
                    return "MUTATED-null"
                return f"MUTATED-{value}"
            rebuilt = copy.deepcopy(value)
            part = path[0]
            rebuilt[part] = mutate(value[part], path[1:])
            return rebuilt

        payload = self.payload()
        original_load = acceptance._load
        for value_path in scalar_paths(payload):
            changed = mutate(payload, value_path)

            def changed_load(path: Path):
                return changed if path == ROOT / self.map_path else original_load(path)

            with self.subTest(value_path=value_path), patch.object(acceptance, "_load", side_effect=changed_load):
                self.assertFalse(validate_constraint_document_acceptance(ROOT).valid)


if __name__ == "__main__":
    unittest.main()
