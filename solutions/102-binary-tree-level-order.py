import math


def levelOrder(root):
    level = 0
    level_start = 0
    res = []

    while level_start < len(root):
        level_contents = []
        level_start = int(math.pow(2, level) - 1)
        level_size = int(math.pow(2, level))

        for i in range(level_start, level_start + level_size):
            if i < len(root) and root[i]:
                level_contents.append(root[i])
        if level_contents:
            res.append(level_contents)

        level += 1

    return res


input = [3, 9, 20, None, None, 15, 7]
print(levelOrder(input))
print(levelOrder([1]))
print(levelOrder([]))

# Outcome: correct for solution cases, but the input was not actually a list on leetcode
# Need to redo for a binary tree object with left and right properties
