class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for i in range(32):
            lsb = n & 1
            reversed_n = reversed_n << 1
            reversed_n = reversed_n | lsb
            n = n >> 1
        return reversed_n