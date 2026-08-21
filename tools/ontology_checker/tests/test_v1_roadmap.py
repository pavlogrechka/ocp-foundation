from __future__ import annotations

from pathlib import Path
import re
import sys
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools/ontology_checker"))

from ocp_checker.current_numeric_accounting import derive_current_numeric_accounting  # noqa: E402


ROADMAP = Path("backlog/roadmap.md")
GATE = Path("architecture/foundation-promotion-gate.yaml")
NEEDS = Path("architecture/consumer-need-discovery.yaml")


class V1RoadmapTests(unittest.TestCase):
    def text(self) -> str:
        return (ROOT / ROADMAP).read_text(encoding="utf-8")

    def test_readiness_percentages_have_live_inputs_sources_and_formulas(self) -> None:
        text = self.text()
        counts = derive_current_numeric_accounting(ROOT)
        lifecycle_numerator = (
            counts["ocp_canonical"] * 2
            + counts["ocp_accepted"]
            + counts["concept_canonical"] * 2
            + counts["concept_accepted"]
        )
        lifecycle_denominator = (counts["ocp_total"] + counts["concept_total"]) * 2

        self.assertIn(
            f"`{counts['ocp_canonical']} × 2 + {counts['ocp_accepted']} × 1 + "
            f"{counts['ocp_draft']} × 0 = {counts['ocp_canonical'] * 2 + counts['ocp_accepted']}`",
            text,
        )
        self.assertIn(
            f"`({lifecycle_numerator - (counts['concept_canonical'] * 2 + counts['concept_accepted'])} + "
            f"{counts['concept_canonical'] * 2 + counts['concept_accepted']}) / "
            f"({counts['ocp_total'] * 2} + {counts['concept_total'] * 2}) × 100 = "
            f"{lifecycle_numerator / lifecycle_denominator * 100:.1f}%`",
            text,
        )
        self.assertIn("`(1 + 1 + 0 + 0 + 0 + 0) / 6 × 100 = 33.3%`", text)
        self.assertIn("`(0 + 0 + 0 + 0) / 4 × 100 = 0.0%`", text)
        self.assertEqual(
            set(re.findall(r"\d+(?:\.\d+)?%", text)),
            {"33.3%", "75.8%", "0.0%"},
        )
        for source in (
            "../architecture/current-numeric-accounting.yaml",
            "../docs",
            "../schemas/README.md",
            "../tools/ontology_checker/README.md",
            "../docs/024-completeness-evaluator/README.md",
        ):
            self.assertIn(source, text)

        self.assertEqual(counts["ocp_draft"], 0)
        self.assertTrue(any((ROOT / "tools/ontology_checker/ocp_checker").glob("*.py")))
        self.assertEqual(
            [path.name for path in (ROOT / "schemas").iterdir() if path.is_file()],
            ["README.md"],
        )
        checker_guide = (ROOT / "tools/ontology_checker/README.md").read_text(encoding="utf-8")
        self.assertIn("not** a production validator, persistence schema, policy engine", checker_guide)
        evaluator = (ROOT / "docs/024-completeness-evaluator/README.md").read_text(encoding="utf-8")
        self.assertIn("A real evaluator remains unresolved", evaluator)
        self.assertFalse((ROOT / "external-conformance").exists())

    def test_v1_non_goals_are_current_normative_boundaries(self) -> None:
        roadmap = self.text()
        required_non_goals = (
            "establish Conflict, Risk, priority or a winner among Assignments",
            "derive capacity sufficiency, availability, remainder, reservation or allocation",
            "establish Order as mandatory, sufficient or an authorization source",
            "establish Constraint precedence, override or contextual waiver",
            "grant permission, approval, authorization, truth or action recommendations",
            "answer OCP-005 withheld Q2/Q4/Q5/Q7/Q8/Q9/Q10/Q11 by silence",
            "answer OCP-006 open Q1/Q2/Q6/Q7/Q8/Q10/Q11/Q12 by silence",
            "claim that synthetic fixtures authenticate a real source, owner, evaluator or complete observation cut",
        )
        for non_goal in required_non_goals:
            self.assertIn(non_goal, roadmap)

        source_tokens = {
            Path("docs/005-assignment-concept/README.md"): (
                "Q2 amendment after Establishment",
                "the rights delta is zero",
            ),
            Path("docs/006-constraint-concept/README.md"): (
                "Q1 Conflict object or aggregation",
                "no previously conditional positive behavior becomes legitimate",
            ),
            Path("docs/016-core-boundary/README.md"): (
                "OCP-016 grants no domain truth",
                "G4 consumer activation remains binding",
            ),
            Path("docs/024-completeness-evaluator/README.md"): (
                "Actual legitimacy cannot be established from those properties alone",
                "A real evaluator remains unresolved",
            ),
        }
        for path, tokens in source_tokens.items():
            body = (ROOT / path).read_text(encoding="utf-8")
            for token in tokens:
                self.assertIn(token, body)

    def test_current_status_version_cycle_and_need_match_live_sources(self) -> None:
        text = self.text()
        counts = derive_current_numeric_accounting(ROOT)
        self.assertIn(
            f"**{counts['ocp_total']} total = {counts['ocp_canonical']} Canonical + "
            f"{counts['ocp_accepted']} Accepted + {counts['ocp_draft']} Draft**",
            text,
        )
        self.assertIn(
            f"**{counts['concept_total']} total = {counts['concept_canonical']} Canonical + "
            f"{counts['concept_accepted']} Accepted**",
            text,
        )

        gate = yaml.safe_load((ROOT / GATE).read_text(encoding="utf-8"))
        active_cycle = gate["cycle_protocol"]["active_cycle_id"]
        cycle = next(item for item in gate["cycles"] if item["cycle_id"] == active_cycle)
        self.assertIn(f"**`{active_cycle}`**", text)
        for key, value in cycle["steps"].items():
            self.assertIn(f"`{key}={value}`", text)

        for document_id in ("OCP-005", "OCP-006"):
            candidate = next(item for item in gate["candidates"] if item["document_id"] == document_id)
            primary = (ROOT / candidate["primary"]).read_text(encoding="utf-8")
            version = re.search(r"^Version: (.+)$", primary, re.MULTILINE).group(1)
            status = re.search(r"^Status: (.+)$", primary, re.MULTILINE).group(1)
            concept = re.search(r"^Concept-Status: (.+)$", primary, re.MULTILINE).group(1)
            self.assertIn(f"`{document_id}`: **{version} / {status}**", text)
            concept_name = "Assignment" if document_id == "OCP-005" else "Constraint"
            self.assertIn(f"Concept `{concept_name}`: **{concept}**", text)

        needs = yaml.safe_load((ROOT / NEEDS).read_text(encoding="utf-8"))
        unmet = needs["current_result"]["unmet_positive_needs"]
        self.assertEqual(unmet, ["RESOURCE_OCCUPANCY_ASSIGNMENT_SET_COMPLETENESS"])
        self.assertIn(f"**`{unmet[0]}`**", text)


if __name__ == "__main__":
    unittest.main()
