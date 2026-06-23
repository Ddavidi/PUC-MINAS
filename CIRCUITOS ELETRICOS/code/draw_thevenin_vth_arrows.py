import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "thevenin_vth_arrows.png"), show=False) as d:
    d += elm.SourceV().up().label('32V', loc='left')
    
    # Resistor 4 ohms: Valor embaixo, Seta de corrente vermelha em cima
    d += elm.Resistor().right().label('4Ω', loc='bot').label('← I fugindo', loc='top', color='red')
    d += elm.Dot().label('Nó C', loc='top')
    
    d.push()
    # Resistor 12 ohms: Valor na esquerda, Seta vermelha na direita
    d += elm.Resistor().down().label('12Ω', loc='left').label('I fugindo ↓', loc='right', color='red')
    d += elm.Line().left()
    d += elm.Ground()
    d.pop()
    
    d += elm.Line().right().length(2)
    
    d.push()
    # Fonte 2A: Valor na esquerda, explicacao azul na direita
    d += elm.SourceI().down().reverse().label('2A', loc='left').label('↑ 2A\n(Entrando)', loc='right', color='blue')
    d += elm.Line().left().length(2)
    d.pop()
    
    # Ramo A com zero corrente: Valor em cima, texto vermelho embaixo
    d += elm.Resistor().right().label('1Ω', loc='top').label('(i=0A)', loc='bot', color='red')
    d += elm.Dot().label('Terminal A (+Vth)', loc='right')
    d += elm.Line().down().length(3).color('white')
    d += elm.Dot().label('Terminal B (-Vth)', loc='right')
    d += elm.Line().left().length(3 + 2 + 3)
