import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_11_t0.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Left branch (Disconnected)
    d += elm.SourceV().up().at((0,0)).label('24 V', loc='left', color='gray').color('gray')
    top_left = d.here
    d += elm.Resistor().right().at(top_left).label('4 Ω', loc='top', color='gray').color('gray')
    mid_top1 = d.here
    
    # Switch is OPEN
    d += elm.Switch(action='open').right().at(mid_top1).label('Aberta', loc='top', color='red').color('red')
    mid_top2 = d.here
    
    # Vertical 4 ohm resistor (Active)
    d += elm.Resistor().down().at(mid_top2).label('4 Ω', loc='bot').toy(0).color('blue')
    
    # Inductor 4 H (Active)
    d += elm.Inductor2().right().at(mid_top2).label('4 H', loc='top').color('blue')
    right_top = d.here
    
    # Vertical 8 ohm resistor (Active)
    d += elm.Resistor().down().at(right_top).label('8 Ω', loc='bottom').toy(0).color('blue')
    bot_right = d.here
    
    # Current label i_o(t)
    d += elm.Line(arrow='->').down().at((right_top[0]+0.8, right_top[1]-0.5)).length(1).color('blue')
    d += elm.Label().at((right_top[0]+1.3, right_top[1]-1)).label('i_o(t)', color='blue')
    
    # Bottom wire (Active part)
    d += elm.Line().left().at(bot_right).tox(mid_top2[0]).color('blue')
    # Bottom wire (Disconnected part)
    d += elm.Line().left().at((mid_top2[0], 0)).tox(0).color('gray')
    
    d += elm.Label().at((1.5, 2.0)).label('Desconectado!', color='gray')

print("Gerado problema_7_11_t0.png")
