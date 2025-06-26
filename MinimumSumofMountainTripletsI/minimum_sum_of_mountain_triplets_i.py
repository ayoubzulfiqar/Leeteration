class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        n = len(nums)
        min_total_sum = float('inf')

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        current_sum = nums[i] + nums[j] + nums[k]
                        min_total_sum = min(min_total_sum, current_sum)

        if min_total_sum == float('inf'):
            return -1
        else:
            return min_total_sum