import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "thevenin_vth_arrows.png"), show=False) as d:
    # 32V Source
    source = elm.SourceV().up().label('32V')
    d += source
    
    # Left branch
    d += elm.Line().right().length(1.5).label('← I', color='red')
    d += elm.Resistor().right().length(3).label('4Ω')
    d += elm.Line().right().length(1.5)
    
    # Node C
    d += elm.Dot().label('Nó C', loc='top')
    
    # Down branch 1 (12 ohm)
    d.push()
    d += elm.Line().down().length(1.5).label('I ↓', loc='bot', color='red')
    d += elm.Resistor().down().length(3).label('12Ω')
    bot_mid = d.here
    d += elm.Line().left().tox(source.start)
    d += elm.Ground()
    d.pop()
    
    # Wire to next branch
    d += elm.Line().right().length(2.5)
    
    # Down branch 2 (2A source)
    d.push()
    d += elm.Line().down().length(1.5).label('↑ 2A\n(Entrando)', loc='bot', color='blue')
    d += elm.SourceI().down().reverse().length(3).label('2A')
    d += elm.Line().left().tox(bot_mid)
    d.pop()
    
    # Right branch
    d += elm.Line().right().length(1.5)
    d += elm.Resistor().right().length(3).label('1Ω\n(i=0A)')
    d += elm.Line().right().length(1.5)
    
    # Terminals
    d += elm.Dot().label('Terminal A (+Vth)', loc='right')
    d += elm.Line().down().toy(bot_mid).color('white')
    d += elm.Dot().label('Terminal B (-Vth)', loc='right')
    
    # Bottom wire
    d += elm.Line().left().tox(bot_mid)
