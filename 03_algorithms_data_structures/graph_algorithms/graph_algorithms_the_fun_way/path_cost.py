import math
from edge import Edge


def compute_path_cost_from_edges(path: list[Edge]) -> float:
    if len(path) == 0:
        return 0.0

    cost: float = 0.0
    prev_node: int = path[0].from_node
    for edge in path:
        if edge.from_node != prev_node:
            cost = math.inf
        else:
            cost += edge.weight
        prev_node = edge.to_node
    return cost
