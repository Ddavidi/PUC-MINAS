import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "exercicio_proposto_cap9_circuito.png"), show=False) as d:
    d.config(unit=3, fontsize=14)
    
    # Fonte CA (subindo)
    d += elm.SourceSin().up().label('110∠0° V\n(Eficaz)', loc='left')
    top_left = d.here
    
    # Resistor
    d += elm.Resistor().right().at(top_left).label('$50\ \Omega$', loc='top')
    r_end = d.here
    
    # Indutor
    d += elm.Inductor().right().at(r_end).label('$150\ mH$', loc='top')
    top_right = d.here
    
    # Capacitor (descendo)
    d += elm.Capacitor().down().at(top_right).label('$20\ \mu F$', loc='bot')
    bot_right = d.here
    
    # Fio fechando embaixo
    d += elm.Line().left().at(bot_right).tox(0)

print("OK: exercicio_proposto_cap9_circuito.png")
