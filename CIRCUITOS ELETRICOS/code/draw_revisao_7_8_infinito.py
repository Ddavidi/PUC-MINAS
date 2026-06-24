import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "revisao_fig_7_80_infinito.png"), show=False) as d:
    d.config(unit=3.5, fontsize=14)
    
    # 10A Source
    d += elm.SourceI().up().label('10 A')
    node_top_left = d.here
    
    # Top wire to R2
    d += elm.Line().right().length(2.5)
    node_top_r2 = d.here
    
    # 2 ohm resistor (bypassed)
    d += elm.Resistor().down().label('2Ω\n(Bypassed)', loc='bot').style(ls=':')
    bot_r2 = d.here
    
    # Top wire to Switch
    d += elm.Line().right().at(node_top_r2).length(2.5)
    node_top_sw = d.here
    
    # Switch CLOSED (Short Circuit)
    d += elm.Line().down().label('Chave Fechada\n(Curto)', loc='bot', color='red').length(3.0).color('red')
    bot_sw = d.here
    
    # Top wire to Inductor
    d += elm.Line().right().at(node_top_sw).length(2.5).style(ls=':')
    node_top_ind = d.here
    
    # Inductor (Wire) and Resistor in series (Bypassed)
    d += elm.Line().down().label('Fio Liso\n(Ex-Indutor)', loc='bot').length(1.5).color('blue').style(ls=':')
    d += elm.Resistor().down().label('3Ω\n↓ i(∞)', loc='bot').length(1.5).style(ls=':')
    bot_ind = d.here
    
    # Bottom wires returning
    d += elm.Line().left().at(bot_ind).tox(bot_sw).style(ls=':')
    d += elm.Line().left().at(bot_sw).tox(bot_r2)
    d += elm.Line().left().at(bot_r2).tox(node_top_left)

print("Gerado revisao_fig_7_80_infinito.png")
