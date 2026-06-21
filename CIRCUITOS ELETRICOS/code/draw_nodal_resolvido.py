import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")

with schemdraw.Drawing(file=os.path.join(img_dir, "nodal_proposto_resolvido.png"), show=False) as d:
    d += elm.SourceI().up().label('3A')
    d += elm.Line().right().length(3)
    d += elm.Dot().label('V1\n(8V)', loc='top', color='red')
    d.push()
    d += elm.Resistor().down().label('4Ω')
    d += elm.Line().left().length(3)
    d.pop()
    d += elm.Resistor().right().label('4Ω')
    d += elm.Dot().label('V2\n(4V)', loc='top', color='red')
    d.push()
    d += elm.Resistor().down().label('2Ω')
    d += elm.Line().left().length(3)
    d.pop()
    d += elm.Line().right().length(3)
    d += elm.SourceI().down().reverse().label('1A')
    d += elm.Line().left().length(3+3+3)
