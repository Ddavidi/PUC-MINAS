# 🎯 Guia de Resolução — Capítulo 9: Senoides e Fasores
### Todos os 15 problemas organizados do mais fácil ao mais difícil

---

> [!TIP]
> **Estratégia geral para resolver QUALQUER problema de circuito CA:**
> 1. Identificar **ω** (frequência angular) da fonte
> 2. Converter a fonte para **fasor** (domínio da frequência)
> 3. Converter **L** e **C** para impedâncias: Z_L = jωL, Z_C = 1/(jωC)
> 4. Resolver como se fosse **circuito CC** (com números complexos)
> 5. Converter o resultado de volta para o **domínio do tempo**

---

## 🟢 NÍVEL 1 — Conceitos Básicos (comece aqui!)

---

### Problema 9.20 — Impedância a partir de V e I *(pág. 381)*

**Enunciado:** Um circuito linear tem corrente de entrada `i = 7,5 cos(10t + 30°) A` e tensão de saída `v = 120 cos(10t + 75°) V`. Determine a impedância associada.

**Conceito necessário:** Z = V/I (Lei de Ohm fasorial)

**Resolução:**

**Passo 1** — Converter para fasores (eliminar o termo temporal):
```
I = 7,5∠30° A
V = 120∠75° V
```

**Passo 2** — Aplicar Z = V/I:
```
Z = V/I = 120∠75° / 7,5∠30°
```

**Passo 3** — Dividir em forma polar (divide magnitudes, subtrai ângulos):
```
Z = (120/7,5) ∠(75° − 30°)
Z = 16∠45° Ω
```

**Passo 4** — Converter para forma retangular (opcional):
```
Z = 16 cos(45°) + j·16 sen(45°)
Z = 11,31 + j11,31 Ω
```

> ✅ **Resposta: Z = 16∠45° Ω = (11,31 + j11,31) Ω**

> [!NOTE]
> A parte real (11,31 Ω) é resistência. A parte imaginária positiva (+j11,31 Ω) indica reatância **indutiva**.

---

### Problema 9.28 — Corrente em Resistor *(pág. 382)*

**Enunciado:** Determine a corrente que flui através de um resistor de 8 Ω conectado a uma fonte de tensão `vs = 110 cos(377t) V`.

**Conceito necessário:** V = R·I → I = V/R (para resistor, a impedância é simplesmente R)

**Resolução:**

**Passo 1** — Identificar dados:
- ω = 377 rad/s
- R = 8 Ω
- Vs = 110∠0° V (fasor)

**Passo 2** — Para o resistor: Z = R = 8 Ω (número real, sem parte imaginária!)

**Passo 3** — Calcular corrente:
```
I = V/Z = 110∠0° / 8 = 13,75∠0° A
```

**Passo 4** — Voltar ao domínio do tempo:
```
i(t) = 13,75 cos(377t) A
```

> ✅ **Resposta: i(t) = 13,75 cos(377t) A**

> [!NOTE]
> No resistor, tensão e corrente estão **em fase** (mesmo ângulo 0°). Isso sempre acontece!

---

### Problema 9.30 — Correntes em Paralelo (R ∥ C) *(pág. 382)*

**Enunciado:** Uma tensão `v(t) = 100 cos(60t + 20°) V` é aplicada a uma associação em paralelo entre um resistor de 40 kΩ e um capacitor de 50 μF. Encontre as correntes em regime estacionário no resistor e no capacitor.

**Conceito necessário:** Em paralelo, a tensão é a mesma em ambos. Calcular I = V/Z para cada elemento.

**Resolução:**

**Passo 1** — Dados:
- ω = 60 rad/s
- V = 100∠20° V
- R = 40 kΩ = 40.000 Ω
- C = 50 μF = 50 × 10⁻⁶ F

**Passo 2** — Corrente no resistor (I_R = V/R):
```
I_R = 100∠20° / 40.000 = 0,0025∠20° A = 2,5∠20° mA
```

**Passo 3** — Impedância do capacitor:
```
Z_C = 1/(jωC) = 1/(j × 60 × 50 × 10⁻⁶) = 1/(j0,003) = −j333,33 Ω
```
Em forma polar: Z_C = 333,33∠−90° Ω

**Passo 4** — Corrente no capacitor (I_C = V/Z_C):
```
I_C = 100∠20° / 333,33∠−90° = 0,3∠110° A = 300∠110° mA
```

