```python
def greatestLetter(s: str) -> str:
    letters = set(s)
    greatest = ""
    for char_code in range(ord('Z'), ord('A') - 1, -1):
        char = chr(char_code)
        if char in letters and char.lower() in letters:
            greatest = char
            break
    return greatest
```