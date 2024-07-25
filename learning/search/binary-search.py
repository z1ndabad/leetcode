def bisect(arr: list, target, lo=0, hi=None) -> int:
    hi = hi if hi is not None else len(arr)
    assert 0 <= lo <= hi <= len(arr)

    while lo < hi:
        # Not necessary in python but prevents int overflows
        # in other languages -- equivalent to (lo + hi) // 2
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    
    return lo # lo and hi are equal at this point

print(bisect([2,3,4,5,6,7,8,9], 7))
print(bisect([2,3,5,4,6,7,9,8], 7))

# This is equivalent to bisect_left from the bisect lib. It finds
# the index where target would be placed in a sorted input, assuming
# we want it placed before all other instances of target.
#
# To get bisect_right, index is the last position of target, change
# condition to if arr[mid] <= target.
#
# The typical question motivating search algo is "How do I find a
# specific collection element?
#
# This leaves many edge cases open -- what do when the element isn't present?
# What do when duplicates?
#
# Better way to phrase the question: If I were inserting an element with
# value foo into this sorted collection, and I wanted it to be the first foo
# you encounter, where should I put it?
# 
# Inputs don't have to be sorted, strictly speaking. The invariant
# is:
#
# For every subarray halving the input, values < the target should
# be on its left, and values > target should be on its right
#
# i.e. [2, 3, 4, 5, 6, 7, 8, 9] is the same as [2, 3, 5, 4, 6, 7, 9, 8]
# PROVIDED I am trying to find 6 or 7
