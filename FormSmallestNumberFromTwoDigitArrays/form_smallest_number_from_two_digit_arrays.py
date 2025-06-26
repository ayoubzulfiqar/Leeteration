class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        min_common = float('inf')
        
        set2 = set(nums2)
        
        for num in nums1:
            if num in set2:
                min_common = min(min_common, num)
                
        if min_common != float('inf'):
            return min_common
        
        min1 = min(nums1)
        min2 = min(nums2)
        
        return min(min1, min2) * 10 + max(min1, min2)