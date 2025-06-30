class Solution:
    def minimum_total_operations(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        n = len(nums)
        
        median = nums[(n - 1) // 2]
        
        total_operations = 0
        for num in nums:
            total_operations += abs(num - median)
            
        return total_operations