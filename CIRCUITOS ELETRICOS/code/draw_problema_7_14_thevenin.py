import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_14_thevenin.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Start at top middle node
    top_mid = (0, 0)
    d += elm.Dot(open=True).at(top_mid).label('A', loc='top', color='green')
    
    # Gap for inductor
    d += elm.Gap().down().at(top_mid).label('Visão para $R_{eq}$', loc='bottom', color='green')
    bot_mid = d.here
    d += elm.Dot(open=True).at(bot_mid).label('B', loc='bottom', color='green')
    
    # Left side (Active blue)
    d += elm.Resistor().left().at(top_mid).label('20 kΩ', loc='top').color('blue')
    top_left = d.here
    d += elm.Resistor().down().at(top_left).label('40 kΩ', loc='bot').toy(bot_mid[1]).color('blue')
    bot_left = d.here
    d += elm.Line().right().at(bot_left).tox(bot_mid[0]).color('blue')
    
    # Right side (Active blue)
    d += elm.Resistor().right().at(top_mid).label('10 kΩ', loc='top').color('blue')
    top_right = d.here
    d += elm.Resistor().down().at(top_right).label('30 kΩ', loc='bottom').toy(bot_mid[1]).color('blue')
    bot_right = d.here
    d += elm.Line().left().at(bot_right).tox(bot_mid[0]).color('blue')

print("Gerado problema_7_14_thevenin.png")
