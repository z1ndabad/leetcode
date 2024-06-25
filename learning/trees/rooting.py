# Australians don't make fun of me pls
# Rooting a tree is assigning a specific node to be the root of a tree
# and making all edges point away from the root

import treedata
import collections


def find_center(graph: dict[int, list]):
    leaves = [node for node in graph if len(graph[node]) == 1]
    degree = [0 for _ in graph]
    for node in graph:
        degree[node] = len(graph[node])
    count = len(leaves)

    while count < len(graph):
        new_leaves = []
        for node in leaves:
            degree[node] = 0
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
        count += len(new_leaves)
        leaves = new_leaves
    return leaves


# Note the visited collection isn't needed for tree DFS
# Because the neighbor != parent check ensures the recursion ends
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


def encode(node: treedata.TreeNode):
    if node == None:
        return ""

    labels = []

    for child in node.children:
        labels.append(encode(child))

    labels.sort()
    res = "(" + "".join(labels) + ")"
    return res


tree = treedata.UnrootedTree()
computed_root = find_center(tree.graph)
print(list(computed_root))
result = create_rooted_tree(0, tree.graph, None)
print_rooted_tree(result)

tree_to_encode = {0: [1], 1: [0, 2, 4], 2: [1], 4: [1, 3], 3: [4, 5], 5: [3]}
another_tree_to_encode = {0: [1], 1: [0, 2], 2: [1, 4], 4: [2, 3, 5], 3: [4], 5: [4]}

rooted_tree_to_encode = create_rooted_tree(
    find_center(tree_to_encode)[0], tree_to_encode, None
)
rooted_another_tree = create_rooted_tree(
    find_center(another_tree_to_encode)[0], another_tree_to_encode, None
)

print(encode(rooted_tree_to_encode))
print(encode(rooted_another_tree))
