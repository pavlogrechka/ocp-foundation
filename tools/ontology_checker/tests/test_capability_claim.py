from __future__ import annotations

import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import (  # noqa: E402
    capability_claim_heads,
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


if __name__ == "__main__":
    unittest.main()
