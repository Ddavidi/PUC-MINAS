# 🕵️ Cola Ninja: Prova 3 Grafos

## 1. Ordenação Topológica
**Algoritmo de Kahn (Graus de Entrada):**
1. Calcule o grau de entrada (flechas chegando) de todos.
2. **Fila:** Coloque quem tem grau 0.
3. Tira 1 da Fila $\rightarrow$ Põe na Ordem Final.
4. Diminui `-1` no grau dos vizinhos dele. 
5. Vizinho zerou o grau? Entra na Fila. Repita até zerar a fila.
*(Dica: Fila esvaziou e sobrou vértice? É Ciclo!)*

**DFS (Tempo de Finalização):**
1. Cores: **Branco** (Não visitado), **Cinza** (Pilha/Na fila), **Preto** (Finalizado).
2. Vizinho é **Branco**? Visita.
3. Vizinho é **Cinza**? **CICLO (Back-edge)! Parou tudo.**
4. Sem vizinhos Brancos? Pinta de **Preto** e anota Tempo de Finalização.
5. **Ordem:** Leia os tempos de finalização de trás pra frente (Decrescente).

## 2. Emparelhamento Máximo (Hopcroft-Karp)
1. Ache vértices **Livres**.
2. Monte caminho alternante saindo do livre: 
   - Aresta **FORA**, depois **DENTRO**, depois **FORA**...
3. Chegou num vértice **Livre** no outro lado? Sucesso, é caminho aumentante!
   - Se bateu em vértice casado, é OBRIGADO a seguir pela aresta de DENTRO dele.
4. **Diferença Simétrica:** Arestas do caminho que eram FORA agora ENTRAM. As que eram DENTRO agora SAEM. (O tamanho sobe +1).
5. Repita até travar e nenhum caminho chegar livre-livre.

## 3. Coloração de Grafos (Welsh-Powell)
1. Faça tabela e ordene vértices do **MAIOR** pro **MENOR** grau.
2. Pegue a Cor 1. Pinte o primeiro da fila.
3. Desça a fila: pinte da Cor 1 todo mundo que **NÃO é vizinho** de quem já tem Cor 1.
4. Volte pro topo, pegue a Cor 2, e repita para quem sobrou.

## 4. Alocação
**Gale-Shapley (Cascata):**
1. Hospital faz proposta pro 1º da sua lista. 
2. Médico avalia: 
   - Livre? Aceita na hora.
   - Casado? Compara. Se o novo for melhor na lista dele, ele troca e chuta o ex!
3. O chutado volta pro mercado e tenta o próximo da sua própria lista.
4. Acaba quando ninguém mais puder ofertar.

**Método Húngaro (Minimização/Designação):**
1. **Zerar Linhas:** Ache o menor da linha, subtraia de toda a linha.
2. **Zerar Colunas:** Ache o menor da coluna, subtraia de toda a coluna.
3. **Cobrir (Tracejar):** Faça traços horizontais/verticais cobrindo todos os Zeros.
   - N de traços = N da matriz? ACABOU! Escolha zeros sem repetir l/c.
4. **Não Acabou (Linhas < N):** 
   - Pegue o MENOR número **NÃO coberto**.
   - Subtraia ele de quem NÃO tem traço.
   - SOME ele onde tem **cruzamento** de traços.
   - Volte pro Passo 3.

## 5. Indep, Dominância e Cobertura
- **Cobertura de Vértices ($\alpha$):** Vértices necessários para "tocar" em todas as linhas. (Guloso: Elimine o vértice de MAIOR grau e apague suas linhas. Repita).
- **Conj. Independente ($\beta$):** Vértices soltos que não encostam um no outro. (Guloso: Pegue o vértice de MENOR grau, apague ele e seus vizinhos. Repita).
- **Dominância ($\gamma$):** Os "chefes". Todo mundo que tá de fora, ou é o chefe, ou é vizinho do chefe. (Guloso: Pegue quem domina mais caras inéditos).
- **Teorema de Gallai:** $\alpha + \beta = |V|$ (Nº total de vértices). Achou um, faz continha de menos pra achar o outro!
