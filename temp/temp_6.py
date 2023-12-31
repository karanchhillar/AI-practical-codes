import networkx as nx
import matplotlib.pyplot as plt

graph = {
    (0, 0): [((0, 1), 1)],
    (0, 1): [((0, 0), 1), ((0, 2), 1)],
    (0, 2): [((0, 1), 1), ((0, 3), 1)],
    (0, 3): [((0, 2), 1), ((0, 4), 1)],
    (0, 4): [((0, 3), 1), ((1, 4), 1)],
    (1, 0): [((1, 1), 1)],
    (1, 1): [((1, 0), 1), ((1, 2), 1)],
    (1, 2): [((1, 1), 1), ((1, 3), 1)],
    (1, 3): [((1, 2), 1), ((1, 4), 1)],
    (1, 4): [((0, 4), 1), ((1, 3), 1), ((2, 4), 1)],
    (2, 0): [((2, 1), 1)],
    (2, 1): [((2, 0), 1), ((2, 2), 1)],
    (2, 2): [((2, 1), 1), ((2, 3), 1)],
    (2, 3): [((2, 2), 1), ((2, 4), 1)],
    (2, 4): [((1, 4), 1), ((2, 3), 1), ((3, 4), 1)],
    (3, 0): [((3, 1), 1)],
    (3, 1): [((3, 0), 1), ((3, 2), 1)],
    (3, 2): [((3, 1), 1), ((3, 3), 1)],
    (3, 3): [((3, 2), 1), ((3, 4), 1)],
    (3, 4): [((2, 4), 1), ((3, 3), 1), ((4, 4), 1)],
    (4, 0): [((4, 1), 1)],
    (4, 1): [((4, 0), 1), ((4, 2), 1)],
    (4, 2): [((4, 1), 1), ((4, 3), 1)],
    (4, 3): [((4, 2), 1), ((4, 4), 1)],
    (4, 4): [((3, 4), 1), ((4, 3), 1)]
}

G = nx.Graph()

for node, edges in graph.items():
    G.add_node(node)
    for edge in edges:
        G.add_edge(node, edge[0], weight=edge[1])

pos = {(0, 0): (0, 0), (0, 1): (1, 0), (0, 2): (2, 0), (0, 3): (3, 0), (0, 4): (4, 0),
       (1, 0): (0, 1), (1, 1): (1, 1), (1, 2): (2, 1), (1, 3): (3, 1), (1, 4): (4, 1),
       (2, 0): (0, 2), (2, 1): (1, 2), (2, 2): (2, 2), (2, 3): (3, 2), (2, 4): (4, 2),
       (3, 0): (0, 3), (3, 1): (1, 3), (3, 2): (2, 3), (3, 3): (3, 3), (3, 4): (4, 3),
       (4, 0): (0, 4), (4, 1): (1, 4), (4, 2): (2, 4), (4, 3): (3, 4), (4, 4): (4, 4)}

nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_color='black')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
