from graph import Graph
from edge import Edge


class DFSTreeStats:
    def __init__(self, num_nodes: int):
        self.parent: list[int] = [-1] * num_nodes
        self.next_order_index: int = 0
        self.order: list[int] = [-1] * num_nodes
        self.lowest: list[int] = [-1] * num_nodes

    def set_order_index(self, node_index: int):
        self.order[node_index] = self.next_order_index
        self.next_order_index += 1
        self.lowest[node_index] = self.order[node_index]


def bridge_finding_dfs(g: Graph, index: int, stats: DFSTreeStats, results: list[Edge]):
    stats.set_order_index(index)

    for edge in g.nodes[index].get_sorted_edge_list():
        neighbor: int = edge.to_node
        if stats.order[neighbor] == -1:
            stats.parent[neighbor] = index
            bridge_finding_dfs(g, neighbor, stats, results)
            stats.lowest[index] = min(stats.lowest[index], stats.lowest[neighbor])

            if stats.lowest[neighbor] >= stats.order[neighbor]:
                results.append(edge)
        elif neighbor != stats.parent[index]:
            stats.lowest[index] = min(stats.lowest[index], stats.order[neighbor])


def find_bridges(g: Graph) -> list[Edge]:
    results: list[Edge] = []
    stats: DFSTreeStats = DFSTreeStats(g.num_nodes)
    for index in range(g.num_nodes):
        if stats.order[index] == -1:
            bridge_finding_dfs(g, index, stats, results)
    return results
