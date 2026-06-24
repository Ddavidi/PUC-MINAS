import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_3_req2.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Start at top left (0, 3)
    d += elm.Dot(open=True).at((0, 3))
    top_term = d.here
    
    # Gap with label
    d += elm.Gap().down().label('Req', loc='left').length(3)
    
    d += elm.Dot(open=True)
    bot_term = d.here
    
    # 10 k ohm resistor (top wire)
    d += elm.Resistor().right().at(top_term).label('10 kΩ')
    top_mid = d.here
    
    # Parallel combo (40 || 50)
    d += elm.Resistor().down().label('22,22 kΩ\n(40||50)', color='red').color('red')
    bot_mid = d.here
    
    # Bottom wire
    d += elm.Line().left().at(bot_mid).tox(bot_term)

print("Gerado problema_7_3_req2.png")
