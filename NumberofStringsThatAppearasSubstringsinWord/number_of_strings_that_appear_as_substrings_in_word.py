```python
def numOfStrings(patterns, word):
    count = 0
    for pattern in patterns:
        if pattern in word:
            count += 1
    return count
```