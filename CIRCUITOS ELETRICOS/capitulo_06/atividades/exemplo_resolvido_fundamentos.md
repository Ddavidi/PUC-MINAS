# Exemplo Resolvido: Fundamentos de Derivadas (Capacitores e Indutores)

Este é um problema essencial que não estava na nossa lista! Além de saber como eles se comportam em Corrente Contínua (CC) e como fazer associações em série/paralelo, a professora **com certeza** pode cobrar as fórmulas fundamentais que envolvem derivadas (taxa de variação no tempo).

**Lembretes Rápidos:**
- Para o **Capacitor**: $i = C \frac{dv}{dt}$ (A corrente depende da variação da tensão)
- Para o **Indutor**: $v = L \frac{di}{dt}$ (A tensão depende da variação da corrente)
- **Energia no Capacitor**: $W_C = \frac{1}{2} C v^2$
- **Energia no Indutor**: $W_L = \frac{1}{2} L i^2$

---

### Parte 1: O Capacitor

**Enunciado:** A tensão sobre um capacitor de $C = 5 \, \mu F$ é dada por $v(t) = 10 \cos(6000t) \, V$. 
1. Calcule a corrente $i(t)$ que flui pelo capacitor.
2. Determine a corrente em $t = 0$.

**Resolução:**
Sabemos que a fórmula fundamental é:
$$ i(t) = C \frac{dv(t)}{dt} $$

Primeiro, vamos derivar a tensão $v(t)$:
$$ \frac{dv}{dt} = \frac{d}{dt} [10 \cos(6000t)] $$
Usando a regra da cadeia (a derivada do cosseno é o menos seno, multiplicado pela derivada do "miolo"):
$$ \frac{dv}{dt} = 10 \cdot (-6000) \cdot \sin(6000t) = -60000 \sin(6000t) $$

Agora, multiplicamos pelo valor da capacitância $C = 5 \, \mu F = 5 \cdot 10^{-6} \, F$:
$$ i(t) = (5 \cdot 10^{-6}) \cdot (-60000 \sin(6000t)) $$
$$ i(t) = -0,3 \sin(6000t) \, A $$

Para calcular a corrente em $t = 0$:
$$ i(0) = -0,3 \sin(0) = 0 \, A $$

---

### Parte 2: O Indutor

**Enunciado:** A corrente em um indutor de $L = 10 \, mH$ é dada por $i(t) = 2 \sin(100t) \, A$. 
1. Calcule a tensão $v(t)$ sobre o indutor.
2. Calcule a energia armazenada no indutor no instante $t = \frac{\pi}{200} \, s$.

**Resolução (Tensão):**
A fórmula fundamental do indutor é:
$$ v(t) = L \frac{di(t)}{dt} $$

Primeiro, vamos derivar a corrente $i(t)$:
$$ \frac{di}{dt} = \frac{d}{dt} [2 \sin(100t)] $$
Usando a regra da cadeia (a derivada do seno é o cosseno, multiplicado pela derivada do "miolo"):
$$ \frac{di}{dt} = 2 \cdot (100) \cdot \cos(100t) = 200 \cos(100t) $$

Multiplicando pela indutância $L = 10 \, mH = 10 \cdot 10^{-3} \, H = 0,01 \, H$:
$$ v(t) = 0,01 \cdot 200 \cos(100t) $$
$$ v(t) = 2 \cos(100t) \, V $$

**Resolução (Energia):**
Para calcular a energia $W_L = \frac{1}{2} L i^2$, precisamos saber o valor da corrente no instante exato $t = \frac{\pi}{200}$.
Substituindo o tempo na fórmula da corrente:
$$ i\left(\frac{\pi}{200}\right) = 2 \sin\left(100 \cdot \frac{\pi}{200}\right) $$
$$ i\left(\frac{\pi}{200}\right) = 2 \sin\left(\frac{\pi}{2}\right) $$
Como o $\sin(\frac{\pi}{2}) = 1$ (lembrando que $\frac{\pi}{2}$ radianos = 90º):
$$ i = 2 \cdot 1 = 2 \, A $$

Agora aplicamos na fórmula da energia:
$$ W_L = \frac{1}{2} \cdot (0,01) \cdot (2)^2 $$
$$ W_L = \frac{1}{2} \cdot 0,01 \cdot 4 $$
$$ W_L = 0,02 \, Joules \, (ou \, 20 \, mJ) $$

---
> **Resumo da Ópera:** Questões que te dão uma equação com "seno", "cosseno" ou $e^{-t}$ no Capítulo 6 geralmente não exigem análise de malhas complexas, exigem apenas que você saiba **derivar/integrar** aplicando a fórmula fundamental do componente!
