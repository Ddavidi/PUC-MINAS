# Questão de Revisão 7.5
*(Página 265 do PDF)*

> **Objetivo:** Encontrar a tensão inicial $v(0)$ no capacitor, que dita de onde a curva exponencial vai partir.
> **Instrução:** Analise o circuito DC em regime estacionário *antes* da chave abrir/fechar. Lembre-se: o que o capacitor vira em CC?

**Enunciado:**
No circuito da Figura 7.79 abaixo, a tensão no capacitor imediatamente antes de $t = 0$ é:
(a) $10 \, \text{V}$
(b) $7 \, \text{V}$
(c) $6 \, \text{V}$
(d) $4 \, \text{V}$
(e) $0 \, \text{V}$

![Circuito 7.79](../../_base_dados_ia/imagens_geradas/revisao_fig_7_79.png)

---

## ✅ Solução Correta: Letra (d)

A questão pede a tensão no capacitor "imediatamente antes de $t=0$", ou seja, $v(0^-)$. 

Nesse momento, a chave (switch) que diz "t=0 (abre)" ainda está **fechada**! Ela ficou fechada por muito tempo.
Como estamos em Corrente Contínua (fonte de 10V constante), após muito tempo, o capacitor se carrega completamente e passa a se comportar como um **Circuito Aberto** (fio cortado).

Portanto, a corrente sai da fonte de 10V, passa pelo resistor de $3 \, \Omega$ e não consegue descer pelo capacitor (pois ele é um buraco). A corrente é obrigada a virar à direita, passar pelo resistor de $2 \, \Omega$ e descer pelo interruptor (que está fechado).

Temos então um circuito série simples (apenas resistores $3 \, \Omega$ e $2 \, \Omega$).
A tensão $v(t)$ que o capacitor enxerga é exatamente a tensão que cai em cima do resistor de $2 \, \Omega$, pois eles estão em paralelo!

Usando a fórmula do **Divisor de Tensão**:
$$ v(0^-) = 10 \cdot \frac{2}{3 + 2} = 10 \cdot \frac{2}{5} = \mathbf{4 \, \text{V}} $$

A alternativa correta é a **(d)**!
