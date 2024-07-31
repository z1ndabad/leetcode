# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root

        res = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)

            curr = curr.right

        return res

    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode], res):
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        res = []
        dfs(root)
        return res


# See /learning for explanations.
