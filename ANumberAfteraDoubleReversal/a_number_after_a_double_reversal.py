```python
def isSameAfterReversals(num: int) -> bool:
    if num == 0:
        return True
    return num % 10 != 0
```