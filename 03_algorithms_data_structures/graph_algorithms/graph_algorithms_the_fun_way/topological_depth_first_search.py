from graph import Graph
from node import Node


def topological_depth_first_search(g: Graph) -> list[int]:
    seen: list[bool] = [False] * g.num_nodes
    s: list[int] = []

    for ind in range(g.num_nodes):
        if not seen[ind]:
            topological_dfs_recursive(g, ind, seen, s)
    s.reverse()
    return s


def topological_dfs_recursive(
    g: Graph, index: int, seen: list[bool], s: list[int]
) -> None:
    seen[index] = True
    current: Node = g.nodes[index]

    for edge in current.get_edge_list():
        neighbor: int = edge.to_node
        if not seen[neighbor]:
            topological_dfs_recursive(g, neighbor, seen, s)
    s.append(index)
