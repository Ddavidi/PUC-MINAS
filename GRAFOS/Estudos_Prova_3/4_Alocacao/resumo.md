# Resumo: Alocação e Otimização

## 1. Casamento Estável (Gale-Shapley)
O problema do casamento estável tenta alocar pares (ex: Médicos e Hospitais) considerando as matrizes de **preferência** de cada lado, sem gerar "Pares Bloqueadores" (um par que não está junto, mas ambos prefeririam estar juntos a estar com seus pares atuais, o que os faria abandonar o alinhamento para fugirem juntos).

**Como funciona o Algoritmo (Cascata):**
- **Proponentes:** O lado que faz as propostas (age ativamente, vai do topo para a base da sua lista de preferências).
- **Revisores:** O lado que recebe propostas. Aceitam "provisoriamente" a melhor oferta e rejeitam propostas piores. Se receberem uma proposta melhor depois, eles trocam!
- O grupo que é o Proponente **sempre leva vantagem**. O algoritmo garante a eles o melhor casamento estável possível.

## 2. Método Húngaro (Minimização de Custos)
Ao invés de preferências, aqui temos **valores monetários/tempo/distância** numa matriz (ex: 4 tarefas para 4 funcionários). Queremos alocar 1 para 1 gerando o **menor custo total** (Emparelhamento Perfeito de Peso Mínimo em grafos bipartidos).

**Passos Principais:**
1. **Redução de Linha:** Ache o menor valor de cada linha e subtraia ele de todos os outros elementos daquela mesma linha.
2. **Redução de Coluna:** Na matriz resultante, ache o menor valor de cada coluna e subtraia de toda a coluna.
3. **Cobertura de Zeros:** Tente traçar **retas** (verticais ou horizontais) cobrindo todos os zeros da matriz. O objetivo é usar o *mínimo* de retas possível.
4. **Verificação:** 
   - Se o número de retas for igual a $N$ (dimensão da matriz, ex: 4 retas numa matriz 4x4), você achou o fim! Vá para o Passo 6.
   - Se for menor que $N$, precisamos criar novos zeros (Passo 5).
5. **Ajuste de Custo:** Encontre o **menor elemento** de toda a matriz que **NÃO foi coberto** por nenhuma reta. 
   - Subtraia ele de todos os outros elementos não cobertos.
   - Some ele onde duas retas se cruzam (interseções).
   - Onde a reta passa simples, deixe quieto.
   - Volte ao Passo 3.
6. **Alocação:** Agora você escolhe os zeros. Dê prioridade a linhas ou colunas que só tem 1 zero isolado. Se a Tarefa 1 tem zero na Máquina 3, aloque T1 para M3.

**E se for um problema de Maximizar Lucro?**
O Húngaro só funciona para minimizar. Para maximizar, ache o MAIOR valor de toda a tabela original, subtraia TODOS os valores da tabela desse valor gigante (isso inverte os valores: o que era lucro vira "perda" a ser evitada), e rode o Húngaro minimizando a perda.
