class Solution:
    def minimumSum(self, num: int) -> int:
        s_num = str(num)
        digits = sorted(list(s_num))
        
        num1_str = ""
        num2_str = ""
        
        for i in range(len(digits)):
            if i % 2 == 0:
                num1_str += digits[i]
            else:
                num2_str += digits[i]
                
        num1 = int(num1_str)
        num2 = int(num2_str)
        
        return num1 + num2