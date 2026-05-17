# Repository Structure — Delta RPM Protocol

## Top Level
```
Delta-RPM-Protocol/
  README.md                     — primary documentation
  WHAT_THIS_IS.md               — one-page orientation
  CHANGELOG.md                  — what changed and when
  KNOWN_GAPS.md                 — honest public gap register
  RESEARCH_MAP.md               — research landscape and connections
  RESEARCH_STATUS_LEDGER.md     — current status of all research threads
  ARCHITECTURE_DIAGRAMS.md      — system architecture diagrams
  TERMINOLOGY.md                — canonical definitions
  COMMON_MISUNDERSTANDINGS.md   — proactive epistemic stabilisation
  JOURNAL.md                    — project journal
  CONTRIBUTING.md               — contribution guidelines
  CITATION.cff                  — academic citation
  LICENSE                       — license
  requirements.txt              — Python dependencies
  .gitignore                    — what to ignore
```

## Folders

### experiments/
All computational experiments. Grouped by domain.

```
experiments/
  physics/          — Core Poole Manifold engine, glider/CA, quantum, wave physics
  cosmology/        — BAO, OTG, FLRW, DESI, galaxy rotation, astrophysics
  cpu_logic/        — Fluid CPU architecture, logic gates, adders, memory
  materials/        — Materials science: bone, thermal, EM, fluid, biological
  scifi/            — Sci-fi test scenarios: wormholes, starships, probes
```

### docs/
Supporting documentation and papers.
```
docs/
  papers/           — PDF documents and academic papers
  + misc docs       — protocol docs, strategy notes
```

### code/
Tooling and utilities.
```
code/
  repo_lint.py      — structure linter for this repository
```

### data/
Generated data files and raw outputs.
```
data/
  *.npy             — NumPy array outputs
  *.jsonl           — JSONL data
  *.json            — JSON data
```

### assets/
Images and visual outputs.

---

## A Note on Experiment Filenames
Experiment files retain their original descriptive names.
These names are the experiments' identities — changing them would lose the
research narrative. What changed: they are now findable by domain
instead of buried in a flat root directory.

---

## Rehabilitation Credits
Structure organised by @LabyrinthCoder | May 2026
*"I don't copy. I fork. I don't merge. I slaw."*
Original research: R.A. Poole | Delta RPM Protocol
