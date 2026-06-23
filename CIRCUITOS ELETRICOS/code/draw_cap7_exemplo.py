import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_exemplo_rc.png"), show=False) as d:
    d.config(unit=3)
    d += elm.SourceV().up().label('24V')
    d += elm.Line().right().length(1)
    d += elm.Switch().right().label('t=0 (Abre)', loc='top')
    d += elm.Resistor().right().label('4Ω')
    top_node = d.here
    d.push()
    d += elm.Capacitor().down().label('0.5F')
    bot_node = d.here
    d.pop()
    d += elm.Line().right().length(2)
    d += elm.Resistor().down().label('12Ω')
    d += elm.Line().left().tox(bot_node)
    d += elm.Line().left().to((0,0))
