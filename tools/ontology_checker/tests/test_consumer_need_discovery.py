from __future__ import annotations

from pathlib import Path
from unittest.mock import patch
import copy
import shutil
import sys
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import consumer_need_discovery  # noqa: E402
from ocp_checker.consumer_need_discovery import (  # noqa: E402
    CONSUMER_NEED_CANDIDATE_DRIFT,
    CONSUMER_NEED_EVIDENCE_DRIFT,
    CONSUMER_NEED_GATE_HISTORY_DRIFT,
    CONSUMER_NEED_MAP_INVALID,
    CONSUMER_NEED_POSITIVE_OUTPUT_DRIFT,
    CONSUMER_NEED_PROMOTION_GATE_DRIFT,
    CONSUMER_NEED_SCOPE_DRIFT,
    validate_consumer_need_discovery,
)


class ConsumerNeedDiscoveryTests(unittest.TestCase):
    map_path = Path("architecture/consumer-need-discovery.yaml")
    gate_path = Path("architecture/foundation-promotion-gate.yaml")

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "docs", destination / "docs")
        shutil.copytree(ROOT / "patterns", destination / "patterns")
        shutil.copytree(ROOT / "architecture/discovery", destination / "architecture/discovery")
        for relative in (self.map_path, self.gate_path):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    def test_repository_consumer_need_discovery_is_valid(self) -> None:
        self.assertTrue(validate_consumer_need_discovery(ROOT).valid)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            "ELIGIBLE_LIFECYCLE_IDS", "ELIGIBLE_GOVERNANCE_IDS", "CANDIDATE_IDS",
            "ESTABLISHED_POSITIVE_IDS", "NEGATIVE_GATE_SUBJECTS", "FORBIDDEN_OUTCOMES",
        )
        for attribute in categories:
            production_values = getattr(consumer_need_discovery, attribute)
            for value in sorted(production_values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    consumer_need_discovery, attribute, production_values - {value}
                ):
                    self.assertFalse(validate_consumer_need_discovery(ROOT).valid)

        dictionaries = (
            "EXPECTED_CANDIDATES", "EXPECTED_POSITIVE_OUTPUTS", "EXPECTED_GATE_HISTORY",
            "EXPECTED_BASELINE_OBJECTS",
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

        def mutate_scalar(value, value_path):
            replacement = not value if isinstance(value, bool) else "MUTATED-DEFENSIVE-VALUE"
            part = value_path[0]
            if len(value_path) == 1:
                if isinstance(value, tuple):
                    rebuilt = list(value)
                    rebuilt[part] = replacement
                    return tuple(rebuilt)
                mutated = copy.deepcopy(value)
                mutated[part] = replacement
                return mutated
            child = mutate_scalar(value[part], value_path[1:])
            if isinstance(value, tuple):
                rebuilt = list(value)
                rebuilt[part] = child
                return tuple(rebuilt)
            mutated = copy.deepcopy(value)
            mutated[part] = child
            return mutated

        for attribute in dictionaries:
            production_values = getattr(consumer_need_discovery, attribute)
            for key in sorted(production_values):
                mutated = dict(production_values)
                del mutated[key]
                with self.subTest(attribute=attribute, removed=key), patch.object(
                    consumer_need_discovery, attribute, mutated
                ):
                    self.assertFalse(validate_consumer_need_discovery(ROOT).valid)
            for value_path in scalar_paths(production_values):
                top_key = value_path[0]
                mutated = copy.deepcopy(production_values)
                mutated[top_key] = mutate_scalar(mutated[top_key], value_path[1:])
                with self.subTest(attribute=attribute, path=value_path), patch.object(
                    consumer_need_discovery, attribute, mutated
                ):
                    self.assertFalse(validate_consumer_need_discovery(ROOT).valid)

    def test_complete_status_scope_is_live_for_primary_and_governance_documents(self) -> None:
        mutations = (
            (Path("docs/014-coordination-profile/README.md"), "Status: Accepted", "Status: Draft"),
            (
                Path("architecture/discovery/AD-022-conflict-derivation-boundary.md"),
                "Status: Accepted", "Status: Discovery",
            ),
        )
        for relative, old, new in mutations:
            with self.subTest(path=relative), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / relative
                path.write_text(path.read_text(encoding="utf-8").replace(old, new, 1), encoding="utf-8")
                self.assertIn(CONSUMER_NEED_SCOPE_DRIFT, validate_consumer_need_discovery(root).errors)

    def test_each_candidate_statement_and_disposition_is_live(self) -> None:
        for candidate in self.payload()["candidate_mentions"]:
            with self.subTest(candidate=candidate["candidate_id"]), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                path = root / candidate["path"]
                text = path.read_text(encoding="utf-8")
                path.write_text(text.replace(candidate["token"], "MUTATED-NEED-TOKEN"), encoding="utf-8")
                self.assertIn(
                    CONSUMER_NEED_CANDIDATE_DRIFT,
                    validate_consumer_need_discovery(root).errors,
                )

    def test_existing_positive_outputs_and_negative_gate_history_are_not_silent(self) -> None:
        groups = (
            ("established_positive_outputs", CONSUMER_NEED_POSITIVE_OUTPUT_DRIFT),
            ("negative_gate_history", CONSUMER_NEED_GATE_HISTORY_DRIFT),
        )
        for group, expected_error in groups:
            for item in self.payload()[group]:
                with self.subTest(group=group, artifact=item["artifact_id"]), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    path = root / item["path"]
                    text = path.read_text(encoding="utf-8")
                    path.write_text(text.replace(item["token"], "MUTATED-EVIDENCE-TOKEN", 1), encoding="utf-8")
                    self.assertIn(expected_error, validate_consumer_need_discovery(root).errors)

    def test_historical_result_and_current_need_cannot_be_conflated(self) -> None:
        mutations = (
            ("historical_result", "disposition", "unmet_positive_consumer_need_declared"),
            ("historical_result", "unmet_positive_needs", ["SYNTH-NEED"]),
            ("current_result", "disposition", "no_unmet_positive_consumer_need_declared"),
            ("current_result", "unmet_positive_needs", []),
            ("gate_first", "applies", True),
            ("gate_first", "accepted_consumer_activation_required", True),
        )
        for section, key, value in mutations:
            with self.subTest(section=section, key=key), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload(root)
                payload[section][key] = value
                self.write_yaml(root, self.map_path, payload)
                self.assertIn(CONSUMER_NEED_MAP_INVALID, validate_consumer_need_discovery(root).errors)

    def test_each_baseline_anchor_value_is_live(self) -> None:
        for index, item in enumerate(self.payload()["baseline_evidence_objects"]):
            for key in ("path", "blob", "sha256"):
                with self.subTest(index=index, key=key), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    payload = self.payload(root)
                    payload["baseline_evidence_objects"][index][key] = str(item[key]) + "-mutated"
                    self.write_yaml(root, self.map_path, payload)
                    self.assertIn(CONSUMER_NEED_EVIDENCE_DRIFT, validate_consumer_need_discovery(root).errors)

    def test_discovery_does_not_start_or_rewrite_a_promotion_cycle(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            gate = yaml.safe_load((root / self.gate_path).read_text(encoding="utf-8"))
            gate["cycle_protocol"]["active_cycle_id"] = "ASSIGNMENT_T7"
            self.write_yaml(root, self.gate_path, gate)
            self.assertIn(
                CONSUMER_NEED_PROMOTION_GATE_DRIFT,
                validate_consumer_need_discovery(root).errors,
            )


if __name__ == "__main__":
    unittest.main()
