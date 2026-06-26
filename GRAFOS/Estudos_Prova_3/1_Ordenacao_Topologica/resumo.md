# Resumo: Ordenação Topológica e DAGs

## O que é um DAG?
**DAG** significa Grafo Acíclico Direcionado (Directed Acyclic Graph).
- **Direcionado:** As arestas possuem setas (indicam fluxo ou dependência).
- **Acíclico:** Não existem ciclos. Você nunca consegue sair de um nó, seguir as setas e voltar para o mesmo nó.

## O que é a Ordenação Topológica?
É uma forma de listar os vértices do DAG em uma linha reta (ordem linear) de modo que, se existe uma tarefa **A** que deve ser feita antes de **B** (A $\rightarrow$ B), então **A** obrigatoriamente vai aparecer antes de **B** na sua lista final.

Exemplo de uso: Ordenar disciplinas da faculdade com pré-requisitos, ordem de compilação de arquivos, agendamento de tarefas em projetos (Project Scheduling).

## 1. Algoritmo de Kahn (O Método dos Graus de Entrada)
A intuição aqui é: *"Sempre escolha quem não depende de ninguém no momento"*.

- **Grau de entrada (In-degree):** Quantidade de setas apontando para um vértice.
- Se o grau de entrada é **zero**, significa que aquela tarefa não tem dependências pendentes e pode ser executada/processada agora.

**Como funciona:**
1. Calcule o grau de entrada de todos os nós.
2. Coloque todos os nós com grau 0 numa **Fila**.
3. Enquanto a fila não estiver vazia:
   - Retire um nó da fila (esse nó vai para a lista final de ordenação).
   - "Apague" as setas que saem desse nó (isso reduz em 1 o grau de entrada dos vizinhos).
   - Se algum vizinho ficar com grau 0 após essa redução, coloque-o na fila.

**Deadlock (Detecção de Ciclos):** Se a fila esvaziar, mas ainda sobrarem nós no grafo, significa que o grafo **tem um ciclo**. Nós em ciclo ficam presos porque um espera o outro, logo ninguém atinge grau 0.

## 2. Ordenação Topológica via DFS (Busca em Profundidade)
A DFS também consegue gerar a ordenação topológica de forma elegante!

**Como funciona:**
1. Rode a DFS passando por todos os vértices (se o vértice já foi visitado, pule).
2. Para cada vértice, registre o seu tempo de término, ou seja, o "finishing time". O tempo de término é o momento em que a recursão daquele nó não tem mais pra onde ir e termina.
3. A ordenação topológica válida é a lista dos vértices em ordem **decrescente de tempo de término** (do maior para o menor).

**Detecção de Ciclos pela DFS:** Se, durante a execução, o algoritmo tentar visitar um vizinho que está no estado "Cinza" (já foi descoberto, mas a recursão dele ainda não terminou), ele encontrou uma **Back-Edge** (aresta de retorno). Isso indica um ciclo e a ordenação falha.

## 3. Caminho Crítico (Critical Path)
Em cronogramas de projeto, cada aresta tem um "peso" (duração em dias/horas).
O Caminho Crítico é o **caminho mais longo** do Início ao Fim. Ele dita o tempo mínimo necessário para que todo o projeto termine. Qualquer atraso nas tarefas do caminho crítico atrasa o projeto inteiro.
