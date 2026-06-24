import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_15_b.png"), show=False) as d:
    d.config(unit=4.0, fontsize=16)
    
    # Ground wire (bottom)
    d += elm.Line().right().length(6)
    bot_right = d.here
    bot_mid = (bot_right[0]-3, bot_right[1])
    bot_left = (bot_right[0]-6, bot_right[1])
    
    # Left branch
    d += elm.Resistor().up().at(bot_left).label('40 Ω', loc='left').length(5)
    top_left = d.here
    
    # Right branch
    d += elm.Resistor().up().at(bot_right).label('160 Ω', loc='right').length(5)
    top_right = d.here
    
    # Middle branch
    # From top_mid down to bot_mid
    top_mid = (bot_mid[0], top_left[1])
    d += elm.Resistor().down().at(top_mid).label('48 Ω', loc='right').length(2.5)
    mid_node = d.here
    d += elm.Inductor2().down().at(mid_node).label('20 mH', loc='right').toy(bot_mid[1])
    
    # Top wire connecting left, mid, right
    d += elm.Line().right().at(top_left).tox(top_right[0])

print("Gerado problema_7_15_b.png")
