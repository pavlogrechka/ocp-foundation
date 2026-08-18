from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker.checker import load_fixture  # noqa: E402
from ocp_checker.resource_occupancy import derive_resource_occupancy  # noqa: E402


BASELINE = "e3ab36c25f4e5e69489b39c87748a9cbdea313a5"
BASELINE_TREE = "6bbc2557b47d55e7556edb4e9b218d30e291dcc2"
ANCHORS = {
    "docs/023-resource-occupancy/README.md": (
        "8d5f5c2b340f78b84ce3de96c52ae18d0780ca66",
        "c8a765053c3bd398eba18508c080f15dbe49a784565faa59bb8a88d266d872d4",
        ("Version: 0.1.0", "Status: Draft", "assignment_set_complete_for_resource"),
    ),
    "docs/001-ontology-governance/README.md": (
        "33524fa3d18f3253faa9a854500be7ddfb20815f",
        "da74645aa4f3cae10c7c59ae7b87abd1840544700e4a58e9efd3f6600a27f1cc",
        ("Status: Canonical", "Accepted"),
    ),
    "docs/005-assignment-concept/README.md": (
        "6e6c00e723b15a348e7610d4ca5a1ae23526c52b",
        "a9226f4f5e168b945ae743626e73ba5e25d67318b390869a493e5fd30bdaa065",
        ("Version: 0.2.8", "Status: Draft", "assignment_effective_at"),
    ),
    "docs/016-core-boundary/README.md": (
        "94f5d997deea0168a3c553c2ac9f19d2ee03b4fb",
        "78b1ff043ea17b862a8157bfac1774352090ec4a9bd34e5dd8389d8673e006d4",
        ("Status: Canonical", "G4"),
    ),
    "architecture/discovery/AD-029-accepted-document-hygiene.md": (
        "b33f218567c53bea06c10efdf93fa5bd78a29a1c",
        "19e62307c98b6b6a62945b5a27c3be8a5e49914eabb94814667b330ca58160c8",
        ("Status: Accepted", "reviewed-contract"),
    ),
    "architecture/discovery/AD-036-consumer-need-discovery.md": (
        "3f8642777c16015226065f29f745b2e31bb6cd3a",
        "564bc5c5b7d12c2be95278af6b3518a3af773ade701e3fee1dc4a9a4daac5603",
        ("Version: 0.1.0", "Status: Discovery", "No current Accepted or Canonical document states an unmet positive consumer need"),
    ),
    "architecture/accepted-document-snapshot-map.yaml": (
        "c4d35d99ba46db310b9dfe9c84268914171f0e28",
        "694ecb76da4851ba8228a738039256a4226a6e4848013c557c37213aa648755a",
        ("schema_version: 1", "OCP-022"),
    ),
    "architecture/consumer-need-discovery.yaml": (
        "b6d85009db5d2a7adbbf80327d6a521f344f6045",
        "bb742bf55e4e7fd3bade6ce88af78f754f6fb64104c3dab9f207dcd0be9ef544",
        ("schema_version: 1", "no_unmet_positive_consumer_need_declared"),
    ),
    "tools/ontology_checker/ocp_checker/resource_occupancy.py": (
        "3d7ee96ac0d9f51cb04fd860cb5117806b422549",
        "a44caaa19f1964e72b3c97f23175fa65695ce3b95e54f4b6f76fdf6bf96658c3",
        ("derive_resource_occupancy", "RESOURCE_OCCUPANCY_ACTIVATION_FORBIDDEN"),
    ),
    "tools/ontology_checker/resource-occupancy-rules.yaml": (
        "32e7ac535b6a24fc30784deee59411597725998d",
        "16cf4094dff5775e34731862dafc3b455b6b31eac0d17733d7fd3496ca06e496",
        ("OCP-023", "derive_resource_occupancy"),
    ),
    "tools/ontology_checker/tests/test_resource_occupancy.py": (
        "e20a3ab0e52b352d119c2b3b769ae376c0f0ac82",
        "4205d139689428a63831deed0cf6efdf42ec71b87c1dd9172cc04119686ac680",
        ("test_every_defensive_value_is_individually_fixture_and_mutation_live",),
    ),
}


class Ocp023AcceptanceTests(unittest.TestCase):
    def test_baseline_anchors_reverse_resolve_state_and_hash_full_chain(self) -> None:
        self.assertEqual(
            subprocess.run(
                ["git", "rev-parse", f"{BASELINE}^{{tree}}"], cwd=ROOT, check=True,
                capture_output=True, text=True,
            ).stdout.strip(),
            BASELINE_TREE,
        )
        tree = subprocess.run(
            ["git", "ls-tree", "-r", BASELINE], cwd=ROOT, check=True,
            capture_output=True, text=True,
        ).stdout.splitlines()
        by_blob: dict[str, list[str]] = {}
        for line in tree:
            metadata, path = line.split("\t", 1)
            by_blob.setdefault(metadata.split()[2], []).append(path)
        for path, (blob, expected_sha, state_tokens) in ANCHORS.items():
            with self.subTest(path=path):
                self.assertIn(path, by_blob.get(blob, ()))
                raw = subprocess.run(
                    ["git", "show", f"{BASELINE}:{path}"], cwd=ROOT, check=True,
                    capture_output=True,
                ).stdout
                self.assertEqual(hashlib.sha256(raw).hexdigest(), expected_sha)
                text = raw.decode("utf-8")
                for token in state_tokens:
                    self.assertIn(token, text)

    def test_reviewed_snapshot_is_the_exact_baseline_draft(self) -> None:
        baseline = subprocess.run(
            ["git", "show", f"{BASELINE}:docs/023-resource-occupancy/README.md"],
            cwd=ROOT, check=True, capture_output=True,
        ).stdout
        snapshot = (ROOT / "docs/023-resource-occupancy/reviewed-contract-v0.1.0.md").read_bytes()
        self.assertEqual(snapshot, baseline)
        self.assertEqual(len(snapshot), 9360)
        self.assertEqual(
            hashlib.sha256(snapshot).hexdigest(),
            "c8a765053c3bd398eba18508c080f15dbe49a784565faa59bb8a88d266d872d4",
        )

    def test_partial_true_false_boundary_remains_exact_after_acceptance(self) -> None:
        fixture = load_fixture(
            ROOT / "tools/ontology_checker/fixtures/resource_occupancy/valid-one-effective.yaml"
        )
        result = derive_resource_occupancy(fixture["dataset"])
        self.assertIs(result.occupied, True)
        self.assertEqual(result.witness_assignment_refs, ("A-001",))
        fixture["dataset"]["assignment_snapshots"][0]["completeness_evidence_ref"] = None
        result = derive_resource_occupancy(fixture["dataset"])
        self.assertIsNone(result.occupied)
        self.assertEqual(result.witness_assignment_refs, ())

    def test_accepted_lifecycle_changes_no_occupancy_runtime_or_fixture_bytes(self) -> None:
        protected = (
            "tools/ontology_checker/ocp_checker/resource_occupancy.py",
            "tools/ontology_checker/resource-occupancy-rules.yaml",
            "tools/ontology_checker/fixtures/resource_occupancy",
        )
        completed = subprocess.run(
            ["git", "diff", "--quiet", BASELINE, "--", *protected], cwd=ROOT,
            check=False,
        )
        self.assertEqual(completed.returncode, 0)


if __name__ == "__main__":
    unittest.main()
