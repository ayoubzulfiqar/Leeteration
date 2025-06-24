class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor_sum = 0
        for i in range(n):
            num = start + 2 * i
            xor_sum ^= num
        return xor_sum