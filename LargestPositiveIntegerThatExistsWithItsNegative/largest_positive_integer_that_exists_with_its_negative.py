class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_k = -1

        for num in num_set:
            if num > 0:
                if -num in num_set:
                    max_k = max(max_k, num)
        
        return max_k