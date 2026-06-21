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