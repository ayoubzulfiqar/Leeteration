```python
def digit_sum(s: str, k: int) -> str:
    while len(s) > k:
        new_s = ""
        for i in range(0, len(s), k):
            group = s[i:i + k]
            sum_digits = sum(int(digit) for digit in group)
            new_s += str(sum_digits)
        s = new_s
    return s
```