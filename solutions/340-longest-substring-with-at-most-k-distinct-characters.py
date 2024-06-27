class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_freq = {}
        current_substring_length = 0
        res = 0
        window_start = 0

        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
            current_substring_length += 1

            while len(char_freq) > k:
                first_char = s[window_start]
                current_substring_length -= 1
                char_freq[first_char] -= 1
                window_start += 1
                if char_freq[first_char] == 0:
                    del char_freq[first_char]

            if current_substring_length > res:
                res = current_substring_length

        return res


# Sliding window problem -- iterate over the string keeping track of
# char frequency.
#
# While the number of distinct chars exceeds k, shrink the window from
# the left, decrement the frequency of the char at the left index
# and decrement the current substring length. If the frequency of
# the char at the left index hits 0, delete it from the hashmap
#
# If the current substring length exceeds the maximum recorded so far,
# update the maximum
