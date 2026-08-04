from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ocp_checker import load_fixture, resolve_capability_definition, validate_reference_fixture  # noqa: E402


class CapabilityContractTests(unittest.TestCase):
    def test_exact_version_resolution_is_deterministic(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/capability/valid-deterministic-resolution.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        resolved = resolve_capability_definition(
            fixture["entries"], fixture["reference"]
        )
        self.assertIsNotNone(resolved)
        self.assertEqual(resolved["version"], "v1")
        self.assertEqual(resolved["provenance_ref"], "ACT-CAP-001")

    def test_namespace_collision_does_not_collapse_identity(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/capability/valid-namespace-collision.yaml"
        )
        communications = resolve_capability_definition(
            fixture["entries"],
            {
                "namespace": "communications",
                "capability_id": "relay",
                "version": "v1",
            },
        )
        logistics = resolve_capability_definition(
            fixture["entries"],
            {
                "namespace": "logistics",
                "capability_id": "relay",
                "version": "v1",
            },
        )
        self.assertIsNotNone(communications)
        self.assertIsNotNone(logistics)
        self.assertNotEqual(
            communications["namespace_owner_ref"],
            logistics["namespace_owner_ref"],
        )
        self.assertEqual(communications["label"], logistics["label"])

    def test_superseded_reference_does_not_redirect(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/capability/valid-superseded-exact-reference.yaml"
        )
        resolved = resolve_capability_definition(
            fixture["entries"], fixture["reference"]
        )
        self.assertIsNotNone(resolved)
        self.assertEqual(resolved["version"], "v1")
        self.assertNotIn("supersedes_capability_ref", resolved)

    def test_registry_context_does_not_create_holder_claim(self) -> None:
        fixture = load_fixture(
            ROOT / "fixtures/capability/valid-registry-not-possession.yaml"
        )
        self.assertTrue(validate_reference_fixture(fixture).valid)
        resolved = resolve_capability_definition(
            fixture["entries"], fixture["reference"]
        )
        self.assertIsNotNone(resolved)
        self.assertNotIn("resource_ref", resolved)
        self.assertNotIn("resource_refs", resolved)
        self.assertNotIn("claim", resolved)
        self.assertNotIn("claims", resolved)


if __name__ == "__main__":
    unittest.main()
