import matplotlib.pyplot as plt
import networkx as nx
import os

base_path = r"c:\Users\DD\Documents\DD\PUC MINAS\PUC-MINAS\GRAFOS\Estudos_Prova_3\Resolucoes_Lista_Completa\imagens"

def draw_5_2_final():
    G = nx.Graph()
    G.add_nodes_from(['u1', 'u2', 'u3'], bipartite=0)
    G.add_nodes_from(['v1', 'v2', 'v3'], bipartite=1)
    G.add_edges_from([('u1', 'v1'), ('u2', 'v1'), ('u2', 'v3'), ('u3', 'v2')])
    pos = {'u1':(0,2), 'u2':(0,1), 'u3':(0,0), 'v1':(1,2), 'v2':(1,1), 'v3':(1,0)}
    plt.figure(figsize=(4, 3))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightgreen', edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=[('u1', 'v1'), ('u2', 'v3'), ('u3', 'v2')], width=3.0, edge_color='blue')
    plt.savefig(os.path.join(base_path, "bipartite_5_2_final.png"))
    plt.close()

def draw_5_3_final():
    G = nx.Graph()
    G.add_edges_from([('A', 'X'), ('A', 'Y'), ('B', 'Z'), ('C', 'Z'), ('C', 'Y')])
    pos = {'A':(0,2), 'B':(0,1), 'C':(0,0), 'X':(1,2), 'Y':(1,1), 'Z':(1,0)}
    plt.figure(figsize=(4, 3))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightgreen', edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=[('A', 'X'), ('B', 'Z'), ('C', 'Y')], width=3.0, edge_color='blue')
    plt.savefig(os.path.join(base_path, "bipartite_5_3_final.png"))
    plt.close()

def draw_5_4_final():
    G = nx.Graph()
    G.add_edges_from([('A', 'W'), ('A', 'X'), ('B', 'Y'), ('B', 'W'), ('C', 'Y'), ('D', 'Z')])
    pos = {'A':(0,3), 'B':(0,2), 'C':(0,1), 'D':(0,0), 'W':(1,3), 'X':(1,2), 'Y':(1,1), 'Z':(1,0)}
    plt.figure(figsize=(4, 4))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightgreen', edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=[('A', 'X'), ('B', 'W'), ('C', 'Y'), ('D', 'Z')], width=3.0, edge_color='blue')
    plt.savefig(os.path.join(base_path, "bipartite_5_4_final.png"))
    plt.close()

def draw_5_5_final():
    G = nx.Graph()
    # Edges from pdf: U1-V1, U1-V2, U1-V3. U2-V1, U2-V3. U3-V3, U3-V4. U4-V2.
    G.add_edges_from([('U1', 'V2'), ('U1', 'V3'), ('U2', 'V1'), ('U2', 'V3'), ('U3', 'V4'), ('U4', 'V2'), ('U1', 'V1'), ('U3', 'V3')])
    pos = {'U1':(0,3), 'U2':(0,2), 'U3':(0,1), 'U4':(0,0), 'V1':(1,3), 'V2':(1,2), 'V3':(1,1), 'V4':(1,0)}
    plt.figure(figsize=(4, 4))
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightgreen', edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=[('U4', 'V2'), ('U1', 'V1'), ('U2', 'V3'), ('U3', 'V4')], width=3.0, edge_color='blue')
    plt.savefig(os.path.join(base_path, "bipartite_5_5_final.png"))
    plt.close()

draw_5_2_final()
draw_5_3_final()
draw_5_4_final()
draw_5_5_final()
