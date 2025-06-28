import math

class Solution:
    def shortestSubarrayWithORAtLeastK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_length = math.inf

        for i in range(n):
            current_or = 0
            for j in range(i, n):
                current_or |= nums[j]
                if current_or >= k:
                    length = j - i + 1
                    min_length = min(min_length, length)
                    break 

        if min_length == math.inf:
            return -1
        else:
            return int(min_length)