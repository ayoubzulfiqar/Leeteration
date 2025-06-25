```python
def canMakeEqual(words):
    if not words:
        return True

    char_counts = {}
    for word in words:
        for char in word:
            char_counts[char] = char_counts.get(char, 0) + 1

    num_words = len(words)
    for count in char_counts.values():
        if count % num_words != 0:
            return False

    return True
```