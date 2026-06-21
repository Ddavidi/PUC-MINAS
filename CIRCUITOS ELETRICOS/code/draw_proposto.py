import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")

with schemdraw.Drawing(file=os.path.join(img_dir, "thevenin_proposto.png"), show=False) as d:
    d += elm.SourceV().up().label('24V')
    d += elm.Resistor().right().label('3Ω')
    d += elm.Dot().label('Nó C', loc='top')
    d.push()
    d += elm.Resistor().down().label('6Ω')
    d += elm.Line().left()
    d += elm.Ground()
    d.pop()
    d += elm.Line().right().length(2)
    d.push()
    d += elm.SourceI().down().reverse().label('4A')
    d += elm.Line().left().length(2)
    d.pop()
    d += elm.Resistor().right().label('2Ω')
    d += elm.Dot().label('A', loc='right')
    d += elm.Line().down().length(3).color('white')
    d += elm.Dot().label('B', loc='right')
    d += elm.Line().left().length(3 + 2 + 3)
