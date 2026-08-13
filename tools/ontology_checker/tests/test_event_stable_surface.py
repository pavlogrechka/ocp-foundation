from __future__ import annotations

from pathlib import Path
from unittest.mock import patch
import shutil
import sys
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import event_stable_surface  # noqa: E402
from ocp_checker.event_stable_surface import (  # noqa: E402
    EVENT_STABLE_SURFACE_CONSUMER_DRIFT,
    EVENT_STABLE_SURFACE_DEPENDENCY_DRIFT,
    EVENT_STABLE_SURFACE_EVIDENCE_DRIFT,
    EVENT_STABLE_SURFACE_MAP_INVALID,
    EVENT_STABLE_SURFACE_NEXT_GATE_REQUIRED,
    EVENT_STABLE_SURFACE_SUBJECT_DRIFT,
    validate_event_stable_surface,
)


EXPECTED_DIRECT_DEPENDENCIES = {
    "OCP-000", "OCP-001", "OCP-002", "OCP-004", "OCP-008", "AD-006", "P-001"
}
EXPECTED_DIRECT_CONSUMERS = {"OCP-011", "OCP-017"}
EXPECTED_BINDING_KINDS = {
    "unversioned-document", "unversioned-decision", "unversioned-pattern-plus-exact-use"
}
EXPECTED_STABLE_SURFACES = {
    "EVENT_IDENTITY_KERNEL",
    "OBSERVATION_RECORD_KERNEL",
    "P001_OBSERVATION_BINDING",
    "CROSS_DOMAIN_NON_IMPLICATIONS",
    "EXECUTABLE_REFERENCE_BOUNDARY",
}
EXPECTED_MOVING_SURFACES = {
    "TEMPORAL_EXTENSION",
    "OPERATION_EVENT_RELATION",
    "EVENT_CORRELATION",
    "EVENT_KIND_GOVERNANCE",
    "LEGACY_ASSESSMENT_ENVELOPE",
}
EXPECTED_BLOCKERS = {
    "UNRESOLVED_OPERATION_EVENT_OWNER",
    "LEGACY_ASSESSMENT_ENVELOPE_OVERLAP",
    "UNVERSIONED_PRIMARY_CONSUMER_BINDINGS",
    "CANDIDATE_BOARD_SELECTION_ABSENT",
}
EXPECTED_REMAINING_GATES = {"CANDIDATE_BOARD_SELECTION"}
EXPECTED_FORBIDDEN_OUTCOMES = {
    "OCP010_ACCEPTANCE",
    "CANONICAL_PROMOTION",
    "T6_OPEN",
    "DISCOVERY_SELF_SUPPLIED_REASSESSMENT",
    "CANDIDATE_BOARD_SELECTION",
}
EXPECTED_DISPOSITIONS = {
    "EVENT_IDENTITY_KERNEL": "candidate",
    "OBSERVATION_RECORD_KERNEL": "candidate",
    "P001_OBSERVATION_BINDING": "candidate",
    "CROSS_DOMAIN_NON_IMPLICATIONS": "candidate",
    "EXECUTABLE_REFERENCE_BOUNDARY": "candidate",
    "TEMPORAL_EXTENSION": "moving",
    "OPERATION_EVENT_RELATION": "moving",
    "EVENT_CORRELATION": "moving",
    "EVENT_KIND_GOVERNANCE": "moving",
    "LEGACY_ASSESSMENT_ENVELOPE": "moving",
    "UNRESOLVED_OPERATION_EVENT_OWNER": "blocks_whole_document_freeze",
    "LEGACY_ASSESSMENT_ENVELOPE_OVERLAP": "blocks_whole_document_freeze",
    "UNVERSIONED_PRIMARY_CONSUMER_BINDINGS": "requires_consumer_compatibility_evidence",
    "CANDIDATE_BOARD_SELECTION_ABSENT": "blocks_promotion",
}
EXPECTED_EVIDENCE = {
    "EVENT_IDENTITY_KERNEL": (("docs/010-event-concept/README.md", ("## 4. Event identity", "`event_id` є єдиною Core identity Event", "## 8. Exact Event resolution")),),
    "OBSERVATION_RECORD_KERNEL": (("docs/010-event-concept/README.md", ("## 6. ObservationRecord", "має власну identity", "## 9. Observation collection derivation")),),
    "P001_OBSERVATION_BINDING": (("docs/010-event-concept/README.md", ("invokes `P-001@0.1.0` для ObservationRecord", "## 20. P-001 conformance for ObservationRecord")),),
    "CROSS_DOMAIN_NON_IMPLICATIONS": (("docs/010-event-concept/README.md", ("## 10. Operation boundary", "## 11. Objective and assessment boundary", "## 12. Constraint, Conflict and Risk boundary", "## 13. Capability, Readiness and State boundary")),),
    "EXECUTABLE_REFERENCE_BOUNDARY": (("tools/ontology_checker/rules.yaml", ("source: OCP-010 §8 exact Event reference contract", "source: OCP-010 §9")), ("tools/ontology_checker/ocp_checker/event.py", ("EVENT_DERIVATION_RULES", "def resolve_event(", "def observations_for_event("))),
    "TEMPORAL_EXTENSION": (("docs/010-event-concept/README.md", ("не визначає interval, uncertainty range, timezone policy", "окремого temporal interval module")),),
    "OPERATION_EVENT_RELATION": (("docs/010-event-concept/README.md", ("не вводить current Concept edge `Event → Operation` або `Operation → Event`", "Operation-to-Event relationship record")),),
    "EVENT_CORRELATION": (("docs/010-event-concept/README.md", ("не визначає автоматичну occurrence deduplication", "domain correlation rules")),),
    "EVENT_KIND_GOVERNANCE": (("docs/010-event-concept/README.md", ("canonical Event taxonomy", "governed Event-kind registry")),),
    "LEGACY_ASSESSMENT_ENVELOPE": (("docs/010-event-concept/README.md", ("checker-local assessment envelope", "не є normative OutcomeAssessmentRecord contract")), ("docs/011-outcome-assessment-record/README.md", ("Status: Accepted", "event@1", "observation-record@1"))),
    "UNRESOLVED_OPERATION_EVENT_OWNER": (("docs/010-event-concept/README.md", ("Який normative owner визначить Operation-to-Event relationship record",)),),
    "LEGACY_ASSESSMENT_ENVELOPE_OVERLAP": (("docs/010-event-concept/README.md", ("checker-local assessment envelope", "General OutcomeAssessmentRecord contract належить AB-056")), ("docs/011-outcome-assessment-record/README.md", ("Status: Accepted", "OutcomeAssessmentRecord"))),
    "UNVERSIONED_PRIMARY_CONSUMER_BINDINGS": (("docs/011-outcome-assessment-record/README.md", ("Depends-On: OCP-000, OCP-001, OCP-002, OCP-004, OCP-006, OCP-008, OCP-010",)), ("docs/017-operation-lifecycle/README.md", ("Depends-On: AD-020, OCP-001, OCP-004, OCP-005, OCP-006, OCP-010",))),
    "CANDIDATE_BOARD_SELECTION_ABSENT": (("architecture/event-stable-surface.yaml", ("baseline_gate_state:", "required_before_promotion: [POST_DISCOVERY_REASSESSMENT, CANDIDATE_BOARD_SELECTION]", "promotion_selections: []")),),
}


