# 🧠 Resumo Básico: Capacitores e Indutores

Nós passamos a vida toda trabalhando com o **Resistor**, que é um cara simples: ele pega energia elétrica e transforma em calor (ele dissipa). 

Agora entram dois novos personagens que não dissipam energia, eles **guardam** a energia e devolvem depois: o **Capacitor** e o **Indutor**.

---

### 🔋 1. O Capacitor (C)
Ele armazena energia num **campo elétrico** (basicamente segurando elétrons em duas placas metálicas separadas por um isolante).

- **A fórmula mágica:** A corrente depende da variação da tensão no tempo:
  > `i = C * (dv / dt)`

- **A pegadinha 1 (Regime Permanente):** Se a fonte for uma bateria de CC (tensão cravada, que não muda), a derivada `dv/dt` é zero, logo a corrente é zero. Isso significa que:
  > **Em Corrente Contínua (após um tempo ligado), o capacitor enche e corta a corrente, funcionando como um FIO ROMPIDO (Circuito Aberto).**

- **A pegadinha 2 (Continuidade):** A tensão num capacitor *não pode mudar de uma hora pra outra*. Isso seria como teletransporte. `vc(0-) = vc(0+)`.

---

### 🧲 2. O Indutor (L)
Ele armazena energia num **campo magnético** (é uma bobina de fio enroladinha).

- **A fórmula mágica:** A tensão depende da variação da corrente no tempo:
  > `v = L * (di / dt)`

- **A pegadinha 1 (Regime Permanente):** Se a bateria for CC (corrente não muda), a derivada `di/dt` é zero, logo a tensão é zero. Isso significa que:
  > **Em Corrente Contínua (após um tempo ligado), o indutor vira um FIO LISO SEM RESISTÊNCIA (Curto-Circuito).**

- **A pegadinha 2 (Continuidade):** A corrente num indutor *não pode mudar de uma hora pra outra*. Se você arrancar o fio de um indutor rodando, ele gera uma tensão absurda para tentar manter a corrente. `iL(0-) = iL(0+)`.

---

### 🧩 3. Associações (Série e Paralelo)
Sabe a conta que você faz para Resistor?
- **O Indutor é Maria-vai-com-as-outras:** As fórmulas são IDÊNTICAS ao resistor.
  - `Série:` Soma.
  - `Paralelo:` Produto dividido pela soma.
- **O Capacitor é do contra:** Ele inverte tudo!
  - `Paralelo:` Você simplesmente **soma** os valores (`C_eq = C1 + C2`).
  - `Série:` Você faz a regra do inverso / "produto pela soma".
