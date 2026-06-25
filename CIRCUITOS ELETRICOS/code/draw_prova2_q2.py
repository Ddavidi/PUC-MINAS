import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

# ============================================================
# CIRCUITO ORIGINAL (como aparece na prova)
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q2_original.png"), show=False) as d:
    d.config(unit=4.0, fontsize=14)

    H = 6

    # Fio inferior
    d += elm.Line().right().at((0,0)).length(14)

    # Fonte de corrente (esquerdo, vertical)
    d += elm.SourceI().up().at((0,0)).length(H).label('$I_1$\n7,5 mA', loc='left').reverse()
    d += elm.Dot().at((0, H))
    d += elm.Dot().at((0, 0))

    # R1 (vertical, paralelo com fonte)
    d += elm.Line().right().at((0, H)).length(2)
    r1_top = d.here
    d += elm.Resistor().down().at(r1_top).length(H).label('$R_1$\n80 kΩ', loc='right')
    d += elm.Line().left().at(r1_top).length(2)
    d += elm.Line().left().at((r1_top[0], 0)).tox(0)

    # Fio superior saindo de R1 para R2
    d += elm.Line().right().at(r1_top).length(1)
    r2_start = d.here
    d += elm.Dot().at(r2_start)

    # R2 (horizontal)
    d += elm.Resistor().right().at(r2_start).length(4).label('$R_2$\n20 kΩ', loc='top')
    k1_left = d.here

    # K1 (switch)
    d += elm.Switch().right().at(k1_left).length(2).label('$K_1$', loc='top')
    k1_right = d.here
    d += elm.Dot().at(k1_right)

    # C1 (vertical)
    d += elm.Capacitor().down().at(k1_right).length(H).label('$C_1$\n0,4 μF', loc='left')
    d += elm.Dot().at(k1_right)

    # R3 (vertical, paralelo com C1)
    d += elm.Line().right().at(k1_right).length(4)
    r3_top = d.here
    d += elm.Dot().at(r3_top)
    d += elm.Resistor().down().at(r3_top).length(H).label('$R_3$\n50 kΩ', loc='right')

    # v label
    d += elm.Gap().down().at((k1_right[0]+1.5, H)).length(H).label(['+', '$v$', '−'])

print("OK: prova2_q2_original.png")

# ============================================================
# CIRCUITO t < 0: K1 FECHADA (regime CC permanente)
# Capacitor = circuito aberto
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q2_t_menor_0.png"), show=False) as d:
    d.config(unit=4.0, fontsize=14)

    H = 6

    # Fio inferior
    d += elm.Line().right().at((0,0)).length(14)

    # Fonte de corrente
    d += elm.SourceI().up().at((0,0)).length(H).label('$I_1$\n7,5 mA', loc='left').reverse()
    d += elm.Dot().at((0, H))
    d += elm.Dot().at((0, 0))

    # R1
    d += elm.Line().right().at((0, H)).length(2)
    r1_top = d.here
    d += elm.Resistor().down().at(r1_top).length(H).label('$R_1$\n80 kΩ', loc='right')
    d += elm.Line().left().at((r1_top[0], 0)).tox(0)

    # Fio superior
    d += elm.Line().right().at(r1_top).length(1)
    r2_start = d.here
    d += elm.Dot().at(r2_start)
    d += elm.Label().at((r2_start[0], H+0.5)).label('Nó A', color='blue', fontsize=12)

    # R2
    d += elm.Resistor().right().at(r2_start).length(4).label('$R_2$\n20 kΩ', loc='top')
    k1_left = d.here

    # K1 fechada = fio
    d += elm.Line().right().at(k1_left).length(2).color('blue')
    k1_right = d.here
    d += elm.Dot().at(k1_right)
    d += elm.Label().at((k1_right[0], H+0.5)).label('Nó B', color='blue', fontsize=12)
    d += elm.Label().at(((k1_left[0]+k1_right[0])/2, H+1.0)).label('K₁ fechada (fio)', color='blue', fontsize=11)

    # C1 = ABERTO (sem elemento, só gap)
    d += elm.Gap().down().at(k1_right).length(H).label(['', 'C aberto', ''], color='red')

    # R3
    d += elm.Line().right().at(k1_right).length(4)
    r3_top = d.here
    d += elm.Dot().at(r3_top)
    d += elm.Resistor().down().at(r3_top).length(H).label('$R_3$\n50 kΩ', loc='right')

    # v no nó B
    d += elm.Label().at((k1_right[0]+1.3, H/2)).label('+\n$v(0^-)$\n−', color='darkgreen', fontsize=13)

print("OK: prova2_q2_t_menor_0.png")

# ============================================================
# CIRCUITO t > 0: K1 ABERTA (descarga RC)
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q2_t_maior_0.png"), show=False) as d:
    d.config(unit=4.0, fontsize=14)

    H = 5

    # Fio inferior
    d += elm.Line().right().at((0,0)).length(8)

    # C1 (esquerda)
    d += elm.Capacitor().up().at((0,0)).length(H).label('$C_1$\n$v(0) = 200$ V', loc='left')
    d += elm.Dot().at((0,H))
    d += elm.Dot().at((0,0))

    # Fio superior
    d += elm.Line().right().at((0,H)).length(8)

    # R3 (direita)
    d += elm.Resistor().down().at((8,H)).length(H).label('$R_3$\n50 kΩ', loc='right')
    d += elm.Dot().at((8,H))
    d += elm.Dot().at((8,0))

    # v_o
    d += elm.Gap().down().at((4, H)).length(H).label(['+', '$v_0(t)$', '−'], color='darkgreen')

    # Titulo
    d += elm.Label().at((4, H+0.8)).label('t > 0: K₁ aberta → descarga livre', color='red', fontsize=12)

print("OK: prova2_q2_t_maior_0.png")
