"""
repo_lint.py — The Poole Manifold Repository Structure Linter
==============================================================
Detects structural issues without touching any files.
Run from the repository root directory.

Usage:
    python repo_lint.py                    # Lint current directory
    python repo_lint.py /path/to/repo      # Lint specific path

Exit 0 = no issues found
Exit 1 = issues found — review output

Rooke Alan Poole | @rookepoole | May 2026
Collaboration: @LabyrinthCoder
"""

import os
import re
import sys
import json
import hashlib
from pathlib import Path
from collections import defaultdict


# ── Configuration ─────────────────────────────────────────────────────────────

EXPECTED_ROOT_DOCS = {
    'README.md',
    'WHAT_THIS_IS.md',
    'KNOWN_GAPS.md',
    'STRUCTURE.md',
    'RESEARCH_MAP.md',
    'RESEARCH_STATUS_LEDGER.md',
    'ARCHITECTURE_DIAGRAMS.md',
    'COMMON_MISUNDERSTANDINGS.md',
    'TERMINOLOGY.md',
    'TERMINOLOGY.md',
    'JOURNAL.md',
    'CHANGELOG.md',
    'CONTRIBUTING.md',
    'CITATION.cff',
    'requirements.txt',
    'LICENSE',
    '.gitignore',
}

VALID_EPISTEMIC_MARKERS = {
    'success', 'fail', 'fixed', 'partial success', 'confirmed',
    'validated', 'verified', 'experimental', 'deprecated',
}

BINARY_EXTENSIONS = {'.pdf', '.npy', '.npz', '.h5', '.png', '.jpg',
                     '.jpeg', '.gif', '.pkl', '.fits'}

MAX_FILENAME_LENGTH = 120  # GitHub truncates at ~256 but long names hurt readability


# ── Issue types ───────────────────────────────────────────────────────────────

class Issue:
    def __init__(self, severity, category, message, path=''):
        self.severity = severity   # CRITICAL / WARNING / INFO
        self.category = category
        self.message  = message
        self.path     = path

    def __repr__(self):
        loc = f' [{self.path}]' if self.path else ''
        return f'[{self.severity}] {self.category}: {self.message}{loc}'


# ── Linter ────────────────────────────────────────────────────────────────────

