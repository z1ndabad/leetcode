# So uh, why graphs and grids?
# Every cell in a grid is connected -- if we think of the cells as nodes,
# adjacent cells have edges between them. Grids are IMPLICIT GRAPHS.
# So graph algorithms apply.
import collections


def constructGrid(rows, columns, rocks: list[tuple], goal: tuple):
    grid = [["." for _ in range(columns)] for _ in range(rows)]
    for x, y in rocks:
        grid[y][x] = "#"

    grid[goal[1]][goal[0]] = "E"
    return grid


def findExit(start, grid: list[list]):
    # Add sr, sc to queue
    # Visit adjacent unvisited neighbors that do not contain rocks

    def grid_bfs(start, grid, directions):
        row_count = len(grid)
        col_count = len(grid[0])
        visited = [[False for _ in range(col_count)] for _ in range(row_count)]
        prev = [row[:] for row in visited]

        move_count = 0
        remaining_nodes_in_layer = 1
        nodes_in_next_layer = 0
        is_end = False
        x_start = start[0]
        y_start = start[1]
        x_queue = collections.deque()
        y_queue = collections.deque()

        x_queue.appendleft(x_start)
        y_queue.appendleft(y_start)

        visited[y_start][x_start] = True
        while x_queue:
            x = x_queue.pop()
            y = y_queue.pop()
            if grid[y][x] == "E":
                is_end = True
                break

            for i in range(len(directions[1])):
                neighbor_x = x + directions[1][i]
                neighbor_y = y + directions[0][i]
                in_bounds = neighbor_x in range(col_count) and neighbor_y in range(
                    row_count
                )

                if (
                    in_bounds
                    and (not visited[neighbor_y][neighbor_x])
                    and (not grid[neighbor_y][neighbor_x] == "#")
                ):
                    x_queue.appendleft(neighbor_x)
                    y_queue.appendleft(neighbor_y)
                    prev[neighbor_y][neighbor_x] = (x, y)
                    visited[neighbor_y][neighbor_x] = True
                    nodes_in_next_layer = nodes_in_next_layer + 1

            remaining_nodes_in_layer -= 1
            if remaining_nodes_in_layer == 0:
                remaining_nodes_in_layer = nodes_in_next_layer
                nodes_in_next_layer = 0
                move_count += 1

        if is_end:
            return move_count, prev
        return -1

    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    return grid_bfs(start, grid, [dy, dx])


rocks = [(0, 4), (1, 1), (1, 2), (2, 3), (2, 4), (3, 0), (3, 3), (5, 1), (5, 4)]
grid = constructGrid(5, 7, rocks, (3, 4))
for line in grid:
    print(line)


def findPath(start, end, grid):
    (_, prev) = findExit(start, grid)
    path = []
    at = end
    while at:
        (x, y) = at
        path.append(at)
        at = prev[y][x]

    if path and path[-1] == start:
        return list(reversed(path))
    return []


print(findPath((0, 0), (3, 4), grid))
