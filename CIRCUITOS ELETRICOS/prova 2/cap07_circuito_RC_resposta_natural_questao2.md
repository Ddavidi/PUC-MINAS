# Prova 2 — Questão 2
**Capítulo 7 | Tema: Circuito RC de Primeira Ordem — Resposta Natural com Chave**

> **Enunciado (07 pontos):**
> A chave K₁ no circuito abaixo esteve **fechada por um longo tempo** e é **aberta** em $t=0$.
> Sabendo que $R_1 = 80\text{ k}\Omega$, $R_2 = 20\text{ k}\Omega$, $R_3 = 50\text{ k}\Omega$ e $C_1 = 0,4\text{ μF}$, determine:
> - a) O valor inicial de $v(t)$. (1,5 pontos)
> - b) A constante de tempo do circuito para $t > 0$. (1,5 pontos)
> - c) A expressão numérica para $v_0(t)$, $t \geq 0$. (1,5 pontos)
> - d) A energia inicial armazenada no capacitor. (1,5 pontos)

---

## 🔑 Passo 0: Entendendo o circuito

O truque aqui é o inverso da Questão 1:
- **Antes de abrir (t < 0):** K₁ **fechada**, todo o circuito está ativo. A fonte de corrente $I_1$ alimenta $R_1$ (em paralelo) e passa por $R_2$ + $R_3$ para carregar o capacitor.
- **Depois de abrir (t > 0):** K₁ **abre**, desconectando a fonte e $R_2$ do restante. O capacitor **descarrega sozinho** através de $R_3$.

---

## ✅ Parte (a): Valor inicial $v(0)$

**Estado $t < 0$ — Chave Fechada:**

![Circuito com chave fechada (t < 0)](../../_base_dados_ia/imagens_geradas/prova2_q2_circuito_t_antes.png)

Em regime permanente de CC, o **capacitor se comporta como circuito aberto** — não passa corrente por ele. Toda a corrente que passa por $R_2$ desce pelo $R_3$.

Aplicamos a LKC no Nó superior esquerdo:
$$I_1 = \frac{V_A}{R_1} + \frac{V_A - V_B}{R_2}$$

No Nó direito (com C aberto, $I_{R2} = I_{R3}$):
$$\frac{V_A - V_B}{R_2} = \frac{V_B}{R_3} \implies V_A = V_B\left(1 + \frac{R_2}{R_3}\right) = V_B\left(1 + \frac{20}{50}\right) = 1,4\,V_B$$

Substituindo na LKC:
$$7,5 \times 10^{-3} = \frac{1,4\,V_B}{80\,000} + \frac{0,4\,V_B}{20\,000}$$
$$7,5 \times 10^{-3} = V_B\left(\frac{1,4}{80\,000} + \frac{0,4}{20\,000}\right) = V_B \times 3,75 \times 10^{-5}$$

$$v(0^-) = V_B = \frac{7,5 \times 10^{-3}}{3,75 \times 10^{-5}} = \mathbf{200\text{ V}}$$

Pela continuidade da tensão no capacitor: $v(0^+) = v(0^-) = \mathbf{200\text{ V}}$

> ✅ **Verificação:** $V_A = 1,4 \times 200 = 280\text{ V}$; $I_{R1} = 280/80\text{k} = 3,5\text{ mA}$; $I_{R2} = 80/20\text{k} = 4\text{ mA}$; $I_{R3} = 200/50\text{k} = 4\text{ mA}$; KCL: $3,5 + 4 = 7,5\text{ mA}$ ✅

---

## ✅ Parte (b): Constante de tempo $\tau$ para $t > 0$

**Estado $t > 0$ — Chave Aberta:**

![Circuito com chave aberta — descarga (t > 0)](../../_base_dados_ia/imagens_geradas/prova2_q2_circuito_t_depois.png)

Com K₁ aberta, o capacitor fica isolado com apenas $R_3$:

$$R_{eq} = R_3 = 50\text{ k}\Omega$$

$$\boxed{\tau = R_{eq} \cdot C_1 = 50\,000 \times 0,4 \times 10^{-6} = 20\text{ ms} = 0,02\text{ s}}$$

---

## ✅ Parte (c): Expressão de $v_0(t)$

Sem fonte ativa, é **Resposta Natural (descarga pura)** do capacitor:

$$v_0(t) = v(0) \cdot e^{-t/\tau}$$

$$\boxed{v_0(t) = 200\,e^{-50t}\text{ V}, \quad t \geq 0}$$

---

## ✅ Parte (d): Energia inicial armazenada no capacitor

$$w_C(0) = \frac{1}{2} C_1 \cdot [v(0)]^2 = \frac{1}{2} \times 0,4 \times 10^{-6} \times (200)^2$$

$$w_C(0) = \frac{1}{2} \times 0,4 \times 10^{-6} \times 40\,000$$

$$\boxed{w_C(0) = 8\text{ mJ}}$$
