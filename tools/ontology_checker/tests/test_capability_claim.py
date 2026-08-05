from __future__ import annotations

from copy import deepcopy
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    capability_claim_heads,
    derive_capability_claim_support_usability,
    effective_capability_claim,
    load_fixture,
    resolve_capability_claim,
    validate_reference_fixture,
)
from ocp_checker.capability_claim import (  # noqa: E402
    CAPABILITY_CLAIM_DERIVATION_RULES,
    CAPABILITY_CLAIM_ERROR_CODES,
)


CAPABILITY_REF = {
    "namespace": "mobility",
    "capability_id": "navigate",
    "version": "v1",
}


class CapabilityClaimContractTests(unittest.TestCase):
    def _fixture(self, name: str) -> dict:
        return load_fixture(ROOT / "fixtures/capability_claim" / name)

    @staticmethod
    def _derive(fixture: dict, *, query_time: str | None = None) -> dict:
        return derive_capability_claim_support_usability(
            fixture["claims"][0],
            freshness_rules=fixture.get("freshness_rules") or [],
            ambiguity_rules=fixture.get("ambiguity_rules") or [],
            evidence_expectations=fixture.get("evidence_expectations") or [],
            evidence_snapshots=fixture.get("evidence_snapshots") or [],
            input_snapshots=fixture.get("input_snapshots") or [],
            events=fixture.get("events") or [],
            observations=fixture.get("observations") or [],
            assessments=fixture.get("assessments") or [],
            query_time=query_time,
        )

    @staticmethod
    def _activated_projection(fixture: dict) -> str:
        return effective_capability_claim(
            fixture["claims"],
            holder_ref=fixture["resources"][0]["resource_id"],
            capability_ref=CAPABILITY_REF,
            claimant_ref=fixture["claims"][0]["claimant_ref"],
            claim_kind_ref="holder-capability@2",
            condition_set_ref=fixture["claims"][0]["condition_set_ref"],
            at="2026-08-05T02:00:00Z",
            resources=fixture.get("resources") or [],
            capabilities=fixture.get("capabilities") or [],
            events=fixture.get("events") or [],
            observations=fixture.get("observations") or [],
            assessments=fixture.get("assessments") or [],
            evidence_snapshots=fixture.get("evidence_snapshots") or [],
            input_snapshots=fixture.get("input_snapshots") or [],
            freshness_rules=fixture.get("freshness_rules") or [],
            ambiguity_rules=fixture.get("ambiguity_rules") or [],
            evidence_expectations=fixture.get("evidence_expectations") or [],
        )

    def test_activated_declaration_preserves_narrow_attribution(self) -> None:
        fixture = self._fixture("valid-activated-declaration.yaml")
        self.assertTrue(validate_reference_fixture(fixture).valid)
        claim = fixture["claims"][0]
        self.assertEqual(claim["support_mode"], "declaration-only")
        self.assertNotIn("freshness_state", claim)
        self.assertEqual(self._activated_projection(fixture), "positive")

    def test_activated_cutoff_equality_is_fresh_and_replayable(self) -> None:
        fixture = self._fixture("valid-activated-fresh.yaml")
        self.assertTrue(validate_reference_fixture(fixture).valid)
        first = self._derive(fixture)
        self.assertEqual(first, self._derive(fixture))
        self.assertEqual(first["freshness_state"], "fresh")
        self.assertEqual(first["ambiguity_state"], "clear")

    def test_activated_projection_requires_complete_exact_context(self) -> None:
        fixture = self._fixture("valid-activated-fresh.yaml")
        claim = fixture["claims"][0]
        without_context = effective_capability_claim(
            fixture["claims"],
            holder_ref=claim["holder_ref"],
            capability_ref=CAPABILITY_REF,
            claimant_ref=claim["claimant_ref"],
            claim_kind_ref="holder-capability@2",
            condition_set_ref=claim["condition_set_ref"],
            at="2026-08-05T02:00:00Z",
        )
        self.assertEqual(without_context, "indeterminate")
        self.assertEqual(self._activated_projection(fixture), "positive")

    def test_explicit_later_query_does_not_mutate_historical_support(self) -> None:
        fixture = self._fixture("valid-activated-fresh.yaml")
        later = self._derive(fixture, query_time="2026-08-05T02:00:00.000001Z")
        self.assertEqual(later["freshness_state"], "stale")
        self.assertEqual(fixture["claims"][0]["freshness_state"], "fresh")
        self.assertEqual(fixture["claims"][0]["support_state"], "sufficient")

    def test_missing_evidence_is_not_relabelled_as_declaration_only(self) -> None:
        fixture = self._fixture("valid-activated-missing.yaml")
        self.assertTrue(validate_reference_fixture(fixture).valid)
        self.assertEqual(self._derive(fixture)["freshness_state"], "not_applicable")
        self.assertEqual(fixture["claims"][0]["support_state"], "missing")
        self.assertEqual(self._activated_projection(fixture), "indeterminate")

    def test_future_temporal_fact_is_non_permissive_ambiguity(self) -> None:
        fixture = self._fixture("valid-activated-temporal-ambiguity.yaml")
        self.assertTrue(validate_reference_fixture(fixture).valid)
        derived = self._derive(fixture)
        self.assertEqual(derived["freshness_state"], "indeterminate")
        self.assertEqual(
            derived["ambiguity_findings"][0]["reason_ref"],
            "temporal-fact-future@1",
        )
        self.assertEqual(self._activated_projection(fixture), "indeterminate")

    def test_same_evidence_can_be_fresh_under_a_different_exact_rule(self) -> None:
        fixture = self._fixture("valid-activated-stale.yaml")
        self.assertEqual(self._derive(fixture)["freshness_state"], "stale")
        alternate = deepcopy(fixture)
        claim = alternate["claims"][0]
        claim["freshness_rule_ref"] = "holder-capability-freshness.long-window@1"
        rule = alternate["freshness_rules"][0]
        rule["rule_ref"] = claim["freshness_rule_ref"]
        observation_policy = next(
            policy
            for policy in rule["evidence_policies"]
            if policy["evidence_kind_ref"] == "observation-record@1"
        )
        observation_policy["max_age_seconds"] = 601
        alternate["input_snapshots"][0]["freshness_rule_ref"] = claim[
            "freshness_rule_ref"
        ]
        self.assertEqual(self._derive(alternate)["freshness_state"], "fresh")

    def test_recorded_at_never_replaces_rule_selected_observed_at(self) -> None:
        fixture = self._fixture("valid-activated-stale.yaml")
        fixture["observations"][0]["recorded_at"] = "2026-08-05T01:59:59Z"
        self.assertEqual(self._derive(fixture)["freshness_state"], "stale")

    def test_each_admitted_evidence_kind_uses_its_selected_temporal_fact(self) -> None:
        base = self._fixture("valid-activated-fresh.yaml")
        cases = (
            (
                "event@1",
                "EV-CLM2",
                "events",
                {
                    "event_id": "EV-CLM2",
                    "event_kind_ref": "capability-demonstration@1",
                    "occurred_at": "2026-08-05T01:00:00Z",
                    "registered_at": "2026-08-05T01:01:00Z",
                    "identity_provenance_ref": "ACT-EV-CLM2",
                },
            ),
            (
                "outcome-assessment-record@1",
                "ASM-CLM2",
                "assessments",
                {
                    "assessment_id": "ASM-CLM2",
                    "assessment_kind_ref": "objective-achievement@1",
                    "target_kind_ref": "objective@1",
                    "target_ref": "OBJ-CLM2",
                    "criterion_ref": "neutral.condition@1",
                    "evidence_bindings": [],
                    "evidence_snapshot_ref": "EVIDENCE-ASM-CLM2",
                    "input_snapshot_ref": "INPUT-ASM-CLM2",
                    "evidence_state": "missing",
                    "evaluator_ref": "EVALUATOR-CLM2",
                    "evaluated_at": "2026-08-05T01:30:00Z",
                    "recorded_at": "2026-08-05T01:31:00Z",
                    "conclusion": "indeterminate",
                    "provenance_ref": "ACT-ASM-CLM2",
                },
            ),
        )
        for kind_ref, record_ref, collection, record in cases:
            with self.subTest(kind_ref=kind_ref):
                fixture = deepcopy(base)
                fixture["observations"] = []
                fixture[collection] = [record]
                binding = {
                    "evidence_kind_ref": kind_ref,
                    "evidence_ref": record_ref,
                }
                fixture["claims"][0]["evidence_bindings"] = [binding]
                fixture["evidence_snapshots"][0]["evidence_bindings"] = [binding]
                self.assertEqual(self._derive(fixture)["freshness_state"], "fresh")

    def test_unavailable_or_duplicate_historical_input_fails_closed(self) -> None:
        fixture = self._fixture("valid-activated-fresh.yaml")
        missing = deepcopy(fixture)
        missing["observations"] = []
        duplicate = deepcopy(fixture)
        duplicate["evidence_snapshots"].append(
            deepcopy(duplicate["evidence_snapshots"][0])
        )
        duplicate_evidence = deepcopy(fixture)
        duplicate_evidence["observations"].append(
            deepcopy(duplicate_evidence["observations"][0])
        )
        for case in (missing, duplicate, duplicate_evidence):
            with self.subTest(case=case):
                derived = self._derive(case)
                self.assertEqual(derived["freshness_state"], "indeterminate")
                self.assertEqual(derived["ambiguity_state"], "ambiguous")

    def test_rule_and_input_snapshot_mismatch_are_rejected(self) -> None:
        fixture = self._fixture("valid-activated-fresh.yaml")
        rule_mismatch = deepcopy(fixture)
        rule_mismatch["freshness_rules"][0]["condition_set_ref"] = (
            "other-context@1"
        )
        partial_rule = deepcopy(fixture)
        partial_rule["freshness_rules"][0]["evidence_policies"].pop()
        snapshot_mismatch = deepcopy(fixture)
        snapshot_mismatch["input_snapshots"][0]["condition_set_ref"] = (
            "other-context@1"
        )
        expectation_mismatch = deepcopy(fixture)
        expectation_mismatch["evidence_expectations"][0][
            "admitted_evidence_kinds"
        ] = ["event@1"]
        self.assertIn(
            "CAPABILITY_CLAIM_FRESHNESS_RULE_INVALID",
            validate_reference_fixture(rule_mismatch).errors,
        )
        self.assertIn(
            "CAPABILITY_CLAIM_FRESHNESS_RULE_INVALID",
            validate_reference_fixture(partial_rule).errors,
        )
        self.assertIn(
            "CAPABILITY_CLAIM_INPUT_SNAPSHOT_RULE_MISMATCH",
            validate_reference_fixture(snapshot_mismatch).errors,
        )
        self.assertIn(
            "CAPABILITY_CLAIM_EVIDENCE_EXPECTATION_INVALID",
            validate_reference_fixture(expectation_mismatch).errors,
        )

    def test_legacy_and_unknown_kinds_cannot_bypass_activation(self) -> None:
        legacy = self._fixture("invalid-legacy-activation-fields.yaml")
        unknown = self._fixture("invalid-unknown-claim-kind.yaml")
        self.assertEqual(
            set(validate_reference_fixture(legacy).errors),
            {"CAPABILITY_CLAIM_ACTIVATION_FIELDS_FORBIDDEN"},
        )
        self.assertEqual(
            set(validate_reference_fixture(unknown).errors),
            {"CAPABILITY_CLAIM_KIND_UNSUPPORTED"},
        )

    def test_support_mode_is_explicit_not_inferred_from_field_presence(self) -> None:
        fixture = self._fixture("valid-activated-declaration.yaml")
        fixture["claims"][0].pop("support_mode")
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"CAPABILITY_CLAIM_SUPPORT_MODE_INVALID"},
        )

    def test_only_forward_mode_transition_with_unchanged_assertion_is_valid(self) -> None:
        forward = self._fixture("valid-activated-forward-transition.yaml")
        self.assertTrue(validate_reference_fixture(forward).valid)

        reverse = self._fixture("valid-activated-fresh.yaml")
        predecessor = reverse["claims"][0]
        successor = {
            "claim_id": "CLM2-REVERSE-B",
            "claim_kind_ref": "holder-capability@2",
            "support_mode": "declaration-only",
            "holder_kind_ref": predecessor["holder_kind_ref"],
            "holder_ref": predecessor["holder_ref"],
            "capability_ref": predecessor["capability_ref"],
            "claimant_ref": predecessor["claimant_ref"],
            "condition_set_ref": predecessor["condition_set_ref"],
            "assertion": predecessor["assertion"],
            "evidence_bindings": [],
            "support_state": "declared",
            "authority_ref": predecessor["authority_ref"],
            "effective_from": predecessor["effective_from"],
            "recorded_at": "2026-08-05T02:02:00Z",
            "provenance_ref": "ACT-CLM2-REVERSE-B",
            "supersedes_claim_ref": predecessor["claim_id"],
        }
        reverse["claims"].append(successor)
        self.assertIn(
            "CAPABILITY_CLAIM_SUPPORT_MODE_TRANSITION_INVALID",
            validate_reference_fixture(reverse).errors,
        )

        assertion_flip = deepcopy(forward)
        assertion_flip["claims"][1]["assertion"] = "negative"
        self.assertIn(
            "CAPABILITY_CLAIM_SUPPORT_MODE_TRANSITION_INVALID",
            validate_reference_fixture(assertion_flip).errors,
        )

    def test_withdrawal_preserves_mode_without_reclassifying_support(self) -> None:
        fixture = self._fixture("valid-activated-fresh.yaml")
        predecessor = fixture["claims"][0]
        withdrawal = {
            "claim_id": "CLM2-WITHDRAWN",
            "claim_kind_ref": "holder-capability@2",
            "support_mode": "evidence-backed",
            "holder_kind_ref": predecessor["holder_kind_ref"],
            "holder_ref": predecessor["holder_ref"],
            "capability_ref": predecessor["capability_ref"],
            "claimant_ref": predecessor["claimant_ref"],
            "condition_set_ref": predecessor["condition_set_ref"],
            "assertion": "withdrawn",
            "evidence_bindings": [],
            "support_state": "declared",
            "authority_ref": predecessor["authority_ref"],
            "effective_from": predecessor["effective_from"],
            "recorded_at": "2026-08-05T02:02:00Z",
            "provenance_ref": "ACT-CLM2-WITHDRAWN",
            "supersedes_claim_ref": predecessor["claim_id"],
        }
        fixture["claims"].append(withdrawal)
        self.assertTrue(validate_reference_fixture(fixture).valid)
        self.assertEqual(self._activated_projection(fixture), "withdrawn")

    def test_transition_branches_remain_visible_without_recency_selection(self) -> None:
        fixture = self._fixture("valid-activated-forward-transition.yaml")
        branch = deepcopy(fixture["claims"][1])
        branch["claim_id"] = "CLM2-TRANSITION-C"
        branch["recorded_at"] = "2026-08-05T02:02:00Z"
        branch["provenance_ref"] = "ACT-CLM2-TRANSITION-C"
        fixture["claims"].append(branch)
        for claims in (fixture["claims"], list(reversed(fixture["claims"]))):
            heads = capability_claim_heads(
                claims,
                holder_ref="R-CLM2-TRANSITION",
                capability_ref=CAPABILITY_REF,
                claimant_ref="SOURCE-CLM2",
                claim_kind_ref="holder-capability@2",
                condition_set_ref="field-context@1",
                at="2026-08-05T02:30:00Z",
            )
            self.assertEqual(
                [claim["claim_id"] for claim in heads],
                ["CLM2-TRANSITION-B", "CLM2-TRANSITION-C"],
            )

    def test_finite_observation_disagreement_is_conflicting_not_a_vote(self) -> None:
        fixture = self._fixture("valid-activated-fresh.yaml")
        fixture["observations"].append(
            {
                "observation_id": "OBS-CLM2-DISAGREE",
                "observer_ref": "SOURCE-EVIDENCE-B",
                "observation_kind_ref": "capability-demonstration.field@1",
                "statement": "Resource did not demonstrate navigation.",
                "observed_at": "2026-08-05T01:51:00Z",
                "recorded_at": "2026-08-05T01:52:00Z",
                "provenance_ref": "ACT-OBS-CLM2-DISAGREE",
            }
        )
        binding = {
            "evidence_kind_ref": "observation-record@1",
            "evidence_ref": "OBS-CLM2-DISAGREE",
        }
        fixture["claims"][0]["evidence_bindings"].append(binding)
        fixture["evidence_snapshots"][0]["evidence_bindings"].append(binding)
        fixture["claims"][0]["support_state"] = "conflicting"
        self.assertTrue(validate_reference_fixture(fixture).valid)
        self.assertEqual(self._activated_projection(fixture), "indeterminate")

    def test_declared_positive_is_attributable_not_verified(self) -> None:
        fixture = self._fixture("valid-declared-positive.yaml")
        self.assertTrue(validate_reference_fixture(fixture).valid)
        claim = resolve_capability_claim(fixture["claims"], "CLM-001")
        self.assertIsNotNone(claim)
        self.assertNotIn("verified", claim)
        self.assertEqual(
            effective_capability_claim(
                fixture["claims"],
                holder_ref="R-CLAIM-001",
                capability_ref=CAPABILITY_REF,
                claimant_ref="SOURCE-001",
                claim_kind_ref="holder-capability@1",
                condition_set_ref="unconditional@1",
                at="2026-08-04T09:00:00Z",
            ),
            "positive",
        )

    def test_withdrawal_does_not_become_negative_polarity(self) -> None:
        fixture = self._fixture("valid-withdrawal-history.yaml")
        self.assertTrue(validate_reference_fixture(fixture).valid)
        before = effective_capability_claim(
            fixture["claims"],
            holder_ref="R-CLAIM-002",
            capability_ref=CAPABILITY_REF,
            claimant_ref="SOURCE-002",
            claim_kind_ref="holder-capability@1",
            condition_set_ref="unconditional@1",
            at="2026-08-04T09:00:00Z",
        )
        after = effective_capability_claim(
            fixture["claims"],
            holder_ref="R-CLAIM-002",
            capability_ref=CAPABILITY_REF,
            claimant_ref="SOURCE-002",
            claim_kind_ref="holder-capability@1",
            condition_set_ref="unconditional@1",
            at="2026-08-04T11:00:00Z",
        )
        self.assertEqual(before, "positive")
        self.assertEqual(after, "withdrawn")
        self.assertNotEqual(after, "negative")

    def test_conflicting_branch_heads_fail_safe_in_any_order(self) -> None:
        fixture = self._fixture("valid-conflicting-heads.yaml")
        self.assertTrue(validate_reference_fixture(fixture).valid)
        for claims in (fixture["claims"], list(reversed(fixture["claims"]))):
            with self.subTest(order=[claim["claim_id"] for claim in claims]):
                heads = capability_claim_heads(
                    claims,
                    holder_ref="R-CLAIM-003",
                    capability_ref=CAPABILITY_REF,
                    claimant_ref="SOURCE-003",
                    claim_kind_ref="holder-capability@1",
                    condition_set_ref="field-context@1",
                    at="2026-08-04T10:00:00Z",
                )
                self.assertEqual(
                    [head["claim_id"] for head in heads], ["CLM-003B", "CLM-003C"]
                )
                self.assertEqual(
                    effective_capability_claim(
                        claims,
                        holder_ref="R-CLAIM-003",
                        capability_ref=CAPABILITY_REF,
                        claimant_ref="SOURCE-003",
                        claim_kind_ref="holder-capability@1",
                        condition_set_ref="field-context@1",
                        at="2026-08-04T10:00:00Z",
                    ),
                    "indeterminate",
                )

    def test_stale_support_cannot_project_positive(self) -> None:
        fixture = self._fixture("valid-stale-support-fails-safe.yaml")
        self.assertTrue(validate_reference_fixture(fixture).valid)
        self.assertEqual(
            effective_capability_claim(
                fixture["claims"],
                holder_ref="R-CLAIM-004",
                capability_ref=CAPABILITY_REF,
                claimant_ref="SOURCE-004",
                claim_kind_ref="holder-capability@1",
                condition_set_ref="field-context@1",
                at="2026-08-04T09:00:00Z",
            ),
            "indeterminate",
        )

    def test_matching_claims_do_not_collapse_resource_identity(self) -> None:
        fixture = self._fixture("valid-matching-claims-distinct-resources.yaml")
        self.assertTrue(validate_reference_fixture(fixture).valid)
        self.assertEqual(
            {resource["resource_id"] for resource in fixture["resources"]},
            {"R-CLAIM-005A", "R-CLAIM-005B"},
        )
        self.assertEqual(len(fixture["claims"]), 2)

    def test_exact_capability_version_and_resource_must_resolve(self) -> None:
        holder = self._fixture("invalid-unresolved-holder.yaml")
        capability = self._fixture("invalid-unresolved-capability-version.yaml")
        self.assertEqual(
            set(validate_reference_fixture(holder).errors),
            {"CAPABILITY_CLAIM_HOLDER_UNRESOLVED"},
        )
        self.assertEqual(
            set(validate_reference_fixture(capability).errors),
            {"CAPABILITY_CLAIM_CAPABILITY_UNRESOLVED"},
        )

    def test_organization_holder_and_semantic_coupling_are_rejected(self) -> None:
        organization = self._fixture("invalid-organization-holder.yaml")
        coupling = self._fixture("invalid-forbidden-coupling.yaml")
        self.assertEqual(
            set(validate_reference_fixture(organization).errors),
            {
                "CAPABILITY_CLAIM_HOLDER_KIND_UNSUPPORTED",
                "CAPABILITY_CLAIM_HOLDER_UNRESOLVED",
            },
        )
        self.assertEqual(
            set(validate_reference_fixture(coupling).errors),
            {"CAPABILITY_CLAIM_FORBIDDEN_COUPLING"},
        )

    def test_supersession_preserves_binding_and_acyclic_history(self) -> None:
        binding = self._fixture("invalid-binding-change.yaml")
        cycle = self._fixture("invalid-supersession-cycle.yaml")
        self.assertEqual(
            set(validate_reference_fixture(binding).errors),
            {"CAPABILITY_CLAIM_BINDING_MISMATCH"},
        )
        self.assertEqual(
            set(validate_reference_fixture(cycle).errors),
            {"CAPABILITY_CLAIM_SUPERSESSION_CYCLE"},
        )

    def test_snapshot_mismatch_is_rejected(self) -> None:
        fixture = self._fixture("invalid-snapshot-mismatch.yaml")
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"CAPABILITY_CLAIM_EVIDENCE_SNAPSHOT_MISMATCH"},
        )

    def test_claim_rules_manifest_is_complete(self) -> None:
        rules = yaml.safe_load(
            (ROOT / "capability-claim-rules.yaml").read_text(encoding="utf-8")
        )["rules"]
        validation_ids = {
            item["id"]
            for item in rules
            if item.get("kind", "validation") == "validation"
        }
        derivation_ids = {
            item["id"] for item in rules if item.get("kind") == "derivation"
        }
        self.assertEqual(validation_ids, set(CAPABILITY_CLAIM_ERROR_CODES))
        self.assertEqual(derivation_ids, set(CAPABILITY_CLAIM_DERIVATION_RULES))

        definitions: dict[tuple[str, str], dict] = {}
        for path in sorted((ROOT / "fixtures/capability_claim").glob("*activated*.yaml")):
            fixture = load_fixture(path)
            for collection, identity_field in (
                ("evidence_expectations", "expectation_ref"),
                ("freshness_rules", "rule_ref"),
                ("ambiguity_rules", "rule_ref"),
            ):
                for definition in fixture.get(collection) or []:
                    identity = (collection, definition[identity_field])
                    if identity in definitions:
                        self.assertEqual(definitions[identity], definition)
                    else:
                        definitions[identity] = definition


if __name__ == "__main__":
    unittest.main()
