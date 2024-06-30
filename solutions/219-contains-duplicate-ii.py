class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        indices = {}
        for end, num in enumerate(nums):
            if num in indices and end - indices[num] <= k:
                return True

            indices[num] = end

        return False


# Hashmap problem
# Return True if the input array contains duplicate numbers within k hops of each other
# Track the last index each number appeared at in a map
# Iterate through the input
# If the current number already exists in the map,
# and the last index it appeared at is <= k, return true
