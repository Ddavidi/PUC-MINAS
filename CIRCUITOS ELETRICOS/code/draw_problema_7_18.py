import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "problema_7_18.png"), show=False) as d:
    d.config(unit=5.0, fontsize=16)
    
    # Fio inferior
    d += elm.Line().right().at((0,0)).length(8)
    
    # Ramo esquerdo (Fonte)
    d += elm.Line().up().at((0,0)).length(1.5)
    source_bot = d.here
    d += elm.SourceV().up().at(source_bot)
    source_top = d.here
    d += elm.Label().at((-0.8, (source_bot[1]+source_top[1])/2)).label('v(t)')
    d += elm.Line().up().at(source_top).length(1.5)
    top_left = d.here
    
    # Ramo superior
    d += elm.Resistor().right().at(top_left).label('3 Ω', loc='top').length(4)
    top_mid = d.here
    
    # Ramo do meio
    d += elm.Resistor().down().at(top_mid).label('2 Ω', loc='left').length(3)
    mid_node = d.here
    d += elm.Inductor2().down().at(mid_node).label('0,4 H', loc='left').toy(0)
    bot_mid = (top_mid[0], 0)
    
    # Seta de corrente
    d += elm.Line(arrow='->').down().at((top_mid[0]+1.0, top_mid[1]-0.5)).length(2).color('red').label('$i(t)$', loc='right')
    
    # Terminais abertos na direita
    d += elm.Line().right().at(top_mid).length(4)
    top_right = d.here
    d += elm.Dot(open=True)
    
    d += elm.Line().right().at(bot_mid).length(4)
    bot_right = d.here
    d += elm.Dot(open=True)
    
    # Label do v_o(t)
    d += elm.Gap().down().at(top_right).toy(0).label(['+', '$v_o(t)$', '-'])

print("Gerado problema_7_18.png")
