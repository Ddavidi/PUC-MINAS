import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_9_t0.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Left part (Disconnected - Gray)
    d += elm.SourceV().up().at((0,0)).label('6 V', loc='left', color='gray').color('gray')
    top_left = d.here
    
    # Top wire with 2k resistor (Gray)
    d += elm.Resistor().right().at(top_left).label('2 kΩ', loc='top', color='gray').color('gray')
    mid_top = d.here
    
    # Switch is OPEN
    d += elm.Switch(action='open').right().at(mid_top).label('Chave Aberta', loc='top', color='red').color('red')
    right_top = d.here
    
    # 4k resistor (Active - Blue)
    d += elm.Resistor().down().at(right_top).label('4 kΩ', loc='bot').toy(0).color('blue')
    bot_right1 = d.here
    
    # Polarity for v_o across the 4k resistor
    d += elm.Label().at((right_top[0]-0.4, right_top[1]-0.5)).label('+', color='blue')
    d += elm.Label().at((right_top[0]-0.4, right_top[1]-1.5)).label('v_o(t)', color='blue')
    d += elm.Label().at((right_top[0]-0.4, right_top[1]-2.5)).label('-', color='blue')
    
    # Capacitor (Active - Blue)
    d += elm.Line().right().at(right_top).length(2).color('blue')
    far_right_top = d.here
    d += elm.Capacitor().down().at(far_right_top).label('3 mF', loc='bottom').toy(0).color('blue')
    far_right_bot = d.here
    
    # Bottom wire for the active circuit (Blue)
    d += elm.Line().left().at(far_right_bot).tox(bot_right1).color('blue')
    
    # Bottom wire for the disconnected circuit (Gray)
    d += elm.Line().left().at(bot_right1).tox(0).color('gray')
    
    # Disconnected text
    d += elm.Label().at((1.5, 2.0)).label('Desconectado!', color='gray')

print("Gerado problema_7_9_t0.png")
