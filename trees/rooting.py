# Australians don't make fun of me pls
# Rooting a tree is assigning a specific node to be the root of a tree
# and making all edges point away from the root

import treedata
import collections


# Note the visited collection isn't needed for tree DFS
# Because the neighbor != parent check ensures the recursion ends
def find_root(graph: dict[int, list]):
    leaves = collections.deque([node for node in graph if len(graph[node]) == 1])
    degree = {node: len(graph[node]) for node in graph}
    count = len(leaves)

    while count < len(graph):
        new_leaves = collections.deque()
        for node in leaves:
            degree[node] = 0
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
        count += len(new_leaves)
        leaves = new_leaves
    return leaves


def create_rooted_tree(node_id, graph: dict[int, list], parent) -> treedata.TreeNode:
    res = treedata.TreeNode(node_id, parent)

    for neighbor in graph[node_id]:
        if neighbor != parent:
            res.children.append(create_rooted_tree(neighbor, graph, node_id))

    return res


def print_rooted_tree(root: treedata.TreeNode):
    print(root.id)
    if not root.children:
        return

    for child in root.children:
        print_rooted_tree(child)


tree = treedata.UnrootedTree()
computed_root = find_root(tree.graph)
print(list(computed_root))
result = create_rooted_tree(0, tree.graph, None)
print_rooted_tree(result)
