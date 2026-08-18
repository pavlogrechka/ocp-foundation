from __future__ import annotations

from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker import current_numeric_accounting  # noqa: E402
from ocp_checker.current_numeric_accounting import (  # noqa: E402
    CURRENT_NUMERIC_ACCOUNTING_DRIFT,
    CURRENT_NUMERIC_ACCOUNTING_MAP_INVALID,
    derive_current_numeric_accounting,
    validate_current_numeric_accounting,
)


class CurrentNumericAccountingTests(unittest.TestCase):
    copied_paths = (
        Path("README.md"),
        Path("architecture/current-numeric-accounting.yaml"),
        Path("architecture/accepted-document-snapshot-map.yaml"),
        Path("tools/ontology_checker/fixtures"),
        Path("tools/ontology_checker/tests"),
        Path("docs"),
    )

    def copy_inputs(self, destination: Path) -> None:
        for relative in self.copied_paths:
            source = ROOT / relative
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copyfile(source, target)

    def test_repository_current_numeric_accounting_is_derived(self) -> None:
        self.assertTrue(validate_current_numeric_accounting(ROOT).valid)
        self.assertEqual(
            derive_current_numeric_accounting(ROOT),
            {
                "ocp_total": 25,
                "ocp_canonical": 10,
                "ocp_accepted": 13,
                "ocp_draft": 2,
                "concept_total": 8,
                "concept_canonical": 6,
                "concept_accepted": 2,
                "snapshot_total": 14,
                "snapshot_current": 13,
                "snapshot_retained": 1,
                "p001_invokers": 9,
                "fixtures": 302,
                "tests": 410,
            },
        )

    def test_every_primary_document_status_change_requires_accounting_update(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            for primary in sorted((root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
                with self.subTest(primary=primary.relative_to(root)):
                    original = primary.read_text(encoding="utf-8")
                    old = next(line for line in original.splitlines() if line.startswith("Status:"))
                    replacement = "Status: Draft" if old != "Status: Draft" else "Status: Accepted"
                    primary.write_text(original.replace(old, replacement, 1), encoding="utf-8")
                    self.assertIn(
                        CURRENT_NUMERIC_ACCOUNTING_DRIFT,
                        validate_current_numeric_accounting(root).errors,
                    )
                    primary.write_text(original, encoding="utf-8")

    def test_every_defining_concept_status_change_requires_accounting_update(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            for primary in sorted((root / "docs").glob("[0-9][0-9][0-9]-*/README.md")):
                original = primary.read_text(encoding="utf-8")
                matches = [line for line in original.splitlines() if line.startswith("Concept-Status:")]
                if not matches:
                    continue
                with self.subTest(primary=primary.relative_to(root)):
                    old = matches[0]
                    replacement = (
                        "Concept-Status: Accepted"
                        if old == "Concept-Status: Canonical"
                        else "Concept-Status: Canonical"
                    )
                    primary.write_text(original.replace(old, replacement, 1), encoding="utf-8")
                    self.assertIn(
                        CURRENT_NUMERIC_ACCOUNTING_DRIFT,
                        validate_current_numeric_accounting(root).errors,
                    )
                    primary.write_text(original, encoding="utf-8")

    def test_each_derived_nonstatus_count_is_live(self) -> None:
        attacks = ("snapshot", "invoker", "fixture", "test")
        for attack in attacks:
            with self.subTest(attack=attack), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.copy_inputs(root)
                if attack == "snapshot":
                    fpath = root / "architecture/accepted-document-snapshot-map.yaml"
                    payload = yaml.safe_load(fpath.read_text(encoding="utf-8"))
                    payload["entries"].pop()
                    fpath.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
                elif attack == "invoker":
                    fpath = root / "docs/004-operation-concept/README.md"
                    text = fpath.read_text(encoding="utf-8")
                    fpath.write_text(text.replace("Uses-Patterns: P-001@0.1.0", "Uses-Patterns: []", 1), encoding="utf-8")
                elif attack == "fixture":
                    fixture = next((root / "tools/ontology_checker/fixtures").rglob("*.yaml"))
                    fixture.unlink()
                else:
                    fpath = root / "tools/ontology_checker/tests/test_current_numeric_accounting.py"
                    text = fpath.read_text(encoding="utf-8")
                    fpath.write_text(text.replace("def test_each_derived_nonstatus_count_is_live", "def helper_each_derived_nonstatus_count_is_live", 1), encoding="utf-8")
                self.assertIn(
                    CURRENT_NUMERIC_ACCOUNTING_DRIFT,
                    validate_current_numeric_accounting(root).errors,
                )

    def test_mutating_each_rendered_number_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.copy_inputs(root)
            readme = root / "README.md"
            text = readme.read_text(encoding="utf-8")
            line = next(item for item in text.splitlines() if item.startswith("- machine-derived current accounting:"))
            matches = tuple(re.finditer(r"(?<!-)\b\d+\b", line))
            self.assertEqual(len(matches), 13)
            for index, match in enumerate(matches):
                with self.subTest(index=index, number=match.group()):
                    mutated = (
                        line[:match.start()]
                        + str(int(match.group()) + 100)
                        + line[match.end():]
                    )
                    readme.write_text(text.replace(line, mutated, 1), encoding="utf-8")
                    self.assertIn(
                        CURRENT_NUMERIC_ACCOUNTING_DRIFT,
                        validate_current_numeric_accounting(root).errors,
                    )
                    readme.write_text(text, encoding="utf-8")

    def test_every_defensive_value_is_individually_fixture_and_mutation_live(self) -> None:
        categories = (
            "MAP_KEYS",
            "DOCUMENT_STATUS_LABELS",
            "CONCEPT_STATUS_LABELS",
            "SNAPSHOT_BASES",
        )
        for attribute in categories:
            values = getattr(current_numeric_accounting, attribute)
            for value in sorted(values):
                with self.subTest(attribute=attribute, value=value), patch.object(
                    current_numeric_accounting, attribute, values - {value}
                ):
                    self.assertIn(
                        CURRENT_NUMERIC_ACCOUNTING_MAP_INVALID,
                        validate_current_numeric_accounting(ROOT).errors,
                    )
        for value in current_numeric_accounting.METRIC_IDS:
            with self.subTest(attribute="METRIC_IDS", value=value), patch.object(
                current_numeric_accounting,
                "METRIC_IDS",
                tuple(item for item in current_numeric_accounting.METRIC_IDS if item != value),
            ):
                self.assertIn(
                    CURRENT_NUMERIC_ACCOUNTING_MAP_INVALID,
                    validate_current_numeric_accounting(ROOT).errors,
                )


if __name__ == "__main__":
    unittest.main()
