class Solution:
    def numberOfGoodPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        count = 0
        n = len(nums1)
        m = len(nums2)
        
        for i in range(n):
            for j in range(m):
                divisor = nums2[j] * k
                if nums1[i] % divisor == 0:
                    count += 1
        
        return count