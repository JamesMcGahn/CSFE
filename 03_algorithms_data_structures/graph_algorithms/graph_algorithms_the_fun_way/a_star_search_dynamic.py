from world import World
from priority_queue import PriorityQueue


def a_star_search_dynamic(w: World) -> dict[int, int]:
    visited: dict[int, bool] = {}
    last: dict[int, int] = {}
    cost: dict[int, float] = {}
    pq: PriorityQueue = PriorityQueue(min_heap=True)
    visited_goal: bool = False

    start: int = w.get_start_index()
    visited[start] = False
    last[start] = -1
    pq.enqueue(start, w.get_heuristic(start))
    cost[start] = 0.0

    while not pq.is_empty() and not visited_goal:
        index: int = pq.dequeue()
        visited[index] = True
        visited_goal = w.is_goal(index)

        for other in w.get_neighbors(index):
            c: float = w.get_cost(index, other)
            h: float = w.get_heuristic(other)

            if other not in visited:
                visited[other] = False
                cost[other] = cost[index] + c
                last[other] = index
                pq.enqueue(other, cost[other] + h)
            elif cost[other] > cost[index] + c:
                cost[other] = cost[index] + c
                last[other] = index
                pq.update_priority(other, cost[other] + h)
    return last
