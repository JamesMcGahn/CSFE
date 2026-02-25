from graph import Graph
from kahns import kahns


def is_topo_ordered(g: Graph, ordering: list[int]) -> bool:
    if len(ordering) != g.num_nodes:
        return False

    index_to_pos: list[int] = [-1] * g.num_nodes

    for pos in range(g.num_nodes):
        current: int = ordering[pos]
        if index_to_pos[current] != -1:
            return False

        index_to_pos[current] = pos

    for n in g.nodes:
        for edge in n.get_edge_list():
            if index_to_pos[edge.to_node] <= index_to_pos[n.index]:
                return False

    return True


def sort_forward_pointers(options: list[list[int]]) -> list[int]:
    num_nodes: int = len(options)
    g: Graph = Graph(num_nodes)
    for current in range(num_nodes):
        for next_index in options[current]:
            if next_index != -1:
                g.insert_edge(current, next_index, 1.0)
    return kahns(g)
