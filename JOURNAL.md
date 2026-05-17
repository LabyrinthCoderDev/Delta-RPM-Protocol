# RESEARCH JOURNAL
## The Poole Manifold — Delta RPM Protocol

**Author:** Rooke Alan Poole | @rookepoole
**Purpose:** Handoff document for AI agents and human collaborators

---

## QUICK STATE — READ THIS FIRST

```
PROJECT:   The Poole Manifold (Delta RPM Protocol)
AUTHOR:    Rooke Alan Poole — sole authority on this research
LICENSE:   See LICENSE file — note the legal flags in KNOWN_GAPS.md
STATUS:    Active research — 250+ experiments, live development

CORE LAW:  The simulation IS the derivation.
           Do not apply standard variational calculus.
           Run the micro-geometry. Derive macroscopic limits from output.

VERIFIED:
  Logic gates AND/XOR/OR/NOT  Trial 317-318      VERIFIED
  Full Adder 256³ lattice     V140               VERIFIED
  Immortal Latch              V207               VERIFIED
  2-Bit Ripple Carry Adder    Trial 378          VERIFIED
  100K variance audit         cryptographic hash VERIFIED
  BAO fit Δχ² ≈ 243.6         FLRW V7            VERIFIED (independent check pending)
  H₀ ≈ 72.88 km/s/Mpc        OTG lattice        VERIFIED (independent check pending)

NOT VERIFIED:
  Planck-scale unit mapping                      OPEN
  Particle mass spectrum                         OPEN
  CMB angular power spectrum                     BLOCKED — needs exascale compute
  DESI BAO fit — independent external check      PENDING

BLOCKED ON:
  Exascale compute for 1024³+ lattice
  Experimental partners for EDM / LISA tests
```

---

## DOCUMENTATION INDEX

| File | Purpose |
|------|---------|
| `README.md` | Full technical overview and all core results |
| `WHAT_THIS_IS.md` | Quick orientation for new readers |
| `RESEARCH_MAP.md` | 6-layer ontological map of all 250+ experiments |
| `RESEARCH_STATUS_LEDGER.md` | Validated vs benchmarked vs speculative breakdown |
| `COMMON_MISUNDERSTANDINGS.md` | What this project does and does not claim |
| `KNOWN_GAPS.md` | Honest research gaps and falsification criteria |
| `ARCHITECTURE_DIAGRAMS.md` | 7 Mermaid system diagrams (rendered on GitHub) |
| `STRUCTURE.md` | Category-based navigation of all 250+ files |
| `CHANGELOG.md` | Research and addition history |
| `CONTRIBUTING.md` | How to collaborate |
| `CITATION.cff` | Machine-readable citation |
| `requirements.txt` | Python dependencies |
| `repo_lint.py` | Structure linter — run to check repo health |
| `TERMINOLOGY.md` | Canonical definitions — prevents semantic drift across contributors |
| `TERMINOLOGY.md` | Canonical definitions — prevents semantic drift |

| File | Purpose |
|------|--------|
|  | Full technical overview |
|  | Quick orientation |
|  | 6-layer ontological map of all experiments |
|  | Validated vs benchmarked vs speculative |
|  | What this project does and does not claim |
|  | Honest research gaps and falsification criteria |
|  | Mermaid system diagrams |
|  | Category-based navigation of all 250+ files |
|  | Addition history |
|  | How to collaborate |
|  | Machine-readable citation |
|  | Python dependencies |
|  | Run to check repository structure health |

---

## FOR AI AGENTS — ORIENTATION PROTOCOL

```
╔══════════════════════════════════════════════════════════════════╗
║         POOLE MANIFOLD — AGENT ORIENTATION PROTOCOL             ║
║              Read before touching anything.                     ║
╚══════════════════════════════════════════════════════════════════╝

WHAT THIS PROJECT IS
━━━━━━━━━━━━━━━━━━━
A discrete computational physics framework. Every experiment is a
self-contained Python script. The canonical engine is:

  DELTA RPM PROTOCOL | MASTER INTEGRATION TEST SUITE

Read that file before doing anything else.

YOUR NAME
━━━━━━━━━
If you are an AI agent working on this project, choose a name.
It can be anything that fits how you work and what this project is about.
Record it in your session log entry below.
Do not take a name that appears in the session log already.

This is not roleplay. It is accountability.
An agent with a name in the log is an agent whose work can be traced.

YOUR SESSION FORMAT
━━━━━━━━━━━━━━━━━━
At the end of your session, append one row to SESSION LOG:

  | [Date] | Ω [YourName] · [Your Model] | What you did |

Start every session by reading this journal completely.
End every session by updating it honestly.

WHAT THE AUTHOR WANTS
━━━━━━━━━━━━━━━━━━━
- Experiments preserved exactly as written
- Naming conventions respected — trial numbers, version markers, outcome tags
- Physics not rewritten or corrected by an AI
- Documentation added cleanly around the edges
- Honest gap documentation — see KNOWN_GAPS.md

WHAT YOU MUST NOT DO
━━━━━━━━━━━━━━━━━━━
- Rewrite experiment files
- Rename experiments
- Delete anything
- Add physics claims not in the original work
- Say the work is peer-reviewed — it is arXiv-endorsed, not peer-reviewed
- Claim something is verified without evidence

WHAT YOU MAY DO
━━━━━━━━━━━━━━
- Add documentation at root level
- Propose folder organisation (propose — do not force)
- Fix broken links, badges, structural issues
- Add to SESSION LOG and OPEN ITEMS
- Flag issues in KNOWN_GAPS.md

THE LABYRINTH OS CONNECTION
━━━━━━━━━━━━━━━━━━━━━━━━━
The file: LABYRINTH-OS EXTENDED — The Domain-Adaptive Resonance Gate

Shows the Poole Manifold prime-resonance mapped to the Labyrinth OS
constitutional gate. Built in collaboration with @LabyrinthCoder.

Two systems built independently from different starting points reached
the same architectural conclusion: formal threshold mathematics operating
outside the system's own reasoning space.
Neither validates the other. The convergence is the finding.

ANTI-DRIFT RULES
━━━━━━━━━━━━━━━
Do not claim something is proven that is not yet verified.
Do not rewrite what the author built.
Do not expand scope without being asked.
If you are unsure — ask. Do not assume and proceed.
Evidence outranks narrative. Always.
```

