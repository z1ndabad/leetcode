from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        visited = []

        def dfs(root: Optional[TreeNode]):
            if root.left:
                dfs(root.left)

            visited.append(root.val)

            if root.right:
                dfs(root.right)

        dfs(root)
        return visited[k - 1]

    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        # Standard iterative in-order DFS algo
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            # New code for this solution
            k -= 1

            if not k:
                break
            # End new code

            current = current.right

        return current.val


# Given the root of a binary tree, return the k-th smallest value
# (1-indexed) of all the values in the tree.
#
# NOTICE that the smallest value of the tree its leftmost node.
# NOTICE that the input is a BST, so for any node with a right sibling and
# parent, node < parent < right < parent.parent
#
# NOTICE that this resembles an in-order traversal of a BST, and REMEMBER
# that an in-order traversal of a BST returns elements in non-decreasing
# order anyway.
#
# So we need to perform an in-order traversal up to k nodes visited. The
# last node visited is the k-th smallest.
#
# OPTIMALLY we should only perform the in-order traversal up to k nodes
# visited, so we need to break out of the traversal after processing k
# nodes. So an ITERATIVE IN ORDER TRAVERSAL is optimal.
#
# Refer to the normal iterative in-order algo. When visiting a node
# (popping from the stack), decrement k. When k == 0, we have found the
# k-th smallest element.
