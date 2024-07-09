# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = deque()

        if root:
            queue.appendleft(root)
        res = []

        while queue:
            current_level = []
            r = range(len(queue))

            for _ in r: 
                node = queue.pop()
                current_level.append(node.val)
                
                if node.left:
                    queue.appendleft(node.left)

                if node.right:
                    queue.appendleft(node.right)

            res.append(current_level)
        return res

# Given the root of a binary tree (object), return the values
# in the tree as a level-order traversal -- i.e. return
# each layer of the tree as a subarray.
#
# Normal breadth-first traversal will visit all the levels in
# order from the root. But there's no indicator of which level
# the current node belongs to.
#
# NOTICE that if, at the start of the new level, the length of
# the queue is the length of the level. So we can save the
# entire level by popping the queue len(queue) times and saving
# the values in a list. While doing this, we continue appending
# each popped node's children to the queue, so once the for loop
# breaks, the queue will contain all nodes in the NEXT level of
# the tree.
#
# Inner for loop goes over each node in a level.
#
# Outer while loop goes through one level of the tree per iteration.
