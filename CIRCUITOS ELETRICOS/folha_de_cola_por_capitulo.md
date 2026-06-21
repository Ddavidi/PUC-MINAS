# 📄 Folha de Cola: Por Capítulos (6, 7, 9 e 11)

Esta folha reúne as fórmulas vitais e os "passo-a-passo" de cada capítulo cobrado na prova. **Sem resoluções numéricas, apenas os caminhos.**

---

## ⚡ Capítulo 6: Capacitores e Indutores

### Comportamento em Corrente Contínua (Regime Permanente)
- **Capacitor (C):** Funciona como um **Circuito Aberto** (a corrente não passa).
- **Indutor (L):** Funciona como um **Curto-Circuito** (passa livre como um fio comum).

### Fórmulas Base (no tempo)
| Componente | Equação de Tensão | Equação de Corrente | Energia Armazenada (W) |
| :--- | :--- | :--- | :--- |
| **Capacitor** | `v = (1/C) * ∫ i dt` | `i = C * (dv/dt)` | `W = (1/2) * C * v²` |
| **Indutor** | `v = L * (di/dt)` | `i = (1/L) * ∫ v dt` | `W = (1/2) * L * i²` |

### Associação de Componentes
- **Capacitores:** `Série` se resolve como resistores em paralelo. `Paralelo` se resolve como resistores em série (soma direta).
- **Indutores:** Resolve igual resistor. (`Série` soma; `Paralelo` faz produto/soma).

---

## ⏱️ Capítulo 7: Circuitos de Primeira Ordem (RC e RL)

A chave vira no instante `t = 0`. O segredo é saber que a tensão no Capacitor e a corrente no Indutor **nunca mudam bruscamente**.
- `vc(0-) = vc(0+)`
- `iL(0-) = iL(0+)`

### A Equação Geral do Degrau
Serve para achar qualquer valor no circuito após a chave virar:
> `x(t) = x(∞) + [x(0+) - x(∞)] * e^(-t/τ)`

### Receita de Bolo: Os 6 Passos
1. **Analise `t < 0`:** Com a chave na posição original e o circuito há muito tempo ligado (regime permanente CC). Troque C por circuito aberto e L por curto-circuito. Ache a tensão inicial `v(0)` ou corrente inicial `i(0)`.
2. **Transferência de Estado:** Garanta que os valores achados acima passam intactos para `t = 0+`.
3. **Analise `t > 0`:** Com a chave na nova posição, "desligue" todas as fontes independentes do circuito (fonte de tensão vira curto, corrente vira aberto).
4. **Ache a Resistência Equivalente (`Req`):** Olhando a partir dos terminais onde o Capacitor ou Indutor estava conectado.
5. **Calcule a Constante de Tempo (`τ`):** 
   - Para RC: `τ = Req * C`
   - Para RL: `τ = L / Req`
6. **Ache o valor de `∞`:** Com o circuito em `t > 0` ainda conectado, analise-o como se muito tempo se passasse (novamente em regime permanente CC, usando aberto/curto). Encontre `v(∞)` ou `i(∞)`. Jogue na Equação Geral.

---

## 🔄 Capítulo 9: Senoides e Fasores

O objetivo é transformar funções trigonométricas ruins de calcular em números complexos fáceis.

### Fórmulas de Conversão e Domínio Fasorial
- `v(t) = Vm * cos(ωt + φ)`  ➡️  `V = Vm ∠ φ`
- Se for **seno**, subtraia 90°: `sen(ωt + φ) ➡️ cos(ωt + φ - 90°)`

### A Nova Lei de Ohm (`V = Z * I`)
Aqui, a Impedância `Z` manda no jogo:
- **Resistor:** `Z_R = R`
- **Indutor:** `Z_L = j * ω * L`
- **Capacitor:** `Z_C = 1 / (j * ω * C)` ou `-j / (ω * C)`

### Álgebra Complexa (Dicas Rápidas)
- **Multiplicação Polar:** Multiplica as magnitudes, SOMA os ângulos.
- **Divisão Polar:** Divide as magnitudes, SUBTRAI os ângulos (cima menos o de baixo).
- **Soma/Subtração:** Só faça convertendo para Retangular (a + jb) antes!

---

## ⚡ Capítulo 11: Análise de Potência em CA

Muitas fórmulas derivadas, cuidado com os valores RMS vs Amplitude (Vm).

### Valor Eficaz (RMS)
Para ondas senoidais perfeitas: `V_rms = Vm / √2` e `I_rms = Im / √2`.

### As 3 Potências
1. **Potência Real/Média (P):** O que realmente faz trabalho (Watts).
   `P = V_rms * I_rms * cos(θv - θi)`
2. **Potência Reativa (Q):** Fica "batendo e voltando" (VAR).
   `Q = V_rms * I_rms * sen(θv - θi)`
3. **Potência Aparente (S):** O módulo da junção das duas (VA).
   `S = V_rms * I_rms` ou `|S| = √(P² + Q²)`

### O Triângulo de Potências e Potência Complexa
A Potência Complexa junta P e Q em um único Fasor:
> **`S = P + jQ`**  (Forma Retangular)
> **`S = V_rms * (I_rms)*`** (Atenção: A corrente é conjugada! Multiplique V pelo I invertendo o sinal do ângulo da corrente).

### Fator de Potência (FP)
> `FP = cos(θv - θi) = P / S`
- Se a corrente está atrasada da tensão (indutivo): FP Atrasado.
- Se a corrente está adiantada da tensão (capacitivo): FP Adiantado.

### Máxima Transferência de Potência Média
Para uma carga puxar a potência máxima possível do circuito:
`Z_carga = Z_Thevenin*` (A impedância de carga deve ser o conjugado complexo da impedância de Thevenin do circuito. Ex: se Z_th = 5 + j2, a carga deve ser 5 - j2).
