import matplotlib.pyplot as plt
import networkx as nx
import os

base_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\GRAFOS\Estudos_Prova_3"

def draw_graph1():
    G = nx.DiGraph()
    G.add_edges_from([(1,4), (2,4), (2,5), (3,5), (4,6), (5,6)])
    pos = {1: (0, 2), 2: (1, 2), 3: (2, 2), 4: (0.5, 1), 5: (1.5, 1), 6: (1, 0)}
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue', font_size=12, font_weight='bold', arrowsize=20)
    plt.savefig(os.path.join(base_path, "1_Ordenacao_Topologica", "atividades", "resolvido.png"))
    plt.close()

def draw_graph2():
    G = nx.DiGraph()
    G.add_edges_from([('A', 'C'), ('A', 'B'), ('C', 'D'), ('B', 'E'), ('D', 'E')])
    labels = {'A': 'A: Comprar', 'B': 'B: Cortar', 'C': 'C: Pintar', 'D': 'D: Montar', 'E': 'E: Transportar'}
    pos = {'A': (0, 1), 'B': (1, 0), 'C': (1, 2), 'D': (2, 2), 'E': (2, 0)}
    plt.figure(figsize=(8, 4))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=2500, node_color='lightgreen', font_size=10, font_weight='bold', arrowsize=20)
    plt.savefig(os.path.join(base_path, "1_Ordenacao_Topologica", "atividades", "proposto.png"))
    plt.close()

def draw_graph3():
    G = nx.Graph()
    edges = [('A', 'X'), ('A', 'W'), ('B', 'X'), ('B', 'Y'), ('B', 'W'), ('C', 'Y'), ('C', 'Z'), ('D', 'Z')]
    matched = [('A', 'X'), ('C', 'Z')]
    G.add_edges_from(edges)
    pos = {'A': (0, 3), 'B': (0, 2), 'C': (0, 1), 'D': (0, 0), 'X': (1, 3), 'W': (1, 2), 'Y': (1, 1), 'Z': (1, 0)}
    
    plt.figure(figsize=(6, 5))
    nx.draw_networkx_nodes(G, pos, node_size=1200, node_color='lightpink')
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    unmatched = [e for e in edges if e not in matched and (e[1], e[0]) not in matched]
    nx.draw_networkx_edges(G, pos, edgelist=unmatched, style='dashed', alpha=0.5)
    nx.draw_networkx_edges(G, pos, edgelist=matched, width=4, edge_color='black')
    
    plt.savefig(os.path.join(base_path, "2_Emparelhamento_Maximo", "atividades", "resolvido.png"))
    plt.close()

def draw_graph4():
    G = nx.Graph()
    G.add_edges_from([('B', 'A'), ('B', 'C'), ('C', 'D'), ('A', 'D'), ('C', 'E')])
    pos = {'B': (1, 2), 'A': (0, 1), 'C': (2, 1), 'D': (1, 0), 'E': (3, 1)}
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightyellow', font_size=12, font_weight='bold')
    plt.savefig(os.path.join(base_path, "3_Coloracao", "atividades", "resolvido.png"))
    plt.close()

def draw_graph5():
    G = nx.Graph()
    G.add_edges_from([('V1', 'V2'), ('V2', 'V3'), ('V3', 'V4'), ('V4', 'V5'), ('V5', 'V6'), ('V6', 'V1'), ('V2', 'V5')])
    pos = {'V1': (0, 1), 'V2': (1, 1), 'V3': (2, 1), 'V4': (2, 0), 'V5': (1, 0), 'V6': (0, 0)}
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='plum', font_size=12, font_weight='bold')
    plt.savefig(os.path.join(base_path, "3_Coloracao", "atividades", "proposto.png"))
    plt.close()

def draw_graph6():
    G = nx.Graph()
    G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')])
    # Pentagon layout
    pos = nx.circular_layout(G)
    # Fix orientation so A is at top
    pos = {'A': (0, 1), 'B': (0.95, 0.31), 'C': (0.59, -0.81), 'D': (-0.59, -0.81), 'E': (-0.95, 0.31)}
    plt.figure(figsize=(5, 5))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightgrey', font_size=12, font_weight='bold')
    plt.savefig(os.path.join(base_path, "5_Independencia_Dominancia_Cobertura", "atividades", "resolvido.png"))
    plt.close()

def draw_graph7():
    G = nx.Graph()
    G.add_edges_from([('S1', 'S2'), ('S1', 'S3'), ('S2', 'S4'), ('S3', 'S4'), ('S3', 'S5')])
    pos = {'S1': (0, 2), 'S2': (2, 2), 'S3': (0, 1), 'S4': (2, 1), 'S5': (0, 0)}
    plt.figure(figsize=(6, 5))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='peachpuff', font_size=12, font_weight='bold')
    plt.savefig(os.path.join(base_path, "5_Independencia_Dominancia_Cobertura", "atividades", "proposto.png"))
    plt.close()

draw_graph1()
draw_graph2()
draw_graph3()
draw_graph4()
draw_graph5()
draw_graph6()
draw_graph7()