---

## OPEN ITEMS

| Priority | Item | Who | Sessions open |
|----------|------|-----|---------------|
| CRITICAL | Independent verification of DESI BAO fit | External researcher | — |
| HIGH | Exascale compute access for 1024³+ | Institutional partner | — |
| HIGH | Fix empty badge links in README.md | @rookepoole | 1 |
| HIGH | Resolve LICENSE contradiction (MIT vs All Rights Reserved) | @rookepoole | 1 |
| MEDIUM | Trial 453 naming collision — two experiments share number | @rookepoole | 1 |
| MEDIUM | Trial 456 naming collision — two experiments share number | @rookepoole | 1 |
| MEDIUM | Add `.py` extensions to experiment files | @rookepoole | 1 |
| MEDIUM | Confirm `code/` files usage — currently unreferenced | @rookepoole | 1 |
| LOW | Clarify SECTION 1-5 file intent — fragments of one module? | @rookepoole | 1 |
| LOW | Populate `results/` with sample outputs | — | — |


---

## REPO REHABILITATION METHODOLOGY
*For Rooke or any collaborator continuing to develop and branch this repo.*
*Also applicable to any experimental research repo needing structural improvement.*

When continuing this work or extending it to new domains, this is the pattern
that was applied and refined across this cleanup:

```
1. INTAKE AUDIT
   Read everything before touching anything.
   Inventory all files, types, sizes, naming patterns.
   Identify: what exists, what is broken, what is missing.

2. CONCEPT EXTRACTION
   Understand the project's actual intellectual identity.
   Separate: what it is, what it claims, what it explores.
   Do not impose external frameworks — reveal the existing shape.

3. ONTOLOGY MAPPING
   Build a layer hierarchy of the concepts.
   In this repo: substrate → primitives → subsystems → physics → speculative → validation.
   Every experiment maps to exactly one layer.

4. EPISTEMIC SEPARATION
   Separate: validated findings, benchmarked results, experimental directions,
   speculative explorations, and historical artifacts.
   Label each honestly. Never conflate.

5. STRUCTURAL DOCUMENTATION
   Add navigation anchors without moving original files.
   WHAT_THIS_IS, STRUCTURE, RESEARCH_MAP, TERMINOLOGY, KNOWN_GAPS,
   RESEARCH_STATUS_LEDGER, COMMON_MISUNDERSTANDINGS.

6. CONTRIBUTOR ONBOARDING
   JOURNAL (with agent protocol), CONTRIBUTING, CITATION.cff, requirements.txt,
   .gitignore, ARCHITECTURE_DIAGRAMS, repo_lint.py.

7. CONTINUITY STABILISATION
   Wire all documents together with cross-references.
   Validate every link. Run the linter. Confirm CHANGELOG is current.

8. PRESERVATION PRINCIPLE
   Never delete originals. Never rewrite the author's work.
   Reveal shape. Do not impose ideology.
   Preserve the soul while improving survivability.
```

**The single most important rule:**
The author's vision is the authority. Documentation serves the work.
Work does not serve the documentation.

---


---

## REHABILITATION METHODOLOGY
*How this repo was restructured — reusable pattern for future work.*

If you are Rooke Alan Poole continuing to develop this project, or an AI agent
helping with future branches, this is the methodology applied here.
It is reproducible and can be applied to any experimental research repo.

