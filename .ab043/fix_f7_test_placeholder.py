from pathlib import Path

path = Path("tools/ontology_checker/tests/test_artifact_governance.py")
text = path.read_text(encoding="utf-8")
old = "  history_audit_baseline: 0000000000000000000000000000000000000000\n"
new = '  history_audit_baseline: "0000000000000000000000000000000000000000"\n'
if text.count(old) != 1:
    raise AssertionError("expected one unquoted test baseline placeholder")
path.write_text(text.replace(old, new), encoding="utf-8")
