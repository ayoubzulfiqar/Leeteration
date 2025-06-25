```python
def checkString(s):
    b_found = False
    for char in s:
        if char == 'b':
            b_found = True
        elif b_found and char == 'a':
            return False
    return True
```