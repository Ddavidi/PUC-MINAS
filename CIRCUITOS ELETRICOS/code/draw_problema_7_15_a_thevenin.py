import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_15_a_thevenin.png"), show=False) as d:
    d.config(unit=3.0, fontsize=14)
    
    # Ground wire
    d += elm.Line().right().length(4).color('blue')
    bot_right = d.here
    bot_left = (bot_right[0]-4, bot_right[1])
    
    # Left vertical
    d += elm.Resistor().up().at(bot_left).label('2 Ω', loc='left').color('blue')
    top_left = d.here
    
    # Right vertical (Inductor Removed)
    d += elm.Dot(open=True).at(bot_right).label('B', loc='bottom', color='green')
    d += elm.Gap().up().at(bot_right).label('Visão para $R_{eq}$', loc='right', color='green').toy(top_left[1])
    top_right = d.here
    d += elm.Dot(open=True).at(top_right).label('A', loc='top', color='green')
    
    # Middle horizontal path
    d += elm.Resistor().right().at(top_left).label('40 Ω', loc='bottom').tox(top_right[0]).color('blue')
    
    # Top horizontal path
    d += elm.Line().up().at(top_left).length(1.2).color('blue')
    top_path_left = d.here
    d += elm.Resistor().right().at(top_path_left).label('10 Ω', loc='top').tox(top_right[0]).color('blue')
    d += elm.Line().down().toy(top_right[1]).color('blue')

print("Gerado problema_7_15_a_thevenin.png")
