# Resumo Definitivo: Prova 3 - Sistemas Operacionais

Este é o resumo consolidado de todos os temas cobrados na Prova 3.

---

## 1. O Conceito de Arquivo e Sistemas de Arquivos
Um **Sistema de Arquivos** é a parte do SO responsável por gerenciar a forma como os dados são armazenados e recuperados do disco.

- **Arquivo:** Unidade lógica de armazenamento de informações definida pelo SO. Os atributos de um arquivo (nome, tipo, tamanho, localização, permissões) ficam armazenados em uma estrutura chamada **diretório** (ou bloco de controle do arquivo / *i-node*).
- **Acesso:**
  - *Sequencial:* Lidos em ordem, do início ao fim (ex: fitas magnéticas).
  - *Direto (Randômico):* Permite ir diretamente a um bloco específico do arquivo sem ler os anteriores (essencial para bancos de dados).

### Métodos de Alocação (COMO os arquivos são guardados no disco)
1. **Contígua:** O arquivo ocupa um conjunto de blocos contíguos (vizinhos) no disco.
   - *Vantagem:* Acesso sequencial e direto extremamente rápidos (pouco movimento de cabeça de leitura).
   - *Desvantagem:* Sofre de severa **fragmentação externa** (buracos vazios) e é muito difícil aumentar o tamanho do arquivo depois de criado.
2. **Encadeada:** Cada bloco do arquivo contém um ponteiro para o próximo bloco. O arquivo pode estar espalhado em qualquer lugar do disco.
   - *Vantagem:* Resolve a fragmentação externa e é fácil aumentar o arquivo.
   - *Desvantagem:* O acesso direto é péssimo (muito lento), pois requer ler o bloco 1 para achar o 2, etc.
3. **Indexada:** Todos os ponteiros são reunidos em um **bloco de índice**.
   - *Vantagem:* Acesso direto excelente e sem fragmentação externa.
   - *Desvantagem:* Desperdício de espaço (fragmentação interna) para arquivos pequenos, pois um bloco inteiro é gasto apenas para guardar meia dúzia de ponteiros.

---

## 2. File Allocation Table (FAT System)
O **FAT** é uma evolução inteligente da **Alocação Encadeada**.
- Em vez de o ponteiro para o próximo bloco estar "junto com os dados no disco" (o que exigiria uma leitura demorada no disco mecânico), o SO cria uma **tabela (FAT)** logo no início do disco e a carrega **inteira para a Memória RAM**.
- Cada entrada na tabela representa um bloco (cluster) do disco. Se um arquivo usa o bloco $X$, a entrada $X$ na FAT contém o número do próximo bloco.
- **Vantagem Absoluta:** O acesso randômico se torna rápido, pois o SO "percorre" a corrente de ponteiros em nanossegundos na RAM, e só vai ao disco uma vez, diretamente no bloco desejado.

---

## 3. I/O (Entrada e Saída) e Discos
O módulo de I/O faz a interface entre o SO e o hardware físico.

- **DMA (Acesso Direto à Memória):** Em vez de a CPU gastar tempo movendo cada byte do disco para a RAM (I/O Programado), a CPU instrui a **Controladora de DMA**. A controladora transfere os dados do disco direto para a memória e apenas avisa a CPU com uma **interrupção** quando termina. Isso deixa a CPU livre para outras tarefas.
- **Desempenho do Disco:** O tempo para ler/escrever algo no disco mecânico é a soma de:
  - *Tempo de Busca (Seek):* Mover o braço para o cilindro correto (é o mais demorado).
  - *Atraso Rotacional (Latência):* Esperar o disco girar até que o setor desejado passe embaixo da cabeça.
  - *Tempo de Transferência:* O tempo efetivo para ler os dados e enviá-los (pode ser otimizado por técnicas como **Interleaving** - pular setores para dar tempo da controladora processar os dados sem perder rotações do disco).

---

## 4. Esculpimento de Arquivos (File Carving)
É uma técnica avançada de **Computação Forense** (e recuperação de dados).
- **O Problema:** Quando você formata um disco ou a tabela de arquivos (como a FAT ou MFT) é destruída, o SO não sabe mais onde começam e terminam os arquivos, pois perdeu os "ponteiros".
- **A Solução (Esculpimento):** O software de recuperação varre o disco "cru" (setor por setor) ignorando o sistema de arquivos. Ele procura por **Magic Numbers** (Assinaturas). 
  - *Exemplo:* Todo arquivo JPEG sempre começa com os bytes `FF D8` e termina com `FF D9`. Ao achar o cabeçalho e o rodapé, o programa "esculpe" o que está no meio e extrai a foto, mesmo sem a FAT.

---

## 5. Esteganografia
Diferente da *Criptografia*, onde a mensagem vira um texto ininteligível (você vê que é um código secreto, só não consegue ler), a **Esteganografia** é a arte de **ocultar a EXISTÊNCIA** da mensagem.
- **Como funciona:** Você esconde um dado confidencial dentro de um "arquivo hospedeiro" perfeitamente normal e funcional (uma foto bonita, um áudio, um vídeo).
- **Técnica comum (LSB - Least Significant Bit):** Substitui-se o último bit da cor de cada pixel de uma foto pelos bits da mensagem secreta. A mudança de cor é imperceptível ao olho humano, o arquivo abre como uma foto normal, mas um software específico consegue extrair a mensagem lendo os últimos bits. É muito usado para vazamento dissimulado de dados e espionagem.
