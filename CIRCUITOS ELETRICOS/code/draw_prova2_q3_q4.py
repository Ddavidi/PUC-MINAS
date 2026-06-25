import schemdraw
import schemdraw.elements as elm
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

# ============================================================
# Q3: Circuito RLC Serie
# ============================================================
with schemdraw.Drawing(file=os.path.join(img_dir, "prova2_q3_circuito_rlc.png"), show=False) as d:
    d.config(unit=5.0, fontsize=16)

    # Fonte senoidal
    d += elm.SourceSin().up().at((0,0)).label('$V_s$\n220∠0° V\n60 Hz', loc='left')
    top_left = d.here

    # Resistor
    d += elm.Resistor().right().at(top_left).label('R\n80 Ω', loc='top').length(4)

    # Indutor
    d += elm.Inductor2().right().label('L\n550 mH', loc='top').length(4)

    # Capacitor
    d += elm.Capacitor().right().label('C\n5 μF', loc='top').length(4)
    top_right = d.here

    # Fio de volta
    d += elm.Line().down().at(top_right).toy(0)
    d += elm.Line().left().at((top_right[0], 0)).tox(0)

    # Seta de corrente
    d += elm.Line(arrow='->').right().at((1.5, top_left[1]+0.5)).length(2).color('blue').label('$I$', loc='top')

print("Gerado Q3")

# ============================================================
# Q4: Diagrama de potencias
# ============================================================
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(9, 5))
ax.set_aspect('equal')

P = 6700
Q = 972
S = np.sqrt(P**2 + Q**2)
theta = np.degrees(np.arctan(Q/P))

# Triangulo
ax.annotate('', xy=(P, Q), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='purple', lw=2))
ax.annotate('', xy=(P, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='blue', lw=2))
ax.annotate('', xy=(P, Q), xytext=(P, 0),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))

# Labels
ax.text(P/2, -250, f'P = {P} W', ha='center', fontsize=13, color='blue', fontweight='bold')
ax.text(P+150, Q/2, f'Q = {Q:.0f} VAr\n(indutivo)', ha='left', fontsize=13, color='red', fontweight='bold')
ax.text(P/2 - 400, Q/2 + 200, f'S = {S:.1f} VA', ha='center', fontsize=13, color='purple', fontweight='bold')

# Angulo
arc = patches.Arc((0,0), 1400, 1400, angle=0, theta1=0, theta2=theta, color='gray', lw=1.5)
ax.add_patch(arc)
ax.text(750, 200, f'θ = {theta:.1f}°', fontsize=12, color='gray')
ax.text(700, 130, f'FP = {P/S:.3f}', fontsize=12, color='gray')

ax.set_xlim(-300, P+800)
ax.set_ylim(-400, Q+400)
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.set_title('Triângulo de Potências — Carga Total (Q4)', fontsize=14, fontweight='bold')
ax.set_xlabel('P (W)', fontsize=12)
ax.set_ylabel('Q (VAr)', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(img_dir, "prova2_q4_triangulo.png"), dpi=120)
plt.close()
print("Gerado Q4 triangulo")
