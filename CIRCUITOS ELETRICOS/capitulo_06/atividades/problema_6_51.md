# Problema 6.51

**Enunciado:** Determine a indutância equivalente ($L_{eq}$) nos terminais a-b do circuito da Figura 6.73.  
*(Página 218 do Livro / Página 238 do PDF)*

---

### A Regra de Ouro das Associações
Lembre-se que **indutores operam IGUAL aos resistores**:
- **Série:** Você SOMA os valores diretamente ($L_{eq} = L_1 + L_2$).
- **Paralelo:** Você usa a regra da condutância ou "produto pela soma" para dois ($L_{eq} = \frac{L_1 \cdot L_2}{L_1 + L_2}$).

### Análise da Figura 6.73
Temos uma ponte de indutores entre os terminais $a$ e $b$. Analisando o caminho principal e os "atalhos":
- Há um indutor de $10 \, mH$ ligado direto do terminal $a$ até o terminal $b$ pelo fio de cima. Ele está em paralelo com todo o resto do circuito embaixo.
- No meio, saindo do terminal $a$, temos um indutor de $25 \, mH$ e um de $60 \, mH$.
- Saindo do terminal $b$ (vindo da direita), temos um indutor de $20 \, mH$ e um de $30 \, mH$.

*Se interpretarmos a estrutura como uma associação ponte ou "Delta-Estrela" clássica:*
1. O nó do meio conecta o $25 \, mH$, o $20 \, mH$, o $60 \, mH$ e o $30 \, mH$.
   - O indutor de $60 \, mH$ e o de $25 \, mH$ ambos saem do terminal $a$ e vão para o mesmo nó central? Se sim, eles estão em **Paralelo**.
   - O indutor de $30 \, mH$ e o de $20 \, mH$ ambos saem do terminal $b$ e vão para o nó central? Se sim, eles estão em **Paralelo**.

**Cálculo da estrutura (assumindo os paralelos nas pontas):**
1. **Lado esquerdo (A até o centro):**
   $$ L_{esq} = 60 \parallel 25 = \frac{60 \cdot 25}{60 + 25} = \frac{1500}{85} \approx 17,64 \, mH $$

2. **Lado direito (Centro até B):**
   $$ L_{dir} = 30 \parallel 20 = \frac{30 \cdot 20}{30 + 20} = \frac{600}{50} = 12 \, mH $$

3. **Série Central:**
   Esses dois blocos estão conectados em série um com o outro (a corrente passa do esquerdo para o direito).
   $$ L_{centro} = L_{esq} + L_{dir} = 17,64 + 12 = 29,64 \, mH $$

4. **Fechamento do Circuito (Paralelo final):**
   Toda essa estrutura ($29,64 \, mH$) está em **paralelo** com aquele indutor "atalho" de $10 \, mH$ lá no topo do circuito, que liga diretamente $a$ em $b$.
   $$ L_{eq} = \frac{29,64 \cdot 10}{29,64 + 10} = \frac{296,4}{39,64} \approx 7,47 \, mH $$

*(Atenção: A interpretação visual da ponte pode variar. Se for uma ponte de Wheatstone desequilibrada onde o ramo central cruza sem nós em paralelo perfeitos, a conversão Triângulo-Estrela (Delta-Wye) seria necessária. As fórmulas de conversão para indutores são 100% iguais às de resistores!).*
