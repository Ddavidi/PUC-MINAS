### Problema 9.65 — Circuito com Divisão de Tensão *(pág. 385)*

**Enunciado:** Determine Z_T e I no circuito da Figura 9.72.
Fonte: `120∠10° V`. Circuito: 2 Ω em série com [ramo 1: (3 Ω + j4 Ω) em paralelo com ramo 2: (4 Ω + (−j6 Ω))].

**Resolução:**

**Passo 1** — Da Figura 9.72:
```
Z₁ = 3 + j4 Ω (ramo superior)
Z₂ = 4 − j6 Ω (ramo inferior)
```

**Passo 2** — Paralelo de Z₁ e Z₂:
```
Z_par = (Z₁ × Z₂)/(Z₁ + Z₂)
      = ((3+j4)(4−j6))/(3+j4+4−j6)
      = ((3+j4)(4−j6))/(7−j2)
```

Numerador: (3)(4) + (3)(−j6) + (j4)(4) + (j4)(−j6)
= 12 − j18 + j16 − j²24 = 12 − j18 + j16 + 24 = 36 − j2

```
Z_par = (36 − j2)/(7 − j2)
```

Multiplicando pelo conjugado:
```
= (36−j2)(7+j2)/(49+4) = (252 + j72 − j14 − j²4)/53
= (252 + 4 + j(72−14))/53 = (256 + j58)/53
= 4,83 + j1,094 Ω
```

**Passo 3** — Impedância total:
```
Z_T = 2 + Z_par = 2 + 4,83 + j1,094 = 6,83 + j1,094 Ω
    = 6,917∠9,1° Ω
```

**Passo 4** — Corrente:
```
I = V/Z_T = 120∠10° / 6,917∠9,1° = 17,35∠0,9° A
```

> ✅ **Resposta: Z_T ≈ 6,83 + j1,09 Ω; I ≈ 17,35∠0,9° A**

---

## 📌 Resumo: "Receita" para Resolver Qualquer Problema

```
┌─────────────────────────────────────────────────────────┐
│  1. Leia ω da fonte (coeficiente do t)                  │
│  2. Converta a fonte para fasor                         │
│     - Se for seno: subtraia 90° → cos(x-90°)           │
│  3. Calcule impedâncias de cada componente:             │
│     R → R    L → jωL    C → 1/(jωC)                    │
│  4. Combine impedâncias:                                │
│     Série → soma    Paralelo → produto/soma             │
│  5. Use V = ZI (Lei de Ohm fasorial)                    │
│  6. Converta de volta: adicione cos(ωt + ...) ao fasor  │
└─────────────────────────────────────────────────────────┘
```

> [!TIP]
> **Dica de ouro para operações com complexos:**
> - **Soma/subtração** → use forma retangular (a + jb)
> - **Multiplicação/divisão** → use forma polar (r∠θ)
> - Multiplicar: multiplica magnitudes, soma ângulos
> - Dividir: divide magnitudes, subtrai ângulos