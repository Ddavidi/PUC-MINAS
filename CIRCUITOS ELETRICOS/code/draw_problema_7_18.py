import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_18.png"), show=False) as d:
    d.config(unit=5.0, fontsize=16)
    
    # Fio inferior
    d += elm.Line().right().at((0,0)).length(6)
    bot_right = d.here
    
    # Ramo esquerdo (Fonte)
    d += elm.Line().up().at((0,0)).length(1.5)
    source_bot = d.here
    d += elm.SourceV().up()
    source_top = d.here
    d += elm.Label().at((-0.8, (source_bot[1]+source_top[1])/2)).label('v(t)')
    d += elm.Line().up().at(source_top).length(1.5)
    node_B_top = d.here
    
    # Divisao do paralelo no topo
    d += elm.Line().up().at(node_B_top).length(1)
    split_top_L = d.here
    d += elm.Line().down().at(node_B_top).length(1)
    split_bot_L = d.here
    
    # Resistor 2 ohms
    d += elm.Resistor().right().at(split_top_L).label('2 Ω', loc='top').length(4)
    split_top_R = d.here
    
    # Indutor 0.4 H
    d += elm.Inductor2().right().at(split_bot_L).label('0,4 H', loc='top').length(4)
    split_bot_R = d.here
    
    # Seta de corrente
    d += elm.Line(arrow='->').right().at((split_bot_L[0]+1, split_bot_L[1]-0.8)).length(2).color('red').label('$i(t)$', loc='bottom')
    
    # Unindo o paralelo
    d += elm.Line().down().at(split_top_R).toy(node_B_top[1])
    node_A = d.here
    d += elm.Line().up().at(split_bot_R).toy(node_B_top[1])
    
    # Indo para a direita
    d += elm.Line().right().at(node_A).length(2)
    top_right = d.here
    
    # Ramo do meio (Resistor 3 ohms)
    d += elm.Resistor().down().at(top_right).label('3 Ω', loc='left').toy(0)
    
    # Terminais abertos na direita
    d += elm.Line().right().at(top_right).length(2)
    term_top = d.here
    d += elm.Dot(open=True)
    
    d += elm.Line().right().at(bot_right).length(2)
    term_bot = d.here
    d += elm.Dot(open=True)
    
    # Label do v_o(t)
    d += elm.Gap().down().at(term_top).toy(0).label(['+', '$v_o(t)$', '-'])

print("Gerado problema_7_18.png")
