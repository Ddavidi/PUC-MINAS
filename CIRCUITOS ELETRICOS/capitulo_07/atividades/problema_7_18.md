# Problema 7.18

> **Objetivo:** Resolver o problema passo a passo.
> **Instrução:** Leia o enunciado abaixo e tente resolver usando a metodologia.

**Enunciado:**
Para o circuito da Figura 7.98, determine $v_o(t)$ quando $i(0) = 5\text{A}$ e $v(t) = 0$.

![Circuito Problema 7.18](../../_base_dados_ia/imagens_geradas/problema_7_18.png)

---

## ✍️ Sua Vez!

Pela sua transcrição, eu deduzi que o circuito do 7.18 é um "irmão gêmeo" do 7.17, só que com valores diferentes! (Se a topologia for diferente e eu tiver desenhado os componentes nos lugares errados, me avise que eu corrijo na hora!).

Assumindo que o formato é esse mesmo, a lógica de resolução é idêntica à do problema anterior. A fonte $v(t) = 0$ volta a ser um **curto-circuito**.

Olhe para a Visão de Thevenin abaixo (com o fio de curto-circuito em azul na esquerda):

![Visão de Thevenin 7.18](../../_base_dados_ia/imagens_geradas/problema_7_18_thevenin.png)

Repita aquele combo poderoso de 3 passos para começarmos:
1. Qual é a nova Resistência Equivalente ($R_{eq}$)?
2. Qual é o novo $\tau$? (Lembrando que o indutor agora é $0,4\text{H}$)
3. Sabendo que $i(0) = 5\text{A}$, qual é a equação final de $i(t)$?

> [!TIP]
> **Receita de Bolo: Análise de Circuitos de Primeira Ordem**
> 1. **Análise em t < 0:** Identifique o estado da chave. Calcule $v(0)$ para capacitores ou $i(0)$ para indutores (eles se comportam como circuito aberto e curto-circuito, respectivamente, em CC).
> 2. **Análise em t > 0:** Redesenhe o circuito com a chave na nova posição. Encontre a resistência equivalente $R_{eq}$ vista pelo capacitor/indutor.
> 3. **Constante de Tempo ($\tau$):** Calcule $\tau = R_{eq}C$ (para RC) ou $\tau = L/R_{eq}$ (para RL).

## ✍️ Sua Vez!
*(Deixe sua resolução passo a passo aqui)*
