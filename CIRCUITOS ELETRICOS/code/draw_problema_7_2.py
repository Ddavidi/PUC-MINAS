import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_2.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # 50V Source (left)
    d += elm.SourceV().up()
    top_left = d.here
    
    # Explicit 50V label to the left of the source
    d += elm.Label().at((top_left[0]-0.8, top_left[1]-1.5)).label('50 V')
    
    # 120 ohm resistor (top wire)
    d += elm.Resistor().right().label('120 Ω')
    top_mid = d.here
    
    # 80 ohm resistor (middle vertical)
    d += elm.Resistor().down().label('80 Ω', loc='bot')
    bot_mid = d.here
    
    # Bottom wire connecting mid to left
    d += elm.Line().left().tox(top_left)
    
    # 12 ohm resistor (top wire right)
    d += elm.Resistor().right().at(top_mid).label('12 Ω')
    top_right = d.here
    
    # Capacitor (right vertical)
    d += elm.Capacitor().down().label('200 mF', loc='bottom')
    bot_right = d.here
    
    # Bottom wire connecting right to mid
    d += elm.Line().left().tox(bot_mid)

print("Gerado problema_7_2.png")
