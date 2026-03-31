# Contributing to ShortTechBible

Thank you for contributing. This guide contains everything you need to know to submit entries that pass CI on the first try.

---

## The Non-Negotiables

Before anything else, burn these rules into memory:

1. **Acronyms must be exactly 3 to 6 characters.** Uppercase letters and digits only. No hyphens, no lowercase, no punctuation. `TCP` ✓, `HTTP` ✓, `Wi-Fi` ✗, `TLS1.3` ✗.
2. **Zero duplicates.** Search the `entries/` folder before writing anything. `grep -r "^## TCP" entries/` takes 2 seconds.
3. **No placeholder language.** Never write "this is a protocol used for..." — explain the mechanism, the context, and why it matters.
4. **No copy-paste.** Do not copy descriptions from Wikipedia, Cisco docs, or any other source. Write from your understanding.
5. **All content in English.** Even if you are not a native speaker — keep it simple and accurate, maintainers will clean up the grammar.

---

## Entry Format — Exact Specification

Every entry must look exactly like this:

```markdown
## ACRONYM — Full Name

Description text. This is one paragraph of 1 to 5 lines maximum.
You can use two lines if needed. Each line should add information, not repeat it.
Do not pad. If you can say it in one line, use one line.

**Difficulty:** Base
**Category:** Networking
```

### Rules for each field

**Header line**
- Format: `## ACRONYM — Full Name` (two hashes, one space, acronym, space, em dash `—`, space, full name)
- The em dash is `—` (U+2014), not a hyphen `-` or an en dash `–`
- Full name is optional only if the acronym *is* the name (e.g., YAML)
- The acronym in the header must match the acronym used as the key

**Description**
- Minimum: 1 line. Maximum: 5 lines.
- Must explain: what it is, how it works at a high level, and where/why it is used
- Avoid: "It is a...", "This stands for...", filler phrases, marketing language
- Allowed: specific version numbers, port numbers, RFC references, protocol names

**Difficulty**
| Value | Meaning |
|-------|---------|
| `Base` | Used daily by most IT people; no domain specialization required to understand |
| `Intermediate` | Requires background in the relevant domain to fully grasp |
| `Advanced` | Typically known only by specialists; touches low-level internals or niche standards |

When in doubt, go one level higher. It's better to call something Intermediate than to label a complex protocol Base.

**Category**
| Value | Covers |
|-------|--------|
| `Networking` | Protocols, addressing, routing, switching, topologies |
| `Security` | Encryption, authentication, access control, attack types, hardening |
| `OS` | Operating system internals, file systems, boot process, kernel concepts |
| `Dev` | Programming, APIs, frameworks, software engineering practices |
| `Hardware` | Physical components, buses, interfaces, storage media |
| `Cloud` | Virtualization, containers, cloud platforms, distributed infrastructure |
| `Database` | Relational and NoSQL databases, query languages, replication, storage engines |
| `AI` | Machine learning, neural networks, inference, AI infrastructure |
| `Protocol` | Communication standards and formats that don't fit Networking or Security alone |

If an acronym fits two categories, pick the one that best represents its primary use. `SSH` is `Security`, not `Protocol`, because its defining characteristic is encryption and authentication.

---

## Examples: Correct vs Incorrect

### ✓ Correct

```markdown
## TLS — Transport Layer Security

A cryptographic protocol that provides confidentiality, integrity, and authentication
for network communications. TLS runs over TCP and uses asymmetric cryptography for
key exchange, then symmetric ciphers for bulk data. TLS 1.3 reduced handshakes to
1-RTT and removed all weak cipher suites.

**Difficulty:** Intermediate
**Category:** Security
```

### ✗ Incorrect — Too vague, copy-paste smell, wrong format

```markdown
## TLS - Transport Layer Security

TLS is a protocol that is used for securing communication over the internet.
It is widely used in HTTPS and other applications. TLS provides encryption.

**Difficulty:** easy
**Category:** network security
```

Problems: hyphen instead of em dash, generic description, repetitive, wrong difficulty value, wrong category value.

