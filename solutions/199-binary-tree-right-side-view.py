from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        queue = deque()
        res = []

        if root:
            queue.appendleft(root)

        while queue:
            node = None
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

            # After the for loop runs, node is always the rightmost node
            # in its level of the tree
            res.append(node.val)

        return res

    def rightSideViewRecursive(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def helper(root: TreeNode, depth: int):
            if root:
                # Only append to res if the tree depth is greater than the
                # depth of the previous rightmost path
                if depth == len(res):
                    res.append(root.val)

                for child in (root.right, root.left):
                    helper(child, depth + 1)

        helper(root, 0)
        return res


# Given the root of a binary tree, imagine yourself standing on the right side
# of it, and return the values of nodes you can see ordered top to bottom.
# e.g., [1,2,3,null,5,null,4] -> [1,3,4]
#
# TLDR: use BFS + level flush technique to find the rightmost node for every
# level of the tree.
#
# OR use height-aware recursive DFS, and only append to the result if the
# current node is deeper in the tree than the length of the last rightmost path
# seen so far (i.e. if height == len(res))
#
# We might naively think to just traverse the rightmost path DFS and save the
# value to the result. BUT this falls apart for most test cases. Consider a
# tree where the right subtree contains a short path on the right, and a longer
# path on the left. We would need to go back up the tree, then back down, and
# start adding values to the result again once the current level exceeds the
# length of the previous rightmost path. I'm too stupid for this.
#
# BFS is easier. NOTICE that if we could separate out the different levels of
# the tree while performing BFS, the rightmost node would be the LAST NODE
# POPPED for a given level.
#
# We can in fact do this -- at the start of the first iteration, len(queue) is
# the length of the first level. Use an inner for loop to pop all nodes up to
# the current length of the queue, while appending children. The for loop will
# run for each node in the level -- so every iteration of the outer while loop
# corresponds to a tree level.
#
# This means the last node popped from the queue by the inner for loop will be
# the rightmost node. Add this node's value to the result.
