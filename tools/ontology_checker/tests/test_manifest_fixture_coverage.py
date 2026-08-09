from __future__ import annotations

import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


class ManifestFixtureCoverageTests(unittest.TestCase):
    def test_manifests_declaring_complete_coverage_have_direct_fixture_evidence(self) -> None:
        fixtures = []
        for path in sorted((ROOT / "fixtures").rglob("*.yaml")):
            value = yaml.safe_load(path.read_text(encoding="utf-8"))
            if isinstance(value, dict):
                fixtures.append((path, value))

        checked = 0
        for manifest_path in sorted(ROOT.glob("*-rules.yaml")):
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
            coverage = manifest.get("fixture_coverage") or {}
            if coverage.get("status") != "complete":
                continue
            checked += 1
            concept = coverage.get("concept")
            expected_ids = {
                rule["id"]
                for rule in manifest.get("rules") or []
                if rule.get("kind", "validation") == "validation"
            }
            observed_ids = {
                code
                for _, fixture in fixtures
                if fixture.get("concept") == concept
                for code in (fixture.get("expected") or {}).get("error_codes", [])
            }
            self.assertEqual(
                observed_ids,
                expected_ids,
                f"{manifest_path.name} complete fixture coverage drift for {concept}",
            )
        self.assertGreaterEqual(checked, 2)


if __name__ == "__main__":
    unittest.main()