### ✗ Incorrect — Acronym too long

```markdown
## HTTPS — Hypertext Transfer Protocol Secure
```

`HTTPS` is 5 characters. Not accepted.

### ✗ Incorrect — Missing fields

```markdown
## NTP — Network Time Protocol

Synchronizes clocks over the network using UDP port 123.
```

Missing `**Difficulty:**` and `**Category:**` fields. CI will fail.

---

## Separator Between Entries

Within a single letter file, entries are separated by a line containing only `---`:

```markdown
## ABC — Something

Description.

**Difficulty:** Base
**Category:** Dev

---

## ABD — Something Else

Description.

**Difficulty:** Intermediate
**Category:** Networking
```

Do not add blank lines around the `---`. Do not use `***` or `===`.

---

## PR Workflow

```
fork → clone → branch → edit → validate locally → commit → push → open PR
```

1. **Fork** the repository on GitHub.
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/ShortTechBible`
3. **Create a branch**: `git checkout -b add/ACRONYM` (e.g., `add/BGP`)
4. **Edit** the correct `entries/X.md` file.
5. **Validate**: `python scripts/validate.py` — fix all errors before pushing.
6. **Commit**: `git commit -m "feat(entries): add BGP — Border Gateway Protocol"`
7. **Push**: `git push origin add/BGP`
8. **Open a PR** on GitHub. Fill in the PR template completely.

One PR should contain one or a small batch of closely related acronyms.
Do not open a PR that adds 50 acronyms at once — it is very hard to review.

---

## What Happens When You Open a PR

1. The CI pipeline triggers automatically.
2. `validate.py` runs against all files, including yours.
3. If it finds any error, the **merge is blocked** — you will see a red ✗ in the PR.
4. Click the failing check → View logs → Find the exact error (file, entry index, message).
5. Fix the error, commit to the same branch, and push — CI re-runs automatically.
6. A maintainer reviews for content quality (technical accuracy, clarity).
7. Once both CI and human review pass, the PR is merged.
8. The build pipeline runs on `main`, regenerates the PDF/JSON/CSV, and deploys the site.

### Common CI failures and how to fix them

| Error | Fix |
|-------|-----|
| `Acronym 'HTTPS' is invalid. Must be 3–6 chars` | The acronym has 7+ characters. Not accepted by design. |
| `Missing **Difficulty:** field` | Add the field. Check spacing — it must be exactly `**Difficulty:** Value` |
| `Invalid category 'network'` | Use the exact capitalized value: `Networking` not `network` |
| `Duplicate acronym 'DNS'` | DNS is already in the repo. Do not re-add existing acronyms. |
| `Acronym 'BGP' does not start with 'A' but is in A.md` | Move the entry to `entries/B.md` |
| `Description is too long: 6 lines` | Trim your description to 5 lines maximum. |

---

## What Maintainers Will Not Merge

- Entries that already exist in the repo
- Acronyms with fewer than 3 or more than 6 characters
- Descriptions copied from Wikipedia or any other source
- Entries without Difficulty or Category fields
- Entries with invalid Difficulty or Category values
- PRs that modify files outside `entries/` (scripts, README, CI are maintainer-only)
- Entries that are product names, not standard acronyms (e.g., `AWS` is accepted as it's a universal term; a niche vendor-specific abbreviation with no wider standard use is not)

---

## Running the Build Locally (optional)

If you want to test the full build pipeline:

```bash
# Python 3.10+ required
python scripts/validate.py   # Check for errors

# For PDF generation, also install:
# Ubuntu/Debian: sudo apt install pandoc texlive-xetex texlive-fonts-recommended
# macOS: brew install pandoc && brew install --cask mactex
python scripts/build.py      # Generates dist/ files and updates README
```

---

## Questions?

Open a [Discussion](https://github.com/YOUR_USERNAME/ShortTechBible/discussions) or a [Bug Report issue](https://github.com/YOUR_USERNAME/ShortTechBible/issues/new?template=bug_report.md).

Do not open issues to ask questions that are answered in this document.
