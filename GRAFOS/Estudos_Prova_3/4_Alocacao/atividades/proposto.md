# Exercício Proposto: O Passo do Ajuste no Método Húngaro

Agora você vai testar o caso em que a matriz trava e precisamos "ajustar" os custos (o Passo 5).

## O Desafio

Imagine que após fazer a **Redução de Linhas** e a **Redução de Colunas** em uma matriz 4x4, você chegue no seguinte estado:

| | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| **L1** | 0 | 5 | 8 | 3 |
| **L2** | 0 | 4 | 7 | 2 |
| **L3** | 2 | 0 | 3 | 0 |
| **L4** | 5 | 3 | 0 | 1 |

> [!IMPORTANT]
> Tente cobrir todos os zeros usando retas. Você vai perceber que dá para cobrir todos eles usando **apenas 3 retas** (ex: Coluna 1, Linha 3, Linha 4). Como 3 é menor que 4, a matriz não está pronta.

**Sua Missão:**
1. Identifique os elementos que ficaram "livres" (sem nenhuma reta passando por eles).
2. Ache o **menor valor** entre esses livres.
3. Subtraia esse valor de todos os livres.
4. Some esse valor onde as retas se cruzam.
5. Monte a nova matriz após o ajuste.

*Faça as contas no papel e confira o gabarito abaixo!*

---
<br><br><br><br><br><br><br><br>

## Gabarito

**Passo 1: Cobertura de Retas**
Se você traçou a Coluna 1, a Linha 3 e a Linha 4, os valores que ficaram **sem risco nenhum (Livres)** foram:
- Em L1: 5, 8, 3
- Em L2: 4, 7, 2

**Passo 2: Menor Valor Livre**
O menor valor entre todos esses livres é o **2** (na posição L2, C4).

**Passo 3 e 4: O Ajuste**
- **Subtraia 2** de todos os que estão Livres.
  - Livres em L1 ficam: 3, 6, 1
  - Livres em L2 ficam: 2, 5, 0 (olha, criamos um zero novo!)
- **Some 2** nos Cruzamentos das retas. Onde a Coluna 1 cruza com a Linha 3 (valor 2) e com a Linha 4 (valor 5).
  - L3, C1 vira: $2 + 2 = 4$
  - L4, C1 vira: $5 + 2 = 7$
- **O resto (coberto por apenas uma reta)** fica idêntico (zeros continuam zeros).

**Passo 5: Matriz Ajustada Final**

| | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| **L1** | 0 | 3 | 6 | 1 |
| **L2** | 0 | 2 | 5 | 0 |
| **L3** | 4 | 0 | 3 | 0 |
| **L4** | 7 | 3 | 0 | 1 |

*Pronto! Agora a matriz precisaria de 4 retas e você poderia prosseguir para a alocação.*
