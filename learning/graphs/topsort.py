def top_sort(graph):
    def dfs_topo(at, V, visited_nodes: list, graph):
        V[at] = True

        for neighbor in graph[at]:
            if V[neighbor] == False:
                dfs_topo(neighbor, V, visited_nodes, graph)
        visited_nodes.append(at)

    V = {node: False for node in graph}
    i = len(graph) - 1
    ordering = [0 for _ in graph]

    for node in graph:
        if V[node] == False:
            visited_nodes = []
            dfs_topo(node, V, visited_nodes, graph)
            for id in visited_nodes:
                ordering[i] = id
                i -= 1

    return ordering


graph = {
    "A": ["D"],
    "B": ["D"],
    "C": ["A", "B"],
    "D": ["G", "H"],
    "E": ["A", "D", "F"],
    "F": ["J", "K"],
    "G": ["I"],
    "H": ["I", "J"],
    "I": ["L"],
    "J": ["L", "M"],
    "K": ["J"],
    "L": [],
    "M": [],
}

print(top_sort(graph))
