```python
def checkAlmostEquivalent(word1: str, word2: str) -> bool:
    freq1 = {}
    freq2 = {}
    for char in word1:
        freq1[char] = freq1.get(char, 0) + 1
    for char in word2:
        freq2[char] = freq2.get(char, 0) + 1
    for char in 'abcdefghijklmnopqrstuvwxyz':
        count1 = freq1.get(char, 0)
        count2 = freq2.get(char, 0)
        if abs(count1 - count2) > 3:
            return False
    return True
```