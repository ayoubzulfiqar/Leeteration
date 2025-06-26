import collections

class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = max(nums)
        
        if len(nums) != n + 1:
            return False
            
        counts = collections.Counter(nums)
        
        for i in range(1, n):
            if counts[i] != 1:
                return False
                
        if counts[n] != 2:
            return False
            
        return True