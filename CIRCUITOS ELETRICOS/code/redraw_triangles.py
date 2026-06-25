import matplotlib.pyplot as plt
import os

img_dir = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\CIRCUITOS ELETRICOS\_base_dados_ia\imagens_geradas"
os.makedirs(img_dir, exist_ok=True)

def draw_triangle(P, Q, S, angle, filename, title):
    fig, ax = plt.subplots(figsize=(7, 5))
    
    # Plot lines
    ax.plot([0, P], [0, 0], 'b-', lw=3)
    ax.plot([P, P], [0, Q], 'r-', lw=3)
    ax.plot([0, P], [0, Q], 'g-', lw=3)
    
    # Dynamic offsets based on values
    p_offset = abs(Q) * 0.08
    q_offset = abs(P) * 0.05
    
    # Annotate P (below the line if Q>0, above if Q<0 to avoid crossing S)
    p_va = 'top' if Q > 0 else 'bottom'
    p_y = -p_offset if Q > 0 else p_offset
    ax.text(P/2, p_y, f"P = {P} W", color='blue', ha='center', va=p_va, fontsize=12, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
    
    # Annotate Q (always to the right of the vertical line)
    ax.text(P + q_offset, Q/2, f"Q = {Q} VAr\n({'Indutivo' if Q>0 else 'Capacitivo'})", color='red', ha='left', va='center', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
    
    # Annotate S (on the other side of the hypotenuse)
    ax.text(P/2 - q_offset, Q/2, f"S = {S} VA", color='green', ha='right', va='center', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
    
    # Angle
    ax.text(P*0.1, Q*0.1, f"{angle}°", fontsize=12, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
    
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    # Add a bit of margin so text isn't cut off
    ax.set_xlim(-abs(P)*0.3, abs(P)*1.6)
    if Q > 0:
        ax.set_ylim(-abs(Q)*0.2, abs(Q)*1.2)
    else:
        ax.set_ylim(-abs(Q)*1.2, abs(Q)*0.2)
        
    ax.grid(True, linestyle='--', alpha=0.4)
    
    # Remove borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(os.path.join(img_dir, filename), dpi=150)
    plt.close()

# Refazendo todos os triângulos com o novo script formatado
draw_triangle(34.86, -140.85, 145.10, -76.11, "prova2_q3_triangulo.png", "Triângulo de Potências (Questão 3)")
draw_triangle(6700, 972, 6770, 8.27, "prova2_q4_triangulo.png", "Triângulo de Potências (Questão 4)")
draw_triangle(6700, 972.8, 6770.2, 8.26, "exemplo_resolvido_cap11_triangulo.png", "Triângulo de Potências - Exemplo Resolvido")
draw_triangle(4000, -3000, 5000, -36.87, "exercicio_proposto_cap11_triangulo.png", "Triângulo de Potências - Exercício Proposto")

print("Triângulos formatados e gerados com sucesso.")
