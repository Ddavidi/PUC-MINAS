import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_pratico_7_10.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Left loop
    # 15V Source
    d += elm.SourceV().up().label('15 V', loc='left')
    node_top_left = d.here
    
    # Top resistor
    d += elm.Resistor().right().label('2 Ω')
    node_top_mid = d.here
    
    # Capacitor branch
    d += elm.Capacitor().down().label('1/3 F', loc='bot').label(('+', 'v', '-'), loc='left')
    node_bot_mid = d.here
    
    # Bottom wire left
    d += elm.Line().left().tox(node_top_left)
    
    # Right loop (starting from top mid)
    d += elm.Switch().right().at(node_top_mid).label('t = 0\n(fecha)', loc='top')
    node_top_sw = d.here
    
    # Resistor 6 ohm
    d += elm.Resistor().right().label('6 Ω')
    node_top_right = d.here
    
    # 7.5V Source
    d += elm.SourceV().down().label('7,5 V', loc='bot').reverse() # Reverse to make + on top
    node_bot_right = d.here
    
    # Bottom wire right
    d += elm.Line().left().tox(node_bot_mid)

print("Gerado problema_pratico_7_10.png")
