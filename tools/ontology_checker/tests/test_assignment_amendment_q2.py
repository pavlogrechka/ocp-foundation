from __future__ import annotations

import copy
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import assignment_amendment_q2  # noqa: E402
from ocp_checker.assignment_amendment_q2 import (  # noqa: E402
    ASSIGNMENT_AMENDMENT_Q2_CONSUMER_DRIFT,
    ASSIGNMENT_AMENDMENT_Q2_GATE_DRIFT,
    ASSIGNMENT_AMENDMENT_Q2_OWNER_TEXT_DRIFT,
    ASSIGNMENT_AMENDMENT_Q2_PROBE_DRIFT,
    ASSIGNMENT_AMENDMENT_Q2_PROJECTION_DRIFT,
    validate_assignment_amendment_q2,
)
from ocp_checker.checker import load_fixture, validate_assignment  # noqa: E402


class AssignmentAmendmentQ2Tests(unittest.TestCase):
    map_path = Path("architecture/assignment-amendment-q2-attempt.yaml")
    surface_path = Path("architecture/assignment-stable-surface.yaml")
    gate_path = Path("architecture/foundation-promotion-gate.yaml")
    fixture_path = Path("tools/ontology_checker/fixtures/assignment/valid-established.yaml")

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "docs", destination / "docs")
        for relative in (self.map_path, self.surface_path, self.gate_path, self.fixture_path):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    def test_repository_assignment_amendment_q2_attempt_is_valid(self) -> None:
        self.assertTrue(validate_assignment_amendment_q2(ROOT).valid)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        sets = (
            "MAP_KEYS",
            "OWNER_EVIDENCE_IDS",
            "MISSING_OBLIGATION_IDS",
            "ACCEPTED_CONSUMER_IDS",
            "PROBE_IDS",
            "UNCHANGED_PROBE_FIELDS",
            "FORBIDDEN_OUTCOMES",
        )
        for attribute in sets:
            production_values = getattr(assignment_amendment_q2, attribute)
            for value in sorted(production_values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    assignment_amendment_q2, attribute, production_values - {value}
                ):
                    self.assertFalse(validate_assignment_amendment_q2(ROOT).valid)

        dictionaries = (
            "EXPECTED_GATE_FIRST",
            "EXPECTED_SUBJECT",
            "EXPECTED_HYPOTHESIS_RESULT",
            "EXPECTED_OWNER_EVIDENCE",
            "EXPECTED_CONSUMERS",
            "EXPECTED_PROBES",
            "EXPECTED_PROJECTION",
            "EXPECTED_GATE_GUARD",
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
                    return "MUTATED-DEFENSIVE-VALUE"
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

        for attribute in dictionaries:
            production_values = getattr(assignment_amendment_q2, attribute)
            for value_path in scalar_paths(production_values):
                mutated = mutate_scalar(production_values, value_path)
                with self.subTest(attribute=attribute, value_path=value_path), patch.object(
                    assignment_amendment_q2, attribute, mutated
                ):
                    self.assertFalse(validate_assignment_amendment_q2(ROOT).valid)

    def test_each_owner_and_consumer_token_is_live(self) -> None:
        payload = self.payload()
        records = [
            (entry["path"], token, ASSIGNMENT_AMENDMENT_Q2_OWNER_TEXT_DRIFT)
            for entry in payload["owner_text_evidence"]
            for token in entry["tokens"]
        ]
        records.extend(
            (
                entry["primary"],
                entry["evidence_token"],
                ASSIGNMENT_AMENDMENT_Q2_CONSUMER_DRIFT,
            )
            for entry in payload["accepted_consumer_review"]
        )
        for relative, token, expected_error in records:
            with self.subTest(path=relative, token=token), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                fpath = root / relative
                text = fpath.read_text(encoding="utf-8")
                self.assertIn(token, text)
                fpath.write_text(text.replace(token, "MUTATED-LIVE-TOKEN"), encoding="utf-8")
                self.assertIn(expected_error, validate_assignment_amendment_q2(root).errors)

    def test_live_consumer_inventory_includes_later_accepted_consumers(self) -> None:
        for document_id in ("OCP-021", "OCP-023"):
            for mutation in ("dependency", "status"):
                with self.subTest(document=document_id, mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    relative = next(
                        entry[0] for key, entry in assignment_amendment_q2.EXPECTED_CONSUMERS.items()
                        if key == document_id
                    )
                    fpath = root / relative
                    text = fpath.read_text(encoding="utf-8")
                    if mutation == "dependency":
                        text = text.replace("OCP-005, ", "", 1)
                    else:
                        text = text.replace("Status: Accepted", "Status: Draft", 1)
                    fpath.write_text(text, encoding="utf-8")
                    self.assertIn(
                        ASSIGNMENT_AMENDMENT_Q2_CONSUMER_DRIFT,
                        validate_assignment_amendment_q2(root).errors,
                    )

    def test_current_checker_exposes_both_post_establishment_value_change_gaps(self) -> None:
        fixture = load_fixture(ROOT / self.fixture_path)
        original = fixture["entity"]
        self.assertTrue(validate_assignment(original).valid)
        variants = (
            ("role_specification", "role_code", "support"),
            (None, "applicability_end", "2026-08-02T13:00:00Z"),
        )
        for container, field, replacement in variants:
            with self.subTest(field=field):
                mutated = copy.deepcopy(original)
                if container is None:
                    mutated[field] = replacement
                else:
                    mutated[container][field] = replacement
                self.assertEqual(mutated["transition_history"], original["transition_history"])
                self.assertEqual(mutated["provenance_ref"], original["provenance_ref"])
                self.assertIsNone(mutated["supersedes_assignment_ref"])
                self.assertTrue(validate_assignment(mutated).valid)

    def test_q2_and_amendment_blocker_must_remain_open(self) -> None:
        mutations = ("question-state", "classification", "moving-surface", "blocker")
        for mutation in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                surface = yaml.safe_load((root / self.surface_path).read_text(encoding="utf-8"))
                if mutation in {"question-state", "classification"}:
                    target = next(item for item in surface["open_question_inventory"] if item["question_id"] == "Q2")
                    if mutation == "question-state":
                        target["state"] = "resolved-historical"
                    else:
                        target["classification"] = "local-after-bounded-freeze"
                elif mutation == "moving-surface":
                    surface["moving_surfaces"] = [
                        item for item in surface["moving_surfaces"]
                        if item["surface_id"] != "AMENDMENT_AFTER_ESTABLISHMENT"
                    ]
                else:
                    surface["blockers"] = [
                        item for item in surface["blockers"]
                        if item["blocker_id"] != "AMENDMENT_MODEL_ABSENT"
                    ]
                self.write_yaml(root, self.surface_path, surface)
                self.assertIn(
                    ASSIGNMENT_AMENDMENT_Q2_PROJECTION_DRIFT,
                    validate_assignment_amendment_q2(root).errors,
                )

    def test_promotion_gate_remains_between_completed_event_and_no_active_cycle(self) -> None:
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
                    ASSIGNMENT_AMENDMENT_Q2_GATE_DRIFT,
                    validate_assignment_amendment_q2(root).errors,
                )


if __name__ == "__main__":
    unittest.main()
