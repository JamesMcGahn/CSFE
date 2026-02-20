import math
from graph import Graph
from priority_queue import PriorityQueue
from node import Node


def a_star_search(g: Graph, h: list[float], start: int, goal: int) -> list[int]:
    visited: list[bool] = [False] * g.num_nodes
    last: list[int] = [-1] * g.num_nodes
    cost: list[float] = [math.inf] * g.num_nodes
    pq: PriorityQueue = PriorityQueue(min_heap=True)

    pq.enqueue(start, h[start])
    cost[start] = 0.0

    while not pq.is_empty() and not visited[goal]:
        ind: int = pq.dequeue()
        current: Node = g.nodes[ind]
        visited[ind] = True

        for edge in current.get_edge_list():
            neighbor: int = edge.to_node
            if cost[neighbor] > cost[ind] + edge.weight:
                cost[neighbor] = cost[ind] + edge.weight
                last[neighbor] = ind

                est_value: float = cost[neighbor] + h[neighbor]
                if pq.in_queue(neighbor):
                    pq.update_priority(neighbor, est_value)
                else:
                    pq.enqueue(neighbor, est_value)

    return last
