# Resoluções da Lista: Alocação (Casamento Estável e Método Húngaro)

Compilação de todas as resoluções das práticas da lista relativas ao tema 4.

---

## 6.2 Gale-Shapley — Simulação Passo a Passo (Cascata)

**Enunciado:** 3 Hospitais e 3 Médicos. (Ver matrizes de preferência no PDF).

**Tabela de Propostas:**

| Rodada | Propostas Feitas | Decisões dos Revisores (Médicos) |
|---|---|---|
| 1 | H1 propõe a M1. <br> H2 propõe a M2. <br> H3 propõe a M1. | M1 aceita H1. <br> M2 aceita H2. <br> M1 recebe H3. Prefere H3 a H1. Rejeita H1 e aceita H3. |
| 2 | H1 (livre) propõe a M2. | M2 recebe H1. Prefere H1 a H2. Rejeita H2 e aceita H1. |
| 3 | H2 (livre) propõe a M1. | M1 recebe H2. Prefere H2 a H3. Rejeita H3 e aceita H2. |
| 4 | H3 (livre) propõe a M2. <br> H3 (livre) propõe a M3. | M2 prefere H1. Rejeita H3. <br> M3 aceita H3. |

*Casamento Estável final:* `{(H1, M2), (H2, M1), (H3, M3)}`.

---

## 6.3 Gale-Shapley — Simulação Estendida (4x4)

**Enunciado:** 4 Empresas (E1 a E4) e 4 Candidatos (C1 a C4).

**Tabela de Rastreio:**

| Rodada | Propostas (Livre tenta próximo) | Decisão (Aceita se melhor) |
|---|---|---|
| 1 | E1 $\rightarrow$ C1 <br> E2 $\rightarrow$ C2 <br> E3 $\rightarrow$ C1 <br> E4 $\rightarrow$ C1 | C2 aceita E2. <br> C1 recebe E1, E3, E4. A preferência de C1 é E3 > E4 > E1. C1 aceita E3 e rejeita os outros. |
| 2 | E1 (livre) $\rightarrow$ C2 <br> E4 (livre) $\rightarrow$ C4 | C4 aceita E4. <br> C2 recebe E1. C2 prefere E1. Aceita E1 e rejeita E2. |
| 3 | E2 (livre) $\rightarrow$ C1 | C1 recebe E2. C1 prefere E2 ao E3. Aceita E2 e rejeita E3. |
| 4 | E3 (livre) $\rightarrow$ C3 | C3 aceita E3. |

*Casamento Estável:* `{(E1, C2), (E2, C1), (E3, C3), (E4, C4)}`.

---

## 7.2 Método Húngaro — Passo a Passo

**Enunciado:** Minimizar custos 4x4.

**Passo 1: Redução de Linha**
Subtrair o mínimo de cada linha.
| | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| F1 | 2 | 11 | 0 | 7 |
| F2 | 3 | 11 | 0 | 10 |
| F3 | 4 | 7 | 0 | 5 |
| F4 | 4 | 11 | 0 | 10 |

**Passo 2: Redução de Coluna**
Subtrair mínimo de cada coluna (C1:2, C2:7, C3:0, C4:5).
| | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| F1 | 0 | 4 | 0 | 2 |
| F2 | 1 | 4 | 0 | 5 |
| F3 | 2 | 0 | 0 | 0 |
| F4 | 2 | 4 | 0 | 5 |

**Passo 3: 1ª Cobertura**
Podemos cobrir os zeros com 3 retas (Linha F1, Linha F3, Coluna T3).
Como 3 < 4, ajustamos. Menor valor livre é 1. Subtrai 1 dos livres, soma 1 nos cruzamentos.

| | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| F1 | 0 | 4 | 1 | 2 |
| F2 | 0 | 3 | 0 | 4 |
| F3 | 2 | 0 | 1 | 0 |
| F4 | 1 | 3 | 0 | 4 |

**Passo 4: 2ª Cobertura**
Ainda podemos cobrir com 3 retas (Col T1, Col T3, Linha F3). Ajustamos de novo (mínimo 2).

| | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| F1 | 0 | 2 | 1 | 0 |
| F2 | 0 | 1 | 0 | 2 |
| F3 | 4 | 0 | 3 | 0 |
| F4 | 1 | 1 | 0 | 2 |

**Passo 5: Alocação**
F4 pega T3. F2 pega T1. F1 pega T4. F3 pega T2.
Custo: 49.

---

## 7.4 Prática Húngaro 1 (Minimização Simples 3x3)

**Enunciado:** 3 Trabalhadores, 3 Máquinas.

Reduzindo linhas (250, 350, 200) e colunas (0, 150, 0):
| | M1 | M2 | M3 |
|---|---|---|---|
| T1 | 0 | 0 | 100 |
| T2 | 50 | 100 | 0 |
| T3 | 0 | 50 | 50 |

Matriz pronta (cobre com 3 retas).
**Alocação:** T2 pega M3. T1 pega M2. T3 pega M1.
Custo: 400 + 350 + 200 = 950.

---

## 7.5 Prática Húngaro 2 (Ajuste de Zeros 4x4)

**Enunciado:** Ajustar matriz fornecida que não atinge 4 retas.

Cobrimos os zeros com 3 retas (C1, L3, L4). Mínimo livre = 2.
**Nova matriz após subtrair 2 dos livres e somar nos cruzamentos:**
| | Col1 | Col2 | Col3 | Col4 |
|---|---|---|---|---|
| L1 | 0 | 3 | 6 | 1 |
| L2 | 0 | 2 | 5 | 0 |
| L3 | 4 | 0 | 3 | 0 |
| L4 | 7 | 3 | 0 | 1 |

---

## 7.6 Prática Húngaro 3 (Maximização)

**Enunciado:** Lucro esperado. Maximizar.

**Conversão:** Maior valor é 60. Nova matriz = 60 - Valores.
| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| C1 | 40 | 20 | 30 | 50 |
| C2 | 20 | 60 | 40 | 30 |
| C3 | 30 | 40 | 50 | 20 |
| C4 | 50 | 30 | 20 | 40 |

Redução de Linha e Coluna gera:
| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| C1 | 10 | 30 | 20 | 0 |
| C2 | 40 | 0 | 20 | 30 |
| C3 | 20 | 10 | 0 | 30 |
| C4 | 0 | 20 | 30 | 10 |

Alocação: C4 pega R1, C2 pega R2, C3 pega R3, C1 pega R4.
Lucro: 50 + 60 + 50 + 50 = 210.
