class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max1 = -1
        max2 = -1
        max1_idx = -1

        for i, num in enumerate(nums):
            if num > max1:
                max2 = max1
                max1 = num
                max1_idx = i
            elif num > max2:
                max2 = num
        
        if max1 >= 2 * max2:
            return max1_idx
        else:
            return -1