**Passo 5** — Voltar ao domínio do tempo:
```
i_R(t) = 2,5 cos(60t + 20°) mA
i_C(t) = 300 cos(60t + 110°) mA
```

> ✅ **Resposta: i_R(t) = 2,5 cos(60t + 20°) mA; i_C(t) = 300 cos(60t + 110°) mA**

> [!TIP]
> Note que a corrente no capacitor está **adiantada 90°** em relação à tensão (20° + 90° = 110°). Isso sempre acontece no capacitor!

---

## 🟡 NÍVEL 2 — Circuitos Série com Impedância

---

### Problema 9.31 — Circuito RLC Série *(pág. 382)*

**Enunciado:** Um circuito RLC série tem R = 80 Ω, L = 240 mH e C = 5 mF. Se a tensão de entrada for `v(t) = 10 cos(2t)`, determine a corrente que flui através do circuito.

**Conceito necessário:** Impedâncias em série se somam: Z_eq = R + Z_L + Z_C. Depois I = V/Z_eq.

**Resolução:**

**Passo 1** — Dados:
- ω = 2 rad/s
- V = 10∠0° V
- R = 80 Ω, L = 240 mH = 0,24 H, C = 5 mF = 5 × 10⁻³ F

**Passo 2** — Calcular impedâncias individuais:
```
Z_R = 80 Ω
Z_L = jωL = j(2)(0,24) = j0,48 Ω
Z_C = 1/(jωC) = 1/(j × 2 × 5 × 10⁻³) = 1/(j0,01) = −j100 Ω
```

**Passo 3** — Impedância total (série = soma):
```
Z_eq = Z_R + Z_L + Z_C = 80 + j0,48 − j100 = 80 − j99,52 Ω
```

**Passo 4** — Converter para polar:
```
|Z| = √(80² + 99,52²) = √(6400 + 9904,2) = √16304,2 = 127,69 Ω
θ = arctan(−99,52/80) = −51,2°
Z_eq = 127,69∠−51,2° Ω
```

**Passo 5** — Calcular corrente:
```
I = V/Z = 10∠0° / 127,69∠−51,2° = 0,0783∠51,2° A
```

**Passo 6** — Domínio do tempo:
```
i(t) = 78,3 cos(2t + 51,2°) mA
```

> ✅ **Resposta: i(t) ≈ 78,3 cos(2t + 51,2°) mA**

---

### Problema 9.35 — Circuito com R, C e L em Série-Paralelo *(pág. 382)*

**Enunciado:** Determine a corrente `i` no circuito da Figura 9.42 quando `vs(t) = 50 cos(200t) V`.

O circuito (Figura 9.42): Fonte vs em série com R = 10 Ω. Depois, em paralelo: capacitor de 5 mF e indutor de 20 mH.

**Resolução:**

**Passo 1** — Dados:
- ω = 200 rad/s
- Vs = 50∠0° V

**Passo 2** — Impedâncias:
```
Z_R = 10 Ω
Z_C = 1/(jωC) = 1/(j × 200 × 5 × 10⁻³) = 1/j1 = −j1 Ω
Z_L = jωL = j × 200 × 20 × 10⁻³ = j4 Ω
```

**Passo 3** — Capacitor e indutor em paralelo:
```
Z_par = (Z_C × Z_L)/(Z_C + Z_L) = (−j1 × j4)/(−j1 + j4)
     = (−j² × 4)/(j3) = 4/(j3) = 4/(j3) × (−j/−j) = −j4/3
     = −j1,333 Ω
```

**Passo 4** — Impedância total (R em série com o paralelo):
```
Z_eq = Z_R + Z_par = 10 − j1,333 Ω
|Z_eq| = √(100 + 1,778) = √101,778 = 10,089 Ω
θ = arctan(−1,333/10) = −7,595°
Z_eq = 10,089∠−7,595° Ω
```

**Passo 5** — Corrente:
```
I = V/Z = 50∠0° / 10,089∠−7,595° = 4,956∠7,595° A
```

**Passo 6** — Domínio do tempo:
```
i(t) = 4,956 cos(200t + 7,595°) A
```

> ✅ **Resposta: i(t) ≈ 4,96 cos(200t + 7,6°) A**

---

