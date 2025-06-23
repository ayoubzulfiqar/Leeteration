class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # The number of 1s in i can be derived from the number of 1s in i // 2.
            # If i is even, i = 2k. Its binary representation is k's binary representation shifted left by one, with a 0 appended.
            # So, count of 1s in i is the same as count of 1s in k (i // 2).
            # If i is odd, i = 2k + 1. Its binary representation is k's binary representation shifted left by one, with a 1 appended.
            # So, count of 1s in i is count of 1s in k (i // 2) plus 1.
            # This can be generalized as: ans[i] = ans[i // 2] + (i % 2)
            # Using bitwise operations for efficiency: i >> 1 is equivalent to i // 2, and i & 1 is equivalent to i % 2.
            ans[i] = ans[i >> 1] + (i & 1)
        return ans