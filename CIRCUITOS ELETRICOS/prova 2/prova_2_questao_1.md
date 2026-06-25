# Prova 2 — Questão 1
**Capítulo 7 | Tema: Circuito RL de Primeira Ordem — Resposta a Degrau com Chave**

> **Enunciado (08 pontos):**
> A chave $K_1$ no circuito abaixo esteve **aberta por um longo tempo** antes de ser fechada em $t=0$.
> Sabendo que $R_1 = 1\,\Omega$, $R_2 = 3\,\Omega$, $L_1 = 80\text{ mH}$ e a fonte $E_1 = 20\text{V}$, determine:
> - a) O valor inicial da corrente $i_0(0)$. (1 ponto)
> - b) A constante de tempo do circuito para $t > 0$. (1,5 pontos)
> - c) A expressão numérica para $i_0(t)$ após a chave ter sido fechada. (2 pontos)
> - d) A expressão numérica para a tensão $v_0(t)$ após a chave ter sido fechada. (2 pontos)
> - e) A energia armazenada no indutor. (1,5 pontos)

---

## 🎂 A "Receita de Bolo" do Circuito RL com Chave

Circuitos de primeira ordem com chave sempre se resolvem em **três fotos de tempo**: o Passado ($t < 0$), o Infinito ($t \to \infty$) e a Transição ($t > 0$). 

### Foto 1: O Passado ($t < 0$) - Achando a Corrente Inicial
Antes da chave fechar, o circuito esteve ligado por muito tempo. 
Regra de Ouro: **Em Corrente Contínua (bateria), depois de muito tempo, o Indutor vira um Fio Liso (Curto-Circuito).**

![Circuito com chave aberta (t < 0)](../_base_dados_ia/imagens_geradas/prova2_q1_circuito_t_antes.png)

Como a chave estava aberta, a corrente tinha que passar por $R_1$ e $R_2$ para completar o caminho.
- Resistência Equivalente (série): $R_{eq} = R_1 + R_2 = 1 + 3 = 4\,\Omega$.
- Corrente de Ohm: $i_0(0^-) = \frac{E_1}{R_{eq}} = \frac{20}{4} = \mathbf{5\text{ A}}$

> 💡 *A principal característica do Indutor é que ele **não aceita mudança brusca de corrente**. Logo, a corrente no milissegundo depois que a chave fecha é a mesma de antes:* **$i_0(0^+) = i_0(0) = 5\text{ A}$**.

### Foto 2: O Infinito ($t \to \infty$) - Achando a Corrente Final
Agora a chave fechou. O que acontece? A chave funciona como um atalho (curto-circuito) perfeito que contorna o $R_2$. A corrente é preguiçosa: em vez de passar pelo resistor $R_2$, ela vai inteira pela chave. **O $R_2$ morre!**

![Circuito com chave fechada (t > 0)](../_base_dados_ia/imagens_geradas/prova2_q1_circuito_t_depois.png)

Deixando o tempo passar até o infinito, o indutor vira fio liso de novo. Mas agora o circuito só tem a fonte e o $R_1$.
- Nova Corrente de Ohm: $i(\infty) = \frac{E_1}{R_1} = \frac{20}{1} = \mathbf{20\text{ A}}$

### Foto 3: A Transição ($t > 0$) - A Constante de Tempo ($\tau$)
Com a chave fechada (e o $R_2$ morto), a resistência que sobrou no circuito é apenas $R_{eq} = 1\,\Omega$.
A constante de tempo ($\tau$) nos diz quão rápido o indutor enche/esvazia:
- $\tau = \frac{L}{R_{eq}} = \frac{80 \times 10^{-3}}{1} = \mathbf{0,08\text{ s}}$

### Passo Final: Montando o Quebra-Cabeças (Equação de $i(t)$)
A fórmula universal para qualquer circuito de 1ª ordem é:
$$ i(t) = i(\infty) + [i(0) - i(\infty)] \cdot e^{-t/\tau} $$

Substituindo os blocos que achamos:
$$ i_0(t) = 20 + [5 - 20] \cdot e^{-t/0,08} $$
Como $1 / 0,08 = 12,5$, a equação fica lindinha assim:
**Letra C:** $\mathbf{i_0(t) = 20 - 15e^{-12,5t} \text{ A}}$

---

## ⚡ Respondendo o Resto da Prova

### Letra D: A Tensão no Indutor $v_0(t)$
Existem dois caminhos: o caminho da Derivada e o Caminho Ninja (Kirchhoff). O Ninja é melhor!
Pela Lei de Kirchhoff das Tensões na malha ligada (K1 fechada): 
A tensão da bateria (20V) é dividida entre o Resistor 1 e o Indutor.
$E_1 = V_{R1} + v_0(t)$
$20 = (R_1 \cdot i_0(t)) + v_0(t)$
$20 = 1 \cdot (20 - 15e^{-12,5t}) + v_0(t)$
$20 = 20 - 15e^{-12,5t} + v_0(t)$
Cortando os 20 de cada lado, a tensão isolada fica:
$\mathbf{v_0(t) = 15e^{-12,5t} \text{ V}}$

### Letra E: Energia Armazenada
A fórmula da energia no campo magnético de um indutor é $W = \frac{1}{2} L i^2$.
Como ele não especificou o tempo, geralmente assumimos a energia inicial no instante da manobra da chave ($t=0$).
$W = \frac{1}{2} \cdot (80 \times 10^{-3}) \cdot (5)^2$
$W = 0,04 \cdot 25 = \mathbf{1\text{ J}}$

---

> [!TIP]
> **Dica de Prova - Casio fx-991LA CW:**
> Para conferir as contas pesadas (como o $\tau$ ou a Energia), você pode usar as memórias (A, B, C...) para guardar os dados e evitar erro de dígito!
> 1. Digite $80 \times 10^{-3}$ e aperte `STO` $\to$ `x` (Guarda o Indutor em x).
> 2. Digite $5$ e aperte `STO` $\to$ `y` (Guarda a Corrente em y).
> 3. Na tela principal, digite: `1/2 × x × y²`.
> 4. Resultado direto: $1$. Muito mais seguro na hora do nervoso!
