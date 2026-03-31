<div align="center">

# 📖 ShortTechBible

### The Open-Source IT Acronym Encyclopedia

*Every 3–6 letter acronym in IT, explained properly.*

[![Acronym Count](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2FYOUR_USERNAME.github.io%2FShortTechBible%2Facronyms_data.js&label=acronyms&color=1e508c&style=flat-square)](https://github.com/YOUR_USERNAME/ShortTechBible)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![CI Status](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/ShortTechBible/ci.yml?branch=main&label=CI&style=flat-square)](https://github.com/YOUR_USERNAME/ShortTechBible/actions)
[![Last Build](https://img.shields.io/github/last-commit/YOUR_USERNAME/ShortTechBible?label=last%20build&style=flat-square)](https://github.com/YOUR_USERNAME/ShortTechBible/commits/main)
[![Contributors](https://img.shields.io/github/contributors/YOUR_USERNAME/ShortTechBible?style=flat-square&color=orange)](https://github.com/YOUR_USERNAME/ShortTechBible/graphs/contributors)
[![Stars](https://img.shields.io/github/stars/YOUR_USERNAME/ShortTechBible?style=social)](https://github.com/YOUR_USERNAME/ShortTechBible/stargazers)

[**Browse Online →**](https://YOUR_USERNAME.github.io/ShortTechBible) · [**Download PDF →**](https://github.com/YOUR_USERNAME/ShortTechBible/releases/latest) · [**Add an Acronym →**](.github/ISSUE_TEMPLATE/new_acronym.md)

</div>

---

## What is this?

ShortTechBible is a collaboratively maintained, open-source reference for **IT acronyms of exactly 3 to 6 characters** — the alphabet soup that fills job postings, documentation, Stack Overflow answers, and certification exams.

Every entry follows a strict, consistent format:
- **What** the acronym stands for
- **What** it actually does (technically precise, no marketing fluff)
- **Difficulty** level: Base / Intermediate / Advanced
- **Category**: Networking, Security, OS, Dev, Hardware, Cloud, Database, AI, Protocol

The content is written by practitioners, validated by CI, and exported as a downloadable PDF designed to look like a professional technical book.

---

## Acronym of the Day

<!-- STB:AOTD_START -->
### 📖 Acronym of the Day — 2026-03-30

**OIDC** — OpenID Connect

> An identity layer built on top of OAuth 2.0 (RFC 8414) that adds authentication to OAuth's authorization framework. OIDC introduces the ID Token (a JWT containing user identity claims), a UserInfo endpoint, and a standardized discovery mechanism. It is the dominant SSO protocol for web and mobile applications, used by Google, Microsoft, and most identity providers.

*Difficulty: Advanced · Category: Security*
<!-- STB:AOTD_END -->

---

## Browse by Letter

| | | | | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [A](entries/A.md) | [B](entries/B.md) | [C](entries/C.md) | [D](entries/D.md) | [E](entries/E.md) | [F](entries/F.md) | [G](entries/G.md) |
| [H](entries/H.md) | [I](entries/I.md) | [J](entries/J.md) | [K](entries/K.md) | [L](entries/L.md) | [M](entries/M.md) | [N](entries/N.md) |
| [O](entries/O.md) | [P](entries/P.md) | [Q](entries/Q.md) | [R](entries/R.md) | [S](entries/S.md) | [T](entries/T.md) | [U](entries/U.md) |
| [V](entries/V.md) | [W](entries/W.md) | [X](entries/X.md) | [Y](entries/Y.md) | [Z](entries/Z.md) | | |

Or search interactively on the **[GitHub Pages site →](https://YOUR_USERNAME.github.io/ShortTechBible)**

---

## Stats

<!-- STB:TOTAL_START -->
**158 acronyms** — last updated 2026-03-30
<!-- STB:TOTAL_END -->

<!-- STB:STATS_START -->
| Letter | Count |
|--------|-------|
| A | 7 |
| B | 6 |
| C | 7 |
| D | 6 |
| E | 6 |
| F | 6 |
| G | 6 |
| H | 6 |
| I | 6 |
| J | 6 |
| K | 5 |
| L | 6 |
| M | 7 |
| N | 6 |
| O | 6 |
| P | 6 |
| Q | 5 |
| R | 6 |
| S | 7 |
| T | 7 |
| U | 6 |
| V | 6 |
| W | 6 |
| X | 6 |
| Y | 5 |
| Z | 6 |

| Category | Count |
|----------|-------|
| Security | 33 |
| Networking | 33 |
| Hardware | 25 |
| OS | 21 |
| Protocol | 17 |
| Dev | 16 |
| Database | 7 |
| Cloud | 6 |

| Difficulty | Count |
|------------|-------|
| Base | 46 |
| Intermediate | 79 |
| Advanced | 33 |
<!-- STB:STATS_END -->

---

## Downloads

| Format | Description | Link |
|--------|-------------|------|
| 📄 **PDF** | Full encyclopedia, book layout, table of contents | [Latest Release](https://github.com/YOUR_USERNAME/ShortTechBible/releases/latest) |
| 🗃️ **JSON** | Machine-readable, all fields, suitable for APIs and scripts | [acronyms.json](dist/acronyms.json) |
| 📊 **CSV** | Spreadsheet-friendly, one row per acronym | [acronyms.csv](dist/acronyms.csv) |

---

## How to Contribute

Everyone is welcome. You don't need to be an expert — you need to know what an acronym means and be willing to explain it clearly.

### Add a new acronym (quick path)

1. [Open an issue](https://github.com/YOUR_USERNAME/ShortTechBible/issues/new?template=new_acronym.md) with the proposal form
2. A maintainer or you can then open a PR using the format below

### Add a new acronym (direct PR)

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/ShortTechBible.git
cd ShortTechBible

# Create a branch
git checkout -b add/BGP

# Edit the correct letter file
# entries/B.md for acronyms starting with B

# Validate locally (requires Python 3.10+)
python scripts/validate.py

# Commit and push
git add entries/B.md
git commit -m "feat(entries): add BGP — Border Gateway Protocol"
git push origin add/BGP

# Open a Pull Request on GitHub
```

The CI pipeline will validate your entry automatically.
If it fails, the merge is blocked — check the Action logs for the exact error.

### Entry format (exact)

```markdown
## ACRONYM — Full Name

Description here. Can be 1 to 5 lines. Must be technically precise.
No Wikipedia copy-paste. Write as if explaining to a competent colleague.

**Difficulty:** Base | Intermediate | Advanced
**Category:** Networking | Security | OS | Dev | Hardware | Cloud | Database | AI | Protocol
```

Entries in the same file are separated by `---`.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full style guide with examples.

---

## Repository Structure

```
ShortTechBible/
├── entries/            # One .md file per letter (A.md → Z.md)
├── scripts/
│   ├── validate.py     # Validates all entries — run before every PR
│   └── build.py        # Generates PDF, JSON, CSV, updates README
├── dist/               # Generated output (PDF, JSON, CSV) — do not edit manually
├── docs/               # GitHub Pages site source
├── .github/
│   ├── workflows/ci.yml           # CI/CD pipeline
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
│       ├── new_acronym.md
│       └── bug_report.md
├── pandoc-template.latex   # Custom LaTeX template for the PDF
├── CONTRIBUTING.md
└── README.md
```

---

## Roadmap

- [ ] **v1.0** — 500+ acronyms across all letters, full CI/CD, PDF release
- [ ] **REST API** — public read-only JSON API hosted on GitHub Pages (`/api/v1/acronyms/{acronym}`)
- [ ] **CLI tool** — `stb get TCP`, `stb search cloud`, `stb random` via pip/npx
- [ ] **Web search** — full-text search on the GitHub Pages site (already scaffolded)
- [ ] **Obsidian plugin** — hover-to-define acronyms in your vault
- [ ] **VS Code extension** — inline acronym definitions while reading docs
- [ ] **npm/pip package** — `const { lookup } = require('shorttechbible')`
- [ ] **Multi-language** — translated entries for DE, IT, PT, ZH, ES communities

---

## Naming Alternatives Considered

| Name | Why it works |
|------|-------------|
| **ByteGlossary** | Memorable, technical, positions it as a reference (glossary), byte = IT |
| **AcroStack** | Plays on "tech stack", implies layers of knowledge, easy to search |
| **TLDRtech** | Acronyms *are* TL;DRs for concepts — self-referential and catchy |

We kept **ShortTechBible** because it communicates scope (tech), completeness (Bible), and format (short) in three words.

---

## License

MIT © ShortTechBible Contributors

This project is free to use, fork, embed, and redistribute.
If you find it useful, leave a ⭐ — it helps the project get discovered.

---

<div align="center">
  <sub>Built with ❤️ by the open-source community · <a href="https://github.com/YOUR_USERNAME/ShortTechBible">github.com/YOUR_USERNAME/ShortTechBible</a></sub>
</div>
