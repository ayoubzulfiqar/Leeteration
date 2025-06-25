```python
def solve():
    n = int(input())
    matches = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            matches.append((i, j))
    
    for match in matches:
        print(match[0], match[1])

solve()
```