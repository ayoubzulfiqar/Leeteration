class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                # Condition 1: grid[i][j] == grid[i + 1][j] (if it exists)
                if i + 1 < m:
                    if grid[i][j] != grid[i + 1][j]:
                        return False

                # Condition 2: grid[i][j] != grid[i][j + 1] (if it exists)
                if j + 1 < n:
                    if grid[i][j] == grid[i][j + 1]:
                        return False
        
        return True