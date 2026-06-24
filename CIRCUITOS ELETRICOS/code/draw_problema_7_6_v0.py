import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_6_v0.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # 40V source
    d += elm.SourceV().up().at((0,0)).label('40 V', loc='left')
    
    # Switch is CLOSED (solid line)
    d += elm.Line().right().length(1.5).label('Chave Fechada', loc='top', color='blue').color('blue')
    
    # 10 k ohm resistor
    d += elm.Resistor().right().length(2.5).label('10 kΩ')
    top_mid = d.here
    
    # 2 k ohm resistor (vertical)
    d += elm.Resistor().down().label('2 kΩ', loc='bot').toy(0)
    bot_mid = d.here
    
    # Bottom wire for the left loop
    d += elm.Line().left().at(bot_mid).tox(0)
    
    # Top wire to capacitor
    d += elm.Line().right().at(top_mid).length(3)
    top_right = d.here
    
    # Capacitor is OPEN
    d += elm.Line().down().at(top_right).length(0.75)
    d += elm.Dot(open=True)
    d += elm.Gap().down().label(('+', 'v(0)', '-'), loc='right').length(1.5)
    d += elm.Dot(open=True)
    d += elm.Line().down().toy(0)
    bot_right = d.here
    
    # Bottom wire for capacitor
    d += elm.Line().left().at(bot_right).tox(bot_mid)

print("Gerado problema_7_6_v0.png")
