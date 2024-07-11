class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        if nums[0] <= nums[len(nums) - 1]:
            return nums[0]

        while l <= r:
            mid = l + (r - l) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[0] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1

# Given a sorted array that has been rotated any number of times,
# return the value of the minimum element in the array. Rotation
# means values are shifted n to the right, [0,1,2,3] -> [3,0,1,2]
#
# NOTICE that as long as the array is rotated (i.e. not rotated by
# 0 or its length), all values fall into 2 ordered groups:
#
# 1. Sorted values equal to or greater than arr[0]
# 2. Sorted values less than arr[0]
#
# For any index in the array, we know that if the value >= arr[0],
# the minimum must be to the right, and if the value < arr[0], the
# minimum must be either the current index or left of it. We need
# to find an inflection point where the condition value >= arr[0]
# stops being true.
#
# So this is basically binary search. Return at the first index
# where arr[i] < arr[i - 1]
#
# EDGE CASES:
# - arr[0] will necessarily be greater than arr[-1] for a rotated
#   array, so when comparing values, ensure indices are positive
#
# - If the input is not rotated, it will not have an inflection point
#   where arr[i] < arr[0], because arr[0] is now the minimum value.
#   So check if the first element is less than the last element and
#   return arr[0] if so
