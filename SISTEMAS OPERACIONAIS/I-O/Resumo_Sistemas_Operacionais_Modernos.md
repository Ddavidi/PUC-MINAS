# Resumo: I/O e Desempenho de Disco (Sistemas Operacionais Modernos - Tanenbaum)

Com base no material do livro *Sistemas Operacionais Modernos* (Tanenbaum), este resumo abrange os princípios de E/S e, fundamentalmente, **a didática de Tanenbaum para o cálculo de desempenho e tempo de leitura de discos** (assunto crítico para as questões abertas da prova).

## 1. Princípios do Hardware de E/S
A interface apresentada ao software divide os dispositivos em duas categorias principais (Cap. 5):
- **Dispositivos de Blocos:** Armazenam informações em blocos de tamanho fixo, cada um com o seu próprio endereço (Ex: HDDs, SSDs, Blu-ray). Podem ser lidos ou escritos independentemente.
- **Dispositivos de Caractere:** Enviam ou recebem um fluxo de caracteres, sem endereços e sem operação de busca (*seek*). (Ex: teclados, impressoras).

---

## 2. Contas de Desempenho de Disco (A Didática de Tanenbaum)
No capítulo 4 (página 207 do PDF), Tanenbaum fornece uma base matemática direta para calcular o tempo necessário para se ler dados de um disco magnético. 

A fórmula fundamental para ler um bloco de dados é a soma de três tempos:
**Tempo Total = Tempo de Busca + Atraso Rotacional + Tempo de Transferência**

### Passo a Passo do Cálculo (Exemplo Prático do Livro)
*Cenário do livro:* Um disco com `1 MB` por trilha, tempo de rotação de `8,33 ms` e tempo de busca de `5 ms`. Pede-se o tempo para ler um bloco de *k* bytes.

1. **Tempo de Busca (*Seek Time*):** 
   - É o tempo mecânico para mover o braço do disco até o cilindro correto.
   - O problema fornece esse valor diretamente: `5 ms`.

2. **Atraso Rotacional (*Rotational Delay*):**
   - É o tempo gasto esperando o setor desejado girar até chegar sob a cabeça de leitura.
   - Segundo a didática do Tanenbaum, usa-se o **atraso médio**, que é exatamente **a metade do tempo de uma rotação completa**.
   - No exemplo: se uma rotação completa demora `8,33 ms`, o atraso rotacional é `8,33 / 2 = 4,165 ms`.

3. **Tempo de Transferência (*Transfer Time*):**
   - É o tempo para a leitura física dos dados enquanto eles passam pela cabeça de leitura.
   - Como calcular: `(Quantidade de dados a ler / Capacidade da trilha) * Tempo de uma rotação`.
   - No exemplo: Para ler *k* bytes, sabendo que a trilha tem 1 MB (que ele simplifica para 1.000.000 de bytes na conta), o tempo de transferência é `(k / 1.000.000) * 8,33 ms`.

### A Equação Final Montada
Para ler *k* bytes no cenário acima, a equação de Tanenbaum fica:
`Tempo = 5 + 4,165 + (k / 1000000) * 8,33`

### 💡 Dica de Ouro para a Prova (Interleaving)
Siga exatamente a ordem de Tanenbaum e identifique os 3 componentes separadamente. 
Se a questão aberta envolver **Interleaving (Entrelaçamento)**, lembre-se de que o **tempo de transferência** e o **tempo total rotacional** serão afetados de forma acoplada. No entrelaçamento, os setores não são lidos consecutivamente de uma vez, mas com "pulos". Isso exige que o disco dê giros adicionais completos para ler todos os setores de uma trilha. Nessas situações, em vez da fórmula simples de transferência, você deverá contar o número de voltas necessárias para ler a trilha completa e multiplicar pelo tempo de uma rotação.
