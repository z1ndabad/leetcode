import collections
import dfs

graph = dfs.adjacency_list


def bfs_traversal(node: int | str, adjacency_list):
    print("BFS function call")
    visited = [False] * len(adjacency_list)
    prev = [None] * len(adjacency_list)
    queue = collections.deque()
    queue.appendleft(node)

    while queue:
        s = queue.pop()
        visited[s] = True

        for neighbor in adjacency_list[s]:
            if not visited[neighbor]:
                visited[neighbor] = True
                prev[neighbor] = s
                queue.appendleft(neighbor)

    return prev


def find_shortest_path(
    start: int | str, end: int | str, adjacency_list: dict[int | str, list[int | str]]
) -> list:
    prev = bfs_traversal(start, adjacency_list)
    path = []
    res = []
    at = end
    while at:
        path.append(at)
        at = prev[at]

    if path and path[-1] == start:
        res = list(reversed(path))
    return res


print(find_shortest_path(13, 16, graph))
