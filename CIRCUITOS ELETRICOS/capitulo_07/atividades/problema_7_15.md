# Problema 7.15 (Letra a)

> **Objetivo:** Resolver o problema passo a passo.
> **Instrução:** Leia o enunciado abaixo e tente resolver usando a metodologia.

**Enunciado:**
Determine a constante de tempo para o circuito da figura abaixo.

![Circuito Problema 7.15a](../../_base_dados_ia/imagens_geradas/problema_7_15_a.png)

---

## ✍️ Sua Vez!

Assim como no problema anterior, queremos apenas a constante de tempo ($\tau$). 
Para isso, arrancamos o indutor de $5\text{H}$ e usamos a nossa famosa **Visão de Thevenin** nos terminais dele:

![Visão de Thevenin 7.15a](../../_base_dados_ia/imagens_geradas/problema_7_15_a_thevenin.png)

Faça o "teste da formiguinha" saindo do Terminal A para tentar chegar no Terminal B:
1. Logo de cara, a corrente pode escolher ir pelo resistor de $10\Omega$ lá no topo, ou pelo resistor de $40\Omega$ no meio. O que isso significa que eles são entre si?
2. Depois que esses dois caminhos se juntam novamente do lado esquerdo, a corrente inteira é obrigada a descer pelo resistor de $2\Omega$ para finalmente conseguir chegar no Terminal B. O que esse $2\Omega$ é em relação ao "blocão" anterior?

Use essa lógica para calcular o seu $R_{eq}$.
Depois, jogue na fórmula $\tau = \frac{L}{R_{eq}}$.
(O indutor agora vale $5\text{H}$ inteiros, sem o "mili").

Faça as contas e me diga qual foi a resistência equivalente e o $\tau$ que você encontrou!
