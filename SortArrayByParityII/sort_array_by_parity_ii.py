class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        i = 0
        j = 1

        while i < n and j < n:
            while i < n and nums[i] % 2 == 0:
                i += 2
            
            while j < n and nums[j] % 2 == 1:
                j += 2
            
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        
        return nums