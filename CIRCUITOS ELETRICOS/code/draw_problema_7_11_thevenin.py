import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_11_thevenin.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Left branch (Source shorted for Thevenin)
    d += elm.Line().up().at((0,0)).label('Fonte\nCurto-circuitada\n(Thevenin)', loc='left', color='purple').color('purple')
    top_left = d.here
    
    # Top wire with 4 ohm resistor (Disconnected part)
    d += elm.Resistor().right().at(top_left).label('4 Ω', loc='top', color='gray').color('gray')
    mid_top1 = d.here
    
    # Switch is OPEN
    d += elm.Switch(action='open').right().at(mid_top1).label('Chave Aberta', loc='top', color='red').color('red')
    mid_top2 = d.here
    
    # Vertical 4 ohm resistor (Active)
    d += elm.Resistor().down().at(mid_top2).label('4 Ω', loc='bot').toy(0).color('blue')
    
    # Inductor removed -> Terminals A and B to look into the circuit for Req
    d += elm.Dot(open=True).at(mid_top2).label('A', loc='top', color='green')
    d += elm.Gap().right().at(mid_top2).label('Visão para $R_{eq}$', loc='top', color='green')
    right_top = d.here
    d += elm.Dot(open=True).at(right_top).label('B', loc='top', color='green')
    
    # Vertical 8 ohm resistor (Active)
    d += elm.Resistor().down().at(right_top).label('8 Ω', loc='bottom').toy(0).color('blue')
    bot_right = d.here
    
    # Bottom wire (Active part)
    d += elm.Line().left().at(bot_right).tox(mid_top2[0]).color('blue')
    # Bottom wire (Disconnected part)
    d += elm.Line().left().at((mid_top2[0], 0)).tox(0).color('purple')

print("Gerado problema_7_11_thevenin.png")
