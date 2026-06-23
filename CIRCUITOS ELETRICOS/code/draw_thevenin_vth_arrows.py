import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "thevenin_vth_arrows.png"), show=False) as d:
    # Aumentando o tamanho dos elementos para separar os textos
    d.config(unit=4)
    
    d += elm.SourceV().up().label('32V', loc='left')
    
    d += elm.Line().right().length(1)
    d += elm.Resistor().right().label('4Ω', loc='bot').label('← I', loc='top', color='red')
    d += elm.Line().right().length(1)
    d += elm.Dot().label('Nó C', loc='top', ofst=0.5)
    
    d.push()
    d += elm.Line().down().length(0.8)
    d += elm.Resistor().down().label('12Ω', loc='left').label('I ↓', loc='right', color='red')
    d += elm.Line().down().length(0.8)
    bot_mid1 = d.here
    d += elm.Ground()
    d.pop()
    
    d += elm.Line().right().length(2)
    
    d.push()
    d += elm.Line().down().length(0.8)
    d += elm.SourceI().down().reverse().label('2A', loc='left').label('↑ 2A (Entrando)', loc='right', color='blue')
    bot_mid2 = d.here
    d.pop()
    
    d += elm.Line().right().length(1)
    d += elm.Resistor().right().label('1Ω', loc='top').label('(i=0A)', loc='bot', color='red')
    d += elm.Line().right().length(1)
    d += elm.Dot().label('Terminal A', loc='right')
    
    d += elm.Line().down().toy(bot_mid2).color('white')
    d += elm.Dot().label('Terminal B', loc='right')
    
    d += elm.Line().left().to(bot_mid2)
    d += elm.Line().left().to(bot_mid1)
    d += elm.Line().left().to((0,0))
