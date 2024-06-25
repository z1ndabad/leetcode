class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_char_count, t_char_count = {}, {}

        for i in range(len(s)):
            s_char_count[s[i]] = s_char_count.get(s[i], 0) + 1
            t_char_count[t[i]] = t_char_count.get(t[i], 0) + 1

        return s_char_count == t_char_count


# Dicts count the frequency of each character in each string
# Using dict.get() instead of subscript initializes dict[i] to 0 if the
# key does not exist
