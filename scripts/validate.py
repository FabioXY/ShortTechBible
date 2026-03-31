#!/usr/bin/env python3
"""
validate.py — ShortTechBible entry validator
Checks every file in entries/ against the spec and reports all violations.
Exit code: 0 = all good, 1 = one or more errors found.
"""

import re
import sys
import os
from pathlib import Path
from collections import defaultdict

# ── Constants ────────────────────────────────────────────────────────────────

ENTRIES_DIR = Path(__file__).parent.parent / "entries"

VALID_DIFFICULTIES = {"Base", "Intermediate", "Advanced"}

VALID_CATEGORIES = {
    "Networking", "Security", "OS", "Dev", "Hardware",
    "Cloud", "Database", "AI", "Protocol",
}

# Each entry block is separated by "---" (horizontal rule)
ENTRY_SEPARATOR = re.compile(r"^---\s*$", re.MULTILINE)

# Matches the header line: ## ACRONYM — Full Name  OR  ## ACRONYM
HEADER_RE = re.compile(
    r"^## ([A-Z0-9]+)(?:\s+—\s+(.+))?$"
)

# Matches **Difficulty:** Value
DIFFICULTY_RE = re.compile(
    r"^\*\*Difficulty:\*\*\s+(.+)$"
)

# Matches **Category:** Value
CATEGORY_RE = re.compile(
    r"^\*\*Category:\*\*\s+(.+)$"
)

# ── Data structures ──────────────────────────────────────────────────────────

class ValidationError:
    def __init__(self, filepath: str, entry_index: int, acronym: str, message: str):
        self.filepath = filepath
        self.entry_index = entry_index
        self.acronym = acronym
        self.message = message

    def __str__(self):
        loc = f"{self.filepath} [entry #{self.entry_index}"
        if self.acronym:
            loc += f", acronym: {self.acronym}"
        loc += "]"
        return f"  ✗ {loc}\n    → {self.message}"


# ── Parsing ──────────────────────────────────────────────────────────────────

def parse_entry_block(block: str, filepath: str, index: int) -> dict | None:
    """
    Parse a single entry block and return a dict with extracted fields,
    or None if the block is empty/whitespace.
    """
    lines = block.strip().splitlines()
    if not lines:
        return None

    entry = {
        "raw_block": block,
        "filepath": filepath,
        "index": index,
        "acronym": None,
        "full_name": None,
        "description_lines": [],
        "difficulty": None,
        "category": None,
        "header_found": False,
        "difficulty_found": False,
        "category_found": False,
    }

    i = 0
    # --- Header ---
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines):
        m = HEADER_RE.match(lines[i].strip())
        if m:
            entry["acronym"] = m.group(1)
            entry["full_name"] = m.group(2)
            entry["header_found"] = True
        i += 1

    # --- Body: collect description lines and metadata ---
    desc_lines = []
    in_desc = True
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        dm = DIFFICULTY_RE.match(stripped)
        cm = CATEGORY_RE.match(stripped)

        if dm:
            entry["difficulty"] = dm.group(1).strip()
            entry["difficulty_found"] = True
            in_desc = False
        elif cm:
            entry["category"] = cm.group(1).strip()
            entry["category_found"] = True
            in_desc = False
        elif in_desc and stripped:
            desc_lines.append(stripped)
        i += 1

    entry["description_lines"] = desc_lines
    return entry


def load_file(filepath: Path) -> list[dict]:
    """Split a letter file into entry blocks and parse each one."""
    text = filepath.read_text(encoding="utf-8")
    raw_blocks = ENTRY_SEPARATOR.split(text)
    entries = []
    for idx, block in enumerate(raw_blocks, start=1):
        parsed = parse_entry_block(block, str(filepath.name), idx)
        if parsed is not None:
            entries.append(parsed)
    return entries


# ── Validation rules ─────────────────────────────────────────────────────────

