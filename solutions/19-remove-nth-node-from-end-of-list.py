# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        tail = head
        pre_removal_pointer = dummy
        last_index = 0

        while tail.next:
            tail = tail.next
            last_index += 1

            if last_index > n - 1:
                pre_removal_pointer = pre_removal_pointer.next

        pre_removal_pointer.next = pre_removal_pointer.next.next

        return dummy.next


# Given the head of a linked list, remove the nth node from the end of the
# list and return its head.
# e.g. head = [1, 2, 3, 4], n = 1 -> [1, 2, 3]
#
# Use a dummy starting node to handle cases like an empty input, or deleting
# the first item in a list. Return dummy.next
#
# We need to find the end of the list no matter what -- do this with a pointer
# and while loop.
#
# Then we need to remove the node at index [len - n], or [last - (n - 1)].
# That means finding node [len - n - 1] and setting next = next.next, skipping
# the node to be deleted. Intialize a PRE-DELETION POINTER to find this node.
#
# NOTICE that we can traverse the list once, maintaining a constant gap of
# size (n) between the tail pointer and the pre-deletion pointer.
# i.e. if the last index value >= n, we can shift the pre-deletion pointer to
# the right.
#
# At the end of the loop, we have found the tail of the list and the
# pre-deletion pointer points to index [last - (n - 1)]
