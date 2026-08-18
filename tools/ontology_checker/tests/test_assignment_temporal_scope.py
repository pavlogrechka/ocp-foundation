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

from ocp_checker import assignment_temporal_scope  # noqa: E402
from ocp_checker.assignment_temporal_scope import (  # noqa: E402
    ASSIGNMENT_TEMPORAL_SCOPE_GATE_DRIFT,
    ASSIGNMENT_TEMPORAL_SCOPE_OWNER_TEXT_DRIFT,
    ASSIGNMENT_TEMPORAL_SCOPE_PROBE_DRIFT,
    ASSIGNMENT_TEMPORAL_SCOPE_PROJECTION_DRIFT,
    validate_assignment_temporal_scope,
)
from ocp_checker.checker import assignment_effective_at, load_fixture, validate_assignment  # noqa: E402


class AssignmentTemporalScopeTests(unittest.TestCase):
    map_path = Path("architecture/assignment-temporal-scope-attempt.yaml")
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

    def test_repository_assignment_temporal_scope_attempt_is_valid(self) -> None:
        self.assertTrue(validate_assignment_temporal_scope(ROOT).valid)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        sets = (
            "MAP_KEYS",
            "OWNER_EVIDENCE_IDS",
            "TEMPORAL_OBLIGATION_IDS",
            "PARTIAL_SCOPE_OBLIGATION_IDS",
            "PROBE_IDS",
            "QUESTION_IDS",
            "FORBIDDEN_OUTCOMES",
        )
        for attribute in sets:
            production_values = getattr(assignment_temporal_scope, attribute)
            for value in sorted(production_values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    assignment_temporal_scope, attribute, production_values - {value}
                ):
                    self.assertFalse(validate_assignment_temporal_scope(ROOT).valid)

        for attribute in ("EXPECTED_PROBE_FIXTURE",):
            production_value = getattr(assignment_temporal_scope, attribute)
            with self.subTest(attribute=attribute), patch.object(
                assignment_temporal_scope, attribute, f"MUTATED-{production_value}"
            ):
                self.assertFalse(validate_assignment_temporal_scope(ROOT).valid)

        dictionaries = (
            "EXPECTED_IDENTITY",
            "EXPECTED_GATE_FIRST",
            "EXPECTED_SUBJECT",
            "EXPECTED_ZONE_RESULTS",
            "EXPECTED_OWNER_EVIDENCE",
            "EXPECTED_CONTROL",
            "EXPECTED_PROBES",
            "EXPECTED_PROJECTION",
            "CURRENT_PROJECTION",
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
            production_values = getattr(assignment_temporal_scope, attribute)
            for value_path in scalar_paths(production_values):
                mutated = mutate_scalar(production_values, value_path)
                with self.subTest(attribute=attribute, value_path=value_path), patch.object(
                    assignment_temporal_scope, attribute, mutated
                ):
                    self.assertFalse(validate_assignment_temporal_scope(ROOT).valid)

    def test_each_owner_text_token_is_live(self) -> None:
        payload = self.payload()
        records = [
            (entry["path"], token)
            for entry in payload["owner_text_evidence"]
            for token in entry["tokens"]
        ]
        for relative, token in records:
            with self.subTest(path=relative, token=token), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                fpath = root / relative
                text = fpath.read_text(encoding="utf-8")
                live_token = (
                    assignment_temporal_scope.CURRENT_Q3_BOUNDARY
                    if token.startswith("До окремого рішення про ретроактивне Establishment")
                    else token
                )
                self.assertIn(live_token, text)
                fpath.write_text(text.replace(live_token, "MUTATED-LIVE-TOKEN"), encoding="utf-8")
                self.assertIn(
                    ASSIGNMENT_TEMPORAL_SCOPE_OWNER_TEXT_DRIFT,
                    validate_assignment_temporal_scope(root).errors,
                )

    def test_existing_pre_establishment_effectivity_boundary_is_isolated(self) -> None:
        fixture = load_fixture(ROOT / self.fixture_path)
        controlled = copy.deepcopy(fixture["entity"])
        controlled["applicability_start"] = "2026-08-02T09:50:00Z"
        self.assertTrue(validate_assignment(controlled).valid)
        self.assertFalse(assignment_effective_at(controlled, "2026-08-02T09:54:00Z"))
        self.assertTrue(assignment_effective_at(controlled, "2026-08-02T09:55:00Z"))

    def test_current_checker_exposes_all_three_remaining_boundary_gaps(self) -> None:
        fixture = load_fixture(ROOT / self.fixture_path)
        original = fixture["entity"]
        self.assertTrue(validate_assignment(original).valid)

        retroactive = copy.deepcopy(original)
        retroactive["transition_history"][0]["occurred_at"] = "2026-08-02T09:52:00Z"
        retroactive["established_at"] = "2026-08-02T09:52:00Z"

        multiple_intervals = copy.deepcopy(original)
        multiple_intervals["applicability_intervals"] = [
            {"start": "2026-08-02T10:00:00Z", "end": "2026-08-02T10:30:00Z"},
            {"start": "2026-08-02T11:00:00Z", "end": "2026-08-02T12:00:00Z"},
        ]

        partial_scope = copy.deepcopy(original)
        partial_scope["resource_scope"] = {
            "kind": "component",
            "component_ref": "R-COMPONENT-001",
        }

        variants = {
            "retroactive-establishment": retroactive,
            "multiple-intervals": multiple_intervals,
            "partial-scope": partial_scope,
        }
        for label, mutated in variants.items():
            with self.subTest(probe=label):
                self.assertTrue(validate_assignment(mutated).valid)

    def test_historical_q3_result_survives_while_current_q3_is_closed_only(self) -> None:
        mutations = (
            "Q3",
            "Q9",
            "Q5",
            "TEMPORAL_EFFECTIVITY_EXTENSION",
            "COMPOSITE_RESOURCE_SCOPE",
            "TEMPORAL_MODEL_UNRESOLVED",
            "PARTIAL_SCOPE_IDENTITY_UNRESOLVED",
        )
        for mutation in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                surface = yaml.safe_load((root / self.surface_path).read_text(encoding="utf-8"))
                if mutation in {"Q3", "Q9", "Q5"}:
                    target = next(
                        item for item in surface["open_question_inventory"]
                        if item["question_id"] == mutation
                    )
                    if mutation == "Q3":
                        target["state"] = "open"
                        target["classification"] = "blocks-whole-document-freeze"
                    else:
                        target["classification"] = "local-after-bounded-freeze"
                elif mutation in {"TEMPORAL_EFFECTIVITY_EXTENSION", "COMPOSITE_RESOURCE_SCOPE"}:
                    surface["moving_surfaces"] = [
                        item for item in surface["moving_surfaces"]
                        if item["surface_id"] != mutation
                    ]
                else:
                    surface["blockers"] = [
                        item for item in surface["blockers"]
                        if item["blocker_id"] != mutation
                    ]
                self.write_yaml(root, self.surface_path, surface)
                self.assertIn(
                    ASSIGNMENT_TEMPORAL_SCOPE_PROJECTION_DRIFT,
                    validate_assignment_temporal_scope(root).errors,
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
                    ASSIGNMENT_TEMPORAL_SCOPE_GATE_DRIFT,
                    validate_assignment_temporal_scope(root).errors,
                )


if __name__ == "__main__":
    unittest.main()
