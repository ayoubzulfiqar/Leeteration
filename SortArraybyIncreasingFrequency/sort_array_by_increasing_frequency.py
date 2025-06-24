import collections

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        counts = collections.Counter(nums)
        nums.sort(key=lambda x: (counts[x], -x))
        return nums