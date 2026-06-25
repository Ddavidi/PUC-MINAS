# 📘 Capítulo 9 — Senoides e Fasores
### Fundamentos de Circuitos Elétricos — Sadiku, 5ª Edição (Páginas 349–388)

---

## 📋 Índice do Capítulo
| Seção | Tópico |
|-------|--------|
| 9.1 | Introdução |
| 9.2 | Senoides |
| 9.3 | Fasores |
| 9.4 | Relações entre fasores para elementos de circuitos |
| 9.5 | Impedância e admitância |
| 9.6 | Leis de Kirchhoff no domínio da frequência |
| 9.7 | Associações de impedâncias |
| 9.8 | Aplicações (Comutadores de fase e Pontes CA) |

---

## 9.1 — Introdução

Até aqui, a análise se limitou a **circuitos CC** (fontes constantes). Agora entramos na análise de circuitos onde a fonte **varia com o tempo** — especificamente, excitação **senoidal**.

> [!IMPORTANT]
> **Senoide** = sinal com forma de seno ou cosseno. Corrente senoidal = **Corrente Alternada (CA)**.

### Por que senoides são importantes?
1. **A natureza é senoidal** — pêndulos, ondas, vibrações, circuitos subamortecidos
2. **Fáceis de gerar e transmitir** — forma dominante de energia elétrica
3. **Análise de Fourier** — qualquer sinal periódico = soma de senoides
4. **Fáceis de manipular** — derivada e integral de senoide = senoide

### Resposta de um circuito CA
- **Resposta transiente** → extingue-se com o tempo
- **Resposta em regime estacionário** → permanece (é o que nos interessa!)

---

## 9.2 — Senoides

### Forma geral
```
v(t) = Vm · sen(ωt)
```

| Símbolo | Significado | Unidade |
|---------|-------------|---------|
| **Vm** | Amplitude da senoide | V ou A |
| **ω** | Frequência angular | rad/s |
| **ωt** | Argumento da senoide | rad ou ° |

### Relações fundamentais

| Fórmula | Descrição |
|---------|-----------|
| **T = 2π/ω** | Período (segundos por ciclo) |
| **f = 1/T** | Frequência cíclica (Hz) |
| **ω = 2πf** | Relação entre ω e f |

> [!NOTE]
> **Periodicidade**: v(t + T) = v(t) → a função se repete a cada T segundos.

### Forma genérica com fase
```
v(t) = Vm · sen(ωt + φ)
```
- **(ωt + φ)** = argumento
- **φ** = fase (em radianos ou graus)

### Comparação entre duas senoides
Dadas:
```
v₁ = Vm · sen(ωt)
v₂ = Vm · sen(ωt + φ)
```
- Se **φ ≠ 0** → v₁ e v₂ estão **fora de fase**
- Se **φ = 0** → estão **em fase**
- v₂ está **avançada** em relação a v₁ em φ
- v₁ está **atrasada** em relação a v₂ em φ

> [!TIP]
> Só é possível comparar fases de senoides com a **mesma frequência**!

### Identidades trigonométricas essenciais
```
sen(A ± B) = sen A · cos B ± cos A · sen B
cos(A ± B) = cos A · cos B ∓ sen A · sen B
```

### Conversões importantes
| Conversão | Resultado |
|-----------|-----------|
| sen(ωt ± 180°) | = −sen(ωt) |
| cos(ωt ± 180°) | = −cos(ωt) |
| sen(ωt − 90°) | = −cos(ωt) |
| cos(ωt − 90°) | = sen(ωt) |
| sen(ωt + 90°) | = cos(ωt) |
| cos(ωt + 90°) | = −sen(ωt) |

### Soma de senoides (Eq. 9.11–9.12)
```
A·cos(ωt) + B·sen(ωt) = C·cos(ωt − θ)
```
onde:
```
C = √(A² + B²)
θ = arctan(B/A)
```

### 📝 Exemplo 9.1 — Determinando parâmetros
Dada: `v(t) = 12 cos(50t + 10°)`
- **Amplitude**: Vm = 12 V
- **Fase**: φ = 10°
- **Frequência angular**: ω = 50 rad/s
- **Período**: T = 2π/50 = **0,1257 s**
- **Frequência**: f = 1/T = **7,958 Hz**

### 📝 Exemplo 9.2 — Ângulo de fase entre senoides
Dadas: `v₁ = −10 cos(ωt + 50°)` e `v₂ = 12 sen(ωt − 10°)`

