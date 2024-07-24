# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            nonlocal max_diameter

            if not root:
                return -1

            left = maxDepth(root.left)
            right = maxDepth(root.right)

            max_diameter = max(res, left + right + 2)

            return max(left, right) + 1

        return max_diameter


# Given the root of a binary tree, return the diameter of the tree. The
# diameter is the length of the longest path between any two nodes in a tree.
# The diameter may or may not pass through the root.
#
# NOTICE that for any given node, the diameter passing through that node is
# the maximum height of the left subtree + max height of the right subtree,
# (where a leaf node has a height of 0), PLUS 2.
#
# WE ADD 2 BECAUSE there are 2 additional edges to traverse on the diameter
# path--the edges between node.left -> node and node-> node.right.
#
# Track the maximum diameter seen so far with a variable (0). Remember to use
# nonlocal in Python so the value can be updated (or use an object).
#
# Write a function to DFS the graph and return the height of the max subtree
# originating at that node (where height of a leaf = 0). Where the current node
# is None, return -1, else return max(maxDepth(left), maxDepth(right)) + 1 to
# offset the -1 base case.
#
# Calculate the diameter of a tree with the current node as its root with
# diameter = maxDepth(left) + maxDepth(right) + 2. If this is greater than
# the max diameter seen so far, update the max diameter.
#
# REMEMBER that the inner maxDepth function must return the maximum depth of
# a tree rooted in the current node, BUT ALSO modifies the max_diameter seen so
# far.
