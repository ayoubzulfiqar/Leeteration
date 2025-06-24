class Solution:
    def specialArray(self, nums: list[int]) -> int:
        n = len(nums)
        
        for x_candidate in range(n + 1):
            count = 0
            for num in nums:
                if num >= x_candidate:
                    count += 1
            
            if count == x_candidate:
                return x_candidate
        
        return -1