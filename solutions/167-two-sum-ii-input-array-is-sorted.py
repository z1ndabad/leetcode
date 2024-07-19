class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:

            if numbers[l] + numbers[r] > target:
                r -= 1

            if numbers[l] + numbers[r] < target:
                l += 1

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

        return []


# Given a sorted array of integers, find two numbers that add up to target.
# Return their indices in numbers, indexed at 1 (not 0).
# Cannot use the same element twice. Must use constant space.
#
# Remember in Two Sum we needed a dict of each number's difference from target,
# taking O(N) space. How does the sorted input let us avoid that?
#
# Two pointers, one at start and one at end of input
# If the sum of the numbers at each pointer < target, the sum needs to be larger,
# so increment start. If sum > target, the sum needs to be smaller, so
# decrement end. If the sum equals target, return start and end positions.
