# Exercício Proposto: O Desafio do Indutor

Agora é a sua vez de sujar as mãos! Este é um problema clássico de circuito RL. 
A chave está **aberta** há muito tempo e, no instante $t=0$, ela se **fecha**, ligando a fonte bruscamente no circuito. Queremos encontrar a equação da corrente no indutor $i(t)$ para $t > 0$.

![Desafio RL](../../_base_dados_ia/imagens_geradas/cap7_proposto_rl.png)

---

## Passo 1: Encontre o Início $i(0)$
> *Dica: Olhe para $t < 0$. A chave está aberta. Tem alguma fonte conectada ao indutor? Qual é a corrente que passa por ele?*

**Sua Resposta para $i(0)$:** `[  ] Amperes`

---

## Passo 2: Encontre o Fim $i(\infty)$
> *Dica: Olhe para $t \to \infty$. A chave fechou há muito tempo. O Indutor se transforma em um "curto-circuito" (fio liso). Calcule a corrente que passa por esse fio liso agora que a fonte de 10V está ligada.*

**Sua Resposta para $i(\infty)$:** `[  ] Amperes`

---

## Passo 3: Encontre a Constante de Tempo ($\tau$)
> *Dica: Olhe para o circuito em $t > 0$ (chave fechada). Apague a fonte de tensão e o indutor. Qual é a Resistência Equivalente (Thevenin) que sobrou enxergada pelo indutor? Use a fórmula $\tau = \frac{L}{R_{eq}}$.*

**Sua Resposta para $\tau$:** `[  ] Segundos`

---

## Passo 4: Jogue na Equação Mágica
> *Fórmula Geral: $i(t) = i(\infty) + [i(0) - i(\infty)] e^{-t/\tau}$*

**Equação Final $i(t)$:** `[   ]`

---
*Dica de Ouro: Esse é um caso de "Resposta ao Degrau", porque a fonte é ligada abruptamente no circuito! Calcule cada etapa, preencha os colchetes e mande suas respostas aqui no chat!*
