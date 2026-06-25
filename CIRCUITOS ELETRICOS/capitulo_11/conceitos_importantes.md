# Capítulo 11: Potência em Corrente Alternada
*(Focado em Cargas Industriais em Paralelo e Correção do Fator de Potência)*

O Capítulo 11 abandona a preocupação de "onde a corrente está passando" e foca apenas na **energia** (Potência) consumida. Na indústria, você raramente liga cargas em série. Quase todas as máquinas (Cargas) são ligadas em **Paralelo** à mesma tomada.

---

## 1. As Três Potências (O Triângulo)
Quando um equipamento elétrico funciona em Corrente Alternada, ele exige energia da rede em dois formatos:

1. **Potência Ativa (P):** É a energia que realmente "trabalha". Gira motor, acende luz, esquenta o forno. Medida em **Watts (W)**. Fica no eixo "X" (real) do triângulo.
2. **Potência Reativa (Q):** É a energia "fantasma" que não faz trabalho útil, mas é exigida pelos motores e capacitores para criar seus campos magnéticos/elétricos. Ela fica "indo e voltando" da tomada. Medida em **VAr (Volt-Ampère Reativo)**. Fica no eixo "Y" (imaginário) do triângulo.
   - ⚠️ **MUITO IMPORTANTE (Regra de Sinal):**
   - Carga Indutiva (Motor) puxa Q **Positivo** ($+Q$). A corrente atrasa.
   - Carga Capacitiva joga Q **Negativo** ($-Q$). A corrente adianta.
3. **Potência Aparente (S):** É a energia **Total** que a usina hidrelétrica tem que entregar na sua porta para suprir a Ativa (P) e a Reativa (Q) ao mesmo tempo. É o tamanho da hipotenusa do triângulo. Medida em **VA (Volt-Ampère)**.

A relação matemática é a velha Pitágoras (Potência Complexa):
$$ \mathbf{S} = P + jQ \quad \text{ (Retangular)} $$
$$ |\mathbf{S}| = \sqrt{P^2 + Q^2} \quad \text{ (Módulo / Aparente)} $$

---

## 2. O Fator de Potência (FP)
O Fator de Potência (FP) é a "nota de eficiência" da máquina. Ele diz o quanto da energia total (S) virou energia útil (P).

$$ FP = \frac{P}{S} = \cos(\theta) $$
- O FP sempre é um número entre $0$ e $1$. (Ex: FP = 0,92 significa que 92% da energia é útil).
- Se a prova te der o FP, você pode descobrir o ângulo do triângulo com a função arco-cosseno ($\arccos$): $\theta = \arccos(FP)$.
- **Atenção ao sobrenome do FP:** 
  - Fator de Potência **Indutivo**: O triângulo sobe (Q positivo).
  - Fator de Potência **Capacitivo**: O triângulo desce (Q negativo).

---

## 3. Cargas em Paralelo (O que cai na Prova!)
Na sua Prova 2 (Questão 4), o professor liga duas máquinas gigantes na mesma rede e pede o total. A regra de ouro é: **As potências Ativas (P) se somam entre si. As Reativas (Q) se somam entre si. Você NÃO PODE somar a Potência Aparente (S) e nem o FP direto!**

**A "Receita de Bolo" para Cargas em Paralelo:**
1. Monte uma tabela com 3 colunas: $P$ (Watts), $Q$ (VAr) e $S$ (VA).
2. Para cada máquina, descubra o seu $P$ e o seu $Q$.
   - *Exemplo:* Se ele te der o P e o FP, calcule $S = P / FP$. Depois descubra $\theta = \arccos(FP)$. Depois calcule $Q = S \cdot \sin(\theta)$.
   - *Se atente aos sinais!* Coloque o sinal $+$ se ele disser "Indutivo", e o sinal $-$ se ele disser "Capacitivo".
3. **Soma Final:** 
   - $P_{total} = P_1 + P_2 + \dots$
   - $Q_{total} = Q_1 + Q_2 + \dots$
4. Agora que tem o $P_{total}$ e o $Q_{total}$, use a Pitágoras ($S = \sqrt{P^2 + Q^2}$) para achar o $S_{total}$. E divida $P/S$ para achar o $FP_{total}$.

> [!TIP]
> **Na Casio fx-991LA CW:** 
> Você não precisa fazer Pitágoras! No aplicativo `Complexo`, apenas digite: $P_{total} + Q_{total}i$ e mande converter para Polar (`FORMAT` $\to$ Polar Coord).
> A Casio vai te dar $S \angle \theta$. O $S$ (primeiro número) já é a sua Potência Aparente. E o $\theta$ é o seu ângulo total. Para achar o FP, é só tirar o cosseno desse ângulo!
