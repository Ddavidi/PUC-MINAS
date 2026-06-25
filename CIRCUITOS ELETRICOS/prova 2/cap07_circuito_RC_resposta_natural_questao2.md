# Prova 2 — Questão 2
**Capítulo 7 | Tema: Circuito RC de Primeira Ordem — Resposta Natural com Chave**

> **Tipo de Problema:** 🟢 **Resposta Natural** (após $t=0$ não há fonte ativa — o capacitor descarrega sozinho até zero)

> **Enunciado (07 pontos):**
> A chave K₁ no circuito abaixo esteve **fechada por um longo tempo** e é **aberta** em $t=0$.
> Sabendo que $R_1 = 80\text{ k}\Omega$, $R_2 = 20\text{ k}\Omega$, $R_3 = 50\text{ k}\Omega$ e $C_1 = 0,4\text{ μF}$, determine:
> - a) O valor inicial de $v(t)$. (1,5 pontos)
> - b) A constante de tempo do circuito para $t > 0$. (1,5 pontos)
> - c) A expressão numérica para $v_0(t)$, $t \geq 0$. (1,5 pontos)
> - d) A energia inicial armazenada no capacitor. (1,5 pontos)

---

## 🔑 Passo 0: Lendo o circuito e entendendo a chave

Antes de fazer qualquer conta, vamos **entender o que acontece fisicamente**.

![Circuito Original da Questão 2](../../_base_dados_ia/imagens_geradas/prova2_q2_original.png)

**O que temos?**
- Uma **fonte de corrente** $I_1 = 7,5\text{ mA}$ no lado esquerdo.
- Um resistor $R_1 = 80\text{ k}\Omega$ **em paralelo** com a fonte (observe que os dois estão conectados entre os mesmos dois nós: o fio de cima e o fio de baixo).
- Um resistor $R_2 = 20\text{ k}\Omega$ **em série** com a chave $K_1$.
- Após a chave, temos um **capacitor** $C_1 = 0,4\text{ μF}$ e um resistor $R_3 = 50\text{ k}\Omega$ **em paralelo** (ambos ligados do nó B ao terra).

**O que a chave faz?**
- **$t < 0$ (chave FECHADA):** Tudo está conectado. A fonte alimenta o circuito inteiro e o capacitor teve tempo de "encher" até um valor estável.
- **$t > 0$ (chave ABERTA):** A chave corta o fio entre $R_2$ e o nó B. A fonte e $R_1$ ficam **completamente isolados** do lado direito. O capacitor fica **sozinho** com $R_3$ e descarrega.

> 💡 **Insight:** Quando a chave **abre**, ela "amputa" uma parte do circuito. É como cortar um cano de água — a parte que ficou desconectada da torneira vai esvaziando sozinha.

---

## ✅ Parte (a): Valor inicial $v(0)$ — Quanto o capacitor "encheu"?

### Raciocínio: O que acontece em $t < 0$?

A chave esteve fechada "por um longo tempo". Isso é a frase mágica que significa **regime permanente de CC** (Corrente Contínua). Nessa situação:

> **Regra de ouro:** Em CC permanente, o **capacitor se comporta como circuito ABERTO** (não passa corrente por ele, pois já carregou totalmente).

Então, para analisar $t < 0$, **removemos o capacitor** do circuito e o substituímos por um espaço vazio (circuito aberto):

![Circuito em t < 0 — Capacitor Aberto](../../_base_dados_ia/imagens_geradas/prova2_q2_t_menor_0.png)

### Passo a passo da análise nodal

Com o capacitor aberto, a corrente que sai da fonte tem apenas dois caminhos: descer por $R_1$ ou ir por $R_2 → R_3$.

Vou chamar os nós de **Nó A** (entre $R_1$ e $R_2$) e **Nó B** (entre $R_2$, $C_1$ e $R_3$).

**Passo 1 — LKC no Nó B:**
Como o capacitor está aberto, **nenhuma corrente entra nele**. Toda corrente que chega por $R_2$ desce por $R_3$:
$$i_{R_2} = i_{R_3}$$
$$\frac{V_A - V_B}{R_2} = \frac{V_B - 0}{R_3}$$
$$\frac{V_A - V_B}{20\text{k}} = \frac{V_B}{50\text{k}}$$

Multiplicando tudo por $100\text{k}$ para limpar as frações:
$$5(V_A - V_B) = 2V_B$$
$$5V_A - 5V_B = 2V_B$$
$$5V_A = 7V_B$$
$$V_A = \frac{7}{5} V_B = 1,4\,V_B \quad \text{...(Eq. 1)}$$

**Passo 2 — LKC no Nó A:**
A corrente que sai da fonte ($7,5\text{ mA}$) se divide: uma parte desce por $R_1$ e outra vai por $R_2$:
$$I_1 = \frac{V_A}{R_1} + \frac{V_A - V_B}{R_2}$$
$$7,5 \times 10^{-3} = \frac{V_A}{80\text{k}} + \frac{V_A - V_B}{20\text{k}}$$

**Passo 3 — Substituindo a Eq. 1** ($V_A = 1,4\,V_B$):
$$7,5 \times 10^{-3} = \frac{1,4\,V_B}{80\,000} + \frac{1,4\,V_B - V_B}{20\,000}$$
$$7,5 \times 10^{-3} = \frac{1,4\,V_B}{80\,000} + \frac{0,4\,V_B}{20\,000}$$
$$7,5 \times 10^{-3} = V_B \times \left(\frac{1,4}{80\,000} + \frac{0,4}{20\,000}\right)$$
$$7,5 \times 10^{-3} = V_B \times (1,75 \times 10^{-5} + 2,0 \times 10^{-5})$$
$$7,5 \times 10^{-3} = V_B \times 3,75 \times 10^{-5}$$

