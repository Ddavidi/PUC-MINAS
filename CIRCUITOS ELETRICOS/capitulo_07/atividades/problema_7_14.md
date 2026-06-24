# Problema 7.14

> **Objetivo:** Resolver o problema passo a passo.
> **Instrução:** Leia o enunciado abaixo e tente resolver usando a metodologia.

**Enunciado:**
Calcule a constante de tempo do circuito na figura abaixo.

![Circuito Problema 7.14](../../_base_dados_ia/imagens_geradas/problema_7_14.png)

---

## ✍️ Sua Vez!

Este problema é rápido e rasteiro! Ele não quer saber corrente, não quer saber tensão... Ele quer **apenas** a Constante de Tempo ($\tau$).

Você já está careca de saber a fórmula:
$$\tau = \frac{L}{R_{eq}}$$

Para achar o $R_{eq}$, nós aplicamos o nosso querido Teorema de Thevenin: arrancamos o Indutor de $5\text{mH}$ e deixamos os terminais A e B escancarados para analisarmos a topologia.

![Visão de Thevenin](../../_base_dados_ia/imagens_geradas/problema_7_14_thevenin.png)

Olhe bem para esse desenho! A partir do terminal A (verde lá no topo), a corrente que tenta ir pro terminal B pode escolher dois caminhos:
1. Ir para a esquerda (passando pelo 20k e depois pelo 40k).
2. Ir para a direita (passando pelo 10k e depois pelo 30k).

Neste caso, queime um pouquinho de neurônio:
- No ramo esquerdo, os resistores de 20 e 40 estão em série ou em paralelo?
- No ramo direito, os resistores de 10 e 30 estão em série ou paralelo?
- E no final das contas, o "blocão" da esquerda fica em quê com o "blocão" da direita?

Resolva essa resistência equivalente e calcule o nosso $\tau$ (dica: ele vai dar um número bem pequeno, na casa dos microsegundos, já que temos um mili-henry dividido por kilo-ohms!).
