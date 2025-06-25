```python
def replace_digits(s: str) -> str:
    """Replaces digits in a string with shifted characters.

    Args:
        s: The input string with lowercase letters at even indices and digits at odd indices.

    Returns:
        The string after replacing all digits with shifted characters.
    """
    result = list(s)
    for i in range(1, len(s), 2):
        result[i] = chr(ord(s[i - 1]) + int(s[i]))
    return "".join(result)
```