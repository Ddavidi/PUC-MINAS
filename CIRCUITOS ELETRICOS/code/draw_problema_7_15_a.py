import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_15_a.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # We will draw it from top to bottom to make it cleaner
    
    # Top wire with 10 ohm
    d += elm.Line().right().length(1)
    top_node_L = d.here
    d += elm.Resistor().right().label('10 Ω', loc='top').length(3)
    top_node_R = d.here
    d += elm.Line().right().length(1)
    
    # Middle wire with 40 ohm
    d += elm.Line().down().at(top_node_L).length(2)
    mid_node_L = d.here
    d += elm.Resistor().right().at(mid_node_L).label('40 Ω', loc='bottom').tox(top_node_R[0])
    mid_node_R = d.here
    d += elm.Line().up().at(mid_node_R).toy(top_node_R[1])
    
    # Left vertical with 2 ohm
    d += elm.Resistor().down().at(mid_node_L).label('2 Ω', loc='left').length(3)
    bot_node_L = d.here
    
    # Right vertical with 5 H inductor
    d += elm.Inductor2().down().at(mid_node_R).label('5 H', loc='right').toy(bot_node_L[1])
    bot_node_R = d.here
    
    # Bottom wire
    d += elm.Line().left().at(bot_node_R).tox(bot_node_L[0])

print("Gerado problema_7_15_a.png")
