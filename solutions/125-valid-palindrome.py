class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        print(s)
        while i <= j:
            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1

            if i < len(s) and j >= 0:
                if s[i].lower() != s[j].lower():
                    return False
            i += 1
            j -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

# For this problem, algo must ignore spaces and non-alphanumeric characters
# Two-pointer pattern, left pointer at start of string and right pointer at end
# Increment left, decrement right, if left != right then not a palindrome
# Optimization: instead of stripping whitespace before iterating, ignore
# non-alphanumeric characters by moving pointers again if the current character !.isalnum()
