import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_4.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Left loop (40V source)
    bot_left = d.here
    d += elm.SourceV().up().label('40 V', loc='left')
    top_left = d.here
    
    # 5 k ohm resistor (top wire)
    d += elm.Resistor().right().label('5 kΩ')
    node_a = d.here
    
    # Node B is below Node A
    node_b = (node_a[0], node_a[1] - 1.5)
    
    # 2k ohm resistor from Node B down to bottom wire
    d += elm.Resistor().down().at(node_b).label('2 kΩ', loc='bot')
    bot_mid = d.here
    
    # Bottom wire
    d += elm.Line().left().tox(bot_left)
    d += elm.Line().right().at(bot_mid).length(3)
    bot_right = d.here
    
    # Capacitor on the right
    d += elm.Capacitor().up().at(bot_right).label('10 μF', loc='bottom').label(('+', 'v', '-'), loc='top')
    top_right = d.here
    
    # Switch wire from capacitor to pole
    pole = (top_right[0] - 1, top_right[1])
    d += elm.Line().left().at(top_right).to(pole)
    
    # Switch connection (currently at A)
    d += elm.Line().at(pole).to(node_a)
    
    # Labels for switch
    d += elm.Label().at(node_a).label('A', loc='left')
    d += elm.Label().at(node_b).label('B', loc='left')
    d += elm.Label().at(pole).label('t = 0\n(B)', loc='top')
    
    # Arrow showing switch movement
    import schemdraw.util as util
    d += elm.Arc2(arrow='->').at(node_a).to(node_b) # simple curve to indicate switch throw

print("Gerado problema_7_4.png")
