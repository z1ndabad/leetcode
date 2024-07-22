# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        tail = head

        while tail:
            if tail in seen:
                return True
            seen.add(tail)
            tail = tail.next

        return False

    def hasCycleOptimal(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False


# Given a linked list, return true if the list contains a cycle, in which the
# tail of the list links back to a previous node in the list. Otherwise return
# false.
#
# Need a way to track nodes seen while traversing the list -- use a hashset.
#
# Iterate through the list, adding each node to a set. If a node already exists
# in the set, there is a cycle -- return True inside the loop. Otherwise the
# iteration will end and we can return False.
#
# Optimal solution is the 'Tortoise & Hare' algorithm (Floyd).
# NOTICE that if the list contains cycles, a slow pointer shifting by 1 each
# iteration and a fast pointer shifting by 2 MUST meet -- the distance between
# them will increase by 1 until the midpoint, then decrease by 1, so the two
# pointers meet in linear time.
#
# HENCE because FAST AND SLOW POINTERS MUST MEET IF THERE IS A CYCLE, return
# True if the pointers meet -- otherwise the loop will terminate and we can
# return False.
