from typing import Any, Union
from .edge import Edge


class Node:
    def __init__(self, index: int, label: Any = None):
        self.index = index
        self.edges: dict[int, Edge] = {}
        self.label = label

    def num_edges(self) -> int:
        return len(self.edges)

    def get_edge(self, neighbor: int) -> Union[Edge, None]:
        if neighbor in self.edges:
            return self.edges[neighbor]
        return None

    def add_edge(self, neighbor: int, weight: float):
        self.edges[neighbor] = Edge(self.index, neighbor, weight)

    def remove_edge(self, neighbor: int) -> None:
        if neighbor in self.edges:
            del self.edges[neighbor]

    def get_edge_list(self) -> list[Edge]:
        return list(self.edges.values())

    def get_sorted_edge_list(self) -> list[Edge]:
        result = []
        neighbors = list(self.edges.keys())
        neighbors.sort()

        for n in neighbors:
            result.append(self.edges[n])
        return result

    def get_neighbors(self) -> set[int]:
        neighbors: set = set()
        for edge in self.edges.values():
            neighbors.add(edge.to_node)
        return neighbors

    def get_out_neighbors(self) -> set[int]:
        neighbors: set = set()
        for edge in self.edges.values():
            neighbors.add(edge.to_node)
        return neighbors
