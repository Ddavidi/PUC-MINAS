# Receita de Bolo: Método Húngaro (Minimização)

Queremos alocar 3 Trabalhadores para 3 Máquinas com o menor custo total possível.

## Tabela Inicial de Custos

| | M1 | M2 | M3 |
|---|---|---|---|
| **T1** | 250 | 400 | 350 |
| **T2** | 400 | 600 | 350 |
| **T3** | 200 | 400 | 250 |

---

## Passo a Passo

### Passo 1: Redução de Linha
Ache o menor valor de cada linha e subtraia ele do resto da linha.
- Linha T1: Mínimo é 250. Fica: (0, 150, 100).
- Linha T2: Mínimo é 350. Fica: (50, 250, 0).
- Linha T3: Mínimo é 200. Fica: (0, 200, 50).

**Tabela após Passo 1:**
| | M1 | M2 | M3 |
|---|---|---|---|
| **T1** | 0 | 150 | 100 |
| **T2** | 50 | 250 | 0 |
| **T3** | 0 | 200 | 50 |

### Passo 2: Redução de Coluna
Na nova tabela, ache o menor valor de cada coluna e subtraia dele mesmo.
- Coluna M1: Mínimo é 0. Não muda nada (fica 0, 50, 0).
- Coluna M2: Mínimo é 150. Fica (0, 100, 50).
- Coluna M3: Mínimo é 0. Não muda nada (fica 100, 0, 50).

**Tabela após Passo 2:**
| | M1 | M2 | M3 |
|---|---|---|---|
| **T1** | 0 | 0 | 100 |
| **T2** | 50 | 100 | 0 |
| **T3** | 0 | 50 | 50 |

### Passo 3: Cobertura de Zeros
Vamos tentar riscar todos os zeros usando o **menor número possível de retas** horizontais ou verticais.
Temos zeros em (T1,M1), (T1,M2), (T2,M3), (T3,M1).

- Uma reta na Linha T1 (Cobre 2 zeros).
- Uma reta na Linha T2 (Cobre 1 zero).
- Uma reta na Coluna M1 (Cobre o zero do T3 que sobrou).

Usamos 3 retas! Como a matriz é 3x3 (N=3), **não precisamos do Passo de Ajuste de Custo**. A tabela já está pronta para alocação.

### Passo 4: Alocação
Sempre comece pelas linhas ou colunas que tem apenas **um zero** disponível.
1. Olhando para T2, só tem um zero: em M3.
   -> **Alocar T2 na M3**. (Risque a coluna M3 e a linha T2, ninguém mais pode usar elas).
2. Olhando para T3, o zero dele é em M1.
   -> **Alocar T3 na M1**. (Risque a coluna M1 e a linha T3).
3. Sobrou apenas o T1. Os zeros dele estavam em M1 e M2. Como M1 já foi pega pelo T3, sobrou a M2.
   -> **Alocar T1 na M2**.

**Alocação Ótima:**
- T1 $\rightarrow$ M2
- T2 $\rightarrow$ M3
- T3 $\rightarrow$ M1

### Custo Total
Volte na **Tabela Inicial (A primeirona!)** e some os custos originais das casinhas alocadas:
- T1-M2: 400
- T2-M3: 350
- T3-M1: 200

**Custo Mínimo Total:** $400 + 350 + 200 =$ **950**.
