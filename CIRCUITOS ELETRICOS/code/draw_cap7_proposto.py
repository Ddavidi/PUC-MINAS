import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_proposto_rl.png"), show=False) as d:
    d.config(unit=3)
    d += elm.SourceV().up().label('10V')
    d += elm.Switch().right().label('t=0 (Fecha)', loc='top')
    d += elm.Resistor().right().label('2Ω')
    d += elm.Inductor().down().label('4H').label('i(t) ↓', loc='bot')
    d += elm.Resistor().left().label('3Ω')
    d += elm.Line().left().to((0,0))
