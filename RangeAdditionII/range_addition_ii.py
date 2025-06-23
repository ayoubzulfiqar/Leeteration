class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        min_row = m
        min_col = n

        for op in ops:
            ai, bi = op
            min_row = min(min_row, ai)
            min_col = min(min_col, bi)

        return min_row * min_col