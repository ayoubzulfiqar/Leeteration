```python
def find_3_digit_even_numbers(digits):
    from collections import Counter
    count = Counter(digits)
    result = set()
    for i in range(100, 1000, 2):
        s = str(i)
        c = Counter(map(int, s))
        possible = True
        for digit, freq in c.items():
            if count[digit] < freq:
                possible = False
                break
        if possible:
            result.add(i)
    return sorted(list(result))
```