import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

# ============================================================
# CIRCUITO ORIGINAL (como aparece na prova)
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q2_original.png"), show=False) as d:
    d.config(unit=3.5, fontsize=14)

    # Fonte de corrente (esquerdo, vertical, de baixo para cima)
    d += elm.SourceI().up().at((0,0)).label('7,5 mA', loc='left')
    top_left = d.here

    # Fio superior ate R1
    d += elm.Line().right().at(top_left).length(2)
    node_A = d.here
    d += elm.Dot()

    # R1 (vertical, desce)
    d += elm.Resistor().down().at(node_A).label('$R_1$ = 80 kΩ', loc='bot')
    r1_bot = d.here

    # R2 (horizontal, para a direita)
    d += elm.Resistor().right().at(node_A).label('$R_2$ = 20 kΩ', loc='top')
    r2_end = d.here

    # K1 (switch)
    d += elm.Switch().right().at(r2_end).label('$K_1$', loc='top')
    node_B = d.here
    d += elm.Dot()

    # C1 (vertical, desce)
    d += elm.Capacitor().down().at(node_B).label('$C_1$ = 0,4 μF', loc='bot')
    c1_bot = d.here

    # R3 (vertical, paralelo com C1)
    d += elm.Line().right().at(node_B).length(3)
    r3_top = d.here
    d += elm.Dot()
    d += elm.Resistor().down().at(r3_top).label('$R_3$ = 50 kΩ', loc='bot')
    r3_bot = d.here

    # Tensao v
    d += elm.Line().right().at(r3_top).length(2)
    vt = d.here
    d += elm.Dot(open=True)
    d += elm.Line().right().at(r3_bot).length(2)
    vb = d.here
    d += elm.Dot(open=True)
    d += elm.Gap().down().at(vt).toy(vb).label(['+', '$v$', '−'])

    # Fio inferior (conecta tudo embaixo)
    d += elm.Line().left().at(r3_bot).tox(r1_bot)
    d += elm.Line().left().at(r1_bot).tox(0)
    d += elm.Line().left().at(c1_bot).tox(r1_bot)

print("OK: prova2_q2_original.png")

# ============================================================
# CIRCUITO t < 0: K1 FECHADA, Capacitor = ABERTO
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q2_t_menor_0.png"), show=False) as d:
    d.config(unit=3.5, fontsize=14)

    # Fonte de corrente
    d += elm.SourceI().up().at((0,0)).label('7,5 mA', loc='left')
    top_left = d.here

    # Fio superior ate nó A
    d += elm.Line().right().at(top_left).length(2)
    node_A = d.here
    d += elm.Dot()
    d += elm.Label().at((node_A[0]-0.8, node_A[1]+0.4)).label('Nó A', color='blue')

    # R1 (desce)
    d += elm.Resistor().down().at(node_A).label('$R_1$ = 80 kΩ', loc='bot')
    r1_bot = d.here

    # R2 (horizontal)
    d += elm.Resistor().right().at(node_A).label('$R_2$ = 20 kΩ', loc='top')
    r2_end = d.here

    # K1 fechada = fio azul
    d += elm.Line().right().at(r2_end).length(3).color('blue').label('K₁ fechada', color='blue', loc='top')
    node_B = d.here
    d += elm.Dot()
    d += elm.Label().at((node_B[0], node_B[1]+0.4)).label('Nó B', color='blue')

    # C1 = ABERTO (gap vermelho)
    d += elm.Gap().down().at(node_B).label(['', 'C₁ aberto', ''], color='red')
    c1_bot = d.here

    # R3 (paralelo)
    d += elm.Line().right().at(node_B).length(3)
    r3_top = d.here
    d += elm.Dot()
    d += elm.Resistor().down().at(r3_top).label('$R_3$ = 50 kΩ', loc='bot')
    r3_bot = d.here

    # Fio inferior
    d += elm.Line().left().at(r3_bot).tox(c1_bot)
    d += elm.Line().left().at(c1_bot).tox(r1_bot)
    d += elm.Line().left().at(r1_bot).tox(0)

print("OK: prova2_q2_t_menor_0.png")

# ============================================================
# CIRCUITO t > 0: K1 ABERTA → C1 descarrega em R3
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q2_t_maior_0.png"), show=False) as d:
    d.config(unit=3.5, fontsize=14)

    # Capacitor (esquerda, sobe)
    d += elm.Capacitor().up().at((0,0)).label('$C_1$\n$v(0) = 200$ V', loc='bot')
    top_left = d.here
    d += elm.Dot()

    # Fio superior
    d += elm.Line().right().at(top_left).length(5)
    top_right = d.here
    d += elm.Dot()

    # R3 (direita, desce)
    d += elm.Resistor().down().at(top_right).label('$R_3$ = 50 kΩ', loc='bot')
    bot_right = d.here

    # Fio inferior
    d += elm.Line().left().at(bot_right).tox(0)

    # Label v_o
    d += elm.Gap().down().at((top_right[0]+2, top_left[1])).toy(0).label(['+', '$v_0(t)$', '−'], color='darkgreen')
    d += elm.Dot(open=True).at((top_right[0]+2, top_left[1]))
    d += elm.Line().right().at(top_right).length(2)
    d += elm.Dot(open=True).at((top_right[0]+2, 0))
    d += elm.Line().right().at(bot_right).length(2)

    # Titulo
    d += elm.Label().at((2.5, top_left[1]+0.6)).label('t > 0: descarga livre (K₁ aberta)', color='red')

print("OK: prova2_q2_t_maior_0.png")
