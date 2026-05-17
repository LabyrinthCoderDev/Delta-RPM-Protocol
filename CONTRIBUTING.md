# Contributing to The Poole Manifold

**Lead Researcher:** Rooke Alan Poole (@rookepoole on X)
**Status:** Active research — collaboration welcome

---

## What Collaboration Looks Like

This is independent research in an unconventional framework.
Contributions that are welcome:

**Experimental validation**
- Independent verification of the DESI BAO fit (Δχ² ≈ 243.6 vs ΛCDM)
- Radium EDM noise analysis
- LISA gravitational wave data analysis for non-Markovian signatures
- Quantum computing coherence experiments

**Computational resources**
- Exascale compute time for cosmological horizon simulations
- Multi-GPU cluster access for 1024³+ lattice runs

**Theoretical work**
- Rigorous continuum limit derivation
- Standard Model fermion/boson mapping
- Planck-scale unit mapping

**Code contributions**
- GPU optimisation of the PooleEngine
- Distributed computing (MPI) port
- C++/CUDA reimplementation for production-scale simulations

---

## How to Engage

Contact via X: **@rookepoole**

For experimental collaboration partnerships, mention:
- Your institutional affiliation (if any)
- What specific prediction you want to test
- What resources you have available

---

## Attribution Requirements

Any use of this work in publications, derivative projects, or presentations
must properly credit Rooke Alan Poole as the original author.

See `CITATION.cff` for the correct citation format.

Unauthorised commercial use or patent filings based on this work
without attribution constitutes intellectual property violation.

---

## Code Style

Experiments are self-contained Python scripts.
The canonical engine is in `DELTA RPM PROTOCOL | MASTER INTEGRATION TEST SUITE`.

When adding experiments:
- Begin with `!pip install` block if Colab-targeted
- Include a docstring describing the test and what result is expected
- Print a clear summary at the end: PASS / FAIL / values
- If the experiment adds to cryptographic audit: use the WORM ledger pattern

---

*The Poole Manifold — Where computation meets cosmology.*
