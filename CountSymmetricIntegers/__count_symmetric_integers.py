class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            length = len(s)
            
            if length % 2 != 0:
                continue
            
            half_length = length // 2
            
            first_half_sum = 0
            for i in range(half_length):
                first_half_sum += int(s[i])
                
            second_half_sum = 0
            for i in range(half_length, length):
                second_half_sum += int(s[i])
                
            if first_half_sum == second_half_sum:
                count += 1
                
        return count