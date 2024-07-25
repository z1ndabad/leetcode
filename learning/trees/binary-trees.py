from treedata import BinaryNode

# Binary trees are trees where each node has at most two children (0-2).
#
# A binary tree can be balanced -- every node has two children where possible
#
# Or unbalanced -- a linked list is the most-unbalanced kind of binary tree,
# because every node has 1 child; there are no branches.
#
# A binary search tree is a binary tree where for every node value,
# node.left < node < node.right -- values can be binary searched intuitively
# because if the target is smaller than the current node we go left, if larger
# we go right, until arriving at the value. And the tree depth is log(N), where
# N is the node count.


def dfs_preorder(root: BinaryNode | None):
    if not root:
        return
    print(root.val)
    dfs_preorder(root.left)
    dfs_preorder(root.right)


def dfs_inorder(root: BinaryNode | None):
    if not root:
        return
    dfs_preorder(root.left)
    print(root.val)
    dfs_preorder(root.right)


def dfs_postorder(root: BinaryNode | None):
    if not root:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.val)


binary_tree = BinaryNode(
    1,
    BinaryNode(2, None, None),
    BinaryNode(3, BinaryNode(4, None, None), BinaryNode(5, None, None)),
)

print("Pre-order traversal: ")
dfs_preorder(binary_tree)

print("In-order traversal: ")
dfs_inorder(binary_tree)

print("Post-order traversal: ")
dfs_postorder(binary_tree)

# There are 3 traversal approaches for binary trees:
# - Preorder: visit a node first, then traverse its left subtree, then
#   traverse its right subtree
#
# - Inorder: traverse left subtree, then visit node, then traverse right
#   subtree
#
# - Postorder: traverse left subtree, then right subtree, then visit node
#
# See above for recursive implementations of each of these.
#
# Common uses are:
# - Expression trees, e.g. for mathematics -- pre-, in- and post-order
#   traversals of the tree yield prefix, infix and postfix expressions.
#   e.g. [+, 2, 1], [2, +, 1], [2, 1, +]
#
# - Inorder: returns a binary search tree in sorted non-increasing order --
#   intuition here is that the left child is always the smallest, then the
#   middle, then the right. For decreasing order, visit right -> root -> left
#   instead
#
# - Preorder: tree copying, visit all nodes in order from the root
#
# - Postorder: tree deletion, delete children before deleting the root


def dfs_preorder_iterative(root: BinaryNode | None):
    stack = []
    if root:
        stack.append(root)

    while stack:

        node = stack.pop()
        print(node.val)

        for child in (node.right, node.left):
            if child:
                stack.append(child)


print("Iterative preorder")
dfs_preorder_iterative(binary_tree)
