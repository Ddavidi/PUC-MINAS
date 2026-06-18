# 🧱 O Resistor em Corrente Alternada (Z = R)

Em circuitos de Corrente Alternada (CA), a Lei de Ohm vira a "Lei de Ohm Fasorial": `V = Z * I`, onde `Z` é a Impedância. 

A Impedância `Z` existe para representar duas coisas que um componente pode fazer:
1. Diminuir a amplitude (força) do sinal.
2. Atrasar ou adiantar a onda (mudar o ângulo/fase).

### 💡 O Caso Especial do Resistor
O Resistor é o cara mais "tranquilo" dos circuitos. Diferente de Indutores e Capacitores que mexem no ângulo da onda, o **Resistor NÃO muda a fase**. Ele só "espreme" a onda, diminuindo sua amplitude.

Por isso, na hora de converter um resistor para impedância, a fórmula é simplesmente:
> **Z_R = R**

Ele não tem a letra `j` (número imaginário) junto dele. 
Isso significa matematicamente que a Tensão e a Corrente que passam por um resistor estarão sempre **perfeitamente sincronizadas (em fase)**. O ângulo do fasor da tensão será exatamente igual ao ângulo do fasor da corrente!

---

## 📌 Passo a Passo: Resolvendo problemas com resistores puros

Se o circuito tiver **apenas resistor** (ou se você estiver analisando apenas a parte do resistor), siga a receita:

1. **Ache o ω:** Identifique a frequência angular na fonte `cos(ωt)`.
2. **Transforme a Fonte em Fasor:** Pegue a amplitude e o ângulo `V = Vm ∠ φ`.
3. **Calcule a Impedância:** No caso do resistor, é só repetir o valor! `Z = R ∠ 0°` (ele tem ângulo zero, pois não muda a fase).
4. **Aplique V = Z * I:** Isole o que o problema pediu.
   - Para achar corrente: `I = V / Z` (o ângulo do `I` vai ficar igual ao do `V`).
   - Para achar tensão: `V = Z * I`
5. **Volte ao Tempo:** Pegue o fasor resultante e escreva na forma `Vm * cos(ωt + φ)`.

---

## 🎯 Praticando com o Problema 9.28

**Enunciado:** Determine a corrente que flui através de um resistor de 8 Ω conectado a uma fonte de tensão `vs = 110 cos(377t) V`.

Vamos seguir nossa receita!

**Passo 1: Ache o ω**
O número que multiplica o `t` na fonte é 377.
- `ω = 377 rad/s` *(Isso é a frequência padrão da rede elétrica de 60Hz, pois 2π*60 ≈ 377)*.

**Passo 2: Transforme a Fonte em Fasor**
A fonte já está em cosseno e positiva: `vs = 110 cos(377t)`. Como não há ângulo visível, a fase inicial é 0°.
- `V = 110 ∠ 0° V`

**Passo 3: Calcule a Impedância**
Temos um resistor de 8 Ω. Pelo conceito estudado, ele não muda fase:
- `Z = 8 Ω` (ou `8 ∠ 0° Ω` em polar).

**Passo 4: Aplique V = Z * I**
Queremos a corrente, então a fórmula é `I = V / Z`:
- `I = (110 ∠ 0°) / (8 ∠ 0°)`
- Dividimos as magnitudes: `110 / 8 = 13,75`
- Subtraímos os ângulos: `0° - 0° = 0°`
- **Fasor da Corrente:** `I = 13,75 ∠ 0° A`

*Nota: Veja como a tensão tinha ângulo 0° e a corrente também ficou com ângulo 0°. Estão em fase!*

**Passo 5: Volte ao Tempo**
Vamos montar a equação final juntando a nova amplitude (13,75), a mesma frequência de antes (377t) e o novo ângulo (0°):
- `i(t) = 13,75 cos(377t) A`

> **✅ Resposta Final: `i(t) = 13,75 cos(377t) A`**
