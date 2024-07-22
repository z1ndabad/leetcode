# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res_digit = dummy
        l1_digit = l1
        l2_digit = l2
        carry_over = 0

        while l1_digit or l2_digit:
            l1_val = l1_digit.val if l1_digit else 0
            l2_val = l2_digit.val if l2_digit else 0

            digit_sum = l1_val + l2_val + carry_over
            carry_over = digit_sum // 10
            res_digit.next = ListNode(digit_sum % 10)
            
            res_digit = res_digit.next

            l1_digit = l1_digit.next if l1_digit else None
            l2_digit = l2_digit.next if l2_digit else None

        if carry_over:
            res_digit.next = ListNode(carry_over)

        return dummy.next


# Given two non-empty linked lists, each representing a non-negative integer 
# with the digits in reverse order, return a list in the same format 
# representing the sum. e.g., [0, 0, 1] + [0, 1, 2] = [0, 1, 3] 
# -- 100 + 210 = 310
#
# This is the same as a written sum:
# - Sum the values of each digit plus any overflow from the previous sum
# - Result % 10 (first digit of the result) is the value of the result digit
# - Result // 10 (overflow above base) is carried over to the next digit sum
# - Repeat for each digit
#
# FINALLY, REMEMBER to check for remaining overflow after the final digit sum
# and add a new node to the result if needed (e.g., 999 + 1 = 1000)
#
# Can handle inputs of different length in different ways:
# 1. while l1 AND l2, then determine which list has digits remaining and
#       continue iterating over it
#
# 2. while l1 OR l2, use conditions inside the loop to account for either l1
#       or l2 running out first (see above)
