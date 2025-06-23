class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        
        # The smallest possible value the maximum element can take is max_val - k.
        # The largest possible value the minimum element can take is min_val + k.
        
        # To minimize the range (max - min), we want to make the maximum as small as possible
        # and the minimum as large as possible.
        # The new minimum will be at most (min_val + k).
        # The new maximum will be at least (max_val - k).
        
        # The minimum possible difference will be (max_val - k) - (min_val + k).
        # This simplifies to max_val - min_val - 2 * k.
        
        # If this calculated difference is negative, it means we can make all elements
        # fall into a range where the adjusted minimum is greater than or equal to the
        # adjusted maximum. In such cases, the minimum possible score is 0.
        
        potential_min_score = max_val - min_val - 2 * k
        
        return max(0, potential_min_score)