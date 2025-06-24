class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total_sum = 0

        for i in range(n):
            # Add element from the primary diagonal
            total_sum += mat[i][i]
            # Add element from the secondary diagonal
            # The column index for secondary diagonal is n - 1 - i
            total_sum += mat[i][n - 1 - i]

        # If the matrix has an odd number of rows/columns,
        # the center element (e.g., mat[1][1] in a 3x3 matrix)
        # is part of both diagonals and has been added twice.
        # We need to subtract it once.
        if n % 2 == 1:
            # The center element is at index n // 2 for both row and column
            total_sum -= mat[n // 2][n // 2]

        return total_sum