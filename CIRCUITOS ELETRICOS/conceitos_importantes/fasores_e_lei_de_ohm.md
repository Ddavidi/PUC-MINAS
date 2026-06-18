# 🔄 Fasores e a Lei de Ohm (Z = V/I)
### O Guia Definitivo para Entender a Base de Circuitos CA

Fica tranquilo, é muito normal ter dificuldade nessa parte porque ela mistura física com números complexos. Vamos dar um passo para trás e entender o que é um fasor e de onde vem essa fórmula mágica `Z = V/I`.

---

## 1. O que é um Fasor e como converter?

Em circuitos de corrente alternada (CA), as fontes de tensão e corrente não são números fixos (como uma pilha de 9V), elas ficam "balançando" como uma onda no tempo. 

Uma tensão no tempo tem essa cara matemática:
`v(t) = Vm * cos(ωt + φ)`

Onde:
- **Vm** é a **amplitude** (o tamanho máximo da onda, ex: 120 V).
- **ω** é a **frequência angular** (quão rápido ela balança, ex: 377 rad/s).
- **φ** é a **fase** (o atraso ou adiantamento da onda, ex: 30°).

Trabalhar com cossenos e senos nas contas de circuitos (que envolvem derivadas e integrais por causa dos indutores e capacitores) é um pesadelo matemático.

### A sacada do Fasor:
Como todos os elementos em um circuito linear vão "balançar" na **mesma frequência ω**, a gente pode "esquecer" o `ωt` nas contas e focar só no que importa: **o tamanho da onda (Vm) e o ângulo dela (φ)**.

Um fasor é simplesmente pegar essa onda no tempo e transformar em um número complexo (polar) com essas duas informações:

> **Tempo:** `v(t) = Vm * cos(ωt + φ)`  ➡️  **Fasor:** `V = Vm ∠ φ`

---

### 🛠️ Regra de Ouro para Converter para Fasor:

1. A função no tempo **TEM QUE SER UM COSSENO**.
2. A amplitude (Vm) tem que ser **positiva**.
3. Se estiver em **seno**, subtraia 90° do ângulo para virar cosseno: 
   `sen(ωt + φ)  ➡️  cos(ωt + φ - 90°)`
4. Pegue o Vm e o ângulo final. Esse é o seu fasor!

> [!TIP]
> **Exemplos Rápidos de Conversão:**
> - `v(t) = 50 cos(10t + 30°)` ➡️ **V = 50 ∠ 30°**
> - `i(t) = 10 cos(377t - 45°)` ➡️ **I = 10 ∠ -45°**
> - `v(t) = 20 sen(5t + 10°)` ➡️ *(Tem que subtrair 90°)* ➡️ **V = 20 ∠ (10° - 90°) = 20 ∠ -80°**

---

## 2. A Lei de Ohm Fasorial (Z = V/I)

Na corrente contínua (CC), você aprendeu a velha e boa Lei de Ohm: `R = V / I` (Resistência é Tensão dividida por Corrente). A resistência só atrapalha a corrente.

Na corrente alternada (CA), nós temos os resistores, mas também temos os indutores (L) e os capacitores (C). Em CA, os indutores e capacitores também atrapalham a corrente, mas de um jeito mais "complexo": eles não apenas seguram a corrente, mas também **atrasam ou adiantam a onda**!

Para colocar resistores, indutores e capacitores no mesmo balaio, inventaram a **Impedância (Z)**.
A impedância Z é um número complexo que diz duas coisas ao mesmo tempo:
1. O quanto o elemento reduz o tamanho da corrente (magnitude).
2. O quanto o elemento defasa (gira) o ângulo da corrente (fase).

Então, a Lei de Ohm evolui para:
> `V = Z * I`  ➡️  `Z = V / I`

Como V e I agora são Fasores (números complexos), a impedância Z também é um número complexo.

### As 3 Impedâncias Básicas que você precisa saber de cor:
A impedância depende da frequência `ω` do circuito.

- **Resistor (R):** Não liga pra frequência. `Z_R = R` (número real).
- **Indutor (L):** `Z_L = j * ω * L` (número imaginário puro positivo).
- **Capacitor (C):** `Z_C = 1 / (j * ω * C) = -j / (ω * C)` (número imaginário puro negativo).

*(Esse "j" na frente do número significa que ele gira a onda em 90 graus).*

---

## 📌 Receita de Bolo: O Passo a Passo Geral para Circuitos CA

Para resolver *qualquer* problema de circuito CA (Corrente Alternada), você sempre vai seguir estes 6 passos lógicos:

1. **Ache o ω** da fonte (o número que multiplica o 't').
2. **Converta a fonte para fasor** (Lembrete: se for seno, subtraia 90° para virar cosseno).
3. **Calcule a impedância** de cada componente usando as fórmulas: `R ➡️ R`, `L ➡️ jωL`, `C ➡️ 1/(jωC)`.
4. **Combine as impedâncias** (Série ➡️ soma, Paralelo ➡️ produto sobre soma) para achar a impedância equivalente (Z_eq) do circuito.
5. **Aplique a Lei de Ohm (V = Z * I)** e/ou as Leis de Kirchhoff para achar o valor que o problema pede.
6. **Volte para o domínio do tempo** transformando o fasor resultante na forma `Vm * cos(ωt + φ)`.

---

## 💡 Vamos ver isso na prática (Problema 9.20)

**Enunciado:** Um circuito tem corrente `i = 7,5 cos(10t + 30°)` A e tensão de saída `v = 120 cos(10t + 75°)` V. Determine a impedância Z.

**Passo 1: Achar ω**
Olhando as equações, quem multiplica o "t" é o 10. Então `ω = 10 rad/s`. As duas ondas estão na mesma frequência, ótimo!

**Passo 2: Converter para fasores**
As duas já estão em cosseno e são positivas. É só pegar o número da frente e o ângulo.
- `I = 7,5 ∠ 30° A`
- `V = 120 ∠ 75° V`

**Passo 3: Aplicar a Lei de Ohm Fasorial**
> **🤔 Por que pulamos o cálculo de L e C (Passo 3 da receita)?** 
> *Neste problema específico, nós não temos o desenho do circuito detalhando onde estão os indutores e capacitores. O problema trata o circuito como uma "caixa preta" e já nos dá a tensão e a corrente finais, pedindo diretamente o `Z` total da caixa. Então pulamos direto para o Passo 5 da nossa receita!*

Queremos achar a impedância do circuito que está causando essa mudança na onda.
- `Z = V / I`
- `Z = (120 ∠ 75°) / (7,5 ∠ 30°)`

**Passo 4: Divisão de números polares**
Na divisão polar, a regra é fácil: **Divide os tamanhos, subtrai o ângulo de cima pelo de baixo.**
- Tamanho: `120 / 7,5 = 16`
- Ângulo: `75° - 30° = 45°`

> **Resposta Final:** `Z = 16 ∠ 45° Ω`

**O que isso significa fisicamente?**
Isso significa que a "caixa preta" do circuito tem uma impedância que corta a tensão por 16 para gerar a corrente, e rotaciona a fase em 45°. 

Se convertermos `16 ∠ 45°` para forma retangular (a + jb) usando `16*cos(45°) + j*16*sen(45°)`, dá `11,31 + j11,31 Ω`. A parte real (11,31) é a resistência, e a parte imaginária (j11,31) é a influência dos indutores/capacitores!
