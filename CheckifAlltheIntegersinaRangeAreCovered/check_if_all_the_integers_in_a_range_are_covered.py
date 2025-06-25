```python
def is_covered(ranges, left, right):
    covered = [False] * (right - left + 1)
    for start, end in ranges:
        for i in range(max(left, start), min(right, end) + 1):
            covered[i - left] = True
    return all(covered)
```