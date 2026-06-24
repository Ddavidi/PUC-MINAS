# Problema 7.18

> **Objetivo:** Resolver o problema passo a passo.
> **Instrução:** Leia o enunciado abaixo e tente resolver usando a metodologia.

**Enunciado:**
Para o circuito da Figura 7.98, determine $v_o(t)$ quando $i(0) = 5\text{A}$ e $v(t) = 0$.

![Circuito Problema 7.18](../../_base_dados_ia/imagens_geradas/problema_7_18.png)

---

## ✍️ Sua Vez!

Opa, eu vi a imagem que você mandou e corrigi tudo na mesma hora! Não tem nada de "irmão gêmeo", a topologia aqui é bem diferente: o indutor de $0,4\text{H}$ está **em paralelo** com o resistor de $2\Omega$ no ramo superior.

Mas a lógica matadora da Resposta Natural é a mesma! A fonte $v(t) = 0$ atua como um **curto-circuito**.

Se você olhar a **Visão de Thevenin** abaixo (onde eu tirei o indutor e substituí a fonte por um fio azul), perceba a mágica:
O fio azul conecta o lado esquerdo de tudo diretamente com o "chão". Isso significa que o lado esquerdo do circuito (Terminal A) está eletricamente no MESMO PONTO que a parte de baixo (Terminal B).
Ou seja, ao olhar a partir dos terminais A e B, **todos os componentes acabam ficando em paralelo entre si**!

![Visão de Thevenin 7.18](../../_base_dados_ia/imagens_geradas/problema_7_18_thevenin.png)

Com essa dica de ouro, calcule nosso combo de 3 passos para o indutor:
**1. Resistência Equivalente:**
Como o fio de curto conecta tudo ao mesmo ponto, o resistor de $2\Omega$ está em paralelo com o de $3\Omega$.
$$R_{eq} = 2 || 3 = \frac{2 \times 3}{2 + 3} = \frac{6}{5} = \mathbf{1,2\Omega}$$

**2. Constante de Tempo:**
$$\tau = \frac{L}{R_{eq}} = \frac{0,4}{1,2} = \mathbf{\frac{1}{3}\text{s}}$$

**3. Equação da Corrente:**
Como $\tau = 1/3$, o inverso é $3$.
$$i(t) = i(0)e^{-t/\tau} = \mathbf{5e^{-3t}\text{ A}}$$

---

## Parte 2: O Xeque-Mate ($v_o(t)$)

Nós temos a corrente no indutor $i(t) = 5e^{-3t}$, e queremos a tensão $v_o(t)$, que é a tensão em cima do resistor de $3\Omega$.

Note que o resistor de $3\Omega$, o resistor de $2\Omega$ e o indutor estão TODOS em paralelo entre si! Isso significa que **a tensão é a mesma para todo mundo**.
A tensão $v_o(t)$ medida nos terminais é a mesma tensão em cima do nó superior (chamaremos de Nó A).

Você pode usar o caminho que preferir para matar o problema:

**Caminho 1 (Lei de Ohm / KCL):**
Pela Lei de Kirchhoff das Correntes (LKC) no Nó A, a corrente que entra pelo indutor ($i(t)$) tem que ser igual à soma das correntes que saem descendo pelos resistores de 2 e 3. 
Ou seja, $i(t) = \frac{v_o(t)}{2} + \frac{v_o(t)}{3}$.
Basta isolar o $v_o(t)$!

**Caminho 2 (Tensão do Indutor):**
Sabemos que a tensão no indutor é $v = L \cdot \frac{di}{dt}$.
Como a seta da corrente do indutor aponta para a direita (em direção ao Nó A), e o indutor está no chão (0V), a tensão "cai" do 0V para o $v_o(t)$. Ou seja, $0 - v_o(t) = L \cdot \frac{di}{dt}$.
Derivando a equação da corrente e multiplicando por $-L$, você acha o resultado!

Tente fazer por um dos caminhos (ou os dois para tirar a prova real) e me diga: **Qual é o valor final de $v_o(t)$?**

**Resolução Alternativa (Caminho 1 - Lei de Ohm / LKC):**
Pela Lei de Kirchhoff das Correntes (LKC) no Nó A, toda a corrente que entra pelo indutor ($i(t)$) deve se dividir e descer pelos dois resistores.
Como os resistores estão em paralelo com a tensão $v_o(t)$, a Lei de Ohm nos diz que a corrente no resistor de 2 é $v_o(t)/2$ e no resistor de 3 é $v_o(t)/3$.
$$i(t) = i_{R2} + i_{R3}$$
$$i(t) = \frac{v_o(t)}{2} + \frac{v_o(t)}{3}$$
$$i(t) = v_o(t) \left( \frac{1}{2} + \frac{1}{3} \right)$$
$$i(t) = v_o(t) \left( \frac{3}{6} + \frac{2}{6} \right)$$
$$i(t) = v_o(t) \left( \frac{5}{6} \right)$$
Isolando o $v_o(t)$:
$$v_o(t) = i(t) \cdot \frac{6}{5}$$
$$v_o(t) = 1,2 \cdot i(t)$$
Substituindo $i(t) = 5e^{-3t}$:
$$v_o(t) = 1,2 \cdot (5e^{-3t})$$
$$v_o(t) = \mathbf{6e^{-3t}\text{ V}}$$

---

**Resolução Final (Caminho da Derivada):**
Usando o Caminho 2, sabemos que a tensão cai do 0V (fio de baixo) para o Nó A.
Portanto:
$$v_o(t) = - v_{\text{indutor}}$$
$$v_o(t) = - \left( L \cdot \frac{di}{dt} \right)$$
$$v_o(t) = -0,4 \cdot \frac{d}{dt} \left( 5e^{-3t} \right)$$
$$v_o(t) = -0,4 \cdot \left( 5 \cdot (-3) e^{-3t} \right)$$
$$v_o(t) = -0,4 \cdot \left( -15e^{-3t} \right)$$
$$v_o(t) = \mathbf{6e^{-3t}\text{ V}}$$

> [!TIP]
> **Receita de Bolo: Análise de Circuitos de Primeira Ordem**
> 1. **Análise em t < 0:** Identifique o estado da chave. Calcule $v(0)$ para capacitores ou $i(0)$ para indutores (eles se comportam como circuito aberto e curto-circuito, respectivamente, em CC).
> 2. **Análise em t > 0:** Redesenhe o circuito com a chave na nova posição. Encontre a resistência equivalente $R_{eq}$ vista pelo capacitor/indutor.
> 3. **Constante de Tempo ($\tau$):** Calcule $\tau = R_{eq}C$ (para RC) ou $\tau = L/R_{eq}$ (para RL).

## ✍️ Sua Vez!
*(Deixe sua resolução passo a passo aqui)*
