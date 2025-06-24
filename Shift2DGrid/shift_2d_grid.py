class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        total_elements = m * n

        new_grid = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                target_1d_idx = r * n + c
                
                source_1d_idx = (target_1d_idx - k) % total_elements

                source_row = source_1d_idx // n
                source_col = source_1d_idx % n

                new_grid[r][c] = grid[source_row][source_col]

        return new_grid