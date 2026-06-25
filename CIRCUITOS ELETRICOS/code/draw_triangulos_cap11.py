import matplotlib.pyplot as plt
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

def draw_power_triangle(P, Q, S, angle, filename, title, is_inductive):
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Coordinates
    origin = [0, 0]
    p_end = [P, 0]
    q_end = [P, Q]
    
    # Plot vectors
    ax.annotate('', xy=p_end, xytext=origin, arrowprops=dict(arrowstyle="->", color="blue", lw=2))
    ax.annotate('', xy=q_end, xytext=p_end, arrowprops=dict(arrowstyle="->", color="red", lw=2))
    ax.annotate('', xy=q_end, xytext=origin, arrowprops=dict(arrowstyle="->", color="green", lw=2))
    
    # Labels
    # P label
    ax.text(P/2, -0.1 * abs(P), f"P = {P} W", color="blue", ha='center', va='top', fontsize=12)
    # Q label
    ha_q = 'left' if P > 0 else 'right'
    va_q = 'center'
    ax.text(P + 0.05 * P, Q/2, f"Q = {abs(Q)} VAr\n({'Indutivo' if Q>0 else 'Capacitivo'})", color="red", ha=ha_q, va=va_q, fontsize=12)
    # S label
    ax.text(P/2, Q/2 + (0.1*abs(Q) if Q>0 else -0.1*abs(Q)), f"S = {S} VA", color="green", ha='right', va='bottom', fontsize=12)
    
    # Angle arc
    import matplotlib.patches as mpatches
    arc_radius = P * 0.15
    arc_angle = abs(angle)
    if Q > 0:
        arc = mpatches.Arc(origin, arc_radius*2, arc_radius*2, angle=0, theta1=0, theta2=arc_angle, color='black')
        ax.text(arc_radius*1.2, arc_radius*0.2, f"{angle}°", fontsize=10)
    else:
        arc = mpatches.Arc(origin, arc_radius*2, arc_radius*2, angle=0, theta1=-arc_angle, theta2=0, color='black')
        ax.text(arc_radius*1.2, -arc_radius*0.2, f"{angle}°", fontsize=10)
    ax.add_patch(arc)
    
    ax.set_aspect('equal', 'datalim')
    ax.axis('off')
    plt.title(title, pad=20, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, filename), dpi=150)
    plt.close()

# 1. Resolvido (Based on Q4 Prova 2: P=6700, Q=972, S=6770, angle=8.27)
draw_power_triangle(6700, 972, 6770, 8.27, "exemplo_resolvido_cap11_triangulo.png", "Triângulo de Potências - Exemplo Resolvido", True)

# 2. Proposto (Custom: P=4000, Q=-3000, S=5000, angle=-36.87)
draw_power_triangle(4000, -3000, 5000, -36.87, "exercicio_proposto_cap11_triangulo.png", "Triângulo de Potências - Exercício Proposto", False)

print("Imagens criadas com sucesso.")
