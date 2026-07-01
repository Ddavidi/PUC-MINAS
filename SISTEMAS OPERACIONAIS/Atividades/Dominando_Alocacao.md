# Dominando: Métodos de Alocação de Arquivos

Para a Prova 3, você precisa entender perfeitamente como o Sistema Operacional decide em quais blocos físicos do disco ele vai gravar os pedaços (blocos lógicos) de um arquivo. Segundo Tanenbaum, existem três abordagens fundamentais.

---

## 1. Alocação Contígua
A ideia mais simples de todas: guardar o arquivo inteiro em **blocos sequenciais** no disco. Se o arquivo tem 50 KB e os blocos têm 1 KB, o SO acha 50 blocos vizinhos (ex: blocos 100 até 149) e grava o arquivo lá.

### ✅ Vantagens:
- **Desempenho Extremo:** É o método mais rápido para leitura. O disco posiciona a cabeça de leitura no bloco inicial (apenas 1 *seek*) e depois apenas lê continuamente, aproveitando a rotação do disco.
- **Implementação Simples:** O SO só precisa anotar no diretório duas coisas: o endereço do primeiro bloco e a quantidade de blocos (tamanho do arquivo).

### ❌ Desvantagens:
- **Fragmentação Externa (O Gargalo):** Conforme arquivos são apagados e criados, o disco vira um "queijo suíço" cheio de pequenos buracos vazios. O disco pode ter espaço livre total, mas se não tiver espaço **contíguo**, você não consegue salvar o arquivo.
- **Crescimento Impossível:** Se você abrir um arquivo do Word e escrever mais páginas, ele vai precisar de mais blocos. Se o bloco vizinho já estiver ocupado por outro arquivo, o SO é obrigado a copiar o seu arquivo inteiro para uma área maior do disco, o que é lentíssimo.

*Exemplo de uso:* CD-ROMs e DVDs. Como você grava tudo de uma vez só e o tamanho já é conhecido (não vai crescer), a alocação contígua é perfeita.

---

## 2. Alocação Encadeada (Lista Ligada)
Para resolver o problema do crescimento e dos buracos da contígua, surgiu a alocação encadeada. Aqui, o arquivo pode ser gravado em **blocos espalhados** por qualquer lugar do disco.
O truque é: O primeiro bloco guarda um pedaço do arquivo e um **ponteiro** indicando o endereço físico do próximo bloco (como uma caça ao tesouro).

### ✅ Vantagens:
- **Zero Fragmentação Externa:** Qualquer bloco livre no disco serve. Não existe mais problema de "buraco pequeno".
- **Crescimento Fácil:** Se o arquivo crescer, basta o SO achar qualquer bloco livre no disco, colocar os dados lá e atualizar o ponteiro do último bloco.

### ❌ Desvantagens:
- **Acesso Randômico Destruído:** Se você quiser ler direto o bloco 50 do arquivo, o SO não sabe onde ele está. Ele é obrigado a ir no disco ler o bloco 1, pegar o ponteiro, ler o bloco 2 no disco, pegar o ponteiro... e fazer isso 50 vezes. Lentidão absurda!
- **Desperdício Interno (Overhead):** Como o ponteiro rouba alguns bytes do bloco, o tamanho útil de dados não é mais potência de 2 (ex: de 512 bytes, sobram 508 para dados). Isso atrapalha a matemática de muitos programas.

---

## 3. Alocação Encadeada com Tabela em Memória (FAT)
A Microsoft pegou a alocação encadeada e deu um "jeitinho" brilhante. E se a gente arrancar os ponteiros de dentro dos blocos no disco e colocá-los todos juntos em uma tabela? Nascia a **File Allocation Table (FAT)**.
A FAT é carregada inteiramente na Memória RAM.

### ✅ Vantagens:
- **Salvação do Acesso Randômico:** Se você quer o bloco 50, o SO não vai ao disco. Ele percorre a corrente de ponteiros dentro da tabela FAT na memória RAM (que é milhares de vezes mais rápida que o disco mecânico) de forma instantânea. Quando acha o endereço final, faz apenas 1 acesso ao disco no bloco certo!
- **Tamanho do bloco volta a ser íntegro:** Como os ponteiros saíram de dentro do disco, os blocos voltam a ter o tamanho total disponível para os dados.

### ❌ Desvantagens:
- **Consumo de RAM:** A tabela FAT inteira precisa ficar na RAM o tempo todo. Se o disco for muito grande (ex: 1 TB), a tabela vai ter milhões de entradas, comendo uma fatia enorme da memória do computador.

---

## 4. Alocação Indexada (Os i-nodes do UNIX)
O UNIX precisava resolver o consumo de RAM da FAT. A ideia foi: em vez de carregar a árvore genealógica de **todos** os arquivos do disco para a RAM, por que não criar uma tabelinha individual para cada arquivo?
Nasce o **bloco de índice (ou i-node)**. Ele é um bloco no disco que serve apenas para guardar os endereços (ponteiros) de onde estão os blocos de dados daquele arquivo específico.

### ✅ Vantagens:
- **Economia de RAM:** O SO só precisa trazer o i-node para a RAM se o arquivo estiver **aberto**. Arquivos fechados ficam quietos no disco. Uma baita economia de memória comparado à FAT.
- **Acesso Randômico Rápido:** Como você tem o índice inteiro do arquivo na mão, se quiser o bloco 50, é só olhar na 50ª linha do índice e ir direto ao disco.
- **Sem fragmentação externa.**

### ❌ Desvantagens:
- **Fragmentação Interna (Overhead):** Todo arquivo, mesmo um script `.sh` minúsculo de 10 bytes, exigirá no mínimo 2 blocos no disco: 1 para os dados e 1 inteiro só para o índice (i-node).
*(Nota: O UNIX contornou isso em versões modernas salvando os arquivos minúsculos dentro do próprio i-node, como vimos na questão 5).*
- **Arquivos Gigantes:** Se um arquivo for gigantesco, a lista de blocos dele não vai caber em um único i-node. O sistema tem que fazer "índices multinível" (um bloco de índice apontando para outros blocos de índices).

---
## Resumo Matador para a Prova:
- **Contígua:** Mais rápida de ler, impossível de crescer. (Buracos/Frag. Externa).
- **Encadeada (Comum):** Fácil crescer, impossível acessar no meio. (Lentidão de disco).
- **Encadeada (FAT):** Resolve acesso randômico botando os ponteiros na RAM. (Gasta muita RAM).
- **Indexada (i-nodes):** Resolve acesso randômico e gasto de RAM, carregando apenas a tabela do arquivo aberto. (Gasta blocos de índice no disco).
