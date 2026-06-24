import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_14.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Start at top middle node
    top_mid = (0, 0)
    d += elm.Dot().at(top_mid)
    
    # Middle Inductor
    d += elm.Inductor2().down().at(top_mid).label('5 mH', loc='bottom')
    bot_mid = d.here
    d += elm.Dot().at(bot_mid)
    
    # Left side
    d += elm.Resistor().left().at(top_mid).label('20 kΩ', loc='top')
    top_left = d.here
    d += elm.Resistor().down().at(top_left).label('40 kΩ', loc='bot').toy(bot_mid[1])
    bot_left = d.here
    d += elm.Line().right().at(bot_left).tox(bot_mid[0])
    
    # Right side
    d += elm.Resistor().right().at(top_mid).label('10 kΩ', loc='top')
    top_right = d.here
    d += elm.Resistor().down().at(top_right).label('30 kΩ', loc='bottom').toy(bot_mid[1])
    bot_right = d.here
    d += elm.Line().left().at(bot_right).tox(bot_mid[0])

print("Gerado problema_7_14.png")
