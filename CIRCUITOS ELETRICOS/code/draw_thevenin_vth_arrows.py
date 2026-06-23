import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "thevenin_vth_arrows.png"), show=False) as d:
    d += elm.SourceV().up().label('32V')
    # Resistor com seta de corrente saindo do Nó C para a esquerda
    d += elm.Resistor().right().label('4Ω').label('← I', loc='top', color='red')
    d += elm.Dot().label('Nó C', loc='top')
    
    d.push()
    # Resistor descendo com seta de corrente descendo
    d += elm.Resistor().down().label('12Ω').label('I ↓', loc='right', color='red')
    d += elm.Line().left()
    d += elm.Ground()
    d.pop()
    
    d += elm.Line().right().length(2)
    
    d.push()
    # Fonte de corrente entrando
    d += elm.SourceI().down().reverse().label('2A').label('↑ 2A\n(Entrando)', loc='right', color='blue')
    d += elm.Line().left().length(2)
    d.pop()
    
    # Ramo A com zero corrente
    d += elm.Resistor().right().label('1Ω\n(i=0A)', color='red')
    d += elm.Dot().label('A (+Vth)', loc='right')
    d += elm.Line().down().length(3).color('white')
    d += elm.Dot().label('B (-Vth)', loc='right')
    d += elm.Line().left().length(3 + 2 + 3)
