class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        total_sum = 0
        sum_single_digit = 0
        sum_double_digit = 0

        for num in nums:
            total_sum += num
            if 1 <= num <= 9:
                sum_single_digit += num
            elif 10 <= num <= 99:
                sum_double_digit += num
        
        if sum_single_digit > (total_sum - sum_single_digit):
            return True
        
        if sum_double_digit > (total_sum - sum_double_digit):
            return True
            
        return False