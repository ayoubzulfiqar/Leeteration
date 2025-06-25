```python
def totalMoney(n: int) -> int:
    weeks = n // 7
    days = n % 7
    total = 0
    for i in range(weeks):
        total += 7 * (i + 1) + 21
    for i in range(days):
        total += weeks + 1 + i
    return total
```