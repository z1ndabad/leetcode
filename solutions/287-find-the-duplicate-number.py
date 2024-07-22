class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast, slow = 0, 0

        # Remember, problem constraints mean this is guaranteed to terminate
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break

        # Now the distance between slow and start is the start of the cycle
        start = 0

        while True:
            start = nums[start]
            slow = nums[slow]

            if start == slow:
                break

        return slow


# Heads-up, this is going to suck. Just memorize it.
#
# Given an array of positive integers nums containing EXACTLY 1 repeated value,
# return the duplicate value. Solution must not modify input, and use
# constant extra space. The duplicate value can appear 2 or more times.
#
# CONSTRAINT: The values in the list can be in the range 1-n, where n+1 is the
# length of the list. A list of length 5 can contain values from 1-5, with one
# duplicate value that appears 2 or more times.
#
# Constant space needed, so maps/sets/new arrays are out.
#
# NOTICE that the values in the array MUST be in the range 1-n as part of the
# constraints, where n+1 is the array length.
#
# This means every value in the array is the INDEX of another value. It also
# means the array CANNOT contain the value 0, so no value can reference the
# start of the array.
#
# We can turn the array into a graph by starting from the first value, nums[0],
# and getting the next linked node with nums[nums[0]], nums[nums[nums[0]]], etc
#
#
# e.g. for the input [1, 2, 3, 4, 2]
# nums[0] = 1
# nums[1] = 2
# nums[2] = 3
# nums[3] = 4
# nums[4] = 2
# nums[2] = 3
# nums[3] = 4 ...
#
# Yielding the graph (really a LINKED LIST):
#
# 1 --> 2 --> 3 --> 4
#       ^           |
#       |           |
#       |-----------|
#
# NOTICE that the repeated value from the input (2) is the first node in the
# cycle. We need to find this node.
#
# This means we can use linked list cycle algorithms.
# Floyd's Tortoise & Hare algorithm comes to mind, as it only needs two
# pointers.
#
# REMEMBER that the T&H algorithm works by initializing slow and fast pointers.
# The GUARANTEE is that the slow pointer, incrementing by 1, and the fast
# pointer, incrementing by 2, will each hit the cycle and meet somewhere inside
# it. Because the fast pointer moves 2x as fast, it will complete a full round
# of the cycle before meeting the slow pointer.
#
# THE SECOND piece of information we need is that the slow and fast pointers
# meet at some node X such that the DISTANCE BETWEEN X AND THE CYCLE START
# IS EQUAL TO the distance between the head of the list and the cycle start.
#
# Meaning that if we find where the fast and slow pointers meet, and then
# follow the list from X AND the beginning of the list simultaneously, with
# two slow pointers, the pointers will meet at the start of the cycle.
#
# Whew. My god.
