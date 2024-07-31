import math
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode], bounds: (int, int)) -> bool:
            if not root:
                return True

            if root.val <= bounds[0] or root.val >= bounds[1]:
                return False

            left = dfs(root.left, (bounds[0], root.val))
            right = dfs(root.right, (root.val, bounds[1]))

            return left and right

        return dfs(root, (-math.inf, math.inf))

    def isValidBSTIterative(self, root: Optional[TreeNode]) -> bool:
        stack = []
        if root:
            stack.append((root, (-math.inf, math.inf)))

        while stack:
            node, bounds = stack.pop()

            if node.val <= bounds[0] or node.val >= bounds[1]:
                return False

            if node.left:
                stack.append((node.left, (bounds[0], node.val)))

            if node.right:
                stack.append((node.right, (node.val, bounds[1])))

        return True

    def isValidBSTBFS(self, root: Optional[TreeNode]) -> bool:
        queue = deque()

        if root:
            queue.appendleft((root, (-math.inf, math.inf)))

        while queue:
            node, bounds = queue.pop()

            if node.val <= bounds[0] or node.val >= bounds[1]:
                return False

            if node.left:
                queue.appendleft((node.left, (bounds[0], node.val)))

            if node.right:
                queue.appendleft((node.right, (node.val, bounds[1])))

        return True


# Similar: 1448 Count Good Nodes in Binary Tree
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree. In a BST, the left subtree of every node contains values less than
# the node, and the right subtree contains values greater than the node.
#
# NAIVELY try so solve this by just enforcing the BST check for every node
# and its children, node.left.val < node.val < node.right.val
#
# NOTICE that this returns true for bad inputs. If node.right.left < root.val,
# it will pass -- but everything to the right of root should be greater than
# root.
#
# NOTICE that starting from the root:
# node.left is in the range (-infinity, node.val)
# node.right in (node.val, infinity)
# node.left.left in (-infinity, node.left.val)
# node.left.right in (node.left.val, node.val)
# node.right.left in (node.val, node.right.val)
# node.right.right in (node.right.val, infinity)
#
# IN OTHER WORDS to be a valid BST, every node has to fall between a specific
# set of bounds.
#
# For node.left, the bound is (previous lower bound, node.val)
# For node.right, the bound is (node.val, previous upper bound)
#
# NOTICE we need to perform a tree traversal and STORE STOME STATE from each
# node's parent (the bounds). Then we need to compare the node value to its
# bounds and return False if it falls ourside.
#
# NOTICE that in every possible solution, we bundle the node with the state
# needed to make a True/False return -- we can have 'bounds' as a recursive
# function arg or use an iterative traversal with tuples of (node, bounds).
#
# BECAUSE every node's bounds are set based on its parent, REGARDLESS OF
# THE ORDER WE VISIT THE PARENTS, the traversal order doesn't matter. We
# can use DFS, BFS, iterative or recursive.
