# FOLHA DE COLA: CAPÍTULO 11 (POTÊNCIA C.A. E CARGAS PARALELAS)
*(Resumo focado para resolver a Questão 4 da Prova: Soma de Cargas)*

---

## 1. FÓRMULAS MÁGICAS DA POTÊNCIA
A relação entre as potências é dada pela equação da **Potência Complexa (S)**:
$$ \mathbf{S} = P + jQ \quad \text{(Forma Retangular)} $$
$$ \mathbf{S} = |S| \angle \theta \quad \text{(Forma Polar)} $$

Desmembrando as fórmulas:
- **S (Aparente - VA):** Hipotenusa $\to S = \sqrt{P^2 + Q^2}$ ou $S = \frac{P}{FP}$
- **P (Ativa - W):** Parte Real $\to P = S \cdot \cos(\theta)$
- **Q (Reativa - VAr):** Parte Imaginária $\to Q = S \cdot \sin(\theta)$ ou $Q = P \cdot \tan(\theta)$
- **FP (Fator de Potência):** $\to FP = \cos(\theta) = \frac{P}{S}$

## 2. A REGRA DE OURO DOS SINAIS DO $Q$
Na equação $S = P + jQ$, errar o sinal do $Q$ zera a sua questão:
- **INDUTIVO (Motores):** O $Q$ é **Positivo** ($+Q$). O Fator de Potência é Indutivo. A corrente *atrasa*.
- **CAPACITIVO (Capacitores):** O $Q$ é **Negativo** ($-Q$). O Fator de Potência é Capacitivo. A corrente *adianta*.

## 3. COMO DESENHAR O TRIÂNGULO NA PROVA
Use os resultados do cálculo final para desenhar na folha:
1. **O Chão (Eixo X):** Desenhe uma reta horizontal sempre para a **direita**, marcando o valor do seu $P$. 
   *(Dica: Para cargas que consomem energia, o $P$ é **sempre positivo**. Ele só seria negativo e apontaria para a esquerda se a sua máquina fosse um gerador devolvendo energia para a rede!)*
2. **A Parede (Eixo Y):** Na ponta dessa reta horizontal, puxe uma linha vertical para o $Q$. 
   - Se o seu $Q$ final for **Positivo**, a linha tem que apontar para **CIMA**.
   - Se o seu $Q$ final for **Negativo**, a linha tem que apontar para **BAIXO**.
3. **O Telhado (Aparente):** Feche o triângulo ligando a origem até a ponta final da linha do $Q$. Essa diagonal é o seu $S$.
4. **O Ângulo ($\theta$):** Escreva o ângulo que você achou lá no biquinho onde você começou o desenho, encostado na linha do $P$.

---

## 4. A RECEITA DE BOLO (CARGAS EM PARALELO)
Se a prova colocar várias máquinas ligadas juntas (Carga 1, Carga 2...), você NUNCA pode somar o $S$ direto. Siga sempre os 4 passos:

### Passo 1: Desmontar cada máquina
Para a **Carga 1**, encontre obrigatoriamente o seu $P_1$ e seu $Q_1$.
Para a **Carga 2**, encontre obrigatoriamente o seu $P_2$ e seu $Q_2$.
*(Se o professor não te der o Q direto, ele vai te dar o FP. Faça $\theta = \arccos(FP)$ e depois use $Q = P \cdot \tan(\theta)$ ou $Q = S \cdot \sin(\theta)$).*
**IMPORTANTE:** Coloque o sinal de $-$ no $Q$ se estiver escrito "Capacitivo".

### Passo 2: O Liquidificador (A Soma)
Some Banana com Banana e Maçã com Maçã:
- **Ativa Total:** $P_{total} = P_1 + P_2$
- **Reativa Total:** $Q_{total} = Q_1 + Q_2$ *(cuidado com as subtrações devido aos sinais!)*

### Passo 3: O Gran Finale na Casio
O seu Fasor de Potência Total ficou assim: $\mathbf{S_{total}} = P_{total} + jQ_{total}$.
Jogue isso na calculadora e peça a resposta em Polar!

### Passo 4: Como responder na folha de prova
A calculadora vai te dar a resposta no formato: **$S \angle \theta^\circ$**.
- O **Módulo** ($S$) é a resposta da Potência Aparente Total.
- Tire o **Cosseno do Ângulo** ($\cos(\theta)$) na calculadora para achar o Fator de Potência Total (FP).
- Se o $\theta$ for positivo, escreva "FP Indutivo". Se for negativo, escreva "FP Capacitivo".

---

> [!TIP]
> **GUIA DE SOBREVIVÊNCIA - CASIO FX-991LA CW:**
> 1. Para achar o $\theta$ a partir do FP: `SHIFT` + `cos` (para fazer $\arccos$) e digite o valor.
> 2. No final, com as potências totais somadas, vá no aplicativo `Complexo`.
> 3. Digite o Retangular (Ex: `6700 + 972.8i`). Lembre que o `i` fica em `SHIFT` + `0`.
> 4. Aperte `FORMAT` $\to$ `Polar Coord`. 
> 5. A calculadora te entregará o $S$ e o ângulo prontos!
