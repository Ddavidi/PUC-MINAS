import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_3_req.png"), show=False) as d:
    d.config(unit=4, fontsize=14)
    
    # Ramo da Fonte de Teste (no lugar do Indutor)
    d.push()
    d += elm.SourceV().down().label('1V', loc='bot').label(('+', '$v_o$', '-'), loc='top', color='red').reverse()
    # Let's draw it from bottom to top to get + on top.
    d.pop()
    
    d.push()
    d += elm.SourceV().up().label('1V\nTeste', loc='bot')
    bot_left = d.here # Wait, up() ends at top
    d.pop()
    
    # Let's just draw it properly:
    start = d.here
    d += elm.SourceV().up().label('1V\nTeste', loc='left').label(('+', '$v_o$', '-'), loc='top', color='red')
    top_left = d.here
    
    # Fio superior com resistor 1 ohm e vx
    d += elm.Resistor().right().label('1Ω', loc='bot').label(('+', '$v_x$', '-'), loc='top', color='blue').label('$i_o$ →', loc='bot', color='red')
    top_mid = d.here
    
    # Ramo do meio
    d.push()
    d += elm.Resistor().down().length(2).label('2Ω', loc='bot')
    d += elm.SourceControlledV().down().length(2).label(('+', '2$v_x$', '-'), loc='top', color='blue')
    bot_mid = d.here
    d.pop()
    
    # Fio superior para a direita
    d += elm.Line().right().length(2)
    
    # Ramo 6 ohm
    d += elm.Resistor().down().length(4).label('6Ω', loc='bot')
    
    # Fio inferior
    d += elm.Line().left().tox(bot_mid)
    d += elm.Line().left().tox(start)
