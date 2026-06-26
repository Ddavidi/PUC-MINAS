# Resumo: Coloração de Grafos

## 1. Coloração de Vértices
Colorir vértices significa atribuir uma "cor" (pode ser um número, letra) a cada nó do grafo com a seguinte regra inviolável: **Dois vértices adjacentes (conectados por uma aresta) NUNCA podem ter a mesma cor.**

*   **Número Cromático ($\chi(G)$):** É o número **mínimo** de cores necessárias para colorir o grafo sem violar a regra.
*   **Grafos Bipartidos:** Sempre podem ser coloridos com exatamente 2 cores ($\chi(G) = 2$).
*   **Ciclos Ímpares:** Qualquer grafo que tenha um ciclo de tamanho ímpar (como um triângulo) precisa de pelo menos 3 cores. Portanto, grafos com ciclos ímpares NUNCA são bipartidos.
*   **Teorema das Quatro Cores:** Qualquer grafo planar (que pode ser desenhado no papel sem cruzar arestas) pode ser colorido com no máximo 4 cores.

### O Algoritmo de Welsh-Powell (Guloso)
É o método clássico para encontrar uma boa coloração (nem sempre a mínima absoluta, mas funciona muito bem).
1. Calcule o grau de cada vértice.
2. Ordene todos os vértices em ordem **decrescente de grau**.
3. Pegue a "Cor 1". Pinte o primeiro vértice da lista (que não tem cor).
4. Desça a lista pintando com a "Cor 1" todos os vértices que ainda não têm cor E que **NÃO são vizinhos** de nenhum vértice que já está pintado com a "Cor 1".
5. Volte para o começo da lista, pegue a "Cor 2", e repita o processo até todo mundo ter cor.

## 2. Coloração de Arestas
Aqui, o objetivo é colorir as *linhas* do grafo. A regra de ouro é: **Arestas que se tocam no mesmo vértice não podem ter a mesma cor.**

*   **Índice Cromático ($\chi'(G)$):** É o número mínimo de cores para colorir as arestas.
*   **Teorema de Vizing:** O índice cromático de qualquer grafo simples será exatamente igual ao **Grau Máximo do Grafo ($\Delta$)** ou ao Grau Máximo **mais um ($\Delta + 1$)**.
    *   *Grafos Bipartidos* sempre usam exatamente $\Delta$ cores.
    *   *Ciclos Ímpares* sempre usam $\Delta + 1$ cores.

### Algoritmo de Misra & Gries
Usado para colorir as arestas iterativamente usando um conceito chamado "Rotação de Leque" (Fan) e Cadeia de Kempe (Dança das Cadeiras).
- **Leque:** Se você tenta pintar uma aresta, mas dá conflito, você levanta um leque olhando as cores livres dos vértices conectados. Se o leque não travar, você empurra as cores para baixo e resolve a aresta.
- **Cadeia de Kempe:** Se o leque travar num ciclo e nenhuma cor encaixar, você busca um caminho de cores alternadas pelo grafo (ex: Cor 1, Cor 3, Cor 1, Cor 3...) e **inverte** as cores nesse caminho. Isso libera a cor que você precisava no começo sem quebrar a validade da coloração no resto do grafo!
