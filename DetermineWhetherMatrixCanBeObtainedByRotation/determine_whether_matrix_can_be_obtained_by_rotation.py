```python
def findRotation(mat, target):
    def rotate(matrix):
        n = len(matrix)
        new_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[j][n - 1 - i] = matrix[i][j]
        return new_matrix

    def are_equal(matrix1, matrix2):
        n = len(matrix1)
        for i in range(n):
            for j in range(n):
                if matrix1[i][j] != matrix2[i][j]:
                    return False
        return True

    if are_equal(mat, target):
        return True

    rotated_mat = rotate(mat)
    if are_equal(rotated_mat, target):
        return True

    rotated_mat = rotate(rotated_mat)
    if are_equal(rotated_mat, target):
        return True

    rotated_mat = rotate(rotated_mat)
    if are_equal(rotated_mat, target):
        return True

    return False
```