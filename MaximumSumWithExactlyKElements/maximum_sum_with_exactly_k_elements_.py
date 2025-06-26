class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        max_val = max(nums)
        total_score = k * max_val + (k * (k - 1)) // 2
        return total_score