import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

with schemdraw.Drawing(file=os.path.join(img_dir, "atividade_avaliativa_cap9.png"), show=False) as d:
    d.config(unit=3, fontsize=14)
    
    # Fonte CA (subindo)
    d += elm.SourceSin().up().label('220∠-30° V\n(Eficaz)', loc='left')
    top_left = d.here
    
    # Resistor
    d += elm.Resistor().right().at(top_left).length(4).label('$150\ \Omega$', loc='top')
    top_right = d.here
    
    # Indutor (descendo)
    d += elm.Inductor().down().at(top_right).label('$j113.1\ \Omega$\n(300 mH)', loc='bot')
    bot_right = d.here
    
    # Fio fechando embaixo
    d += elm.Line().left().at(bot_right).tox(0)

print("OK: atividade_avaliativa_cap9.png")
