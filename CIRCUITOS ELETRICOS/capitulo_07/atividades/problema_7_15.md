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
1. Logo de cara, a corrente pode escolher ir pelo resistor de $10\Omega$ lá no topo, ou pelo resistor de $40\Omega$ no meio. Isso forma um **paralelo**:
$$10 || 40 = \frac{10 \times 40}{10 + 40} = \frac{400}{50} = 8\Omega$$
2. Depois que esses dois caminhos se juntam novamente do lado esquerdo, a corrente inteira é obrigada a descer pelo resistor de $2\Omega$ para finalmente conseguir chegar no Terminal B. Ou seja, esse $2\Omega$ está em **série** com o blocão anterior:
$$R_{eq} = 8 + 2 = \mathbf{10\Omega}$$

**Cálculo do $\tau$:**
Com o indutor de $5\text{H}$:
$$\tau = \frac{L}{R_{eq}} = \frac{5}{10} = \mathbf{0,5\text{s}}$$

Como $0,5\text{s}$ é a mesma coisa que multiplicar por $1000$ para converter para mili:
**Resposta Final:** $\tau = \mathbf{500\text{ms}}$
