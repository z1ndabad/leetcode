from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_height(root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            return max(max_height(root.left), max_height(root.right)) + 1

        return max_height(root) + 1

    def maxDepthIterative(self, root: Optional[TreeNode]) -> int:
        stack = []
        depth = 0

        if root:
            stack.append((1, root))

        while stack:
            current_depth, node = stack.pop()
            depth = max(depth, current_depth)

            if node.left:
                stack.append((current_depth + 1, node.left))

            if node.right:
                stack.append((current_depth + 1, node.right))

        return depth

    def maxDepthBfs(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        depth = 0

        if root:
            queue.appendleft(root)

        while queue:
            depth += 1
            level = len(queue)
            for _ in range(level):
                node = queue.pop()

                if node.left:
                    queue.appendleft(node.left)

                if node.right:
                    queue.appendleft(node.right)

        return depth


# Given the root of a binary tree, return the maximum depth of the tree.
# The depth of the root is 1.
#
# Remember tree depth is the longest path from the root to a leaf node.
#
# We can calculate this with any tree traversal:
#
# DFS recursive -- at a leaf node, return 0. Otherwise return the maximum
# of maxDepth(left) and maxDepth(right) + 1
#
# NOTE: defining a helper method that returns the 0-based max height, instead
# of the 1-based max height, and then returning helper(root) + 1 is a better
# general approach for other problems like 543 Diameter of Binary Tree, and
# 110 Balanced Binary Tree.
#
# DFS iterative -- modify the normal stack to contain a tuple of (depth, node)
# where the depth of the root is 1. A node's children will have a depth of
# current_depth + 1. Each iteration, if the depth of the node popped from the
# stack exceeds the current max depth recorded, set max depth to the current
# depth.
#
# BFS -- taking inspiration from 102. Binary Tree Level Order Traversal,
# at the start of every iteration, the queue contains only nodes in the
# current level of the tree. Use an inner for loop to pop and append children
# len(queue) times, so all nodes from the current level are removed and all
# children (next level) are added.
#
# Then every iteration of the outer while loop corresponds to a level of the
# tree, so depth +=1 every iteration.
