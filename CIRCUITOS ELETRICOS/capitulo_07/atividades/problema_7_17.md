# Problema 7.17

> **Objetivo:** Resolver o problema passo a passo.
> **Instrução:** Leia o enunciado abaixo e tente resolver usando a metodologia.

**Enunciado:**
Considere o circuito abaixo. Determine $v_o(t)$ se $i(0) = 6\text{A}$ e $v(t) = 0$.

![Circuito Problema 7.17](../../_base_dados_ia/imagens_geradas/problema_7_17.png)

---

## ✍️ Sua Vez!

Bem-vindo ao Lote 4! Aqui as coisas começam a misturar tudo que aprendemos. 

Neste circuito, o enunciado nos dá uma informação de ouro: **$v(t) = 0$**. 
Uma fonte de tensão que vale zero volts é nada mais, nada menos que um **curto-circuito** (um fio liso). Além disso, temos uma corrente inicial no indutor de $6\text{A}$. Isso significa que estamos lidando com uma **Resposta Natural** pura!

Para resolver, vamos usar a nossa velha tática de achar o $R_{eq}$ pela Visão de Thevenin. Eu troquei a fonte $v(t)$ por um fio liso (curto) e abri o buraco do indutor nos terminais A e B:

![Visão de Thevenin 7.17](../../_base_dados_ia/imagens_geradas/problema_7_17_thevenin.png)

Faça o "teste da formiguinha" saindo do Terminal A para tentar chegar no Terminal B:
1. Ela tem que passar pelo resistor de $3\Omega$.
2. Depois disso, ela chega no nó superior. O lado direito do circuito está totalmente aberto (não passa corrente). A única saída é ir para a esquerda!
3. Ela passa pelo resistor de $1\Omega$ e desce pelo fio liso para finalmente chegar no Terminal B (terra).

**Com base nessa viagem:**
1. Qual é o valor da Resistência Equivalente ($R_{eq}$)?
2. Qual é a constante de tempo $\tau = L / R_{eq}$? (Lembrando que o indutor vale $1/4\text{H}$)
3. Monte a equação da corrente $i(t) = i(0)e^{-t/\tau}$.

Calcule esses 3 passos iniciais e me diga qual foi a equação de $i(t)$ que você encontrou! (Deixe o cálculo do $v_o(t)$ para a parte 2).