**Método**: expressar ambas na mesma forma (cosseno com amplitude positiva)
- v₁ = 10 cos(ωt − 130°) ou 10 cos(ωt + 230°)
- v₂ = 12 cos(ωt − 100°)
- **Resultado**: v₂ está avançada em relação a v₁ em **30°**

---

## 9.3 — Fasores

> [!IMPORTANT]
> **Fasor** = número complexo que representa a **amplitude** e a **fase** de uma senoide. É a ferramenta central para análise de circuitos CA!

### Números complexos — Formas de representação
```
z = x + jy          (forma retangular)
z = r∠φ             (forma polar)
z = r·e^(jφ)        (forma exponencial)
```
onde **j = √(−1)**

### Relações entre formas
```
r = √(x² + y²)     φ = arctan(y/x)
x = r·cos(φ)        y = r·sen(φ)
```

### Operações com números complexos

| Operação | Melhor forma | Fórmula |
|----------|-------------|---------|
| **Adição** | Retangular | z₁ + z₂ = (x₁+x₂) + j(y₁+y₂) |
| **Subtração** | Retangular | z₁ − z₂ = (x₁−x₂) + j(y₁−y₂) |
| **Multiplicação** | Polar | z₁·z₂ = r₁r₂∠(φ₁+φ₂) |
| **Divisão** | Polar | z₁/z₂ = (r₁/r₂)∠(φ₁−φ₂) |
| **Inverso** | Polar | 1/z = (1/r)∠(−φ) |
| **Raiz quadrada** | Polar | √z = √r ∠(φ/2) |
| **Conjugado** | Ambas | z* = x − jy = r∠(−φ) |

### Identidade de Euler
```
e^(jφ) = cos(φ) + j·sen(φ)
```

### Transformação senoide → fasor

| Domínio do tempo | Domínio dos fasores (Amplitude Máxima) | Domínio dos fasores (Valor Eficaz / RMS) |
|-----------------|-------------------|----------------|
| $V_m \cos(\omega t + \phi)$ | $V_m \angle \phi$ | $\frac{V_m}{\sqrt{2}} \angle \phi$ |
| $V_m \sin(\omega t + \phi)$ | $V_m \angle (\phi - 90^\circ)$ | $\frac{V_m}{\sqrt{2}} \angle (\phi - 90^\circ)$ |

> [!TIP]
> **Regra prática**: para converter seno → cosseno, subtraia 90° do argumento:
> `sen(ωt + φ) = cos(ωt + φ − 90°)`

### ⚡ CUIDADO: Amplitude Máxima vs Valor Eficaz (RMS)
Ao converter uma senoide para fasor, existem **duas formas** de representar a magnitude:
1. **Pela Amplitude Máxima ($V_m$):** Usada na maioria dos exercícios básicos de Fasores (Capítulo 9). Exemplo: $120 \cos(\omega t) \to 120 \angle 0^\circ$.
2. **Pelo Valor Eficaz ($V_{rms}$):** Usada intensamente no **Capítulo 11 (Potência)** e cobrada por alguns professores já no Capítulo 9. O Valor Eficaz é simplesmente a Amplitude Máxima dividida por $\sqrt{2}$ (para ondas senoidais).
   - *Exemplo:* $311 \cos(\omega t - 30^\circ) \to \text{RMS:} \frac{311}{\sqrt{2}} \angle -30^\circ \approx 220 \angle -30^\circ \text{ V}$.
   - *Por que usar RMS?* Porque é assim que a energia é medida no mundo real (a tomada da sua casa é 127V ou 220V RMS, não amplitude máxima).
   - **Dica de Prova:** Se a questão pedir "Fasor Tensão Eficaz", lembre-se de dividir o $V_m$ por $\sqrt{2}$. Todas as leis de Ohm ($V=ZI$) e Leis de Kirchhoff funcionam perfeitamente com valores eficazes, desde que você use RMS em tudo!

### Propriedades dos fasores na derivação e integração

| Operação no tempo | Equivalente no domínio dos fasores |
|---|---|
| **dv/dt** | **jω · V** |
| **∫v dt** | **V / jω** |

> [!IMPORTANT]
> - Diferenciar uma senoide = **multiplicar** seu fasor por **jω**
> - Integrar uma senoide = **dividir** seu fasor por **jω**
> - Somar senoides de mesma frequência = **somar** seus fasores

### Diferenças entre v(t) e V
1. v(t) = representação no **domínio do tempo**; V = no **domínio dos fasores**
2. v(t) depende do tempo; **V não depende**
3. v(t) é sempre **real**; V geralmente é **complexo**

---

## 9.4 — Relações Fasores-Elementos de Circuito

