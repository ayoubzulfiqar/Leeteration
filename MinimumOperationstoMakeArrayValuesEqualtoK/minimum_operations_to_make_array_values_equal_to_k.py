class Solution:
    def minimumOperations(self, nums: list[int], k: int) -> int:
        for num in nums:
            if num < k:
                return -1
        
        distinct_values_gt_k = set()
        for num in nums:
            if num > k:
                distinct_values_gt_k.add(num)
                
        return len(distinct_values_gt_k)