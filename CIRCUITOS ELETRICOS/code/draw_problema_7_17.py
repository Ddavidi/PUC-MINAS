import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_17.png"), show=False) as d:
    d.config(unit=3.0, fontsize=16)
    
    # Fio inferior
    d += elm.Line().right().at((0,0)).length(6)
    
    # Ramo esquerdo (Fonte)
    d += elm.SourceV().up().at((0,0)).label('v(t)', loc='left')
    top_left = d.here
    
    # Ramo superior (Resistor 1 ohm)
    d += elm.Resistor().right().at(top_left).label('1 Ω', loc='top').length(3)
    top_mid = d.here
    
    # Ramo do meio (Resistor 3 ohm + Indutor 1/4 H)
    d += elm.Resistor().down().at(top_mid).label('3 Ω', loc='left').length(1.5)
    mid_node = d.here
    d += elm.Inductor2().down().at(mid_node).label('1/4 H', loc='left').toy(0)
    bot_mid = (top_mid[0], 0)
    
    # Seta de corrente
    d += elm.Line(arrow='->').down().at((top_mid[0]+0.8, top_mid[1]-0.2)).length(1).color('red').label('$i(t)$', loc='right')
    
    # Terminais abertos na direita
    d += elm.Line().right().at(top_mid).length(3)
    top_right = d.here
    d += elm.Dot(open=True)
    
    d += elm.Line().right().at(bot_mid).length(3)
    bot_right = d.here
    d += elm.Dot(open=True)
    
    # Label do v_o(t)
    d += elm.Gap().down().at(top_right).toy(0).label(['+', '$v_o(t)$', '-'])

print("Gerado problema_7_17.png")
