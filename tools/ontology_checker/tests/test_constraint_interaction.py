from __future__ import annotations

import copy
import itertools
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    derive_constraint_application_order_boundary,
    derive_constraint_override_boundary,
    derive_contextual_waiver_boundary,
    load_fixture,
    validate_reference_fixture,
)
from ocp_checker import constraint_interaction  # noqa: E402
from ocp_checker.constraint_interaction import (  # noqa: E402
    APPLICATION_REQUEST_FIELDS,
    CONSTRAINT_INTERACTION_DERIVATION_RULES,
    CONSTRAINT_INTERACTION_ERROR_CODES,
    INPUT_FIELDS,
    OVERRIDE_REQUEST_FIELDS,
    WAIVER_REQUEST_FIELDS,
)


EXPECTED_PRECEDENCE_FIELDS = frozenset(
    {
        "precedence_timestamp",
        "precedence_record_order",
        "precedence_source_count",
        "precedence_issuer_count",
        "precedence_caller_identity",
        "precedence_provenance_label",
        "precedence_operation_relation_value",
    }
)
EXPECTED_CONVENIENCE_OVERRIDE_FIELDS = frozenset({"convenience_override"})
EXPECTED_OCP018_TAKEOVER_FIELDS = frozenset(
    {
        "operation_authorization_level_order",
        "operation_authorization_derivation_override",
    }
)
EXPECTED_WAIVER_BYPASS_FIELDS = frozenset(
    {
        "waiver_ref",
        "exception_ref",
        "exception_label",
        "producer_bypass",
        "policy_ref",
        "authority_ref",
        "approval_ref",
    }
)
EXPECTED_POSITIVE_RESULTS = frozenset(
    {"precedence_established", "override_effective", "waiver_granted"}
)
DEFENSIVE_FIXTURE_NAMES = {
    "precedence_timestamp": "invalid-precedence-timestamp",
    "precedence_record_order": "invalid-precedence-record-order",
    "precedence_source_count": "invalid-precedence-source-count",
    "precedence_issuer_count": "invalid-precedence-issuer-count",
    "precedence_caller_identity": "invalid-precedence-caller-identity",
    "precedence_provenance_label": "invalid-precedence-provenance-label",
    "precedence_operation_relation_value": "invalid-precedence-operation-relation-value",
    "convenience_override": "invalid-convenience-override",
    "operation_authorization_level_order": "invalid-ocp018-level-order-takeover",
    "operation_authorization_derivation_override": "invalid-ocp018-derivation-takeover",
    "waiver_ref": "invalid-waiver-ref",
    "exception_ref": "invalid-exception-ref",
    "exception_label": "invalid-exception-label",
    "producer_bypass": "invalid-producer-bypass",
    "policy_ref": "invalid-policy-ref",
    "authority_ref": "invalid-authority-ref",
    "approval_ref": "invalid-approval-ref",
    "precedence_established": "invalid-positive-precedence-result",
    "override_effective": "invalid-positive-override-result",
    "waiver_granted": "invalid-positive-waiver-result",
}


class ConstraintInteractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fixture_root = ROOT / "fixtures/constraint_interaction"
        cls.fixtures = {
            path.stem: load_fixture(path) for path in sorted(fixture_root.glob("*.yaml"))
        }

    def test_all_three_negative_contracts_are_distinct_and_valid(self) -> None:
        cases = {
            "valid-application-order-not-established": (
                "application_order",
                "constraint-application-order-boundary@1",
                "constraint_application_order_not_established",
                derive_constraint_application_order_boundary,
            ),
            "valid-override-not-established": (
                "override",
                "constraint-override-boundary@1",
                "constraint_override_not_established",
                derive_constraint_override_boundary,
            ),
            "valid-waiver-not-established": (
                "contextual_waiver",
                "constraint-waiver-boundary@1",
                "contextual_waiver_not_established",
                derive_contextual_waiver_boundary,
            ),
        }
        self.assertEqual(
            {name for name, fixture in self.fixtures.items() if fixture["expected"]["valid"]},
            set(cases),
        )
        for name, (kind, rule_ref, expected_result, derivation) in cases.items():
            with self.subTest(fixture=name):
                fixture = self.fixtures[name]
                request = fixture["dataset"]["interaction_request"]
                self.assertTrue(validate_reference_fixture(fixture).valid)
                self.assertEqual(request["interaction_kind"], kind)
                self.assertEqual(request["rule_ref"], rule_ref)
                self.assertEqual(request["stored_result"], expected_result)
                self.assertEqual(derivation(fixture["dataset"]), expected_result)

    def test_all_34_fixtures_match_exact_expected_errors(self) -> None:
        self.assertEqual(len(self.fixtures), 34)
        for name, fixture in self.fixtures.items():
            with self.subTest(fixture=name):
                validation = validate_reference_fixture(fixture)
                self.assertEqual(validation.valid, bool(fixture["expected"]["valid"]))
                self.assertEqual(
                    set(validation.errors),
                    set(fixture["expected"].get("error_codes", [])),
                )

    def test_application_order_is_permutation_and_provenance_invariant(self) -> None:
        original = self.fixtures["valid-application-order-not-established"]
        dataset = original["dataset"]
        expected = "constraint_application_order_not_established"
        refs = dataset["interaction_request"]["constraint_version_refs"]
        inputs = dataset["constraint_application_inputs"]
        for ref_order in itertools.permutations(refs):
            for input_order in itertools.permutations(inputs):
                with self.subTest(refs=ref_order, inputs=[x["constraint_version_ref"] for x in input_order]):
                    candidate = copy.deepcopy(original)
                    candidate["dataset"]["interaction_request"]["constraint_version_refs"] = list(ref_order)
                    candidate["dataset"]["constraint_application_inputs"] = list(input_order)
                    self.assertTrue(validate_reference_fixture(candidate).valid)
                    self.assertEqual(
                        derive_constraint_application_order_boundary(candidate["dataset"]),
                        expected,
                    )

        changed_provenance = copy.deepcopy(original)
        for index, item in enumerate(changed_provenance["dataset"]["constraint_application_inputs"]):
            item["provenance_ref"] = f"PROVENANCE-SYNTH-CHANGED-{index}"
        self.assertTrue(validate_reference_fixture(changed_provenance).valid)
        self.assertEqual(
            derive_constraint_application_order_boundary(changed_provenance["dataset"]),
            expected,
        )

    def test_contracts_are_non_interchangeable_and_never_positive(self) -> None:
        derivations = {
            "application_order": derive_constraint_application_order_boundary,
            "override": derive_constraint_override_boundary,
            "contextual_waiver": derive_contextual_waiver_boundary,
        }
        valid_names = [
            "valid-application-order-not-established",
            "valid-override-not-established",
            "valid-waiver-not-established",
        ]
        for name in valid_names:
            dataset = self.fixtures[name]["dataset"]
            own_kind = dataset["interaction_request"]["interaction_kind"]
            for kind, derivation in derivations.items():
                with self.subTest(fixture=name, derivation=kind):
                    result = derivation(dataset)
                    if kind == own_kind:
                        self.assertEqual(result, constraint_interaction.NEGATIVE_RESULTS[kind])
                    else:
                        self.assertEqual(result, "indeterminate")

        self.assertTrue(EXPECTED_POSITIVE_RESULTS.isdisjoint(constraint_interaction.DERIVED_RESULTS))
        for name, fixture in self.fixtures.items():
            if fixture["expected"]["valid"]:
                continue
            for derivation in derivations.values():
                with self.subTest(fixture=name, derivation=derivation.__name__):
                    self.assertNotIn(derivation(fixture.get("dataset")), EXPECTED_POSITIVE_RESULTS)

    def test_every_contract_declared_element_is_live(self) -> None:
        valid_by_kind = {
            "application_order": self.fixtures["valid-application-order-not-established"],
            "override": self.fixtures["valid-override-not-established"],
            "contextual_waiver": self.fixtures["valid-waiver-not-established"],
        }
        original_kinds = constraint_interaction.INTERACTION_KINDS
        original_rules = dict(constraint_interaction.RULE_REFS)
        original_results = dict(constraint_interaction.NEGATIVE_RESULTS)
        original_states = constraint_interaction.EVIDENCE_STATES
        try:
            for kind, fixture in valid_by_kind.items():
                constraint_interaction.INTERACTION_KINDS = original_kinds - {kind}
                self.assertFalse(validate_reference_fixture(fixture).valid, kind)
                constraint_interaction.INTERACTION_KINDS = original_kinds

                constraint_interaction.RULE_REFS[kind] = "rule-synth-mutated@1"
                self.assertFalse(validate_reference_fixture(fixture).valid, kind)
                constraint_interaction.RULE_REFS = dict(original_rules)

                constraint_interaction.NEGATIVE_RESULTS[kind] = "negative_synth_mutated"
                self.assertFalse(validate_reference_fixture(fixture).valid, kind)
                constraint_interaction.NEGATIVE_RESULTS = dict(original_results)

            field_sets = {
                "application_order": APPLICATION_REQUEST_FIELDS,
                "override": OVERRIDE_REQUEST_FIELDS,
                "contextual_waiver": WAIVER_REQUEST_FIELDS,
            }
            for kind, fields in field_sets.items():
                for field in fields:
                    with self.subTest(kind=kind, request_field=field):
                        candidate = copy.deepcopy(valid_by_kind[kind])
                        del candidate["dataset"]["interaction_request"][field]
                        self.assertFalse(validate_reference_fixture(candidate).valid)

            for field in INPUT_FIELDS:
                with self.subTest(input_field=field):
                    candidate = copy.deepcopy(valid_by_kind["override"])
                    del candidate["dataset"]["constraint_application_inputs"][0][field]
                    self.assertFalse(validate_reference_fixture(candidate).valid)

            for field in constraint_interaction.DATASET_FIELDS:
                with self.subTest(dataset_field=field):
                    candidate = copy.deepcopy(valid_by_kind["override"])
                    del candidate["dataset"][field]
                    self.assertFalse(validate_reference_fixture(candidate).valid)

            constraint_interaction.EVIDENCE_STATES = original_states - {"current"}
            self.assertFalse(validate_reference_fixture(valid_by_kind["override"]).valid)
            constraint_interaction.EVIDENCE_STATES = original_states - {"stale"}
            self.assertNotEqual(
                set(validate_reference_fixture(self.fixtures["invalid-stale-input"]).errors),
                set(self.fixtures["invalid-stale-input"]["expected"]["error_codes"]),
            )
        finally:
            constraint_interaction.INTERACTION_KINDS = original_kinds
            constraint_interaction.RULE_REFS = original_rules
            constraint_interaction.NEGATIVE_RESULTS = original_results
            constraint_interaction.EVIDENCE_STATES = original_states

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            (
                "PRECEDENCE_SELECTOR_FIELDS",
                EXPECTED_PRECEDENCE_FIELDS,
                "CONSTRAINT_INTERACTION_PRECEDENCE_SELECTOR_FORBIDDEN",
                "valid-application-order-not-established",
            ),
            (
                "CONVENIENCE_OVERRIDE_FIELDS",
                EXPECTED_CONVENIENCE_OVERRIDE_FIELDS,
                "CONSTRAINT_INTERACTION_CONVENIENCE_OVERRIDE_FORBIDDEN",
                "valid-override-not-established",
            ),
            (
                "OCP018_TAKEOVER_FIELDS",
                EXPECTED_OCP018_TAKEOVER_FIELDS,
                "CONSTRAINT_INTERACTION_OCP018_TAKEOVER_FORBIDDEN",
                "valid-override-not-established",
            ),
            (
                "WAIVER_BYPASS_FIELDS",
                EXPECTED_WAIVER_BYPASS_FIELDS,
                "CONSTRAINT_INTERACTION_WAIVER_BYPASS_FORBIDDEN",
                "valid-waiver-not-established",
            ),
        )
        for attr, expected_values, error_code, valid_name in categories:
            original = getattr(constraint_interaction, attr)
            self.assertEqual(original, expected_values)
            try:
                for value in expected_values:
                    with self.subTest(category=attr, value=value):
                        direct_fixture = self.fixtures[DEFENSIVE_FIXTURE_NAMES[value]]
                        direct_request = direct_fixture["dataset"]["interaction_request"]
                        self.assertIn(value, direct_request)
                        self.assertNotIn(direct_request[value], (None, False, "", [], {}))
                        self.assertIn(
                            error_code,
                            validate_reference_fixture(direct_fixture).errors,
                        )
                        candidate = copy.deepcopy(self.fixtures[valid_name])
                        request = candidate["dataset"]["interaction_request"]
                        request["stored_result"] = "indeterminate"
                        request[value] = f"SYNTH-{value.upper()}"
                        self.assertIn(error_code, validate_reference_fixture(candidate).errors)
                        setattr(constraint_interaction, attr, original - {value})
                        self.assertNotIn(error_code, validate_reference_fixture(candidate).errors)
                        setattr(constraint_interaction, attr, original)
            finally:
                setattr(constraint_interaction, attr, original)

        original_positive = constraint_interaction.POSITIVE_RESULTS
        self.assertEqual(original_positive, EXPECTED_POSITIVE_RESULTS)
        result_fixtures = {
            "precedence_established": "valid-application-order-not-established",
            "override_effective": "valid-override-not-established",
            "waiver_granted": "valid-waiver-not-established",
        }
        try:
            for value, valid_name in result_fixtures.items():
                with self.subTest(positive_result=value):
                    direct_fixture = self.fixtures[DEFENSIVE_FIXTURE_NAMES[value]]
                    self.assertEqual(
                        direct_fixture["dataset"]["interaction_request"]["stored_result"],
                        value,
                    )
                    candidate = copy.deepcopy(self.fixtures[valid_name])
                    candidate["dataset"]["interaction_request"]["stored_result"] = value
                    self.assertIn(
                        "CONSTRAINT_INTERACTION_POSITIVE_RESULT_FORBIDDEN",
                        validate_reference_fixture(candidate).errors,
                    )
                    constraint_interaction.POSITIVE_RESULTS = original_positive - {value}
                    self.assertNotIn(
                        "CONSTRAINT_INTERACTION_POSITIVE_RESULT_FORBIDDEN",
                        validate_reference_fixture(candidate).errors,
                    )
                    constraint_interaction.POSITIVE_RESULTS = original_positive
        finally:
            constraint_interaction.POSITIVE_RESULTS = original_positive

    def test_manifest_matches_exported_rules_and_complete_fixture_coverage(self) -> None:
        manifest = yaml.safe_load(
            (ROOT / "constraint-interaction-rules.yaml").read_text(encoding="utf-8")
        )
        self.assertEqual(
            manifest["fixture_coverage"],
            {"status": "complete", "concept": "ConstraintInteractionDataset"},
        )
        validation_ids = {
            item["id"]
            for item in manifest["rules"]
            if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {
            item["id"] for item in manifest["rules"] if item.get("kind") == "derivation"
        }
        self.assertEqual(validation_ids, set(CONSTRAINT_INTERACTION_ERROR_CODES))
        self.assertEqual(derivation_ids, set(CONSTRAINT_INTERACTION_DERIVATION_RULES))


if __name__ == "__main__":
    unittest.main()
