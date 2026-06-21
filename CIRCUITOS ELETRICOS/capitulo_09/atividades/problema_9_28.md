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