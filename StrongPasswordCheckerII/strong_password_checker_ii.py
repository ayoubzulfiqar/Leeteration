```python
def strongPasswordCheckerII(password: str) -> bool:
    if len(password) < 8:
        return False
    
    lower = False
    upper = False
    digit = False
    special = False
    
    special_chars = "!@#$%^&*()-+"
    
    for char in password:
        if 'a' <= char <= 'z':
            lower = True
        elif 'A' <= char <= 'Z':
            upper = True
        elif '0' <= char <= '9':
            digit = True
        elif char in special_chars:
            special = True
    
    if not (lower and upper and digit and special):
        return False
    
    for i in range(len(password) - 1):
        if password[i] == password[i+1]:
            return False
    
    return True
```