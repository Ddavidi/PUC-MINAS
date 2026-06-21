### Problema 9.39 — Impedância Equivalente com Múltiplos Elementos *(pág. 383)*

**Enunciado:** Para o circuito da Figura 9.46, determine Z_eq e use para determinar I. Considere ω = 10 rad/s. Fonte: `12∠0° V`.

Circuito (Figura 9.46): Fonte 12∠0° em série com [4Ω + j20Ω + (−j14Ω em paralelo com {16Ω em série com j25Ω})].

**Resolução:**

**Passo 1** — Da Figura 9.46, identificamos:
```
Z₁ = 4 Ω (resistor)
Z₂ = j20 Ω (indutor)  
Z₃ = −j14 Ω (capacitor)
Z₄ = 16 Ω (resistor)
Z₅ = j25 Ω (indutor)
```

**Passo 2** — Z₄ em série com Z₅:
```
Z_a = 16 + j25 Ω
```

**Passo 3** — Z_a em paralelo com Z₃:
```
Z_b = (Z₃ × Z_a)/(Z₃ + Z_a)
    = (−j14)(16 + j25)/(−j14 + 16 + j25)
    = (−j224 − j²350)/(16 + j11)
    = (350 − j224)/(16 + j11)
```

Convertendo:
```
Num = 350 − j224 → 415,5∠−32,6°
Den = 16 + j11 → 19,42∠34,5°
Z_b = 415,5∠−32,6° / 19,42∠34,5° = 21,4∠−67,1°
    = 8,33 − j19,7 Ω
```

**Passo 4** — Impedância total:
```
Z_eq = Z₁ + Z₂ + Z_b = 4 + j20 + 8,33 − j19,7
     = 12,33 + j0,3 Ω ≈ 12,33∠1,39° Ω
```

**Passo 5** — Corrente:
```
I = V/Z_eq = 12∠0° / 12,33∠1,39° = 0,973∠−1,39° A
```

> ✅ **Resposta: Z_eq ≈ 12,33 + j0,3 Ω; I ≈ 0,973∠−1,39° A**