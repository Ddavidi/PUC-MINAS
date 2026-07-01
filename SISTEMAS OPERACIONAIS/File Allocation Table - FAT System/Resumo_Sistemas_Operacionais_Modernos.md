# Resumo: File Allocation Table - FAT (Sistemas Operacionais Modernos - Tanenbaum)

Com base no Capítulo 4 do livro *Sistemas Operacionais Modernos* (Tanenbaum), a FAT é explicada como uma evolução da alocação por lista encadeada de blocos no disco.

## 1. O Problema da Alocação por Lista Encadeada no Disco
Originalmente, os arquivos podiam ser armazenados em uma lista encadeada, onde o primeiro bloco de disco do arquivo continha um ponteiro para o próximo bloco, e assim por diante. 
**Desvantagens originais:**
- O ponteiro ocupava alguns bytes no início do bloco, fazendo com que os dados não tivessem um tamanho potência de dois (ex: 512 bytes), o que prejudicava a eficiência de leitura de muitos programas.
- O acesso aleatório era extremamente lento, pois o SO precisava ler todos os blocos no disco desde o começo para chegar a um bloco no meio do arquivo.

## 2. A Solução: Tabela na Memória (FAT)
Para resolver isso, os ponteiros de cada bloco de disco foram movidos do próprio bloco de disco para uma **tabela na memória principal**, chamada **FAT (File Allocation Table - Tabela de Alocação de Arquivos)**.
- O bloco inteiro no disco fica disponível exclusivamente para armazenar dados.
- O acesso aleatório torna-se muito mais rápido. Embora ainda seja necessário percorrer a cadeia de ponteiros, essa cadeia está **inteiramente na memória RAM**, eliminando as lentas leituras físicas do disco para procurar ponteiros.
- A entrada de diretório armazena apenas o número do bloco inicial. Na FAT, a posição correspondente a esse bloco contém o endereço do bloco seguinte, até que seja encontrado um marcador de fim de arquivo (ex: -1).

## 3. Desvantagens da FAT
O principal ponto fraco é que **a tabela inteira precisa estar na memória o tempo todo** para funcionar corretamente. 
- A FAT cresce linearmente com o tamanho do disco.
- Para um disco de 1 TB com blocos de 1 KB, a tabela precisaria de 1 bilhão de entradas (cada uma com 3 a 4 bytes), ocupando até 3 GB de memória RAM principal só para a tabela de alocação. 
- Por isso, a ideia da FAT não escala muito bem para discos enormes modernos (daí a necessidade do NTFS, ext4, etc.).

## 4. O Sistema MS-DOS (Implementação Real da FAT)
Tanenbaum cita as versões da FAT: **FAT-12, FAT-16 e FAT-32**.
- O MS-DOS usava a tabela FAT para monitorar não só os blocos do arquivo, mas também os blocos livres (qualquer bloco não alocado recebe um código especial de "livre" na tabela, dispensando o uso de mapas de bits separados).
- O número (12, 16 ou 32) refere-se à quantidade de bits usada para os endereços dos blocos (clusters).
- Tamanhos de partição eram limitados pelo tamanho do bloco. O FAT-32 foi introduzido para suportar partições maiores e usa tamanhos de bloco flexíveis (de 1 KB a 32 KB) dependendo do tamanho total da partição.