def validate_entry(entry: dict) -> list[ValidationError]:
    errors = []
    fp = entry["filepath"]
    idx = entry["index"]
    acr = entry.get("acronym") or "UNKNOWN"

    def err(msg):
        errors.append(ValidationError(fp, idx, acr, msg))

    # 1. Header present
    if not entry["header_found"]:
        err("Missing or malformed header. Expected: ## ACRONYM — Full Name")
        return errors  # Can't validate further without header

    # 2. Acronym length (3–6 chars, A-Z0-9)
    acronym = entry["acronym"]
    if not re.match(r"^[A-Z0-9]{3,6}$", acronym):
        err(
            f"Acronym '{acronym}' is invalid. Must be 3–4 uppercase letters/digits only."
        )

    # 3. Full name recommended (warn, not error — some acronyms are the name)
    # We do not block on missing full name; it's optional per spec.

    # 4. Description: 1–5 non-empty lines
    desc = entry["description_lines"]
    if len(desc) == 0:
        err("Description is missing. At least 1 line required.")
    elif len(desc) > 5:
        err(
            f"Description is too long: {len(desc)} lines. Maximum is 5 lines."
        )

    # 5. Difficulty present and valid
    if not entry["difficulty_found"]:
        err("Missing **Difficulty:** field.")
    elif entry["difficulty"] not in VALID_DIFFICULTIES:
        err(
            f"Invalid difficulty '{entry['difficulty']}'. "
            f"Allowed: {', '.join(sorted(VALID_DIFFICULTIES))}"
        )

    # 6. Category present and valid
    if not entry["category_found"]:
        err("Missing **Category:** field.")
    elif entry["category"] not in VALID_CATEGORIES:
        err(
            f"Invalid category '{entry['category']}'. "
            f"Allowed: {', '.join(sorted(VALID_CATEGORIES))}"
        )

    return errors


def check_duplicates(all_entries: list[dict]) -> list[ValidationError]:
    """Find global duplicate acronyms across all files."""
    seen: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for entry in all_entries:
        acr = entry.get("acronym")
        if acr:
            seen[acr].append((entry["filepath"], entry["index"]))

    errors = []
    for acr, locations in seen.items():
        if len(locations) > 1:
            loc_str = ", ".join(f"{fp} entry #{idx}" for fp, idx in locations)
            errors.append(
                ValidationError(
                    locations[0][0],
                    locations[0][1],
                    acr,
                    f"Duplicate acronym '{acr}' found in: {loc_str}",
                )
            )
    return errors


def check_filename_vs_content(filepath: Path, entries: list[dict]) -> list[ValidationError]:
    """Ensure all acronyms in a file start with the correct letter."""
    expected_letter = filepath.stem.upper()  # e.g. "A" from "A.md"
    errors = []
    for entry in entries:
        acr = entry.get("acronym")
        if acr and not acr.startswith(expected_letter):
            errors.append(
                ValidationError(
                    filepath.name,
                    entry["index"],
                    acr,
                    f"Acronym '{acr}' does not start with '{expected_letter}' "
                    f"but is in {filepath.name}.",
                )
            )
    return errors


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> int:
    if not ENTRIES_DIR.exists():
        print(f"[ERROR] entries/ directory not found at: {ENTRIES_DIR}")
        return 1

    md_files = sorted(ENTRIES_DIR.glob("*.md"))
    if not md_files:
        print("[ERROR] No .md files found in entries/")
        return 1

    all_errors: list[ValidationError] = []
    all_entries: list[dict] = []
    file_stats: dict[str, int] = {}

    print(f"\n{'─'*60}")
    print(" ShortTechBible — Entry Validator")
    print(f"{'─'*60}")
    print(f" Scanning {len(md_files)} files in {ENTRIES_DIR}/\n")

    for md_file in md_files:
        entries = load_file(md_file)
        file_errors: list[ValidationError] = []

        for entry in entries:
            file_errors.extend(validate_entry(entry))

        file_errors.extend(check_filename_vs_content(md_file, entries))

        all_entries.extend(entries)
        all_errors.extend(file_errors)
        file_stats[md_file.name] = len(entries)

        status = "✓" if not file_errors else f"✗ ({len(file_errors)} error(s))"
        print(f"  {md_file.name:8s}  {len(entries):3d} entries  {status}")

    # Global duplicate check
    dup_errors = check_duplicates(all_entries)
    all_errors.extend(dup_errors)

    total_entries = len(all_entries)
    total_errors = len(all_errors)

    print(f"\n{'─'*60}")
    print(f" Total entries scanned : {total_entries}")
    print(f" Total errors found    : {total_errors}")
    print(f"{'─'*60}\n")

    if total_errors == 0:
        print(" ✅  All entries are valid. Ready to build.\n")
        return 0

    print(" ❌  Validation FAILED. Fix the following errors:\n")
    for error in all_errors:
        print(str(error))
        print()

    return 1


if __name__ == "__main__":
    sys.exit(main())
