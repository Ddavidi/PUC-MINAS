import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_pratico_7_12.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # 5 ohm resistor (far left)
    d += elm.Resistor().down().label('5 Ω', loc='left')
    bot_left = d.here
    
    # Bottom wire
    d += elm.Line().right().length(2)
    bot_sw = d.here
    
    # Switch (opening at t=0)
    d += elm.Switch().up().label('t = 0\n(abre)', loc='right')
    top_sw = d.here
    
    # Top wire to 5 ohm
    d += elm.Line().left().tox(bot_left)
    
    # Inductor on top wire (from switch to right)
    d += elm.Inductor().right().at(top_sw).label('1,5 H\n← i', loc='top')
    top_right = d.here
    
    # 10 ohm resistor
    d += elm.Resistor().down().label('10 Ω', loc='right')
    bot_right = d.here
    
    # Bottom wire connecting switch to 10 ohm
    d += elm.Line().left().tox(bot_sw)
    
    # 6A source (far right)
    d += elm.Line().right().at(bot_right).length(2)
    bot_far_right = d.here
    
    d += elm.SourceI().up().label('6 A', loc='right')
    top_far_right = d.here
    
    # Top wire connecting 10 ohm to 6A source
    d += elm.Line().left().tox(top_right)

print("Gerado problema_pratico_7_12.png")
