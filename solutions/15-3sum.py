class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i == 0 or num != nums[i - 1]:
                l, r = i + 1, len(nums) - 1
                
                while l < r:
                    three_sum = num + nums[l] + nums[r]
                    if three_sum < 0:
                        l += 1

                    elif three_sum > 0:
                        r -= 1

                    else:
                        res.append([num, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
        return res 

# Given an integer array, return all combinations of 3 values that sum to 0
# The 3 values must be at different indices. Return should contain no
# duplicates irrespective of order
# 
# This is an ugly horrible solution that optimally takes O(N^2) time. Oof.
# Intuition: If the input array is sorted, it's easy to block duplicate
# triplets by checking if the current item being iterated over is equal to
# the previous item. i.e. for [-3, -3 ,-1, 0, 1, 2, 3] we can see on the 
# second iteration that nums[1] == nums[0] and skip processing the second -3.
#
# After sorting the input this is an outer loop iterating through the sorted
# input, and an inner loop executing 167 Two Sum II. If the outer iteration 
# item the items at the left and right pointers < 0, increment left. If 
# > 0, decrement right.
#
# Changes from Two Sum II is that after finding a match, we need to avoid
# dupes by moving the pointers again, hence the third nested while loop.
# Incrementing l until nums[l] != nums[l-1] will skip any dupes on the left,
# and then the outer while loop decrements right to skip any repeats there.
#
# Optimization: since the inner Two Sum II already checks the right of the
# input, we can break the outermost for loop when num > 0. Must be > 0, not
# >= 0, because an array of all 0s is a valid input.
#
# Can actually be done in O(NlogN) time with multiple counters for positive
# and negative numbers, but this was too complicated for me. Try again later.

            
