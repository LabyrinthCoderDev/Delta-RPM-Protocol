# TERMINOLOGY
## The Poole Manifold — Canonical Definitions

**Author:** Rooke Alan Poole | @rookepoole
**Purpose:** Prevent semantic drift as the project grows and new contributors engage.
Every significant term used across the repo is defined here.

---

## Core Substrate Terms

### Poole Manifold
**Category:** Substrate | **Status:** VALIDATED
The three-dimensional totalistic cellular automaton governed by the B5-7/S5-9 rule
with prime-resonance sharpening. The fundamental computational substrate from which
all other behaviours emerge. Not a mathematical manifold in the differential geometry
sense — a computational substrate named by the author.

### B5-7/S5-9 Rule
**Category:** Substrate | **Status:** VALIDATED
The birth/survival rule governing the substrate:
- **Birth:** A dead cell with 5, 6, or 7 live neighbours becomes alive
- **Survival:** A live cell with 5, 6, 7, 8, or 9 live neighbours stays alive
All other cells die or remain dead. This rule is the only governing law.
All complex behaviour emerges from it.

### Prime-Resonance Sharpening
**Category:** Substrate | **Status:** VALIDATED
An additive potential applied based on proximity to prime numbers.
Formula: α × exp(−(potential − p)² / σ²) for each prime p in {2,3,5,7,11,13,17,19,23}.
Parameters: α = 0.35 (amplitude), σ² = 0.01 (sharpness).
Effect: Amplifies phase transitions at prime-number density thresholds.
This is the key novelty beyond standard cellular automata.

### Succession Flux (Φ)
**Category:** Substrate | **Status:** VERIFIED
The macroscopic fraction of cells that change state per timestep at equilibrium.
Stable value: Φ ≈ 0.4002. Observed across varied initial conditions.
Cosmological interpretation: claimed to correspond to what ΛCDM calls Dark Energy.
*The cosmological interpretation is benchmarked, not independently validated.*

### Delta RPM Protocol
**Category:** Infrastructure | **Status:** VERIFIED
The canonical engine implementation and test harness.
Contains: PooleEngine class, WORM audit infrastructure, step() function, test suite.
File: `DELTA RPM PROTOCOL | MASTER INTEGRATION TEST SUITE`
Read this before running any experiment.

---

## Computational Terms

### Orthogonal Blowout
**Category:** Logic | **Status:** VALIDATED
The mechanism by which AND and XOR gates emerge from substrate pressure dynamics.
Orthogonal pressure venting at gate boundaries creates functionally correct logic.
First demonstrated in Trial 317. Cryptographically proven.

### Immortal Latch
**Category:** Memory | **Status:** VALIDATED
A cross-coupled memory structure that survives repeated high-amplitude noise bursts.
Topologically protected — the structure's geometry prevents noise from flipping state.
Demonstrated in V207. The substrate's equivalent of radiation-hardened SRAM.

### Fluidic Logic / Fluid Tensor Architecture
**Category:** Logic | **Status:** VERIFIED
The framework in which logic gates, memory, and computation emerge from pressure
dynamics rather than electronic switching. Density fields behave like a compressible
fluid, and information propagates as density waves.

### Glider
**Category:** Particle analogs | **Status:** VERIFIED
A self-propagating localised excitation that moves coherently through the lattice.
Analogous to a particle with defined velocity and lifetime.
Used as information carriers in computation experiments.

### Swarm Arithmetic
**Category:** Computation | **Status:** EXPERIMENTAL
Arithmetic operations implemented using coordinated glider swarms rather than
fixed gate structures. Swarms route information dynamically.
Demonstrated in Trials 407-411.

### Von Neumann Cascade
**Category:** Computation | **Status:** VERIFIED
A synchronised sequence modelled on Von Neumann architecture (fetch, decode,
execute, write-back). Implemented in the 3D fluid full-adder series (Trials 374-382).

---

## Cosmological Terms

### OTG (Observative Tetrahedral Gravity)
**Category:** Cosmological model | **Status:** BENCHMARKED
The author's cosmological framework derived from the substrate.
Key result: BAO fit Δχ² ≈ 243.6 better than ΛCDM on DESI DR2 data.
*Computational result. Independent external verification pending.*

### BAO (Baryon Acoustic Oscillations)
**Category:** Cosmological observable | **Status:** External reference
Periodic density fluctuations observable as a peak in the matter power spectrum
at ~150 Mpc comoving scale. The Poole Manifold claims to reproduce this peak
naturally. Reference dataset: DESI DR2.

### Prime-Stepping (Δk ≈ 0.0124 h/Mpc)
**Category:** Cosmological prediction | **Status:** BENCHMARKED
The claim that BAO peak positions are quantised in prime-resonance steps.
Computational result — awaiting independent verification.

### FLRW Embedding
**Category:** Cosmological model | **Status:** BENCHMARKED
Friedmann–Lemaître–Robertson–Walker metric embedded into the substrate.
Primary result: FLRW-EMBEDDED POOLE MANIFOLD V7 (640³ lattice).

---

## Substrate Control Terms

