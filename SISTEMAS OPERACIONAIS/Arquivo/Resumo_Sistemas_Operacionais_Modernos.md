# Resumo: Arquivos (Sistemas Operacionais Modernos - Tanenbaum)

Com base no Capítulo 4 do livro *Sistemas Operacionais Modernos* (Tanenbaum), aqui está o resumo focado na didática e conceitos de Arquivos:

## 1. O Conceito de Arquivo
Arquivos são unidades lógicas de informação criadas por processos, atuando como um mecanismo de abstração. Eles permitem armazenar grandes quantidades de dados em disco e protegê-los dos detalhes complexos de hardware (como setores e trilhas). As informações armazenadas devem ser **persistentes**, ou seja, não podem ser perdidas quando o processo que as criou for concluído.

## 2. Estruturas Lógicas de Arquivos
Os arquivos podem ser estruturados de várias maneiras:
1. **Sequência Desestruturada de Bytes:** O sistema operacional não sabe o que há no arquivo; ele vê apenas bytes. O significado dos dados é imposto pelos programas de usuário (usado por UNIX e Windows). Oferece máxima flexibilidade.
2. **Sequência de Registros:** Um arquivo é uma sequência de registros de tamanho fixo com estrutura interna. A leitura retorna um registro e a escrita anexa/sobrescreve um registro (usado em antigos mainframes com cartões perfurados).
3. **Árvore de Registros:** O arquivo consiste em uma árvore de registros de tamanhos variáveis, organizados por um campo "chave" para buscas rápidas. A operação básica é obter um registro com uma chave específica.

## 3. Tipos de Arquivos
Muitos SOs aceitam diferentes tipos de arquivos:
- **Arquivos Regulares:** Contêm informações do usuário. Podem ser ASCII (texto puro legível e editável) ou binários (com estrutura interna conhecida pelos programas, ex: executáveis com números mágicos, cabeçalhos, texto e dados).
- **Diretórios:** Arquivos de sistema para manter a estrutura do sistema de arquivos.
- **Arquivos Especiais de Caracteres:** Relacionados a entrada/saída, modelam dispositivos seriais como terminais, impressoras e redes.
- **Arquivos Especiais de Blocos:** Usados para modelar discos.

## 4. Acesso aos Arquivos
- **Acesso Sequencial:** O processo lê todos os bytes em ordem. Não é possível pular nem ler fora de ordem.
- **Acesso Aleatório:** Os bytes podem ser lidos fora de ordem, o que é essencial para bancos de dados. Pode ser feito indicando a posição em cada `read` ou usando uma operação de `seek` (buscar) para definir a posição atual antes da leitura.

## 5. Atributos (Metadados)
Todo arquivo possui metadados além dos seus dados em si. Atributos comuns incluem:
- **Proteção e Proprietário:** Quem criou e quem pode acessar (e como).
- **Sinalizações (Flags):** Arquivo oculto, de sistema, temporário, somente leitura, etc.
- **Tempos:** Data e hora de criação, último acesso e última alteração.
- **Tamanhos:** Tamanho atual e máximo permitido.
