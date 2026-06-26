# Resumo: Cobertura, Independência e Dominância

Este trio foca em selecionar vértices de um grafo de acordo com regras específicas de otimização (normalmente achar o menor ou o maior conjunto). São clássicos problemas NP-Completos, frequentemente resolvidos com aproximações.

## 1. Conjunto Independente (Independent Set - IS)
Um Conjunto Independente é um grupo de vértices onde **nenhum toca no outro**. Se o vértice A está no conjunto e B está no conjunto, não pode haver uma aresta entre A e B.
- **Conjunto Independente Máximo ($IS_{max}$):** O maior número de vértices que você consegue isolar desse jeito no grafo. Seu tamanho é denotado por $\alpha(G)$.

## 2. Cobertura de Vértices (Vertex Cover - VC)
Um conjunto de vértices funciona como "seguranças" de arestas. Você coloca um guarda em um vértice e ele "cobre" todas as arestas que encostam nele. A Cobertura de Vértices ocorre quando **todas as arestas do grafo estão cobertas** por pelo menos um nó do conjunto escolhido.
- **Cobertura de Vértices Mínima ($VC_{min}$):** O menor número de seguranças (nós) necessários para vigiar todas as ruas (arestas).

### O Teorema Mágico de Gallai
As ideias de Cobertura e Independência são metades da mesma laranja. O Teorema de Gallai afirma que, para qualquer grafo sem nós isolados:
**Tamanho do $IS_{max}$ + Tamanho do $VC_{min}$ = Total de Vértices do Grafo ($|V|$)**

Isso significa que, se você achou o maior conjunto de nós que não se tocam, os nós que sobraram fora do conjunto formam, obrigatoriamente, a menor cobertura de vértices possível!

### Aproximação Gulosa para VC
Como é difícil achar o $VC_{min}$ perfeito num grafo gigante, usamos um truque que nos garante chegar até, no pior dos casos, o dobro do tamanho ideal (2-Aproximação):
1. Escolha uma aresta qualquer do grafo (ex: A-B).
2. Adicione **ambos os vértices** (A e B) na sua Cobertura.
3. Apague A, apague B, e **apague todas as arestas que tocavam neles**.
4. Repita com o grafo que sobrou até que não reste nenhuma aresta.

## 3. Conjunto Dominante (Dominating Set)
Imagine que os vértices são salas. Se você coloca um Roteador Wi-Fi numa sala, ele dá sinal para a sala dele E para todas as salas diretamente vizinhas (que têm porta/aresta pra lá).
Um Conjunto Dominante é colocar roteadores de forma que **todos os vértices do grafo ou tenham o roteador ou sejam vizinhos diretos de quem tem**.
- O objetivo é o Conjunto Dominante Mínimo (usar o mínimo de roteadores).
- *Heurística comum:* Seja guloso. Sempre coloque o roteador no nó de maior grau (o cara que alcança mais vizinhos ainda sem internet). Atualize quem ganhou internet, e repita para quem sobrou sem.
