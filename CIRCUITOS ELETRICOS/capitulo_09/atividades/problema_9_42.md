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