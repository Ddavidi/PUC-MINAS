import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_2_v0.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # 50V Source
    d += elm.SourceV().up().label('50 V', loc='left')
    top_left = d.here
    
    # 120 ohm resistor
    d += elm.Resistor().right().label('120 Ω')
    top_mid = d.here
    
    # 80 ohm resistor
    d += elm.Resistor().down().label('80 Ω', loc='bot')
    bot_mid = d.here
    
    # Bottom wire
    d += elm.Line().left().tox(top_left)
    
    # 12 ohm resistor
    d += elm.Resistor().right().at(top_mid).label('12 Ω')
    top_right = d.here
    
    # Open terminals for Capacitor
    d += elm.Line().down().at(top_right).length(0.5)
    d += elm.Dot(open=True)
    d += elm.Gap().down().label(('+', 'v(0)', '-'), loc='right').length(2)
    d += elm.Dot(open=True)
    d += elm.Line().up().length(0.5)
    
    bot_right = d.here
    
    # Connect bottom
    d += elm.Line().left().at(bot_right).tox(bot_mid)

print("Gerado problema_7_2_v0.png")
