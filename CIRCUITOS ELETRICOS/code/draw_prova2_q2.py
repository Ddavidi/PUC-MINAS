import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

# ============================================================
# Q2 CIRCUITO t < 0: K1 FECHADA  (estado estacionario)
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q2_circuito_t_antes.png"), show=False) as d:
    d.config(unit=5.0, fontsize=16)

    # Fio inferior
    d += elm.Line().right().at((0,0)).length(12)

    # Fonte de corrente (lado esquerdo)
    d += elm.SourceI().up().at((0,0)).label('$I_1$\n7,5 mA', loc='left').reverse()
    top_left = d.here

    # R1 em paralelo (vertical, mesmo ponto)
    d += elm.Line().right().at(top_left).length(1.0)
    d += elm.Resistor().down().label('$R_1$\n80 kΩ', loc='left').toy(0)

    # Top wire going right
    d += elm.Line().right().at(top_left).length(3)
    d += elm.Resistor().right().label('$R_2$\n20 kΩ', loc='top').length(4)
    node_k1 = d.here

    # K1 fechada (fio simples)
    d += elm.Line().right().at(node_k1).length(2)
    d += elm.Label().at((node_k1[0]+1, node_k1[1]+0.4)).label('K₁ FECHADA', color='blue')
    node_after_k1 = (node_k1[0]+2, node_k1[1])

    # C1 (vertical, direita)
    d += elm.Capacitor().down().at(node_after_k1).label('$C_1$\n0,4 μF', loc='left').toy(0)

    # R3 (vertical, extrema direita)
    d += elm.Line().right().at(node_after_k1).length(2)
    node_r3_top = d.here
    d += elm.Resistor().down().at(node_r3_top).label('$R_3$\n50 kΩ', loc='right').toy(0)

    # Tensao v
    d += elm.Label().at((node_after_k1[0]-0.8, node_after_k1[1]-2)).label('+\n$v$\n−', color='darkgreen')

print("Gerado Q2 t<0")

# ============================================================
# Q2 CIRCUITO t > 0: K1 ABERTA  (descarga RC)
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q2_circuito_t_depois.png"), show=False) as d:
    d.config(unit=5.0, fontsize=16)

    # Fio inferior
    d += elm.Line().right().at((0,0)).length(6)

    # C1 (vertical, esquerda)
    d += elm.Capacitor().up().at((0,0)).label('$C_1$\n$v(0)=200\\text{ V}$', loc='left')
    top_c = d.here

    # Fio superior
    d += elm.Line().right().at(top_c).length(6)

    # R3 (vertical, direita)
    d += elm.Resistor().down().at((6,top_c[1])).label('$R_3$\n50 kΩ', loc='right').toy(0)

    # Tensao v_o
    d += elm.Label().at((3.5, top_c[1]-2.5)).label('+\n$v_0(t)$\n−', color='darkgreen')
    d += elm.Label().at((3, top_c[1]+0.6)).label('K₁ ABERTA — Circuito isolado', color='red')

print("Gerado Q2 t>0")
