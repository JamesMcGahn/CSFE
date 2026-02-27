import random
from typing import Union
from graph import Graph
from edge import Edge
from union_find import UnionFind


def kruskals(g: Graph) -> Union[list, None]:
    djs: UnionFind = UnionFind(g.num_nodes)
    all_edges: list[Edge] = []
    mst_edges: list[Edge] = []

    for idx in range(g.num_nodes):
        for edge in g.nodes[idx].get_edge_list():
            if edge.to_node > edge.from_node:
                all_edges.append(edge)
    all_edges.sort(key=lambda edge: edge.weight)

    for edge in all_edges:
        if djs.are_disjoint(edge.to_node, edge.from_node):
            mst_edges.append(edge)
            djs.union_sets(edge.to_node, edge.from_node)

    if djs.num_disjoint_sets == 1:
        return mst_edges
    else:
        return None


def randomized_kruskals(g: Graph) -> Union[list, None]:
    """
    Given a n * n connected undirected maze graph returns a random path through maze
    """
    djs: UnionFind = UnionFind(g.num_nodes)
    all_edges: list[Edge] = []
    maze_edges: list[Edge] = []

    for idx in range(g.num_nodes):
        for edge in g.nodes[idx].get_edge_list():
            if edge.to_node > edge.from_node:
                all_edges.append(edge)

    while djs.num_disjoint_sets > 1:
        num_edges: int = len(all_edges)
        edge_ind: int = random.randint(0, num_edges - 1)
        new_edge: Edge = all_edges.pop(edge_ind)

        if djs.are_disjoint(new_edge.to_node, new_edge.from_node):
            maze_edges.append(new_edge)
            djs.union_sets(new_edge.to_node, new_edge.from_node)
    return maze_edges
