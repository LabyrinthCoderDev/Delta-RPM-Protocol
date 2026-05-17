# ARCHITECTURE DIAGRAMS
## The Poole Manifold — Signal Flow and System Relationships

**Author:** Rooke Alan Poole | @rookepoole
**Format:** Mermaid diagrams — rendered automatically on GitHub

---

## 1. The Core Computation Loop

```mermaid
flowchart LR
    A[Input State\nf_tensor] --> B[Circular Padding]
    B --> C[3×3×3 Convolution\npotential field]
    C --> D{Masks Applied?}
    D -->|Inhibitor| E[potential − 15.0\nreduced pressure zone]
    D -->|Amplifier| F[potential + 1.0\nboost zone]
    D -->|Threshold| G[potential − 2.0\ngate zone]
    D -->|None| H[raw potential]
    E & F & G & H --> I[Prime Resonance\nalpha × exp−distance²/σ²\nfor each prime p]
    I --> J[total_phi =\npotential + resonance]
    J --> K{Birth/Survival\nB5-7 / S5-9}
    K -->|Birth: dead cell, total 5-7| L[Cell becomes alive]
    K -->|Survival: live cell, neighbors 5-9| M[Cell stays alive]
    K -->|Otherwise| N[Cell dies]
    L & M & N --> O[Next State\nf_tensor_t+1]
    O -->|Loop| A
```

---

## 2. The Gate Architecture — From Substrate to Logic

```mermaid
flowchart TD
    subgraph SUBSTRATE[Layer 1 — Substrate Physics]
        S1[B5-7/S5-9 Rule] --> S2[Prime Resonance\nSharpening]
        S2 --> S3[Pressure Field\nDynamics]
    end

    subgraph PRIMITIVES[Layer 2 — Primitives]
        P1[AND Gate\nTrial 317 ✓]
        P2[XOR Gate\nTrial 317 ✓]
        P3[OR Gate\nTrial 318 ✓]
        P4[NOT Gate\nTrial 318 ✓]
    end

    subgraph MEMORY[Layer 2 — Memory]
        M1[Immortal Latch\nV207 ✓]
        M2[Delay-Line\nTrial 265 ✓]
        M3[Shift Register]
    end

    subgraph CPU[Layer 3 — CPU Architecture]
        C1[Half-Adder\nTrial 219 ✓]
        C2[Full Adder\nV140 ✓]
        C3[2-Bit Adder\nTrial 378 ✓]
        C4[8-Bit ALU\nV54 ✓]
        C5[OpCode MUX\nV67 ✓]
    end

    S3 --> P1 & P2 & P3 & P4 & M1 & M2
    P1 & P2 --> C1
    C1 --> C2 --> C3 --> C4 --> C5
    M1 & M2 --> M3
    M3 --> C4
```

---

## 3. Cosmological Model Pipeline

```mermaid
flowchart LR
    A[Poole Manifold\nSubstrate] --> B[Succession Flux\nΦ ≈ 0.4002]
    B --> C[Density Dynamics]
    C --> D[BAO Peak\nExtraction FFT]
    D --> E{Comparison}
    E --> F[ΛCDM prediction]
    E --> G[OTG prediction\nΔk ≈ 0.0124 h/Mpc]
    F & G --> H[DESI DR2\nObservations]
    H --> I{Fit Quality}
    I -->|OTG| J[Δχ² ≈ 243.6\nbetter than ΛCDM ✓]
    I -->|ΛCDM| K[Standard fit]
    
    A --> L[H₀ Convergence]
    L --> M[72.88 km/s/Mpc ✓\nfrom substrate alone]
```

---

## 4. Validation Chain — How Results Are Proven

```mermaid
flowchart TD
    E[Experiment] --> R[Result]
    R --> V{Validation method?}
    
    V -->|Truth table| TT[Compare expected\nvs actual output]
    V -->|Statistical| ST[N=100,000 trials\nVariance Audit]
    V -->|Cryptographic| CR[SHA-256 hash\nWORM ledger\nimmutable proof]
    V -->|DESI comparison| DS[Bayesian fit\nto observed BAO data]
    
    TT --> L1[VALIDATED ✓\nif 100% accuracy]
    ST --> L2[VALIDATED ✓\nif cryptographic hash matches]
    CR --> L2
    DS --> L3[BENCHMARKED ~\npending independent verification]
    
    L1 & L2 & L3 --> PUB[Record in\nRESEARCH_STATUS_LEDGER.md]
```

---

## 5. Memory Architecture Hierarchy

```mermaid
flowchart TD
    A[Immortal Latch V207\nTopologically protected ✓] --> B[Cross-coupled\nstructure]
    
    C[Delay-Line Memory\nTrial 265 ✓] --> D[Circulating\npropagation]
    
    E[Reservoir\nTrial 379d] --> F[Fluidic RAM\nconcept]
    
    B & D & F --> G[4-Bit Register\nV26 ✓]
    G --> H[8-Bit Data Bus\nV27 ✓]
    H --> I[Accumulator\nTrial 380]
    I --> J[CPU + RAM\nIntegrated]
```

---

## 6. Epistemic Layer Map
*Where each experiment type sits in the knowledge hierarchy*

```mermaid
flowchart TD
    subgraph V[VALIDATED — Can be cited]
        V1[Logic gates AND/XOR/OR/NOT]
        V2[Full Adder 256³]
        V3[Immortal Latch V207]
        V4[100K variance audit]
    end
    
    subgraph B[BENCHMARKED — Needs external replication]
        B1[BAO fit Δχ²]
        B2[H₀ convergence]
        B3[DESI DR2 parameter fit]
    end
    
    subgraph EX[EXPERIMENTAL — Research direction]
        E1[Swarm arithmetic]
        E2[Complex manifold quantum effects]
        E3[Material physics analogs]
    end
    
    subgraph SP[SPECULATIVE — Frontier / stress tests]
        S1[Exotic spacetime]
        S2[Consciousness analogs]
        S3[Sci-fi scenarios]
    end
    
    V --> B --> EX --> SP
```

---

## 7. Labyrinth OS Integration Point

```mermaid
flowchart LR
    subgraph PM[Poole Manifold]
        PM1[Prime primes p₁...p₉]
        PM2[Resonance peaks\nalpha × exp−x²/σ²]
        PM3[B_LOW B_HIGH thresholds]
    end
    
    subgraph LOS[Labyrinth OS Gate]
        L1[Sigma Anchor channels\ntau chi drift betti kappa]
        L2[Z3-proven constants\nTAU_KILL_FLOOR CHI_KILL]
        L3[Epistemic labels\nVERIFIED HALLUCINATION etc]
    end
    
    subgraph HYBRID[HybridGate]
        H1[echo_gate_adapter.py\nρ/γ/Δ from sensors]
        H2[hybrid_gate.py\nstrictest wins]
        H3[PAUSE state\nnew decision tier]
    end
    
    PM2 -.->|"Independent convergence\nsame architecture\ndifferent domains"| L1
    PM3 -.-> L2
    
    PM --> HYBRID
    LOS --> HYBRID
    HYBRID --> H3
```

---

*Diagrams rendered by GitHub Mermaid — view on GitHub for visual output*
*Rooke Alan Poole — @rookepoole — May 2026*
*Collaboration: @LabyrinthCoder*
