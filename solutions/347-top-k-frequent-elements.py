from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        hist = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for number, frequency in count.items():
            hist[frequency].append(number)

        res = []
        for i in range(len(hist) - 1, 0, -1):
            for n in hist[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def topKFrequent_no_bucket(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        res = sorted(freq, key=lambda i: freq[i])
        return res[len(res) - k :]

    def topKFrequent_counter(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        return [key for (key, _) in counter.most_common(k)]


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(sol.topKFrequent([1], 1))

print(sol.topKFrequent_no_bucket([1, 1, 1, 2, 2, 3], 2))
print(sol.topKFrequent_counter([1, 1, 1, 2, 2, 3], 2))

# Build a mapping from elements to frequency, sort the mapping by frequency,
# then return the top k keys in the sorted mapping
#
# Optimizations: just use collections.Counter, which is a dict subclass
# for this use case that returns most_common(k)
#
# Or, use bucket sort with a bucket size of 1 -- initialize a 2d list
# where list[frequency] = [list of elements with that frequency], and
# iterate from the end backwards until we cover k elements
# (in practice this was not faster than other methods)
