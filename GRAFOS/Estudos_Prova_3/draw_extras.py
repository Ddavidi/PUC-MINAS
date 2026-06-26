import matplotlib.pyplot as plt
import networkx as nx
import os

base_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\GRAFOS\Estudos_Prova_3"

def draw_extra_kahn():
    G = nx.DiGraph()
    G.add_edges_from([('T1', 'T3'), ('T2', 'T3'), ('T2', 'T4'), ('T3', 'T5'), ('T4', 'T5'), ('T5', 'T6')])
    pos = {'T1': (0, 2), 'T2': (0, 0), 'T3': (1, 2), 'T4': (1, 0), 'T5': (2, 1), 'T6': (3, 1)}
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='thistle', font_size=12, font_weight='bold', arrowsize=20)
    plt.savefig(os.path.join(base_path, "1_Ordenacao_Topologica", "imagens", "extra_kahn.png"))
    plt.close()

def draw_extra_dfs():
    G = nx.DiGraph()
    G.add_edges_from([('N1', 'N2'), ('N1', 'N3'), ('N2', 'N4'), ('N3', 'N4'), ('N4', 'N5')])
    pos = {'N1': (0, 1), 'N2': (1, 2), 'N3': (1, 0), 'N4': (2, 1), 'N5': (3, 1)}
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='khaki', font_size=12, font_weight='bold', arrowsize=20)
    plt.savefig(os.path.join(base_path, "1_Ordenacao_Topologica", "imagens", "extra_dfs.png"))
    plt.close()

draw_extra_kahn()
draw_extra_dfs()
