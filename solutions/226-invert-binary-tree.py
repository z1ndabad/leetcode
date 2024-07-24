# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            tmp = node.left
            node.left = node.right
            node.right = tmp

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return root

    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.right
        root.right = self.invertTreeRecursive(root.left)
        root.left = self.invertTreeRecursive(tmp)

        return root


# Given the root of a binary tree, invert the tree and return the root.
# e.g. [2, 1, 3] --> [2, 3, 1]
#
# For every node, we need to swap the positions of its children, i.e.
# node.left, node.right = node.right, node.left
#
# Can do this with any kind of graph traversal -- BFS, iterative DFS, recursive
# DFS. See above for DFS examples.
