import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_17_thevenin.png"), show=False) as d:
    d.config(unit=3.0, fontsize=16)
    
    # Fio inferior
    d += elm.Line().right().at((0,0)).length(3).color('blue')
    bot_mid = d.here
    
    # Ramo esquerdo (Curto)
    d += elm.Line().up().at((0,0)).color('blue').label('Curto\n$v(t)=0$', loc='left')
    top_left = d.here
    
    # Ramo superior
    d += elm.Resistor().right().at(top_left).label('1 Ω', loc='top').length(3).color('blue')
    top_mid = d.here
    
    # Ramo do meio
    d += elm.Resistor().down().at(top_mid).label('3 Ω', loc='left').length(1.5).color('blue')
    mid_node = d.here
    
    # Terminais de Thevenin
    d += elm.Dot(open=True).at(mid_node).label('A', loc='top', color='green')
    d += elm.Dot(open=True).at(bot_mid).label('B', loc='bottom', color='green')
    d += elm.Label().at((mid_node[0] + 1.2, (mid_node[1] + bot_mid[1])/2)).label('Visão para\n$R_{eq}$', color='green')

print("Gerado problema_7_17_thevenin.png")
