import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_17_thevenin.png"), show=False) as d:
    d.config(unit=4.0, fontsize=16)
    
    # Left branch (Shorted)
    d += elm.Line().up().at((0,0)).color('blue').label('Curto\n$v(t)=0$', loc='left')
    top_left = d.here
    
    # Top branch
    d += elm.Resistor().right().at(top_left).label('1 Ω', loc='top').color('blue')
    top_mid = d.here
    
    # Middle branch (top half)
    d += elm.Resistor().down().at(top_mid).label('3 Ω', loc='bottom').color('blue')
    mid_node = d.here
    
    # Gap for inductor
    bot_mid = (top_mid[0], 0)
    d += elm.Dot(open=True).at(mid_node).label('A', loc='top', color='green')
    d += elm.Dot(open=True).at(bot_mid).label('B', loc='bottom', color='green')
    d += elm.Label().at((mid_node[0] + 1.5, (mid_node[1] + bot_mid[1])/2)).label('Visão para\n$R_{eq}$', color='green')
    
    # Bottom branch
    d += elm.Line().left().at(bot_mid).tox(0).color('blue')

print("Gerado problema_7_17_thevenin.png")
