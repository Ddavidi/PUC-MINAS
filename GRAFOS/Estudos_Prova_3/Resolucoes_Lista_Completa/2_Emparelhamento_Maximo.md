# Resoluções da Lista: Emparelhamento Máximo

Compilação de todas as resoluções das práticas da lista relativas ao tema 2.

---

## 5.2 Prática: Caminhos Aumentantes em Grafo Bipartido

**Enunciado:** Considere o grafo bipartido $G = (U \cup V, E)$, com $M = \{(u_2, v_1)\}$.

![Grafo 5.2](imagens/bipartite_5_2.png)

**a. O que é um caminho alternante e um caminho aumentante?**
- **Caminho alternante:** Caminho cujas arestas alternam entre pertencer a $M$ e não pertencer a $M$.
- **Caminho aumentante:** É um caminho alternante que começa e termina em vértices **livres** (não cobertos por $M$).

**b. M é maximal? Vértices livres:**
$M$ não é maximal, pois podemos adicionar $(u_3, v_2)$ sem conflito.
Vértices livres em $U$: $\{u_1, u_3\}$. Em $V$: $\{v_2, v_3\}$.

**c. Caminho aumentante partindo de $u_1$:**

| Sequência do Caminho | Status da Aresta |
|---|---|
| $u_1 \rightarrow v_1$ | Fora de $M$ (Nova) |
| $v_1 \rightarrow u_2$ | Dentro de $M$ (Existente) |
| $u_2 \rightarrow v_3$ | Fora de $M$ (Nova) |

Como $v_3$ também é livre, temos um caminho aumentante válido.
**Diferença Simétrica ($M \oplus P$):**
> [!NOTE] 
> **Regra de Ouro da Diferença Simétrica:** 
> - Arestas do caminho que estão **Fora** do emparelhamento atual **Entram** (adicionadas).
> - Arestas do caminho que estão **Dentro** do emparelhamento atual **Saem** (removidas).
> *(Isso garante que o emparelhamento sempre cresça em tamanho +1 mantendo a validade, sem vértices com duas arestas).*

- Removemos (Dentro $\rightarrow$ Saem): $(u_2, v_1)$
- Adicionamos (Fora $\rightarrow$ Entram): $(u_1, v_1)$ e $(u_2, v_3)$
*Novo emparelhamento:* $M' = \{(u_1, v_1), (u_2, v_3)\}$.

**d. É um casamento perfeito?**
Ainda não. $u_3$ e $v_2$ continuam livres e existe aresta entre eles. Caminho aumentante trivial: $u_3 \rightarrow v_2$.
*Resultado final:* $M'' = \{(u_1, v_1), (u_2, v_3), (u_3, v_2)\}$. Como cobre todos os 6 vértices, atingimos um casamento perfeito.

**Grafo Final Resultante:**
![Grafo 5.2 Final](imagens/bipartite_5_2_final.png)

---

## 5.3 Prática Hopcroft-Karp 1 (Aumento Simples)

**Enunciado:** $M = \{(A, X), (C, Z)\}$. Encontre vértices livres e um caminho aumentante.

![Grafo 5.3](imagens/bipartite_5_3.png)

**a. Vértices Livres:**
- $B$ e $Y$.

**b. Caminho Aumentante:**
Começa em $B$ e termina em $Y$.
Sequência: $B \rightarrow Z$ (Fora), $Z \rightarrow C$ (Dentro), $C \rightarrow Y$ (Fora).

**c. Diferença Simétrica ($M \oplus P$):**
> [!NOTE] 
> **Regra de Ouro da Diferença Simétrica:** 
> - Arestas do caminho que estão **Fora** do emparelhamento **Entram**.
> - Arestas do caminho que estão **Dentro** do emparelhamento **Saem**.

- Arestas Removidas (Dentro $\rightarrow$ Saem): $(C, Z)$.
- Arestas Adicionadas (Fora $\rightarrow$ Entram): $(B, Z)$ e $(C, Y)$.
*Novo $M'$:* $\{(A, X), (B, Z), (C, Y)\}$.

**Grafo Final Resultante:**
![Grafo 5.3 Final](imagens/bipartite_5_3_final.png)

---

## 5.4 Prática Hopcroft-Karp 2 (Múltiplos Caminhos)

**Enunciado:** $M = \{(A, W), (B, Y)\}$.

![Grafo 5.4](imagens/bipartite_5_4.png)

**a. Vértices livres e Maximalidade:**
Livres: $\{C, D\}$ e $\{X, Z\}$. O emparelhamento não é maximal, pois $D$ e $Z$ possuem aresta direta entre eles.

**b. Caminho Aumentante partindo de C:**
Sequência: $C \rightarrow Y$ (Fora), $Y \rightarrow B$ (Dentro), $B \rightarrow W$ (Fora), $W \rightarrow A$ (Dentro), $A \rightarrow X$ (Fora).
*Diferença Simétrica ($M \oplus P$):* 
> [!NOTE] 
> **Regra de Ouro da Diferença Simétrica:** 
> - Arestas do caminho que estão **Fora** do emparelhamento **Entram**.
> - Arestas do caminho que estão **Dentro** do emparelhamento **Saem**.

- Removemos (Dentro $\rightarrow$ Saem): $(B, Y)$ e $(A, W)$. 
- Inserimos (Fora $\rightarrow$ Entram): $(C, Y), (B, W)$ e $(A, X)$.
*Novo $M_1$:* $\{(C, Y), (B, W), (A, X)\}$.

**c. Caminho aumentante final:**
Restam livres $D$ e $Z$. Caminho aumentante é a aresta direta $D \rightarrow Z$.
*Final $M_{final}$:* $\{(C, Y), (B, W), (A, X), (D, Z)\}$.

**Grafo Final Resultante:**
![Grafo 5.4 Final](imagens/bipartite_5_4_final.png)

---

## 5.5 Prática Hopcroft-Karp 3 (Grafo Denso)

**Enunciado:** $M = \{(U_1, V_2), (U_2, V_1), (U_3, V_4)\}$.

![Grafo 5.5](imagens/bipartite_5_5.png)

**a. Vértices Livres e ligação direta:**
Livres: $U_4$ e $V_3$. A ligação direta $U_4 \rightarrow V_3$ **não é válida** pois não existe essa aresta no grafo original. O caminho precisa trafegar por arestas existentes.

**b. Caminho aumentante de $U_4$:**
$U_4 \rightarrow V_2$ (Fora) $\rightarrow U_1$ (Dentro) $\rightarrow V_1$ (Fora) $\rightarrow U_2$ (Dentro) $\rightarrow V_3$ (Fora).

**c. Novo Emparelhamento via Diferença Simétrica ($M \oplus P$):**
> [!NOTE] 
> **Regra de Ouro da Diferença Simétrica:** 
> - Arestas do caminho que estão **Fora** do emparelhamento **Entram**.
> - Arestas do caminho que estão **Dentro** do emparelhamento **Saem**.

- Remove (Dentro $\rightarrow$ Saem): $(U_1, V_2)$ e $(U_2, V_1)$.
- Insere (Fora $\rightarrow$ Entram): $(U_4, V_2), (U_1, V_1)$ e $(U_2, V_3)$. 
Aresta $(U_3, V_4)$ fica intacta (não fazia parte do caminho).
*Final $M'$:* $\{(U_4, V_2), (U_1, V_1), (U_2, V_3), (U_3, V_4)\}$.

**Grafo Final Resultante:**
![Grafo 5.5 Final](imagens/bipartite_5_5_final.png)
