class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            grid[i].sort(reverse=True)

        total_answer = 0

        for _ in range(n):
            deleted_values_in_this_step = []
            for row_idx in range(m):
                deleted_value = grid[row_idx].pop(0)
                deleted_values_in_this_step.append(deleted_value)
            
            total_answer += max(deleted_values_in_this_step)
            
        return total_answer