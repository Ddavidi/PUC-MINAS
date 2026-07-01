# Resolução da Lista 7 (IO e Sistema de Arquivos)

## Questão 1 (Métodos de Alocação de Arquivos)
**Enunciado:** Compare os métodos de alocação de arquivos em disco por alocação contígua, encadeada e indexada, discutindo: facilidade de inserção e remoção de blocos, rapidez no acesso a registros, formas de acesso possíveis (sequencial/randômica), necessidade de armazenamento de informações adicionais para manutenção do arquivo, fragmentação interna e externa.

**Resolução:**
- **Facilidade de inserção e remoção de blocos:**
  - *Contígua:* Muito difícil. Como os blocos precisam estar sequenciais, se um arquivo crescer além do espaço alocado inicial, ele terá de ser movido por inteiro para outra região do disco que possua o espaço contínuo necessário.
  - *Encadeada:* Muito fácil. Basta achar qualquer bloco livre no disco e atualizar os ponteiros, conectando-o ao último bloco do arquivo.
  - *Indexada:* Fácil. Apenas adiciona-se o endereço do novo bloco ao bloco de índice (desde que o bloco de índice ainda tenha espaço).
- **Rapidez no acesso a registros (desempenho):**
  - *Contígua:* Extremamente rápido, pois todos os blocos estão vizinhos no disco, exigindo apenas uma busca (seek) inicial da cabeça de leitura.
  - *Encadeada:* Lento para acessos diretos/randômicos. Para ler o bloco $n$, é necessário ler todos os blocos anteriores no disco (ou ter os ponteiros na memória, como ocorre com a FAT).
  - *Indexada:* Rápido. O índice tem o mapeamento direto, permitindo pular direto para o bloco desejado (exige ler o bloco de índice primeiro).
- **Formas de acesso possíveis:**
  - *Contígua:* Sequencial e Randômica excelentes.
  - *Encadeada:* Apenas Sequencial. Randômica é ineficiente.
  - *Indexada:* Sequencial e Randômica muito eficientes.
- **Necessidade de armazenamento adicional (overhead):**
  - *Contígua:* Mínimo (apenas o bloco de início e o tamanho no diretório).
  - *Encadeada:* Médio (parte de cada bloco é ocupada por um ponteiro para o próximo bloco, reduzindo o espaço útil para os dados; ou uso da tabela FAT na memória).
  - *Indexada:* Alto (necessidade de alocar blocos de índice inteiros apenas para guardar os ponteiros, mesmo para arquivos muito pequenos).
- **Fragmentação interna e externa:**
  - *Contígua:* Sofre fortemente de fragmentação externa (buracos entre arquivos) e tem fragmentação interna no último bloco alocado.
  - *Encadeada:* Nenhuma fragmentação externa. Fragmentação interna apenas no último bloco do arquivo.
  - *Indexada:* Nenhuma fragmentação externa. Pode sofrer uma piora na fragmentação interna (desperdício do bloco de índice em arquivos pequenos).

---

## Questão 2 (DMA e Transferência de I/O)
**Enunciado:** Descreva o processo de transferência de dados de um disco para a memória, com acesso direto à memória (DMA). Deixe claros os papeis da CPU, driver, controladoras e barramentos neste processo.

**Resolução:**
1. A **CPU** quer ler algo do disco. O **driver de dispositivo** do SO prepara os comandos e programa a **Controladora de DMA**, fornecendo os parâmetros: qual bloco ler no disco, endereço de destino na memória RAM, e quantos bytes devem ser lidos.
2. Após programar o DMA, a **CPU** fica liberada para executar outros processos, enquanto o hardware resolve a transferência (I/O assíncrono).
3. A **Controladora de Disco** lê mecanicamente os setores solicitados e coloca os dados num *buffer* interno próprio da controladora.
4. Para mover esses dados para a RAM, a **Controladora de DMA** solicita o uso temporário do **Barramento** principal (método *cycle stealing* ou *burst mode*), assumindo o papel da CPU na transferência.
5. O **DMA** copia os bytes diretamente do buffer da controladora de disco para a memória RAM, pelos barramentos.
6. Quando a contagem de bytes atingir zero (transferência completa), a controladora de DMA envia uma **interrupção de hardware** à **CPU**, informando que os dados solicitados já estão disponíveis na memória. O driver do SO então finaliza a solicitação.

---

