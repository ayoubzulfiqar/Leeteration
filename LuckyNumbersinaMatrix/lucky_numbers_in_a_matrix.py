class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])

        row_mins = [float('inf')] * m
        col_maxs = [float('-inf')] * n

        for r in range(m):
            row_mins[r] = min(matrix[r])

        for c in range(n):
            for r in range(m):
                col_maxs[c] = max(col_maxs[c], matrix[r][c])
        
        lucky_numbers = []
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == row_mins[r] and matrix[r][c] == col_maxs[c]:
                    lucky_numbers.append(matrix[r][c])
                    
        return lucky_numbers