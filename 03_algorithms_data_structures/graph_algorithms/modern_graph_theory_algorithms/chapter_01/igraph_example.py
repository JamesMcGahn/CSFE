import igraph as ig


# create network

group = ig.Graph(edges=[(0, 1), (0, 2), (1, 2)], n=3, directed=False)

# plot
ig.plot(
    group,
    bbox=(200, 200),
    vertex_size=40,
    vertex_label=["M", "A", "G"],
    target="example.png",
)
