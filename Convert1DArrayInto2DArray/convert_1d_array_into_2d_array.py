```python
def construct2DArray(original, m, n):
    if len(original) != m * n:
        return []
    
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(original[i * n + j])
        result.append(row)
    
    return result
```