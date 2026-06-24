# Questão de Revisão 7.9
*(Página 286 do PDF)*

> **Objetivo:** Expressar funções matemáticas usando a Função Degrau Unitário $u(t)$.
> **Instrução:** Essa questão não possui circuito! É puramente de interpretação matemática de fontes que mudam de valor no tempo $t=0$.

**Enunciado:**
Se a tensão de uma fonte $v_s$ mudar de $2 \, \text{V}$ para $4 \, \text{V}$ no exato momento $t = 0$, podemos expressar matematicamente a função de $v_s$ como:

(a) $\delta(t) \, \text{V}$
(b) $2u(t) \, \text{V}$
(c) $2u(-t) + 4u(t) \, \text{V}$
(d) $2 + 2u(t) \, \text{V}$
(e) $4u(t) - 2 \, \text{V}$

---

## ✅ Solução Correta: Letras (c) e (d)

> [!TIP]
> **Receita de Bolo: Modelando Fontes com a Função Degrau $u(t)$**
> 1. **Entenda o Degrau:** A função $u(t)$ é como um "interruptor matemático". Antes do tempo zero ($t<0$), ela vale **0**. A partir do tempo zero ($t \ge 0$), ela vale **1**.
> 2. **Monte o Cenário Antes de Zero:** Se a fonte tem um valor inicial antes da chave fechar, você precisa de uma constante somada ou de um $u(-t)$ (que é o inverso, liga no passado e desliga no futuro).
> 3. **Monte o Cenário Depois de Zero:** Calcule a diferença que a fonte sofre e multiplique essa diferença por $u(t)$.
> 4. **Teste a Fórmula:** Jogue $t=-1$ e $t=+1$ na sua equação e veja se os valores batem com o enunciado.

**Aplicando a Receita:**

O enunciado diz que a fonte $v_s$:
- Para $t < 0$, vale **$2\text{V}$**.
- Para $t > 0$, vale **$4\text{V}$**.

Vamos testar as duas alternativas que parecem promissoras:

**Testando a Letra (c): $v_s = 2u(-t) + 4u(t)$**
A função $u(-t)$ vale $1$ no passado e $0$ no futuro.
- No passado ($t < 0$): $v_s = 2(1) + 4(0) = \mathbf{2\text{V}}$. Bateu!
- No futuro ($t > 0$): $v_s = 2(0) + 4(1) = \mathbf{4\text{V}}$. Bateu!

**Testando a Letra (d): $v_s = 2 + 2u(t)$**
Aqui temos uma constante $2$ somada com um degrau $2u(t)$.
- No passado ($t < 0$): $u(t) = 0$, então $v_s = 2 + 2(0) = \mathbf{2\text{V}}$. Bateu!
- No futuro ($t > 0$): $u(t) = 1$, então $v_s = 2 + 2(1) = 2 + 2 = \mathbf{4\text{V}}$. Bateu também!

As alternativas (c) e (d) representam rigorosamente a mesma onda de tensão! É por isso que o gabarito do livro acusa ambas como certas. A forma (d) é a mais comum de se encontrar na engenharia.
