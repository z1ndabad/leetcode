class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        index_stack = []
        answer = [0 for _ in temperatures]

        for i, temp in enumerate(temperatures):

            while index_stack and temp > temperatures[index_stack[-1]]:
                colder_day = index_stack.pop()
                answer[colder_day] = i - colder_day

            index_stack.append(i)

        return answer


# Given an array of temperatures where temperatures[i] is the temp on the
# i-th day, return an array res such that res[i] is the number of days,
# after day i, that you have to wait to get a warmer temp. If there is
# no future day, res[i] == 0.
#
# Example input: [23, 22, 24, 21, 19, 22, 27, 25, 24]
# Output: [2, 1, 4, 2, 1, 1, 0, 0, 0]
#
# Read input and solve the problem mentally, left to right.
# If the temperature on a given day i is higher than i-1, then
# res[i-1] == i - (i - 1). Go back another day. If
# temp[i] > temp[i-2], res[i-2] == i - (i-2). Repeat until we reach
# a day where the temp is not lower than temp[i]. Then increment i.
#
# NOTICE that backtracking through the input until we reach a day
# that isn't suitable for the answer resembles building + popping
# a stack.
#
# Use the stack to track the position of each element in the input.
# FOR each element in the input i
#
# WHILE the current temperature is larger than the last element
# of the stack j, pop the last element and set res[j] to i - j,
# the difference between the current day and the last day that
# was lower in temperature.
#
# Append i to the stack
