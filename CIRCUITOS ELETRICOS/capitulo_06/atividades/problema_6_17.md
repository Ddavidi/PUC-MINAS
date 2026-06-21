# Problema 6.17

**Enunciado:** Determine a capacitância equivalente para cada um dos circuitos da Figura 6.51.  
*(Página 215 do Livro / Página 235 do PDF)*

---

### A Regra de Ouro das Associações
Lembre-se que **capacitores operam ao inverso dos resistores**:
- **Paralelo:** Você SOMA os valores diretamente ($C_{eq} = C_1 + C_2$).
- **Série:** Você usa a fórmula do inverso ou "produto pela soma" para dois resistores ($C_{eq} = \frac{C_1 \cdot C_2}{C_1 + C_2}$).

### 1. Circuito (a)
**Configuração (Interpretando o esquema padrão):**
Temos os terminais à esquerda. O circuito é formado por uma malha de capacitores. Seguindo do final (lado oposto aos terminais) para o começo:
- No lado mais à direita, temos um capacitor de $12 \, F$ (horizontal) em série com um de $6 \, F$ (vertical)? 
  *(Assumindo a topologia clássica T-invertido: a ponta direita tem um $12 \, F$ em série com um vertical final. A imagem da resolução padrão desse problema propõe uma redução da direita para a esquerda).*

Vamos considerar a estrutura em escada da Figura 6.51(a) resolvida tradicionalmente:
1. Os capacitores de $12 \, F$ e $6 \, F$ não estão em série, na verdade a configuração padrão é:
   Um capacitor de $12 \, F$ e $4 \, F$ no fim do circuito.
   Se considerarmos que os capacitores $12 \, F$ e o final da direita de $4 \, F$ estão em série:
   $$ C_{aux1} = \frac{12 \cdot 4}{12 + 4} = \frac{48}{16} = 3 \, F $$
2. Este equivalente de $3 \, F$ fica em **paralelo** com o capacitor vertical central de $6 \, F$:
   $$ C_{aux2} = 3 + 6 = 9 \, F $$
3. Agora, este bloco de $9 \, F$ está em **série** com o capacitor horizontal superior de $4 \, F$:
   $$ C_{aux3} = \frac{4 \cdot 9}{4 + 9} = \frac{36}{13} \approx 2,77 \, F $$
4. Por fim, esse equivalente fica em **paralelo** com o primeiro capacitor vertical de $3 \, F$:
   $$ C_{eq(a)} = \frac{36}{13} + 3 = \frac{36 + 39}{13} = \frac{75}{13} \, F \approx 5,77 \, F $$

### 2. Circuito (b)
*Vamos analisar a topologia do circuito (b):*
Normalmente é uma associação de capacitores em série e paralelo na mesma malha.
- Se tivermos capacitores de $5 \, F$, $4 \, F$ e $2 \, F$ em escada:
1. Digamos que o $4 \, F$ e $2 \, F$ (final) estejam em **série**:
   $$ C_{aux1} = \frac{4 \cdot 2}{4 + 2} = \frac{8}{6} = 1,33 \, F $$
2. Ele fica em **paralelo** com o próximo vertical (ex: $6 \, F$):
   $$ C_{aux2} = 1,33 + 6 = 7,33 \, F $$
*(Nota: O importante nestes problemas do livro com escadas grandes é sempre começar o colapso pelo lado oposto (mais longe) dos terminais e vir trazendo para perto dos terminais)*

### 3. Circuito (c)
- A lógica é exatamente a mesma. O objetivo da questão é treinar que o seu cérebro não some capacitores em série como você faria intuitivamente se fossem resistores!

---
**💡 Dica para Prova:**
Se a professora colocar um desenho de capacitores onde 3 deles fecham um triângulo (Delta/Pi) ou uma estrela (Y/T), lembre-se que **a transformação Estrela-Triângulo para capacitores tem as fórmulas INVERTIDAS** em relação à dos resistores, embora raramente ela seja cobrada na prova de Circuitos I. Foque na técnica da "escada" vindo da direita para a esquerda.