### Problema Prático 9.8 — Corrente no Capacitor *(pág. 365)*

**Enunciado:** Se a tensão `v = 10 cos(100t + 30°)` for aplicada a um capacitor de 50 μF, calcule a corrente através do capacitor.

**Resolução:**

**Passo 1** — Dados: ω = 100, V = 10∠30° V, C = 50 μF

**Passo 2** — Usar I = jωC × V (relação para capacitor):
```
I = jωC · V = j(100)(50 × 10⁻⁶) × 10∠30°
  = j0,005 × 10∠30°
  = 0,005∠90° × 10∠30°
  = 0,05∠120° A = 50∠120° mA
```

**Passo 3** — Domínio do tempo:
```
i(t) = 50 cos(100t + 120°) mA
```

> ✅ **Resposta: i(t) = 50 cos(100t + 120°) mA**

---

### Problema Prático 9.9 — Circuito RL Série *(pág. 367)*

**Enunciado:** Consulte a Figura 9.17. `vs = 20 sen(10t + 30°) V`, R = 4 Ω, L = 0,2 H. Determine v(t) e i(t).

**Resolução:**

**Passo 1** — Converter seno → cosseno:
```
vs = 20 sen(10t + 30°) = 20 cos(10t + 30° − 90°) = 20 cos(10t − 60°)
Vs = 20∠−60° V,  ω = 10 rad/s
```

**Passo 2** — Impedâncias:
```
Z_R = 4 Ω
Z_L = jωL = j(10)(0,2) = j2 Ω
Z_eq = 4 + j2 Ω = √(16+4)∠arctan(2/4) = √20∠26,57° = 4,472∠26,57° Ω
```

**Passo 3** — Corrente:
```
I = Vs/Z_eq = 20∠−60° / 4,472∠26,57° = 4,472∠−86,57° A
```

**Passo 4** — Tensão no indutor (V = Z_L × I):
```
V = j2 × 4,472∠−86,57° = 2∠90° × 4,472∠−86,57°
  = 8,944∠3,43° V
```

**Passo 5** — Domínio do tempo (lembrando que a entrada era seno, convertemos para seno na saída):
```
i(t) = 4,472 sen(10t − 86,57° + 90°) = 4,472 sen(10t + 3,43°) A
v(t) = 8,944 sen(10t + 3,43° + 90°) = 8,944 sen(10t + 93,43°) V
```

> ✅ **Resposta: v(t) = 8,944 sen(10t + 93,43°) V; i(t) = 4,472 sen(10t + 3,43°) A**

---

### Problema Prático 9.10 — Impedância de Entrada *(pág. 372)*

**Enunciado:** Determine a impedância de entrada do circuito da Figura 9.24 com ω = 10 rad/s.
Circuito: C₁ = 1 mF em série com [R₁ = 100 Ω em série com (indutor de 8 H em paralelo com {R₂ = 200 Ω em série com C₂ = 1 mF})].

**Resolução:**

**Passo 1** — Impedâncias (ω = 10):
```
Z_C1 = 1/(j × 10 × 1 × 10⁻³) = 1/(j0,01) = −j100 Ω
Z_R1 = 100 Ω
Z_L = j × 10 × 8 = j80 Ω
Z_R2 = 200 Ω
Z_C2 = 1/(j × 10 × 1 × 10⁻³) = −j100 Ω
```

**Passo 2** — R₂ em série com C₂:
```
Z_a = 200 − j100 Ω
```

**Passo 3** — Z_a em paralelo com Z_L:
```
Z_b = (Z_L × Z_a)/(Z_L + Z_a) = (j80)(200 − j100)/(j80 + 200 − j100)
    = (j80)(200 − j100)/(200 − j20)
```
Numerador: j80 × (200 − j100) = j16000 − j²8000 = 8000 + j16000
Denominador: 200 − j20

Convertendo para polar:
```
Num = 8000 + j16000 → |N| = √(64M + 256M) = √320M = 17889; θ = arctan(2) = 63,43°
Den = 200 − j20 → |D| = √(40000 + 400) = 201; θ = −5,71°
Z_b = 17889∠63,43° / 201∠−5,71° = 89∠69,14°
    = 89 cos(69,14°) + j89 sen(69,14°) = 31,62 + j83,2 ≈ (31,52 + j83,2) Ω  
```

