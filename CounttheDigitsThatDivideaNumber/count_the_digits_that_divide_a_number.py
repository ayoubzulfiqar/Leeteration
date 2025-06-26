class Solution:
    def countDigits(self, num: int) -> int:
        original_num = num
        count = 0
        
        while num > 0:
            digit = num % 10
            # According to constraints, num does not contain 0 as one of its digits,
            # so digit will never be 0 here.
            # If constraints allowed 0, an 'if digit != 0:' check would be necessary.
            
            if original_num % digit == 0:
                count += 1
            
            num //= 10
            
        return count