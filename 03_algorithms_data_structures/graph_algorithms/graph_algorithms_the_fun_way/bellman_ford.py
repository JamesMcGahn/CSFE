from typing import Union
import math
from graph import Graph
from edge import Edge


def bellman_ford(g: Graph, start_index: int) -> Union[list, None]:
    cost: list[float] = [math.inf] * g.num_nodes
    last: list[int] = [-1] * g.num_nodes
    all_edges: list[Edge] = g.make_edge_list()
    cost[start_index] = 0.0

    for _ in range(g.num_nodes - 1):
        for edge in all_edges:
            cost_thr_node: float = cost[edge.from_node] + edge.weight
            if cost_thr_node < cost[edge.to_node]:
                cost[edge.to_node] = cost_thr_node
                last[edge.to_node] = edge.from_node

    for edge in all_edges:
        if cost[edge.to_node] > cost[edge.from_node] + edge.weight:
            return None
    return last
