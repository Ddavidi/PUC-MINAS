# Resumo Teórico: Capítulo 6 — Capacitores e Indutores

Neste capítulo, somos apresentados a dois novos elementos de circuito passivos: o **Capacitor** e o **Indutor**. Diferente do resistor, que apenas dissipa energia (transforma energia elétrica em calor), esses novos componentes conseguem **armazenar energia** e devolvê-la ao circuito depois.

---

## 1. O Capacitor (C)
O capacitor é basicamente construído por duas placas metálicas separadas por um isolante (chamado de dielétrico). Ele armazena energia na forma de um **campo elétrico**.
- **Unidade:** Farad (F). Como 1 Farad é algo gigantesco, é muito comum usarmos microfarads (μF), nanofarads (nF) ou picofarads (pF).

### Equações Fundamentais
A relação entre a carga ($q$), a capacitância ($C$) e a tensão ($v$) é dada por:
> $q = C \cdot v$

Derivando essa equação no tempo, chegamos na fórmula mais importante do capacitor (como a corrente se relaciona com a tensão):
> $i = C \cdot \frac{dv}{dt}$

**O que essa fórmula nos ensina na prática?**
1. Se a tensão for constante (Corrente Contínua - CC), a derivada é zero. Ou seja, $i = 0$. Isso significa que **em CC, o capacitor se comporta como um circuito aberto** (um fio cortado).
2. A tensão em um capacitor não pode mudar instantaneamente. Se a tensão mudasse de 0 para 5V em zero segundos, a derivada seria infinita, exigindo uma corrente infinita (o que é fisicamente impossível).

### Invertendo a Fórmula (Tensão)
Se quisermos achar a tensão a partir da corrente, integramos:
> $v(t) = \frac{1}{C} \int_{t_0}^{t} i(\tau) d\tau + v(t_0)$
*(Onde $v(t_0)$ é a tensão inicial que o capacitor já tinha armazenada).*

### Energia Armazenada
> $w = \frac{1}{2} C \cdot v^2$ (Dada em Joules)

---

## 2. O Indutor (L)
O indutor é feito enrolando um fio condutor (uma bobina). Quando uma corrente passa por ele, ele armazena energia na forma de um **campo magnético**.
- **Unidade:** Henry (H). É comum usarmos milihenrys (mH) ou microhenrys (μH).

### Equação Fundamental
A tensão no indutor depende da variação da corrente no tempo:
> $v = L \cdot \frac{di}{dt}$

**O que essa fórmula nos ensina na prática?**
1. Se a corrente for constante (Corrente Contínua - CC), a derivada é zero. Ou seja, $v = 0$. Isso significa que **em CC, o indutor se comporta como um curto-circuito** (um fio liso sem resistência).
2. A corrente em um indutor não pode mudar instantaneamente. Tentar cortar a corrente de um indutor de repente gera uma tensão ("faísca") gigantesca.

### Invertendo a Fórmula (Corrente)
> $i(t) = \frac{1}{L} \int_{t_0}^{t} v(\tau) d\tau + i(t_0)$

### Energia Armazenada
> $w = \frac{1}{2} L \cdot i^2$ (Dada em Joules)

---

## 3. Associações em Série e Paralelo

A regra de ouro aqui é: **O Indutor se comporta igual ao Resistor. O Capacitor faz tudo ao contrário.**

### Indutores (Fórmulas iguais aos Resistores)
- **Série:** Soma tudo. $\implies L_{eq} = L_1 + L_2 + ... + L_N$
- **Paralelo:** Produto pela soma (para 2) ou soma dos inversos. $\implies \frac{1}{L_{eq}} = \frac{1}{L_1} + \frac{1}{L_2} + ...$

### Capacitores (Fórmulas invertidas)
- **Paralelo:** Soma tudo. $\implies C_{eq} = C_1 + C_2 + ... + C_N$
- **Série:** Produto pela soma. $\implies \frac{1}{C_{eq}} = \frac{1}{C_1} + \frac{1}{C_2} + ...$

---

## 💡 Resumo do Comportamento (O Mais Importante para a Prova)

| Componente | O que ele armazena? | Comportamento em Regime CC (Muito tempo ligado) | Regra de Continuidade (O que não muda do nada) |
| :--- | :--- | :--- | :--- |
| **Capacitor** | Tensão (Campo Elétrico) | **Circuito Aberto** (rompe o fio) | A **Tensão** não muda instantaneamente. |
| **Indutor** | Corrente (Campo Magnético)| **Curto-Circuito** (fio reto) | A **Corrente** não muda instantaneamente. |
