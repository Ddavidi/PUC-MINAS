### Problema 9.35 — Circuito com R, C e L em Série-Paralelo *(pág. 382)*

**Enunciado:** Determine a corrente `i` no circuito da Figura 9.42 quando `vs(t) = 50 cos(200t) V`.

O circuito (Figura 9.42): Fonte vs em série com R = 10 Ω. Depois, em paralelo: capacitor de 5 mF e indutor de 20 mH.

**Resolução:**

**Passo 1** — Dados:
- ω = 200 rad/s
- Vs = 50∠0° V

**Passo 2** — Impedâncias:
```
Z_R = 10 Ω
Z_C = 1/(jωC) = 1/(j × 200 × 5 × 10⁻³) = 1/j1 = −j1 Ω
Z_L = jωL = j × 200 × 20 × 10⁻³ = j4 Ω
```

**Passo 3** — Capacitor e indutor em paralelo:
```
Z_par = (Z_C × Z_L)/(Z_C + Z_L) = (−j1 × j4)/(−j1 + j4)
     = (−j² × 4)/(j3) = 4/(j3) = 4/(j3) × (−j/−j) = −j4/3
     = −j1,333 Ω
```

**Passo 4** — Impedância total (R em série com o paralelo):
```
Z_eq = Z_R + Z_par = 10 − j1,333 Ω
|Z_eq| = √(100 + 1,778) = √101,778 = 10,089 Ω
θ = arctan(−1,333/10) = −7,595°
Z_eq = 10,089∠−7,595° Ω
```

**Passo 5** — Corrente:
```
I = V/Z = 50∠0° / 10,089∠−7,595° = 4,956∠7,595° A
```

**Passo 6** — Domínio do tempo:
```
i(t) = 4,956 cos(200t + 7,595°) A
```

> ✅ **Resposta: i(t) ≈ 4,96 cos(200t + 7,6°) A**