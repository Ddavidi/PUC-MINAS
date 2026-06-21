### Problema Prático 9.11 — Divisão de Tensão *(pág. 372)*

**Enunciado:** Calcule vo no circuito da Figura 9.27: fonte `50 cos(10t + 30°)`, em série com indutor de 0,5 H e resistor de 10 Ω, com capacitor de 1/20 F em paralelo com R. A saída vo é no capacitor.

**Resolução:**

**Passo 1** — Dados (ω = 10):
```
Vs = 50∠30° V
Z_L = jωL = j(10)(0,5) = j5 Ω
Z_R = 10 Ω
Z_C = 1/(jωC) = 1/(j × 10 × 1/20) = 1/(j0,5) = −j2 Ω
```

**Passo 2** — R em paralelo com C:
```
Z_par = (Z_R × Z_C)/(Z_R + Z_C) = (10)(−j2)/(10 − j2)
      = −j20/(10 − j2)
```
Multiplicando pelo conjugado:
```
= −j20(10 + j2)/(100 + 4) = (−j200 − j²40)/104
= (40 − j200)/104 = 0,385 − j1,923 Ω
```

Hmm, vou usar outra abordagem. Olhando a Figura 9.27: L = 0,5 H em série com a fonte, R = 10 Ω em série, C = 1/20 F com vo medido no capacitor.

Na verdade, pela figura, parece ser L em série, depois R em série, depois C (tudo em série). Vo é a tensão no capacitor.

**Passo 2 (revisado)** — Tudo em série:
```
Z_eq = Z_L + Z_R + Z_C = j5 + 10 − j2 = 10 + j3 Ω
|Z_eq| = √(100 + 9) = √109 = 10,44 Ω
θ = arctan(3/10) = 16,7°
```

**Passo 3** — Corrente:
```
I = Vs/Z_eq = 50∠30° / 10,44∠16,7° = 4,79∠13,3° A
```

**Passo 4** — Tensão no capacitor (divisão de tensão):
```
Vo = (Z_C / Z_eq) × Vs = (−j2 / (10 + j3)) × 50∠30°
   = (2∠−90° / 10,44∠16,7°) × 50∠30°
   = 0,1916∠−106,7° × 50∠30°
   = 9,58∠−76,7° V
```

Hmm, a resposta do livro dá 35,36 cos(10t − 105°) V. Vou reverificar a figura.

Olhando a Figura 9.27 de novo: a fonte é `50 cos(10t + 30°)`, L = 0,5 H está no topo, R = 10 Ω está em um ramo, e C = 1/20 F está em outro ramo, com vo medido no capacitor. Parece que R e C estão em **paralelo** (não em série).

**Passo 2 (re-revisado)** — R ∥ C:
```
Z_par = (10 × (−j2))/(10 − j2) = −j20/(10 − j2)
      = −j20(10 + j2)/(104) = (40 − j200)/104
      = 0,3846 − j1,923 Ω
      = 1,961∠−78,69° Ω
```

**Passo 3** — Impedância total: Z_L + Z_par:
```
Z_eq = j5 + 0,3846 − j1,923 = 0,3846 + j3,077
     = 3,101∠82,87° Ω
```

**Passo 4** — Vo por divisão de tensão:
```
Vo = (Z_par/Z_eq) × Vs = (1,961∠−78,69° / 3,101∠82,87°) × 50∠30°
   = 0,6324∠−161,56° × 50∠30°
   = 31,62∠−131,56° V
```

Ainda não bate exatamente. A configuração exata na figura importa muito. A resposta do livro é:

> ✅ **Resposta (do livro): vo(t) = 35,36 cos(10t − 105°) V**

> [!IMPORTANT]
> **Lição importante:** A topologia do circuito (como os componentes estão conectados) é CRUCIAL. Sempre consulte a figura do circuito para identificar o que está em série e o que está em paralelo.

---

## 🟠 NÍVEL 3 — Circuitos com Análise Mais Elaborada