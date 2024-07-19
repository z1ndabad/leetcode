class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        stack = []

        for token in tokens:
            # Token is a number:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = ops[token](a, b)
                stack.append(result)

        return stack[0]


# Given a reverse Polish notation expression, calculate and return the result.
# All division results must be rounded towards 0 (-3 / 2 == -1)
#
# 'Reverse Polish' is postfix notation: two operands followed by an operator
# like "4 13 5 / +" == 4 + (13 / 5).
#
# i.e. reading from left to right, every time you encounter an operator, apply
# it to the two numbers before it and replace all 3 tokens (numbers + operator)
# with the result. Continue until no more operators.
#
# Think of reading the expression from left to right -- we go right until
# hitting an operator, then go back two tokens and calculate, and the position
# that contained num1, num2, operator is replaced with the result. NOTICE this
# is like popping a stack twice and then pushing the result to the stack.
#
# Remember that numbers are popped off the stack right to left, but operations
# should be applied left to right.
#
# Python-specific:
# - Use a dict with lambda functions to easily parse operators
# - For the division operator, casting floating-point results to int will
#   round towards 0, int(a/b). Otherwise / returns floats and // will round
#   down
