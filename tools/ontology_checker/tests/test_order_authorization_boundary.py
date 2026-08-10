from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    derive_order_authorization_boundary,
    load_fixture,
    validate_reference_fixture,
)
from ocp_checker import order_authorization_boundary  # noqa: E402
from ocp_checker.order_authorization_boundary import (  # noqa: E402
    AUTHORIZATION_SNAPSHOT_FIELDS,
    DATASET_FIELDS,
    ORDER_AUTHORIZATION_BOUNDARY_DERIVATION_RULES,
    ORDER_AUTHORIZATION_BOUNDARY_ERROR_CODES,
    REQUEST_FIELDS,
)


EXPECTED_POSITIVE_AUTHORITY_FIELDS = frozenset(
    {
        "order_required",
        "order_sufficient",
        "order_admissible",
        "authorization_established",
        "permission_granted",
    }
)
EXPECTED_CONCEPT_COUPLING_FIELDS = frozenset(
    {"order_concept_ref", "concept_status", "registry_entry", "graph_edge"}
)
EXPECTED_CONVENIENCE_SELECTOR_FIELDS = frozenset(
    {"newest_timestamp", "record_order", "source_count", "issuer_count", "caller_identity"}
)
EXPECTED_SELF_SUPPLY_FIELDS = frozenset({"activation_attempt"})
EXPECTED_FORBIDDEN_FIELDS = frozenset(
    {
        "authority_concept_ref",
        "approval_concept_ref",
        "policy_concept_ref",
        "lifecycle_stage",
        "assignment_mutation",
        "production_profile",
    }
)
DEFENSIVE_FIXTURE_NAMES = {
    "order_required": "invalid-positive-authority",
    "order_sufficient": "invalid-positive-order-sufficient",
    "order_admissible": "invalid-positive-order-admissible",
    "authorization_established": "invalid-positive-authorization-established",
    "permission_granted": "invalid-positive-permission-granted",
    "order_concept_ref": "invalid-concept-coupling",
    "concept_status": "invalid-concept-status",
    "registry_entry": "invalid-registry-entry",
    "graph_edge": "invalid-graph-edge",
    "newest_timestamp": "invalid-newest-timestamp",
    "record_order": "invalid-record-order",
    "source_count": "invalid-convenience-selector",
    "issuer_count": "invalid-issuer-count",
    "caller_identity": "invalid-caller-identity",
    "activation_attempt": "invalid-self-supply",
    "authority_concept_ref": "invalid-authority-concept-ref",
    "approval_concept_ref": "invalid-approval-concept-ref",
    "policy_concept_ref": "invalid-policy-concept-ref",
    "lifecycle_stage": "invalid-lifecycle-stage",
    "assignment_mutation": "invalid-forbidden-coupling",
    "production_profile": "invalid-production-profile",
}


class OrderAuthorizationBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = ROOT / "fixtures/order_authorization_boundary"
        cls.fixtures = {
            path.stem: load_fixture(path) for path in sorted(fixture_root.glob("*.yaml"))
        }

    def test_all_three_questions_have_distinct_valid_negative_results(self) -> None:
        valid = {
            name: fixture
            for name, fixture in self.fixtures.items()
            if fixture["expected"]["valid"]
        }
        self.assertEqual(len(valid), 3)
        observed = {
            (
                fixture["dataset"]["boundary_request"]["question"],
                fixture["dataset"]["boundary_request"]["stored_result"],
            )
            for fixture in valid.values()
        }
        self.assertEqual(observed, set(order_authorization_boundary.NEGATIVE_RESULTS.items()))
        for name, fixture in valid.items():
            with self.subTest(fixture=name):
                self.assertEqual(
                    derive_order_authorization_boundary(fixture["dataset"]),
                    fixture["dataset"]["boundary_request"]["stored_result"],
                )

    def test_all_fixtures_match_exact_expected_errors(self) -> None:
        self.assertEqual(len(self.fixtures), 35)
        for name, fixture in self.fixtures.items():
            with self.subTest(fixture=name):
                validation = validate_reference_fixture(fixture)
                self.assertEqual(validation.valid, bool(fixture["expected"]["valid"]))
                self.assertEqual(
                    set(validation.errors),
                    set(fixture["expected"].get("error_codes", [])),
                )

    def test_every_invalid_fixture_fails_safe(self) -> None:
        permissive = {
            "order_required",
            "order_sufficient",
            "order_admissible",
            "authorization_established",
            "permission_granted",
        }
        self.assertTrue(permissive.isdisjoint(order_authorization_boundary.DERIVED_RESULTS))
        for name, fixture in self.fixtures.items():
            if fixture["expected"]["valid"] or name == "invalid-result-mismatch":
                continue
            with self.subTest(fixture=name):
                self.assertEqual(
                    derive_order_authorization_boundary(fixture.get("dataset")),
                    "indeterminate",
                )
        mismatch = self.fixtures["invalid-result-mismatch"]["dataset"]
        self.assertNotEqual(
            derive_order_authorization_boundary(mismatch),
            mismatch["boundary_request"]["stored_result"],
        )

    def test_unreferenced_snapshots_and_order_do_not_select_authority(self) -> None:
        dataset = copy.deepcopy(self.fixtures["valid-admissible-not-established"]["dataset"])
        expected = derive_order_authorization_boundary(dataset)
        dataset["authorization_snapshots"].reverse()
        self.assertEqual(derive_order_authorization_boundary(dataset), expected)
        dataset["authorization_snapshots"].append(
            {
                "snapshot_ref": "SNAPSHOT-SYNTH-EXTRA",
                "subject_operation_ref": "OPERATION-SYNTH-EXTRA",
                "source_contract_ref": "OCP-018@0.2.1",
                "source_owner_ref": "OWNER-SYNTH-EXTRA",
                "input_snapshot_ref": "INPUT-SYNTH-EXTRA",
                "evaluation_context_ref": "CONTEXT-SYNTH-EXTRA",
                "evidence_state": "current",
                "source_result": "denied",
                "order_candidate_ref": "ORDER-CANDIDATE-SYNTH-EXTRA",
            }
        )
        self.assertEqual(derive_order_authorization_boundary(dataset), expected)

    def test_every_declared_element_and_defensive_value_is_live(self) -> None:
        valid_by_question = {
            fixture["dataset"]["boundary_request"]["question"]: fixture
            for fixture in self.fixtures.values()
            if fixture["expected"]["valid"]
        }
        mandatory = self.fixtures["valid-mandatory-not-established"]
        sufficient = self.fixtures["valid-sufficient-not-established"]

        original_questions = order_authorization_boundary.QUESTIONS
        original_rules = dict(order_authorization_boundary.RULE_REFS)
        original_results = dict(order_authorization_boundary.NEGATIVE_RESULTS)
        original_contract = order_authorization_boundary.SOURCE_CONTRACT_REF
        original_source_results = order_authorization_boundary.SOURCE_RESULTS
        defensive_categories = (
            (
                "POSITIVE_AUTHORITY_FIELDS",
                EXPECTED_POSITIVE_AUTHORITY_FIELDS,
                "ORDER_AUTHORIZATION_BOUNDARY_POSITIVE_AUTHORITY_FORBIDDEN",
            ),
            (
                "CONCEPT_COUPLING_FIELDS",
                EXPECTED_CONCEPT_COUPLING_FIELDS,
                "ORDER_AUTHORIZATION_BOUNDARY_CONCEPT_COUPLING_FORBIDDEN",
            ),
            (
                "CONVENIENCE_SELECTOR_FIELDS",
                EXPECTED_CONVENIENCE_SELECTOR_FIELDS,
                "ORDER_AUTHORIZATION_BOUNDARY_CONVENIENCE_SELECTOR_FORBIDDEN",
            ),
            (
                "SELF_SUPPLY_FIELDS",
                EXPECTED_SELF_SUPPLY_FIELDS,
                "ORDER_AUTHORIZATION_BOUNDARY_SELF_SUPPLY_FORBIDDEN",
            ),
            (
                "FORBIDDEN_FIELDS",
                EXPECTED_FORBIDDEN_FIELDS,
                "ORDER_AUTHORIZATION_BOUNDARY_FORBIDDEN_COUPLING",
            ),
        )
        original_defensive = {
            name: getattr(order_authorization_boundary, name)
            for name, _, _ in defensive_categories
        }
        try:
            for question, fixture in valid_by_question.items():
                order_authorization_boundary.QUESTIONS = original_questions - {question}
                self.assertFalse(validate_reference_fixture(fixture).valid, question)
                order_authorization_boundary.QUESTIONS = original_questions

                order_authorization_boundary.RULE_REFS[question] = "RULE-SYNTH-MUTATED@1"
                self.assertFalse(validate_reference_fixture(fixture).valid, question)
                order_authorization_boundary.RULE_REFS = dict(original_rules)

                order_authorization_boundary.NEGATIVE_RESULTS[question] = (
                    "negative_result_synth_mutated"
                )
                self.assertFalse(validate_reference_fixture(fixture).valid, question)
                order_authorization_boundary.NEGATIVE_RESULTS = dict(original_results)

            order_authorization_boundary.SOURCE_CONTRACT_REF = "OCP-SYNTH-MUTATED@1"
            self.assertFalse(validate_reference_fixture(mandatory).valid)
            order_authorization_boundary.SOURCE_CONTRACT_REF = original_contract

            for source_result, fixture in (("accepted", mandatory), ("denied", sufficient)):
                order_authorization_boundary.SOURCE_RESULTS = original_source_results - {
                    source_result
                }
                self.assertFalse(validate_reference_fixture(fixture).valid, source_result)
                order_authorization_boundary.SOURCE_RESULTS = original_source_results

            for field in REQUEST_FIELDS:
                candidate = copy.deepcopy(mandatory)
                del candidate["dataset"]["boundary_request"][field]
                self.assertFalse(validate_reference_fixture(candidate).valid, field)
            for field in DATASET_FIELDS:
                candidate = copy.deepcopy(mandatory)
                del candidate["dataset"][field]
                self.assertFalse(validate_reference_fixture(candidate).valid, field)
            for field in AUTHORIZATION_SNAPSHOT_FIELDS:
                candidate = copy.deepcopy(mandatory)
                del candidate["dataset"]["authorization_snapshots"][0][field]
                self.assertFalse(validate_reference_fixture(candidate).valid, field)

            for set_name, expected_values, error_code in defensive_categories:
                original_values = original_defensive[set_name]
                self.assertEqual(original_values, expected_values)
                for field in expected_values:
                    candidate = copy.deepcopy(mandatory)
                    candidate["dataset"]["claims"] = {field: "VALUE-SYNTH-LIVE"}
                    direct_fixture = self.fixtures[DEFENSIVE_FIXTURE_NAMES[field]]
                    self.assertIn(field, direct_fixture["dataset"]["claims"])
                    self.assertNotIn(
                        direct_fixture["dataset"]["claims"][field],
                        (None, False, "", [], {}),
                    )
                    self.assertIn(error_code, validate_reference_fixture(direct_fixture).errors)
                    self.assertIn(error_code, validate_reference_fixture(candidate).errors)
                    setattr(
                        order_authorization_boundary,
                        set_name,
                        original_values - {field},
                    )
                    self.assertNotIn(
                        error_code,
                        validate_reference_fixture(candidate).errors,
                    )
                    setattr(order_authorization_boundary, set_name, original_values)
        finally:
            order_authorization_boundary.QUESTIONS = original_questions
            order_authorization_boundary.RULE_REFS = original_rules
            order_authorization_boundary.NEGATIVE_RESULTS = original_results
            order_authorization_boundary.SOURCE_CONTRACT_REF = original_contract
            order_authorization_boundary.SOURCE_RESULTS = original_source_results
            for name, values in original_defensive.items():
                setattr(order_authorization_boundary, name, values)

    def test_manifest_matches_rules_and_complete_fixture_coverage(self) -> None:
        manifest = yaml.safe_load(
            (ROOT / "order-authorization-boundary-rules.yaml").read_text(encoding="utf-8")
        )
        rules = manifest["rules"]
        validation_ids = {
            item["id"] for item in rules if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {item["id"] for item in rules if item.get("kind") == "derivation"}
        observed = {
            code
            for fixture in self.fixtures.values()
            for code in fixture["expected"].get("error_codes", [])
        }
        self.assertEqual(validation_ids, set(ORDER_AUTHORIZATION_BOUNDARY_ERROR_CODES))
        self.assertEqual(derivation_ids, set(ORDER_AUTHORIZATION_BOUNDARY_DERIVATION_RULES))
        self.assertEqual(observed, validation_ids)
        self.assertEqual(
            manifest["fixture_coverage"],
            {"status": "complete", "concept": "OrderAuthorizationBoundaryDataset"},
        )


if __name__ == "__main__":
    unittest.main()
