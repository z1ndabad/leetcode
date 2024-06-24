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


def findExit(start, end, grid: list[list]):
    # Add sr, sc to queue
    # Visit adjacent unvisited neighbors that do not contain rocks

    def grid_bfs(start, end, grid, directions):

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        prev = [row[:] for row in visited]
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
            if (x, y) == end:
                break

            for i in range(len(directions[1])):
                neighbor_x = x + directions[1][i]
                neighbor_y = y + directions[0][i]
                in_bounds = neighbor_x in range(len(grid[0])) and neighbor_y in range(
                    len(grid)
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

        return prev

    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    return grid_bfs(start, end, grid, [dy, dx])


rocks = [(0, 4), (1, 1), (1, 2), (2, 3), (2, 4), (3, 0), (3, 3), (5, 1), (5, 4)]
grid = constructGrid(5, 7, rocks, (3, 4))
for line in grid:
    print(line)


def findPath(start, end, grid):
    (prev) = findExit(start, end, grid)
    path = []
    at = end
    while at:
        (x, y) = at
        path.append(at)
        at = prev[y][x]

    if path and path[-1] == start:
        return (list(reversed(path)), len(path) - 1)
    return ([], -1)


print(findPath((3, 0), (3, 4), grid))
