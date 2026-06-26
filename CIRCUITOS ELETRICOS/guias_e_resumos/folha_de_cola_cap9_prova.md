# FOLHA DE COLA: CAPÍTULOS 9 E 11 (FASORES E POTÊNCIA)
*(Focada 100% no padrão da Questão 3 da Prova e na Atividade Avaliativa)*

---

## 1. PREPARAÇÃO E IMPEDÂNCIAS
Se a prova não te der o $\omega$, ache pela frequência ($f$):
$$ \omega = 2\pi f \quad \text{(se } f=60\text{Hz, } \omega \approx 377\text{ rad/s)} $$

**Fórmulas das Impedâncias:**
- **Resistor:** $Z_R = R$ 
- **Indutor:** $Z_L = j\omega L$ 
- **Capacitor:** $Z_C = \frac{-j}{\omega C}$ 
*(Não esqueça o sinal negativo do Capacitor!)*

## 2. CARÁTER DO CIRCUITO (A SOMA DE $Z$)
- Em um circuito série, $Z_{eq} = Z_R + Z_L + Z_C$. O resultado sai no formato $R + jX$ (Retangular).
- **Indutivo:** Se a parte com o $j$ der POSITIVA.
- **Capacitivo:** Se a parte com o $j$ der NEGATIVA.

## 3. AS LEIS MESTRAS
- **Lei de Ohm Fasorial:** $\tilde{V} = Z_{eq} \cdot \tilde{I}$
- **Potência Complexa ($S$):** $S = \tilde{V} \cdot \tilde{I}^*$
  *(Atenção! O asterisco significa INVERTER o sinal do ângulo da Corrente! Ex: se $\tilde{I} = 2 \angle 30^\circ$, use $\tilde{I}^* = 2 \angle -30^\circ$ na conta de $S$).*
- **O que significa o $S = P + jQ$?**
  - **$P$ (Parte Real):** Potência Ativa (Watts)
  - **$Q$ (Parte Imag):** Potência Reativa (VAr)
  - **$|S|$ (Módulo/Polar):** Potência Aparente (VA)

---

## 4. A RECEITA DE BOLO PARA A QUESTÃO DA PROVA
1. **Prepare o terreno ($\omega$ e a Fonte):** 
   - Ache o $\omega = 2\pi f$ (se necessário).
   - **O pulo do gato (Fasor Eficaz - RMS):** Para calcular Potência, usamos o "Valor Eficaz" (RMS). Se a questão te der a equação no tempo (ex: $311 \cos(\dots)$), **divida o 311 por $\sqrt{2}$** para achar o valor Eficaz real (ex: $220$). Transforme em Fasor: $220 \angle \theta^\circ$. Se já der $220 \angle 0^\circ \text{ (rms)}$, sorria e use direto.
   - ⚠️ **E se for SENO?** Fasores SÓ funcionam com Cosseno! Se a professora te der uma onda com "$\sin$" (ex: $311 \sin(377t + 30^\circ)$), você **obrigatoriamente deve subtrair $90^\circ$** do ângulo antes de virar fasor. Ela vira $311 \cos(377t - 60^\circ)$. A partir daí, divida pela $\sqrt{2}$ normalmente.
2. Calcule $Z_R, Z_L$ e $Z_C$.
3. Some tudo para achar o $Z_{eq}$ Retangular e justifique se é Indutivo ou Capacitivo pelo sinal do $j$.
4. Jogue o $Z_{eq}$ na Casio e aperte `FORMAT` para ver o Polar.
5. Calcule a Corrente: divida o fasor da Tensão pelo fasor $Z_{eq}$ polar.
6. Calcule a Potência Complexa ($S = V \cdot I^*$) multiplicando a tensão original pela corrente com o **ângulo invertido**.
7. Anote a resposta da Casio: a parte sem o $i$ é Watts, a parte com o $i$ é VAr.

---

> [!TIP]
> **GUIA DE SOBREVIVÊNCIA - CASIO FX-991LA CW:**
> - **Entrar no modo:** `HOME` $\to$ `Complexo`.
> - **Garantir Graus:** `SETTINGS` $\to$ `Config Calc` $\to$ `Unidade Ângulo` $\to$ `Grau`.
> - **Símbolo de Ângulo ($\angle$):** Pressione `CATALOG` $\to$ `Complexo` $\to$ `$\angle$`.
> - **Colocar o "j":** Aperte `SHIFT` + `0` (botão com $i$ amarelo).
> - **Mudar para Polar ($r\angle\theta$):** Aperte `FORMAT` $\to$ Polar Coord.
> - **Tirar o "x10" de números pequenos:** `SETTINGS` $\to$ `Formato Número` $\to$ `Norm 2`.
