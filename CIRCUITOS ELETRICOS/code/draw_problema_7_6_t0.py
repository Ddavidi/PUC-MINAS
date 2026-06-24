import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_6_t0.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Left part (Disconnected - Gray)
    d += elm.SourceV().up().at((0,0)).label('40 V', loc='left', color='gray').color('gray')
    
    # Switch is OPEN
    d += elm.Switch(action='open').right().label('Chave Aberta', loc='top', color='red').color('red')
    
    # 10 k ohm resistor (Gray)
    d += elm.Resistor().right().label('10 kΩ', color='gray').color('gray')
    top_mid = d.here
    
    # 2 k ohm resistor (Active - Blue)
    d += elm.Resistor().down().label('2 kΩ', loc='bot').toy(0).color('blue')
    bot_mid = d.here
    
    # Bottom wire for left loop (Gray)
    d += elm.Line().left().at(bot_mid).tox(0).color('gray')
    
    # Top wire to capacitor (Active - Blue)
    d += elm.Line().right().at(top_mid).length(3).color('blue')
    top_right = d.here
    
    # Capacitor (Active - Blue)
    d += elm.Capacitor().down().label('40 μF', loc='right', color='blue').toy(0).color('blue')
    bot_right = d.here
    
    # Polarity labels
    d += elm.Label().at((top_right[0]-0.4, top_right[1]-0.5)).label('+', color='blue')
    d += elm.Label().at((top_right[0]-0.4, top_right[1]-1.5)).label('v(t)', color='blue')
    d += elm.Label().at((top_right[0]-0.4, top_right[1]-2.5)).label('-', color='blue')
    
    # Bottom wire for right loop (Active - Blue)
    d += elm.Line().left().at(bot_right).tox(bot_mid).color('blue')
    
    # Disconnected text
    d += elm.Label().at((1.5, 2.0)).label('Desconectado!', color='gray')

print("Gerado problema_7_6_t0.png")
