# Problema 11.46

**Enunciado:** Para os fasores de tensão e corrente a seguir, calcule a potência complexa, a potência aparente, a potência real e a potência reativa. Especifique se o Fator de Potência (FP) está adiantado ou atrasado.  
*(Página 459 do PDF)*

---

### Resumo das Fórmulas Utilizadas
Quando a tensão $\mathbf{V}$ e a corrente $\mathbf{I}$ são dadas em valores **RMS** (Eficazes):
- **Potência Complexa ($\mathbf{S}$):** $\mathbf{S} = \mathbf{V} \cdot \mathbf{I}^*$ *(onde $\mathbf{I}^*$ é o complexo conjugado da corrente).*
- **Potência Aparente ($S$):** É o módulo da potência complexa, $S = |\mathbf{S}|$ em **VA**.
- **Potência Real/Ativa ($P$):** É a parte real da potência complexa, $P = \operatorname{Re}(\mathbf{S}) = S \cos(\theta)$ em **W**.
- **Potência Reativa ($Q$):** É a parte imaginária da potência complexa, $Q = \operatorname{Im}(\mathbf{S}) = S \sin(\theta)$ em **VAR**.
- **Fator de Potência (FP):** Determinado pelo sinal de $Q$ (ou pela diferença de ângulo $\theta = \theta_v - \theta_i$). 
  - Se $Q < 0$ (corrente está à frente da tensão), o FP é **adiantado** (capacitivo).
  - Se $Q > 0$ (corrente está atrás da tensão), o FP é **atrasado** (indutivo).

---

### Caso (a)
$\mathbf{V} = 220 \angle 30^\circ \, \text{V RMS}$  
$\mathbf{I} = 0,5 \angle 60^\circ \, \text{A RMS}$

1. **Conjugado da corrente:** $\mathbf{I}^* = 0,5 \angle -60^\circ \, \text{A}$
2. **Potência Complexa:** $\mathbf{S} = (220 \angle 30^\circ) \cdot (0,5 \angle -60^\circ) = 110 \angle -30^\circ \, \text{VA}$
3. **Potência Aparente:** $S = 110 \, \text{VA}$
4. **Potência Real:** $P = 110 \cos(-30^\circ) = 110 \cdot \frac{\sqrt{3}}{2} \approx 95,26 \, \text{W}$
5. **Potência Reativa:** $Q = 110 \sin(-30^\circ) = -55 \, \text{VAR}$
6. **Fator de Potência:** Como $Q$ é negativo (a fase da corrente $60^\circ$ é maior que a da tensão $30^\circ$), o FP está **adiantado**.

---

### Caso (b)
$\mathbf{V} = 250 \angle -10^\circ \, \text{V RMS}$  
$\mathbf{I} = 6,2 \angle -25^\circ \, \text{A RMS}$

1. **Conjugado da corrente:** $\mathbf{I}^* = 6,2 \angle +25^\circ \, \text{A}$
2. **Potência Complexa:** $\mathbf{S} = (250 \angle -10^\circ) \cdot (6,2 \angle 25^\circ) = 1550 \angle 15^\circ \, \text{VA}$
3. **Potência Aparente:** $S = 1550 \, \text{VA}$
4. **Potência Real:** $P = 1550 \cos(15^\circ) \approx 1497,2 \, \text{W}$
5. **Potência Reativa:** $Q = 1550 \sin(15^\circ) \approx 401,2 \, \text{VAR}$
6. **Fator de Potência:** Como $Q$ é positivo, o FP está **atrasado**.

---

### Caso (c)
$\mathbf{V} = 120 \angle 0^\circ \, \text{V RMS}$  
$\mathbf{I} = 2,4 \angle -15^\circ \, \text{A RMS}$

1. **Conjugado da corrente:** $\mathbf{I}^* = 2,4 \angle +15^\circ \, \text{A}$
2. **Potência Complexa:** $\mathbf{S} = (120 \angle 0^\circ) \cdot (2,4 \angle 15^\circ) = 288 \angle 15^\circ \, \text{VA}$
3. **Potência Aparente:** $S = 288 \, \text{VA}$
4. **Potência Real:** $P = 288 \cos(15^\circ) \approx 278,2 \, \text{W}$
5. **Potência Reativa:** $Q = 288 \sin(15^\circ) \approx 74,5 \, \text{VAR}$
6. **Fator de Potência:** Como $Q$ é positivo, o FP está **atrasado**.

---

### Caso (d)
$\mathbf{V} = 160 \angle 45^\circ \, \text{V RMS}$  
$\mathbf{I} = 8,5 \angle 90^\circ \, \text{A RMS}$

1. **Conjugado da corrente:** $\mathbf{I}^* = 8,5 \angle -90^\circ \, \text{A}$
2. **Potência Complexa:** $\mathbf{S} = (160 \angle 45^\circ) \cdot (8,5 \angle -90^\circ) = 1360 \angle -45^\circ \, \text{VA}$
3. **Potência Aparente:** $S = 1360 \, \text{VA}$
4. **Potência Real:** $P = 1360 \cos(-45^\circ) = 1360 \cdot \frac{\sqrt{2}}{2} \approx 961,7 \, \text{W}$
5. **Potência Reativa:** $Q = 1360 \sin(-45^\circ) = -1360 \cdot \frac{\sqrt{2}}{2} \approx -961,7 \, \text{VAR}$
6. **Fator de Potência:** Como $Q$ é negativo, o FP está **adiantado**.
