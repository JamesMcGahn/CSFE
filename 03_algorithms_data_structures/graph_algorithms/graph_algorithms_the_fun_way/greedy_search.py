from priority_queue import PriorityQueue
from graph import Graph
from node import Node


def greedy_search(g: Graph, h: list[float], start: int, goal: int) -> list[int]:
    visited: list[bool] = [False] * g.num_nodes
    last: list[int] = [-1] * g.num_nodes
    pq: PriorityQueue = PriorityQueue(min_heap=True)

    pq.enqueue(start, h[start])

    while not pq.is_empty() and not visited[goal]:
        ind: int = pq.dequeue()
        current: Node = g.nodes[ind]
        visited[ind] = True

        for edge in current.get_edge_list():
            neighbor: int = edge.to_node
            if not visited[neighbor] and not pq.in_queue(neighbor):
                pq.enqueue(neighbor, h[neighbor])
                last[neighbor] = ind
    return last