Refazendo com mais precisão:
```
Num = (j80)(200 − j100) = j16000 + 8000 = 8000 + j16000
Den = 200 − j20

Z_b = (8000 + j16000)/(200 − j20)
    
Multiplicando por conjugado:
= (8000 + j16000)(200 + j20) / (200² + 20²)
= (1600000 + j160000 + j3200000 + j²320000) / (40400)
= (1600000 − 320000 + j(160000 + 3200000)) / 40400
= (1280000 + j3360000) / 40400
= 31,68 + j83,17 Ω
```

**Passo 4** — Impedância de entrada (tudo em série):
```
Z_ent = Z_C1 + Z_R1 + Z_b
      = −j100 + 100 + 31,68 + j83,17
      = 131,68 − j16,83 Ω
```

Hmm, a resposta do livro é (149,52 − j195) Ω. Deixe-me reanalisar o circuito pela figura...

Olhando a Figura 9.24 novamente: parece que C₁ (1 mF) está em série com R₁ (100 Ω), e depois temos a combinação de (8H em série com C₂ = 1 mF) em paralelo com R₂ = 200 Ω.

**Refazendo:**
```
Z_C1 = −j100 Ω
Z_R1 = 100 Ω  
Z_L = j80 Ω
Z_C2 = −j100 Ω
Z_R2 = 200 Ω
```

Ramo superior: Z_L em série com Z_C2 = j80 − j100 = −j20 Ω
Paralelo com R₂: Z_par = (−j20 × 200)/(−j20 + 200) = −j4000/(200 − j20)

```
= −j4000(200 + j20)/(200² + 20²)
= (−j800000 − j²80000)/40400
= (80000 − j800000)/40400
= 1,98 − j19,8 Ω
```

Nope, ainda não bate. Olhando a figura mais cuidadosamente, a topologia é:
- C₁ = 1 mF (em cima, horizontal)
- R₁ = 100 Ω em série com L = 8H (ramo superior)
- R₂ = 200 Ω em paralelo com C₂ = 1 mF (ramo inferior)

Z_ramo_sup = R₁ + Z_L = 100 + j80 Ω
Z_ramo_inf = R₂ ∥ Z_C2 = (200)(−j100)/(200 − j100) = −j20000/(200 − j100)

```
= −j20000(200 + j100)/(200² + 100²)
= (−j4000000 − j²2000000)/50000
= (2000000 − j4000000)/50000
= 40 − j80 Ω
```

Paralelo dos dois ramos:
```
Z_par = Z_sup ∥ Z_inf = ((100+j80)(40−j80))/((100+j80)+(40−j80))
= ((100+j80)(40−j80))/140
```
Num: (100)(40) + (100)(−j80) + j80(40) + j80(−j80)
= 4000 − j8000 + j3200 + 6400 = 10400 − j4800

Z_par = (10400 − j4800)/140 = 74,29 − j34,29 Ω

Z_ent = Z_C1 + Z_par = −j100 + 74,29 − j34,29 = 74,29 − j134,29 Ω

Ainda não bate exatamente... A topologia exata pode ser diferente do que interpreto. Vou deixar a explicação do método e indicar a resposta do livro.

> ✅ **Resposta (do livro): Z_ent = (149,52 − j195) Ω**

> [!NOTE]
> **Método**: Calcule a impedância de cada componente, depois combine usando regras de série (soma) e paralelo (produto/soma). A topologia exata do circuito na Figura 9.24 deve ser consultada para a conexão correta.

---

### Problema Prático 9.11 — Divisão de Tensão *(pág. 372)*

**Enunciado:** Calcule vo no circuito da Figura 9.27: fonte `50 cos(10t + 30°)`, em série com indutor de 0,5 H e resistor de 10 Ω, com capacitor de 1/20 F em paralelo com R. A saída vo é no capacitor.

**Resolução:**

**Passo 1** — Dados (ω = 10):
```
Vs = 50∠30° V
Z_L = jωL = j(10)(0,5) = j5 Ω
Z_R = 10 Ω
Z_C = 1/(jωC) = 1/(j × 10 × 1/20) = 1/(j0,5) = −j2 Ω
```

**Passo 2** — R em paralelo com C:
```
Z_par = (Z_R × Z_C)/(Z_R + Z_C) = (10)(−j2)/(10 − j2)
      = −j20/(10 − j2)
```
Multiplicando pelo conjugado:
```
= −j20(10 + j2)/(100 + 4) = (−j200 − j²40)/104
= (40 − j200)/104 = 0,385 − j1,923 Ω
```

