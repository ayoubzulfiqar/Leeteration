class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if 2 * left_sum == total_sum - num:
                return i
            left_sum += num
        return -1