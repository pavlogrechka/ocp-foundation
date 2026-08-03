from __future__ import annotations
import tempfile, unittest
from pathlib import Path
from ocp_checker.concept_graph import validate_and_render_concept_graph
REGISTRY="""# registry
| Concept | Status | Specification |
|---|---|---|
| Resource | Accepted | OCP-003 |
| Operation | Accepted | OCP-004 |
| Assignment | Accepted | OCP-005 |
"""
def write(p,c): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(c)
class ConceptGraphTests(unittest.TestCase):
    def make_repo(self,d,status="Accepted",omit=None,legacy=False):
        r=Path(tempfile.mkdtemp()); write(r/"docs/000-operational-ontology/README.md",REGISTRY)
        for n,doc,concept in ((3,"OCP-003","Resource"),(4,"OCP-004","Operation"),(5,"OCP-005","Assignment")):
            dec="" if concept==omit else f"\nConcept-Depends-On: [{', '.join(d[concept])}]"; write(r/f"docs/{n:03d}-concept/README.md",f"---\nDocument-ID: {doc}\nDefines-Concepts: {concept}{dec}\nConcept-Status: {status if concept=='Assignment' else 'Accepted'}\n---\n")
        if legacy: write(r/"architecture/baselines/concept-dependencies.yaml","concepts: {}\n")
        write(r/"architecture/baselines/foundation-future-edges.yaml","edges: []\n"); return r
    def deps(self): return {"Resource":[],"Operation":[],"Assignment":["Resource","Operation"]}
    def test_valid(self): self.assertTrue(validate_and_render_concept_graph(self.make_repo(self.deps())).valid)
    def test_missing(self): self.assertIn("CONCEPT_GRAPH_DEPENDENCY_DECLARATION_MISSING",validate_and_render_concept_graph(self.make_repo(self.deps(),omit="Resource")).errors)
    def test_legacy(self): self.assertIn("CONCEPT_GRAPH_MULTIPLE_DEPENDENCY_SOURCES",validate_and_render_concept_graph(self.make_repo(self.deps(),legacy=True)).errors)
    def test_phantom(self): d=self.deps(); d["Assignment"]=["Phantom"]; self.assertIn("CONCEPT_GRAPH_PHANTOM_REFERENCE",validate_and_render_concept_graph(self.make_repo(d)).errors)
    def test_cycle(self): d=self.deps(); d["Resource"]=["Assignment"]; d["Assignment"]=["Resource"]; self.assertIn("CONCEPT_GRAPH_CYCLE",validate_and_render_concept_graph(self.make_repo(d)).errors)
    def test_contexts(self): r=self.make_repo(self.deps(),status="Under Review"); self.assertNotIn("MAIN_CONCEPT_UNDER_REVIEW",validate_and_render_concept_graph(r,"pr").errors); self.assertIn("MAIN_CONCEPT_UNDER_REVIEW",validate_and_render_concept_graph(r,"main").errors)