class RepoLinter:
    def __init__(self, root: Path):
        self.root   = root
        self.issues = []
        self.checks = []

    def run(self) -> list[Issue]:
        self._check_root_docs()
        self._check_duplicate_trial_numbers()
        self._check_filename_issues()
        self._check_duplicate_folder_names()
        self._check_empty_folders()
        self._check_orphan_data_files()
        self._check_cryptographic_worm()
        self._check_code_references()
        self._check_badge_links()
        return self.issues

    def _add(self, severity, category, message, path=''):
        self.issues.append(Issue(severity, category, message, path))

    def _ok(self, message):
        self.checks.append(message)

    def _check_root_docs(self):
        """All expected root-level documentation files present."""
        root_files = {f.name for f in self.root.iterdir() if f.is_file()}
        for doc in sorted(EXPECTED_ROOT_DOCS):
            if doc in root_files:
                self._ok(f'Root doc present: {doc}')
            else:
                self._add('WARNING', 'ROOT_DOCS',
                    f'Expected root doc missing: {doc}')

    def _check_duplicate_trial_numbers(self):
        """Detect experiments sharing the same trial number."""
        trial_map = defaultdict(list)
        for item in self.root.iterdir():
            name = item.name
            m = re.match(r'Trial (\d+)', name)
            if m:
                trial_map[m.group(1)].append(name)

        duplicates = {k: v for k, v in trial_map.items() if len(v) > 1}
        if duplicates:
            for num, names in sorted(duplicates.items()):
                self._add('WARNING', 'DUPLICATE_TRIAL',
                    f'Trial {num} has {len(names)} entries: {names[0][:40]}...',
                    f'root/Trial {num}')
        else:
            self._ok('No duplicate trial numbers found')

    def _check_filename_issues(self):
        """Detect problematic filename patterns."""
        long_names = []
        double_spaces = []
        trailing_spaces = []

        for item in self.root.iterdir():
            name = item.name
            if len(name) > MAX_FILENAME_LENGTH:
                long_names.append(name[:60] + '...')
            if '  ' in name:
                double_spaces.append(name[:60])
            if name != name.rstrip():
                trailing_spaces.append(repr(name))

        if long_names:
            for n in long_names[:3]:
                self._add('INFO', 'FILENAME',
                    f'Very long filename (>{MAX_FILENAME_LENGTH} chars): {n}')
        else:
            self._ok('No excessively long filenames')

        if double_spaces:
            for n in double_spaces:
                self._add('WARNING', 'FILENAME',
                    f'Double space in filename: {n}')
        else:
            self._ok('No double spaces in filenames')

        if trailing_spaces:
            for n in trailing_spaces:
                self._add('CRITICAL', 'FILENAME',
                    f'Trailing space in filename: {n}')
        else:
            self._ok('No trailing spaces in filenames')

    def _check_duplicate_folder_names(self):
        """Detect folders that differ only in whitespace (common accident)."""
        folder_names = [f.name for f in self.root.iterdir() if f.is_dir()]
        normalised = defaultdict(list)
        for name in folder_names:
            normalised[name.strip()].append(name)

        for norm, variants in normalised.items():
            if len(variants) > 1:
                self._add('WARNING', 'DUPLICATE_FOLDER',
                    f'Near-duplicate folders: {variants}')
        if not any(len(v) > 1 for v in normalised.values()):
            self._ok('No duplicate folder names found')

    def _check_empty_folders(self):
        """Detect folders with only .gitkeep (intentional placeholder)."""
        for item in self.root.iterdir():
            if item.is_dir():
                contents = list(item.iterdir())
                non_keep = [f for f in contents if f.name != '.gitkeep']
                if len(contents) > 0 and len(non_keep) == 0:
                    self._add('INFO', 'EMPTY_FOLDER',
                        f'Folder contains only .gitkeep: {item.name}',
                        str(item.name))

    def _check_orphan_data_files(self):
        """Detect binary/data files at root that may be unintentional."""
        for item in self.root.iterdir():
            if item.is_file():
                if item.suffix.lower() in BINARY_EXTENSIONS:
                    self._add('INFO', 'DATA_FILE',
                        f'Binary/data file at root level: {item.name} '
                        f'({item.stat().st_size // 1024} KB)',
                        item.name)

    def _check_cryptographic_worm(self):
        """Verify the cryptographic audit receipt exists and is non-empty."""
        worm_dir = self.root / 'Cryptographic Proof WORM'
        worm_dir2 = self.root / 'Cryptographic Proof WORM '  # trailing space variant

        if worm_dir.exists():
            self._ok('Cryptographic Proof WORM folder present')
            receipt = worm_dir / 'Poole_Audit_Receipt.json'
            if receipt.exists():
                try:
                    data = json.loads(receipt.read_text())
                    self._ok('Poole_Audit_Receipt.json is valid JSON')
                except json.JSONDecodeError as e:
                    self._add('CRITICAL', 'WORM',
                        f'Audit receipt is invalid JSON: {e}')
            else:
                self._add('WARNING', 'WORM',
                    'Poole_Audit_Receipt.json missing from WORM folder')

            ledger = worm_dir / 'run_ledger.jsonl'
            if ledger.exists():
                lines = ledger.read_text().strip().splitlines()
                self._ok(f'run_ledger.jsonl present ({len(lines)} entries)')
            else:
                self._add('WARNING', 'WORM', 'run_ledger.jsonl missing')
        else:
            self._add('CRITICAL', 'WORM',
                'Cryptographic Proof WORM folder missing — audit infrastructure absent')

        if worm_dir2.exists():
            self._add('WARNING', 'WORM',
                'Ghost folder exists: "Cryptographic Proof WORM " (trailing space) — '
                'same content as main WORM folder. Remove the ghost.')

    def _check_code_references(self):
        """Check if files in code/ are actually referenced by experiments."""
        code_dir = self.root / 'code'
        if not code_dir.exists():
            self._add('INFO', 'CODE_DIR', 'code/ directory not found')
            return

        code_files = [f.stem for f in code_dir.iterdir()
                      if f.suffix == '.py' and f.name != '.gitkeep']

        if not code_files:
            self._add('INFO', 'CODE_DIR', 'code/ directory contains no .py files')
            return

        # Scan all experiment files for imports
        refs = defaultdict(int)
        for item in self.root.iterdir():
            if item.is_file() and item.suffix.lower() not in BINARY_EXTENSIONS:
                try:
                    content = item.read_text(errors='replace')
                    for cf in code_files:
                        if cf in content:
                            refs[cf] += 1
                except Exception:
                    pass

        for cf in code_files:
            if refs[cf] == 0:
                self._add('WARNING', 'CODE_REFS',
                    f'code/{cf}.py is not referenced by any experiment file')
            else:
                self._ok(f'code/{cf}.py referenced in {refs[cf]} files')

    def _check_badge_links(self):
        """Check README badges for empty links."""
        readme = self.root / 'README.md'
        if not readme.exists():
            return

        content = readme.read_text(errors='replace')
        badge_pattern = re.compile(r'\[!\[([^\]]+)\]\([^\)]+\)\]\(([^\)]*)\)')
        badges = badge_pattern.findall(content)

        empty_badges = [(name, link) for name, link in badges
                        if not link or link == '']
        if empty_badges:
            for name, link in empty_badges:
                self._add('WARNING', 'BADGES',
                    f'Badge "{name}" has empty link — renders but goes nowhere on GitHub')
        else:
            self._ok(f'All {len(badges)} README badges have links')


