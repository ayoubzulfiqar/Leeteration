class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # The largest power of 3 that fits within a 32-bit signed integer (2^31 - 1 = 2147483647) is 3^19.
        # 3^19 = 1162261467
        # If n is a power of three, it must be a divisor of 3^19.
        # This is because if n = 3^k and k <= 19, then 3^19 = 3^k * 3^(19-k),
        # which means 3^19 is perfectly divisible by 3^k (n).
        return 1162261467 % n == 0