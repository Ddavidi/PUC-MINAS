# Resumo: Esculpimento / File Carving (Sistemas Operacionais Modernos - Tanenbaum)

**Aviso Importante sobre o Livro-Base:** 
O material fornecido do livro *Sistemas Operacionais Modernos* (Tanenbaum) no Capítulo 4 trata da implementação tradicional e estrutural de Sistemas de Arquivos (alocação, diretórios, inodes, FAT, otimizações de disco e consistência).

Tópicos de Forense Digital avançada, como **Esculpimento (File Carving)** — que é a técnica de recuperar arquivos fragmentados ou deletados a partir dos dados brutos do disco, sem o auxílio das tabelas do sistema de arquivos (como a FAT ou Inodes) — **não são o foco** deste capítulo clássico do Tanenbaum. 

Para estudar esse conteúdo para a prova, recomenda-se focar nos materiais complementares (slides e PDFs específicos sobre forense/recuperação). 

### Relação com Tanenbaum
A teoria básica do Tanenbaum que ajuda no Carving é o entendimento de que os arquivos são armazenados em blocos lógicos no disco e que arquivos binários costumam ter um formato apropriado com "números mágicos" no cabeçalho (conforme mencionado na página 185 do PDF). As ferramentas de Carving usam exatamente esses cabeçalhos (headers) e rodapés (footers) estruturados para tentar reconstruir os dados diretamente do disco, ignorando a estrutura corrompida do sistema de arquivos.
