import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "revisao_fig_7_79_infinito.png"), show=False) as d:
    d.config(unit=3.5, fontsize=14)
    
    # 10V Source
    d += elm.SourceV().up().label('10 V')
    node_top_left = d.here
    
    # 3 ohm resistor
    d += elm.Resistor().right().label('3Ω')
    node_mid = d.here
    
    # Open Capacitor (Buraco)
    d += elm.Line().down().length(0.5)
    d += elm.Gap().down().label('+ v(∞) -\n(Buraco)', loc='bot').length(2.0)
    d += elm.Line().down().length(0.5)
    bot_mid = d.here
    
    # Dead Branch (Braço Morto - desenhado mais claro/pontilhado)
    d += elm.Line().right().at(node_mid).length(3).style(ls=':')
    node_right = d.here
    d += elm.Resistor().down().length(1.5).label('2Ω\n(Morto)', loc='bot').style(ls=':')
    
    # Switch opened
    d += elm.Switch().down().length(1.5).label('Chave Aberta', loc='bot')
    bot_right = d.here
    
    # Bottom wire
    d += elm.Line().left().at(bot_right).tox(bot_mid).style(ls=':')
    d += elm.Line().left().at(bot_mid).tox(node_top_left)

print("Gerado revisao_fig_7_79_infinito.png")
