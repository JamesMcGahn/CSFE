from typing import Union
import math
from graph import Graph
from edge import Edge


def floyd_warshall(g: Graph) -> Union[list[list[int]], None]:
    N: int = g.num_nodes
    cost: list[list[float]] = [[math.inf] * N for _ in range(N)]
    last: list[list[int]] = [[-1] * N for _ in range(N)]

    for from_node in range(N):
        for to_node in range(N):
            if from_node == to_node:
                cost[from_node][to_node] = 0.0
            else:
                edge: Union[Edge, None] = g.get_edge(from_node, to_node)
                if edge is not None:
                    cost[from_node][to_node] = edge.weight
                    last[from_node][to_node] = from_node

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][j] > cost[i][k] + cost[k][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]
                    last[i][j] = last[k][j]

    return last
