# Problema 7.8

> **Objetivo:** Resolver o problema passo a passo.
> **Instrução:** Leia o enunciado abaixo e tente resolver usando a metodologia.

**Enunciado:**
Para o circuito da figura abaixo, considere as equações para o tempo $t > 0$:
$$v(t) = 10 e^{-4t} \, \text{V}$$
$$i(t) = 0,2 e^{-4t} \, \text{A}$$

(a) Determine $R$ e $C$.
(b) Determine a constante de tempo $\tau$.
(c) Calcule a energia inicial no capacitor.
(d) Obtenha o tempo necessário para dissipar 50% da energia inicial.

![Circuito Problema 7.8](../../_base_dados_ia/imagens_geradas/problema_7_8.png)

---

## ✍️ Sua Vez!

Esse problema tem uma "pegada" um pouquinho diferente dos anteriores porque ele já te deu a equação final pronta! Vamos destrinchar ela para descobrirmos os componentes.

### Parte (a) e (b): Determinar $R$, $C$ e a constante de tempo $\tau$
Você matou a charada perfeitamente só de "bater o olho" nas equações!

**Para o $\tau$:**
Comparando a equação do problema com a nossa fórmula geral de descarga $v(t) = v(0)e^{-t/\tau}$:
$$e^{-4t} = e^{-t/\tau} \implies \frac{1}{\tau} = 4 \implies \tau = \frac{1}{4} = \mathbf{0,25 \, \text{s}}$$
*(Isso já resolve a Letra B!)*

**Para o $R$:**
Como você bem notou, as constantes que multiplicam o exponencial são os valores iniciais em $t=0$:
- $v(0) = 10 \, \text{V}$
- $i(0) = 0,2 \, \text{A}$

No circuito, toda a tensão do capacitor cai diretamente no resistor. Como a corrente $i$ flui do capacitor para o resistor, podemos usar a Lei de Ohm ($V = R \cdot i$):
$$10 = R \cdot 0,2$$
$$R = \frac{10}{0,2} = \mathbf{50 \, \Omega}$$

**Para o $C$:**
Sabendo que $\tau = R \cdot C$, é só substituir o que acabamos de descobrir:
$$0,25 = 50 \cdot C$$
$$C = \frac{0,25}{50} = 0,005 \, \text{F} = \mathbf{5 \, \text{mF}}$$

---

### Parte (c): Calcular a energia inicial no capacitor
A energia $w(t)$ armazenada em um capacitor é calculada pela fórmula clássica de energia capacitiva. 
Como o problema pede a energia **inicial**, queremos saber o $w(0)$.

Você lembra qual é a fórmula da energia do capacitor? Calcule o valor dela e me mande aqui!
