class Solution:
    def maxDiff(self, num: int) -> int:
        s_num = str(num)

        # Calculate max_val
        # To maximize, find the first digit (from left) that is not '9'
        # and replace all occurrences of that digit with '9'.
        # If all digits are '9', the number is already maximal.
        d1_for_max = ''
        for char_digit in s_num:
            if char_digit != '9':
                d1_for_max = char_digit
                break
        
        if d1_for_max == '': # All digits in num are '9'
            max_val_str = s_num
        else:
            max_val_str = s_num.replace(d1_for_max, '9')
        
        max_val = int(max_val_str)

        # Calculate min_val
        # To minimize, find the first digit (from left) that is not '0'
        # and replace all occurrences of that digit with '0'.
        # The constraint 1 <= num means num will always have at least one non-'0' digit,
        # so d1_for_min will always be found.
        d1_for_min = ''
        for char_digit in s_num:
            if char_digit != '0':
                d1_for_min = char_digit
                break
        
        min_val_str = s_num.replace(d1_for_min, '0')
        
        min_val = int(min_val_str)

        return max_val - min_val