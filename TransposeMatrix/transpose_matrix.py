class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0])

        transposed_matrix = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                transposed_matrix[j][i] = matrix[i][j]
        
        return transposed_matrix