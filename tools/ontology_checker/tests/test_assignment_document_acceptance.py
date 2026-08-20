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

from ocp_checker import assignment_document_acceptance as acceptance  # noqa: E402
from ocp_checker.assignment_document_acceptance import (  # noqa: E402
    ASSIGNMENT_ACCEPTANCE_ATOMICITY_DRIFT,
    ASSIGNMENT_ACCEPTANCE_CONSUMER_DRIFT,
    ASSIGNMENT_ACCEPTANCE_CRITERION_DRIFT,
    ASSIGNMENT_ACCEPTANCE_NEED_DRIFT,
    ASSIGNMENT_ACCEPTANCE_NON_IMPLICATION_DRIFT,
    ASSIGNMENT_ACCEPTANCE_SNAPSHOT_DRIFT,
    ASSIGNMENT_ACCEPTANCE_SUBJECT_DRIFT,
    validate_assignment_document_acceptance,
)
from ocp_checker.assignment_amendment_q2 import validate_assignment_amendment_q2  # noqa: E402
from ocp_checker.assignment_consumer_compatibility import validate_assignment_consumer_compatibility  # noqa: E402
from ocp_checker.assignment_stable_surface import validate_assignment_stable_surface  # noqa: E402
from ocp_checker.assignment_temporal_scope import validate_assignment_temporal_scope  # noqa: E402
from ocp_checker.constraint_document_acceptance import validate_constraint_document_acceptance  # noqa: E402
from ocp_checker.constraint_document_status_readiness import validate_constraint_document_status_readiness  # noqa: E402
from ocp_checker.consumer_need_discovery import validate_consumer_need_discovery  # noqa: E402
from ocp_checker.ocp024_acceptance import validate_ocp024_acceptance  # noqa: E402


