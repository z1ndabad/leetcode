class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return not len(set(nums)) == len(nums)


# Sets (hashsets) cannot contain duplicates
# If the length of the set is equal to the length of the input, the input
# must contain only unique values
