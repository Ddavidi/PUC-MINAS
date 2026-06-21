### Problema Prático 9.9 — Circuito RL Série *(pág. 367)*

**Enunciado:** Consulte a Figura 9.17. `vs = 20 sen(10t + 30°) V`, R = 4 Ω, L = 0,2 H. Determine v(t) e i(t).

**Resolução:**

**Passo 1** — Converter seno → cosseno:
```
vs = 20 sen(10t + 30°) = 20 cos(10t + 30° − 90°) = 20 cos(10t − 60°)
Vs = 20∠−60° V,  ω = 10 rad/s
```

**Passo 2** — Impedâncias:
```
Z_R = 4 Ω
Z_L = jωL = j(10)(0,2) = j2 Ω
Z_eq = 4 + j2 Ω = √(16+4)∠arctan(2/4) = √20∠26,57° = 4,472∠26,57° Ω
```

**Passo 3** — Corrente:
```
I = Vs/Z_eq = 20∠−60° / 4,472∠26,57° = 4,472∠−86,57° A
```

**Passo 4** — Tensão no indutor (V = Z_L × I):
```
V = j2 × 4,472∠−86,57° = 2∠90° × 4,472∠−86,57°
  = 8,944∠3,43° V
```

**Passo 5** — Domínio do tempo (lembrando que a entrada era seno, convertemos para seno na saída):
```
i(t) = 4,472 sen(10t − 86,57° + 90°) = 4,472 sen(10t + 3,43°) A
v(t) = 8,944 sen(10t + 3,43° + 90°) = 8,944 sen(10t + 93,43°) V
```

> ✅ **Resposta: v(t) = 8,944 sen(10t + 93,43°) V; i(t) = 4,472 sen(10t + 3,43°) A**