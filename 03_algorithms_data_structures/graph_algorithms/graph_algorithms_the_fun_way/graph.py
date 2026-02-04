from typing import Union
from .node import Node
from .edge import Edge


class Graph:
    def __init__(self, num_nodes: int, undirected: bool = False):
        self.num_nodes: int = num_nodes
        self.undirected: bool = undirected
        self.nodes: list[Node] = [Node(j) for j in range(num_nodes)]

    def get_edge(self, from_node: int, to_node: int) -> Union[Edge, Node]:
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError
        return self.nodes[from_node].get_edge(to_node)

    def is_edge(self, from_node: int, to_node: int) -> bool:
        return self.get_edge(from_node, to_node) is not None

    def make_edge_list(self) -> list[Edge]:
        all_edges: list[Edge] = []
        for node in self.nodes:
            for edge in node.edges.values():
                all_edges.append(edge)
        return all_edges

    def insert_edge(self, from_node: int, to_node: int, weight: float) -> None:
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError

        self.nodes[from_node].add_edge(to_node, weight)

    def remove_edge(self, from_node: int, to_node: int, weight: float) -> None:
        if from_node < 0 or from_node >= self.num_nodes:
            raise IndexError
        if to_node < 0 or to_node >= self.num_nodes:
            raise IndexError

        self.nodes[from_node].remove_edge(to_node)
        if self.undirected:
            self.nodes[to_node].remove_edge(from_node)

    def insert_node(self, label=None) -> Node:
        new_node: Node = Node(self.num_nodes, label=label)
        self.nodes.append(new_node)
        self.num_nodes += 1
        return new_node

    def make_copy(self):
        graph_copy: Graph = Graph(self.num_nodes, undirected=self.undirected)
        for node in self.nodes:
            graph_copy.nodes[node.index].label = node.label
            for edge in node.edges.values():
                graph_copy.insert_edge(edge.from_node, edge.to_node, edge.weight)
        return graph_copy
