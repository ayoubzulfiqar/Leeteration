class Solution:
    def modifyMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0])

        answer = [row[:] for row in matrix]

        for j in range(n):
            max_val_in_col_j = float('-inf')
            
            for i in range(m):
                if matrix[i][j] != -1:
                    max_val_in_col_j = max(max_val_in_col_j, matrix[i][j])
            
            for i in range(m):
                if answer[i][j] == -1:
                    answer[i][j] = max_val_in_col_j
        
        return answer