## Questão 3 (File Allocation Table - FAT System)
**Enunciado:** O que é uma FAT (Tabela de alocação de arquivos)? Qual seu papel no método de alocação encadeado?

**Resolução:**
A **FAT (File Allocation Table)** é uma estrutura de dados de índice criada no início do volume lógico do disco e que, normalmente, é carregada integralmente para a memória principal. Ela centraliza todos os ponteiros do sistema de arquivos.

O papel dela na alocação encadeada é resolver o problema do acesso randômico lento. Ao invés de o ponteiro para o próximo bloco ficar gravado no próprio disco (o que obrigaria a ler fisicamente o bloco 1 para achar o 2, o 2 para achar o 3, etc.), a tabela armazena a relação na memória RAM.
Com a FAT, se o sistema operacional precisa acessar o bloco 50 de um arquivo, ele percorre a cadeia de blocos de forma instantânea (na RAM) pela tabela FAT e descobre qual é o endereço final do bloco procurado no disco. Assim, a FAT permite que um método originalmente sequencial atue de maneira próxima a um método de alocação indexada, precisando apenas de um acesso ao disco para chegar ao bloco desejado.

---

## Questão 4 (Desempenho de Disco e Interleaving)
**Enunciado:** Um disco tem oito setores de 512 bytes por trilha, e uma taxa de rotação de 300rpm. Quanto tempo leva para a leitura de todos os setores da trilha em ordem assumindo que o braço já está corretamente posicionado, que meia (0.5) rotação é necessária para localizar o setor 0 (zero), e que a taxa de transferência do bloco demanda 15 msegundos? Seria possível adotar uma nova política para melhorar a performance? Faça o mesmo calculo para a nova situação (interleaving simples). E se a taxa de transferência demandar 40 msegundos o que aconteceria? Seria possível adotar uma nova política para melhorar a performance? (interleaving duplo).

**Passo a passo da resolução (Segundo a Receita de Cálculo de Interleaving):**

**PASSO 1: Levantamento de Variáveis (A Base)**
- **$T_{rot}$ (Tempo de 1 Rotação):** 300 rpm = `60.000 ms / 300 = 200 ms`.
- **$T_{setor}$ (Tempo de 1 Setor):** `200 ms / 8 setores = 25 ms`.
- **$T_{transf}$:** O enunciado fornecerá 15ms ou 40ms dependendo do cenário.
- **$T_{cego}$ (Leitura + Transf):** `25 ms + T_transf`.

---

**Cenário A: Sem Interleaving (ordem sequencial bruta) | $T_{transf}$ = 15ms**
- **Passo 1 (Base):** $T_{cego} = 25 + 15 = 40 ms$.
- **Passo 2 ($T_{pulo}$):** Sem interleaving (pula 1 setor físico). $T_{pulo} = 1 \times 25 = 25 ms$.
- **Passo 3 (Teste do Gargalo):** $T_{cego} (40ms) > T_{pulo} (25ms)$. Caiu no gargalo!
  - Custo do Salto Punitivo = $T_{pulo} + T_{rot} = 25 + 200 = 225 ms$.
- **Passo 4 (Anomalias):** $N=8$, Pulo=1. MDC(8,1) = 1. Como $MDC - 1 = 0$, não há pulos anômalos.
- **Passo 5 (Fórmula da Transf. Total):** Total de 7 saltos.
  - Soma dos Saltos = `(7 normais × 225 ms) + (0 anômalos) = 1575 ms`.
  - Transf. Total = `Soma dos Saltos + Último Bloco (40)` = `1575 + 40 = 1615 ms`.
- **Tempo Total (Equação de Tanenbaum):** 
  `Busca (0) + Atraso Rotacional (100) + Transferência Total (1615)` = **1715 ms**.

---

**Cenário B: Melhorando a performance - Interleaving Simples | $T_{transf}$ = 15ms**
- **Passo 1 (Base):** $T_{cego} = 25 + 15 = 40 ms$.
- **Passo 2 ($T_{pulo}$):** Interleaving Simples (pula 2). $T_{pulo} = 2 \times 25 = 50 ms$.
- **Passo 3 (Teste do Gargalo):** $T_{cego} (40ms) \le T_{pulo} (50ms)$. Fluxo Ideal!
  - Custo do Salto Normal = $50 ms$.
