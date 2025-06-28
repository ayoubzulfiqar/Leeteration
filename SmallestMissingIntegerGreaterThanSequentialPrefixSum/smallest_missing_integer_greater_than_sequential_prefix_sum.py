class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)

        max_len = 1
        current_len = 1
        
        longest_prefix_sum = nums[0] 
        current_prefix_sum = nums[0]

        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                current_len += 1
                current_prefix_sum += nums[i]
            else:
                current_len = 1
                current_prefix_sum = nums[i]
            
            if current_len > max_len:
                max_len = current_len
                longest_prefix_sum = current_prefix_sum
        
        nums_set = set(nums)
        
        x = longest_prefix_sum
        while x in nums_set:
            x += 1
            
        return x