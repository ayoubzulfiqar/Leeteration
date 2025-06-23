import collections

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts1 = collections.Counter(nums1)
        result = []
        
        for num in nums2:
            if counts1[num] > 0:
                result.append(num)
                counts1[num] -= 1
                
        return result