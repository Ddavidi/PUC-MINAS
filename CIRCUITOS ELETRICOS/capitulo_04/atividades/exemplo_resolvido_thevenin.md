# Exemplo Resolvido Clássico: Teorema de Thevenin

Este é um exercício clássico que mistura fonte de tensão e fonte de corrente. Vamos aplicar a **Receita de Bolo do Thevenin** mostrada no `resgate_da_base.md` passo a passo.

**Enunciado:** Determine o circuito equivalente de Thevenin (ou seja, encontre $R_{th}$ e $V_{th}$) visto pelos terminais A e B no circuito abaixo.

![Circuito Original](/c:/Users/DD/Documents/DD/PUC%20MINAS/PUC-MINAS/CIRCUITOS%20ELETRICOS/_base_dados_ia/imagens_geradas/thevenin_ex.png)

---

## Parte 1: Calculando a Resistência de Thevenin ($R_{th}$)

A regra é: olhe pelos terminais A e B com **todas as fontes independentes desligadas**.
- Fonte de Tensão de $32V \implies$ Vira um Curto-Circuito (fio liso aterrado).
- Fonte de Corrente de $2A \implies$ Vira um Circuito Aberto (nós a arrancamos do circuito).

O circuito para calcularmos a $R_{th}$ fica assim:
![Circuito para Rth](/c:/Users/DD/Documents/DD/PUC%20MINAS/PUC-MINAS/CIRCUITOS%20ELETRICOS/_base_dados_ia/imagens_geradas/thevenin_rth.png)

**Resolvendo:**
1. Olhando de trás para frente (da esquerda para a direita em direção aos terminais A-B).
2. O resistor de $4 \, \Omega$ e o de $12 \, \Omega$ estão ligados entre o Nó C e o Terra. Isso significa que eles estão em **Paralelo**.
   $$ R_{paralelo} = \frac{4 \cdot 12}{4 + 12} = \frac{48}{16} = 3 \, \Omega $$
3. Esse bloco equivalente de $3 \, \Omega$ fica em **série** com o resistor de $1 \, \Omega$ que liga o Nó C ao terminal A.
   $$ R_{th} = 3 + 1 = 4 \, \Omega $$

> **✅ Resultado da Parte 1:** $R_{th} = 4 \, \Omega$.

---

## Parte 2: Calculando a Tensão de Thevenin ($V_{th}$)

A regra é: ligue as fontes de volta, deixe os terminais A e B **abertos** (no vazio) e calcule a tensão entre eles ($V_A - V_B$).

Como o terminal A está no vazio, **nenhuma corrente passa pelo resistor de $1 \, \Omega$**. Logo, a queda de tensão nele é zero. Isso significa que a tensão no terminal A é exatamente igual à tensão no Nó C ($V_{th} = V_A = V_C$).

Vamos desenhar a nossa missão usando a Análise Nodal no Nó C:
![Circuito para Vth](/c:/Users/DD/Documents/DD/PUC%20MINAS/PUC-MINAS/CIRCUITOS%20ELETRICOS/_base_dados_ia/imagens_geradas/thevenin_vth.png)

**Resolvendo (Aplicando LKC no Nó C):**
1. Corrente saindo para a esquerda (passando pelo de $4 \, \Omega$): $\frac{V_C - 32}{4}$
2. Corrente saindo para baixo (passando pelo de $12 \, \Omega$): $\frac{V_C - 0}{12}$
3. A fonte de $2A$ está **entrando** no nó C. Como na nossa receita todas as correntes "fogem", colocamos ela negativa (ou no lado direito da igualdade).

$$ \frac{V_C - 32}{4} + \frac{V_C}{12} - 2 = 0 $$

*Para facilitar a matemática, vamos multiplicar tudo por 12:*
$$ 3 \cdot (V_C - 32) + 1 \cdot (V_C) - 24 = 0 $$
$$ 3V_C - 96 + V_C - 24 = 0 $$
$$ 4V_C - 120 = 0 \implies 4V_C = 120 $$
$$ V_C = 30 \, V $$

> **✅ Resultado da Parte 2:** $V_{th} = V_C = 30 \, V$.

---
### O Circuito Equivalente Final
Todo aquele circuito monstruoso original pode ser substituído por uma simples fonte de **$30V$** em série com um resistor de **$4 \, \Omega$**. É esse "combo" simplificado que você usará quando formos calcular as descargas de capacitores no Capítulo 7!
