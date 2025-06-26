class Solution:
    def columnWidths(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        
        ans = [0] * n
        
        for j in range(n):
            max_width_for_current_column = 0
            for i in range(m):
                num = grid[i][j]
                current_length = len(str(num))
                max_width_for_current_column = max(max_width_for_current_column, current_length)
            ans[j] = max_width_for_current_column
            
        return ans