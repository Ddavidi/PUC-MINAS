# FOLHA DE COLA: CAPÍTULO 7 (CIRCUITOS DE 1ª ORDEM)
*(Resumo denso projetado para cópia manual em folha de consulta para a prova)*

---

## 1. CONVERSÃO DE UNIDADES (PREFIXOS)
- **Mili (m):** $\times 10^{-3}$  *(Ex: $5\text{ mH} = 5 \times 10^{-3}\text{ H}$)*
- **Micro ($\mu$):** $\times 10^{-6}$ *(Ex: $4\text{ }\mu\text{F} = 4 \times 10^{-6}\text{ F}$)*
- **Nano (n):** $\times 10^{-9}$
- **Pico (p):** $\times 10^{-12}$
- **Kilo (k):** $\times 10^{3}$   *(Ex: $50\text{ k}\Omega = 50 \times 10^3\text{ }\Omega$)*

## 2. REGIME PERMANENTE (CC) - $t<0$ ou $t=\infty$
Após muito tempo na mesma posição (chave estável, o sistema para de mudar):
- **CAPACITOR = Circuito Aberto (Fio Quebrado).** A corrente é zero. Você deve calcular a **Tensão** entre os terminais rompidos para achar $v(0)$ ou $v(\infty)$.
- **INDUTOR = Curto-Circuito (Fio Liso).** A tensão é zero. Você deve calcular a **Corrente** passando por esse fio liso para achar $i(0)$ ou $i(\infty)$.

## 3. FÓRMULAS ESSENCIAIS E PEQUENAS REGRAS
- **Divisor de Tensão (Série):** $V_{alvo} = V_{total} \times \frac{R_{alvo}}{R_{eq\_serie}}$
- **Divisor de Corrente (Paralelo):** $I_{alvo} = I_{total} \times \frac{R_{outro}}{R_{alvo} + R_{outro}}$ *(obs: só vale para 2 resistores dividindo)*
- **LKT (Malhas):** A soma das tensões em um laço fechado é sempre zero. *(Útil para achar $v(t)$ sobre um indutor).*
- **Tensão no Indutor:** $v_L(t) = L \cdot \frac{di}{dt}$ *(Use essa derivada se ele pedir $v_0(t)$ e não $i_0(t)$).*
- **Corrente no Capacitor:** $i_C(t) = C \cdot \frac{dv}{dt}$

---

## 4. A RECEITA DE BOLO UNIVERSAL (PASSOS DA QUESTÃO)
*(Serve para Resposta Natural e Resposta ao Degrau, tanto RC quanto RL).*

### 🔹 Passo 1: O Início ($t < 0$)
- Olhe o circuito *antes* da chave mudar. Ele está em regime permanente.
- Transforme o **Capacitor em Aberto** ou **Indutor em Curto**.
- Descubra a condição inicial: $v_C(0)$ ou $i_L(0)$.
- *Regra:* Tensão no capacitor e Corrente no indutor não dão saltos ($0^- = 0^+$).
- Calcule a **Energia Inicial** se a prova pedir: 
  - $w_C(0) = \frac{1}{2} C \cdot v(0)^2$
  - $w_L(0) = \frac{1}{2} L \cdot i(0)^2$

### 🔹 Passo 2: O Fim ($t \to \infty$)
- Olhe o circuito em sua configuração *depois* da chave abrir/fechar ($t > 0$).
- **Resposta Natural:** Se a fonte sumiu ou foi isolada, toda a energia dissipará e **$x(\infty) = 0$**.
- **Resposta ao Degrau:** Se uma fonte foi ligada/mantida no circuito, ele vai carregar de novo. Use a regra do regime permanente do Passo 1 e ache o novo valor final $v_C(\infty)$ ou $i_L(\infty)$.

### 🔹 Passo 3: O Thevenin e a Constante $\tau$
- Trabalhe apenas com o circuito da direita/restante para $t > 0$.
- Arranque o Indutor/Capacitor e desligue as fontes independentes que sobraram (*Tensão vira Fio Liso, Corrente vira Fio Quebrado*). Ache o $R_{eq}$ "visto" pelos terminais.
- **🚨 Caso Avançado (Fonte Dependente):** Se houver uma fonte com símbolo de losango ($2v_x$, etc), você não pode agrupar os resistores normalmente.
  1. No lugar do Indutor/Capacitor arrancado, ligue uma **Fonte de Teste** ($1V$ ou $1A$).
  2. Ache a corrente $i_o$ (se injetou 1V) ou a tensão $v_o$ (se injetou 1A).
  3. Calcule $R_{eq} = \frac{V_o}{I_o}$.
- Encontre a constante $\tau$:
  - **Para RC:** $\tau = R_{eq} \cdot C$
  - **Para RL:** $\tau = \frac{L}{R_{eq}}$

### 🔹 Passo 4: A Equação Mágica
- Monte a equação de transição para $t > 0$:
$$ x(t) = x(\infty) + [x(0) - x(\infty)] \cdot e^{-\frac{t}{\tau}} $$

### ⚠️ A PEGADINHA FINAL DA PROVA (Cuidado com variáveis soltas)
- A "Equação Mágica" **SÓ FUNCIONA GARANTIDAMENTE** para $v_C(t)$ (no Capacitor) ou $i_L(t)$ (no Indutor).
- Se a prova pedir $v_x(t)$ em um resistor num circuito com Indutor, **NÃO** jogue $v_x$ direto na fórmula mágica!
- **Como resolver:** Faça a Receita de Bolo completa para achar o $i_L(t)$. Então, desenhe o circuito de $t > 0$, coloque a corrente $i_L(t)$ descendo pelo indutor, e aplique as Leis de Kirchhoff (LKT ou LKC) para descobrir quem é $v_x(t)$ em função de $i_L(t)$ (que você já sabe). No Indutor, a tensão é calculada por $v = L \frac{di}{dt}$.
