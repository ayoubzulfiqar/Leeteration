class Solution:
    def findTheChild(self, n: int, k: int) -> int:
        cycle_length = 2 * (n - 1)
        effective_k = k % cycle_length

        if effective_k < n - 1:
            return effective_k
        else:
            return cycle_length - effective_k