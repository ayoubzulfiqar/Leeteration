```python
def count_max_squares(rectangles):
    max_len = 0
    for l, w in rectangles:
        max_len = max(max_len, min(l, w))
    count = 0
    for l, w in rectangles:
        if min(l, w) == max_len:
            count += 1
    return count
```