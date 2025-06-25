```python
def maxDistance(colors):
    n = len(colors)
    max_dist = 0
    for i in range(n):
        for j in range(i + 1, n):
            if colors[i] != colors[j]:
                max_dist = max(max_dist, abs(i - j))
    return max_dist
```