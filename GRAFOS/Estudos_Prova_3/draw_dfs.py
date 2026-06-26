import matplotlib.pyplot as plt
import networkx as nx
import os

base_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\GRAFOS\Estudos_Prova_3"

def draw_dfs_cycle():
    G = nx.DiGraph()
    G.add_edges_from([('X', 'Y'), ('Y', 'Z'), ('Z', 'W'), ('W', 'Y')])
    pos = {'X': (0, 1), 'Y': (1, 1), 'Z': (2, 1), 'W': (1.5, 0)}
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightgreen', font_size=12, font_weight='bold', arrowsize=20)
    plt.savefig(os.path.join(base_path, "1_Ordenacao_Topologica", "imagens", "resolvido_dfs.png"))
    plt.close()

draw_dfs_cycle()