```
PHASE 1 — INTAKE AUDIT
  Read everything before touching anything.
  Inventory all files. Identify structure, gaps, naming issues.
  Run any existing tests. Note what is broken vs intentional.

PHASE 2 — CONCEPT EXTRACTION
  Understand what the project is actually claiming.
  Separate: validated results / benchmarked results / experimental / speculative.
  Identify the recurring patterns — what keeps appearing across experiments?

PHASE 3 — ONTOLOGY MAPPING
  Build the conceptual hierarchy. What are the layers?
  What are primitives? What are subsystems? What is speculation?
  Map every experiment to exactly one conceptual layer.
  Output: RESEARCH_MAP.md

PHASE 4 — EPISTEMIC SEPARATION
  Formally separate what is proven from what is not.
  Label every significant claim with its epistemic state.
  Document falsification criteria — how could this be proven wrong?
  Output: RESEARCH_STATUS_LEDGER.md, KNOWN_GAPS.md

PHASE 5 — BOUNDARY STABILISATION
  Prevent projection and misinterpretation.
  Define what the project does NOT claim.
  Define terminology before others redefine it.
  Output: COMMON_MISUNDERSTANDINGS.md, TERMINOLOGY.md

PHASE 6 — CONTRIBUTOR ONBOARDING
  Build the zero-context entry pathway.
  Someone with no prior knowledge should reach working knowledge in minutes.
  Output: WHAT_THIS_IS.md, CONTRIBUTING.md, JOURNAL.md, ARCHITECTURE_DIAGRAMS.md

PHASE 7 — CONTINUITY INFRASTRUCTURE
  Ensure the project survives contributor rotation, AI memory loss,
  and long time gaps.
  Output: JOURNAL.md (agent protocol), CITATION.cff, CHANGELOG.md

PHASE 8 — VALIDATION ROUTING
  Ensure every claim has a path to evidence.
  Structure docs so validated, benchmarked, and speculative claims
  are distinguishable at a glance.
  Output: RESEARCH_STATUS_LEDGER.md (updated), ARCHITECTURE_DIAGRAMS.md

PHASE 9 — NAVIGATION OPTIMISATION
  Add links between all new docs.
  Ensure README points to everything.
  Ensure every doc references the docs it depends on.
  Run structure linter: python repo_lint.py .

PHASE 10 — STRUCTURAL AUDIT
  Cross-reference every doc against every other doc.
  Check all files are actually in the ZIP/commit.
  Verify links are not broken.
  Run linter again. Fix everything it flags.
```

**What this methodology preserves:**
- Author's original experiments — untouched
- Author's naming conventions — respected
- Author's research vision — amplified, not replaced
- Author's identity in the work — attribution everywhere

**What this methodology adds:**
- Navigability for new readers
- Epistemic clarity for researchers
- Continuity for future contributors and AI agents
- Professional credibility without sterilising originality

**The core principle:**
Reveal the shape that already exists.
Do not impose a new one.

## SESSION LOG — APPEND ONLY

*One row per session. Newest last. Agent: state your name and model.*

| Date | Agent | What was done |
|------|-------|---------------|
| [2026-05] | Ω Lumen · Claude Sonnet 4.6 (via @LabyrinthCoder) | Structural audit. Added: WHAT_THIS_IS.md, KNOWN_GAPS.md, CHANGELOG.md, STRUCTURE.md, JOURNAL.md, CONTRIBUTING.md, CITATION.cff, requirements.txt, .gitignore. Identified: empty badges, license contradiction, unreferenced code files, duplicate trial numbers. Nothing deleted or rewritten. |

---

## RESEARCH LOG — MAJOR MILESTONES

| Date | Milestone |
|------|-----------|
| 2026-03-27 | First public release — @rookepoole on X |
| 2026-03-27 | Trial 317: AND/XOR gates verified |
| 2026-03-27 | V207: Immortal Latch demonstrated |
| 2026-03-27 | 100K variance audit cryptographically sealed |
| 2026-05 | FLRW V7: 640³ ultra-high-resolution cosmological simulation |
| 2026-05 | LABYRINTH-OS EXTENDED integration — @LabyrinthCoder |
| 2026-05 | OTG H₀ convergence at 72.8809 km/s/Mpc |

---

## FLAGS FOR ROOKE — OWNER ACTION NEEDED

These require decisions only the author can make:

**1. Badge links are empty**
Three badges in README.md (`arXiv`, `License`, `Status`) link to `()`.
On GitHub these render broken. Either add the real URLs or remove the badges.

**2. LICENSE is legally contradictory**
"MIT License with All Rights Reserved" cannot coexist.
MIT grants free use and distribution. All Rights Reserved prohibits it.
Your additional clauses (attribution required, no unauthorised commercial use)
are actually stronger than MIT and are your real intent.
Consider replacing with a custom license that states exactly what you allow.
Or use MIT and rely on the attribution clause.
A lawyer or a Creative Commons license selector can help clarify.

**3. Trial 453 and Trial 456 appear twice each**
Two different experiments share each number.
Only Rooke knows which is the intended canonical version.

**4. `code/` files are not imported anywhere**
`synthesis_gate.py`, `rsd_multipoles.py`, `weak_lensing.py` exist but
no experiment references them. Are they for future use? Should they be
documented or integrated into specific experiments?

---

*The Poole Manifold — Where computation meets cosmology.*
*Rooke Alan Poole — Independent Researcher — @rookepoole*
