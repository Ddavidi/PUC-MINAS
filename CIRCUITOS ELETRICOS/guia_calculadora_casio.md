# Guia Definitivo: Casio fx-991LA CW em Circuitos Elétricos

A **Casio fx-991LA CW (ClassWiz)** é uma das calculadoras científicas mais modernas e potentes do mercado. Dominar os aplicativos dela vai te poupar horas de prova e zerar os seus erros de sinal.

Abaixo estão os guias para você sobreviver às provas de Circuitos usando todo o potencial da sua calculadora.

---

## 1. Resolvendo Sistemas de Equações Nodal / Malhas (Números Reais)
Para a sua primeira prova (Capítulos 3 e 4), os circuitos lidam com corrente contínua (CC), então todos os coeficientes são números reais.

**Passo a Passo na Calculadora:**
1. Ligue a calculadora e aperte a tecla **`HOME`** (com o ícone da casinha).
2. Usando as setas, navegue até o aplicativo **`Equação`** (ou *Equation* dependendo do idioma) e aperte **`OK`**.
3. Selecione a opção **`Sist linear`** (ou *Simul Equation*).
4. A calculadora perguntará o **Número de incógnitas**. Selecione **`3`** (para circuitos com $V_1, V_2, V_3$).
5. Você verá na tela uma matriz vazia com as letras $x, y, z$ (que representam nossas tensões) e os coeficientes $a, b, c, d$.
6. Basta digitar os coeficientes que você montou na sua matriz (ou deduziu das equações) um por um, apertando **`EXE`** para confirmar cada número e pular para o próximo quadradinho.
7. Quando preencher a última linha, aperte **`EXE`** mais uma vez.
8. Pronto! Ela te dará os valores de $x$ ($V_1$), aperte `seta para baixo` para ver o $y$ ($V_2$) e o $z$ ($V_3$).
> **Dica:** Se o resultado der em fração (ex: $238/13$) e você quiser em decimal, aperte a tecla **`FORMAT`** e selecione "Decimal".

---

## 2. A Armadilha do Capítulo 9 (Fasores e Números Complexos)
Na sua segunda prova, a Análise Nodal será feita com Corrente Alternada, o que significa que os seus resistores, capacitores e indutores virarão **Números Complexos** (ex: $3 + 4i$).

> [!WARNING]
> **A Grande Limitação da Casio:**
> O aplicativo `Equação` da fx-991LA CW **NÃO ACEITA** que você digite a letra $i$ (número complexo) dentro da matriz do sistema. Ela dará erro!

**Como resolver sistemas Nodal com números complexos na Casio?**
Como a calculadora não resolve a matriz complexa inteira de uma vez por você, você precisará trabalhar dentro do aplicativo **`Complexo`** (ou *Complex*).

**O Caminho Seguro:**
1. Aperte **`HOME`** e vá no aplicativo **`Complexo`**.
2. Neste aplicativo você pode apertar **`SHIFT`** e depois o número **`0`** (onde tem o $i$ em amarelo) para colocar o número imaginário nas contas.
3. Se você usar Análise Nodal em CA e chegar em um sistema $2x2$, a forma mais segura é fazer por **Substituição** na mão: isole o $V_1$ na primeira equação e digite todo o cálculo gigantesco substituindo no $V_2$ usando a calculadora para fazer as multiplicações/divisões de parênteses com $i$.
4. **Outra alternativa é a Regra de Cramer**: Você calcula o Determinante Principal ($\Delta$) multiplicando cruzado e diminuindo, guarda na memória. Depois calcula o Determinante de $V_1$ ($\Delta V_1$) substituindo a coluna dos resultados e guarda na memória. A resposta é $V_1 = \Delta V_1 / \Delta$. A calculadora resolve as multiplicações cruzadas de complexos em segundos.

---

## 3. Como usar Formato Polar ($A \angle \theta$)
Em Fasores (Capítulos 9 e 11), os professores vão dar valores como $10 \angle 30^\circ$ V. 
1. Dentro do aplicativo **`Complexo`**, para digitar o símbolo de ângulo ($\angle$), aperte **`SHIFT`** e depois a tecla **`ENG`** (ou a tecla de símbolo de ângulo que fica acima do número 7/8 dependendo da versão regional da sua CW).
2. Para transformar de Retangular ($3 + 4i$) para Polar ($5 \angle 53^\circ$):
   - Digite `3 + 4i` e aperte `EXE`.
   - Aperte a tecla **`FORMAT`** (ou **`TOOLS`**) e procure a conversão para **$r \angle \theta$**.
   - Aperte `EXE` e a mágica acontece.