### Resumo das relações tensão-corrente

| Elemento | Domínio do tempo | Domínio da frequência | Relação de fase |
|----------|-----------------|---------------------|-----------------|
| **Resistor (R)** | v = R·i | **V = R·I** | V e I **em fase** |
| **Indutor (L)** | v = L·(di/dt) | **V = jωL·I** | I **atrasada** 90° em relação a V |
| **Capacitor (C)** | i = C·(dv/dt) | **V = I/(jωC)** | I **adiantada** 90° em relação a V |

> [!TIP]
> Mnemônico: **"ELI the ICE man"**
> - **ELI**: no indutor (**L**), a tensão (**E**) vem antes da corrente (**I**) → tensão avançada
> - **ICE**: no capacitor (**C**), a corrente (**I**) vem antes da tensão (**E**) → corrente avançada

### 📝 Exemplo 9.8
Dada: v = 12 cos(60t + 45°) aplicada a indutor de 0,1 H

**V = jωL·I** → I = V/(jωL) = 12∠45° / (j6) = 12∠45° / 6∠90° = **2∠−45° A**

No tempo: `i(t) = 2 cos(60t − 45°) A`

---

## 9.5 — Impedância e Admitância

### Impedância Z (Ω)
```
Z = V/I    ou    V = Z·I    (Lei de Ohm no domínio fasorial)
```

> A impedância **não é um fasor** — ela é a razão entre dois fasores.

### Impedância dos elementos

| Elemento | Impedância Z | Admitância Y = 1/Z |
|----------|-------------|-------------------|
| **R** | R | 1/R |
| **L** | jωL | 1/(jωL) |
| **C** | 1/(jωC) = −j/(ωC) | jωC |

### Casos extremos de frequência

| Elemento | ω = 0 (CC) | ω → ∞ (alta freq.) |
|----------|-----------|-------------------|
| **Indutor** | Z_L = 0 → **curto-circuito** | Z_L → ∞ → **circuito aberto** |
| **Capacitor** | Z_C → ∞ → **circuito aberto** | Z_C = 0 → **curto-circuito** |

### Forma retangular e polar da impedância
```
Z = R + jX          (retangular)
Z = |Z|∠θ           (polar)
```
- **R** = Resistência (parte real)
- **X** = Reatância (parte imaginária)
  - X > 0 → impedância **indutiva**
  - X < 0 → impedância **capacitiva**

```
|Z| = √(R² + X²)    θ = arctan(X/R)
R = |Z|·cos(θ)      X = |Z|·sen(θ)
```

### Admitância Y (S — siemens)
```
Y = 1/Z = G + jB
```
- **G** = Condutância (parte real)
- **B** = Susceptância (parte imaginária)

> [!WARNING]
> **G ≠ 1/R** em geral! Só vale G = 1/R quando X = 0.
> As fórmulas corretas são:
> ```
> G = R/(R² + X²)    B = −X/(R² + X²)
> ```

---

## 9.6 — Leis de Kirchhoff no Domínio da Frequência

As leis de Kirchhoff são **válidas para fasores**:

### LKT (Lei de Kirchhoff para Tensões)
```
∑ Vk = 0    (soma dos fasores de tensão em um laço = 0)
```

### LKC (Lei de Kirchhoff para Correntes)
```
∑ Ik = 0    (soma dos fasores de corrente em um nó = 0)
```

> [!NOTE]
> Com LKT e LKC validadas no domínio dos fasores, **todas as técnicas de circuitos CC** podem ser aplicadas a circuitos CA: divisão de tensão/corrente, análise nodal, análise de malhas, superposição, Thévenin/Norton, etc.

---

## 9.7 — Associações de Impedâncias

### Impedâncias em série
```
Zeq = Z₁ + Z₂ + ... + ZN
```
**Divisão de tensão** (para N=2):
```
V₁ = Z₁/(Z₁ + Z₂) · V
V₂ = Z₂/(Z₁ + Z₂) · V
```

### Impedâncias em paralelo
```
1/Zeq = 1/Z₁ + 1/Z₂ + ... + 1/ZN
Yeq = Y₁ + Y₂ + ... + YN
```
Para **duas impedâncias** em paralelo:
```
Zeq = (Z₁ · Z₂)/(Z₁ + Z₂)
```
**Divisão de corrente** (para N=2):
```
I₁ = Z₂/(Z₁ + Z₂) · I
I₂ = Z₁/(Z₁ + Z₂) · I
```

### Transformação Estrela-Triângulo (Y-Δ)

