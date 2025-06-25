```python
def check_valid(matrix):
    n = len(matrix)
    for i in range(n):
        row_set = set()
        col_set = set()
        for j in range(n):
            row_set.add(matrix[i][j])
            col_set.add(matrix[j][i])
        if len(row_set) != n or max(row_set) != n or min(row_set) != 1:
            return False
        if len(col_set) != n or max(col_set) != n or min(col_set) != 1:
            return False
    return True
```