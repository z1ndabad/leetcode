# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split list into 2 halves -- slow/fast pointer
        l, r = head, head.next

        while r and r.next:
            l = l.next
            r = r.next.next

        # Reverse second half
        prev = None
        second_half = l.next

        # Required -- splits list into two different lists
        l.next = None

        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp
        
        first_half, second_half = head, prev

        while second_half:
            tmp1, tmp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = tmp1

            # Increment both pointers
            first_half, second_half = tmp1, tmp2

# Given a singly-linked list [0 -> 1 -> 2 -> ... -> n-1 -> n],
# reorder it to the form [0 -> n -> 1 -> n-1 -> 2 -> ...]
#
# i.e. [0 -> 1 -> 2 -> 3] becomes [0 -> 3 -> 1 -> 2]
#
# NOTICE that this is the same as interpolating the first half
# of the list with the reverse of the second half. If the list
# is of odd length, the first half should be 1 longer.
#
# Since this is a linked list, we don't know the length. Use
# a slow + fast pointer approach. Set a slow pointer at
# index 0 and fast at index 1 (head and head.next), increment
# the slow by 1 and fast by 2 until reaching the end of the
# list. 
#
# At the end of the loop, fast pointer will be at the end
# of the list, and slow will be at the middle (end of the first
# half).
#
# To get the start of the second half, store slow.next in a new
# variable. Then SET SLOW.NEXT TO NULL to split the lists.
#
# Finally modify the input head in-place using two temp
# variables to store first_half.next and second_half.next.
