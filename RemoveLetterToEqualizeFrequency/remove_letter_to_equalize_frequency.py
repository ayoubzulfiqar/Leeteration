```python
def equalFrequency(word: str) -> bool:
    from collections import Counter
    counts = Counter(word)
    for char in counts:
        temp_counts = counts.copy()
        temp_counts[char] -= 1
        if temp_counts[char] == 0:
            del temp_counts[char]
        if len(set(temp_counts.values())) <= 1:
            return True
    return False
```