# Problema 7.11

> **Objetivo:** Resolver o problema passo a passo.
> **Instrução:** Leia o enunciado abaixo e tente resolver usando a metodologia.

**Enunciado:**
Para o circuito na figura abaixo, determine $i_o(t)$ para $t > 0$.

![Circuito Problema 7.11](../../_base_dados_ia/imagens_geradas/problema_7_11.png)

---

> [!TIP]
> **Receita de Bolo: Análise de Circuitos de Primeira Ordem (RL)**
> 1. **Análise em t < 0:** O Indutor se comporta como um **Curto-Circuito** em regime de Corrente Contínua (CC). Calcule a corrente inicial do indutor $i_L(0)$.
> 2. **Análise em t > 0:** Redesenhe o circuito com a nova posição da chave. Encontre a resistência equivalente $R_{eq}$ vista pelo indutor.
> 3. **Constante de Tempo ($\tau$):** Para circuitos RL, a fórmula muda! Use $\tau = \frac{L}{R_{eq}}$.
> 4. **Equação Final:** Use a fórmula natural $i(t) = i_L(0)e^{-t/\tau}$. Lembre-se que essa é a corrente **DO INDUTOR**. Se o problema pedir outra corrente ($i_o$), você precisa relacionar ela com a do indutor.

## ✍️ Sua Vez!

### Passo 1: O cálculo de $i(0)$ (Para $t < 0$)
Antes do tempo zero, a chave estava **fechada**, deixando a corrente da fonte fluir livremente. O Indutor, por estar muito tempo em corrente contínua, virou um fio liso (curto-circuito).

Veja a topologia em $t < 0$:
![Circuito em t < 0](../../_base_dados_ia/imagens_geradas/problema_7_11_v0.png)

Como o Indutor é um fio liso contínuo unindo a parte de cima, os resistores de $4\text{k}\Omega$ (vertical) e $8\text{k}\Omega$ ficaram em **paralelo**. A corrente sai da fonte, passa pelo resistor horizontal de $4\text{k}\Omega$, e então se divide entre o de 4 vertical e o de 8 vertical.

Nesta etapa o seu objetivo é: descobrir a **corrente total** que sai da fonte e aplicar o **Divisor de Corrente** para achar a corrente $i_o(0)$ (que passa no resistor de 8 e, consequentemente, é a mesma que passou pelo indutor).

> [!NOTE]
> **Fórmula do Divisor de Corrente**
> Quando você tem dois resistores em paralelo ($R_A$ e $R_B$) dividindo uma corrente total $I_{total}$, a corrente que vai para um dos resistores é calculada multiplicando a Corrente Total pela fração que tem o **OUTRO** resistor no numerador:
> $$I_x = I_{total} \cdot \left(\frac{R_{oposto}}{R_x + R_{oposto}}\right)$$
>
> Para este circuito (onde a corrente $i_o$ passa no resistor de $8\Omega$ e o oposto é o de $4\Omega$):
> $$i_o(0) = I_{total} \cdot \left(\frac{4}{8 + 4}\right)$$

Para resolver, siga o roteiro:
1. Calcule o $R_{eq}$ do paralelo (entre 4 e 8).
2. Some com o resistor de 4 que está em série para achar a $R_{Total}$.
3. Descubra a $I_{total}$ saindo da fonte usando a Lei de Ohm ($I = V/R_{Total}$).
4. Jogue a $I_{total}$ na fórmula do Divisor de Corrente acima para achar $i_o(0)$.

Faça essa continha e me mande qual é a corrente inicial do indutor!
