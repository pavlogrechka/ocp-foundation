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

from ocp_checker import assignment_consumer_compatibility  # noqa: E402
from ocp_checker.assignment_consumer_compatibility import (  # noqa: E402
    ASSIGNMENT_CONSUMER_COMPATIBILITY_GATE_DRIFT,
    ASSIGNMENT_CONSUMER_COMPATIBILITY_INVENTORY_DRIFT,
    ASSIGNMENT_CONSUMER_COMPATIBILITY_PROBE_DRIFT,
    ASSIGNMENT_CONSUMER_COMPATIBILITY_PROJECTION_DRIFT,
    ASSIGNMENT_CONSUMER_COMPATIBILITY_TEXT_DRIFT,
    EXPECTED_ANCHORS,
    EXPECTED_CONSUMERS,
    validate_assignment_consumer_compatibility,
)


class AssignmentConsumerCompatibilityTests(unittest.TestCase):
    map_path = Path("architecture/assignment-consumer-compatibility.yaml")
    surface_path = Path("architecture/assignment-stable-surface.yaml")
    gate_path = Path("architecture/foundation-promotion-gate.yaml")

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "docs", destination / "docs")
        for relative in (self.map_path, self.surface_path, self.gate_path):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)
        for consumer in EXPECTED_CONSUMERS.values():
            relative = Path(consumer["fixture"])
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    def test_repository_assignment_consumer_compatibility_is_valid(self) -> None:
        self.assertTrue(validate_assignment_consumer_compatibility(ROOT).valid)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        sets = (
            "MAP_KEYS", "CONSUMER_IDS", "NEGATIVE_CONSUMER_IDS", "POSITIVE_CONSUMER_IDS",
            "STABLE_SURFACE_IDS", "MOVING_SURFACE_IDS", "REMAINING_BLOCKER_IDS",
            "FORBIDDEN_OUTCOMES",
        )
        for attribute in sets:
            production = getattr(assignment_consumer_compatibility, attribute)
            for value in sorted(production):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    assignment_consumer_compatibility, attribute, production - {value}
                ):
                    self.assertFalse(validate_assignment_consumer_compatibility(ROOT).valid)

        dictionaries = (
            "EXPECTED_IDENTITY", "EXPECTED_GATE_FIRST", "EXPECTED_SUBJECT", "EXPECTED_CRITERION",
            "EXPECTED_CONSUMERS", "EXPECTED_PROJECTION", "EXPECTED_GATE_GUARD", "EXPECTED_ANCHORS",
        )

        def scalar_paths(value, prefix=()):
            if isinstance(value, dict):
                for key, child in value.items():
                    yield from scalar_paths(child, prefix + (key,))
            elif isinstance(value, (tuple, list)):
                for index, child in enumerate(value):
                    yield from scalar_paths(child, prefix + (index,))
            else:
                yield prefix

        def mutate(value, path):
            if not path:
                if isinstance(value, bool):
                    return not value
                if isinstance(value, int):
                    return value + 100
                if value is None:
                    return "MUTATED"
                return f"MUTATED-{value}"
            key = path[0]
            child = mutate(value[key], path[1:])
            if isinstance(value, tuple):
                rebuilt = list(value)
                rebuilt[key] = child
                return tuple(rebuilt)
            result = copy.deepcopy(value)
            result[key] = child
            return result

        for attribute in dictionaries:
            production = getattr(assignment_consumer_compatibility, attribute)
            for value_path in scalar_paths(production):
                with self.subTest(attribute=attribute, value_path=value_path), patch.object(
                    assignment_consumer_compatibility, attribute, mutate(production, value_path)
                ):
                    self.assertFalse(validate_assignment_consumer_compatibility(ROOT).valid)

    def test_all_five_accepted_consumers_and_each_consumed_token_are_live(self) -> None:
        for consumer_id, consumer in EXPECTED_CONSUMERS.items():
            for mutation in ("status", "dependency", *consumer["consumed_tokens"]):
                with self.subTest(consumer=consumer_id, mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    path = root / consumer["primary"]
                    text = path.read_text(encoding="utf-8")
                    if mutation == "status":
                        text = text.replace("Status: Accepted", "Status: Draft", 1)
                        expected = ASSIGNMENT_CONSUMER_COMPATIBILITY_INVENTORY_DRIFT
                    elif mutation == "dependency":
                        text = text.replace("OCP-005", "OCP-005-MUTATED", 1)
                        expected = ASSIGNMENT_CONSUMER_COMPATIBILITY_INVENTORY_DRIFT
                    else:
                        text = text.replace(mutation, "MUTATED-CONSUMED-TOKEN", 1)
                        expected = ASSIGNMENT_CONSUMER_COMPATIBILITY_TEXT_DRIFT
                    path.write_text(text, encoding="utf-8")
                    self.assertIn(expected, validate_assignment_consumer_compatibility(root).errors)

    def test_each_predeclared_real_fixture_probe_is_replayed(self) -> None:
        for consumer_id, consumer in EXPECTED_CONSUMERS.items():
            with self.subTest(consumer=consumer_id):
                observed = assignment_consumer_compatibility._probe(ROOT, consumer_id, consumer)
                self.assertEqual(observed, (consumer["expected_control"], consumer["expected_probe"]))

    def test_probe_mutations_cannot_silently_change_a_consumer_result(self) -> None:
        mutations = {
            "OCP-013": ("assignment_mutation", "assignment_mutation_removed"),
            "OCP-015": ("all_invited_responders_confirm", "missing_response_fails_safe"),
            "OCP-017": ("remains_effective_independently", "not_effective_at_transition"),
            "OCP-020": ("role: demand", "role: capacity_limit"),
            "OCP-021": ("assignment_mutation", "assignment_mutation_removed"),
        }
        for consumer_id, (old, new) in mutations.items():
            with self.subTest(consumer=consumer_id), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                fixture = root / EXPECTED_CONSUMERS[consumer_id]["fixture"]
                text = fixture.read_text(encoding="utf-8")
                self.assertIn(old, text)
                fixture.write_text(text.replace(old, new, 1), encoding="utf-8")
                self.assertIn(
                    ASSIGNMENT_CONSUMER_COMPATIBILITY_PROBE_DRIFT,
                    validate_assignment_consumer_compatibility(root).errors,
                )

    def test_removed_blocker_and_five_consumer_projection_are_enforced(self) -> None:
        mutations = ("restore-blocker", "remove-consumer", "remove-stable-surface")
        for mutation in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                surface = yaml.safe_load((root / self.surface_path).read_text(encoding="utf-8"))
                if mutation == "restore-blocker":
                    surface["blockers"].append({
                        "blocker_id": "ACCEPTED_CONSUMER_COMPATIBILITY_UNPROVEN",
                        "disposition": "blocks-promotion-not-discovery",
                        "consumer_ids": ["OCP-013", "OCP-015", "OCP-017", "OCP-020", "OCP-021"],
                    })
                elif mutation == "remove-consumer":
                    surface["direct_consumers"] = [
                        item for item in surface["direct_consumers"] if item["document_id"] != "OCP-021"
                    ]
                else:
                    surface["stable_candidates"] = surface["stable_candidates"][1:]
                self.write_yaml(root, self.surface_path, surface)
                self.assertIn(
                    ASSIGNMENT_CONSUMER_COMPATIBILITY_PROJECTION_DRIFT,
                    validate_assignment_consumer_compatibility(root).errors,
                )

    def test_promotion_gate_remains_completed_event_with_no_active_cycle(self) -> None:
        for mutation in ("activate", "remove-event", "downgrade-schema"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                gate = yaml.safe_load((root / self.gate_path).read_text(encoding="utf-8"))
                if mutation == "activate":
                    gate["cycle_protocol"]["active_cycle_id"] = "ASSIGNMENT_T7"
                elif mutation == "remove-event":
                    gate["cycles"] = []
                else:
                    gate["schema_version"] = 4
                self.write_yaml(root, self.gate_path, gate)
                self.assertIn(
                    ASSIGNMENT_CONSUMER_COMPATIBILITY_GATE_DRIFT,
                    validate_assignment_consumer_compatibility(root).errors,
                )

    def test_baseline_anchors_reverse_resolve_and_hash_full_chain(self) -> None:
        baseline = "747d5aa2e71bd87c4e024d62f80d8cfa122d8279"
        tree = subprocess.run(
            ["git", "ls-tree", "-r", baseline], cwd=ROOT, check=True, capture_output=True, text=True
        ).stdout.splitlines()
        by_blob: dict[str, list[str]] = {}
        for line in tree:
            metadata, path = line.split("\t", 1)
            blob = metadata.split()[2]
            by_blob.setdefault(blob, []).append(path)
        for path, (blob, expected_sha) in EXPECTED_ANCHORS.items():
            with self.subTest(path=path):
                self.assertIn(path, by_blob.get(blob, []))
                raw = subprocess.run(
                    ["git", "show", f"{baseline}:{path}"], cwd=ROOT, check=True, capture_output=True
                ).stdout
                self.assertEqual(hashlib.sha256(raw).hexdigest(), expected_sha)


if __name__ == "__main__":
    unittest.main()
