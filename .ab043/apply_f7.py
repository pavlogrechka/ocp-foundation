from __future__ import annotations

from pathlib import Path
import re

BASELINE = "fc15d2dfc6d0529735347d8c78dd0e3e5225721d"
ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{path}: expected one occurrence, found {count}: {old!r}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def replace_regex_once(path: Path, pattern: str, replacement: str, flags: int = 0) -> None:
    text = path.read_text(encoding="utf-8")
    updated, count = re.subn(pattern, replacement, text, count=1, flags=flags)
    if count != 1:
        raise AssertionError(f"{path}: expected one regex occurrence, found {count}: {pattern!r}")
    path.write_text(updated, encoding="utf-8")


# Machine-readable taxonomy: baseline is the last accepted legacy merge.
taxonomy = ROOT / "architecture/artifact-taxonomy.yaml"
replace_once(
    taxonomy,
    "  history_audit_scope: all_reachable_commits\n"
    "  history_audit_requires_complete_history: true\n"
    "  note: Branch protection is the preventive control; repository checks audit complete reachable history post-factum.\n",
    "  history_audit_scope: post_baseline_reachable_commits\n"
    "  history_audit_requires_complete_history: true\n"
    f"  history_audit_baseline: {BASELINE}\n"
    "  note: Branch protection is preventive; repository checks audit complete history after the governed legacy baseline.\n",
)

# Human-readable taxonomy mirrors the baseline contract.
taxonomy_md = ROOT / "architecture/artifact-taxonomy.md"
replace_once(
    taxonomy_md,
    "The post-factum process audit requires complete Git history and inspects every merge commit reachable from `HEAD`. A shallow repository is an audit failure, not a successful result. Pull-request merge refs are not audited as repository history because the process audit is enabled only in `main` context.\n",
    "The post-factum process audit requires complete Git history and uses the governed baseline "
    f"`{BASELINE}` (the last legacy merge accepted before squash-only enforcement). It inspects merge commits only in "
    "`<baseline>..HEAD`; the baseline and earlier history remain historical evidence rather than current violations. The baseline must be a full commit SHA and an ancestor of `HEAD`, otherwise the audit fails closed. A shallow repository is an audit failure, not a successful result. Pull-request synthetic merge refs are not audited as repository history because the normal process audit is enabled only in `main` context.\n",
)

# Checker implementation: validate baseline policy and audit only post-baseline history.
checker = ROOT / "tools/ontology_checker/ocp_checker/artifact_governance.py"
replace_once(
    checker,
    'AB_REF = re.compile(r"\\bAB-\\d{3}\\b")\n',
    'AB_REF = re.compile(r"\\bAB-\\d{3}\\b")\nCOMMIT_SHA = re.compile(r"^[0-9a-f]{40}$")\n',
)
replace_once(
    checker,
    "    commit_spec = taxonomy.get(\"commit_convention\") or {}\n"
    "    if (\n"
    "        commit_spec.get(\"merge_method\") != \"squash\"\n"
    "        or commit_spec.get(\"linear_history_required\") is not True\n"
    "        or commit_spec.get(\"history_audit_scope\") != \"all_reachable_commits\"\n"
    "        or commit_spec.get(\"history_audit_requires_complete_history\") is not True\n"
    "    ):\n"
    "        errors.append(ARTIFACT_TAXONOMY_INVALID)\n",
    "    commit_spec = taxonomy.get(\"commit_convention\") or {}\n"
    "    baseline = str(commit_spec.get(\"history_audit_baseline\") or \"\")\n"
    "    if (\n"
    "        commit_spec.get(\"merge_method\") != \"squash\"\n"
    "        or commit_spec.get(\"linear_history_required\") is not True\n"
    "        or commit_spec.get(\"history_audit_scope\") != \"post_baseline_reachable_commits\"\n"
    "        or commit_spec.get(\"history_audit_requires_complete_history\") is not True\n"
    "        or not COMMIT_SHA.fullmatch(baseline)\n"
    "    ):\n"
    "        errors.append(ARTIFACT_TAXONOMY_INVALID)\n",
)
replace_once(
    checker,
    "    taxonomy, _ = _load_taxonomy(repo_root)\n"
    "    commit_spec = taxonomy.get(\"commit_convention\") if taxonomy else None\n"
    "    if not isinstance(commit_spec, dict) or (\n"
    "        commit_spec.get(\"linear_history_required\") is not True\n"
    "        or commit_spec.get(\"history_audit_scope\") != \"all_reachable_commits\"\n"
    "        or commit_spec.get(\"history_audit_requires_complete_history\") is not True\n"
    "    ):\n"
    "        return _result((ARTIFACT_TAXONOMY_INVALID,))\n",
    "    taxonomy, _ = _load_taxonomy(repo_root)\n"
    "    commit_spec = taxonomy.get(\"commit_convention\") if taxonomy else None\n"
    "    baseline = str(commit_spec.get(\"history_audit_baseline\") or \"\") if isinstance(commit_spec, dict) else \"\"\n"
    "    if not isinstance(commit_spec, dict) or (\n"
    "        commit_spec.get(\"linear_history_required\") is not True\n"
    "        or commit_spec.get(\"history_audit_scope\") != \"post_baseline_reachable_commits\"\n"
    "        or commit_spec.get(\"history_audit_requires_complete_history\") is not True\n"
    "        or not COMMIT_SHA.fullmatch(baseline)\n"
    "    ):\n"
    "        return _result((PROCESS_HISTORY_AUDIT_FAILED,))\n",
)
replace_once(
    checker,
    "    merges = _run_git(repo_root, \"rev-list\", \"--min-parents=2\", \"HEAD\")\n"
    "    if merges is None:\n"
    "        return _result((PROCESS_HISTORY_AUDIT_FAILED,))\n"
    "    return _result((PROCESS_HISTORY_NON_LINEAR,)) if merges.stdout.strip() else _result(())\n",
    "    ancestor = _run_git(repo_root, \"merge-base\", \"--is-ancestor\", baseline, \"HEAD\")\n"
    "    if ancestor is None:\n"
    "        return _result((PROCESS_HISTORY_AUDIT_FAILED,))\n\n"
    "    merges = _run_git(repo_root, \"rev-list\", \"--min-parents=2\", f\"{baseline}..HEAD\")\n"
    "    if merges is None:\n"
    "        return _result((PROCESS_HISTORY_AUDIT_FAILED,))\n"
    "    return _result((PROCESS_HISTORY_NON_LINEAR,)) if merges.stdout.strip() else _result(())\n",
)

