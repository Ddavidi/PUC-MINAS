### Problema 9.30 — Correntes em Paralelo (R ∥ C) *(pág. 382)*

**Enunciado:** Uma tensão `v(t) = 100 cos(60t + 20°) V` é aplicada a uma associação em paralelo entre um resistor de 40 kΩ e um capacitor de 50 μF. Encontre as correntes em regime estacionário no resistor e no capacitor.

**Conceito necessário:** Em paralelo, a tensão é a mesma em ambos. Calcular I = V/Z para cada elemento.

**Resolução:**

**Passo 1** — Dados:
- ω = 60 rad/s
- V = 100∠20° V
- R = 40 kΩ = 40.000 Ω
- C = 50 μF = 50 × 10⁻⁶ F

**Passo 2** — Corrente no resistor (I_R = V/R):
```
I_R = 100∠20° / 40.000 = 0,0025∠20° A = 2,5∠20° mA
```

**Passo 3** — Impedância do capacitor:
```
Z_C = 1/(jωC) = 1/(j × 60 × 50 × 10⁻⁶) = 1/(j0,003) = −j333,33 Ω
```
Em forma polar: Z_C = 333,33∠−90° Ω

**Passo 4** — Corrente no capacitor (I_C = V/Z_C):
```
I_C = 100∠20° / 333,33∠−90° = 0,3∠110° A = 300∠110° mA
```

**Passo 5** — Voltar ao domínio do tempo:
```
i_R(t) = 2,5 cos(60t + 20°) mA
i_C(t) = 300 cos(60t + 110°) mA
```

> ✅ **Resposta: i_R(t) = 2,5 cos(60t + 20°) mA; i_C(t) = 300 cos(60t + 110°) mA**

> [!TIP]
> Note que a corrente no capacitor está **adiantada 90°** em relação à tensão (20° + 90° = 110°). Isso sempre acontece no capacitor!

---

## 🟡 NÍVEL 2 — Circuitos Série com Impedância