from pathlib import Path

path = Path("tools/ontology_checker/tests/test_artifact_governance.py")
text = path.read_text(encoding="utf-8")
old = "  history_audit_baseline: 0000000000000000000000000000000000000000\n"
new = '  history_audit_baseline: "0000000000000000000000000000000000000000"\n'
if text.count(old) != 1:
    raise AssertionError("expected one unquoted test baseline placeholder")
text = text.replace(old, new)
old_regex = '            r"history_audit_baseline: [0-9a-f]{40}",\n            f"history_audit_baseline: {baseline}",\n'
new_regex = "            r'history_audit_baseline: \\\"?[0-9a-f]{40}\\\"?',\n            f'history_audit_baseline: \\\"{baseline}\\\"',\n"
if text.count(old_regex) != 1:
    raise AssertionError("expected one baseline replacement helper")
path.write_text(text.replace(old_regex, new_regex), encoding="utf-8")
