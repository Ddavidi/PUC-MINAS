# Problema 6.13

**Enunciado:** Determine a tensão nos capacitores do circuito da Figura 6.49 em CC (Corrente Contínua).

---

### 1. Entendendo o Comportamento em CC
A regra de ouro deste capítulo diz que:
> **Em Corrente Contínua (regime permanente), o capacitor funciona como um circuito aberto (um fio rompido).**

Neste circuito (Figura 6.49), temos dois capacitores ($C_1$ e $C_2$). Ao substituí-los por circuitos abertos, a corrente **não pode** passar pelos ramos onde eles estão.

### 2. Análise do Circuito Equivalente
Se removermos os capacitores (deixando os terminais abertos), o circuito simplifica drasticamente:

1. **O Ramo da Direita ($C_2$):** O capacitor $C_2$ está no ramo mais à direita, em série com o resistor de $50 \, \Omega$. Como o circuito ali está aberto, **nenhuma corrente flui pelo resistor de $50 \, \Omega$**. A queda de tensão nele é $0$ V.
2. **O Ramo da Esquerda ($C_1$):** O capacitor $C_1$ está em paralelo com um resistor de $40 \, \Omega$. A corrente simplesmente ignorará o caminho do capacitor e passará toda pelo resistor de $40 \, \Omega$.

Portanto, o circuito fechado real pelo qual a corrente flui consiste apenas de um *loop* (malha) contendo:
- A fonte de $60$ V (no ramo central)
- O resistor de $20 \, \Omega$ (no ramo central)
- O resistor de $10 \, \Omega$ (no ramo superior)
- O resistor de $40 \, \Omega$ (no ramo da esquerda)

### 3. Calculando a Corrente da Malha
A resistência equivalente ($R_{eq}$) dessa malha única é a soma dos resistores em série:
$$ R_{eq} = 20 + 10 + 40 = 70 \, \Omega $$

A corrente ($I$) que sai da fonte de $60$ V é:
$$ I = \frac{V}{R_{eq}} = \frac{60}{70} = \frac{6}{7} \, A \approx 0,857 \, A $$

### 4. Calculando as Tensões nos Capacitores

#### Tensão em $C_1$ ($v_1$)
O capacitor $C_1$ está em paralelo com o resistor de $40 \, \Omega$. Portanto, a tensão $v_1$ é exatamente a mesma tensão sobre esse resistor.
Pela Lei de Ohm:
$$ v_1 = R \cdot I = 40 \cdot \left(\frac{6}{7}\right) = \frac{240}{7} \, V \approx 34,28 \, V $$

#### Tensão em $C_2$ ($v_2$)
A tensão $v_2$ é a diferença de potencial do nó superior direito para o terra. 
Como não há corrente passando pelo resistor de $50 \, \Omega$, não há queda de tensão nele. Logo, a tensão no nó superior direito é a mesma do nó central (acima do resistor de $20 \, \Omega$).

Podemos calcular a tensão neste nó central ($V_{central}$) de duas formas:
1. Olhando para o ramo da esquerda: A tensão é a soma das quedas nos resistores de $10 \, \Omega$ e $40 \, \Omega$.
   $$ V_{central} = I \cdot (10 + 40) = \left(\frac{6}{7}\right) \cdot 50 = \frac{300}{7} \, V $$
2. Olhando para o ramo da fonte: É a tensão da fonte menos a queda no resistor de $20 \, \Omega$.
   $$ V_{central} = 60 - I \cdot 20 = 60 - \left(\frac{6}{7}\right) \cdot 20 = 60 - \frac{120}{7} = \frac{420 - 120}{7} = \frac{300}{7} \, V $$

Assim, a tensão no capacitor $C_2$ é:
$$ v_2 = \frac{300}{7} \, V \approx 42,85 \, V $$

---
**Resposta Final:**
- $v_1 \approx 34,28 \, V$
- $v_2 \approx 42,85 \, V$
