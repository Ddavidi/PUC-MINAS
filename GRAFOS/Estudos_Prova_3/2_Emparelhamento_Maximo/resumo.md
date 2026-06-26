# Resumo: Emparelhamento (Matching)

## O que é Emparelhamento?
Um **Emparelhamento** (ou Matching) $M$ em um grafo é um conjunto de arestas que **não compartilham nenhum vértice**. Ou seja, não existem duas arestas no conjunto $M$ que toquem o mesmo nó. É como formar pares de dança onde cada pessoa só pode dançar com um par.

**Classificações do Emparelhamento:**
1. **Maximal:** Um emparelhamento em que você **não consegue adicionar nenhuma aresta extra** sem quebrar a regra (dois pares usando o mesmo nó). Ele pode não ser o maior possível.
2. **Máximo:** O emparelhamento que contém o **maior número possível de arestas** para aquele grafo inteiro. Todo emparelhamento máximo é maximal, mas nem todo maximal é máximo.
3. **Casamento Perfeito:** É um emparelhamento onde **todos os vértices do grafo estão emparelhados**. O tamanho dele é sempre $|V| / 2$. Todo casamento perfeito é um emparelhamento máximo, mas nem todo emparelhamento máximo é um casamento perfeito.

## Grafos Bipartidos
Grafos onde os vértices podem ser divididos em dois grupos (ex: $U$ e $V$) e todas as arestas ligam alguém de $U$ a alguém de $V$. Não há ligações dentro do mesmo grupo. Muito úteis em problemas de matching (ex: Trabalhadores para Máquinas).

## Como Aumentar um Emparelhamento (Caminhos Aumentantes)
Se você tem um emparelhamento que não é máximo, como aumentá-lo? Usando **Caminhos Aumentantes**.

*   **Vértice Livre:** Um vértice que não está conectado a nenhuma aresta do emparelhamento atual.
*   **Caminho Alternante:** Um caminho cujas arestas **alternam** entre pertencer ao emparelhamento ($M$) e não pertencer ao emparelhamento (não-$M$).
*   **Caminho Aumentante:** Um caminho alternante que **começa num vértice livre** e **termina noutro vértice livre**.

**A Operação Mágica (Diferença Simétrica):**
Se você achar um Caminho Aumentante, faça a diferença simétrica:
- Remova do emparelhamento as arestas que estavam dentro do caminho.
- Adicione ao emparelhamento as arestas que estavam fora, mas agora pertencem ao caminho.
*Resultado:* O seu emparelhamento cresceu em exatamente +1 aresta. O algoritmo de **Hopcroft-Karp** baseia-se exatamente em achar múltiplos caminhos aumentantes.

## E em Grafos Gerais? (Algoritmo de Edmonds / Blossom)
Em grafos não bipartidos, podem existir ciclos de tamanho ímpar (ex: um triângulo). Esses ciclos atrapalham a busca simples por caminhos aumentantes.
O algoritmo de Edmonds resolve isso:
1. Detectando o ciclo ímpar, chamado de **Blossom (Flor)**.
2. **Contraindo** essa flor em um único "supervértice".
3. Procurando o caminho aumentante no grafo contraído.
4. Ao achar o caminho, **expandindo** o supervértice de volta, garantindo que o caminho passe por dentro do ciclo ímpar da forma correta (sempre buscando manter a alternância do tamanho par).
