import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_2.png"), show=False) as d:
    d.config(unit=4, fontsize=14)
    
    # Inicia na base da fonte
    start_point = d.here
    d += elm.SourceV().up().label('24V', loc='left')
    
    # Fio superior com resistor 6 e chave
    d += elm.Resistor().right().label('6Ω', loc='bot')
    d += elm.Switch().right().label('t=0', loc='top')
    top_mid = d.here
    
    # Ramo do Capacitor
    d.push()
    d += elm.Capacitor().down().label('1/6 F', loc='bot').label(('+', '$v$', '-'), loc='top', color='blue')
    d.pop()
    
    # Fio superior ate o 12 ohm
    d += elm.Line().right().length(2)
    
    # Ramo 12 ohm
    d.push()
    d += elm.Resistor().down().label('12Ω', loc='bot')
    d.pop()
    
    # Fio superior ate o 4 ohm
    d += elm.Line().right().length(2)
    
    # Ramo 4 ohm
    d += elm.Resistor().down().label('4Ω', loc='bot')
    
    # Fechando o circuito embaixo (volta até o start_point)
    d += elm.Line().left().tox(top_mid)
    d += elm.Line().left().tox(start_point)