Hmm, vou usar outra abordagem. Olhando a Figura 9.27: L = 0,5 H em série com a fonte, R = 10 Ω em série, C = 1/20 F com vo medido no capacitor.

Na verdade, pela figura, parece ser L em série, depois R em série, depois C (tudo em série). Vo é a tensão no capacitor.

**Passo 2 (revisado)** — Tudo em série:
```
Z_eq = Z_L + Z_R + Z_C = j5 + 10 − j2 = 10 + j3 Ω
|Z_eq| = √(100 + 9) = √109 = 10,44 Ω
θ = arctan(3/10) = 16,7°
```

**Passo 3** — Corrente:
```
I = Vs/Z_eq = 50∠30° / 10,44∠16,7° = 4,79∠13,3° A
```

**Passo 4** — Tensão no capacitor (divisão de tensão):
```
Vo = (Z_C / Z_eq) × Vs = (−j2 / (10 + j3)) × 50∠30°
   = (2∠−90° / 10,44∠16,7°) × 50∠30°
   = 0,1916∠−106,7° × 50∠30°
   = 9,58∠−76,7° V
```

Hmm, a resposta do livro dá 35,36 cos(10t − 105°) V. Vou reverificar a figura.

Olhando a Figura 9.27 de novo: a fonte é `50 cos(10t + 30°)`, L = 0,5 H está no topo, R = 10 Ω está em um ramo, e C = 1/20 F está em outro ramo, com vo medido no capacitor. Parece que R e C estão em **paralelo** (não em série).

**Passo 2 (re-revisado)** — R ∥ C:
```
Z_par = (10 × (−j2))/(10 − j2) = −j20/(10 − j2)
      = −j20(10 + j2)/(104) = (40 − j200)/104
      = 0,3846 − j1,923 Ω
      = 1,961∠−78,69° Ω
```

**Passo 3** — Impedância total: Z_L + Z_par:
```
Z_eq = j5 + 0,3846 − j1,923 = 0,3846 + j3,077
     = 3,101∠82,87° Ω
```

**Passo 4** — Vo por divisão de tensão:
```
Vo = (Z_par/Z_eq) × Vs = (1,961∠−78,69° / 3,101∠82,87°) × 50∠30°
   = 0,6324∠−161,56° × 50∠30°
   = 31,62∠−131,56° V
```

Ainda não bate exatamente. A configuração exata na figura importa muito. A resposta do livro é:

> ✅ **Resposta (do livro): vo(t) = 35,36 cos(10t − 105°) V**

> [!IMPORTANT]
> **Lição importante:** A topologia do circuito (como os componentes estão conectados) é CRUCIAL. Sempre consulte a figura do circuito para identificar o que está em série e o que está em paralelo.

---

## 🟠 NÍVEL 3 — Circuitos com Análise Mais Elaborada

---

### Problema 9.39 — Impedância Equivalente com Múltiplos Elementos *(pág. 383)*

**Enunciado:** Para o circuito da Figura 9.46, determine Z_eq e use para determinar I. Considere ω = 10 rad/s. Fonte: `12∠0° V`.

Circuito (Figura 9.46): Fonte 12∠0° em série com [4Ω + j20Ω + (−j14Ω em paralelo com {16Ω em série com j25Ω})].

**Resolução:**

**Passo 1** — Da Figura 9.46, identificamos:
```
Z₁ = 4 Ω (resistor)
Z₂ = j20 Ω (indutor)  
Z₃ = −j14 Ω (capacitor)
Z₄ = 16 Ω (resistor)
Z₅ = j25 Ω (indutor)
```

**Passo 2** — Z₄ em série com Z₅:
```
Z_a = 16 + j25 Ω
```

**Passo 3** — Z_a em paralelo com Z₃:
```
Z_b = (Z₃ × Z_a)/(Z₃ + Z_a)
    = (−j14)(16 + j25)/(−j14 + 16 + j25)
    = (−j224 − j²350)/(16 + j11)
    = (350 − j224)/(16 + j11)
```

Convertendo:
```
Num = 350 − j224 → 415,5∠−32,6°
Den = 16 + j11 → 19,42∠34,5°
Z_b = 415,5∠−32,6° / 19,42∠34,5° = 21,4∠−67,1°
    = 8,33 − j19,7 Ω
```

