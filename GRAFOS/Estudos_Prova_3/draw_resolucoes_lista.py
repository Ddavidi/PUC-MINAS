import matplotlib.pyplot as plt
import networkx as nx
import os

base_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\GRAFOS\Estudos_Prova_3\Resolucoes_Lista_Completa\imagens"

def draw_kahn_2_2():
    G = nx.DiGraph()
    G.add_edges_from([('A', 'C'), ('C', 'D'), ('B', 'E'), ('D', 'E'), ('E', 'F')])
    pos = {'A': (0, 2), 'B': (0, 0), 'C': (1, 2), 'D': (2, 2), 'E': (2, 0), 'F': (3, 0)}
    plt.figure(figsize=(5, 3))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_weight='bold', arrowsize=20)
    plt.savefig(os.path.join(base_path, "kahn_2_2.png"))
    plt.close()

def draw_bipartite_5_2():
    G = nx.Graph()
    U = ['u1', 'u2', 'u3']
    V = ['v1', 'v2', 'v3']
    G.add_nodes_from(U, bipartite=0)
    G.add_nodes_from(V, bipartite=1)
    G.add_edges_from([('u1', 'v2'), ('u2', 'v1'), ('u2', 'v3'), ('u3', 'v2')])
    pos = {'u1':(0,2), 'u2':(0,1), 'u3':(0,0), 'v1':(1,2), 'v2':(1,1), 'v3':(1,0)}
    plt.figure(figsize=(4, 3))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightgreen')
    nx.draw_networkx_edges(G, pos, edgelist=[('u2', 'v1')], width=3.0, edge_color='blue')
    plt.savefig(os.path.join(base_path, "bipartite_5_2.png"))
    plt.close()

def draw_bipartite_5_3():
    G = nx.Graph()
    G.add_edges_from([('A', 'X'), ('A', 'Y'), ('B', 'Z'), ('C', 'Z'), ('C', 'Y')])
    pos = {'A':(0,2), 'B':(0,1), 'C':(0,0), 'X':(1,2), 'Y':(1,1), 'Z':(1,0)}
    plt.figure(figsize=(4, 3))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightgreen')
    nx.draw_networkx_edges(G, pos, edgelist=[('A', 'X'), ('C', 'Z')], width=3.0, edge_color='blue')
    plt.savefig(os.path.join(base_path, "bipartite_5_3.png"))
    plt.close()

def draw_bipartite_5_4():
    G = nx.Graph()
    G.add_edges_from([('A', 'W'), ('A', 'X'), ('B', 'Y'), ('B', 'W'), ('C', 'Y'), ('D', 'Z')])
    pos = {'A':(0,3), 'B':(0,2), 'C':(0,1), 'D':(0,0), 'W':(1,3), 'X':(1,2), 'Y':(1,1), 'Z':(1,0)}
    plt.figure(figsize=(4, 4))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightgreen')
    nx.draw_networkx_edges(G, pos, edgelist=[('A', 'W'), ('B', 'Y')], width=3.0, edge_color='blue')
    plt.savefig(os.path.join(base_path, "bipartite_5_4.png"))
    plt.close()

def draw_bipartite_5_5():
    G = nx.Graph()
    G.add_edges_from([('U1', 'V2'), ('U1', 'V3'), ('U2', 'V1'), ('U2', 'V3'), ('U3', 'V4'), ('U4', 'V2')])
    pos = {'U1':(0,3), 'U2':(0,2), 'U3':(0,1), 'U4':(0,0), 'V1':(1,3), 'V2':(1,2), 'V3':(1,1), 'V4':(1,0)}
    plt.figure(figsize=(4, 4))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightgreen')
    nx.draw_networkx_edges(G, pos, edgelist=[('U1', 'V2'), ('U2', 'V1'), ('U3', 'V4')], width=3.0, edge_color='blue')
    plt.savefig(os.path.join(base_path, "bipartite_5_5.png"))
    plt.close()

def draw_coloracao_10_4():
    G = nx.wheel_graph(6)
    mapping = {0:'C', 1:'P1', 2:'P2', 3:'P3', 4:'P4', 5:'P5'}
    G = nx.relabel_nodes(G, mapping)
    plt.figure(figsize=(4, 4))
    nx.draw(G, with_labels=True, node_size=1000, node_color='lightcoral', font_weight='bold')
    plt.savefig(os.path.join(base_path, "coloracao_10_4.png"))
    plt.close()

def draw_cobertura_12_1():
    G = nx.Graph()
    G.add_edges_from([('A','B'), ('A','D'), ('B','C'), ('D','C'), ('B','D'), ('C','E'), ('C','F')])
    pos = {'A':(0,1), 'B':(1,2), 'D':(1,0), 'C':(2,1), 'E':(3,2), 'F':(3,0)}
    plt.figure(figsize=(5, 3))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='thistle', font_weight='bold')
    plt.savefig(os.path.join(base_path, "cobertura_12_1.png"))
    plt.close()

def draw_grade_12_2():
    G = nx.grid_2d_graph(3, 2)
    mapping = {(0,1):'A', (1,1):'B', (2,1):'C', (0,0):'D', (1,0):'E', (2,0):'F'}
    G = nx.relabel_nodes(G, mapping)
    pos = {'A':(0,1), 'B':(1,1), 'C':(2,1), 'D':(0,0), 'E':(1,0), 'F':(2,0)}
    plt.figure(figsize=(5, 3))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='thistle', font_weight='bold')
    plt.savefig(os.path.join(base_path, "grade_12_2.png"))
    plt.close()

def draw_roteadores_12_3():
    G = nx.Graph()
    G.add_edges_from([('S1','S2'), ('S2','S3'), ('S1','S4'), ('S4','S2'), ('S2','S5'), ('S5','S3')])
    pos = {'S1':(0,1), 'S2':(1,1), 'S3':(2,1), 'S4':(0.5,0), 'S5':(1.5,0)}
    plt.figure(figsize=(5, 3))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='thistle', font_weight='bold')
    plt.savefig(os.path.join(base_path, "roteadores_12_3.png"))
    plt.close()

def draw_vc_12_5():
    G = nx.Graph()
    G.add_edges_from([('v1','v2'), ('v1','v4'), ('v2','v3'), ('v4','v3'), ('v2','v5'), ('v3','v5')])
    pos = {'v1':(0,1), 'v4':(0,0), 'v2':(1,1), 'v3':(1,0), 'v5':(2,0.5)}
    plt.figure(figsize=(5, 3))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='thistle', font_weight='bold')
    plt.savefig(os.path.join(base_path, "vc_12_5.png"))
    plt.close()

draw_kahn_2_2()
draw_bipartite_5_2()
draw_bipartite_5_3()
draw_bipartite_5_4()
draw_bipartite_5_5()
draw_coloracao_10_4()
draw_cobertura_12_1()
draw_grade_12_2()
draw_roteadores_12_3()
draw_vc_12_5()
