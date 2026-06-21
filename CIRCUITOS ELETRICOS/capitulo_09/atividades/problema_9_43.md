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