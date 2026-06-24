import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_17.png"), show=False) as d:
    d.config(unit=4.0, fontsize=16)
    
    # Left branch
    d += elm.SourceV().up().at((0,0)).label('v(t)', loc='left')
    top_left = d.here
    
    # Top branch
    d += elm.Resistor().right().at(top_left).label('1 Ω', loc='top')
    top_mid = d.here
    
    # Middle branch
    d += elm.Resistor().down().at(top_mid).label('3 Ω', loc='bottom')
    mid_node = d.here
    d += elm.Inductor2().down().at(mid_node).label('1/4 H', loc='bottom')
    bot_mid = d.here
    
    # Current label
    d += elm.Label().at((top_mid[0] + 0.5, top_mid[1] - 1)).label('$i(t) \downarrow$', color='red')
    
    # Right branch (open terminals)
    d += elm.Line().right().at(top_mid).length(2)
    top_right = d.here
    d += elm.Dot(open=True).at(top_right)
    
    d += elm.Line().right().at(bot_mid).length(2)
    bot_right = d.here
    d += elm.Dot(open=True).at(bot_right)
    
    d += elm.Gap().down().at(top_right).label(['+', '$v_o(t)$', '-'])
    
    # Bottom branch
    d += elm.Line().left().at(bot_mid).tox(0)

print("Gerado problema_7_17.png")
