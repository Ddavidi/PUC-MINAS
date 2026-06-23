import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

# Passo de Req
with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_1_req.png"), show=False) as d:
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
    d += elm.Resistor().down().label('6Ω')
    bot2 = d.here
    d.pop()
    d += elm.Resistor().right().label('8Ω')
    node2 = d.here
    
    d.push()
    d += elm.Dot().label('Terminal Sup.', loc='left')
    d += elm.Gap().down().label('Req visto\npelo Cap.', color='blue')
    d += elm.Dot().label('Terminal Inf.', loc='left')
    bot3 = d.here
    d.pop()
    
    d += elm.Line().left().tox(bot2)
    d += elm.Line().left().tox(bot1)
    d += elm.Line().left().to((0,-3))
