import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_11.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Left branch: 24V source
    d += elm.SourceV().up().at((0,0)).label('24 V', loc='left')
    top_left = d.here
    
    # Top wire: 4 ohm resistor
    d += elm.Resistor().right().at(top_left).label('4 Ω', loc='top')
    mid_top1 = d.here
    
    # Switch (Opens at t=0)
    d += elm.Switch().right().at(mid_top1).label('t = 0\n(abre)', loc='top')
    mid_top2 = d.here
    
    # Vertical 4 ohm resistor
    d += elm.Resistor().down().at(mid_top2).label('4 Ω', loc='bot').toy(0)
    
    # Top wire continues right with 4 H inductor
    d += elm.Inductor2().right().at(mid_top2).label('4 H', loc='top')
    right_top = d.here
    
    # Vertical 8 ohm resistor
    d += elm.Resistor().down().at(right_top).label('8 Ω', loc='bottom').toy(0)
    bot_right = d.here
    
    # Current label i_o pointing down on the right branch
    # We draw an arrow next to it
    d += elm.Line(arrow='->').down().at((right_top[0]+0.8, right_top[1]-0.5)).length(1)
    d += elm.Label().at((right_top[0]+1.1, right_top[1]-1)).label('i_o')
    
    # Bottom wire connecting everything
    d += elm.Line().left().at(bot_right).tox(0)

print("Gerado problema_7_11.png")
