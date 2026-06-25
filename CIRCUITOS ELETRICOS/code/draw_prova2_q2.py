import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

# ============================================================
# Q2 CIRCUITO t < 0: K1 FECHADA  (estado estacionario)
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q2_circuito_t_antes.png"), show=False) as d:
    d.config(unit=4.0, fontsize=15)

    H = 6  # altura do circuito

    # Fio inferior total
    d += elm.Line().right().at((0,0)).length(16)

    # Fonte de corrente (extremo esquerdo, vertical)
    d += elm.SourceI().up().at((0,0)).length(H).label('$I_1$\n7,5 mA', loc='left').reverse()
    d += elm.Dot().at((0, H))

    # R1 (vertical, em paralelo com a fonte)
    d += elm.Resistor().down().at((2, H)).length(H).label('$R_1$\n80 kΩ', loc='right')
    d += elm.Line().left().at((2,H)).length(2)
    d += elm.Line().right().at((2,0)).length(0)  # just to anchor

    # Fio superior esquerdo
    d += elm.Line().right().at((0, H)).length(2)

    # R2 (horizontal)
    d += elm.Resistor().right().at((2, H)).label('$R_2$\n20 kΩ', loc='top').length(5)
    node_k1_L = d.here  # (7, H)

    # K1 fechada: fio simples de nó
    d += elm.Line().right().at(node_k1_L).length(2)
    d += elm.Label().at((node_k1_L[0]+1, H+0.5)).label('K₁ FECHADA', color='blue')
    node_after = (node_k1_L[0]+2, H)  # (9, H)

    # C1 (vertical)
    d += elm.Capacitor().down().at(node_after).length(H).label('$C_1$\n0,4 μF', loc='left')

    # Fio superior para R3
    d += elm.Line().right().at(node_after).length(4)
    node_r3 = (node_after[0]+4, H)  # (13, H)

    # R3 (vertical)
    d += elm.Resistor().down().at(node_r3).length(H).label('$R_3$\n50 kΩ', loc='right')

    # Fio superior fechando
    d += elm.Line().right().at(node_r3).length(3)

    # Sinal de tensão v no capacitor
    d += elm.Gap().down().at((node_after[0]-0.6, H)).length(H).label(['+', '$v$', '−'], color='darkgreen')

print("Gerado Q2 t<0")

# ============================================================
# Q2 CIRCUITO t > 0: K1 ABERTA  (descarga RC)
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q2_circuito_t_depois.png"), show=False) as d:
    d.config(unit=4.0, fontsize=15)

    H = 6  # altura

    # Fio inferior
    d += elm.Line().right().at((0,0)).length(8)

    # C1 (vertical, esquerda) com tensão inicial
    d += elm.Capacitor().up().at((0,0)).length(H).label('$C_1$\n$v(0)=200$ V', loc='left')
    d += elm.Dot().at((0,H))

    # Fio superior
    d += elm.Line().right().at((0,H)).length(8)

    # R3 (vertical, direita)
    d += elm.Resistor().down().at((8,H)).length(H).label('$R_3$\n50 kΩ', loc='right')

    # Sinal de tensão v_o
    d += elm.Gap().down().at((4.5, H)).length(H).label(['+', '$v_0(t)$', '−'], color='darkgreen')

    # Label K1 aberta
    d += elm.Label().at((4, H+0.6)).label('K₁ ABERTA — descarga livre', color='red')

print("Gerado Q2 t>0")
