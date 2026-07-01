# Resumo: Esteganografia (Sistemas Operacionais Modernos - Tanenbaum)

**Aviso Importante sobre o Livro-Base:** 
O material fornecido do livro *Sistemas Operacionais Modernos* (Tanenbaum) no Capítulo 4 é focado nos fundamentos da construção de um SO e gerenciamento de arquivos (como estruturas de alocação, diretórios, limites de tamanho e recuperação com backups).

A **Esteganografia** — a prática de ocultar informações (arquivos, mensagens) dentro de outros arquivos não secretos (como imagens ou áudios), muitas vezes manipulando bits menos significativos ou espaços vazios (*slack space*) — **não é abordada** no capítulo de arquivos do Tanenbaum, por ser um tópico pertencente ao ramo da segurança da informação e forense digital.

Para o estudo da prova, concentre-se nos materiais da disciplina dedicados à esteganografia.

### Relação com Tanenbaum
O conceito de "fragmentação interna" (o espaço desperdiçado no final do último bloco de um arquivo por ele não preencher o bloco inteiro, como descrito na página 195) e o uso detalhado de metadados ensinados por Tanenbaum são as bases teóricas estruturais do SO. É exatamente nesses espaços de sobra em disco (conhecidos em forense como *slack space*) que algumas ferramentas de esteganografia costumam atuar no nível do sistema de arquivos para ocultar dados.
