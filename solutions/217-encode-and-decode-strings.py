class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        lengths = ""
        strings = ""
        for s in strs:
            lengths += str(len(s)) + ","
            strings += s

        return lengths[:-1] + "$" + strings

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res = []
        lengths_string = s.split("$")[0]
        lengths = lengths_string.split(",")
        start = len(lengths_string) + 1

        for l in lengths:
            length = int(l)
            res.append(s[start : start + length])
            start += length

        return res


# Implement Codec where Codec.encode() will be called on one machine to encode
# a list of strings into one string, and Codec.decode() will be called on a
# different machine to decode construct the original list.
#
# Need a way to encode word length information into the original string.
# Easy way is to iterate over the string in encode() and save length
# of each word to a new list. Return length list + a separator + string list.
#
# Then in decode(), retrieve the length list by splitting at the separator,
# iterate through and append the substring s[start:start + length] to results.
# Remember to initialize start = len(lengths + 1) and increment it by length
# each iteration.
#
# Alternatively, can encode length before each word with a separator like
# '4#Word5#Word2'. Then in decode(), while end pointer < len(string), parse
# the length of the next word, increment start until the separator ('#'),
# increment start 1 more time, then set end to start + the parsed length.
# Add string[start:end] to the list and repeat.
