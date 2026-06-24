import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_3.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # 100 pF Capacitor (left)
    d += elm.Capacitor().up().label('100 pF', loc='left')
    top_left = d.here
    
    # 10 k ohm resistor (top wire)
    d += elm.Resistor().right().label('10 kΩ')
    top_mid = d.here
    
    # 40 k ohm resistor (middle vertical)
    d += elm.Resistor().down().label('40 kΩ', loc='bot')
    bot_mid = d.here
    
    # Bottom wire connecting mid to left
    d += elm.Line().left().tox(top_left)
    
    # 20 k ohm resistor (top wire right)
    d += elm.Resistor().right().at(top_mid).label('20 kΩ')
    top_right = d.here
    
    # 30 k ohm resistor (right vertical)
    d += elm.Resistor().down().label('30 kΩ', loc='bot')
    bot_right = d.here
    
    # Bottom wire connecting right to mid
    d += elm.Line().left().tox(bot_mid)

print("Gerado problema_7_3.png")
