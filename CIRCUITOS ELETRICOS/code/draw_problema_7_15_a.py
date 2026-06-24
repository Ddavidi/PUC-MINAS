import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_15_a.png"), show=False) as d:
    d.config(unit=4.0, fontsize=16)
    
    # Fio terra (base)
    d += elm.Line().right().length(6)
    bot_right = d.here
    bot_left = (bot_right[0]-6, bot_right[1])
    
    # Ramo vertical esquerdo (Resistor 2 ohms)
    d += elm.Resistor().up().at(bot_left).label('2 Ω', loc='left').length(2.5)
    node_C = d.here
    d += elm.Line().up().at(node_C).length(2.5)
    node_G = d.here
    
    # Ramo horizontal superior (Resistor 10 ohms)
    d += elm.Resistor().right().at(node_G).label('10 Ω', loc='top').length(6)
    node_I = d.here
    
    # Ramo horizontal do meio (Resistor 40 ohms)
    d += elm.Resistor().right().at(node_C).label('40 Ω', loc='bottom').length(6)
    node_H = d.here
    
    # Fio conectando a parte direita superior
    d += elm.Line().down().at(node_I).toy(node_H[1])
    
    # Ramo vertical direito inferior (Indutor)
    d += elm.Inductor2().down().at(node_H).label('5 H', loc='right').toy(bot_right[1])

print("Gerado problema_7_15_a.png")
