# Exemplo Resolvido: Resposta Natural de um Circuito RC

Este é um exemplo clássico para aplicarmos a **"Receita de Bolo"** passo a passo. 
A chave está **fechada há muito tempo** e, no instante $t=0$, ela se **abre**. Queremos encontrar a equação da tensão no capacitor $v(t)$ para $t > 0$.

![Exemplo RC](../../_base_dados_ia/imagens_geradas/cap7_exemplo_rc.png)

---

## Passo 1: Encontrar o Início $v(0)$
Temos que olhar o circuito no instante **antes** da chave abrir ($t < 0$).
Como a chave estava fechada há muito tempo, o circuito atingiu o *Regime Permanente*.
- **Regra:** O Capacitor se comporta como um **Circuito Aberto** (fio quebrado).
- A fonte de 24V está empurrando corrente pelo resistor de $4 \, \Omega$ e pelo resistor de $12 \, \Omega$. O capacitor é apenas um buraco onde não entra corrente, mas ele está em **paralelo** com o resistor de $12 \, \Omega$.
- Logo, a tensão no capacitor $v(0)$ é igual à tensão no resistor de $12 \, \Omega$.
- Usando um simples Divisor de Tensão:
  $$ v(0) = 24 \cdot \left( \frac{12}{4 + 12} \right) = 24 \cdot \left( \frac{12}{16} \right) = 24 \cdot 0.75 = 18V $$
- Como a tensão no capacitor não dá "saltos" instantâneos, **$v(0) = 18V$**.

## Passo 2: Encontrar o Fim $v(\infty)$
Agora olhamos para o circuito **muito tempo depois** da chave abrir ($t \to \infty$).
- Quando a chave abre, a fonte de 24V e o resistor de $4 \, \Omega$ são desconectados do resto do circuito e "morrem".
- O capacitor fica trancado em uma sala sozinho com o resistor de $12 \, \Omega$.
- Como não há nenhuma fonte empurrando nova energia para o capacitor, ele vai descarregar toda a energia de $18V$ que ele tinha armazenado em cima do resistor de $12 \, \Omega$, até zerar.
- Portanto, o valor final é **$v(\infty) = 0V$** (Essa é a clássica **Resposta Natural**).

## Passo 3: Encontrar a Constante de Tempo ($\tau$)
Olhe para o circuito **depois que a chave mudou ($t > 0$)**.
- O circuito do lado direito da chave é apenas o Capacitor de $0.5F$ em paralelo com o resistor de $12 \, \Omega$.
- O Thevenin "visto" pelo capacitor é simplesmente o resistor de $12 \, \Omega$. Logo, $R_{eq} = 12 \, \Omega$.
- Fórmula do RC: 
  $$ \tau = R_{eq} \cdot C = 12 \cdot 0.5 = 6 \text{ segundos} $$

## Passo 4: Jogar na Equação Mágica
A equação geral é:
$$ v(t) = v(\infty) + [v(0) - v(\infty)] \cdot e^{-\frac{t}{\tau}} $$

Substituindo os três ingredientes que achamos ($v(0) = 18$, $v(\infty) = 0$, $\tau = 6$):
$$ v(t) = 0 + [18 - 0] \cdot e^{-\frac{t}{6}} $$
$$ v(t) = 18 e^{-\frac{t}{6}} \text{ V} $$

**Resposta Final:** $v(t) = 18 e^{-t/6} \, V$ para $t > 0$.