class EventStableSurfaceTests(unittest.TestCase):
    map_path = Path("architecture/event-stable-surface.yaml")
    gate_path = Path("architecture/foundation-promotion-gate.yaml")

    def payload(self, root: Path = ROOT) -> dict:
        return yaml.safe_load((root / self.map_path).read_text(encoding="utf-8"))

    def copy_inputs(self, destination: Path) -> None:
        shutil.copytree(ROOT / "docs", destination / "docs")
        for relative in (
            self.map_path,
            self.gate_path,
            Path("tools/ontology_checker/rules.yaml"),
            Path("tools/ontology_checker/ocp_checker/event.py"),
        ):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)

    def write_yaml(self, root: Path, relative: Path, payload: dict) -> None:
        (root / relative).write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    def test_repository_event_stable_surface_is_valid(self) -> None:
        self.assertTrue(validate_event_stable_surface(ROOT).valid)

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            ("DIRECT_DEPENDENCY_IDS", EXPECTED_DIRECT_DEPENDENCIES),
            ("DIRECT_CONSUMER_IDS", EXPECTED_DIRECT_CONSUMERS),
            ("BINDING_KINDS", EXPECTED_BINDING_KINDS),
            ("STABLE_SURFACE_IDS", EXPECTED_STABLE_SURFACES),
            ("MOVING_SURFACE_IDS", EXPECTED_MOVING_SURFACES),
            ("BLOCKER_IDS", EXPECTED_BLOCKERS),
            ("REMAINING_GATE_IDS", EXPECTED_REMAINING_GATES),
            ("FORBIDDEN_OUTCOMES", EXPECTED_FORBIDDEN_OUTCOMES),
        )
        for attribute, expected_values in categories:
            production_values = getattr(event_stable_surface, attribute)
            self.assertEqual(production_values, frozenset(expected_values))
            for value in sorted(expected_values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    event_stable_surface, attribute, production_values - {value}
                ):
                    self.assertIn(
                        EVENT_STABLE_SURFACE_MAP_INVALID,
                        validate_event_stable_surface(ROOT).errors,
                    )

        self.assertEqual(event_stable_surface.EXPECTED_DISPOSITIONS, EXPECTED_DISPOSITIONS)
        for entry_id, disposition in EXPECTED_DISPOSITIONS.items():
            mutated = dict(EXPECTED_DISPOSITIONS)
            mutated[entry_id] = disposition + "-mutated"
            with self.subTest(entry_id=entry_id, disposition=disposition), patch.object(
                event_stable_surface, "EXPECTED_DISPOSITIONS", mutated
            ):
                self.assertIn(
                    EVENT_STABLE_SURFACE_MAP_INVALID,
                    validate_event_stable_surface(ROOT).errors,
                )

        self.assertEqual(event_stable_surface.EXPECTED_EVIDENCE, EXPECTED_EVIDENCE)
        for entry_id, items in EXPECTED_EVIDENCE.items():
            for item_index, (source, tokens) in enumerate(items):
                for token in tokens:
                    mutated = dict(EXPECTED_EVIDENCE)
                    mutated_items = list(items)
                    mutated_items[item_index] = (source, tuple(value for value in tokens if value != token))
                    mutated[entry_id] = tuple(mutated_items)
                    with self.subTest(entry_id=entry_id, defensive_token=token), patch.object(
                        event_stable_surface, "EXPECTED_EVIDENCE", mutated
                    ):
                        self.assertIn(
                            EVENT_STABLE_SURFACE_MAP_INVALID,
                            validate_event_stable_surface(ROOT).errors,
                        )

    def test_historical_subject_identity_version_and_lifecycle_snapshot_is_individually_live(self) -> None:
        mutations = (
            ("Document-ID: OCP-010", "Document-ID: OCP-099"),
            ("Version: 0.2.1", "Version: 0.2.2"),
            ("Status: Draft", "Status: Accepted"),
            ("Concept-Status: Accepted", "Concept-Status: Canonical"),
            ("Uses-Patterns: P-001@0.1.0", "Uses-Patterns: P-001@0.2.0"),
        )
        for old, new in mutations:
            with self.subTest(old=old), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                payload = self.payload(root)
                for field, value in tuple(payload["subject"].items()):
                    if str(value) == old.split(": ", 1)[-1]:
                        payload["subject"][field] = new.split(": ", 1)[-1]
                self.write_yaml(root, self.map_path, payload)
                self.assertIn(
                    EVENT_STABLE_SURFACE_SUBJECT_DRIFT,
                    validate_event_stable_surface(root).errors,
                )

    def test_every_baseline_evidence_object_value_is_individually_live(self) -> None:
        payload = self.payload()
        self.assertEqual(set(event_stable_surface.BASELINE_OBJECT_KEYS), {"path", "blob", "sha256"})
        for item_index, item in enumerate(payload["baseline_evidence_objects"]):
            for key in sorted(event_stable_surface.BASELINE_OBJECT_KEYS):
                with self.subTest(item=item_index, key=key), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    mutated = self.payload(root)
                    mutated["baseline_evidence_objects"][item_index][key] = item[key] + "-mutated"
                    self.write_yaml(root, self.map_path, mutated)
                    self.assertIn(
                        EVENT_STABLE_SURFACE_EVIDENCE_DRIFT,
                        validate_event_stable_surface(root).errors,
                    )

    def test_every_direct_dependency_and_exact_pattern_binding_is_live(self) -> None:
        for dependency in event_stable_surface.DIRECT_DEPENDENCY_ORDER:
            with self.subTest(dependency=dependency), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                primary = root / "docs/010-event-concept/README.md"
                text = primary.read_text(encoding="utf-8")
                line = next(item for item in text.splitlines() if item.startswith("Depends-On:"))
                values = [item.strip() for item in line.split(":", 1)[1].split(",")]
                values.remove(dependency)
                primary.write_text(
                    text.replace(line, "Depends-On: " + ", ".join(values), 1), encoding="utf-8"
                )
                self.assertIn(
                    EVENT_STABLE_SURFACE_DEPENDENCY_DRIFT,
                    validate_event_stable_surface(root).errors,
                )

    def test_each_direct_consumer_and_record_binding_is_live(self) -> None:
        payload = self.payload()
        for consumer in payload["direct_consumers"]:
            mutations = ["OCP-010", *consumer["exact_record_refs"]]
            for token in mutations:
                with self.subTest(consumer=consumer["document_id"], token=token), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.copy_inputs(root)
                    primary = root / consumer["primary"]
                    text = primary.read_text(encoding="utf-8")
                    replacement = token + "-mutated" if token == "OCP-010" else token.replace("@", "-mutated@")
                    primary.write_text(text.replace(token, replacement), encoding="utf-8")
                    self.assertIn(
                        EVENT_STABLE_SURFACE_CONSUMER_DRIFT,
                        validate_event_stable_surface(root).errors,
                    )

    def test_every_declared_surface_and_blocker_token_remains_in_historical_witness(self) -> None:
        payload = self.payload()
        for category in ("stable_candidates", "moving_surfaces", "blockers"):
            for entry in payload[category]:
                entry_id = entry.get("surface_id") or entry.get("blocker_id")
                for evidence in entry["evidence"]:
                    for token in evidence["tokens"]:
                        with self.subTest(category=category, entry=entry_id, token=token), tempfile.TemporaryDirectory() as tmp:
                            root = Path(tmp)
                            self.copy_inputs(root)
                            payload = self.payload(root)
                            mutated_entry = next(
                                value for value in payload[category]
                                if (value.get("surface_id") or value.get("blocker_id")) == entry_id
                            )
                            mutated_evidence = next(value for value in mutated_entry["evidence"] if value["path"] == evidence["path"])
                            mutated_evidence["tokens"].remove(token)
                            self.write_yaml(root, self.map_path, payload)
                            self.assertIn(EVENT_STABLE_SURFACE_MAP_INVALID, validate_event_stable_surface(root).errors)

    def test_discovery_baseline_witness_rejects_mutation_but_survives_live_selection(self) -> None:
        mutations = ("regress_discovery", "regress_reassessment", "self_select")
        for mutation in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                gate = self.payload(root)["baseline_gate_state"]
                if mutation == "regress_discovery":
                    gate["completed_steps"].remove("Y10D")
                elif mutation == "regress_reassessment":
                    gate["required_before_promotion"].remove("POST_DISCOVERY_REASSESSMENT")
                else:
                    gate["promotion_selections"] = ["OCP-010"]
                payload = self.payload(root)
                payload["baseline_gate_state"] = gate
                self.write_yaml(root, self.map_path, payload)
                self.assertIn(
                    EVENT_STABLE_SURFACE_MAP_INVALID,
                    validate_event_stable_surface(root).errors,
                )


if __name__ == "__main__":
    unittest.main()
