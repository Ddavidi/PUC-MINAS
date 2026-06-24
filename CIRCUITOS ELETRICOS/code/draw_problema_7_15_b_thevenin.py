import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_15_b_thevenin.png"), show=False) as d:
    d.config(unit=4.0, fontsize=16)
    
    # Ground wire (bottom)
    d += elm.Line().right().length(6).color('blue')
    bot_right = d.here
    bot_mid = (bot_right[0]-3, bot_right[1])
    bot_left = (bot_right[0]-6, bot_right[1])
    
    # Left branch
    d += elm.Resistor().up().at(bot_left).label('40 Ω', loc='left').length(5).color('blue')
    top_left = d.here
    
    # Right branch
    d += elm.Resistor().up().at(bot_right).label('160 Ω', loc='right').length(5).color('blue')
    top_right = d.here
    
    # Middle branch -> Inductor removed
    top_mid = (bot_mid[0], top_left[1])
    d += elm.Resistor().down().at(top_mid).label('48 Ω', loc='right').length(2.5).color('blue')
    mid_node = d.here
    
    # Gap for inductor (Terminals A and B)
    d += elm.Dot(open=True).at(mid_node).label('A', loc='top', color='green')
    d += elm.Dot(open=True).at(bot_mid).label('B', loc='bottom', color='green')
    d += elm.Label().at((bot_mid[0] + 1.2, (mid_node[1] + bot_mid[1])/2)).label('Visão para\n$R_{eq}$', color='green')
    
    # Top wire connecting left, mid, right
    d += elm.Line().right().at(top_left).tox(top_right[0]).color('blue')

print("Gerado problema_7_15_b_thevenin.png")