# Checker documentation.
readme = ROOT / "tools/ontology_checker/README.md"
replace_once(
    readme,
    "- process audit: main-context verification that complete reachable Git history contains no merge commit.\n",
    "- process audit: main-context verification that complete post-baseline Git history contains no merge commit.\n",
)
replace_once(
    readme,
    "- the complete-history, all-reachable-commits process-audit scope.\n",
    "- the complete-history, post-baseline process-audit scope and governed baseline SHA.\n",
)
replace_regex_once(
    readme,
    r"In `main` context the audit:\n\n1\. requires a non-shallow repository;\n2\. requires the taxonomy's complete-history policy;\n3\. searches every commit reachable from `HEAD` for commits with two or more parents;\n4\. fails closed when Git history cannot be inspected\.\n\nThe workflow therefore checks out with `fetch-depth: 0`\. A shallow clone emits `PROCESS_HISTORY_SHALLOW`; a Git infrastructure failure emits `PROCESS_HISTORY_AUDIT_FAILED`\. Neither condition can report PASS\.\n",
    "In `main` context the audit:\n\n"
    "1. requires a non-shallow repository;\n"
    "2. reads the full-SHA `history_audit_baseline` from taxonomy;\n"
    "3. requires that baseline to be an ancestor of `HEAD`;\n"
    "4. searches `<baseline>..HEAD` for commits with two or more parents;\n"
    "5. fails closed when the baseline or Git history cannot be inspected.\n\n"
    f"Taxonomy `0.4.0` sets the baseline to `{BASELINE}`, the last accepted legacy merge before squash-only enforcement. The baseline and earlier merge commits are historical evidence and are not reclassified as current violations. Any merge commit after that baseline emits `PROCESS_HISTORY_NON_LINEAR`.\n\n"
    "The workflow checks out with `fetch-depth: 0`. A shallow clone emits `PROCESS_HISTORY_SHALLOW`; an absent, malformed, unreachable baseline or Git infrastructure failure emits `PROCESS_HISTORY_AUDIT_FAILED`. Neither condition can report PASS. PR CI also checks out the actual proposed head and runs the repository checker explicitly in `main` context, avoiding false evidence from GitHub's synthetic merge ref.\n",
)
replace_once(
    readme,
    "- a real merge commit below `HEAD`;\n- a shallow Git clone that must fail closed.\n",
    "- a legacy merge at the configured baseline that remains valid;\n"
    "- a merge commit after the baseline, including one below `HEAD`, that is rejected;\n"
    "- an unreachable baseline and a shallow Git clone that must fail closed;\n"
    "- a real-repository proposed-head run in explicit `main` context.\n",
)
replace_once(
    readme,
    "python tools/ontology_checker/check.py tools/ontology_checker/fixtures\n",
    "python tools/ontology_checker/check.py tools/ontology_checker/fixtures\n"
    "python tools/ontology_checker/check.py tools/ontology_checker/fixtures --context main\n",
)

