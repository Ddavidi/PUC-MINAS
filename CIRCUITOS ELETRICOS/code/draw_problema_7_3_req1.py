import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_3_req1.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Left open terminals
    d += elm.Line().up().length(0.75)
    d += elm.Dot(open=True)
    d += elm.Gap().down().label('R_eq', loc='left').length(1.5)
    d += elm.Dot(open=True)
    d += elm.Line().down().length(0.75)
    bot_term = d.here
    
    d += elm.Line().up().length(1.5)
    
    # 10 k ohm resistor (top wire)
    d += elm.Resistor().right().label('10 kΩ')
    top_mid = d.here
    
    # 40 k ohm resistor (middle vertical)
    d += elm.Resistor().down().label('40 kΩ', loc='bot')
    bot_mid = d.here
    
    # Series combo (50k)
    d += elm.Resistor().right().at(top_mid).label('50 kΩ\n(20+30)', color='red').color('red')
    d += elm.Line().down().toy(bot_mid).color('red')
    bot_right = d.here
    
    # Bottom wires
    d += elm.Line().left().at(bot_right).tox(bot_mid)
    d += elm.Line().left().at(bot_mid).tox(bot_term)

print("Gerado problema_7_3_req1.png")
