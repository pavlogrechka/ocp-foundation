from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import assignment_promotion_selection as selection  # noqa: E402
from ocp_checker.assignment_promotion_selection import (  # noqa: E402
    ASSIGNMENT_SELECTION_BOUNDARY_DRIFT,
    ASSIGNMENT_SELECTION_CANDIDATE_DRIFT,
    ASSIGNMENT_SELECTION_CLOSABILITY_DRIFT,
    ASSIGNMENT_SELECTION_GATE_DRIFT,
    ASSIGNMENT_SELECTION_HISTORICAL_DRIFT,
    ASSIGNMENT_SELECTION_PROJECTION_DRIFT,
    validate_assignment_promotion_selection,
)


class AssignmentPromotionSelectionTests(unittest.TestCase):
    def payload(self) -> dict:
        return yaml.safe_load((ROOT / selection.MAP_PATH).read_text(encoding="utf-8"))

    def with_changed_map(self, changed: dict):
        original_load = selection._load

        def changed_load(path: Path):
            return changed if path == ROOT / selection.MAP_PATH else original_load(path)

        digest = hashlib.sha256(
            yaml.safe_dump(changed, sort_keys=True, allow_unicode=True).encode()
        ).hexdigest()
        return patch.object(selection, "_load", side_effect=changed_load), patch.object(
            selection, "MAP_SHA256", digest
        )

    def test_repository_assignment_promotion_selection_is_valid(self) -> None:
        result = validate_assignment_promotion_selection(ROOT)
        self.assertTrue(result.valid, result.errors)

    def test_all_gate_candidates_are_individually_derived_and_only_assignment_is_eligible(self) -> None:
        rows = {row["document_id"]: row for row in self.payload()["candidate_inventory"]}
        self.assertEqual(tuple(rows), selection.CANDIDATE_IDS)
        self.assertEqual(rows["OCP-005"]["eligibility"], "eligible")
        self.assertEqual(rows["OCP-006"]["l2_blockers"], [])
        self.assertEqual(rows["OCP-006"]["l2_result"], "pass")
        self.assertEqual(rows["OCP-006"]["disposition"], "rejected-not-selected-by-this-Board-decision")
        self.assertEqual(rows["OCP-006"]["eligibility"], "ineligible")
        self.assertEqual(rows["OCP-010"]["prior_cycle"], "EVENT_T6")
        self.assertEqual(rows["OCP-010"]["eligibility"], "ineligible")
        changed = self.payload()
        changed["candidate_inventory"][1]["eligibility"] = "eligible"
        first, second = self.with_changed_map(changed)
        with first, second:
            self.assertIn(
                ASSIGNMENT_SELECTION_CANDIDATE_DRIFT,
                validate_assignment_promotion_selection(ROOT).errors,
            )

    def test_only_selection_step_is_completed(self) -> None:
        original_load = selection._load
        for step in ("DOCUMENT_PROMOTION", "CONCEPT_CANONICALIZATION"):
            gate = copy.deepcopy(original_load(ROOT / selection.GATE_PATH))
            gate["cycles"][1]["steps"][step] = "completed"
            gate["cycles"][1]["evidence"][step] = "UNAUTHORIZED"

            def changed_load(path: Path, gate=gate):
                return gate if path == ROOT / selection.GATE_PATH else original_load(path)

            with self.subTest(step=step), patch.object(selection, "_load", side_effect=changed_load):
                self.assertIn(
                    ASSIGNMENT_SELECTION_GATE_DRIFT,
                    validate_assignment_promotion_selection(ROOT).errors,
                )

    def test_active_cycle_id_is_atomic_in_both_directions(self) -> None:
        original_load = selection._load
        attacks = []
        gate_without_active = copy.deepcopy(original_load(ROOT / selection.GATE_PATH))
        gate_without_active["cycle_protocol"]["active_cycle_id"] = None
        attacks.append(gate_without_active)
        active_without_cycle = copy.deepcopy(original_load(ROOT / selection.GATE_PATH))
        active_without_cycle["cycles"].pop()
        attacks.append(active_without_cycle)
        for index, gate in enumerate(attacks):
            def changed_load(path: Path, gate=gate):
                return gate if path == ROOT / selection.GATE_PATH else original_load(path)

            with self.subTest(direction=index), patch.object(selection, "_load", side_effect=changed_load):
                self.assertIn(
                    ASSIGNMENT_SELECTION_GATE_DRIFT,
                    validate_assignment_promotion_selection(ROOT).errors,
                )

    def test_every_document_status_version_and_concept_status_is_protected(self) -> None:
        current = selection._current_documents(ROOT)
        for document_id, values in current.items():
            for index, label in enumerate(("version", "status", "concept_status")):
                if values[index] is None:
                    continue
                changed = dict(current)
                replacement = list(values)
                replacement[index] = f"MUTATED-{replacement[index]}"
                changed[document_id] = tuple(replacement)
                with self.subTest(document_id=document_id, field=label), patch.object(
                    selection, "_current_documents", return_value=changed
                ), patch.object(selection, "_baseline_documents", return_value=current):
                    self.assertIn(
                        ASSIGNMENT_SELECTION_BOUNDARY_DRIFT,
                        validate_assignment_promotion_selection(ROOT).errors,
                    )

    def test_forward_and_rollback_closure_are_both_enforced(self) -> None:
        self.assertTrue(selection.rollback_gate_probe(ROOT))
        for axis in ("forward", "rollback"):
            changed = self.payload()
            changed["closability"][axis]["defined"] = False
            first, second = self.with_changed_map(changed)
            with self.subTest(axis=axis), first, second:
                self.assertIn(
                    ASSIGNMENT_SELECTION_CLOSABILITY_DRIFT,
                    validate_assignment_promotion_selection(ROOT).errors,
                )

    def test_live_carriers_and_predecessors_are_byte_exact(self) -> None:
        payload = self.payload()
        successions = payload["historical_evidence_successions"]
        self.assertEqual(len(successions), len(selection.LIVE_CARRIERS) + 1)
        for row in successions:
            with self.subTest(path=row["original_path"]):
                baseline = selection._baseline_object(ROOT, row["original_path"])
                self.assertIsNotNone(baseline)
                raw = (ROOT / row["preserved_path"]).read_bytes()
                self.assertEqual(raw, baseline[1])
                self.assertEqual(hashlib.sha256(raw).hexdigest(), row["sha256"])
        changed = self.payload()
        changed["historical_evidence_successions"][0]["sha256"] = "0" * 64
        first, second = self.with_changed_map(changed)
        with first, second:
            self.assertIn(
                ASSIGNMENT_SELECTION_HISTORICAL_DRIFT,
                validate_assignment_promotion_selection(ROOT).errors,
            )

    def test_each_live_projection_guard_value_is_individually_derived(self) -> None:
        original_load = selection._load
        for relative in selection.LIVE_CARRIERS:
            carrier = original_load(ROOT / relative)
            guards = selection._gate_guards(carrier)
            for guard_index, guard in enumerate(guards):
                for key in ("schema_version", "completed_cycle_ids", "active_cycle_id"):
                    changed = copy.deepcopy(carrier)
                    changed_guard = selection._gate_guards(changed)[guard_index]
                    changed_guard[key] = f"MUTATED-{changed_guard[key]}"

                    def changed_load(path: Path, changed=changed, relative=relative):
                        return changed if path == ROOT / relative else original_load(path)

                    with self.subTest(path=relative, key=key), patch.object(
                        selection, "_load", side_effect=changed_load
                    ):
                        self.assertIn(
                            ASSIGNMENT_SELECTION_PROJECTION_DRIFT,
                            validate_assignment_promotion_selection(ROOT).errors,
                        )

    def test_baseline_anchors_are_full_chain(self) -> None:
        payload = self.payload()
        tree = subprocess.check_output(
            ["git", "ls-tree", "-r", payload["baseline"]], cwd=ROOT, text=True
        ).splitlines()
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
        original_load = selection._load
        for value_path in scalar_paths(payload):
            changed = mutate(payload, value_path)

            def changed_load(path: Path, changed=changed):
                return changed if path == ROOT / selection.MAP_PATH else original_load(path)

            with self.subTest(value_path=value_path), patch.object(
                selection, "_load", side_effect=changed_load
            ):
                self.assertFalse(validate_assignment_promotion_selection(ROOT).valid)


if __name__ == "__main__":
    unittest.main()
