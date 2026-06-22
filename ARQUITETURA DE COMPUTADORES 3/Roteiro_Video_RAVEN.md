# Roteiro: Demonstração de Load-use Hazard (Preset D2-01) - Simulador RAVEN

**[0:00 - 0:10] Abertura**
*   **Ação na tela:** Comece a gravar já com o RAVEN aberto. Clique na aba **Activity** e carregue o preset **D2-01**.
*   **Fale:** "Olá! Sou [Seu Nome] e vou demonstrar a atividade D2 sobre Hazards de Dados usando o simulador didático RAVEN."

**[0:10 - 0:25] Contexto**
*   **Ação na tela:** Clique na aba **Pipeline**. Use o mouse para apontar para a parte esquerda da tela onde estão as instruções (você verá o `lw` e o `add` logo abaixo dele).
*   **Fale:** "Carreguei o preset D2-01. Este preset mostra um caso clássico de load-use hazard, em que uma instrução usa logo em seguida o valor carregado por um lw. Temos uma instrução 'load word' seguida imediatamente por um 'add', que precisa exatamente do valor que a instrução anterior está buscando na memória."

**[0:25 - 0:45] Execução (O clímax do vídeo)**
*   **Ação na tela:** Pressione a tecla **`s`** do seu teclado de forma pausada (cerca de 1 vez por segundo) para avançar ciclo a ciclo. Deixe o mouse perto de onde a instrução `add` está presa no diagrama.
*   **Fale:** "Avançando a execução ciclo a ciclo com a tecla 'S', observamos o fluxo no pipeline. Quando o 'add' tenta executar, ele precisa esperar. O RAVEN nos mostra claramente o hardware resolvendo esse conflito..."

**[0:45 - 1:00] Conclusão**
Quantas bolhas aparecem antes do add entrar em execução nessa primeira ocorrência?
*   **Ação na tela:** Continue apertando **`s`** até a instrução `add` seguir em frente. Aponte com o mouse para o símbolo de "bolha" (normalmente indicado por um espaço em branco ou um tracinho `──` no diagrama do pipeline).
*   **Fale:** "...inserindo automaticamente uma 'bolha' ou stall, que é este ciclo de espera aqui. O pipeline atrasa por um momento, mas garante que o programa execute sem erros. Muito obrigado!"
