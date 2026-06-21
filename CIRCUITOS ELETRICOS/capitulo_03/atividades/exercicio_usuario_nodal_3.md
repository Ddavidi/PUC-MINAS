# Resolução: Circuito Enviado 2 (Com Condutâncias)

Este é um exercício de nível **Mestre** em Análise Nodal. Ele foi projetado por um professor com uma criatividade incrível! 

Primeiro, perceba que as unidades estão em **S (Siemens)**. Siemens é a unidade de **Condutância** ($G$), que é o inverso da Resistência ($G = 1/R$).
Em vez de dividir a tensão pela resistência, nós simplesmente **multiplicamos a tensão pela condutância** ($I = V \cdot G$). Fica até mais fácil pois não temos frações!

**Enunciado:** Determine as tensões $V_1$ (esquerda), $V_2$ (meio) e $V_3$ (direita).

![Circuito Enviado 2](../../_base_dados_ia/imagens_geradas/usuario_nodal_3.png)

---

## Passo a Passo

### 1. Equação do Nó $V_1$ (Esquerda)
Correntes fugindo:
1. Fonte de $3A$ para a direita: **$+3$**
2. Fonte de $8A$ para o Terra (flecha para baixo): **$+8$**
3. Caminho superior para $V_3$: **$4 \cdot (V_1 - V_3)$**
4. Caminho do meio para $V_2$: **$3 \cdot (V_1 - V_2)$**

Equação:
$$ 3 + 8 + 4(V_1 - V_3) + 3(V_1 - V_2) = 0 $$
$$ 11 + 4V_1 - 4V_3 + 3V_1 - 3V_2 = 0 $$
$$ 7V_1 - 3V_2 - 4V_3 = -11 \quad \text{--- (Equação 1)} $$

### 2. Equação do Nó $V_2$ (Centro)
Correntes fugindo:
1. Fonte de $3A$ que veio do $V_1$ está **entrando**: **$-3$**
2. Caminho de volta para $V_1$: **$3 \cdot (V_2 - V_1)$**
3. Caminho para o Terra: **$1 \cdot (V_2 - 0) = V_2$**
4. Caminho para $V_3$: **$2 \cdot (V_2 - V_3)$**

Equação:
$$ -3 + 3V_2 - 3V_1 + V_2 + 2V_2 - 2V_3 = 0 $$
$$ -3V_1 + 6V_2 - 2V_3 = 3 \quad \text{--- (Equação 2)} $$

### 3. Equação do Nó $V_3$ (Direita)
Correntes fugindo:
1. Fonte de $-25A$ para o Terra (flecha para baixo). Como ela **foge**, usamos o valor exatamente como está: **$-25$**
2. Caminho superior de volta para $V_1$: **$4 \cdot (V_3 - V_1)$**
3. Caminho do meio de volta para $V_2$: **$2 \cdot (V_3 - V_2)$**

Equação:
$$ -25 + 4V_3 - 4V_1 + 2V_3 - 2V_2 = 0 $$
$$ -4V_1 - 2V_2 + 6V_3 = 25 \quad \text{--- (Equação 3)} $$

---

### O Truque de Gênio do Exercício
Olhe para o nosso sistema linear:
1) $7V_1 - 3V_2 - 4V_3 = -11$
2) $-3V_1 + 6V_2 - 2V_3 = 3$
3) $-4V_1 - 2V_2 + 6V_3 = 25$

Se você somar as três equações lado a lado (como se todo o circuito fosse um nó só), olhe o que acontece com as colunas de $V_1$ e $V_3$:
- Coluna $V_1$: $7 - 3 - 4 = 0$
- Coluna $V_3$: $-4 - 2 + 6 = 0$
- Coluna $V_2$: $-3 + 6 - 2 = 1$
- Resultado: $-11 + 3 + 25 = 17$

**Somando tudo, temos instantaneamente:**
$$ 1V_2 = 17 \implies V_2 = 17 \, V $$

Agora fica fácil! Substitua $V_2 = 17$ nas equações 1 e 2:
- Eq 1: $7V_1 - 3(17) - 4V_3 = -11 \implies 7V_1 - 4V_3 = 40$
- Eq 2: $-3V_1 + 6(17) - 2V_3 = 3 \implies -3V_1 - 2V_3 = -99$

Multiplicando a Eq 2 por $2$ e subtraindo da Eq 1, chegamos nos valores finais.

---
> **✅ Respostas Finais:** 
> - **$V_1 = \frac{238}{13} \, V$** (aprox. $18,3 \, V$)
> - **$V_2 = 17 \, V$**
> - **$V_3 = \frac{573}{26} \, V$** (aprox. $22,04 \, V$)

---

## O Caminho Ninja: Método de Inspeção (Matrizes)

Como vimos, resolver o sistema de 3 equações na mão dá trabalho. Mas com a sua calculadora, você pode usar o **Método de Inspeção** e pular toda a montagem das equações, montando a matriz diretamente "de cabeça" só olhando pro desenho.

A regra da matriz $[G] \cdot [V] = [I]$ é a seguinte:
1. **Diagonal Principal (Posições 1,1 | 2,2 | 3,3):** Soma de todas as condutâncias ligadas no nó (sempre positivo).
2. **Posições Fora da Diagonal:** Condutância que liga um nó ao outro (sempre negativo).
3. **Vetor de Corrente (Depois do igual):** Correntes de fonte **entrando** no nó são Positivas. **Saindo** são Negativas.

Montando no olhômetro:
- Para o $V_1$: As condutâncias encostadas nele são 4S e 3S (Soma = **7**). Entre V1 e V2 tem 3S (vira **-3**). Entre V1 e V3 tem 4S (vira **-4**). As fontes de corrente nele (8A e 3A) estão saindo, logo **-11**.
- Para o $V_2$: Encostadas nele (3S, 1S, 2S = **6**). Entre V2 e V1 tem **-3**. Entre V2 e V3 tem **-2**. Fonte entrando nele é 3A (**+3**).
- Para o $V_3$: Encostadas nele (4S e 2S = **6**). Entre V3 e V1 tem **-4**. Entre V3 e V2 tem **-2**. Fonte de -25A "saindo" significa que, na verdade, entra +25A. Logo: **25**.

Olhe como a matriz se forma em 30 segundos sem fazer conta de frações:
$$
\begin{bmatrix}
7 & -3 & -4 \\
-3 & 6 & -2 \\
-4 & -2 & 6
\end{bmatrix}
\cdot
\begin{bmatrix}
V_1 \\
V_2 \\
V_3
\end{bmatrix}
=
\begin{bmatrix}
-11 \\
3 \\
25
\end{bmatrix}
$$

Este é exatamente o mesmo sistema que montamos lá em cima. Agora é só jogar isso no aplicativo `Equação` da sua Casio e correr pro abraço!
