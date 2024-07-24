# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Given the roots of two binary trees, return whether they are the same. Two
# trees are the same if they have identical structure and each node in each
# position has the same value.
#
# Note this is NOT the same as the two trees being isomorphic.
#
# NOTICE that when comparing two optional nodes we have 3 scenarios:
# - Both nodes are None -> True
# - One node is None and the other is not None -> False
# - The values of the nodes are not equal -> False
#
# Now we just need to traverse the tree and perform this comparison at every
# node.
#
# We can write a recursive function running a DFS and applying these conditions
# at each node.
#
# NOTICE that a recursive DFS will go to the bottom of a subtree before any
# recursive function calls can return -- i.e. deeper nodes in a subtree will
# always be processed before shallower nodes.
#
# That means that if we return:
# isSameTree(node.left) and isSameTree(node.right)
# if ANY CHILD of node.left and node.right returns False, the function call
# for its parent will return False, the call for the parent of the parent will
# return False, etc.
#
# DFS TRAVERSAL and an AND CONDITION RETURN ensure that a single False result,
# at any child, will 'bubble up' the tree -- it ensures failure on any of the
# above conditions is persistent and affects the OVERALL RESULT. And if the
# overall result is not False, it must be True.
