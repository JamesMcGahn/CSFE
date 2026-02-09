def make_node_path_from_last(last: list, dest: int) -> list:
    reverse_path = []
    current: int = dest
    while current != -1:
        reverse_path.append(current)
        current = last[current]

    path: list = list(reversed(reverse_path))
    return path
