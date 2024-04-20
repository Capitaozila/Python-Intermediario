import networkx as nx
import matplotlib.pyplot as plt

# Cria um grafo vazio
G = nx.Graph()

# Adiciona nós ao grafo
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

#exemplo de entrada com uma matrix 

V = [0,1,2,3,4]
A = [(0,1),(0,2),(1,2),(1,3),(1,2),(2,3),(2,4)]

matrix = [[0,1,1,0,0],
          [1,0,1,1,0],
          [1,1,0,1,1],
          [0,1,1,0,0],
          [0,0,1,0,0]]


# Adiciona arestas ao grafo
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 0)
G.add_edge(1, 3)
G.add_edge(1, 2)
G.add_edge(2, 0)
G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 1)
G.add_edge(3, 2)
G.add_edge(4, 2)

# Desenha o grafo
nx.draw(G, with_labels=True)
plt.show()