**Passo 4** — Impedância total:
```
Z_eq = Z₁ + Z₂ + Z_b = 4 + j20 + 8,33 − j19,7
     = 12,33 + j0,3 Ω ≈ 12,33∠1,39° Ω
```

**Passo 5** — Corrente:
```
I = V/Z_eq = 12∠0° / 12,33∠1,39° = 0,973∠−1,39° A
```

> ✅ **Resposta: Z_eq ≈ 12,33 + j0,3 Ω; I ≈ 0,973∠−1,39° A**

---

### Problema 9.40 — Corrente em Função de ω *(pág. 383)*

**Enunciado:** No circuito da Figura 9.47, determine io quando: (a) ω = 1 rad/s; (b) ω = 5 rad/s; (c) ω = 10 rad/s.

Circuito: Fonte `4 cos(ωt) V` em série com R = 2 Ω. Em paralelo: C = 0,05 F e L = 1 H.

**Resolução para (a) ω = 1 rad/s:**

**Passo 1** — Impedâncias:
```
Z_R = 2 Ω
Z_C = 1/(jωC) = 1/(j × 1 × 0,05) = 1/(j0,05) = −j20 Ω
Z_L = jωL = j × 1 × 1 = j1 Ω
```

**Passo 2** — C ∥ L:
```
Z_par = (−j20 × j1)/(−j20 + j1) = (−j²20)/(−j19) = 20/(−j19)
      = 20/(19∠−90°) = 1,053∠90° = j1,053 Ω
```

**Passo 3** — Impedância total:
```
Z_eq = 2 + j1,053 = 2,26∠27,8° Ω
```

**Passo 4** — Corrente total:
```
I = 4∠0° / 2,26∠27,8° = 1,77∠−27,8° A
```

**Passo 5** — io é a corrente no indutor (divisão de corrente):
```
io = I × Z_C/(Z_C + Z_L) = 1,77∠−27,8° × (−j20)/(−j20 + j1)
   = 1,77∠−27,8° × (−j20)/(−j19)
   = 1,77∠−27,8° × 20/19
   = 1,863∠−27,8° A
```

```
io(t) = 1,863 cos(t − 27,8°) A
```

> O mesmo método se aplica para (b) ω = 5 e (c) ω = 10, apenas recalculando as impedâncias!

**Para (b) ω = 5:**
```
Z_C = 1/(j5 × 0,05) = −j4 Ω
Z_L = j5 Ω
Z_par = (−j4)(j5)/(−j4 + j5) = 20/j1 = −j20 Ω
Z_eq = 2 − j20 = 20,1∠−84,3° Ω
I = 4∠0° / 20,1∠−84,3° = 0,199∠84,3° A
io = I × Z_C/(Z_C + Z_L) = 0,199∠84,3° × (−j4)/j = 0,199∠84,3° × 4∠−180°
   = 0,796∠−95,7° A → io(t) = 0,796 cos(5t − 95,7°) A
```

**Para (c) ω = 10:**
```
Z_C = 1/(j10 × 0,05) = −j2 Ω
Z_L = j10 Ω
Z_par = (−j2)(j10)/(−j2 + j10) = 20/(j8) = −j2,5 Ω
Z_eq = 2 − j2,5 = 3,2∠−51,3° Ω
I = 4∠0° / 3,2∠−51,3° = 1,25∠51,3° A
io = I × Z_C/(Z_C + Z_L) = 1,25∠51,3° × (−j2)/(j8)
   = 1,25∠51,3° × 0,25∠−180° = 0,3125∠−128,7° A
→ io(t) = 0,3125 cos(10t − 128,7°) A
```

> ✅ **Respostas:**
> - **(a)** io ≈ 1,86 cos(t − 27,8°) A
> - **(b)** io ≈ 0,80 cos(5t − 95,7°) A
> - **(c)** io ≈ 0,31 cos(10t − 128,7°) A

---

### Problema 9.42 — Divisão de Tensão em Circuito Misto *(pág. 383)*

**Enunciado:** Calcule vo(t) no circuito da Figura 9.49.
Fonte: `60 sen(200t) V`, R₁ = 30 Ω em série com [R₂ = 50 Ω em paralelo com (L = 0,1 H em série com C = 50 μF)]. Saída vo em R₂.

