from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = Counter(s1)
        freq_s2 = {}
        total_s2 = 0
        start = 0

        for end, char in enumerate(s2):
            freq_s2[char] = freq_s2.get(char, 0) + 1
            total_s2 += 1

            if freq_s1 == freq_s2:
                return True

            if total_s2 >= len(s1):
                freq_s2[s2[start]] -= 1
                if freq_s2[s2[start]] == 0:
                    del freq_s2[s2[start]]
                    total_s2 -= 1
                start += 1

        return False


# Given two strings s1 and s2, return true if s2 contains a permutation of s1
# i.e. s2 contains a substring that is any reordering of s1
#
# Intuition: two strings are permutations of each other if they have the same
# character frequency
#
# Iterate over s2, adding chars to a frequency map. The map should contain
# freq of all characters in a window the size of s1 -- increment/decrement
# frequencies and delete entries to maintain the s2 freq map
#
# If at any point the frequency maps are equal, s2 contains a window of len(s1)
# with the same char frequency as s1 -- return true
