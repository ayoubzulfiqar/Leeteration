class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0
        
        row = 0
        col = n - 1

        while row < m and col >= 0:
            if grid[row][col] < 0:
                count += (m - row)
                col -= 1
            else:
                row += 1
        
        return count