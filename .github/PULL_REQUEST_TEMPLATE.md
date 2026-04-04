## PR Checklist

Before submitting this pull request, confirm you have completed **every item** below.
Unchecked items will result in the PR being closed without review.

### Content validation
- [ ] Each new entry follows the exact format: `## ACRONYM — Full Name`
- [ ] Acronym is 3–6 uppercase characters (A–Z, 0–9 only)
- [ ] Description is 1–5 lines, technically accurate, written in my own words
- [ ] `**Difficulty:**` field is present and set to one of: `Base`, `Intermediate`, `Advanced`
- [ ] `**Category:**` field is present and set to one of: `Networking`, `Security`, `OS`, `Dev`, `Hardware`, `Cloud`, `Database`, `AI`, `Protocol`
- [ ] The acronym does not already exist in the repository (I checked with `Ctrl+F` in the entries/ folder)
- [ ] The entry is placed in the correct letter file (`entries/X.md` where X is the first letter)
- [ ] The entry is separated from adjacent entries with a `---` line

### Process
- [ ] I ran `python scripts/validate.py` locally and got zero errors
- [ ] My branch is named `add/ACRONYM` (e.g., `add/BGP`) or `fix/ACRONYM`
- [ ] I am not modifying any file outside of `entries/` (scripts, README, CI are maintainer-only)
- [ ] My commit message follows the convention: `feat(entries): add ACRONYM — Full Name`

### By submitting this PR
I confirm this content is original, technically accurate, and licensed under MIT.
I agree it may be modified for style and consistency by maintainers.

---
**What acronym(s) does this PR add?**

<!-- List them here, one per line: -->
- `ACRONYM` — Full Name
