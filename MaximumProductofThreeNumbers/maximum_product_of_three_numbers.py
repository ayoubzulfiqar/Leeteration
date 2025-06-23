class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # The maximum product can be either:
        # 1. The product of the three largest numbers (if all are positive or if there are an odd number of negatives among the largest)
        # 2. The product of the two smallest (most negative) numbers and the largest number (if the two negatives multiply to a large positive)
        
        # Product of the three largest numbers
        prod1 = nums[n-1] * nums[n-2] * nums[n-3]
        
        # Product of the two smallest numbers and the largest number
        prod2 = nums[0] * nums[1] * nums[n-1]
        
        return max(prod1, prod2)