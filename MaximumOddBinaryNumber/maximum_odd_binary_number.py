class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_ones = 0
        for char in s:
            if char == '1':
                count_ones += 1
        
        n = len(s)
        
        # One '1' must be at the end to make the number odd.
        # The remaining (count_ones - 1) '1's should be placed at the beginning
        # to maximize the number.
        # The rest of the positions will be '0's.
        
        result = ['0'] * n
        
        # Place (count_ones - 1) ones at the beginning
        for i in range(count_ones - 1):
            result[i] = '1'
            
        # Place the last '1' at the very end
        result[n - 1] = '1'
        
        return "".join(result)