**Estrela → Triângulo (Y → Δ):**
```
Za = (Z₁Z₂ + Z₂Z₃ + Z₃Z₁) / Z₁
Zb = (Z₁Z₂ + Z₂Z₃ + Z₃Z₁) / Z₂
Zc = (Z₁Z₂ + Z₂Z₃ + Z₃Z₁) / Z₃
```

**Triângulo → Estrela (Δ → Y):**
```
Z₁ = (Zb · Zc) / (Za + Zb + Zc)
Z₂ = (Zc · Za) / (Za + Zb + Zc)
Z₃ = (Za · Zb) / (Za + Zb + Zc)
```

**Caso equilibrado** (impedâncias iguais):
```
ZΔ = 3·ZY    ou    ZY = ZΔ/3
```

---

## 9.8 — Aplicações

### 9.8.1 — Comutadores de Fase (Phase Shifters)

Circuitos RC usados para corrigir ou produzir deslocamentos de fase.

**Circuito RC — saída no resistor** (avanço de fase):
```
θ = arctan(Xc/R) = arctan(1/(ωRC))
```
→ Vo está **adiantada** em relação a Vi

**Circuito RC — saída no capacitor** (atraso de fase):
→ Vo está **atrasada** em relação a Vi

> [!NOTE]
> À medida que θ → 90°, a tensão de saída Vo → 0. Por isso, para deslocamentos > 60°, usa-se **cascata** de circuitos RC.

### 📝 Exemplo 9.13 — Avanço de 90° com cascata
Usando dois estágios RC com R = |Xc| = 20 Ω:
- Cada estágio dá 45° de avanço
- Resultado: **90° de avanço total**, mas magnitude = **1/3 da entrada**

### 9.8.2 — Pontes CA

Similar à ponte de Wheatstone, mas para medir **L** e **C**.

**Condição de equilíbrio:**
```
Z₁ · Zx = Z₂ · Z₃
```
ou
```
Zx = (Z₃/Z₁) · Z₂
```

**Para medir indutância:**
```
Lx = (R₂/R₁) · Ls
```

**Para medir capacitância:**
```
Cx = (R₁/R₂) · Cs
```

> [!TIP]
> O equilíbrio dessas pontes **não depende da frequência** da fonte CA!

---

## 📊 Resumo Rápido — Tabela Mestra

| Conceito | Fórmula |
|----------|---------|
| Senoide | v(t) = Vm cos(ωt + φ) |
| Período | T = 2π/ω |
| Frequência | f = 1/T = ω/(2π) |
| Fasor | V = Vm∠φ |
| Impedância | Z = V/I = R + jX |
| Admitância | Y = 1/Z = G + jB |
| Z do resistor | R |
| Z do indutor | jωL |
| Z do capacitor | 1/(jωC) |
| Série | Zeq = Z₁ + Z₂ + ... |
| Paralelo | 1/Zeq = 1/Z₁ + 1/Z₂ + ... |
| Div. tensão | V₁ = Z₁/(Z₁+Z₂) · V |
| Div. corrente | I₁ = Z₂/(Z₁+Z₂) · I |

---

## ✅ Questões para Revisão (Respostas)

| Questão | Resposta |
|---------|----------|
| 9.1 | **(d)** — A sen(ωt − 90°) não é equivalente a A cos ωt (seria cos(ωt) = sen(ωt + 90°)) |
| 9.2 | **(c)** — periódica |
| 9.3 | **(b)** — 1 kHz (tem período menor que 1 krad/s) |
| 9.4 | **(b) e (d)** — v₂ avançada e v₁ atrasada |
| 9.5 | **(a)** — Verdadeiro |
| 9.6 | **(e)** — reatância |
| 9.7 | **(b)** — Falso (impedância do capacitor DIMINUI com a frequência) |
| 9.8 | **(d)** — ω → ∞ (indutor vira circuito aberto) |
| 9.9 | **(c)** — 13 V (√(12² + 5²) = 13) |
| 9.10 | **(b)** — 30 + j40 Ω |

---

## 🎯 Dicas de Estudo

1. **Domine a conversão seno ↔ cosseno** — é usado em praticamente todos os exercícios
2. **Pratique operações com números complexos** — forma retangular para soma, polar para multiplicação
3. **Memorize as impedâncias dos 3 elementos** — R, jωL, 1/(jωC)
4. **Lembre das relações de fase** — ELI the ICE man
5. **Use a técnica do fasor**: converta para fasores → resolva no domínio da frequência → converta de volta
6. **Divisão de tensão e corrente** funcionam igual ao CC, só que com impedâncias complexas


---

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
