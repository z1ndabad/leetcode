adjacency_list = {
    0: [1, 9],
    1: [0, 8],
    2: [3],
    3: [2, 4],
    4: [3],
    5: [3, 6],
    6: [5, 7],
    7: [3, 6, 8, 10, 11],
    8: [1, 7],
    9: [0, 8],
    10: [7, 11],
    11: [7, 10],
    12: [],
    13: [14, 15],
    14: [13, 15],
    15: [13, 14, 16],
    16: [15],
}


def iterative_dfs(node: int, adjacency_list: dict[int, list[int]]):
    print("DFS function call")
    visited = {}
    stack = []
    stack.append(node)
    while stack:
        s = stack.pop()
        visited[s] = True

        for neighbor in adjacency_list[s]:
            if not neighbor in visited or not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    return visited


# Don't specify a default arg for visited
# Remember that mutable default args (like lists) are stateful and
# defined at func definition (not at call) -- the visited list would persist between calls
def recursive_dfs(
    node: int,
    adjacency_list: dict[int, list[int]],
    visited: dict[int, bool],
):
    print("DFS FUNCTION CALL")
    if visited[node]:
        return

    visited[node] = True

    for neighbor in adjacency_list[node]:
        recursive_dfs(neighbor, adjacency_list, visited)

    return visited


# Time complexity:
# 1 connected component = 1 DFS call
# DFS iterates only the # vertices and edges in the connected component
# The sum of all calls to DFS should be the number of vertices + edges in the graph overall
# Call to dict.update() is probably too much, adds iterations over the whole graph
# If graph is all islands, iterate N times, call DFS N times, but DFS only iterates once -- O(V)
# If graph is complete (all nodes connect to all nodes), iterate N times, call DFS once, DFS iterates V + E times -- O(V + E)
def find_connected_components(adjacency_list: dict[int, list[int]]):
    visited_overall = {k: False for k in adjacency_list.keys()}
    components = []
    for node in adjacency_list:
        if not visited_overall[node]:
            visited_new = iterative_dfs(node, adjacency_list)
            visited_overall.update(visited_new)
            components.append(visited_new)
    return components


print(find_connected_components(adjacency_list))
