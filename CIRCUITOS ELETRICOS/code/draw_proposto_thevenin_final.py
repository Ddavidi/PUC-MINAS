import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "thevenin_proposto_final.png"), show=False) as d:
    d += elm.Dot().label('A (+)', loc='left')
    d += elm.Resistor().right().label('Rth = 4Ω')
    d += elm.SourceV().down().reverse().label('Vth = 24V')
    d += elm.Line().left()
    d += elm.Dot().label('B (-)', loc='left')
