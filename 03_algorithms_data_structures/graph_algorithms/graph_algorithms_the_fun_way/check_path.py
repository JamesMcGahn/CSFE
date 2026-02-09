from graph import Graph
from edge import Edge


def check_node_path_vald(g: Graph, path: list) -> bool:
    num_nodes_on_path: int = len(path)
    if num_nodes_on_path == 0:
        return True
    prev_node: int = path[0]

    if prev_node < 0 or prev_node >= g.num_nodes:
        return False

    for step in range(1, num_nodes_on_path):
        next_node: int = path[step]
        if not g.is_edge(prev_node, next_node):
            return False
        prev_node = next_node
    return True


def check_edge_path_valid(g: Graph, path: list[Edge]) -> bool:
    if len(path) == 0:
        return True

    prev_node: int = path[0].from_node
    if prev_node < 0 or prev_node >= g.num_nodes:
        return False

    for edge in path:
        if edge.from_node != prev_node:
            return False

        next_node: int = edge.to_node
        if not g.is_edge(prev_node, next_node):
            return False

        prev_node = next_node

    return True


def check_last_path_valid(g: Graph, last: list[int]) -> bool:
    if len(last) != g.num_nodes:
        return False

    for to_node, from_node in enumerate(last):
        if from_node != -1 and not g.is_edge(from_node, to_node):
            return False

    return True
