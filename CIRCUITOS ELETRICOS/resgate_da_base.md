# 🚑 Resgate da Base Teórica (Capítulos 1 a 4)

Se você não dominar os três tópicos abaixo, vai ser muito difícil sobreviver aos Capítulos 7 (Transientes) e 10 (Análise Nodal em CA). Este é o seu manual de sobrevivência, focado nas maiores "dores" dos estudantes.

---

## 1. Análise Nodal (Capítulo 3)
A Análise Nodal usa a **Lei de Kirchhoff dos Nós (LKC)**. A regra é: A soma das correntes que entram = A soma das correntes que saem.

**A Receita de Bolo Definitiva:**
![Exemplo de Análise Nodal](/c:/Users/DD/Documents/DD/PUC%20MINAS/PUC-MINAS/CIRCUITOS%20ELETRICOS/_base_dados_ia/imagens_geradas/nodal_ex.png)

1. **Escolha o Chão (Referência):** Olhe para o circuito e escolha o nó de baixo (ou o nó que conecta mais componentes) para ser o seu Terra ($0 \, V$).
2. **Batize os outros Nós:** Dê nomes para as tensões dos outros nós principais (Ex: $V_1, V_2$). **O seu objetivo inteiro é descobrir o valor numérico de $V_1$ e $V_2$!**
3. **Assuma que todo mundo foge:** Em cada nó, assuma que as correntes sempre estão SAINDO dele.
4. **Traduza as correntes:** Use a Lei de Ohm ($I = V/R$) para escrever as correntes saindo em função das tensões dos nós.
   - Fórmula chave: `I_saindo = (V_Meu_Nó - V_Outro_Nó) / R`
5. **Monte a Equação:** Some todas as correntes traduzidas do nó e iguale a Zero.
   - Exemplo no nó $V_1$: $\frac{V_1 - 0}{R_1} + \frac{V_1 - V_2}{R_2} - 5A = 0$ *(Atenção: Se tem uma fonte de corrente apontando PARA DENTRO do nó, coloque como negativo ou jogue direto para o lado direito do sinal de igual!)*
6. Resolva o sistema linear.

**💥 O que ferra na prova (Supernó):**
Se existir uma **fonte de tensão** pendurada entre os nós $V_1$ e $V_2$ (e nenhum deles é o Terra), você não consegue escrever a corrente dela. A solução?
Crie um "Supernó" englobando $V_1$ e $V_2$ numa bolha só, e escreva a LKC para a bolha inteira. Depois, use a equação da própria fonte: $V_1 - V_2 = V_{fonte}$.

---

## 2. Análise de Malhas (Capítulo 3)
Enquanto a Nodal usa os nós (LKC), as Malhas usam as "janelas" do circuito e a **Lei de Kirchhoff das Malhas (LKT)**: A soma das tensões numa malha fechada é zero.

**A Receita de Bolo Definitiva:**
![Exemplo de Análise de Malhas](/c:/Users/DD/Documents/DD/PUC%20MINAS/PUC-MINAS/CIRCUITOS%20ELETRICOS/_base_dados_ia/imagens_geradas/malhas_ex.png)

1. **Desenhe os furacões:** Em cada "janela" livre do circuito, desenhe uma corrente rodando no sentido horário (Ex: $i_1, i_2$). **O seu objetivo inteiro é descobrir o valor dessas correntes.**
2. **Ande na Malha:** Comece num canto inferior e dê a volta no sentido horário, somando as quedas de tensão.
   - Ao passar por uma Bateria/Fonte: Pegue o sinal da placa que você bater primeiro. (Ex: Bateu no traço menor/negativo primeiro? Escreva $-12V$).
   - Ao passar por um Resistor: A queda de tensão é sempre $+ R \cdot i_{minhamalha}$.
3. **Resistores Compartilhados:** Se um resistor estiver na fronteira entre a sua malha 1 e a malha 2 vizinha, a corrente efetiva nele é uma "guerra" entre as duas.
   - A queda fica: $+ R \cdot (i_{minhamalha} - i_{vizinha})$.
4. Igualou tudo a zero? Resolva o sistema.

**💥 O que ferra na prova (Supermalha):**
Se existir uma **fonte de corrente** compartilhada entre a malha 1 e a malha 2, você não sabe qual é a tensão sobre ela!
A solução? Arranque ela dali mentalmente, fundindo a malha 1 e 2 num "caminhão grandão" (Supermalha) e ande pela borda externa de tudo. Depois, use a equação da própria fonte: $i_1 - i_2 = I_{fonte}$.

---

## 3. Teorema de Thevenin (Capítulo 4)
Todo circuito, por mais feio, monstruoso e complexo que seja, pode ser simplificado em apenas duas coisas ligadas em série:
- Uma **Fonte de Tensão** ($V_{th}$)
- Uma **Resistência** ($R_{th}$)

Isso salva vidas no **Capítulo 7**, onde você precisa reduzir o circuito inteiro para saber como ele afeta um único Capacitor ou Indutor.

**A Receita de Bolo Definitiva (Como achar a Rth e Vth):**

Você vai focar em dois terminais abertos (ex: os terminais onde estava o capacitor). Chame-os de $A$ e $B$.

**Parte 1: Achando a Resistência de Thevenin ($R_{th}$)**
1. **Desligue a Força:** Zere TODAS as fontes independentes do circuito.
   - Fonte de Tensão ($V$) $\implies$ Vira um Fio Liso (Curto-Circuito).
   - Fonte de Corrente ($A$) $\implies$ Vira um Fio Rompido (Circuito Aberto / Apague ela).
2. Olhe pelos terminais $A$ e $B$ e calcule a resistência equivalente ($R_{eq}$) do que sobrou.
   - Essa é a sua $R_{th}$. Fim.

**Parte 2: Achando a Tensão de Thevenin ($V_{th}$)**
1. Ligue as fontes de volta.
2. Com os terminais $A$ e $B$ ainda abertos (nada conectado neles), calcule qual é a Tensão entre $A$ e $B$ usando o método que você quiser (Nodal, Malhas, Divisor de Tensão).
   - O valor medido ali no "vazio" entre A e B é o seu $V_{th}$. Fim.

*(Observação: Se o circuito tiver fontes DEPENDENTES — aquelas com formato de losango —, a Parte 1 de achar $R_{th}$ muda. Você não pode zerar as fontes dependentes! Tem que injetar uma fonte de teste de $1V$ nos terminais e medir a corrente de teste $i_0$. A $R_{th}$ será $1 / i_0$.)*
