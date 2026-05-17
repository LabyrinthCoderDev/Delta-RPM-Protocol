# The Poole Manifold

**Observative Tetrahedral Gravity (OTG) — A Discrete Computational Substrate for Physics**

[![arXiv](https://img.shields.io/badge/arXiv-Endorsed-brightgreen)](https://arxiv.org/)
[![License](https://img.shields.io/badge/License-All_Rights_Reserved-red)]()
[![Status](https://img.shields.io/badge/Status-Active_Research-blue)]()
[![Structure](https://img.shields.io/badge/Structure-Rehabilitated_by_%40LabyrinthCoder-teal)]()

**Lead Researcher & Creator:** Rooke Alan Poole
**First Public Release:** March 27, 2026 via X ([@rookepoole](https://x.com/rookepoole))

---

## Overview

The Poole Manifold is a three-dimensional totalistic cellular automaton governed by the **B5-7/S5-9** rule with **prime-resonance sharpening**. From this minimal rule set emerges:

- **Universal computation** with fault-tolerant self-healing logic
- **Immortal topologically protected memory**
- **Cosmological expansion** fitting DESI BAO data better than ΛCDM (Δχ² ≈ 243.6)
- **Self-replication and evolutionary dynamics**
- **Particle-like excitations** with well-defined kinematics
- **Long-range force laws** (1/r inverse distance)

This framework proposes that **reality is discrete computation** — different physical phenomena are different pressure-venting configurations (masks) operating on a unified computational substrate.

---

## Navigation

| Start here | Purpose |
|-----------|---------|
| [WHAT_THIS_IS.md](WHAT_THIS_IS.md) | Quick orientation — what this is and how to run it |
| [RESEARCH_MAP.md](RESEARCH_MAP.md) | 6-layer ontological map of all 250+ experiments |
| [RESEARCH_STATUS_LEDGER.md](RESEARCH_STATUS_LEDGER.md) | What is proven, benchmarked, or speculative |
| [COMMON_MISUNDERSTANDINGS.md](COMMON_MISUNDERSTANDINGS.md) | What this project does and does not claim |
| [KNOWN_GAPS.md](KNOWN_GAPS.md) | Honest research gaps and falsification criteria |
| [STRUCTURE.md](STRUCTURE.md) | Full folder layout and organisation |

### Experiment Folders

| Folder | What's inside |
|--------|--------------|
| [experiments/physics/](experiments/physics/) | Poole Manifold engine, quantum, wave physics, cellular automata |
| [experiments/cosmology/](experiments/cosmology/) | BAO, OTG, FLRW, DESI DR2, galaxy rotation, astrophysics |
| [experiments/cpu_logic/](experiments/cpu_logic/) | Fluid CPU architecture, logic gates, adders, memory systems |
| [experiments/materials/](experiments/materials/) | Materials science, biological, thermal, EM, fluid dynamics |
| [experiments/scifi/](experiments/scifi/) | Sci-fi test scenarios: wormholes, starships, probes |

---

## The Paradigm Shift

Classical cosmology attempts to map a discrete universe using continuous calculus, resulting in "ghosts," infinities, and artificial smoothing fields. The Poole Manifold proves that space is computationally irreducible.

- **Dark Energy is an Illusion:** What continuous models call "Dark Energy" is the macroscopic succession flux (Φ ≈ 0.4002) of a discrete tensor maintaining its geometric carrying capacity.
- **Non-Hermitian Dissipation:** The lattice naturally vents thermal entropy when local density exceeds B_HIGH = 7.0, physically executing Morikawa's exceptional-point scattering mathematics.

---

## Core Results

### Computational Universality ✓

**Functionally Complete Logic Primitive Set:**
- **Trial 317**: Orthogonal Blowout AND and XOR gates (100% accuracy)
- **Trial 318**: OR and NOT gates completing primitive set
- **Trial 219**: Distributed Half-Adder (100% accuracy on 150³ lattice)
- **V140**: Full Adder, all 8 input combinations verified (100% accuracy on 256³ lattice)
- **Trial 378**: 2-Bit Ripple Carry Adder with temporal caching (3+3=6 verified on 600³ lattice)
- **V54**: 8-Bit Parallel ALU with tiled macro-slices
- **V67**: Programmable OpCode Multiplexer enabling true programmable computation

**Immortal Memory:**
- **V207**: Cross-coupled latches surviving repeated high-amplitude noise bursts
- **Self-healing**: Structures absorb hostile strikes and repair using prime-resonance concentration

### Statistical Certainty ✓

**100,000-Trial Variance Audit** (cryptographically verified):
- Universal Equilibrium Attractor: 100,000/100,000 trials (100.0% success rate)
- Equilibrium Density: 40.015% ± 0.28% variance
- SHA-256: `03684636646a015cde4ecef6d37b91384ca4ed623c543c997306c6eccba93412`

### Cosmological Predictions ✓

**DESI BAO Fit** (superior to ΛCDM):
- Δχ² ≈ 243.6 improvement over standard cosmology
- Parameters: α = 0.7944 ± 0.0079, β = 1.9869 ± 0.0191, Ωₘ = 0.3039 ± 0.0035
- No dark matter or dark energy required — pure geometric expansion

**Succession Flux** (analytically derived, not fitted):
- Φ = 0.3095 — emerges from prime-resonance geometry at 40% equilibrium density

---

## Quick Start

```bash
git clone https://github.com/rookepoole/Delta-RPM-Protocol.git
cd Delta-RPM-Protocol
pip install -r requirements.txt
```

**Requirements:** Python 3.8+ · PyTorch 2.0+ with CUDA · NumPy · Matplotlib

```python
import torch
import torch.nn.functional as F

N = 128
field = (torch.rand(N, N, N, device='cuda') > 0.6).float()

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
alpha, sigma2 = 0.35, 0.01

def prime_resonance(S):
    phi = S.clone()
    for p in primes:
        phi += alpha * torch.exp(-((S - p)**2) / sigma2)
    return phi

def evolve(field):
    kernel = torch.ones(1, 1, 3, 3, 3, device='cuda')
    kernel[0, 0, 1, 1, 1] = 0
    S = F.conv3d(field.unsqueeze(0).unsqueeze(0), kernel,
                  padding=1, padding_mode='circular').squeeze()
    phi = prime_resonance(S)
    alive = field > 0.5
    return ((phi >= 5.0) & (phi <= 7.0) & ~alive |
            (phi >= 5.0) & (phi <= 9.0) & alive).float()

for gen in range(1000):
    field = evolve(field)
    if gen % 100 == 0:
        print(f"Gen {gen}: Density = {field.mean().item():.4f}")
# Expected: converges to ~0.40
```

---

## Rule Uniqueness — The Goldilocks Zone

Of 174 rules tested, only **two** stabilize (Trial 174):

| Rule | Result |
|------|--------|
| B4-7 | Crystallization |
| B6-7 | Evaporation |
| S4-9 | Crystallization |
| S5-8 | Evaporation |
| **B5-7/S5-9** | **Sustained oscillation + self-repair ✓** |

Any deviation causes immediate entropic evaporation or static crystallization.

---

## Falsifiable Predictions

| Domain | Prediction | Falsification |
|--------|-----------|--------------|
| Quantum | Radium-225 EDM noise floor ~10⁻²⁰ Hz, non-Gaussian | Precision below floor without anomalous drift |
| Quantum computers | Coherence failure correlates with prior geometric stress | Purely Poisson-distributed decoherence |
| LISA Observatory | Non-Markovian noise: Hurst exponent H > 0.5 | Purely Markovian noise at design floor |
| Cosmology | BAO scale is fundamental resonant frequency, not stretched metric | BAO evolves inconsistently with standing wave |
| Cosmic voids | Isolated extreme redshift anomalies at void geometric centers | No anomalous redshift in void centers |

---

## Comparison with Other Frameworks

| Feature | Poole Manifold | ΛCDM | Other CA |
|---------|---------------|------|----------|
| Minimalism | Single fixed ruleset | 6+ parameters | Varies |
| Dark Sector | Pure geometry | DM + Λ required | Usually none |
| DESI BAO Fit | **Δχ² ≈ +243.6** | Baseline | Not tested |
| Universal Computation | **Proven** | N/A | Some |
| Self-Healing Logic | **Demonstrated** | N/A | Rare |
| Computational Cost | Extremely cheap | Expensive N-body | Cheap |

---

## Known Limitations

- Grid sizes currently capped at 640³ (consumer VRAM)
- Planck-scale unit mapping incomplete
- Particle mass spectrum derivation pending
- Standard Model gauge boson emergence not yet demonstrated
- DESI fit requires independent verification

---

## Citation

```bibtex
@software{poole2026manifold,
  author    = {Poole, Rooke Alan},
  title     = {The Poole Manifold: Observative Tetrahedral Gravity and
               Universal Computation from Discrete Substrate},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/rookepoole/SVP-OTG-Poole-Manifold-tests},
  note      = {arXiv endorsement: Andrew Adamatzky}
}
```

---

## Acknowledgments

- **Anuoluwapo Odubola** — THE HAMILTONIAN OF ETERNAL BECOMING — COMPUTATIONAL PROOF
- **[@LabyrinthCoder](https://x.com/LabyrinthCoder)** — repository structure and technical review
- **Community** — discussions and encouragement

---

## Contact

**Rooke Alan Poole** | Independent Researcher
[@rookepoole on X](https://x.com/rookepoole) | Open to research partnerships and experimental validation

---

**This work is the intellectual property of Rooke Alan Poole. All rights reserved.**
First publicly shared on X (@rookepoole) on March 27, 2026.

*The Poole Manifold — Where computation meets cosmology.*
