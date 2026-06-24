# Problema 7.6

> **Objetivo:** Resolver o problema passo a passo.
> **Instrução:** Leia o enunciado abaixo e tente resolver usando a metodologia.

**Enunciado:**
7.6 	 A chave na Figura 7.86 foi fechada há um bom tempo e é 
aberta em t = 0. Determine v(t) para t  0.
40 V
+

2 k:
A chave na figura abaixo foi fechada há um bom tempo e é aberta em $t = 0$. Determine $v(t)$ para $t \ge 0$.

![Circuito Problema 7.6](../../_base_dados_ia/imagens_geradas/problema_7_6.png)

---

> [!TIP]
> **Receita de Bolo: Análise de Circuitos de Primeira Ordem**
> 1. **Análise em t < 0:** Identifique o estado da chave. Calcule $v(0)$ para capacitores ou $i(0)$ para indutores (eles se comportam como circuito aberto e curto-circuito, respectivamente, em CC).
> 2. **Análise em t > 0:** Redesenhe o circuito com a chave na nova posição. Encontre a resistência equivalente $R_{eq}$ vista pelo capacitor/indutor.
> 3. **Constante de Tempo ($\tau$):** Calcule $\tau = R_{eq}C$ (para RC) ou $\tau = L/R_{eq}$ (para RL).
> 4. **Equação Final:** Use a fórmula da resposta $x(t) = x(\infty) + [x(0) - x(\infty)]e^{-t/\tau}$.

## ✍️ Sua Vez!

### Passo 1: O cálculo de $v(0)$ (Para $t < 0$)
Antes do tempo zero, a chave estava **fechada**, agindo como um fio liso. 
E o nosso capacitor, em regime de corrente contínua, age como um **circuito aberto** (uma parede que não deixa a corrente passar). 

Veja como a topologia fica:
![Circuito em t < 0](../../_base_dados_ia/imagens_geradas/problema_7_6_v0.png)

Como o ramo da direita (o capacitor) está rompido, a corrente da fonte só consegue girar na malha da esquerda, descendo pelo resistor de 2k.
Para descobrirmos a tensão no capacitor $v(0)$, notamos que ele está conectado diretamente em paralelo com o resistor de 2k (toca nos mesmos nós de cima e de baixo). 

Logo, basta usarmos o **Divisor de Tensão** para descobrir a queda de tensão no resistor de 2k:
$$v(0) = V_{2k} = 40 \cdot \left(\frac{2k}{10k + 2k}\right)$$
$$v(0) = 40 \cdot \left(\frac{2}{12}\right) = 40 \cdot \left(\frac{1}{6}\right) = \mathbf{\frac{20}{3} \, \text{V}}$$

---

### Passo 2: O Circuito em $t > 0$
Agora a nossa chave finalmente **abre**. O que vai acontecer com o circuito?
*(Tente deduzir o $R_{eq}$ e escreva no chat!)*