class AssignmentDocumentAcceptanceTests(unittest.TestCase):
    map_path = acceptance.MAP_PATH

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        paths = {
            self.map_path, acceptance.SNAPSHOT_MAP_PATH, acceptance.GATE_PATH,
            acceptance.NEED_PATH, acceptance.SNAPSHOT_PATH,
        }
        paths.update(Path(row["preserved_path"]) for row in self.payload()["historical_evidence_successions"])
        for source in (ROOT / "docs").glob("[0-9][0-9][0-9]-*/README.md"):
            paths.add(source.relative_to(ROOT))
        for relative in paths:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def test_repository_assignment_document_acceptance_is_valid(self) -> None:
        result = validate_assignment_document_acceptance(ROOT)
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
                    self.assertIn(ASSIGNMENT_ACCEPTANCE_CRITERION_DRIFT, validate_assignment_document_acceptance(root).errors)

    def test_route_f_gate_first_and_difference_inventory_are_explicit(self) -> None:
        payload = self.payload()
        self.assertEqual(payload["route_decision"]["selected"], "Route-F")
        self.assertTrue(payload["route_decision"]["precedent_guide_is_not_route_proof"])
        self.assertEqual(set(payload["route_decision"]["rejected_routes"]), {"Route-C", "Route-E", "Route-D", "Route-I"})
        self.assertFalse(payload["gate_first"]["positive_capable"])
        self.assertFalse(payload["gate_first"]["ocp016_g4_applies"])
        self.assertFalse(payload["gate_first"]["activation_performed"])
        differences = payload["differences_from_previously_accepted_subject"]["differences"]
        self.assertEqual({row["axis"] for row in differences}, {
            "direct-dependencies", "accepted-consumers", "whole-freeze-surfaces",
            "unmet-positive-consumer-need", "direct-dependent-previous-subject",
        })

    def test_baseline_anchors_are_full_chain_and_predecessors_are_exact(self) -> None:
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
        for row in payload["historical_evidence_successions"]:
            with self.subTest(path=row["preserved_path"]):
                self.assertEqual(hashlib.sha256((ROOT / row["preserved_path"]).read_bytes()).hexdigest(), row["sha256"])

    def test_seven_consumers_are_individually_bound_and_need_remains_unmet(self) -> None:
        payload = self.payload()
        self.assertEqual({row["document_id"] for row in payload["consumers"]}, acceptance.CONSUMERS)
        for row in payload["consumers"]:
            with self.subTest(document_id=row["document_id"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / row["path"]
                path.write_text(path.read_text(encoding="utf-8").replace(row["token"], "MUTATED-CONSUMER", 1), encoding="utf-8")
                self.assertIn(ASSIGNMENT_ACCEPTANCE_CONSUMER_DRIFT, validate_assignment_document_acceptance(root).errors)
        need = payload["unmet_positive_need"]
        self.assertEqual((need["before"], need["after"], need["blocked_output"]), ("unmet", "unmet", "occupied-false"))
        self.assertFalse(any(need[key] for key in (
            "acceptance_supplies_completeness", "acceptance_names_legitimate_evaluator",
            "acceptance_activates_positive_model",
        )))

    def test_snapshot_loss_substitution_and_atomic_status_version_changes_fail(self) -> None:
        for relative, old, new, expected in (
            (acceptance.SNAPSHOT_PATH, "Document-ID: OCP-005", "Document-ID: MUTATED", ASSIGNMENT_ACCEPTANCE_SNAPSHOT_DRIFT),
            (acceptance.SUBJECT_PATH, "Status: Accepted", "Status: Draft", ASSIGNMENT_ACCEPTANCE_SUBJECT_DRIFT),
            (acceptance.SUBJECT_PATH, "Version: 0.4.0", "Version: 0.3.0", ASSIGNMENT_ACCEPTANCE_SUBJECT_DRIFT),
            (acceptance.SUBJECT_PATH, "Version: 0.4.0", "Version: 0.4.1", ASSIGNMENT_ACCEPTANCE_SUBJECT_DRIFT),
        ):
            with self.subTest(path=relative, old=old), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / relative
                path.write_text(path.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8")
                self.assertIn(expected, validate_assignment_document_acceptance(root).errors)

    def test_each_non_implication_is_individually_mutation_live(self) -> None:
        payload = self.payload()
        self.assertEqual(frozenset(payload["non_implications"]), acceptance.NON_IMPLICATIONS)
        original_load = acceptance._load
        for index, value in enumerate(payload["non_implications"]):
            changed = copy.deepcopy(payload)
            changed["non_implications"][index] = f"MUTATED-{value}"

            def changed_load(path: Path):
                return changed if path == ROOT / self.map_path else original_load(path)

            with self.subTest(non_implication=value), patch.object(acceptance, "_load", side_effect=changed_load):
                self.assertIn(ASSIGNMENT_ACCEPTANCE_NON_IMPLICATION_DRIFT, validate_assignment_document_acceptance(ROOT).errors)

    def test_all_live_status_scanners_reject_the_pre_transition_value(self) -> None:
        validators = (
            validate_assignment_stable_surface,
            validate_assignment_amendment_q2,
            validate_assignment_temporal_scope,
            validate_assignment_consumer_compatibility,
            validate_consumer_need_discovery,
            validate_constraint_document_status_readiness,
            validate_constraint_document_acceptance,
            validate_ocp024_acceptance,
        )
        for validator in validators:
            with self.subTest(scanner=validator.__name__):
                self.assertTrue(validator(ROOT).valid, validator(ROOT).errors)
        payload = self.payload()
        self.assertEqual(payload["current_projection_sync"]["expected"]["primary_document_status_counts"], {"Canonical": 10, "Accepted": 15, "Draft": 0})

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
        original_load = acceptance._load
        baseline_cache = {}
        for item in payload["baseline_evidence_objects"]:
            raw = subprocess.check_output(["git", "cat-file", "blob", item["blob"]], cwd=ROOT)
            baseline_cache[item["path"]] = (item["blob"], raw)
        for value_path in scalar_paths(payload):
            changed = mutate(payload, value_path)

            def changed_load(path: Path):
                return changed if path == ROOT / self.map_path else original_load(path)

            with self.subTest(value_path=value_path), patch.object(acceptance, "_load", side_effect=changed_load), patch.object(
                acceptance, "_baseline_blob", side_effect=lambda _root, _baseline, path: baseline_cache.get(path)
            ):
                self.assertFalse(validate_assignment_document_acceptance(ROOT).valid)


if __name__ == "__main__":
    unittest.main()
