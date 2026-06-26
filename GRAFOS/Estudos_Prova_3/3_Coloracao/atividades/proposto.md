# Exercício Proposto: Welsh-Powell Básico

Tente aplicar a receita de bolo do algoritmo de Welsh-Powell neste grafo para descobrir o número cromático dele.

## O Desafio

![Grafo](../imagens/proposto.png)

> [!IMPORTANT]
> Lembre-se do desempate: Para graus iguais, ordene por ordem alfabética/numérica menor (ex: V1 antes de V2).

**Sua Missão:**
1. Monte a tabela de graus para V1, V2, V3, V4, V5, V6.
2. Ordene os vértices por grau decrescente.
3. Aplique as rodadas de cores (Cor 1, Cor 2...).
4. Diga quantas cores foram necessárias no final.

*Tente resolver no papel antes de conferir o gabarito!*

---
<br><br><br><br><br><br><br><br>

## Gabarito

**Passo 1 e 2: Tabela de Graus e Ordenação**
- V1: 2
- V2: 3
- V3: 2
- V4: 2
- V5: 3
- V6: 2
- **Ordem:** V2(3), V5(3), V1(2), V3(2), V4(2), V6(2)

**Passo 3: Tabelas de Coloração (Rodadas)**

*Rodada da Cor 1:*

| Vértice | Grau | Ação (Conflitos verificados) | Cor |
|---|---|---|---|
| **V2** | 3 | Primeiro não colorido. | **Cor 1** |
| **V5** | 3 | Adjacente a V2 (Cor 1). Pula. | - |
| **V1** | 2 | Adjacente a V2 (Cor 1). Pula. | - |
| **V3** | 2 | Adjacente a V2 (Cor 1). Pula. | - |
| **V4** | 2 | Não adjacente a V2. | **Cor 1** |
| **V6** | 2 | Não adjacente a V2 e V4. | **Cor 1** |

*Rodada da Cor 2 (Para os que sobraram: V5, V1, V3):*

| Vértice | Grau | Ação (Conflitos verificados) | Cor |
|---|---|---|---|
| **V5** | 3 | Primeiro não colorido. | **Cor 2** |
| **V1** | 2 | Não adjacente a V5. | **Cor 2** |
| **V3** | 2 | Não adjacente a V5 nem a V1. | **Cor 2** |

*(Todos foram pintados)*

**Passo 4: Resultado Final**
Usamos apenas **2 cores**. Logo, este é um grafo bipartido e $\chi(G) = 2$.
