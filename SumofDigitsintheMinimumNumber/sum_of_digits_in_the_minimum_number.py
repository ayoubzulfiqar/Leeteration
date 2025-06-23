class Solution:
    def sumOfDigits(self, nums: list[int]) -> int:
        min_val = min(nums)
        
        digit_sum = 0
        temp_min_val = min_val
        
        # Calculate the sum of digits of the minimum number
        # This loop handles positive numbers. If min_val is 0, digit_sum remains 0.
        while temp_min_val > 0:
            digit_sum += temp_min_val % 10
            temp_min_val //= 10
        
        # According to the common interpretation of this problem (e.g., LeetCode 1085):
        # Return 1 if the sum of the digits is even, otherwise return 0.
        if digit_sum % 2 == 0:
            return 1
        else:
            return 0