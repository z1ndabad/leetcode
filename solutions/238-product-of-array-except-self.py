class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        left_products_of = [1 for _ in nums]
        right_products_of = [1 for _ in nums]

        for i in range(1, len(nums)):
            left_products_of[i] = left_products_of[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right_products_of[i] = right_products_of[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            res.append(left_products_of[i] * right_products_of[i])

        return res

    def productExceptSelfOptimal(self, nums: list[int]) -> list[int]:
        left_product, right_product = 1, 1
        res = []

        for i in range(len(nums)):
            res.append(left_product)
            left_product *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res


# Given an integer aray, return an answer array such that answer[i]
# is the product of all input elements except input[i].
# Do not use the division operator, solution must be linear time.
#
# For any index i, answer[i] is the product of the entire array divided
# by input[i]. But we can't use the division operator.
#
# Instead notice that multiplying everything and then dividing by
# input[i] is THE SAME AS multiplying everthing item to the left of input[i]
# with everything to the right of input[i].
#
# So we can store two arrays (l, r) where l[i] = product of all numbers to the
# left of i, and r[i] = prod of all numbers to the right of i
#
# Create l by iterating through the array from 1-end, create r by iterating
# backwards from end to 0. Then return the product of both arrays at each
# index
#
# Optimal solution does this in O(1) space, excluding the return value,
# because calculating the l[i] or r[i] does not require two full arrays.
# We only need the value of l[i - 1], then l[i] = l[i-1]*input[i-1]. So
# we store the previous product in a variable.
#
# Notice our return is l[i] * r[i] for all i. That's the same as multiplying
# every element in l[i] by r[i] as we calculate r[i] by iterating backwards
# over nums. So we write the left product to the results array, then
# iterate backwards over the results array and multiply each value by the
# right product.
