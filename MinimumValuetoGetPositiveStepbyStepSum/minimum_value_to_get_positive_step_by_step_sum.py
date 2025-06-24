class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        current_sum = 0
        min_sum_so_far = 0

        for num in nums:
            current_sum += num
            min_sum_so_far = min(min_sum_so_far, current_sum)

        required_start_value = 1 - min_sum_so_far
        
        return max(1, required_start_value)