**Resolução:**

**Passo 1** — Converter para cosseno e fasor:
```
vs = 60 sen(200t) = 60 cos(200t − 90°)
Vs = 60∠−90° V, ω = 200
```

**Passo 2** — Impedâncias:
```
Z_R1 = 30 Ω
Z_R2 = 50 Ω
Z_L = j(200)(0,1) = j20 Ω
Z_C = 1/(j × 200 × 50 × 10⁻⁶) = 1/(j0,01) = −j100 Ω
```

**Passo 3** — L em série com C:
```
Z_LC = j20 − j100 = −j80 Ω
```

**Passo 4** — R₂ em paralelo com Z_LC:
```
Z_par = (50 × (−j80))/(50 − j80) = −j4000/(50 − j80)
```
Multiplicando pelo conjugado:
```
= −j4000(50 + j80)/(2500 + 6400)
= (−j200000 + 320000)/8900
= 35,96 − j22,47 Ω = 42,4∠−32° Ω
```

**Passo 5** — Vo por divisão de tensão:
```
Vo = (Z_par/(Z_R1 + Z_par)) × Vs
   = (42,4∠−32°)/(30 + 35,96 − j22,47) × 60∠−90°
   = (42,4∠−32°)/(65,96 − j22,47) × 60∠−90°
```
Denominador: |den| = √(65,96² + 22,47²) = √(4351 + 505) = √4856 = 69,7
θ = arctan(−22,47/65,96) = −18,8°

```
Vo = (42,4∠−32° / 69,7∠−18,8°) × 60∠−90°
   = 0,608∠−13,2° × 60∠−90°
   = 36,5∠−103,2° V
```

**Passo 6** — Domínio do tempo:
```
vo(t) = 36,5 cos(200t − 103,2°) V
```

> ✅ **Resposta: vo(t) ≈ 36,5 cos(200t − 103,2°) V**

---

### Problema 9.43 — Determinar Corrente com Impedâncias Complexas *(pág. 383)*

**Enunciado:** Determine Io no circuito da Figura 9.50.
Fonte: `60∠0° V`, em série com [50 Ω em série com (j80 Ω)], em paralelo com [100 Ω em série com (−j40 Ω)]. Io passa pelo ramo de 100 Ω.

**Resolução:**

**Passo 1** — Impedâncias dos ramos:
```
Ramo 1: Z₁ = 50 + j80 Ω (R + indutor)
Ramo 2: Z₂ = 100 − j40 Ω (R + capacitor)
```

**Passo 2** — Os dois ramos estão em paralelo, alimentados pela fonte 60∠0° V.

Como a tensão é a mesma em ambos os ramos (paralelo):
```
Io = V/Z₂ = 60∠0° / (100 − j40)
```

**Passo 3** — Converter denominador para polar:
```
|Z₂| = √(100² + 40²) = √(10000 + 1600) = √11600 = 107,7 Ω
θ = arctan(−40/100) = −21,8°
Z₂ = 107,7∠−21,8° Ω
```

**Passo 4** — Calcular Io:
```
Io = 60∠0° / 107,7∠−21,8° = 0,557∠21,8° A
```

> ✅ **Resposta: Io = 0,557∠21,8° A ≈ 557∠21,8° mA**

---

## 🔴 NÍVEL 4 — Circuitos Mais Complexos

---

### Problema 9.64 — Impedância Total e Corrente (Série-Paralelo) *(pág. 385)*

**Enunciado:** Determine Z_T e I no circuito da Figura 9.71.
Fonte: `30∠90° V`. Circuito: 4 Ω em série com 6 Ω, depois (−j10 Ω em paralelo com j8 Ω).

**Resolução:**

**Passo 1** — Da Figura 9.71:
- Ramo série: 4 Ω + (−j10 Ω) = 4 − j10 Ω
- Em paralelo com: 6 Ω + j8 Ω

Espera, olhando a figura mais cuidadosamente:
- Fonte 30∠90° V
- Em série: 4 Ω e 6 Ω no topo
- −j10 Ω e j8 Ω nas laterais

Pela Figura 9.71: parece que (4 Ω em série com −j10 Ω) está em paralelo com (6 Ω em série com j8 Ω).

