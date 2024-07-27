# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        stack = [(root, root.val)]

        while stack:
            node, current_largest = stack.pop()
            
            if node.val >= current_largest:
                good += 1

            for child in (node.right, node.left):
                if child:
                    if node.val > current_largest:
                        stack.append(child, node.val)
                    else:
                        stack.append(child, current_largest)

        return good

    def goodNodesRecursive(self, root: TreeNode) -> int:
        
        def dfs(node, current_largest):
            nonlocal good
            if node.val >= current_largest:
                good += 1
                current_largest = node.val
            
            if node.left:
                dfs(node.left, current_largest)
            if node.right:
                dfs(node.right, current_largest)

        good = 0
        dfs(root, root.val)

        return good

# Given a binary tree root, a node X is good if in the path from the root to X,
# there are no nodes with a value greater than X. The root is always good.
# Return the number of good nodes in the tree.
#
# NOTICE that, traversing the tree from the root, if the current node's value
# is greater than or equal to the largest value seen so far on that path, the
# node is good.
#
# NOTICE that we can track the largest value seen so far on ANY kind of
# traversal, if we start with the root as the max so far, then compare its
# children's values with the root -- if larger, update the max -- and
# so on.
#
# So EACH NODE needs access to either its parent's value or the value of an
# earlier ancestor that was larger. We can STORE THIS STATE by turning the
# traversal collection (stack/queue/recursion stack) into a set of TUPLES.
#
# Instead of [node1, node2, ...], 
# store [(node1, node1.val OR MAXIMUM), (node2, node2.val OR MAXIMUM)]
# 
# If the value of the current node >= max so far, increment count of good
# nodes.
#
# NOTICE that every tuple contains all the information needed to check whether
# the current node is good -- the current maximum value, and the value of the
# node. THE ORDER OF THE TUPLES DOES NOT MATTER. So any traversal of the tree
# will work, BFS/DFS/inorder/preorder/postorder
