# Resumo Básico para a Prova: Capítulo 7

Este resumo vai direto ao ponto com as fórmulas nuas e cruas que você vai usar para gabaritar o Capítulo 7.

## 1. A Equação Mágica (Fórmula Geral)
Serve para qualquer circuito RC ou RL, seja para calcular tensão ou corrente:
$$ x(t) = x(\infty) + [x(0) - x(\infty)] e^{-t/\tau} $$

- Se a questão for de **Resposta Natural** (sem fontes ativas para $t>0$), o $x(\infty) = 0$. A equação vira:
  $$ x(t) = x(0) e^{-t/\tau} $$

## 2. Constante de Tempo ($\tau$)
É o ritmo em que o circuito descarrega ou carrega. O Thevenin é o segredo aqui.
- **Circuito RC:** $\tau = R_{eq} \cdot C$ (Onde $R_{eq}$ é a resistência enxergada pelo capacitor).
- **Circuito RL:** $\tau = \frac{L}{R_{eq}}$ (Onde $R_{eq}$ é a resistência enxergada pelo indutor).

## 3. Comportamento no Regime Estacionário ($t < 0$ ou $t \to \infty$)
Quando uma fonte DC fica ligada no circuito por muito tempo (Regime Permanente):
- **Capacitor** vira um **Circuito Aberto** (fio quebrado). Calcule a Tensão nos terminais dele.
- **Indutor** vira um **Curto-Circuito** (fio liso). Calcule a Corrente que passa no fio.

## 4. Continuidade (O Truque Matador)
- **Tensão no Capacitor NUNCA dá salto:** $v_C(0^-) = v_C(0^+) = v_C(0)$. Se antes de virar a chave tinha 12V, um milissegundo depois de virar a chave continua tendo 12V.
- **Corrente no Indutor NUNCA dá salto:** $i_L(0^-) = i_L(0^+) = i_L(0)$. A inércia magnética mantém a corrente igual na virada da chave.

## Passo a Passo Expresso
1. **Instante $t < 0$:** Substitua C por aberto ou L por curto. Calcule $v(0)$ ou $i(0)$.
2. **Instante $t > 0$:** Apague C ou L. Calcule o $R_{eq}$ (Resistência de Thevenin) olhando para os buracos.
3. **Ache o $\tau$:** $\tau = R_{eq} C$ ou $\tau = \frac{L}{R_{eq}}$.
4. **Instante $t = \infty$:** (Só para Degrau). Substitua C por aberto ou L por curto no circuito com $t>0$. Calcule $v(\infty)$ ou $i(\infty)$.
5. **Monte a Equação:** Jogue os valores na Fórmula Geral.
