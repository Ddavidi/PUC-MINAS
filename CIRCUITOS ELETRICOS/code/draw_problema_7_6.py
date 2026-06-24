import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_6.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # 40V source
    d += elm.SourceV().up().at((0,0))
    top_left = d.here
    d += elm.Label().at((top_left[0]-0.8, top_left[1]-1.5)).label('40 V')
    
    # Top wire with Switch (opens at t=0)
    d += elm.Switch().right().label('t = 0\n(abre)', loc='top')
    
    # 10 k ohm resistor
    d += elm.Resistor().right().label('10 kΩ')
    top_mid = d.here
    
    # 2 k ohm resistor (vertical)
    d += elm.Resistor().down().label('2 kΩ', loc='bot').toy(0)
    bot_mid = d.here
    
    # Top wire to capacitor
    d += elm.Line().right().at(top_mid).length(3)
    top_right = d.here
    
    # Capacitor
    d += elm.Capacitor().down().label('40 μF', loc='right').toy(0)
    bot_right = d.here
    
    # Polarity labels for capacitor
    d += elm.Label().at((top_right[0]-0.4, top_right[1]-0.5)).label('+')
    d += elm.Label().at((top_right[0]-0.4, top_right[1]-1.5)).label('v(t)')
    d += elm.Label().at((top_right[0]-0.4, top_right[1]-2.5)).label('-')
    
    # Bottom wire
    d += elm.Line().left().at(bot_right).tox(0)

print("Gerado problema_7_6.png")
