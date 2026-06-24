# Questão de Revisão 7.4
*(Página 265 do PDF)*

> **Objetivo:** Calcular o tempo necessário para um indutor atingir uma porcentagem do seu valor estacionário.
> **Instrução:** Encontre o $	au$ e use a fórmula universal de carga/descarga!

**Enunciado:**
Um circuito RL tem $R = 2 \, \Omega$ e $L = 4 \, \text{H}$. O tempo necessário para a corrente no indutor atingir 40% de seu valor em regime estacionário é:
(a) $0,5 \, \text{s}$
(b) $1 \, \text{s}$
(c) $2 \, \text{s}$
(d) $4 \, \text{s}$
(e) nenhuma das anteriores

---

## ✅ Solução Correta: Letra (b)

O primeiro passo é encontrar a Constante de Tempo do circuito RL:
$$ \tau = \frac{L}{R} = \frac{4 \, \text{H}}{2 \, \Omega} = 2 \, \text{s} $$

Como a corrente parte do zero e vai subindo (carregando), usamos a equação de resposta ao degrau:
$$ i(t) = i(\infty) \cdot [1 - e^{-t/\tau}] $$

O enunciado diz que a corrente $i(t)$ atinge **40%** do valor final $i(\infty)$. Então podemos substituir $i(t)$ por $0,4 \cdot i(\infty)$:
$$ 0,4 \cdot i(\infty) = i(\infty) \cdot [1 - e^{-t/2}] $$

Agora começa a álgebra! Podemos cortar o $i(\infty)$ dos dois lados da equação:
$$ 0,4 = 1 - e^{-t/2} $$

Passamos o $1$ para o outro lado:
$$ 0,4 - 1 = - e^{-t/2} $$
$$ -0,6 = - e^{-t/2} $$
$$ 0,6 = e^{-t/2} $$

Para "descer" o $t$ que está preso lá no expoente, aplicamos o Logaritmo Natural ($\ln$) dos dois lados:
$$ \ln(0,6) = \ln(e^{-t/2}) $$
$$ -0,5108 = -\frac{t}{2} $$

Multiplicando os dois lados por $-2$:
$$ t = 2 \times 0,5108 $$
$$ t = 1,0216 \, \text{segundos} \approx \mathbf{1 \, \text{s}} $$

A alternativa correta é a **(b)**!
