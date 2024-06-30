# Given an input string, return the longest substring length
# Where the substring contains at most k distinct characters


def longest_substring(string, k) -> int:
    char_freq = {}
    current_max = 0
    res = 0
    window_start = 0

    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1
        current_max += 1

        while len(char_freq) > k:
            first_char = string[window_start]
            current_max -= 1
            char_freq[first_char] -= 1
            window_start += 1
            if char_freq[first_char] == 0:
                del char_freq[first_char]

        if current_max > res:
            res = current_max

    return res


print(longest_substring("IBCAAHAH", 2))
