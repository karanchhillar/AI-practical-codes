import networkx as nx
import matplotlib.pyplot as plt

graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((0, 2), 1), ((1, 1), 1)],
    (0, 2): [((0, 1), 1), ((1, 2), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1), ((1, 2), 1), ((2, 1), 1)],
    (1, 2): [((0, 2), 1), ((1, 1), 1)],
    (2, 0): [((2, 1), 1)],
    (2, 1): [((2, 0), 1), ((1, 1), 1), ((2, 2), 1)],
    (2, 2): [((2, 1), 1)]
}

G = nx.Graph()

for node, edges in graph.items():
    G.add_node(node)
    for edge in edges:
        G.add_edge(node, edge[0], weight=edge[1])

pos = {(0, 0): (0, 0), (0, 1): (1, 0), (0, 2): (2, 0),
       (1, 0): (0, 1), (1, 1): (1, 1), (1, 2): (2, 1),
       (2, 0): (0, 2), (2, 1): (1, 2), (2, 2): (2, 2)}

nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_color='black')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
