class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

# For this problem, algo must ignore spaces and non-alphanumeric characters
# Two-pointer pattern, left pointer at start of string and right pointer at end
#
# Ignore non-alphanumeric characters by moving pointers while the characters at
# start and end ! .isalnum(). Ensure the pointers do not cross while doing this
#
# Once both pointers are at an equivalent alnum character, compare and return
# False if characters are not equal. Move pointers forward/back by 1
# at the end of the loop.
#
# Keep in mind it doesn't matter if l == r at one point within the
# loop (i.e. on the final iteration), because then s[l] must equal s[r].
