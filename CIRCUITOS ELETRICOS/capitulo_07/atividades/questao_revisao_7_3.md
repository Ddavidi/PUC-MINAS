# Questão de Revisão 7.3
*(Página 265 do PDF)*

> **Objetivo:** Compreender o significado prático da constante de tempo ($\tau$) no carregamento de um capacitor.
> **Instrução:** Leia o enunciado, tente deduzir a resposta e escreva a sua lógica para eu corrigir!

**Enunciado:**
Um capacitor em um circuito RC com $R = 2 \, \Omega$ e $C = 4 \, \text{F}$ está sendo carregado. O tempo necessário para a tensão no capacitor atingir 63,2% de seu valor em regime estacionário é:
(a) $2 \, \text{s}$
(b) $4 \, \text{s}$
(c) $8 \, \text{s}$
(d) $16 \, \text{s}$
(e) nenhuma das anteriores

## ✅ Solução Correta: Letra (c)

Você caiu numa das maiores e mais clássicas "pegadinhas" dessa matéria!

Ao fazer $8 \times 0,632 = 5,056 \, \text{s}$, você calculou "63,2% do tempo total", mas não é assim que a curva funciona. O **63,2% refere-se ao Eixo Y (Tensão)** e não ao Eixo X (Tempo).

A grande "mágica" (e a definição matemática) da Constante de Tempo $\tau$ é exatamente essa:
**"Um $\tau$ é o tempo exato que demora para um circuito carregar (ou descarregar) 63,2% da sua capacidade."**

Portanto, a pergunta "Quanto tempo demora para atingir 63,2%?" é uma pergunta "pegadinha" que na verdade está perguntando apenas: **"Qual é o valor de UM $\tau$?"**

Como é um circuito RC:
$$ \tau = R \cdot C $$
$$ \tau = 2 \, \Omega \cdot 4 \, \text{F} = 8 \, \text{segundos} $$

Ou seja, em exatamente $8$ segundos, a tensão vai chegar aos famosos $63,2\%$. 
A alternativa correta é **(c)**.

*(A título de curiosidade: a carga total prática de um capacitor ocorre em $5\tau$, o que daria $40$ segundos para atingir $99,3\%$ de carga!)*
