# Receita de Bolo: Ordenação Topológica com DFS e Detecção de Ciclos

Vamos relembrar como a **Busca em Profundidade (DFS)** funciona e resolver o exercício exato da **Seção 3.2** da sua lista, que demonstra como a DFS identifica um ciclo através de uma *Back-Edge*.

## Como a DFS funciona (Lembrete)
1. **Descoberta:** A DFS chega num vértice. Ele sai do estado "Branco" (Não visitado) e vai para "Cinza" (Em exploração). O relógio marca o **Tempo de Descoberta**.
2. **Aprofundamento:** O algoritmo avança para os vizinhos desse vértice que ainda estão Brancos.
3. **Finalização:** Quando o vértice não tem mais para onde ir (todos os vizinhos já foram finalizados ou não tem vizinhos), ele muda de "Cinza" para "Preto" (Finalizado). O relógio marca o **Tempo de Finalização**.
4. **Regra de Ouro:** A ordenação topológica é formada listando os vértices em ordem **decrescente de Tempo de Finalização**!

## O Desafio (Lista Seção 3.2)

Considere o grafo direcionado a seguir:

![Grafo DFS Ciclo](../imagens/resolvido_dfs.png)

> [!IMPORTANT]
> **Detecção de Ciclos:** Se a DFS, estando em um vértice, tentar visitar um vizinho que está no estado **"Cinza"** (Em exploração), ela acabou de encontrar uma **Back-Edge** (Aresta de Retorno). Isso significa que ela deu a volta e esbarrou no próprio caminho atual. Isso **comprova a existência de um ciclo** e o algoritmo aborta (não existe ordenação topológica).

**Missão:**
Rastreie uma DFS começando pelo vértice **X** e mostre em que ponto exato a DFS detecta o ciclo.

---

## Gabarito e Rastreio de Estados

| Tempo | Ação (Pilha de Recursão) | Nó Atual | Estado do Nó |
|---|---|---|---|
| 1 | Descoberta a partir do `main` | X | X muda para **Cinza** |
| 2 | X visita Y | Y | Y muda para **Cinza** |
| 3 | Y visita Z | Z | Z muda para **Cinza** |
| 4 | Z visita W | W | W muda para **Cinza** |
| 5 | W tenta visitar Y | Y | **Conflito! Y já é Cinza.** |

**Conclusão:**
No **tempo 5**, partindo do nó W, a recursão tenta avançar para o vizinho Y. No entanto, o nó Y já está com o estado "Cinza" (ativo na pilha de exploração, pois foi ele que chamou Z, que chamou W). 

Essa aresta de W para Y é a **Back-Edge**. O algoritmo percebe que retornou para um de seus próprios ancestrais, formando o ciclo fechado: **Y $\rightarrow$ Z $\rightarrow$ W $\rightarrow$ Y**. A ordenação é abortada!
