class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        row_counts = [0] * m
        col_counts = [0] * n

        for r_idx, c_idx in indices:
            row_counts[r_idx] += 1
            col_counts[c_idx] += 1

        odd_rows = 0
        for count in row_counts:
            if count % 2 == 1:
                odd_rows += 1

        even_rows = m - odd_rows

        odd_cols = 0
        for count in col_counts:
            if count % 2 == 1:
                odd_cols += 1

        even_cols = n - odd_cols

        return odd_rows * even_cols + even_rows * odd_cols