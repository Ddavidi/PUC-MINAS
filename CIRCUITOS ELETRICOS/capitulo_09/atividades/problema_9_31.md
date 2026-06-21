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