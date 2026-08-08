from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    assignment_effective_at,
    derive_operation_lifecycle_stage,
    load_fixture,
    validate_reference_fixture,
)
from ocp_checker.operation_lifecycle import (  # noqa: E402
    OPERATION_LIFECYCLE_DERIVATION_RULES,
    OPERATION_LIFECYCLE_ERROR_CODES,
)


class OperationLifecycleContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = load_fixture(
            ROOT / "fixtures/operation_lifecycle/valid-q3i-completed.yaml"
        )

    def candidate(self) -> dict:
        return copy.deepcopy(self.fixture)

    def test_complete_q3i_fixture_is_valid(self) -> None:
        self.assertTrue(validate_reference_fixture(self.candidate()).valid)

    def test_predecessor_chain_not_storage_order_selects_current_stage(self) -> None:
        candidate = self.candidate()
        lifecycle = candidate["operation_lifecycles"][0]
        lifecycle["transition_history"].reverse()
        self.assertEqual(derive_operation_lifecycle_stage(lifecycle), "Completed")
        self.assertTrue(validate_reference_fixture(candidate).valid)

    def test_branching_history_fails_closed(self) -> None:
        candidate = self.candidate()
        history = candidate["operation_lifecycles"][0]["transition_history"]
        branch = copy.deepcopy(history[-1])
        branch.update(
            transition_id="OP-Q3I-ALPHA-T4-BRANCH",
            predecessor_transition_ref="OP-Q3I-ALPHA-T3",
            to_stage="Aborted",
        )
        history.append(branch)
        self.assertIn(
            "OPERATION_LIFECYCLE_HISTORY_INVALID",
            validate_reference_fixture(candidate).errors,
        )

    def test_transition_time_must_follow_its_predecessor(self) -> None:
        for index, value in ((0, "not-a-time"), (2, "2026-08-08T10:00:00Z")):
            with self.subTest(index=index):
                candidate = self.candidate()
                candidate["operation_lifecycles"][0]["transition_history"][index][
                    "occurred_at"
                ] = value
                self.assertIn(
                    "OPERATION_LIFECYCLE_TRANSITION_INVALID",
                    validate_reference_fixture(candidate).errors,
                )

    def test_materialized_stage_cannot_override_history(self) -> None:
        candidate = self.candidate()
        candidate["operations"][0]["lifecycle_stage"] = "Active"
        self.assertIn(
            "OPERATION_LIFECYCLE_STAGE_MISMATCH",
            validate_reference_fixture(candidate).errors,
        )

    def test_domain_completeness_resolution_and_result_fail_safe(self) -> None:
        for mutation, error in (
            (("profile_ref", "unknown.profile@1"), "OPERATION_LIFECYCLE_COMPLETENESS_UNRESOLVED"),
            (("result", "failed"), "OPERATION_LIFECYCLE_COMPLETENESS_FAILED"),
            (("input_state", "stale"), "OPERATION_LIFECYCLE_COMPLETENESS_FAILED"),
            (("input_state", "conflicting"), "OPERATION_LIFECYCLE_COMPLETENESS_FAILED"),
        ):
            with self.subTest(error=error):
                candidate = self.candidate()
                binding = candidate["operation_lifecycles"][0]["transition_history"][0][
                    "completeness_binding"
                ]
                binding[mutation[0]] = mutation[1]
                self.assertIn(error, validate_reference_fixture(candidate).errors)

    def test_ambiguous_profile_owner_does_not_gain_authority_by_count(self) -> None:
        candidate = self.candidate()
        candidate["completeness_profiles"].append(
            {
                "profile_ref": "synthetic.operation-minimum@1",
                "profile_owner_ref": "domain://second-owner",
            }
        )
        self.assertIn(
            "OPERATION_LIFECYCLE_COMPLETENESS_UNRESOLVED",
            validate_reference_fixture(candidate).errors,
        )

    def test_authorization_binding_is_exact_evidence_not_permission(self) -> None:
        for field, value in (
            ("subject_operation_ref", "OP-Q3I-BRAVO"),
            ("input_state", "stale"),
            ("input_state", "conflicting"),
        ):
            with self.subTest(field=field, value=value):
                candidate = self.candidate()
                binding = candidate["operation_lifecycles"][0]["transition_history"][1][
                    "authorization_evidence_binding"
                ]
                binding[field] = value
                self.assertIn(
                    "OPERATION_LIFECYCLE_AUTHORIZATION_INVALID",
                    validate_reference_fixture(candidate).errors,
                )

    def test_unknown_authorization_owner_fails_closed(self) -> None:
        candidate = self.candidate()
        candidate["authorization_evidence_sources"].append(
            {
                "source_contract_ref": "synthetic.authorization-evidence@1",
                "source_owner_ref": "domain://second-owner",
            }
        )
        self.assertIn(
            "OPERATION_LIFECYCLE_AUTHORIZATION_UNRESOLVED",
            validate_reference_fixture(candidate).errors,
        )

    def test_terminal_alignment_does_not_mutate_effective_assignment(self) -> None:
        candidate = self.candidate()
        assignment = candidate["assignments"][0]
        self.assertTrue(assignment_effective_at(assignment, "2026-08-08T12:00:00Z"))
        self.assertTrue(validate_reference_fixture(candidate).valid)
        self.assertEqual(assignment["lifecycle_stage"], "Established")

    def test_terminal_alignment_rejects_wrong_disposition(self) -> None:
        candidate = self.candidate()
        disposition = candidate["operation_lifecycles"][0]["transition_history"][-1][
            "assignment_alignment"
        ]["dispositions"][0]
        disposition["disposition"] = "not_effective_at_transition"
        self.assertIn(
            "OPERATION_LIFECYCLE_ASSIGNMENT_ALIGNMENT_INVALID",
            validate_reference_fixture(candidate).errors,
        )

    def test_io2_has_no_independent_record_fields(self) -> None:
        candidate = self.candidate()
        relation = candidate["operations"][0]["inter_operation_relationships"][0]
        relation["relationship_id"] = "REL-Q3I-001"
        self.assertIn(
            "OPERATION_Q3I_RELATION_FORBIDDEN_INDEPENDENT_RECORD",
            validate_reference_fixture(candidate).errors,
        )

    def test_io2_target_resolution_and_duplicate_tuple_are_exact(self) -> None:
        candidate = self.candidate()
        relation = candidate["operations"][0]["inter_operation_relationships"][0]
        relation["target_operation_ref"] = "OP-Q3I-UNKNOWN"
        self.assertIn(
            "OPERATION_Q3I_RELATION_TARGET_UNRESOLVED",
            validate_reference_fixture(candidate).errors,
        )

        candidate = self.candidate()
        relations = candidate["operations"][0]["inter_operation_relationships"]
        relations.append(copy.deepcopy(relations[0]))
        self.assertIn(
            "OPERATION_Q3I_RELATION_DUPLICATE",
            validate_reference_fixture(candidate).errors,
        )

    def test_parent_child_graph_is_exact_and_acyclic(self) -> None:
        candidate = self.candidate()
        candidate["operations"][0]["parent_operation_ref"] = "OP-Q3I-BRAVO"
        candidate["operations"][1]["parent_operation_ref"] = "OP-Q3I-ALPHA"
        self.assertIn(
            "OPERATION_Q3I_COMPOSITION_CYCLE",
            validate_reference_fixture(candidate).errors,
        )

    def test_f1_v1_require_distinct_fixed_kinds_and_provenance(self) -> None:
        candidate = self.candidate()
        intent = candidate["operations"][0]["explicit_intent_record"]
        intent.pop("authoring_provenance_ref")
        intent["validation_records"][0]["record_kind_ref"] = "generic-record@1"
        self.assertIn(
            "OPERATION_Q3I_INTENT_CONFORMANCE_INVALID",
            validate_reference_fixture(candidate).errors,
        )

    def test_record_identity_is_unique_across_f1_v1(self) -> None:
        candidate = self.candidate()
        intent = candidate["operations"][0]["explicit_intent_record"]
        intent["validation_records"][0]["validation_id"] = intent["intent_id"]
        self.assertIn(
            "OPERATION_Q3I_RECORD_ID_DUPLICATE",
            validate_reference_fixture(candidate).errors,
        )

    def test_forbidden_conclusions_do_not_enter_lifecycle_evidence(self) -> None:
        for location in ("operation", "lifecycle"):
            with self.subTest(location=location):
                candidate = self.candidate()
                owner = (
                    candidate["operations"][0]
                    if location == "operation"
                    else candidate["operation_lifecycles"][0]
                )
                owner["readiness"] = "ready"
                self.assertIn(
                    "OPERATION_LIFECYCLE_FORBIDDEN_COUPLING",
                    validate_reference_fixture(candidate).errors,
                )

    def test_legacy_operation_fixture_replays_under_prior_contract(self) -> None:
        legacy = load_fixture(ROOT / "fixtures/operation/valid-planned-explicit-intent.yaml")
        self.assertTrue(validate_reference_fixture(legacy).valid)
        self.assertNotIn("operation_contract_ref", legacy["entity"])

    def test_manifest_is_complete(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "operation-lifecycle-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"] for item in rules if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {
            item["id"] for item in rules if item.get("kind") == "derivation"
        }
        self.assertEqual(validation_ids, set(OPERATION_LIFECYCLE_ERROR_CODES))
        self.assertEqual(
            derivation_ids, set(OPERATION_LIFECYCLE_DERIVATION_RULES)
        )


if __name__ == "__main__":
    unittest.main()
