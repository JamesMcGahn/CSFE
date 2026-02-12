from graph import Graph
from breadth_first_search import breadth_first_search


def make_grid_graph(width: int, height: int) -> Graph:
    num_nodes: int = width * height
    g: Graph = Graph(num_nodes=num_nodes, undirected=True)
    for r in range(height):
        for c in range(width):
            index: int = r * width + c

            if c < width - 1:
                g.insert_edge(index, index + 1, 1.0)
            if r < height - 1:
                g.insert_edge(index, index + width, 1.0)
    return g


print(make_grid_graph(4, 4).get_edge(0, 4))


def make_grid_with_obstacles(
    width: int, height: int, obstacles: set[tuple[int, int]]
) -> Graph:
    num_nodes: int = width * height
    g: Graph = Graph(num_nodes=num_nodes, undirected=True)
    for r in range(height):
        for c in range(width):
            if (r, c) not in obstacles:
                index: int = r * width + c

                if c < width - 1 and (r, c + 1) not in obstacles:
                    g.insert_edge(index, index + 1, 1.0)
                if r < height - 1 and (r + 1, c) not in obstacles:
                    g.insert_edge(index, index + width, 1.0)
    return g


grid = make_grid_with_obstacles(5, 3, {(0, 1), (0, 4), (1, 2)})
print(grid.get_edge(0, 1))
print(grid.get_edge(5, 4))
print(grid.get_edge(1, 7))

print(breadth_first_search(grid, 0))

# Row 0:   0    X    2    3    X
# Row 1:   5    6    X    8    9
# Row 2:  10   11   12   13   14

# [-1, -1, -1, -1, -1, 0, 5, -1, -1, -1, 5, 6, 11, 12, 13]
# -1, -1, -1, -1, -1
#   0, 5, -1, -1, -1,
#   5, 6, 11, 12, 13

print(breadth_first_search(grid, 2))
# [-1, -1, -1, 2, -1,
#  -1, -1, -1, 3, 8,
#  -1, -1, -1, 8, 9]
