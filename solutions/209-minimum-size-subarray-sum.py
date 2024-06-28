import sys


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_length = sys.maxsize
        running_sum = 0
        start = 0

        if sum(nums) < target:
            return 0

        for end, num in enumerate(nums):
            running_sum += num

            while running_sum >= target:
                current_length = end - start + 1

                if min_length > current_length:
                    min_length = current_length

                running_sum -= nums[start]
                start += 1

        return min_length if min_length != sys.maxsize else 0


# Sliding window: return the size of the smallest subarray that sums to
# target or greater
#
# Initialize variables for:
# - Condition being optimized for (min array length),
# - Value that signals when to update the optimal value (current subarray sum)
# - Start of window index (start)
#
# Then iterate over the input (outer for loop)
# Inner loop: while the condition is satisfied (current_sum >= k):
# - Recalculate the return value and compare to the current optimal value
# - Update the optimal value if the new calculated value is better
# - Finally shrink the window -- increment start, update signal value (current_sum)
