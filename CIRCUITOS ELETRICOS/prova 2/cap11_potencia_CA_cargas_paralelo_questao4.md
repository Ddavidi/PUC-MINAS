# Prova 2 — Questão 4
**Capítulo 11 | Tema: Potência em CA — Cargas em Paralelo e Fator de Potência**

> **Enunciado (05 pontos):**
> Uma fonte de 240 V alimenta as seguintes cargas:
>
> | Carga 1 | Carga 2 |
> |---------|---------|
> | P = 5500 W | P = 1200 W |
> | Q = 850 VAr (capacitivo) | FP = 0,55 (indutivo) |
>
> Determine:
> - a) A potência aparente total.
> - b) O fator de potência da carga total.

---

## 🔑 Passo 0: Estratégia

Quando cargas estão em paralelo, basta **somar** as potências ativa e reativa de cada uma separadamente, e então calcular a potência aparente total com o triângulo de potências.

⚠️ **Cuidado com sinais:**
- Q **capacitivo** = **negativo** (corrente adianta a tensão)
- Q **indutivo** = **positivo** (corrente atrasa a tensão)

---

## ✅ Carga 1: Dados diretos

$$P_1 = 5500\text{ W}$$
$$Q_1 = -850\text{ VAr} \quad \text{(capacitivo → negativo)}$$

---

## ✅ Carga 2: Calculando Q₂ a partir do FP

$$FP_2 = \cos(\theta_2) = 0,55 \implies \theta_2 = \arccos(0,55) = 56,6°$$

A potência aparente da Carga 2:
$$S_2 = \frac{P_2}{FP_2} = \frac{1200}{0,55} = 2181,8\text{ VA}$$

A potência reativa da Carga 2:
$$Q_2 = S_2 \cdot \sin(\theta_2) = 2181,8 \times \sin(56,6°) = 2181,8 \times 0,8352$$

$$Q_2 = +1822,0\text{ VAr} \quad \text{(indutivo → positivo)}$$

---

## ✅ Parte (a): Potência Aparente Total

**Somando tudo:**

$$P_{total} = P_1 + P_2 = 5500 + 1200 = \mathbf{6700\text{ W}}$$

$$Q_{total} = Q_1 + Q_2 = -850 + 1822 = +972\text{ VAr} \quad \text{(resultante indutivo)}$$

$$S_{total} = \sqrt{P_{total}^2 + Q_{total}^2} = \sqrt{6700^2 + 972^2} = \sqrt{44\,890\,000 + 944\,784}$$

$$S_{total} = \sqrt{45\,834\,784}$$

$$\boxed{S_{total} \approx 6770\text{ VA} = 6,77\text{ kVA}}$$

---

## ✅ Parte (b): Fator de Potência Total

$$\theta_{total} = \arctan\!\left(\frac{Q_{total}}{P_{total}}\right) = \arctan\!\left(\frac{972}{6700}\right) = \arctan(0,1451) = 8,27°$$

$$\boxed{FP_{total} = \cos(8,27°) \approx \mathbf{0,990} \text{ (indutivo)}}$$

---

## 📐 Triângulo de Potências

![Triângulo de Potências Q4](../../_base_dados_ia/imagens_geradas/prova2_q4_triangulo.png)

| Grandeza | Valor |
|----------|-------|
| **P total** (ativa) | **6700 W** |
| **Q total** (reativa) | **+972 VAr** (indutivo) |
| **S total** (aparente) | **≈ 6770 VA** |
| **FP total** | **≈ 0,990 indutivo** |
| **θ** | **≈ 8,27°** |

> 💡 O fator de potência quase unitário (0,990) indica que as cargas se **compensam muito bem** entre si: a carga capacitiva 1 quase cancela a carga indutiva 2!
