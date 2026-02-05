from graph import Graph


def clustering_coefficient(graph: Graph, index: int) -> float:
    neighbors: set[int] = graph.nodes[index].get_neighbors()
    num_neighbors: int = len(neighbors)

    count: int = 0
    for n1 in neighbors:
        for edge in graph.nodes[n1].get_edge_list():
            # first check is to guard against double counting
            # as undirected edges appear twice in adjacency lists
            if edge.to_node > n1 and edge.to_node in neighbors:
                count += 1

    total_possible = (num_neighbors * (num_neighbors - 1)) / 2.0
    if total_possible == 0.0:
        return 0.0
    return count / total_possible


def avg_clustering_coefficient(graph: Graph) -> float:
    """
    Provides numerical measure (average) of the local interconnectedness of an undirected graph

    :param graph: Description
    :type graph: Graph
    :return: Description
    :rtype: float
    """
    total: float = 0.0
    for n in range(graph.num_nodes):
        total += clustering_coefficient(graph, n)

    if graph.nodes == 0:
        return 0.0
    return total / graph.num_nodes
