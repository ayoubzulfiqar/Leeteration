```python
def repeatedCharacter(s: str) -> str:
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return ""
```