# Problema 6.46

**Enunciado:** Determine $v_C$, $i_L$ e a energia armazenada no capacitor e no indutor no circuito da Figura 6.69 em condições de CC (Corrente Contínua).  
*(Página 218 do Livro / Página 238 do PDF)*

---

### 1. Simplificando o Circuito para o Regime CC
A regra de ouro diz que depois de muito tempo sob corrente contínua:
- O **Capacitor ($2 \, F$)** está totalmente carregado e bloqueia a passagem de corrente $\implies$ **Circuito Aberto** (fio rompido).
- O **Indutor ($0,5 \, H$)** não sofre mais variação de corrente e não se opõe a nada $\implies$ **Curto-Circuito** (um fio liso sem resistência).

Com isso, vamos desenhar o circuito mentalmente:
1. No lado esquerdo, temos uma fonte de corrente de $3 \, A$ subindo em paralelo com um resistor de $4 \, \Omega$. 
   *💡 **Dica (Transformação de Fonte):** Podemos converter essa fonte de corrente + resistor em paralelo para uma fonte de Tensão + resistor em série para facilitar os cálculos.*
   $$ V = 3 \, A \cdot 4 \, \Omega = 12 \, V $$
   *(A fonte de $12 \, V$ fica em série com o resistor de $4 \, \Omega$).*

2. Seguindo o circuito para a direita, temos um resistor de $2 \, \Omega$ em série.
3. Depois, o circuito se divide:
   - Um ramo desce com o capacitor (Aberto). **Nenhuma corrente flui por aqui.** A tensão $v_C$ será apenas a tensão no nó de cima (Nó B) em relação ao terra.
   - O outro ramo desce com o Indutor (fio liso) em série com o resistor de $5 \, \Omega$. Então, a corrente que chega do lado esquerdo vai TODA para esse resistor de $5 \, \Omega$.

### 2. Calculando a Corrente Total ($i_L$)
O circuito real (fechado) que sobra é uma malha simples de série pura:
- A fonte virtual de $12 \, V$.
- O resistor transformado de $4 \, \Omega$.
- O resistor existente de $2 \, \Omega$.
- O resistor final de $5 \, \Omega$ (cujo ramo tinha o indutor).

A resistência total da série é:
$$ R_{eq} = 4 + 2 + 5 = 11 \, \Omega $$

A corrente que flui por essa malha única é a própria corrente do indutor $i_L$ (já que toda a corrente passa por ele antes de passar pelo $5 \, \Omega$):
$$ i_L = \frac{V}{R_{eq}} = \frac{12}{11} \approx 1,09 \, A $$

### 3. Calculando a Tensão no Capacitor ($v_C$)
O capacitor está ligado em paralelo com o ramo do Indutor+Resistor de $5 \, \Omega$.
Como o indutor virou um fio liso (queda de tensão = $0$), a tensão sobre o capacitor $v_C$ é exatamente igual à tensão sobre o resistor de $5 \, \Omega$.
Pela Lei de Ohm:
$$ v_C = R \cdot i_L = 5 \cdot \left(\frac{12}{11}\right) = \frac{60}{11} \approx 5,45 \, V $$

### 4. Calculando a Energia Armazenada
Com $v_C$ e $i_L$ em mãos, usamos as fórmulas de energia ($W$):

#### Energia no Capacitor ($W_C$)
$$ W_C = \frac{1}{2} C \cdot v_C^2 $$
$$ W_C = \frac{1}{2} (2) \cdot \left(\frac{60}{11}\right)^2 = 1 \cdot \frac{3600}{121} \approx 29,75 \, J $$

#### Energia no Indutor ($W_L$)
$$ W_L = \frac{1}{2} L \cdot i_L^2 $$
$$ W_L = \frac{1}{2} (0,5) \cdot \left(\frac{12}{11}\right)^2 = 0,25 \cdot \frac{144}{121} = \frac{36}{121} \approx 0,297 \, J $$

---
**Resumo dos Resultados:**
- Corrente no indutor: **$1,09 \, A$** ($12/11 \, A$)
- Tensão no capacitor: **$5,45 \, V$** ($60/11 \, V$)
- Energia no capacitor: **$29,75 \, J$**
- Energia no indutor: **$0,297 \, J$**
