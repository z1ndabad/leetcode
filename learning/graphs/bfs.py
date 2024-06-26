import collections
from graphdata import Graph


# Process nodes in order of distance from the origin.
# This uses a queue under the hood because, for a given current node,
# the node's unvisited neighbors are necessarily further from the origin
# than the current node. So the PREVIOUS node's neighbors all need to
# be processed before the current node's neighbors.
#
# Taking the current node from the head of a queue, and adding
# its neighbors to the start of the queue, enforces this behavior
def bfs_traversal(node: int | str, adjacency_list):
    print("BFS function call")
    visited = [False for _ in adjacency_list]
    prev = [None for _ in adjacency_list]
    queue = collections.deque()
    queue.appendleft(node)

    while queue:
        s = queue.pop()
        visited[s] = True

        for neighbor in adjacency_list[s]:
            if not visited[neighbor]:
                # Ensures neighbors with two paths from the origin are not visited twice
                visited[neighbor] = True
                prev[neighbor] = s
                queue.appendleft(neighbor)

    return prev


# BFS traverses in order of distance, so for a given end/goal node, the node that was
# being processed when the end node was marked visited must be 1 step closer to the origin
def find_shortest_path(
    start: int | str, end: int | str, adjacency_list: dict[int | str, list[int | str]]
) -> list:
    prev = bfs_traversal(start, adjacency_list)
    path = []
    res = []
    at = end
    # 0 is a valid node ID, so loop should terminate when prev[at] = None
    while at is not None:
        path.append(at)
        at = prev[at]

    if path and path[-1] == start:
        res = list(reversed(path))
    return res


graph = Graph().graph
print(find_shortest_path(0, 9, graph))
