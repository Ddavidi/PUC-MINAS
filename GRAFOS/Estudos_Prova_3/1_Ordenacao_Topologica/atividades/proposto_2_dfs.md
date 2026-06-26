# Exercício Proposto: Ordenação Topológica via DFS

Baseado **diretamente na Seção 3.4 da sua lista de exercícios**, vamos tentar fazer a ordenação usando a Busca em Profundidade (DFS) em vez do algoritmo de Kahn.

## O Desafio

Considere o seguinte DAG de pacotes de software e suas dependências (onde a seta de A para B indica que "A depende de B", ou seja, A tem que ser feito antes de B).

![Grafo Proposto DFS](../imagens/proposto_novo.png)

> [!IMPORTANT]
> Regra do algoritmo DFS para ordenação topológica:
> 1. Inicie a DFS a partir de um vértice (comece pelo A). 
> 2. Em caso de empate para visitar vizinhos, vá pela ordem alfabética.
> 3. Marque o **tempo de finalização** (finishing time) de cada vértice. O vértice só finaliza quando não tem mais vizinhos para visitar ou quando todos os vizinhos já foram visitados.
> 4. A ordenação final é a lista de vértices em ordem **decrescente de tempo de finalização**.

**Sua Missão:**
1. Rastreie a DFS começando pelo nó **A**.
2. Anote o tempo de finalização de cada nó (A, B, C, D).
3. Escreva a ordenação topológica final baseada nos tempos.

*Tente resolver no papel antes de conferir o gabarito!*

---
<br><br><br><br><br><br><br><br>

## Gabarito

**Passo 1 e 2: Rastreio da DFS (Tempos de Descoberta e Finalização)**

Começamos o relógio no Tempo 1.
- **Tempo 1:** Descobre A.
- **Tempo 2:** A visita o vizinho B (ordem alfabética entre B e D).
- **Tempo 3:** B visita o vizinho C.
- **Tempo 4:** C não tem vizinhos para visitar. C **finaliza**. (F(C) = 4)
- **Tempo 5:** A recursão volta para B. B não tem mais vizinhos não visitados. B **finaliza**. (F(B) = 5)
- **Tempo 6:** A recursão volta para A. A visita o seu outro vizinho, D.
- **Tempo 7:** D tenta visitar C, mas C já foi visitado. Logo, D **finaliza**. (F(D) = 7)
- **Tempo 8:** A recursão volta para A. A não tem mais vizinhos. A **finaliza**. (F(A) = 8)

Tempos de finalização $F$:
- A: 8
- D: 7
- B: 5
- C: 4

**Passo 3: Ordenação Topológica (Decrescente de F)**
Basta ordenar do maior tempo de finalização para o menor:
**A $\rightarrow$ D $\rightarrow$ B $\rightarrow$ C**

*(Você também veria que "A -> B -> D -> C" respeita as setas e é válida, mas usando a DFS com as regras acima, a resposta correta e precisa do algoritmo é A -> D -> B -> C).*
