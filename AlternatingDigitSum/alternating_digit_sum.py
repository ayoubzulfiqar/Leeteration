class Solution:
    def alternatingDigitSum(self, n: int) -> int:
        s = str(n)
        total_sum = 0
        sign = 1  # Start with positive sign for the most significant digit

        for char_digit in s:
            digit = int(char_digit)
            total_sum += digit * sign
            sign *= -1  # Flip the sign for the next digit
            
        return total_sum