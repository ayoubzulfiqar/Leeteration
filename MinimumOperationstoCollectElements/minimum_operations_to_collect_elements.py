class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        collected_elements = set()
        operations_count = 0
        
        for i in range(len(nums) - 1, -1, -1):
            operations_count += 1
            current_num = nums[i]
            
            if 1 <= current_num <= k:
                collected_elements.add(current_num)
            
            if len(collected_elements) == k:
                return operations_count
        
        return operations_count