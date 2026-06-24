import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_4_v0.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # 40V source
    d += elm.SourceV().up().at((0,0)).label('40 V', loc='left')
    
    # 5 k ohm resistor
    d += elm.Resistor().right().label('5 kΩ')
    node_a = d.here # (3,3)
    
    # Switch is fixed at A, forming a solid line to the right
    d += elm.Line().right().at(node_a).length(3).color('blue').label('Chave em A', loc='top', color='blue')
    top_right = d.here # (6,3)
    
    # Capacitor is an open circuit (gap)
    # Total drop is from Y=3 to Y=0
    d += elm.Line().down().at(top_right).length(0.75)
    d += elm.Dot(open=True)
    d += elm.Gap().down().label(('+', 'v(0)  ', '-'), loc='right').length(1.5)
    d += elm.Dot(open=True)
    d += elm.Line().down().toy(0)
    
    # Bottom wire
    d += elm.Line().left().at((6,0)).tox(0)
    
    # The 2k resistor is left floating!
    node_b = (3, 1.5)
    d += elm.Dot(open=True).at(node_b)
    d += elm.Resistor().down().at(node_b).label('2 kΩ', loc='right').toy(0).color('gray')
    d += elm.Label().at((3, 2)).label('Desconectado!', color='gray')

print("Gerado problema_7_4_v0.png")
