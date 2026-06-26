# Exercício Proposto: Hopcroft-Karp Básico

Agora é com você! Treine a busca por caminhos aumentantes e a diferença simétrica.

## O Desafio

Temos um grafo bipartido. O Emparelhamento inicial $M$ tem as seguintes arestas: $M = \{(A, W), (B, Y)\}$.

1. Identifique os **vértices livres**.
2. Encontre um **Caminho Aumentante** que comece no vértice livre **C**. Lembre-se, o caminho deve alternar entre (Fora de M) -> (Dentro de M) -> (Fora de M)...
3. Aplique a **Diferença Simétrica** para este caminho.
4. Qual é o **novo emparelhamento máximo** $M'$?

*Faça no papel antes de ler a resposta abaixo!*

---
<br><br><br><br><br><br><br><br>

## Gabarito

**Passo 1: Vértices Livres**
- Livres de um lado: C, D
- Livres do outro lado: X, Z

**Passo 2: Caminho Aumentante partindo de C**
- `C -> Y` (Aresta Fora de $M$)
- `Y -> B` (Aresta Dentro de $M$)
- `B -> W` (Aresta Fora de $M$)
- `W -> A` (Aresta Dentro de $M$)
- `A -> X` (Aresta Fora de $M$)
- Chegamos no vértice livre **X**.

O Caminho Aumentante é: **C $\rightarrow$ Y $\rightarrow$ B $\rightarrow$ W $\rightarrow$ A $\rightarrow$ X**

**Passo 3: Diferença Simétrica**
- Remover de $M$ (Dentro): $(B, Y)$ e $(A, W)$
- Adicionar a $M$ (Fora): $(C, Y)$, $(B, W)$ e $(A, X)$

**Passo 4: Novo Emparelhamento Máximo**
- $M'$ = **$\{(C, Y), (B, W), (A, X)\}$**