$$V_B = \frac{7,5 \times 10^{-3}}{3,75 \times 10^{-5}} = \mathbf{200\text{ V}}$$

**Passo 4 — Conclusão:**
A tensão no Nó B é a tensão sobre o capacitor (e sobre $R_3$). Como o capacitor estava em paralelo com $R_3$:
$$v(0^-) = V_B = 200\text{ V}$$

Pela **continuidade da tensão no capacitor** (a tensão de um capacitor **nunca** pula instantaneamente):
$$\boxed{v(0) = v(0^+) = v(0^-) = 200\text{ V}}$$

> ✅ **Verificação da LKC:**
> - $V_A = 1,4 \times 200 = 280\text{ V}$
> - $i_{R_1} = 280/80\text{k} = 3,5\text{ mA}$ (desce por $R_1$)
> - $i_{R_2} = (280-200)/20\text{k} = 80/20\text{k} = 4,0\text{ mA}$ (vai para a direita)
> - $i_{R_3} = 200/50\text{k} = 4,0\text{ mA}$ (desce por $R_3$)
> - LKC no Nó A: $3,5 + 4,0 = 7,5\text{ mA}$ ✅ Bate com a fonte!

---

## ✅ Parte (b): Constante de tempo $\tau$ para $t > 0$

### Raciocínio: O que acontece em $t > 0$?

Quando K₁ abre, o circuito **se parte em dois pedaços**:
- **Lado esquerdo** (fonte + $R_1$ + $R_2$): isolado, irrelevante.
- **Lado direito** ($C_1$ + $R_3$): o capacitor carregado com 200 V descarrega através de $R_3$.

![Circuito em t > 0 — Descarga livre](../../_base_dados_ia/imagens_geradas/prova2_q2_t_maior_0.png)

O capacitor vê apenas um resistor: $R_3$. Não há paralelo nem série — é direto!

$$R_{eq} = R_3 = 50\text{ k}\Omega = 50\,000\,\Omega$$

$$\boxed{\tau = R_{eq} \cdot C_1 = 50\,000 \times 0,4 \times 10^{-6} = 0,02\text{ s} = 20\text{ ms}}$$

> 💡 **O que $\tau = 20\text{ ms}$ significa na prática?** Após 20 ms, a tensão no capacitor cai para 37% do valor inicial (de 200 V para ~74 V). Após $5\tau = 100\text{ ms}$, a tensão é praticamente zero.

---

## ✅ Parte (c): Expressão de $v_0(t)$

### Raciocínio: Qual fórmula usar?

Como **não há fonte ativa** após $t > 0$ (a fonte ficou isolada do outro lado da chave), este é um caso de **Resposta Natural pura**. O capacitor simplesmente descarrega exponencialmente até zero:

$$v_0(t) = v(0) \cdot e^{-t/\tau}$$

Calculando $1/\tau$:
$$\frac{1}{\tau} = \frac{1}{0,02} = 50$$

Substituindo os valores:

$$\boxed{v_0(t) = 200\,e^{-50t}\text{ V}, \quad t \geq 0}$$

> 💡 **Conferindo nos extremos:**
> - Em $t = 0$: $v_0(0) = 200 \cdot e^{0} = 200\text{ V}$ ✅ (bate com a condição inicial)
> - Em $t \to \infty$: $v_0 \to 200 \cdot 0 = 0\text{ V}$ ✅ (capacitor descarregou totalmente)

---

## ✅ Parte (d): Energia inicial armazenada no capacitor

### Raciocínio: A fórmula da energia

A energia armazenada num capacitor é análoga à energia potencial elástica de uma mola ($\frac{1}{2}kx^2$). Aqui, a "rigidez" é a capacitância e o "deslocamento" é a tensão:

$$w_C = \frac{1}{2} C \cdot v^2$$

Substituindo com os valores iniciais ($v(0) = 200\text{ V}$):

$$w_C(0) = \frac{1}{2} \times 0,4 \times 10^{-6} \times (200)^2$$
$$w_C(0) = \frac{1}{2} \times 0,4 \times 10^{-6} \times 40\,000$$
$$w_C(0) = 0,2 \times 10^{-6} \times 40\,000$$

$$\boxed{w_C(0) = 8 \times 10^{-3}\text{ J} = 8\text{ mJ}}$$

> 💡 Essa energia toda vai ser dissipada (transformada em calor) no resistor $R_3$ durante a descarga.

---

> [!TIP]
> **Receita de Bolo: Circuito RC — Resposta Natural com Chave**
> 1. **Análise em $t < 0$ (regime permanente CC):** Substitua o capacitor por circuito ABERTO. Resolva o circuito normalmente (LKC/LKT) para achar a tensão $v(0^-)$ sobre o capacitor.
> 2. **Continuidade:** Use $v(0^+) = v(0^-)$ (a tensão de um capacitor nunca salta).
> 3. **Redesenhe para $t > 0$:** Abra a chave e veja o que sobrou. Identifique o $R_{eq}$ que o capacitor "enxerga".
> 4. **Constante de Tempo:** $\tau = R_{eq} \cdot C$.
> 5. **Equação Final:** $v(t) = v(0) \cdot e^{-t/\tau}$ (resposta natural pura, vai a zero).
> 6. **Energia Inicial:** $w_C(0) = \frac{1}{2}Cv(0)^2$.
