```python
def minRecolors(blocks: str, k: int) -> int:
    n = len(blocks)
    min_ops = float('inf')
    
    for i in range(n - k + 1):
        ops = 0
        for j in range(i, i + k):
            if blocks[j] == 'W':
                ops += 1
        min_ops = min(min_ops, ops)
    
    return min_ops
```