import math
from typing import Union
from graph import Graph
from floyd_warshall import floyd_warshall
from edge import Edge


# diameter from reconstructing the last matrix and walking each of the paths
def GraphDiameter(g: Graph) -> float:
    last: list[list[int]] = floyd_warshall(g)
    max_cost: float = -math.inf

    for i in range(g.num_nodes):
        for j in range(g.num_nodes):
            cost: float = 0.0
            current: int = j

            while current != i:
                prev: int = last[i][current]
                if prev == -1:
                    return math.inf

                edge: Union[Edge, None] = g.get_edge(prev, current)
                cost = cost + edge.weight
                current = prev

            if cost > max_cost:
                max_cost = cost
    return max_cost
