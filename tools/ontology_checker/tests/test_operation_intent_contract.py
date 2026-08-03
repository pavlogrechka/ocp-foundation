from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import validate_reference_fixture  # noqa: E402


def valid_explicit_intent_fixture() -> dict:
    return {
        "concept": "Operation",
        "entity": {
            "operation_id": "OP-INTENT-TEST-001",
            "lifecycle_stage": "Planned",
            "explicit_intent_record": {
                "intent_id": "INT-TEST-001",
                "intent_version_ref": "INT-TEST-001@1",
                "statement": "Preserve access to the transit corridor",
                "validation_rule_ref": "RULE-INTENT-TEST@2",
                "input_snapshot_ref": "SNAP-INTENT-TEST-001",
                "validation_status": "passed",
                "validation_records": [
                    {
                        "validation_id": "INT-VAL-TEST-001",
                        "intent_version_ref": "INT-TEST-001@1",
                        "validation_rule_ref": "RULE-INTENT-TEST@2",
                        "input_snapshot_ref": "SNAP-INTENT-TEST-001",
                        "evaluated_at": "2026-08-03T18:00:00Z",
                        "evaluator_ref": "checker://intent-test-v2",
                        "result": "passed",
                    }
                ],
            },
        },
    }


class OperationIntentContractTests(unittest.TestCase):
    def test_exact_binding_evidence_is_authoritative(self) -> None:
        self.assertTrue(validate_reference_fixture(valid_explicit_intent_fixture()).valid)

    def test_each_evidence_binding_is_structurally_required(self) -> None:
        mutations = {
            "validation_id": lambda record: record.pop("validation_id"),
            "intent_version_ref": lambda record: record.update(intent_version_ref="INT-TEST-001"),
            "validation_rule_ref": lambda record: record.update(validation_rule_ref="RULE-INTENT-TEST"),
            "input_snapshot_ref": lambda record: record.pop("input_snapshot_ref"),
            "evaluated_at": lambda record: record.update(evaluated_at="not-a-time"),
            "evaluator_ref": lambda record: record.pop("evaluator_ref"),
            "result": lambda record: record.update(result="unknown"),
        }
        for field, mutate in mutations.items():
            with self.subTest(field=field):
                fixture = copy.deepcopy(valid_explicit_intent_fixture())
                mutate(fixture["entity"]["explicit_intent_record"]["validation_records"][0])
                self.assertEqual(
                    set(validate_reference_fixture(fixture).errors),
                    {"OPERATION_EXPLICIT_INTENT_EVIDENCE_INVALID"},
                )

    def test_substantive_binding_change_makes_prior_evidence_stale(self) -> None:
        for field, replacement in {
            "intent_version_ref": "INT-TEST-001@2",
            "validation_rule_ref": "RULE-INTENT-TEST@3",
            "input_snapshot_ref": "SNAP-INTENT-TEST-002",
        }.items():
            with self.subTest(field=field):
                fixture = copy.deepcopy(valid_explicit_intent_fixture())
                fixture["entity"]["explicit_intent_record"][field] = replacement
                self.assertEqual(
                    set(validate_reference_fixture(fixture).errors),
                    {"OPERATION_EXPLICIT_INTENT_EVIDENCE_STALE"},
                )

    def test_materialized_status_cannot_override_evidence(self) -> None:
        fixture = valid_explicit_intent_fixture()
        fixture["entity"]["explicit_intent_record"]["validation_status"] = "failed"
        self.assertEqual(
            set(validate_reference_fixture(fixture).errors),
            {"OPERATION_EXPLICIT_INTENT_STATUS_MISMATCH"},
        )


if __name__ == "__main__":
    unittest.main()
