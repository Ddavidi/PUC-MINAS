import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_9_v0.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # 6V source
    d += elm.SourceV().up().at((0,0)).label('6 V', loc='left')
    top_left = d.here
    
    # Top wire with 2k resistor
    d += elm.Resistor().right().at(top_left).label('2 kΩ', loc='top')
    mid_top = d.here
    
    # Switch is CLOSED at t < 0
    d += elm.Line().right().at(mid_top).label('Chave\nFechada', loc='top', color='blue').color('blue')
    right_top = d.here
    
    # 4k resistor (vertical)
    d += elm.Resistor().down().at(right_top).label('4 kΩ', loc='bot').toy(0)
    bot_right1 = d.here
    
    # Polarity for v_o across the 4k resistor
    d += elm.Label().at((right_top[0]-0.4, right_top[1]-0.5)).label('+')
    d += elm.Label().at((right_top[0]-0.4, right_top[1]-1.5)).label('v_o(0)')
    d += elm.Label().at((right_top[0]-0.4, right_top[1]-2.5)).label('-')
    
    # Capacitor is OPEN
    d += elm.Line().right().at(right_top).length(2)
    far_right_top = d.here
    
    d += elm.Line().down().at(far_right_top).length(0.75)
    d += elm.Dot(open=True)
    d += elm.Gap().down().label('Aberto\n(Regime CC)', loc='right').length(1.5)
    d += elm.Dot(open=True)
    d += elm.Line().down().toy(0)
    far_right_bot = d.here
    
    # Bottom wire
    d += elm.Line().left().at(far_right_bot).tox(0)

print("Gerado problema_7_9_v0.png")
