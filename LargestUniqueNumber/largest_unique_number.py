import collections

class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        
        # Sort the unique numbers found in descending order
        # This allows us to return as soon as we find the first number
        # that appears exactly once, as it will be the largest.
        sorted_unique_nums = sorted(counts.keys(), reverse=True)
        
        for num in sorted_unique_nums:
            if counts[num] == 1:
                return num
                
        # If no number appears exactly once, return -1
        return -1