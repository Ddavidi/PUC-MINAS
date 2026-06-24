import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "revisao_fig_7_79.png"), show=False) as d:
    d.config(unit=3.5, fontsize=14)
    
    # 10V Source
    d += elm.SourceV().up().label('10 V')
    node_top_left = d.here
    
    # 3 ohm resistor
    d += elm.Resistor().right().label('3Ω')
    node_mid = d.here
    
    # Capacitor 7F
    d += elm.Capacitor().down().label('7 F\n+ v(t) -', loc='bot') # using text for polarity
    bot_mid = d.here
    
    # Right branch
    d += elm.Line().right().at(node_mid).length(3)
    node_right = d.here
    d += elm.Resistor().down().length(1.5).label('2Ω', loc='bot')
    
    # Switch opening at t=0
    d += elm.Switch().down().length(1.5).label('t = 0\n(abre)', loc='bot')
    bot_right = d.here
    
    # Bottom wire
    d += elm.Line().left().at(bot_right).tox(bot_mid)
    d += elm.Line().left().at(bot_mid).tox(node_top_left)

print("Gerado revisao_fig_7_79.png")