# Regression tests: taxonomy baseline plus before/after baseline behavior.
tests = ROOT / "tools/ontology_checker/tests/test_artifact_governance.py"
replace_once(
    tests,
    "  history_audit_scope: all_reachable_commits\n"
    "  history_audit_requires_complete_history: true\n",
    "  history_audit_scope: post_baseline_reachable_commits\n"
    "  history_audit_requires_complete_history: true\n"
    "  history_audit_baseline: 0000000000000000000000000000000000000000\n",
)
replace_once(
    tests,
    "    def make_git_repo(self) -> Path:\n"
    "        temp = tempfile.TemporaryDirectory()\n"
    "        self.addCleanup(temp.cleanup)\n"
    "        root = Path(temp.name)\n"
    "        (root / \"architecture\").mkdir()\n"
    "        (root / \"architecture/artifact-taxonomy.yaml\").write_text(TAXONOMY, encoding=\"utf-8\")\n"
    "        self.git(root, \"init\", \"-b\", \"main\")\n"
    "        self.git(root, \"add\", \".\")\n"
    "        self.git(root, \"commit\", \"-m\", \"initial\")\n"
    "        return root\n\n"
    "    def test_process_audit_accepts_linear_complete_history(self) -> None:\n"
    "        root = self.make_git_repo()\n"
    "        self.assertTrue(validate_process_audit(root, context=\"main\").valid)\n\n"
    "    def test_process_audit_finds_merge_below_head(self) -> None:\n"
    "        root = self.make_git_repo()\n"
    "        self.git(root, \"checkout\", \"-b\", \"feature\")\n"
    "        (root / \"feature.txt\").write_text(\"feature\\n\", encoding=\"utf-8\")\n"
    "        self.git(root, \"add\", \"feature.txt\")\n"
    "        self.git(root, \"commit\", \"-m\", \"feature\")\n"
    "        self.git(root, \"checkout\", \"main\")\n"
    "        (root / \"main.txt\").write_text(\"main\\n\", encoding=\"utf-8\")\n"
    "        self.git(root, \"add\", \"main.txt\")\n"
    "        self.git(root, \"commit\", \"-m\", \"main\")\n"
    "        self.git(root, \"merge\", \"--no-ff\", \"feature\", \"-m\", \"merge\")\n"
    "        (root / \"after.txt\").write_text(\"after\\n\", encoding=\"utf-8\")\n"
    "        self.git(root, \"add\", \"after.txt\")\n"
    "        self.git(root, \"commit\", \"-m\", \"after merge\")\n"
    "        self.assertEqual(\n"
    "            set(validate_process_audit(root, context=\"main\").errors),\n"
    "            {PROCESS_HISTORY_NON_LINEAR},\n"
    "        )\n\n",
    "    def make_git_repo(self) -> Path:\n"
    "        temp = tempfile.TemporaryDirectory()\n"
    "        self.addCleanup(temp.cleanup)\n"
    "        root = Path(temp.name)\n"
    "        (root / \"architecture\").mkdir()\n"
    "        (root / \"architecture/artifact-taxonomy.yaml\").write_text(TAXONOMY, encoding=\"utf-8\")\n"
    "        self.git(root, \"init\", \"-b\", \"main\")\n"
    "        self.git(root, \"add\", \".\")\n"
    "        self.git(root, \"commit\", \"-m\", \"initial\")\n"
    "        return root\n\n"
    "    def head(self, root: Path) -> str:\n"
    "        return subprocess.run(\n"
    "            [\"git\", \"rev-parse\", \"HEAD\"], cwd=root, check=True, capture_output=True, text=True\n"
    "        ).stdout.strip()\n\n"
    "    def set_history_baseline(self, root: Path, baseline: str) -> None:\n"
    "        path = root / \"architecture/artifact-taxonomy.yaml\"\n"
    "        text = path.read_text(encoding=\"utf-8\")\n"
    "        updated, count = re.subn(\n"
    "            r\"history_audit_baseline: [0-9a-f]{40}\",\n"
    "            f\"history_audit_baseline: {baseline}\",\n"
    "            text,\n"
    "            count=1,\n"
    "        )\n"
    "        self.assertEqual(count, 1)\n"
    "        path.write_text(updated, encoding=\"utf-8\")\n"
    "        self.git(root, \"add\", str(path.relative_to(root)))\n"
    "        self.git(root, \"commit\", \"-m\", \"set history audit baseline\")\n\n"
    "    def create_merge(self, root: Path, name: str) -> str:\n"
    "        self.git(root, \"checkout\", \"-b\", name)\n"
    "        (root / f\"{name}.txt\").write_text(f\"{name}\\n\", encoding=\"utf-8\")\n"
    "        self.git(root, \"add\", f\"{name}.txt\")\n"
    "        self.git(root, \"commit\", \"-m\", name)\n"
    "        self.git(root, \"checkout\", \"main\")\n"
    "        marker = root / f\"main-{name}.txt\"\n"
    "        marker.write_text(f\"main {name}\\n\", encoding=\"utf-8\")\n"
    "        self.git(root, \"add\", marker.name)\n"
    "        self.git(root, \"commit\", \"-m\", f\"main before {name}\")\n"
    "        self.git(root, \"merge\", \"--no-ff\", name, \"-m\", f\"merge {name}\")\n"
    "        return self.head(root)\n\n"
    "    def test_process_audit_accepts_linear_history_after_baseline(self) -> None:\n"
    "        root = self.make_git_repo()\n"
    "        baseline = self.head(root)\n"
    "        self.set_history_baseline(root, baseline)\n"
    "        (root / \"linear.txt\").write_text(\"linear\\n\", encoding=\"utf-8\")\n"
    "        self.git(root, \"add\", \"linear.txt\")\n"
    "        self.git(root, \"commit\", \"-m\", \"linear after baseline\")\n"
    "        self.assertTrue(validate_process_audit(root, context=\"main\").valid)\n\n"
    "    def test_process_audit_accepts_legacy_merge_at_baseline(self) -> None:\n"
    "        root = self.make_git_repo()\n"
    "        legacy_merge = self.create_merge(root, \"legacy-feature\")\n"
    "        self.set_history_baseline(root, legacy_merge)\n"
    "        (root / \"after-baseline.txt\").write_text(\"linear\\n\", encoding=\"utf-8\")\n"
    "        self.git(root, \"add\", \"after-baseline.txt\")\n"
    "        self.git(root, \"commit\", \"-m\", \"linear after legacy baseline\")\n"
    "        self.assertTrue(validate_process_audit(root, context=\"main\").valid)\n\n"
    "    def test_process_audit_rejects_merge_after_baseline(self) -> None:\n"
    "        root = self.make_git_repo()\n"
    "        baseline = self.head(root)\n"
    "        self.set_history_baseline(root, baseline)\n"
    "        self.create_merge(root, \"post-baseline-feature\")\n"
    "        (root / \"after-merge.txt\").write_text(\"after\\n\", encoding=\"utf-8\")\n"
    "        self.git(root, \"add\", \"after-merge.txt\")\n"
    "        self.git(root, \"commit\", \"-m\", \"after post-baseline merge\")\n"
    "        self.assertEqual(\n"
    "            set(validate_process_audit(root, context=\"main\").errors),\n"
    "            {PROCESS_HISTORY_NON_LINEAR},\n"
    "        )\n\n"
    "    def test_process_audit_rejects_unreachable_baseline(self) -> None:\n"
    "        root = self.make_git_repo()\n"
    "        self.set_history_baseline(root, \"f\" * 40)\n"
    "        self.assertEqual(\n"
    "            set(validate_process_audit(root, context=\"main\").errors),\n"
    "            {PROCESS_HISTORY_AUDIT_FAILED},\n"
    "        )\n\n",
)
# Tests now use re.subn in the generated file.
replace_once(tests, "import os\nimport subprocess\n", "import os\nimport re\nimport subprocess\n")

# CI evidence: run the actual proposed head as if it were main, not the synthetic PR merge ref.
workflow = ROOT / ".github/workflows/ontology-checker.yml"
replace_once(
    workflow,
    "      - name: Validate reference fixtures\n"
    "        run: python tools/ontology_checker/check.py tools/ontology_checker/fixtures\n",
    "      - name: Validate reference fixtures\n"
    "        run: python tools/ontology_checker/check.py tools/ontology_checker/fixtures\n\n"
    "      - name: Validate proposed head in main audit context\n"
    "        if: github.event_name == 'pull_request'\n"
    "        env:\n"
    "          PR_HEAD_SHA: ${{ github.event.pull_request.head.sha }}\n"
    "        run: |\n"
    "          git checkout --detach \"$PR_HEAD_SHA\"\n"
    "          python tools/ontology_checker/check.py tools/ontology_checker/fixtures --context main\n",
)

print("F7 materialization complete")
