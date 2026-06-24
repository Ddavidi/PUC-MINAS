import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_15_a.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Ground wire
    d += elm.Line().right().length(4)
    bot_right = d.here
    bot_left = (bot_right[0]-4, bot_right[1])
    
    # Left vertical
    d += elm.Resistor().up().at(bot_left).label('2 Ω', loc='left')
    top_left = d.here
    
    # Right vertical (Inductor)
    d += elm.Inductor2().up().at(bot_right).label('5 H', loc='right').toy(top_left[1])
    top_right = d.here
    
    # Middle horizontal path
    d += elm.Resistor().right().at(top_left).label('40 Ω', loc='bottom').tox(top_right[0])
    
    # Top horizontal path
    d += elm.Line().up().at(top_left).length(1.2)
    top_path_left = d.here
    d += elm.Resistor().right().at(top_path_left).label('10 Ω', loc='top').tox(top_right[0])
    d += elm.Line().down().toy(top_right[1])

print("Gerado problema_7_15_a.png")