**Passo 2** — Impedâncias dos ramos:
```
Z_a = 4 − j10 Ω → |Z_a| = √(16+100) = √116 = 10,77∠−68,2° Ω
Z_b = 6 + j8 Ω → |Z_b| = √(36+64) = √100 = 10∠53,13° Ω
```

**Passo 3** — Paralelo:
```
Z_T = (Z_a × Z_b)/(Z_a + Z_b)
    = ((4−j10)(6+j8))/(4−j10+6+j8)
    = ((4−j10)(6+j8))/(10−j2)
```

Numerador: (4)(6) + (4)(j8) + (−j10)(6) + (−j10)(j8)
= 24 + j32 − j60 + j²(−80) → CUIDADO: (−j10)(j8) = −j²80 = +80
= 24 + j32 − j60 + 80 = 104 − j28

```
Z_T = (104 − j28)/(10 − j2)
```

Multiplicando pelo conjugado:
```
= (104 − j28)(10 + j2)/(100 + 4)
= (1040 + j208 − j280 − j²56)/104
= (1040 + 56 + j(208−280))/104
= (1096 − j72)/104
= 10,54 − j0,692 Ω
≈ 10,56∠−3,76° Ω
```

**Passo 4** — Corrente:
```
I = V/Z_T = 30∠90° / 10,56∠−3,76° = 2,84∠93,76° A
```

> ✅ **Resposta: Z_T ≈ 10,54 − j0,69 Ω; I ≈ 2,84∠93,8° A**

---

### Problema 9.65 — Circuito com Divisão de Tensão *(pág. 385)*

**Enunciado:** Determine Z_T e I no circuito da Figura 9.72.
Fonte: `120∠10° V`. Circuito: 2 Ω em série com [ramo 1: (3 Ω + j4 Ω) em paralelo com ramo 2: (4 Ω + (−j6 Ω))].

**Resolução:**

**Passo 1** — Da Figura 9.72:
```
Z₁ = 3 + j4 Ω (ramo superior)
Z₂ = 4 − j6 Ω (ramo inferior)
```

**Passo 2** — Paralelo de Z₁ e Z₂:
```
Z_par = (Z₁ × Z₂)/(Z₁ + Z₂)
      = ((3+j4)(4−j6))/(3+j4+4−j6)
      = ((3+j4)(4−j6))/(7−j2)
```

Numerador: (3)(4) + (3)(−j6) + (j4)(4) + (j4)(−j6)
= 12 − j18 + j16 − j²24 = 12 − j18 + j16 + 24 = 36 − j2

```
Z_par = (36 − j2)/(7 − j2)
```

Multiplicando pelo conjugado:
```
= (36−j2)(7+j2)/(49+4) = (252 + j72 − j14 − j²4)/53
= (252 + 4 + j(72−14))/53 = (256 + j58)/53
= 4,83 + j1,094 Ω
```

**Passo 3** — Impedância total:
```
Z_T = 2 + Z_par = 2 + 4,83 + j1,094 = 6,83 + j1,094 Ω
    = 6,917∠9,1° Ω
```

**Passo 4** — Corrente:
```
I = V/Z_T = 120∠10° / 6,917∠9,1° = 17,35∠0,9° A
```

> ✅ **Resposta: Z_T ≈ 6,83 + j1,09 Ω; I ≈ 17,35∠0,9° A**

---

## 📌 Resumo: "Receita" para Resolver Qualquer Problema

```
┌─────────────────────────────────────────────────────────┐
│  1. Leia ω da fonte (coeficiente do t)                  │
│  2. Converta a fonte para fasor                         │
│     - Se for seno: subtraia 90° → cos(x-90°)           │
│  3. Calcule impedâncias de cada componente:             │
│     R → R    L → jωL    C → 1/(jωC)                    │
│  4. Combine impedâncias:                                │
│     Série → soma    Paralelo → produto/soma             │
│  5. Use V = ZI (Lei de Ohm fasorial)                    │
│  6. Converta de volta: adicione cos(ωt + ...) ao fasor  │
└─────────────────────────────────────────────────────────┘
```

> [!TIP]
> **Dica de ouro para operações com complexos:**
> - **Soma/subtração** → use forma retangular (a + jb)
> - **Multiplicação/divisão** → use forma polar (r∠θ)
> - Multiplicar: multiplica magnitudes, soma ângulos
> - Dividir: divide magnitudes, subtrai ângulos
