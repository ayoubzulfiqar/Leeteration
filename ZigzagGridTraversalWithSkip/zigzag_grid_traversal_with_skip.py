class Solution:
    def zigzagTraversalWithSkip(self, grid: list[list[int]]) -> list[int]:
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        result = []
        visited_count = 0

        for r in range(num_rows):
            if r % 2 == 0:  # Even row index: traverse right
                for c in range(num_cols):
                    if visited_count % 2 == 0:
                        result.append(grid[r][c])
                    visited_count += 1
            else:  # Odd row index: traverse left
                for c in range(num_cols - 1, -1, -1):
                    if visited_count % 2 == 0:
                        result.append(grid[r][c])
                    visited_count += 1
        
        return result