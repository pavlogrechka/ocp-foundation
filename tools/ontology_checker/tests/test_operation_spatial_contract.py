from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    load_fixture,
    validate_operation_spatial_transition,
    validate_reference_fixture,
)


class OperationSpatialContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.one = load_fixture(ROOT / "fixtures/operation/valid-draft-spatial-one.yaml")
        cls.many = load_fixture(
            ROOT / "fixtures/operation/valid-draft-spatial-many-equal-payload.yaml"
        )

    def test_zero_one_and_many_local_bindings_are_valid(self) -> None:
        zero_absent = {
            "concept": "Operation",
            "entity": {"operation_id": "OP-ZERO-ABSENT", "lifecycle_stage": "Draft"},
        }
        zero_explicit = load_fixture(
            ROOT / "fixtures/operation/valid-draft-spatial-empty-context.yaml"
        )
        for fixture in (zero_absent, zero_explicit, self.one, self.many):
            with self.subTest(case=fixture.get("case_id", "zero-absent")):
                self.assertTrue(validate_reference_fixture(fixture).valid)

    def test_equal_payload_does_not_collapse_local_binding_identity(self) -> None:
        bindings = self.many["entity"]["spatial_context"]["bindings"]
        self.assertEqual(bindings[0]["payload_snapshot_ref"], bindings[1]["payload_snapshot_ref"])
        self.assertNotEqual(bindings[0]["binding_id"], bindings[1]["binding_id"])
        self.assertTrue(validate_reference_fixture(self.many).valid)

    def test_equal_local_bindings_in_distinct_operations_remain_valid(self) -> None:
        first = copy.deepcopy(self.one)
        second = copy.deepcopy(self.one)
        second["entity"]["operation_id"] = "OP-SPATIAL-ONE-002"
        self.assertTrue(validate_reference_fixture(first).valid)
        self.assertTrue(validate_reference_fixture(second).valid)
        self.assertNotEqual(first["entity"]["operation_id"], second["entity"]["operation_id"])

    def test_reference_order_has_no_authority(self) -> None:
        candidate = copy.deepcopy(self.many)
        candidate["references"]["spatial_representation_profiles"].reverse()
        candidate["references"]["spatial_payload_snapshots"].reverse()
        self.assertTrue(validate_reference_fixture(candidate).valid)

    def test_duplicate_exact_profile_fails_closed(self) -> None:
        candidate = copy.deepcopy(self.one)
        profile = copy.deepcopy(candidate["references"]["spatial_representation_profiles"][0])
        profile["profile_owner_ref"] = "domain://another-owner"
        candidate["references"]["spatial_representation_profiles"].append(profile)
        self.assertEqual(
            set(validate_reference_fixture(candidate).errors),
            {"OPERATION_SPATIAL_PROFILE_UNRESOLVED"},
        )

    def test_duplicate_exact_snapshot_fails_closed(self) -> None:
        candidate = copy.deepcopy(self.one)
        snapshot = copy.deepcopy(candidate["references"]["spatial_payload_snapshots"][0])
        snapshot["opaque_payload_ref"] = "synthetic://spatial-payload/other@1"
        candidate["references"]["spatial_payload_snapshots"].append(snapshot)
        self.assertEqual(
            set(validate_reference_fixture(candidate).errors),
            {"OPERATION_SPATIAL_SNAPSHOT_UNRESOLVED"},
        )

    def test_binding_version_subject_must_match_local_identity(self) -> None:
        candidate = copy.deepcopy(self.one)
        candidate["entity"]["spatial_context"]["bindings"][0][
            "binding_version_ref"
        ] = "ANOTHER-LOCAL-ID@1"
        self.assertEqual(
            set(validate_reference_fixture(candidate).errors),
            {"OPERATION_SPATIAL_CONTEXT_INVALID"},
        )

    def test_planned_and_actual_scope_require_matching_operation_context(self) -> None:
        planned = copy.deepcopy(self.one)
        self.assertTrue(validate_reference_fixture(planned).valid)
        actual = copy.deepcopy(self.one)
        binding = actual["entity"]["spatial_context"]["bindings"][0]
        binding["temporal_scope"] = "actual-context"
        actual["entity"].pop("planned_start")
        self.assertIn(
            "OPERATION_SPATIAL_TEMPORAL_CONTEXT_INVALID",
            validate_reference_fixture(actual).errors,
        )
        actual["entity"]["actual_start"] = "2026-08-06T10:00:00Z"
        self.assertTrue(validate_reference_fixture(actual).valid)

    def test_forbidden_conclusion_fields_never_enter_binding_envelope(self) -> None:
        fields = (
            "resource_ref",
            "assignment_ref",
            "organization_ref",
            "coordination_ref",
            "conflict_ref",
            "authorization_ref",
            "readiness",
            "availability",
            "admissibility",
            "suitability",
            "selection_ref",
            "overlap",
            "visibility",
            "coordinates",
            "geometry",
        )
        for field in fields:
            with self.subTest(field=field):
                candidate = copy.deepcopy(self.one)
                candidate["entity"]["spatial_context"]["bindings"][0][field] = "forbidden"
                self.assertIn(
                    "OPERATION_SPATIAL_FORBIDDEN_COUPLING",
                    validate_reference_fixture(candidate).errors,
                )

    def test_changed_binding_requires_new_context_and_binding_versions(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/operation/valid-spatial-transition-new-versions.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        self.assertTrue(
            validate_operation_spatial_transition(fixture["previous"], fixture["current"]).valid
        )

    def test_binding_order_does_not_create_a_spatial_transition(self) -> None:
        previous = copy.deepcopy(self.many["entity"])
        current = copy.deepcopy(previous)
        current["spatial_context"]["bindings"].reverse()
        self.assertTrue(validate_operation_spatial_transition(previous, current).valid)

    def test_transition_version_reuse_and_operation_switch_fail_closed(self) -> None:
        paths = (
            "invalid-spatial-transition-context-version-reuse.yaml",
            "invalid-spatial-transition-binding-version-reuse.yaml",
            "invalid-spatial-transition-operation-id.yaml",
        )
        for name in paths:
            with self.subTest(name=name):
                fixture = load_fixture(ROOT / "fixtures/operation" / name)
                self.assertFalse(validate_reference_fixture(fixture).valid)


if __name__ == "__main__":
    unittest.main()
