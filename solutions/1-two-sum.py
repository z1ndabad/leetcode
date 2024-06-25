class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_map:
                return [i, index_map[diff]]
            index_map[num] = i


# Track the index of each number in a hashmap
# Subtract the number from the target to get the second number needed
# Check if the hashmap contains the second number and return if yes
