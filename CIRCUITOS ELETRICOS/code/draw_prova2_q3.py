import schemdraw
import schemdraw.elements as elm
import os
import math

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

# 1. Circuito RLC
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q3_circuito.png"), show=False) as d:
    d.config(unit=3, fontsize=14)
    d += elm.SourceSin().up().label('220∠0° V (rms)', loc='left')
    top = d.here
    d += elm.Resistor().right().at(top).label('R = 80 Ω')
    d += elm.Inductor().right().label('L = 550 mH')
    d += elm.Capacitor().down().label('C = 5 μF', loc='bot')
    bot = d.here
    d += elm.Line().left().at(bot).tox(0)

print("OK: prova2_q3_circuito.png")

# 2. Triângulo de Potência
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q3_triangulo.png"), show=False) as d:
    d.config(unit=1, fontsize=14)
    
    # Base = P = 34.86 W
    # Altura = Q = -140.85 VAr (para baixo)
    # Hipotenusa = S = 145.10 VA
    
    # Fator de escala visual
    scale = 0.03
    p_len = 34.86 * scale
    q_len = 140.85 * scale
    
    # Origem
    d += elm.Dot().label('Origem')
    orig = d.here
    
    # Reta da Potência Ativa (P) - Horizontal
    d += elm.Line().right().length(p_len).label('P = 34,86 W', loc='top')
    p_end = d.here
    
    # Reta da Potência Reativa (Q) - Vertical para baixo (capacitivo)
    d += elm.Line().down().at(p_end).length(q_len).label('Q = -140,85 VAr\n(Capacitivo)', loc='right')
    q_end = d.here
    
    # Reta da Potência Aparente (S) - Hipotenusa
    d += elm.Line().at(orig).to(q_end).label('S = 145,10 VA', loc='bot').color('red')
    
    # Angulo
    d += elm.Arc2(r=0.4, theta1=-76.11, theta2=0).at(orig).label('θ = -76,11°', loc='right')

print("OK: prova2_q3_triangulo.png")
