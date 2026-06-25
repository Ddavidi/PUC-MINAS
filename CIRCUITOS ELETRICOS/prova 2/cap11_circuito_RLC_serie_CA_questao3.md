# Prova 2 — Questão 3
**Capítulo 11 | Tema: Circuito RLC Série em CA — Impedância, Corrente e Potências**

> **Enunciado (10 pontos):**
> Um circuito RLC série é alimentado por uma fonte alternada senoidal de $220\angle0°\text{ V}$ (rms) e frequência $f = 60\text{ Hz}$. O valor dos elementos são: $R = 80\,\Omega$, $L = 550\text{ mH}$ e $C = 5\text{ μF}$. Calcule:
> - a) A impedância total do circuito. O circuito é predominantemente indutivo ou capacitivo, justifique. (2 pontos)
> - b) A corrente elétrica (módulo e ângulo). (2 pontos)
> - c) As potências ativa, reativa e aparente. Desenhe o triângulo de potências. (6 pontos)

---

## 🔑 Passo 0: Circuito e dados

![Circuito RLC Série](../../_base_dados_ia/imagens_geradas/prova2_q3_circuito_rlc.png)

| Dado | Valor |
|------|-------|
| $V_s$ | $220\angle0°\text{ V rms}$ |
| $f$ | $60\text{ Hz}$ → $\omega = 2\pi \times 60 = 376,99\text{ rad/s}$ |
| $R$ | $80\,\Omega$ |
| $L$ | $550\text{ mH}$ |
| $C$ | $5\text{ μF}$ |

---

## ✅ Parte (a): Impedância total

**Reatâncias individuais:**

$$X_L = \omega L = 376,99 \times 0,550 = 207,3\,\Omega$$

$$X_C = \frac{1}{\omega C} = \frac{1}{376,99 \times 5 \times 10^{-6}} = \frac{1}{1,885 \times 10^{-3}} = 530,5\,\Omega$$

**Impedância total:**

$$Z = R + j(X_L - X_C) = 80 + j(207,3 - 530,5)$$

$$Z = 80 - j323,2\,\Omega$$

$$|Z| = \sqrt{80^2 + 323,2^2} = \sqrt{6400 + 104\,458} = \sqrt{110\,858} \approx 333,0\,\Omega$$

$$\angle Z = \arctan\!\left(\frac{-323,2}{80}\right) = \arctan(-4,04) \approx -76,1°$$

$$\boxed{Z = 333,0\angle{-76,1°}\,\Omega}$$

**O circuito é predominantemente CAPACITIVO**, pois $X_C > X_L$ ($530,5 > 207,3$), fazendo a parte imaginária da impedância ser **negativa** e o ângulo da corrente ficar **positivo** (corrente adianta a tensão).

---

## ✅ Parte (b): Corrente elétrica

$$I = \frac{V_s}{Z} = \frac{220\angle 0°}{333,0\angle{-76,1°}}$$

$$\boxed{I = 0,661\angle{76,1°}\text{ A}}$$

---

## ✅ Parte (c): Potências

**Potência Ativa (consumida no resistor):**
$$P = |I|^2 \cdot R = (0,661)^2 \times 80 = 0,437 \times 80 \approx \mathbf{34,9\text{ W}}$$

**Potência Reativa (diferença de reatâncias):**
$$Q = |I|^2 \cdot (X_L - X_C) = 0,437 \times (207,3 - 530,5) = 0,437 \times (-323,2)$$

$$\mathbf{Q \approx -141,2\text{ VAr}} \quad \text{(negativo = capacitivo)}$$

**Potência Aparente:**
$$S = |V_s| \times |I| = 220 \times 0,661 = \mathbf{145,4\text{ VA}}$$

**Verificação:** $S = \sqrt{P^2 + Q^2} = \sqrt{34,9^2 + 141,2^2} = \sqrt{1218 + 19937} = \sqrt{21155} \approx 145,4\text{ VA}$ ✅

**Fator de Potência:**
$$FP = \frac{P}{S} = \frac{34,9}{145,4} = 0,240 \text{ (capacitivo, corrente adianta)}$$

**Triângulo de Potências:**

> Como Q é negativo (capacitivo), o triângulo aponta para baixo do eixo real.

```
         P = 34,9 W
    ←─────────────────────┐
    │                     │ Q = 141,2 VAr (↓ capacitivo)
    │       S = 145,4 VA  │
    └─────────────────────┘
    θ = -76,1° (ângulo de desfasagem)
```

| Grandeza | Valor |
|----------|-------|
| **P** (ativa) | **34,9 W** |
| **Q** (reativa) | **−141,2 VAr** (capacitivo) |
| **S** (aparente) | **145,4 VA** |
| **FP** | **0,240 capacitivo** |