- **Passo 4 (Anomalias):** $N=8$, Pulo=2. MDC(8,2) = 2. Há 1 salto anômalo.
  - Distância do anômalo = $50 + 25 = 75 ms$. (Não há gargalo nele também: $40 \le 75$).
- **Passo 5 (Fórmula da Transf. Total):** Total de 7 saltos.
  - Soma dos Saltos = `(6 normais × 50 ms) + (1 anômalo × 75 ms) = 300 + 75 = 375 ms`.
  - Transf. Total = `375 + Último Bloco (40)` = `415 ms`.
- **Tempo Total (Equação de Tanenbaum):** 
  `Busca (0) + Atraso Rotacional (100) + Transferência Total (415)` = **515 ms** (Performance mais de 3x superior!).

---

**Cenário C: Interleaving Simples | $T_{transf}$ piora para 40ms**
- **Passo 1 (Base):** $T_{cego} = 25 + 40 = 65 ms$.
- **Passo 2 ($T_{pulo}$):** Interleaving Simples (pula 2). $T_{pulo} = 2 \times 25 = 50 ms$.
- **Passo 3 (Teste do Gargalo):** $T_{cego} (65ms) > T_{pulo} (50ms)$. Caiu no gargalo!
  - Custo do Salto Punitivo = $50 + 200 = 250 ms$.
- **Passo 4 (Anomalias):** $N=8$, Pulo=2. MDC(8,2) = 2. Há 1 salto anômalo de $75 ms$.
  - *Teste do Gargalo no Anômalo:* $T_{cego} (65) \le T_{anomalo} (75)$. **Escapou do gargalo!** 
  - Custo do Salto Anômalo = $75 ms$.
- **Passo 5 (Fórmula da Transf. Total):** Total de 7 saltos.
  - Soma dos Saltos = `(6 punitivos × 250 ms) + (1 livre × 75 ms) = 1500 + 75 = 1575 ms`.
  - Transf. Total = `1575 + Último Bloco (65)` = `1640 ms`.
- **Tempo Total (Equação de Tanenbaum):** 
  `Busca (0) + Atraso Rotacional (100) + Transferência Total (1640)` = **1740 ms**.

---

**Cenário D: Interleaving Duplo | $T_{transf}$ = 40ms**
- **Passo 1 (Base):** $T_{cego} = 25 + 40 = 65 ms$.
- **Passo 2 ($T_{pulo}$):** Interleaving Duplo (pula 3). $T_{pulo} = 3 \times 25 = 75 ms$.
- **Passo 3 (Teste do Gargalo):** $T_{cego} (65ms) \le T_{pulo} (75ms)$. Fluxo Ideal!
  - Custo do Salto Normal = $75 ms$.
- **Passo 4 (Anomalias):** $N=8$, Pulo=3. MDC(8,3) = 1. Como $MDC - 1 = 0$, **não há saltos anômalos**. A ordem forma uma espiral perfeita.
- **Passo 5 (Fórmula da Transf. Total):** Total de 7 saltos.
  - Soma dos Saltos = `(7 normais × 75 ms) + (0 anômalos) = 525 ms`.
  - Transf. Total = `525 + Último Bloco (65)` = `590 ms`.
- **Tempo Total (Equação de Tanenbaum):** 
  `Busca (0) + Atraso Rotacional (100) + Transferência Total (590)` = **690 ms**.

---

## Questão 5 (i-node e Estrutura de Arquivos no UNIX)
**Enunciado:** Foi sugerido que a primeira parte de cada arquivo UNIX fosse mantido no mesmo bloco de disco com o seu i-node. Que benefícios está política gera?

**Resolução:**
O principal benefício é a **economia de acessos a disco e a drástica redução no tempo de leitura para arquivos pequenos** (como scripts, arquivos de texto ou de configuração), que são a grande maioria nos ambientes UNIX.

Normalmente, para ler um arquivo no UNIX, o sistema operacional tem que ir ao disco pelo menos duas vezes:
1. Buscar o i-node do arquivo para saber os atributos e onde estão os blocos de dados;
2. Ir ao disco novamente no endereço que estava no i-node para ler o bloco real de dados.

Com a política sugerida, se os primeiros bytes (ou o arquivo inteiro, se for pequeno o suficiente) estiverem embarcados dentro do próprio bloco do i-node, os dados já são trazidos à memória na primeira leitura. Isso corta o número de leituras em disco pela metade para pequenos arquivos, reduzindo sensivelmente a latência do sistema de arquivos de forma geral.
