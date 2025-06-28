import collections

class Solution:
    def splitArray(self, nums: list[int]) -> bool:
        counts = collections.Counter(nums)
        for count in counts.values():
            if count > 2:
                return False
        return True