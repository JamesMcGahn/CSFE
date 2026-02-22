import math
from graph import Graph


class World:
    def __init__(self, g: Graph, start_ind: int, goal_ind: int):
        self.g = g
        self.start_ind = start_ind
        self.goal_ind = goal_ind

    def get_num_states(self) -> int:
        return self.g.num_nodes

    def get_start_index(self) -> int:
        return self.start_ind

    def is_goal(self, state: int) -> bool:
        return state == self.goal_ind

    def get_neighbors(self, state: int) -> set:
        return self.g.nodes[state].get_neighbors()

    def get_cost(self, from_state: int, to_state: int) -> float:
        if not self.g.is_edge(from_state, to_state):
            return math.inf
        return self.g.get_edge(from_state, to_state).weight

    def get_heuristic(self, state: int):
        pos1 = self.g.nodes[state].label
        pos2 = self.g.nodes[self.goal_ind].label
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
