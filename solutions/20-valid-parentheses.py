class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closing_brackets_map = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in closing_brackets_map:
                top = stack.pop() if stack else None
                if top != closing_brackets_map[char]:
                    return False
            else:
                stack.append(char)

        return not stack


# Given a string containing only parentheses, return true if all parents are
# closed correctly
#
# For every close paren encountered, the last-seen open paren must match it
# Keep a map/helper method to match open and close parens by type.
#
# For every char in the input, if the char is an open paren, add it to the
# stack.
#
# If the char is a closed paren, and it does not match the top of the stack,
# or the stack is empty, there is no matching open and we can return False
# early.
#
# Otherwise return true if the stack is empty by the end.
#
# Note: it might seem smart to return False early if len(s) is odd, and that may
# be true for really long inputs, but for short inputs it works out slower.
