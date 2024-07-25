# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestorIterative(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            if node.left and p.val < node.val and q.val < node.val:
                stack.append(node.left)
            elif node.right and p.val > node.val and q.val > node.val:
                stack.append(node.right)
            else:
                return node

    def bothLeft(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        return p.val < root.val and q.val < root.val

    def bothRight(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        return p.val > root.val and q.val > root.val

    def lowestCommonAncestorRecursive(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root.left and self.bothLeft(root, p, q):
            return self.lowestCommonAncestorRecursive(root.left, p, q)

        if root.right and self.bothRight(root, p, q):
            return self.lowestCommonAncestorRecursive(root.right, p, q)

        return root


# Given a binary search tree, find the lowest common ancestor (LCA) of two
# given nodes. LCA(p,q) returns the lowest node that has both P and Q as
# descendants. Assume a node can be a descendant of itself, and all values in
# the tree are unique.
#
# NOTICE that we're working with a binary search tree, i.e. for every node,
# node.left < node < node.right
#
# NOTICE that for any node, if p and q belong to the same subtree, the LCA must
# be in the direction of the root of the subtree, and not the root or its other
# subtree. i.e. if p and q are both in node.left, then the LCA must be
# node.left or its desendants -- NOT node or node.right.
#
# NOTICE that if p and q belong to different subtrees of a node, THAT NODE must
# be the LCA.
#
# THEREFORE we're looking for the lowest node where p and q are either the
# node itself, OR in different subtrees.
#
# From a node, we know if p and q are in different subtrees based on their
# values. If p < node, it is in node.left. If p > node, it is in node.right.
#
# DFS the tree, appending nodes to the stack if both p and q are on the same
# side of the current node (either left or right).

# As soon as the two nodes are no longer on the same side of the current node
# (incl. when either p or q is the current node and the other node is its
# descendant), return the current node.
#
# See above for both iterative and recursive implementations.
