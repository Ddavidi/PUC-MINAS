import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

# ============================================================
# CIRCUITO t < 0: Chave K1 ABERTA  (estado estacionario)
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q1_circuito_t_antes.png"), show=False) as d:
    d.config(unit=5.0, fontsize=16)

    # Fio inferior
    d += elm.Line().right().at((0,0)).length(10)

    # Fonte (lado esquerdo)
    d += elm.Line().up().at((0,0)).length(1.5)
    src_bot = d.here
    d += elm.SourceV().up().at(src_bot)
    src_top = d.here
    d += elm.Label().at((-1.0, (src_bot[1]+src_top[1])/2)).label('$E_1$\n20 V')
    d += elm.Line().up().at(src_top).length(1.5)
    top_left = d.here

    # R1 (serie)
    d += elm.Resistor().right().at(top_left).label('$R_1$\n1 Ω', loc='top').length(4)
    node_mid = d.here

    # R2 (serie)
    d += elm.Resistor().right().at(node_mid).label('$R_2$\n3 Ω', loc='top').length(4)
    node_right_top = d.here

    # K1 aberta (label)
    d += elm.Line().up().at(node_mid).length(2)
    k1_left = d.here
    d += elm.Line().right().at(k1_left).length(3)
    k1_mid = d.here
    d += elm.Label().at(k1_mid).label('K₁ ABERTA', color='red')
    d += elm.Dot(open=True).at(k1_mid)

    # Indutor (lado direito, vertical)
    d += elm.Inductor2().down().at(node_right_top).label('$L_1$\n80 mH', loc='left').toy(0)

    # Seta de corrente
    d += elm.Line(arrow='->').right().at((node_right_top[0]+0.5, node_right_top[1]-0.5)).length(1.5).color('blue').label('$i_0$', loc='right')
    d += elm.Label().at((node_right_top[0]-0.7, node_right_top[1]-2)).label('+\n$v_0$\n−', color='darkgreen')

print("Gerado t<0")

# ============================================================
# CIRCUITO t > 0: Chave K1 FECHADA  (resposta a degrau RL)
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q1_circuito_t_depois.png"), show=False) as d:
    d.config(unit=5.0, fontsize=16)

    # Fio inferior
    d += elm.Line().right().at((0,0)).length(8)

    # Fonte (lado esquerdo)
    d += elm.Line().up().at((0,0)).length(1.5)
    src_bot = d.here
    d += elm.SourceV().up().at(src_bot)
    src_top = d.here
    d += elm.Label().at((-1.0, (src_bot[1]+src_top[1])/2)).label('$E_1$\n20 V')
    d += elm.Line().up().at(src_top).length(1.5)
    top_left = d.here

    # R1 (serie)
    d += elm.Resistor().right().at(top_left).label('$R_1$\n1 Ω', loc='top').length(4)
    node_mid = d.here

    # Fio de curto (K1 fechada, bypassa R2)
    d += elm.Line().up().at(node_mid).length(2)
    k1_top_L = d.here
    d += elm.Line().right().at(k1_top_L).length(4)
    k1_top_R = d.here
    d += elm.Label().at(((k1_top_L[0]+k1_top_R[0])/2, k1_top_L[1]+0.3)).label('K₁ FECHADA (curto em $R_2$)', color='blue')
    d += elm.Line().down().at(k1_top_R).toy(node_mid[1])
    node_right = (k1_top_R[0], node_mid[1])

    # Indutor (lado direito, vertical)
    d += elm.Inductor2().down().at(node_right).label('$L_1$\n80 mH', loc='left').toy(0)

    # Seta de corrente
    d += elm.Line(arrow='->').right().at((node_right[0]+0.5, node_right[1]-0.5)).length(1.5).color('blue').label('$i_0$', loc='right')
    d += elm.Label().at((node_right[0]-0.7, node_right[1]-2)).label('+\n$v_0$\n−', color='darkgreen')

    # R2 riscado / em cinza
    d += elm.Resistor().right().at(node_mid).label('$R_2$ (bypass)', loc='bottom', color='gray').length(4).color('gray')

print("Gerado t>0")
