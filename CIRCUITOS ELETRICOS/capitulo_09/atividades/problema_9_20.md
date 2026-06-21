### Problema 9.20 — Impedância a partir de V e I *(pág. 381)*

**Enunciado:** Um circuito linear tem corrente de entrada `i = 7,5 cos(10t + 30°) A` e tensão de saída `v = 120 cos(10t + 75°) V`. Determine a impedância associada.

**Conceito necessário:** Z = V/I (Lei de Ohm fasorial)

**Resolução:**

**Passo 1** — Converter para fasores (eliminar o termo temporal):
```
I = 7,5∠30° A
V = 120∠75° V
```

**Passo 2** — Aplicar Z = V/I:
```
Z = V/I = 120∠75° / 7,5∠30°
```

**Passo 3** — Dividir em forma polar (divide magnitudes, subtrai ângulos):
```
Z = (120/7,5) ∠(75° − 30°)
Z = 16∠45° Ω
```

**Passo 4** — Converter para forma retangular (opcional):
```
Z = 16 cos(45°) + j·16 sen(45°)
Z = 11,31 + j11,31 Ω
```

> ✅ **Resposta: Z = 16∠45° Ω = (11,31 + j11,31) Ω**

> [!NOTE]
> A parte real (11,31 Ω) é resistência. A parte imaginária positiva (+j11,31 Ω) indica reatância **indutiva**.