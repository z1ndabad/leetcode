import sys


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = -sys.maxsize
        current_maximum = 0

        for num in nums:
            if num + current_maximum >= num:
                current_maximum += num

            elif num + current_maximum < num:
                current_maximum = num

            if res < current_maximum:
                res = current_maximum

        return res


# Find maximum subarray -> Kadane's algorithm
# Intuition:
# For a subarray that must end at index n, the maximum sum has to either be:
# 1. The previous maximum sum + arr[n] -- we extend the last maximum subarray to cover n
# 2. arr[n] itself -- adding arr[n] will not increase the previous maximum sum,
#       so we need to start looking at a new subarray starting at n
#
# The variable current_maximum is a proxy for tracking array indices in a
# sliding window. In case 1, the window extends from the right. In case 2,
# the window start skips forward to index n
