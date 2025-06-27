class Solution:
    def checkBitwiseOrHasTrailingZeros(self, nums: list[int]) -> bool:
        even_count = 0
        for num in nums:
            if num % 2 == 0:
                even_count += 1
        
        return even_count >= 2