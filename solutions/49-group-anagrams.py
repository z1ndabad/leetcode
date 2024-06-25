class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for str in strs:
            chars = "".join(sorted(str))
            if not chars in res:
                res[chars] = []
            res[chars].append(str)

        return res.values()


# Sorting the characters of two anagrams produces the same string
# Store a hashtable mapping sorted char sequence to a list of strings that sort into it
# Table values are lists of anagrams
