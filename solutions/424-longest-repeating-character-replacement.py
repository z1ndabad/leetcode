class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = max_freq = 0
        freq = {}
        start = 0

        for end, char in enumerate(s):

            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])

            if end - start + 1 - max_freq > k:
                freq[s[start]] -= 1
                start += 1

            if max_length < end - start + 1:
                max_length = end - start + 1

        return max_length


# Given a string and a number k, give the longest substring containing
# the same repeated character IF you can replace up to k characters
# e.g. "ABCAA", k = 2 --> replace 2 characters  to get AAAAA, return 5
#
# Intuition: for any substring, to get the longest repeating sequence, we
# would find the most frequent char in the substring and replace all other chars,
# until we run out of replacements.
#
# Hence we can keep growing the substring until
# len(substring) - [highest char frequency] > k
#
# Sliding window pattern: track char frequencies in a dict, increment freq
# of the current char each iteration. If end - start - max_char_freq > k,
# shrink window from the left by decrementing `freq[s[start]]` and incrementing
# `start`. Record the current length and update max_length if greater
#
# Optimization: the highest-frequency char each iteration must be either
# the frequency of the current char, or a max freq from a previous iteration
# So max_freq = max(max_freq, freq[char])
