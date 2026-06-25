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
1. Para inserir o símbolo de ângulo ($\angle$) na notação de fase:
   - Digite o valor da magnitude (ex: `10`).
   - Pressione a tecla **`CATALOG`** (localizada logo abaixo do botão direcional redondo).
   - Selecione **`Complexo`** (ou *Complex*) na lista.
   - Escolha o símbolo **$\angle$**.
   - Digite o valor do ângulo.
2. Para transformar de Retangular ($3 + 4i$) para Polar ($5 \angle 53^\circ$):
   - Digite `3 + 4i` e aperte `EXE`.
   - Aperte a tecla **`FORMAT`** (ou **`TOOLS`**) e procure a conversão para **$r \angle \theta$**.
   - Aperte `EXE` e a mágica acontece.

---

## 4. O Cuidado com Graus (Degree) vs Radianos (Radian)
No Capítulo 9, há uma grande confusão entre a Frequência Angular ($\omega$) que é medida em **rad/s**, e as Fases ($\theta$) que são dadas em **Graus ($^\circ$)**.

Na hora de fazer contas no aplicativo **Complexo** (multiplicar, dividir e somar fasores):
- Você **SEMPRE** deve manter a calculadora em **Graus (Degree)**. Os ângulos $30^\circ$, $-90^\circ$, etc. são todos em graus.
- Se a sua calculadora estiver em Radiano e você digitar $10 \angle 30$, ela achará que são 30 Radianos e o resultado sairá completamente errado.

**Como mudar a unidade na Casio fx-991LA CW:**
1. Pressione o botão **`SETTINGS`** (o botão com o ícone de uma engrenagem/ferramenta).
2. Selecione **`Config Calculadora`** (ou *Calc Settings*).
3. Selecione **`Unidade Ângulo`** (ou *Angle Unit*).
4. Vai aparecer uma lista. Selecione **`Grau`** (Degree) para trabalhar com fasores.
5. Se você realmente precisar calcular um cosseno de radianos no aplicativo normal, volte aqui e mude para **`Radiano`** (Radian).
6. Você saberá em qual modo está olhando na parte superior da tela (se tem um quadradinho com o **"D"** de Degree, ou o **"R"** de Radian).

---

## 5. Como tirar o resultado de Notação Científica ($\times 10^x$)
Se a sua calculadora está dando resultados no formato $2,65 \times 10^3$ em vez de te mostrar $2650$, ou te dando $3,768 \times 10^{-4}$ em vez de $0,0003768$, é porque ela está configurada no modo de exibição "Norm 1" ou "Sci" (Científico).

Para forçar a Casio a te mostrar os números decimais por extenso:
1. Pressione **`SETTINGS`** (botão de engrenagem).
2. Selecione **`Config Calculadora`**.
3. Selecione **`Formato Número`** (ou *Number Format*).
4. Escolha a opção **`Norm`** (Normal).
5. Ela vai te perguntar se quer `Norm 1` ou `Norm 2`. **Escolha `Norm 2`**.

> **Qual a diferença?** 
> O `Norm 1` transforma qualquer número menor que $0,01$ ou muito grande em notação científica (com o $\times 10$). O `Norm 2` tenta te mostrar a resposta sempre em número decimal normal (ex: $0,0003768$) até que o número fique ridiculamente minúsculo (menor que 9 casas decimais). Isso facilita demais a leitura dos Fasores na prova!

---

## 6. Onde está o "j" na Calculadora e Como Usar?
Na engenharia elétrica usamos a letra **"j"** para não confundir com o $i$ de corrente, mas as calculadoras usam o padrão da matemática, que é a letra **"i"**.

Você **PODE E DEVE** fazer todas as contas com o $i$ na calculadora (exceção: o aplicativo `Equação` para matrizes de sistema nodal/malhas, que bloqueia números imaginários).

**Como colocar o $i$ nas contas normais (Impedância, Soma, Multiplicação):**
1. O aplicativo atual **deve** ser o `Complexo` (Home $\to$ Complexo).
2. Para digitar o $i$, aperte o botão **`SHIFT`** e depois aperte o botão do número **`0`** (repare que tem um $i$ minúsculo pintado em amarelo em cima do zero).
3. **Exemplo de cálculo de Impedância:**
   Se você quer achar a impedância do indutor $Z_L = j \cdot 377 \cdot 0,3$:
   - Digite na Casio: `i × 377 × 0.3` e aperte `EXE`. Ela te dará o resultado direto!
4. **Exemplo de divisão complexa:**
   Se você quiser calcular a expressão $\frac{-j}{377 \times 10^{-5}}$:
   - Digite o sinal de fração. Em cima, digite `-i`. Embaixo, digite `377 × 10^-5`. Aperte `EXE`.
   - Ela vai resolver perfeitamente para você! (se der notação científica, lembre-se do Norm 2).
