import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_4.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # 40V source (starts at 0,0, goes to 0,3)
    d += elm.SourceV().up().at((0,0)).label('40 V', loc='left')
    
    # 5 k ohm resistor (top wire, from 0,3 to 3,3)
    d += elm.Resistor().right().label('5 kΩ')
    node_a = d.here
    
    # Node B is below Node A (at 3, 1.5)
    node_b = (node_a[0], node_a[1] - 1.5)
    
    # 2k ohm resistor from Node B down to bottom wire (from 3, 1.5 to 3, 0)
    d += elm.Resistor().down().at(node_b).label('2 kΩ', loc='bot').toy(0)
    
    # Right wire and Capacitor (from 6,0 to 6,3)
    d += elm.Capacitor().up().at((6,0)).label('10 μF', loc='right').toy(3)
    node_c = d.here
    
    # Top right wire from capacitor to hinge (from 6,3 to 4.5, 3)
    d += elm.Line().left().at(node_c).tox(4.5)
    hinge = d.here
    
    # Switch lever (from Hinge to Node A)
    # The book draws it slightly angled. Let's draw it from Hinge to slightly above A
    lever_tip = (node_a[0] + 0.1, node_a[1] + 0.5)
    d += elm.Line().at(hinge).to(lever_tip)
    
    # Switch labels
    d += elm.Label().at((node_a[0]+0.2, node_a[1]+0.2)).label('A')
    d += elm.Label().at((node_b[0]-0.3, node_b[1])).label('B')
    
    # Arrow for switch movement
    import schemdraw.util as util
    d += elm.Arc2(arrow='->').at(lever_tip).to((node_b[0], node_b[1]+0.2))
    
    # Bottom wire (from 6,0 to 0,0)
    d += elm.Line().left().at((6,0)).tox(0)
    
    # Polarity labels for the capacitor
    d += elm.Label().at((5.7, 2.5)).label('+')
    d += elm.Label().at((5.7, 1.5)).label('v')
    d += elm.Label().at((5.7, 0.5)).label('-')

print("Gerado problema_7_4.png")
