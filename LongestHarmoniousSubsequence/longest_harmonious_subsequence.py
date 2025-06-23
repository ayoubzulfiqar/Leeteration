import collections

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        max_len = 0

        for num in counts:
            if (num + 1) in counts:
                current_len = counts[num] + counts[num + 1]
                if current_len > max_len:
                    max_len = current_len
        
        return max_len