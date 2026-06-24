import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_18_thevenin.png"), show=False) as d:
    d.config(unit=5.0, fontsize=16)
    
    # Fio inferior
    d += elm.Line().right().at((0,0)).length(6).color('blue')
    bot_right = d.here
    
    # Ramo esquerdo (Curto)
    d += elm.Line().up().at((0,0)).length(6).color('blue').label('Curto\n$v(t)=0$', loc='left')
    node_B_top = d.here
    
    # Divisao do paralelo no topo
    d += elm.Line().up().at(node_B_top).length(1).color('blue')
    split_top_L = d.here
    d += elm.Line().down().at(node_B_top).length(1).color('blue')
    split_bot_L = d.here
    
    # Resistor 2 ohms
    d += elm.Resistor().right().at(split_top_L).label('2 Ω', loc='top').length(4).color('blue')
    split_top_R = d.here
    
    # Buraco do Indutor (Terminais A e B)
    split_bot_R = (split_bot_L[0]+4, split_bot_L[1])
    d += elm.Dot(open=True).at(split_bot_L).label('A', loc='left', color='green')
    d += elm.Dot(open=True).at(split_bot_R).label('B', loc='right', color='green')
    d += elm.Label().at(((split_bot_L[0]+split_bot_R[0])/2, split_bot_L[1])).label('Visão para\n$R_{eq}$', color='green')
    
    # Unindo o paralelo
    d += elm.Line().down().at(split_top_R).toy(node_B_top[1]).color('blue')
    node_A = d.here
    d += elm.Line().up().at(split_bot_R).toy(node_B_top[1]).color('blue')
    
    # Indo para a direita
    d += elm.Line().right().at(node_A).length(2).color('blue')
    top_right = d.here
    
    # Ramo do meio (Resistor 3 ohms)
    d += elm.Resistor().down().at(top_right).label('3 Ω', loc='right').toy(0).color('blue')

print("Gerado problema_7_18_thevenin.png")
