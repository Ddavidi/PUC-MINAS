import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "usuario_thevenin_1_original.png"), show=False) as d:
    d += elm.SourceV().up().label('4V').reverse()
    d += elm.Line().right().length(1)
    d += elm.Resistor().right().label('2Ω')
    d.push()
    d += elm.SourceI().down().reverse().label('2A')
    d += elm.Line().left().length(1+3)
    d.pop()
    d += elm.Resistor().right().label('3Ω')
    d += elm.Dot().label('a', loc='right')
    d += elm.Resistor().down().label('R1')
    d += elm.Dot().label('b', loc='right')
    d += elm.Line().left().length(3)

with schemdraw.Drawing(file=os.path.join(img_dir, "usuario_thevenin_1_eq.png"), show=False) as d:
    d += elm.SourceV().up().label('8V').reverse()
    d += elm.Resistor().right().label('5Ω')
    d += elm.Dot().label('a', loc='right')
    d += elm.Resistor().down().label('R1')
    d += elm.Dot().label('b', loc='right')
    d += elm.Line().left().length(3)
