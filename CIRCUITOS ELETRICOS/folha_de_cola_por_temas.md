# 📄 Folha de Cola Temática

Esta folha reúne as ferramentas matemáticas e os métodos de análise consolidados por temas, ideal para não precisar ficar pulando entre capítulos para achar algo interligado. **Sem resoluções, apenas a estrutura lógica.**

---

## 🛠️ Tema 1: Propriedades Físicas (C e L)

### Associações e Constantes
| Componente | Série | Paralelo | Equação Carga/Descarga | Constante de Tempo (τ) |
| :--- | :--- | :--- | :--- | :--- |
| **Resistor** | Soma `R1+R2` | Produto/Soma | `N/A` | `N/A` |
| **Capacitor** | Produto/Soma | Soma `C1+C2` | Tensão não muda bruscamente | `τ = Req * C` |
| **Indutor** | Soma `L1+L2` | Produto/Soma | Corrente não muda bruscamente | `τ = L / Req` |

### O Macete do Regime Permanente (CC)
- Quando passa muito tempo (`t < 0` ou `t = ∞`), se for apenas fonte DC (Bateria de Tensão contínua ou Corrente constante):
  - **Capacitor vira Fio Partindo/Aberto** (Acha a tensão nos pontos rompidos).
  - **Indutor vira Fio Reto/Curto** (Acha a corrente que passa nele).

---

## 🧩 Tema 2: Passo a Passo (Transientes 1ª Ordem)

Se o problema tem uma chave abrindo ou fechando em `t=0`, use a **Receita do Degrau**:

1. **Ache a Condição Inicial:** Olhe para `t < 0`, assuma regime permanente (macete acima) e descubra `v_c(0)` ou `i_L(0)`.
2. **Transferência:** `v_c(0-) = v_c(0+)`.
3. **Equivalência em t > 0:** Apague (curto p/ tensão, aberto p/ corrente) as fontes independentes em `t > 0`. Ache a resistência total (`Req`) "vista" de onde o L ou C foi tirado.
4. **Calcule τ:** Use `τ = Req * C` ou `τ = L / Req`.
5. **Ache o Infinito:** Com o circuito montado para `t > 0`, assuma regime permanente novamente e descubra a tensão/corrente nova final `x(∞)`.
6. **Fórmula Mestra:** `x(t) = x(∞) + [x(0+) - x(∞)] * e^(-t/τ)`

---

## 🔄 Tema 3: O Mundo de CA (Fasores e Impedâncias)

### Conversão Tempo ➡️ Frequência
1. Sempre garanta que a fonte está em **cosseno positivo**. (Se for seno, faz -90° no ângulo interno).
2. Puxa a Amplitude (`Vm`) e a Fase (`φ`).
3. Fasor = `Vm ∠ φ`.
4. Leia o valor de `ω` que multiplica o `t` dentro do cosseno.

### As Impedâncias (A "Resistência" da CA)
- `Z_Resistor = R`
- `Z_Indutor = j * ω * L`
- `Z_Capacitor = -j / (ω * C)`

*Na forma polar:*
- Um `j` puro é `∠ 90°`. Um `-j` puro é `∠ -90°`.
- *Ex:* Indutor fica `(ωL) ∠ 90°`. Capacitor fica `(1/ωC) ∠ -90°`.

### A Álgebra
- Para **Multiplicar e Dividir**, use o modo Polar (`10 ∠ 30°`).
- Para **Somar e Subtrair** (ex: Lei dos Nós ou Série), use o modo Retangular (`8,66 + j5`).

---

## ⚡ Tema 4: Tudo sobre Potência em CA

Muitas vezes você precisará dos valores RMS (Dividir amplitude de pico por √2). Cuidado com qual valor a fórmula pede!

1. **Potência Aparente (S):** `S = V_rms * I_rms` [VA]
2. **Potência Média/Real (P):** `P = S * cos(θ_v - θ_i)` [W]
3. **Potência Reativa (Q):** `Q = S * sen(θ_v - θ_i)` [VAR]
4. **Potência Complexa (vetor completo):** `S = P + jQ`
   - O *Santo Graal* das fórmulas: `S = V_fasor_rms * (I_fasor_rms)*` (Use sempre o conjugado da corrente!).
5. **Fator de Potência (FP):** `FP = P / |S| = cos(θ_v - θ_i)`.
   - Atrasa = Indutivo.
   - Adianta = Capacitivo.
6. **Casamento de Impedância:** Para extrair a potência máxima, a impedância de carga tem que espelhar invertendo o j da Thevenin. `Z_L = Z_Th*`.
