### Problema 9.40 — Corrente em Função de ω *(pág. 383)*

**Enunciado:** No circuito da Figura 9.47, determine io quando: (a) ω = 1 rad/s; (b) ω = 5 rad/s; (c) ω = 10 rad/s.

Circuito: Fonte `4 cos(ωt) V` em série com R = 2 Ω. Em paralelo: C = 0,05 F e L = 1 H.

**Resolução para (a) ω = 1 rad/s:**

**Passo 1** — Impedâncias:
```
Z_R = 2 Ω
Z_C = 1/(jωC) = 1/(j × 1 × 0,05) = 1/(j0,05) = −j20 Ω
Z_L = jωL = j × 1 × 1 = j1 Ω
```

**Passo 2** — C ∥ L:
```
Z_par = (−j20 × j1)/(−j20 + j1) = (−j²20)/(−j19) = 20/(−j19)
      = 20/(19∠−90°) = 1,053∠90° = j1,053 Ω
```

**Passo 3** — Impedância total:
```
Z_eq = 2 + j1,053 = 2,26∠27,8° Ω
```

**Passo 4** — Corrente total:
```
I = 4∠0° / 2,26∠27,8° = 1,77∠−27,8° A
```

**Passo 5** — io é a corrente no indutor (divisão de corrente):
```
io = I × Z_C/(Z_C + Z_L) = 1,77∠−27,8° × (−j20)/(−j20 + j1)
   = 1,77∠−27,8° × (−j20)/(−j19)
   = 1,77∠−27,8° × 20/19
   = 1,863∠−27,8° A
```

```
io(t) = 1,863 cos(t − 27,8°) A
```

> O mesmo método se aplica para (b) ω = 5 e (c) ω = 10, apenas recalculando as impedâncias!

**Para (b) ω = 5:**
```
Z_C = 1/(j5 × 0,05) = −j4 Ω
Z_L = j5 Ω
Z_par = (−j4)(j5)/(−j4 + j5) = 20/j1 = −j20 Ω
Z_eq = 2 − j20 = 20,1∠−84,3° Ω
I = 4∠0° / 20,1∠−84,3° = 0,199∠84,3° A
io = I × Z_C/(Z_C + Z_L) = 0,199∠84,3° × (−j4)/j = 0,199∠84,3° × 4∠−180°
   = 0,796∠−95,7° A → io(t) = 0,796 cos(5t − 95,7°) A
```

**Para (c) ω = 10:**
```
Z_C = 1/(j10 × 0,05) = −j2 Ω
Z_L = j10 Ω
Z_par = (−j2)(j10)/(−j2 + j10) = 20/(j8) = −j2,5 Ω
Z_eq = 2 − j2,5 = 3,2∠−51,3° Ω
I = 4∠0° / 3,2∠−51,3° = 1,25∠51,3° A
io = I × Z_C/(Z_C + Z_L) = 1,25∠51,3° × (−j2)/(j8)
   = 1,25∠51,3° × 0,25∠−180° = 0,3125∠−128,7° A
→ io(t) = 0,3125 cos(10t − 128,7°) A
```

> ✅ **Respostas:**
> - **(a)** io ≈ 1,86 cos(t − 27,8°) A
> - **(b)** io ≈ 0,80 cos(5t − 95,7°) A
> - **(c)** io ≈ 0,31 cos(10t − 128,7°) A