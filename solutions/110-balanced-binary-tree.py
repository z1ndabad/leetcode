# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        max_difference = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return -1

            nonlocal max_difference
            left = maxDepth(root.left)
            right = maxDepth(root.right)

            max_difference = max(max_difference, abs(left - right))

            return max(left, right) + 1

        if root:
            maxDepth(root)

        if max_difference > 1:
            return False

        return True


# Given the root of a binary tree, return whether the tree is height-balanced.
# i.e. return true if, for every node, the difference in height between the
# left and right subtrees is max 1. Else return false.
#
# DFS the tree, returning the maximum height of the subtree rooted in the
# current node. Each recursion, calulate the difference between the heights
# of the left and right subtree (abs(left_height - right_height)) and record
# the maximum difference seen so far.
#
# If the max distance ever exceeds 1, return False, otherwise True.
