class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = 0
        start = 0
        indices = {}

        for end, char in enumerate(s):
            if char in indices and indices[char] >= start:
                start = indices[char] + 1

            indices[char] = end
            current_length = end - start + 1

            if max_substring < current_length:
                max_substring = current_length

        return max_substring


# Sliding window, return the longest substring without repeating chars
# Store the result being optimized for (max_substring) and a variable/collection
# that we will check to decide when to move the window (indices)
#
# Collection is a dict storing the last index each char appeared at
#
# If the char has appeared within the window already (in dict and index within window),
# move the start index past the last index of the char
#
# Then update the last index of the char to the current position and calculate
# current length, compare to recorded max length
