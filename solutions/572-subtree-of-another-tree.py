class Solution:
    def isSubtreeNaive(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            
            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return False

# Given a tree (root) and a possible subtree(subroot), return whether subroot
# is a subtree of root.
#
# Similar to: 100 Same Tree.
#
# NOTICE that if subroot is a subtree of root, root must contain a subtree that
# is identical to subroot. i.e. for some node in the root tree,
# isSameTree(node, subroot) must be true.
