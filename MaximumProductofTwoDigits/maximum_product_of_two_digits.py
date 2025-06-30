class Solution:
    def maxProduct(self, n: int) -> int:
        s_n = str(n)
        digits = []
        for char_digit in s_n:
            digits.append(int(char_digit))
        digits.sort()
        return digits[-1] * digits[-2]