# ── Report ────────────────────────────────────────────────────────────────────

def print_report(root: Path, issues: list[Issue], checks: list[str]):
    print()
    print('=' * 68)
    print('  POOLE MANIFOLD — REPOSITORY STRUCTURE LINT')
    print(f'  {root}')
    print('=' * 68)
    print()

    criticals = [i for i in issues if i.severity == 'CRITICAL']
    warnings  = [i for i in issues if i.severity == 'WARNING']
    infos     = [i for i in issues if i.severity == 'INFO']

    if criticals:
        print(f'  CRITICAL ({len(criticals)})')
        print('  ' + '─' * 50)
        for i in criticals:
            print(f'  ✗ [{i.category}] {i.message}')
            if i.path:
                print(f'      → {i.path}')
        print()

    if warnings:
        print(f'  WARNINGS ({len(warnings)})')
        print('  ' + '─' * 50)
        for i in warnings:
            print(f'  ⚠ [{i.category}] {i.message}')
            if i.path:
                print(f'      → {i.path}')
        print()

    if infos:
        print(f'  INFO ({len(infos)})')
        print('  ' + '─' * 50)
        for i in infos:
            print(f'  ℹ [{i.category}] {i.message}')
        print()

    print(f'  CHECKS PASSED ({len(checks)})')
    print('  ' + '─' * 50)
    for c in checks:
        print(f'  ✓ {c}')
    print()

    print('=' * 68)
    total = len(issues)
    if not criticals:
        print(f'  RESULT: HEALTHY — {len(checks)} checks passed, '
              f'{len(warnings)} warnings, {len(infos)} info')
    else:
        print(f'  RESULT: ACTION REQUIRED — {len(criticals)} critical, '
              f'{len(warnings)} warnings')
    print('=' * 68)
    print()


def main():
    root_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')

    if not root_path.exists():
        print(f'Path not found: {root_path}')
        sys.exit(1)

    linter = RepoLinter(root_path)
    issues = linter.run()
    print_report(root_path, issues, linter.checks)

    criticals = [i for i in issues if i.severity == 'CRITICAL']
    sys.exit(0 if not criticals else 1)


if __name__ == '__main__':
    main()
