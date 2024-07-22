"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        old_to_copy = {None: None}

        curr = head

        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]


# Given a linked list where each node contains a pointer to the next node, and
# a 'random' pointer that can point to any node in the list or null, return
# a deep copy of the list. None of the nodes in the new list should point to
# the original list.
#
# NOTICE we need a unique way to indentify each node in the list, as different
# nodes could have the same value.
#
# NOTICE that if we can map nodes to their copies, connecting pointers is
# simple -- every node maps to a copy with the same value, and for a given
# node x, x_copy.next = copies[x.next], x_copy.random = copies[x.random]
#
# Iterate the input once, creating a hashmap that maps nodes in the original
# list to new copies. Then iterate a second time, setting pointers in the
# copied list using the hashmap. Return the copy of the input list head.
