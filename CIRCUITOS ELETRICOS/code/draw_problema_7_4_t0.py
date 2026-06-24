import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_4_t0.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # 40V source (Gray because it's disconnected)
    d += elm.SourceV().up().at((0,0)).label('40 V', loc='left', color='gray').color('gray')
    
    # 5 k ohm resistor (Gray)
    d += elm.Resistor().right().label('5 kΩ', color='gray').color('gray')
    node_a = d.here # (3,3)
    d += elm.Label().at((node_a[0]+0.2, node_a[1]+0.2)).label('A', color='gray')
    
    # Node B is below Node A (at 3, 1.5)
    node_b = (node_a[0], node_a[1] - 1.5)
    
    # 2k ohm resistor from Node B down to bottom wire
    d += elm.Resistor().down().at(node_b).label('2 kΩ', loc='left').toy(0).color('blue')
    d += elm.Label().at((node_b[0]-0.3, node_b[1])).label('B', color='blue')
    
    # Right wire and Capacitor (from 6,0 to 6,3)
    d += elm.Capacitor().up().at((6,0)).label('10 μF', loc='right').toy(3).color('blue')
    node_c = d.here
    
    # Top right wire from capacitor to hinge (from 6,3 to 4.5, 3)
    d += elm.Line().left().at(node_c).tox(4.5).color('blue')
    hinge = d.here
    
    # Switch lever (from Hinge to Node B)
    d += elm.Line().at(hinge).to(node_b).color('blue')
    
    # Bottom wire (from 6,0 to 0,0)
    # The part from 6 to 3 is blue (active circuit)
    d += elm.Line().left().at((6,0)).tox(3).color('blue')
    # The part from 3 to 0 is gray (disconnected circuit)
    d += elm.Line().left().at((3,0)).tox(0).color('gray')
    
    # Polarity labels for the capacitor
    d += elm.Label().at((5.7, 2.5)).label('+', color='blue')
    d += elm.Label().at((5.7, 1.5)).label('v', color='blue')
    d += elm.Label().at((5.7, 0.5)).label('-', color='blue')
    
    # Label saying "Desconectado"
    d += elm.Label().at((1.5, 2)).label('Desconectado!', color='gray')

print("Gerado problema_7_4_t0.png")
