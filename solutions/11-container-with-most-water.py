class Solution:
    def maxArea(self, height: list[int]) -> int:

        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            current_area = (r - l) * min(height[r], height[l])

            if current_area > max_area:
                max_area = current_area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


# Given an array where each index is a horizontal position of a line, and
# each value is the vertical height of that line, return the size of the
# largest possible water-holding container that can be created using
# two lines and the x-axis
#
# Two-pointer solution, pointers to start and end of input.
#
# NOTICE the container area for two indices in the input is:
# (i2 - i1) * min(height[i2], height[i1])
#
# The SHORTER of the two lines and the size of the GAP between them scales
# the area. Start with maximum gap, i.e. pointers to the start and end of the
# input.
#
# There is only a chance of the area growing if the smaller of the two lines
# becomes taller -- i.e. the increase in height may be larger than the
# reduction in area caused by shrinking the gap. So each iteration, move the
# pointer pointing to the shorter line.
#
# Compare the new area with the current max. If moving the pointer did result
# in it pointing to a taller line, which is tall enough to offset the gap, the
# new area will be larger.
