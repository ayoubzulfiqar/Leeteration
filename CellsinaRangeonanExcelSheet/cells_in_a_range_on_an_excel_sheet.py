```python
def cellsInRange(s: str) -> list[str]:
    col1 = s[0]
    row1 = int(s[1])
    col2 = s[3]
    row2 = int(s[4])
    
    result = []
    for col in range(ord(col1), ord(col2) + 1):
        for row in range(row1, row2 + 1):
            result.append(chr(col) + str(row))
    
    return result
```