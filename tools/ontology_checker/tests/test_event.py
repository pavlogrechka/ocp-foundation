from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    load_fixture,
    observations_for_event,
    resolve_event,
    validate_reference_fixture,
)


class EventContractTests(unittest.TestCase):
    def test_event_with_zero_observations_is_valid(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/event/valid-zero-observations.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        self.assertEqual(
            observations_for_event(fixture["observations"], "EV-ZERO-001"), ()
        )
        self.assertIsNotNone(resolve_event(fixture["events"], "EV-ZERO-001"))

    def test_two_observations_do_not_collapse(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/event/valid-two-observations-one-event.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        observations = observations_for_event(
            fixture["observations"], "EV-TWO-001"
        )
        self.assertEqual(len(observations), 2)
        self.assertEqual(
            {item["observation_id"] for item in observations},
            {"OBS-TWO-001", "OBS-TWO-002"},
        )

    def test_equal_kind_and_time_do_not_collapse_event_identity(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/event/valid-equal-kind-time-distinct-events.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        first = resolve_event(fixture["events"], "EV-EQUAL-001")
        second = resolve_event(fixture["events"], "EV-EQUAL-002")
        self.assertIsNotNone(first)
        self.assertIsNotNone(second)
        self.assertNotEqual(first["event_id"], second["event_id"])
        self.assertEqual(first["event_kind_ref"], second["event_kind_ref"])
        self.assertEqual(first["occurred_at"], second["occurred_at"])

    def test_duplicate_event_identity_is_order_independent(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/event/invalid-duplicate-event-identity.yaml"
        )
        expected = {"EVENT_IDENTITY_DUPLICATE", "EVENT_REFERENCE_AMBIGUOUS"}
        for order, events in (
            ("original", fixture["events"]),
            ("reversed", list(reversed(fixture["events"]))),
        ):
            with self.subTest(order=order):
                candidate = dict(fixture)
                candidate["events"] = events
                self.assertEqual(
                    set(validate_reference_fixture(candidate).errors), expected
                )
                self.assertIsNone(resolve_event(events, "EV-DUP-001"))

    def test_conflicting_observations_remain_visible(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/event/valid-conflicting-observations.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        observations = observations_for_event(
            fixture["observations"], "EV-CONFLICT-001"
        )
        self.assertEqual(len(observations), 2)
        self.assertEqual(len({item["statement"] for item in observations}), 2)

    def test_unresolved_observation_does_not_manufacture_event(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/event/valid-unresolved-observation.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        observation = fixture["observations"][0]
        self.assertNotIn("event_ref", observation)
        self.assertEqual(observations_for_event(fixture["observations"], "missing"), ())

    def test_reference_normalization_is_consistent(self) -> None:
        event = {
            "event_id": " EV-NORM-001 ",
            "event_kind_ref": "neutral.test@1",
            "registered_at": "2026-08-04T01:00:00Z",
            "identity_provenance_ref": "ACT-EVENT-NORM-001",
        }
        reference_fixture = {
            "concept": "EventReference",
            "events": [event],
            "reference": {"event_ref": "EV-NORM-001"},
        }
        self.assertTrue(validate_reference_fixture(reference_fixture).valid)

        observations = [
            {
                "observation_id": "OBS-NORM-001",
                "observer_ref": "SOURCE-NORM",
                "observation_kind_ref": "neutral.test@1",
                "statement": "A normalized reference is retained.",
                "observed_at": "2026-08-04T01:01:00Z",
                "recorded_at": "2026-08-04T01:02:00Z",
                "provenance_ref": "ACT-OBS-NORM-001",
                "event_ref": " EV-NORM-001 ",
            }
        ]
        self.assertEqual(
            len(observations_for_event(observations, "EV-NORM-001")),
            1,
        )

    def test_integrated_scenario_keeps_completion_separate_from_achievement(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/event/valid-integrated-scenario.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        scenario = fixture["scenario"]
        self.assertEqual(scenario["operation"]["lifecycle_stage"], "Completed")
        self.assertEqual(scenario["assessment"]["conclusion"], "indeterminate")

    def test_integrated_scenario_rejects_dangling_assignment_reference(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/event/invalid-integrated-dangling-assignment.yaml"
        )
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"SCENARIO_ASSIGNMENT_INVALID"},
        )

    def test_conflicting_evidence_cannot_produce_positive_conclusion(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/event/invalid-integrated-positive-conflict.yaml"
        )
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {
                "OUTCOME_ASSESSMENT_DEFINITIVE_EVIDENCE_UNSAFE",
                "OUTCOME_ASSESSMENT_EVIDENCE_STATE_MISMATCH",
            },
        )


if __name__ == "__main__":
    unittest.main()
