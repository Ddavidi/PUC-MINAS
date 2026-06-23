import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_1.png"), show=False) as d:
    d.config(unit=3)
    d += elm.Line().right().length(1)
    node1 = d.here
    d.push()
    d += elm.Resistor().down().label('12Ω')
    bot1 = d.here
    d.pop()
    d += elm.Line().right().length(2)
    node1_b = d.here
    d.push()
    d += elm.Resistor().down().label('6Ω').label('+ vx -', loc='bot') # actually vx is across it
    bot2 = d.here
    d.pop()
    d += elm.Resistor().right().label('8Ω').label('io →', loc='top')
    node2 = d.here
    d += elm.Capacitor().down().label('1/3 F').label('+ vC -', loc='bot')
    bot3 = d.here
    
    d += elm.Line().left().tox(bot2)
    d += elm.Line().left().tox(bot1)
    d += elm.Line().left().to((0,-3)) # rough ground line