### Inhibitor Mask
**Category:** Control | **Status:** VERIFIED
Boolean mask reducing local potential by 15.0. Suppresses birth in marked regions.
Used to create logic gate boundaries, memory isolation, routing channels.

### Amplifier Mask
**Category:** Control | **Status:** VERIFIED
Boolean mask increasing local potential by 1.0. Encourages birth.
Used for signal injection and strengthening computation pathways.

### Threshold Mask
**Category:** Control | **Status:** VERIFIED
Boolean mask reducing potential by 2.0. Moderates growth.
Used to create controlled density gradients.

---

## Named Structures

### Resonance Ringing
**Category:** Dynamics | **Status:** EXPERIMENTAL
Oscillatory behaviour observed when BAO-bias structures are driven with decaying
sine wave inputs. The substrate rings at frequencies related to prime-resonance peaks.
Subject of Trials 450-457.

### Mechanimal / MechanimalChief
**Category:** Structural | **Status:** EXPERIMENTAL
Author's term for a self-stabilising knot structure in the substrate.
Etymology: mechanical + animal — a structure that behaves autonomously.
The "Chief" variant appears in BAO experiments as a persistent anchor.

### Orthogon
**Category:** Structural | **Status:** EXPERIMENTAL
A geometric configuration forming orthogonal routing channels.
Used in FPGA-inspired logic routing experiments.

---

## Infrastructure Terms

### WORM Ledger
**Category:** Infrastructure | **Status:** VERIFIED
Write Once Read Many — a hash-chained audit log. Each entry contains the SHA-256
of the previous entry. Makes the record tamper-evident and cryptographically auditable.
Location: `Cryptographic Proof WORM/run_ledger.jsonl`

### Labyrinth OS Gate (Extended)
**Category:** External integration | **Status:** VERIFIED
The constitutional AI enforcement gate from the Labyrinth OS project.
In this repo: `LABYRINTH-OS EXTENDED` maps Poole Manifold prime-resonance
to Labyrinth OS sigma anchor channels. Independent convergence finding —
two systems built in different domains reached the same architectural conclusion.

---

## Reproducibility Levels

| Level | Label | Meaning |
|-------|-------|---------|
| A | Fully reproducible | Exact result, cryptographically sealed |
| B | Reproducible with variance | Consistent but GPU/seed-dependent variance |
| C | Requires tuning | Manual parameter adjustment needed |
| D | Partial reconstruction | Key result reproducible, environment not fully documented |
| E | Historical artifact | Observed but full reproduction not currently possible |

Known levels:
- Trial 317 AND/XOR gates: **A** — cryptographically proven
- V207 Immortal Latch: **A** — deterministic
- FLRW V7 BAO fit: **B** — GPU-dependent variance
- Material physics tests: **C** — parameter-sensitive
- Speculative simulations: **D/E** — exploratory

---

## Terms To Use With Care

| Avoid | Prefer | Reason |
|-------|--------|--------|
| "proves" (physics) | "demonstrates" or "is consistent with" | Computational ≠ physical proof |
| "AGI" | Not applicable | Cellular automaton, not general intelligence |
| "solves Dark Energy" | "proposes an alternative model for" | Benchmarked, not validated |
| "first of its kind" | Omit unless cited | Requires literature review |
| "immortal" (literally) | "topologically protected" | Survives noise in simulation |

---

*Rooke Alan Poole — @rookepoole — May 2026*
*Add terms here as the project grows — prevents semantic drift across contributors*

### WORM Ledger
**Category:** Infrastructure | **Status:** VALIDATED
Write-Once Read-Many ledger. A hash-chained JSONL file where each entry contains
a SHA-256 hash of the previous entry. Provides cryptographic proof that results
have not been altered after the fact. Used to seal the 100,000-trial variance audit.

### Cryptographic Audit Receipt
**Category:** Infrastructure | **Status:** VALIDATED
A JSON file containing: timestamp, system telemetry (GPU, PyTorch version),
result summary, and SHA-256 hash. Provides tamper-evident proof of a specific
experimental result at a specific point in time.

---

## Terms Requiring Author Clarification

The following terms appear in the repo but have no formal definition.
Rooke Alan Poole should clarify these before the project is widely shared:

| Term | Appears in | Clarification needed |
|------|-----------|---------------------|
| Mechanimal Chief Knot | BAO trials 430-457 | Formal definition of "knot" topology in substrate |
| Orthogon | FPGA experiments | Distinction from standard cellular automaton routing |
| Hudson | 3D Fluid Half-Adder | Who or what "Hudson" refers to |
| Incabloc | V140 CPU test | Reference to watch shock absorber — confirm this analogy |
| DTN Merge | Phase 2 simulator | Define Delay-Tolerant Network in this context |
| Fertility Filter | V207 deep scan | Define filter criteria |

---

## What This Terminology List Is Not

- Not a claim that all terms correspond to real physical phenomena
- Not a peer-reviewed glossary
- Not exhaustive — experiments may introduce new terms not yet listed here

When a new term is introduced in an experiment, it should be added here.
Terms should include: category, implementation status, and whether the
physical interpretation is validated, benchmarked, or speculative.

---

*Rooke Alan Poole — @rookepoole — May 2026*
*Maintained alongside the repo — update when new terms are introduced*
