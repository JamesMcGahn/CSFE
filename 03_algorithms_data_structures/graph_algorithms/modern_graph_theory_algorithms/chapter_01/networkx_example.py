import networkx as nx
import matplotlib.pyplot as plt


# create network

g = nx.Graph()
g.add_nodes_from([1, 3])
g.add_edges_from([(1, 2), (1, 3), (2, 3)])
g.nodes[1]["initial"] = "M"
g.nodes[2]["initial"] = "A"
g.nodes[3]["initial"] = "G"
labels = nx.get_node_attributes(g, "initial")
nx.draw(g, labels=labels, font_weight="bold")
plt.show()
