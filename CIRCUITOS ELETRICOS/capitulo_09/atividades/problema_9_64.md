### Problema 9.64 — Impedância Total e Corrente (Série-Paralelo) *(pág. 385)*

**Enunciado:** Determine Z_T e I no circuito da Figura 9.71.
Fonte: `30∠90° V`. Circuito: 4 Ω em série com 6 Ω, depois (−j10 Ω em paralelo com j8 Ω).

**Resolução:**

**Passo 1** — Da Figura 9.71:
- Ramo série: 4 Ω + (−j10 Ω) = 4 − j10 Ω
- Em paralelo com: 6 Ω + j8 Ω

Espera, olhando a figura mais cuidadosamente:
- Fonte 30∠90° V
- Em série: 4 Ω e 6 Ω no topo
- −j10 Ω e j8 Ω nas laterais

Pela Figura 9.71: parece que (4 Ω em série com −j10 Ω) está em paralelo com (6 Ω em série com j8 Ω).

**Passo 2** — Impedâncias dos ramos:
```
Z_a = 4 − j10 Ω → |Z_a| = √(16+100) = √116 = 10,77∠−68,2° Ω
Z_b = 6 + j8 Ω → |Z_b| = √(36+64) = √100 = 10∠53,13° Ω
```

**Passo 3** — Paralelo:
```
Z_T = (Z_a × Z_b)/(Z_a + Z_b)
    = ((4−j10)(6+j8))/(4−j10+6+j8)
    = ((4−j10)(6+j8))/(10−j2)
```

Numerador: (4)(6) + (4)(j8) + (−j10)(6) + (−j10)(j8)
= 24 + j32 − j60 + j²(−80) → CUIDADO: (−j10)(j8) = −j²80 = +80
= 24 + j32 − j60 + 80 = 104 − j28

```
Z_T = (104 − j28)/(10 − j2)
```

Multiplicando pelo conjugado:
```
= (104 − j28)(10 + j2)/(100 + 4)
= (1040 + j208 − j280 − j²56)/104
= (1040 + 56 + j(208−280))/104
= (1096 − j72)/104
= 10,54 − j0,692 Ω
≈ 10,56∠−3,76° Ω
```

**Passo 4** — Corrente:
```
I = V/Z_T = 30∠90° / 10,56∠−3,76° = 2,84∠93,76° A
```

> ✅ **Resposta: Z_T ≈ 10,54 − j0,69 Ω; I ≈ 2,84∠93,8° A**