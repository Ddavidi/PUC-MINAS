import os
import schemdraw
import schemdraw.elements as elm

base_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS"
img_dir = os.path.join(base_dir, "_base_dados_ia", "imagens_geradas")
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "cap7_pratico_7_3.png"), show=False) as d:
    d.config(unit=4, fontsize=14)
    
    # Ramo do Indutor
    d.push()
    d += elm.Inductor().down().label('2 H', loc='bot').label('$i$ ↓', loc='top', color='red')
    bot_left = d.here
    d.pop()
    
    # Fio superior com resistor 1 ohm e vx
    d += elm.Resistor().right().label('1Ω', loc='bot').label(('+', '$v_x$', '-'), loc='top', color='blue')
    top_mid = d.here
    
    # Ramo do meio
    d.push()
    d += elm.Resistor().down().length(2).label('2Ω', loc='bot')
    d += elm.SourceControlledV().down().length(2).label('2$v_x$', loc='bot').reverse() # + on top
    # wait, standard SourceControlledV has + on top if drawn up. 
    # Let's verify: if down(), + is usually on the bottom. Let's just draw it down() and see.
    # Actually, we can use label(('+', '2$v_x$', '-')) to be sure, or just draw it up() from the bottom.
    d.pop()
    
    # Let's redraw middle branch to be safe
    d.push()
    d += elm.Resistor().down().length(2).label('2Ω', loc='bot')
    d += elm.SourceControlledV().down().length(2).label(('+', '2$v_x$', '-'), loc='top', color='blue')
    bot_mid = d.here
    d.pop()
    
    # Fio superior para a direita
    d += elm.Line().right().length(2)
    top_right = d.here
    
    # Ramo 6 ohm
    d += elm.Resistor().down().length(4).label('6Ω', loc='bot')
    bot_right = d.here
    
    # Fio inferior
    d += elm.Line().left().tox(bot_mid)
    d += elm.Line().left().tox(bot_left)
