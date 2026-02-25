from graph import Graph


def kahns(g: Graph) -> list[int]:
    count: list[int] = [0] * g.num_nodes
    s: list[int] = []
    result: list[int] = []

    for current in g.nodes:
        for edge in current.get_edge_list():
            count[edge.to_node] = count[edge.to_node] + 1
    for current in g.nodes:
        if count[current.index] == 0:
            s.append(current.index)

    while len(s) > 0:
        current_index: int = s.pop()
        result.append(current_index)
        for edge in g.nodes[current_index].get_edge_list():
            count[edge.to_node] = count[edge.to_node] - 1
            if count[edge.to_node] == 0:
                s.append(edge.to_node)
    return result


def check_cycle_kahns(g: Graph) -> bool:
    result: list[int] = kahns(g)
    if len(result) == g.num_nodes:
        return False
    return True
