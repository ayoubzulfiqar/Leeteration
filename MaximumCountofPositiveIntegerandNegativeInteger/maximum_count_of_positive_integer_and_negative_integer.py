import bisect

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        neg_count = bisect.bisect_left(nums, 0)
        pos_count = len(nums) - bisect.bisect_right(nums, 0)
        return max(neg_count, pos_count)