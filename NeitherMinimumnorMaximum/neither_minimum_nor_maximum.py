class Solution:
    def findNonMinMax(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return -1
        
        nums.sort()
        return nums[1]