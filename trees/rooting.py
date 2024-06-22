# Australians don't make fun of me pls
# Rooting a tree is assigning a specific node to be the root of a tree
# and making all edges point away from the root

import treedata


# Note the visited collection isn't needed for tree DFS
# Because the neighbor != parent check ensures the recursion ends
def create_rooted_tree(
    node_id, unrooted_tree: treedata.UnrootedTree, parent
) -> treedata.TreeNode:
    res = treedata.TreeNode(node_id, parent)

    for neighbor in unrooted_tree.graph[node_id]:
        if neighbor != parent:
            res.children.append(create_rooted_tree(neighbor, unrooted_tree, node_id))

    return res


def print_rooted_tree(root: treedata.TreeNode):
    print(root.id)
    if not root.children:
        return

    for child in root.children:
        print_rooted_tree(child)


tree = treedata.UnrootedTree()
result = create_rooted_tree(0, tree, None)
print_rooted_tree(result)
